"""Combine agent traces + human review labels into the BENCHMARK.md answer metrics.

Run:  python -m src.summarize_agent --split dev --configs A0_dense,A1_dense_rerank
Needs results/agent/<split>/<config>/{traces,cases,auto,reviews}.json. Label aggregation is done by
starter/agent_metrics.py (unchanged); this script only adds the auto metrics and writes a table.
"""
from __future__ import annotations

import argparse
import json
import sys

from .common import RESULTS, ROOT, utf8_stdout, write_json

sys.path.insert(0, str(ROOT / "starter"))
from agent_metrics import aggregate  # noqa: E402


def frac(d):
    return f"{d['n']}/{d['N']}" + (f" = {d['n'] / d['N']:.2f}" if d["N"] else " (không áp dụng)")


def main() -> None:
    utf8_stdout()
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", choices=("dev", "test"), required=True)
    ap.add_argument("--configs", required=True)
    args = ap.parse_args()
    rows = []
    for name in args.configs.split(","):
        d = RESULTS / "agent" / args.split / name
        load = lambda f: json.loads((d / f).read_text(encoding="utf-8"))  # noqa: E731
        traces, cases, auto = load("traces.json"), load("cases.json"), load("auto.json")
        agg = aggregate(cases, traces, load("reviews.json"))
        write_json(d / "summary.json", {"auto": auto, "labels": agg})
        g = agg["grounded_answer"]
        rows.append(f"| {name} | {frac(agg['tool_use'])} | {auto['mean_searches']} {auto['searches_distribution']} "
                    f"| {g['0']}/{g['1']}/{g['2']}, TB {g['mean']:.2f}/2 | {frac(agg['citation_validity'])} "
                    f"| {frac(agg['answer_citation_coverage'])} | {frac(agg['abstention'])} | {frac(agg['false_abstention'])} "
                    f"| {auto['context_evidence_rate']} | {auto['median_latency_s']} s | ${auto['cost_usd_list_price']:.4f} "
                    f"| {agg['provider_errors']} |")
        print(name, json.dumps(agg, ensure_ascii=False))
    head = ("| Cấu hình | Tool use | Số lượt search TB {phân bố} | Grounded 0/1/2, TB | Citation hợp lệ "
            "| Câu trả lời có citation | Abstention đúng | Từ chối nhầm | Context Evidence Rate | Latency trung vị "
            "| Chi phí (giá niêm yết) | Lỗi provider |\n|---|---|---|---|---|---|---|---|---|---|---|---|")
    text = f"# Agent summary — {args.split}\n\n{head}\n" + "\n".join(rows) + "\n"
    (RESULTS / "agent" / args.split / "summary.md").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
