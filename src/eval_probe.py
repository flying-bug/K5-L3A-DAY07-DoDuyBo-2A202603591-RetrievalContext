"""Post-hoc probe (added after the frozen test run): questions that ask about a whole AI RMF Core
category or one subcategory by code. Measures completeness automatically:
- context coverage: share of the category's table entries ('MAP 1.1:' ...) present in the final context
- answer coverage: share of entries whose code ('1.3', 'MAP 1.3') is mentioned in the answer
Expected entries are read from the document structure (regex on chunks), evaluation only.

Run:  python -m src.eval_probe --configs A5_dense_rerank_seed,A6_seed_category_lookup
"""
from __future__ import annotations

import argparse
import json
import re

from .agent import make_agent
from .common import BENCH, RESULTS, load_chunks, now_iso, utf8_stdout, write_json
from .retrievers import build_retriever
from .run_agent import CONFIGS

PROBE = BENCH.parent / "probe_category.json"


def expected_entries(code: str, chunks) -> list[str]:
    func, num = code.split()
    if "." in num:
        return [code]
    pat = re.compile(rf"\b{func} {num}\.(\d+):")
    found = sorted({int(m.group(1)) for c in chunks for m in pat.finditer(c["text"])})
    return [f"{func} {num}.{i}" for i in found]


def main() -> None:
    utf8_stdout()
    ap = argparse.ArgumentParser()
    ap.add_argument("--configs", required=True)
    args = ap.parse_args()
    probes = json.loads(PROBE.read_text(encoding="utf-8"))
    chunks = load_chunks("para800")
    by_id = {c["id"]: c for c in chunks}
    report = {"created_at": now_iso(), "configs": {}}
    for name in args.configs.split(","):
        cfg = CONFIGS[name]
        agent = make_agent(cfg, build_retriever(cfg.retrieval, cfg.index))
        rows = []
        for p in probes:
            t = agent.run(p["id"], p["question"], p.get("filter"))
            exp = expected_entries(p["code"], chunks)
            ctx = "\n".join(by_id[i]["text"] for i in t.get("context_ids", []))
            in_ctx = [e for e in exp if f"{e}:" in ctx]
            num = lambda e: e.split()[1]  # noqa: E731  '1.3'
            in_ans = [e for e in exp if re.search(rf"(?<![\d.]){re.escape(num(e))}(?![\d])", t["answer"] or "")]
            rows.append({"id": p["id"], "question": p["question"], "status": t["status"], "expected": exp,
                         "context_coverage": f"{len(in_ctx)}/{len(exp)}", "answer_coverage": f"{len(in_ans)}/{len(exp)}",
                         "missing_in_answer": [e for e in exp if e not in in_ans], "n_searches": t["n_searches"],
                         "elapsed_s": round(t["elapsed_ms"] / 1000, 2), "cost_usd": t["cost_usd"],
                         "answer": t["answer"], "citations": t["citations"],
                         "searches": [{"tool": e["tool"], "query": e["query"], "added": e["added"]}
                                      for e in t["events"] if e["event"] == "search"]})
            print(f"{name:26s} {p['id']} {t['status']:8s} ctx {rows[-1]['context_coverage']:>6s} "
                  f"ans {rows[-1]['answer_coverage']:>6s} {rows[-1]['elapsed_s']}s missing={rows[-1]['missing_in_answer']}",
                  flush=True)
        tot = lambda k: (sum(int(r[k].split("/")[0]) for r in rows), sum(int(r[k].split("/")[1]) for r in rows))  # noqa: E731
        report["configs"][name] = {"context_coverage": "%d/%d" % tot("context_coverage"),
                                   "answer_coverage": "%d/%d" % tot("answer_coverage"),
                                   "cost_usd": round(sum(r["cost_usd"] for r in rows), 4), "rows": rows}
        print(name, report["configs"][name]["context_coverage"], report["configs"][name]["answer_coverage"])
    write_json(RESULTS / "probe_category.json", report)


if __name__ == "__main__":
    main()
