"""Body pages of WHO World health statistics 2023: text chunks and figure regions.

- Running headers/footers and page numbers are dropped.
- A figure region starts at its caption ("Figure 1.1 ...", caption sits ABOVE the graphic) and ends
  at the next "Source:" line below it (WHO style), or at the next caption / page bottom.
- Text blocks inside a figure region (axis labels, legend, data labels) belong to the figure, not
  to the body text. Region bbox (PDF points) is kept so the crop can be regenerated and checked.
Printed page number = PDF page - 10 for pages 11-128.
"""
from __future__ import annotations

import re
from typing import Any

import pymupdf

SOURCE_ID = "who-whs-2023"
SOURCE = "WHO, World health statistics 2023: monitoring health for the SDGs (ISBN 978-92-4-007432-3)"
CAPTION_RE = re.compile(r"^(Figure|Fig\.)\s*(\d+\.\d+)\s+(.*)", re.S)
NOISE = re.compile(r"^(World health statistics 2023\s*–\s*Monitoring health for the SDGs|"
                   r"Key issues and trends in global health|Summary status of the health-related SDGs.*|"
                   r"Building on past achievements.*|Annex 1\. Country, area, WHO region and global health statistics|"
                   r"Part\s*\d|\d{1,3})$")


def printed_page(pno: int) -> int | None:
    return pno - 10 if 11 <= pno <= 128 else None


def clean(text: str) -> str:
    text = text.replace("­", "").replace("​", "")
    text = re.sub(r"-\n(?=[a-z])", "", text)          # hyphenated line breaks
    return re.sub(r"\s*\n\s*", " ", text).strip()


def figure_regions(page: pymupdf.Page) -> list[dict[str, Any]]:
    blocks = [b for b in page.get_text("blocks") if b[6] == 0]
    caps = []
    for b in blocks:
        m = CAPTION_RE.match(b[4].strip())
        # a real caption starts its block; in-text references ("Figure 1.2 shows ...") are lower-case verbs
        if m and not re.match(r"^(shows|presents|illustrates|depicts)\b", m.group(3)):
            caps.append((b, m))
    caps.sort(key=lambda c: c[0][1])
    regions = []
    for i, (b, m) in enumerate(caps):
        y_next = caps[i + 1][0][1] - 1 if i + 1 < len(caps) else page.rect.height - 40
        src = [s for s in blocks if b[1] < s[1] < y_next + 1 and s[4].strip().startswith("Source")]
        y_end = max(s[3] for s in src) if src else y_next
        rect = pymupdf.Rect(40, b[1] - 2, page.rect.width - 30, y_end + 2)
        regions.append({"figure": f"Figure {m.group(2)}", "title": clean(m.group(3)), "bbox": [round(v, 1) for v in rect],
                        "rect": rect})
    return regions


def page_text_and_figures(page: pymupdf.Page, pno: int) -> tuple[list[str], list[dict[str, Any]]]:
    regions = figure_regions(page)
    body, inside = [], {r["figure"]: [] for r in regions}
    for b in sorted((b for b in page.get_text("blocks") if b[6] == 0), key=lambda b: (b[1], b[0])):
        t = clean(b[4])
        if not t or NOISE.match(t):
            continue
        r = next((r for r in regions if pymupdf.Rect(b[:4]).intersects(r["rect"])
                  and pymupdf.Rect(b[:4]).y0 >= r["rect"].y0 - 1), None)
        (inside[r["figure"]] if r else body).append(t)
    for r in regions:
        r["embedded_text"] = " | ".join(inside[r["figure"]])
        r.pop("rect")
    return body, regions


def text_chunks(doc: pymupdf.Document, pages: range, max_chars: int = 900) -> list[dict[str, Any]]:
    """Greedy grouping of body paragraphs per page (never across pages, so `page` is exact)."""
    out = []
    for pno in pages:
        body, _ = page_text_and_figures(doc[pno - 1], pno)
        groups, cur = [], ""
        for para in body:
            if cur and len(cur) + 1 + len(para) > max_chars:
                groups.append(cur)
                cur = para
            else:
                cur = f"{cur}\n{para}".strip()
            while len(cur) > max_chars * 1.6:  # very long paragraph: split at sentence end
                cut = cur.rfind(". ", 0, max_chars) + 1 or max_chars
                groups.append(cur[:cut].strip())
                cur = cur[cut:].strip()
        if cur:
            groups.append(cur)
        for i, g in enumerate(groups):
            out.append({"id": f"{SOURCE_ID}:p{pno:03d}:text:{i:02d}", "text": g, "source_id": SOURCE_ID,
                        "source": SOURCE, "page": pno,
                        "metadata": {"kind": "text", "printed_page": printed_page(pno), "section": section_of(doc, pno)}})
    return out


_TOC_CACHE: dict[int, list] = {}


def section_of(doc: pymupdf.Document, pno: int) -> str:
    toc = _TOC_CACHE.setdefault(id(doc), doc.get_toc())
    title = ""
    for lvl, t, p in toc:
        if p <= pno:
            title = t.strip()
    return title
