"""Build the multimodal index of WHO World health statistics 2023 (bonus challenge).

Run from the repo root (PDF downloaded to advanced/source/who_whs2023.pdf, see advanced/README.md):
    python advanced/build_index.py
Outputs
- data/chunks_whs2023.json            all chunks (used by BM25, evaluation, the UI)
- pgvector table `chunks`, index_name='whs2023' (same Day 6 DB, same EmbeddingGemma-300m, 768 d);
  only rows with this index_name are replaced, Day 6 rows are untouched
- advanced/results/index_stats.json   counts, timing, vision cost, skipped pages
Chunk kinds: text (body paragraphs), figure (vision description + labels in the figure + bbox),
table_row (one Annex 1 row: every column label with its value, exact numbers from the PDF).
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
import time
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "advanced"))
from annex_tables import parse_spread  # noqa: E402
from pdf_extract import SOURCE, SOURCE_ID, page_text_and_figures, printed_page, text_chunks  # noqa: E402
import vision  # noqa: E402
from src.common import DATA, now_iso, utf8_stdout, write_json  # noqa: E402

PDF = ROOT / "advanced" / "source" / "who_whs2023.pdf"
PDF_SHA256 = "30cbc640d72082c4dec1ae5c0c66b6438686013b2554432d5f5621c9618deb0b"
INDEX = "whs2023"
DECORATIVE = {1: "cover", 2: "inside cover (image only)", 3: "title page", 11: "chapter 1 divider", 42: "blank",
              43: "chapter 2 divider", 81: "chapter 3 divider", 92: "blank", 130: "back cover"}
TEXT_PAGES = [p for p in list(range(4, 92)) + [93, 126, 127, 128, 129] if p not in DECORATIVE]
# annex spreads: (left page, table title, page whose header labels were checked by eye for each side)
SPREADS = {94: "Table 1 (Annex 1-1)", 96: "Table 1 (Annex 1-1)", 98: "Table 1 (Annex 1-1)", 100: "Table 1 (Annex 1-1)",
           102: "Table 2 (Annex 1-2)", 104: "Table 2 (Annex 1-2)", 106: "Table 2 (Annex 1-2)", 108: "Table 2 (Annex 1-2)",
           110: "Table 3 (Annex 1-3)", 112: "Table 3 (Annex 1-3)", 114: "Table 3 (Annex 1-3)", 116: "Table 3 (Annex 1-3)",
           118: "Table 4 (printed 'Annex 2-4')", 120: "Table 4 (printed 'Annex 2-4')", 122: "Table 4 (printed 'Annex 2-4')",
           124: "Table 4 (printed 'Annex 2-4')"}
CANON_HEADER = {"left": {94: 94, 102: 102, 110: 110, 118: 120}, "right": {94: 95, 102: 103, 110: 113, 118: 119}}


def _labels(page: int) -> list[str]:
    return json.loads((vision.CACHE / "annex_headers" / f"p{page:03d}.json").read_text(encoding="utf-8"))["columns"]


def figure_chunks(doc) -> list[dict]:
    out = []
    for pno in range(1, 93):
        _, regs = page_text_and_figures(doc[pno - 1], pno)
        for r in regs:
            v = vision.describe_figure(PDF, pno, r)
            values = v.get("values") or []
            legend = v.get("legend") or []
            legend = [x if isinstance(x, str) else "; ".join(f"{k}: {val}" for k, val in x.items()) for x in legend]
            tin = v.get("text_in_image") or ""
            tin = tin if isinstance(tin, str) else "; ".join(map(str, tin))
            text = (f"{r['figure']} — {r['title']} (page {printed_page(pno)})\n"
                    f"Type: {v.get('kind')}. Axes/units: {v.get('axes_units') or '-'}\n"
                    f"Legend: {'; '.join(legend) or '-'}\n"
                    f"Summary: {v.get('summary', '')}\n"
                    f"Values read from the figure (\"~\" = estimated from the axis, not printed): {'; '.join(map(str, values))}\n"
                    f"Text in the graphic: {tin}\n"
                    f"Labels extracted from the PDF in the figure area: {r['embedded_text']}")
            out.append({"id": f"{SOURCE_ID}:p{pno:03d}:fig:{r['figure'].split()[-1]}", "text": text,
                        "source_id": SOURCE_ID, "source": SOURCE, "page": pno,
                        "metadata": {"kind": "figure", "figure": r["figure"], "figure_kind": v.get("kind"),
                                     "printed_page": printed_page(pno), "bbox": r["bbox"],
                                     "section": f"{r['figure']} {r['title']}"[:160],
                                     "described_by": vision.VISION_MODEL}})
    return out


def _slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")[:60]


def table_chunks(doc) -> list[dict]:
    out = []
    for left, title in SPREADS.items():
        base = max(b for b in CANON_HEADER["left"] if b <= left)
        lab_l, lab_r = _labels(CANON_HEADER["left"][base]), _labels(CANON_HEADER["right"][base])
        L, R, problems = parse_spread(doc, left)
        if problems:
            raise RuntimeError(f"spread {left}: {problems}")
        for a, b in zip(L["rows"], R["rows"]):
            cells = []
            for lab, val in list(zip(lab_l, a["vals"])) + list(zip(lab_r, b["vals"])):
                note = f" (note {val['note']})" if val["note"] else ""
                cells.append(f"{lab}: {val['v']}{note}")
            name = a["name"]
            text = (f"{title} — {name} (WHO World health statistics 2023, Annex 1, printed pages "
                    f"{printed_page(left)}-{printed_page(left + 1)}). '-' = no data.\n" + "\n".join(cells))
            out.append({"id": f"{SOURCE_ID}:annex:{title.split()[1]}:{_slug(name)}", "text": text,
                        "source_id": SOURCE_ID, "source": SOURCE, "page": left,
                        "metadata": {"kind": "table_row", "table": title, "row": name, "pages": [left, left + 1],
                                     "printed_page": printed_page(left), "section": f"{title} — {name}"}})
    ids = [c["id"] for c in out]
    assert len(ids) == len(set(ids)), "duplicate table row ids"
    return out


def upsert(chunks: list[dict]) -> dict:
    import psycopg

    from src.common import setting
    from src.day6_store import QueryEmbedder, _vec

    emb = QueryEmbedder.shared()
    t0 = time.perf_counter()
    vecs = emb.embed_documents([c["text"] for c in chunks])
    embed_s = time.perf_counter() - t0
    with psycopg.connect(setting("DAY6_DATABASE_URL")) as conn, conn.cursor() as cur:
        cur.execute("DELETE FROM chunks WHERE index_name = %s", (INDEX,))
        cur.executemany(
            "INSERT INTO chunks (index_name, chunk_id, document_id, source, page, part, section, function, text, "
            "content_sha256, metadata, embedding_model, embedding) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s::jsonb,%s,%s::vector)",
            [(INDEX, c["id"], c["source_id"], c["source"], c["page"], c["metadata"]["kind"],
              c["metadata"].get("section"), None, c["text"], hashlib.sha256(c["text"].encode()).hexdigest(),
              json.dumps(c["metadata"], ensure_ascii=False), emb.model_path, _vec(v.tolist())) for c, v in zip(chunks, vecs)])
        n = cur.execute("SELECT count(*), count(DISTINCT chunk_id) FROM chunks WHERE index_name=%s", (INDEX,)).fetchone()
    return {"embed_seconds": round(embed_s, 1), "rows_in_pgvector": n[0], "distinct_ids": n[1], "model": emb.name}


def main() -> None:
    utf8_stdout()
    sha = hashlib.sha256(PDF.read_bytes()).hexdigest()
    if sha != PDF_SHA256:
        raise RuntimeError(f"PDF sha256 {sha} != expected {PDF_SHA256}: wrong file/version")
    doc = pymupdf.open(PDF)
    t0 = time.perf_counter()
    text = text_chunks(doc, TEXT_PAGES)
    figs = figure_chunks(doc)
    rows = table_chunks(doc)
    chunks = text + figs + rows
    build_s = time.perf_counter() - t0
    write_json(DATA / f"chunks_{INDEX}.json", chunks)
    db = upsert(chunks)
    stats = {"created_at": now_iso(), "pdf_sha256": sha, "pdf_pages": doc.page_count, "index_name": INDEX,
             "chunks": {"text": len(text), "figure": len(figs), "table_row": len(rows), "total": len(chunks)},
             "text_pages": len(TEXT_PAGES), "figure_pages": sorted({c["page"] for c in figs}),
             "annex_pages": "94-125 (16 two-page spreads)", "skipped_pages": DECORATIVE,
             "vision": {"model": vision.VISION_MODEL, **vision.USAGE, "cost_usd_this_run": vision.cost_usd(),
                        "note": "cached calls are free; first full run cost is in advanced/README.md"},
             "build_seconds": round(build_s, 1), **db}
    write_json(ROOT / "advanced" / "results" / "index_stats.json", stats)
    print(json.dumps(stats, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
