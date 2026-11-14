"""Vision-model helpers (OpenAI, image input) with a disk cache under advanced/cache/.

describe_figure(): crop of one figure region -> structured JSON description used for indexing.
annex_headers():   header strip of an annex table page -> ordered column labels.
Model outputs are cached as JSON so re-runs cost nothing; they are NOT trusted blindly: annex
labels are checked against the deterministic column count, and figure descriptions are spot-checked
by hand against the page image (see advanced/README.md).
"""
from __future__ import annotations

import base64
import json
import sys
import time
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.common import setting  # noqa: E402

CACHE = ROOT / "advanced" / "cache"
VISION_MODEL = "gpt-4.1-mini"
PRICE_IN, PRICE_OUT = 0.40, 1.60  # USD / 1M tokens (gpt-4.1-mini list price)
USAGE = {"calls": 0, "input": 0, "output": 0, "cached_hits": 0}

FIGURE_PROMPT = """You are indexing a figure from the WHO report "World health statistics 2023".
Figure: {figure} — {title}
Text labels extracted from the PDF inside this figure region (may be jumbled): {labels}

Describe ONLY what is visible in the image. Return JSON with keys:
"kind": one of bar_chart, line_chart, stacked_bar_chart, scatter_chart, pie_or_donut_chart, map, diagram, timeline, table, mixed;
"axes_units": text describing axes, units and scales (empty if none);
"legend": list of legend entries / series / map categories with their colours;
"values": list of strings "series | category/x : value", one per readable data point. Use the exact printed number when
          a data label is shown; if you must estimate from the axis, prefix with "~". For maps, list the legend classes and
          any countries/regions that are explicitly labelled; do not guess colours of unlabelled countries;
"summary": 2-4 sentences on what the figure shows (main comparison, trend, highest/lowest), only from the image;
"text_in_image": important words/numbers written inside the graphic (titles of boxes, steps, milestones)."""

HEADER_PROMPT = """This is the header of a WHO Annex 1 table page (World health statistics 2023), page {page}.
The data rows below it have exactly {k} value columns (left to right), excluding the country-name column{note}.
Header words extracted from the PDF: {words}
Return JSON {{"columns": [ ... exactly {k} strings ... ]}}, one per value column left to right. Each string must combine,
from top to bottom, the SDG number (if any), the indicator name with units, the data type (e.g. Comparable estimates /
Primary data) and the sex or sub-group, and the year(s), e.g. "3.2 | Under-five mortality rate (per 1000 live births) |
Comparable estimates | 2021". Drop footnote letters. Use only the header text visible in the image."""


def _client():
    import openai

    setting("OPENAI_API_KEY")
    return openai.OpenAI(max_retries=3, timeout=180)


def render_clip(pdf: Path, page: int, bbox: list[float] | None, dpi: int = 200) -> bytes:
    doc = pymupdf.open(pdf)
    p = doc[page - 1]
    clip = pymupdf.Rect(bbox) if bbox else None
    return p.get_pixmap(dpi=dpi, clip=clip).tobytes("png")


def _ask(prompt: str, png: bytes, cache_file: Path) -> dict:
    if cache_file.exists():
        USAGE["cached_hits"] += 1
        return json.loads(cache_file.read_text(encoding="utf-8"))
    client = _client()
    t0 = time.perf_counter()
    resp = client.chat.completions.create(
        model=VISION_MODEL, temperature=0, response_format={"type": "json_object"},
        messages=[{"role": "user", "content": [
            {"type": "text", "text": prompt},
            {"type": "image_url", "image_url": {"url": "data:image/png;base64," + base64.b64encode(png).decode(),
                                                "detail": "high"}}]}])
    out = json.loads(resp.choices[0].message.content)
    u = resp.usage
    USAGE["calls"] += 1
    USAGE["input"] += u.prompt_tokens
    USAGE["output"] += u.completion_tokens
    out["_meta"] = {"model": VISION_MODEL, "seconds": round(time.perf_counter() - t0, 2),
                    "input_tokens": u.prompt_tokens, "output_tokens": u.completion_tokens}
    cache_file.parent.mkdir(parents=True, exist_ok=True)
    cache_file.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    return out


def describe_figure(pdf: Path, page: int, fig: dict) -> dict:
    png = render_clip(pdf, page, fig["bbox"])
    prompt = FIGURE_PROMPT.format(figure=fig["figure"], title=fig["title"], labels=fig["embedded_text"][:2500])
    key = f"p{page:03d}_{fig['figure'].replace(' ', '_')}"
    return _ask(prompt, png, CACHE / "figures" / f"{key}.json")


def annex_headers(pdf: Path, page: int, header_bbox: list[float], k: int, words: str, note: str = "") -> dict:
    png = render_clip(pdf, page, header_bbox, dpi=220)
    prompt = HEADER_PROMPT.format(page=page, k=k, words=words[:2500], note=note)
    return _ask(prompt, png, CACHE / "annex_headers" / f"p{page:03d}.json")


def cost_usd() -> float:
    return round((USAGE["input"] * PRICE_IN + USAGE["output"] * PRICE_OUT) / 1e6, 4)
