"""Write a Markdown sheet for manual review: question, expected answer + gold evidence, every search
the agent made, the answer, and the full text of each cited chunk (to check support by reading).

Run:  python -m src.review_sheet --split dev --config A1_dense_rerank
Output: results/agent/<split>/<config>/review_sheet.md
"""
from __future__ import annotations

import argparse
import json

from .common import RESULTS, is_evidence_hit, load_chunks, load_questions, utf8_stdout


def main() -> None:
    utf8_stdout()
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", required=True)
    ap.add_argument("--config", required=True)
    args = ap.parse_args()
    d = RESULTS / "agent" / args.split / args.config
    traces = json.loads((d / "traces.json").read_text(encoding="utf-8"))
    qs = {q["id"]: q for q in load_questions(args.split)}
    chunks = {c["id"]: c for c in load_chunks("para800")}
    out = [f"# Review sheet — {args.config} / {args.split}", ""]
    for t in traces:
        q = qs[t["query_id"]]
        out += [f"## {q['id']} ({q['type']}) — {t['status']}", "", f"**Q:** {q['question']}", ""]
        if q["answerable"]:
            g = q["gold"][0]
            out += [f"**Expected:** {q['expected_answer']}", "",
                    f"**Gold:** p{g['page']} — \"{g['evidence']}\"", ""]
        else:
            out += [f"**Unanswerable:** {q['absence_reason']}", ""]
        for e in t["events"]:
            if e["event"] == "search":
                marks = []
                for r in e["results"]:
                    hit = q["answerable"] and is_evidence_hit(chunks[r["id"]], q["gold"])
                    marks.append(f"{r['id'].split(':', 1)[1]}{'*' if hit else ''}")
                out.append(f"- search `{e['query']}` filter={e['filter']} → {', '.join(marks)} "
                           f"(added {len(e['added'])}, dropped {len(e['dropped_budget'])})")
        out += ["", f"**Answer:** {t['answer']}", ""]
        if t.get("raw_final") and t["raw_final"]["status"] == "answered" and t["status"] != "answered":
            out += [f"**Raw (rejected) answer:** {t['raw_final']}", ""]
        for cid in t["citations"]:
            out += [f"> **{cid}** (p{chunks[cid]['page']}): {chunks[cid]['text']}", ""]
    (d / "review_sheet.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(d / "review_sheet.md")


if __name__ == "__main__":
    main()
