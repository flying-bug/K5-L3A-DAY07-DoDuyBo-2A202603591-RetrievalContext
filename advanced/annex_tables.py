"""Parse WHO WHS 2023 Annex 1 tables (PDF pages 94-125) into one record per country/region row.

Each table is printed as 2-page spreads: the left (even) page has the country names, the right (odd)
page continues the same rows with more indicators but no names. Rows are matched by ORDER, and the
row-to-row spacing is checked on both pages (multi-line names make taller rows on both sides).
Values come from PDF word coordinates (exact, no OCR); "5 582"-style thousands groups are merged;
superscript footnote letters are kept as notes. Column labels are read by the vision model from the
header strip and must match the column count found in the data (else the page fails loudly).
"""
from __future__ import annotations

import re
from collections import Counter, defaultdict
from pathlib import Path

import pymupdf

VAL = re.compile(r"^(-|<?>?-?\d[\d.,]*|<\d[\d.,]*|>\d[\d.,]*)$")
NOTE = re.compile(r"^[a-z]{1,3}$")
YEAR = re.compile(r"^(19|20)\d\d(–(19|20)\d\d)?$")
NAME_X = 175.0            # country names live left of this x (pt) on left pages
TAB_LEFT, TAB_RIGHT = 60.0, 565.0   # "Part N" side tabs


def _lines(page, left: bool, tol=2.0):
    rows = defaultdict(list)
    for x0, y0, x1, y1, w, *_ in page.get_text("words"):
        if (left and x0 < TAB_LEFT) or (not left and x0 > TAB_RIGHT):  # side tab "Part N"
            continue
        rows[round((y0 + y1) / 2 / tol)].append((x0, y0, x1, y1, w))
    return [sorted(v) for _, v in sorted(rows.items())]


def _merge(tokens):
    """Join '5' '582' -> '5 582' (gap < 3.5pt); keep '-' separate; split off footnote letters."""
    out = []
    for t in tokens:
        if out and VAL.match(t[4]) and t[4] != "-" and out[-1]["v"] != "-" and t[0] - out[-1]["x1"] < 3.5 \
                and re.fullmatch(r"\d{3}", t[4]):
            out[-1]["v"] += " " + t[4]
            out[-1]["x1"] = t[2]
        elif VAL.match(t[4]):
            out.append({"v": t[4], "x0": t[0], "x1": t[2], "note": ""})
        elif NOTE.match(t[4]) and out:
            out[-1]["note"] += t[4]
    return out


def _header_end(lines, left: bool):
    if left:
        for ln in lines:
            if any(w[4] == "Countries" for w in ln):
                return max(w[3] for w in ln)
        return None
    # right pages: FIRST line made of years (a later one introduces the WHO-region block)
    for ln in lines:
        if sum(bool(YEAR.match(w[4])) for w in ln) >= 3:
            return max(w[3] for w in ln)
    return None


def parse_side(page, left: bool):
    lines = _lines(page, left)
    hdr_end = _header_end(lines, left)
    if hdr_end is None:
        raise ValueError(f"page {page.number + 1}: header end not found")
    bottom = page.rect.height - 45
    body = [ln for ln in lines if ln[0][1] > hdr_end + 0.5 and ln[0][3] < bottom]
    rows = []      # value rows: y, tokens
    names = []     # (y, text) name fragments on left pages
    for ln in body:
        y = sum((w[1] + w[3]) / 2 for w in ln) / len(ln)
        name_words = [w for w in ln if left and w[2] <= NAME_X]
        vals = _merge([w for w in ln if not left or w[0] > NAME_X])
        if name_words:
            names.append((y, " ".join(w[4] for w in name_words)))
        if vals and all(YEAR.match(v["v"]) for v in vals):
            continue  # repeated year sub-header before the WHO-region rows
        if vals:
            rows.append({"y": y, "vals": vals})
        elif not name_words and rows:  # superscript-only line: attach notes to previous row
            pass
    if left:
        for r in rows:
            frag = [t for (y, t) in names if abs(y - r["y"]) < 6.5 and t != "WHO region"]
            r["name"] = " ".join(frag)
    header_words = " ".join(w[4] for ln in lines if ln[0][3] <= hdr_end + 0.5 and ln[0][1] > 80 for w in ln)
    k = Counter(len(r["vals"]) for r in rows).most_common(1)[0][0]
    return {"hdr_end": hdr_end, "rows": rows, "k": k, "header_words": header_words, "top": min(
        (w[1] for ln in lines for w in ln if w[1] > 80), default=90)}


def parse_spread(doc, left_pno: int):
    L = parse_side(doc[left_pno - 1], left=True)
    R = parse_side(doc[left_pno], left=False)
    problems = []
    if len(L["rows"]) != len(R["rows"]):
        problems.append(f"row count {len(L['rows'])} vs {len(R['rows'])}")
    else:
        dl = [b["y"] - a["y"] for a, b in zip(L["rows"], L["rows"][1:])]
        dr = [b["y"] - a["y"] for a, b in zip(R["rows"], R["rows"][1:])]
        bad = [i for i, (a, b) in enumerate(zip(dl, dr)) if abs(a - b) > 2.0]
        if bad:
            problems.append(f"row spacing differs at rows {bad[:5]}")
    for side, s in (("left", L), ("right", R)):
        odd = [r.get("name", r["y"]) for r in s["rows"] if len(r["vals"]) != s["k"]]
        if odd:
            problems.append(f"{side}: rows with != {s['k']} values: {odd[:5]}")
    return L, R, problems
