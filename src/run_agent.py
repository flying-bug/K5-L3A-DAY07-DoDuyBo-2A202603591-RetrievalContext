"""Run the Gemini agent on a split with one named configuration and save full traces.

Run:  python -m src.run_agent --config A0_dense --split dev
Writes results/agent/<split>/<config>/traces.json, auto.json (automatic metrics) and
cases.json (input for starter/agent_metrics.py). Human labels go to reviews.json next to them.

Automatic metrics here never judge answer quality: they count status, tool calls, latency, tokens,
cost, and (evaluation only, using gold) whether the final context held the evidence.
"""
from __future__ import annotations

import argparse
import statistics
from collections import Counter
from typing import Any

from .agent import AgentConfig, make_agent
from .common import RESULTS, is_evidence_hit, load_chunks, load_questions, now_iso, public_question, utf8_stdout, write_json
from .retrievers import build_retriever

CONFIGS = {
    # baseline: Day 6 strategy C as the tool (dense pgvector + user filter), 3 chunks per search
    "A0_dense": AgentConfig(name="A0_dense", retrieval="dense", top_k=3, budget_chars=3000, max_searches=3),
    # improvement 1: same agent, retrieval tool = dense top-20 + cross-encoder rerank
    "A1_dense_rerank": AgentConfig(name="A1_dense_rerank", retrieval="dense_rerank", top_k=3,
                                   budget_chars=3000, max_searches=3),
    # improvement 2: hybrid (dense+BM25 RRF) top-20 + rerank
    "A2_hybrid_rerank": AgentConfig(name="A2_hybrid_rerank", retrieval="hybrid_rerank", top_k=3,
                                    budget_chars=3000, max_searches=3),
    # context/turn ablation: one search only, top-5, bigger budget
    "A3_dense_rerank_1shot_k5": AgentConfig(name="A3_dense_rerank_1shot_k5", retrieval="dense_rerank", top_k=5,
                                            budget_chars=4500, max_searches=1),
    # improvement 3 (from dev error analysis): the model may no longer add its own function_filter;
    # only the user-supplied filter applies. Otherwise identical to A1.
    "A4_dense_rerank_userfilter": AgentConfig(name="A4_dense_rerank_userfilter", retrieval="dense_rerank", top_k=3,
                                              budget_chars=3000, max_searches=3, model_filter=False),
    # improvement 4: A4 + first search = the question verbatim (seed), budget 4500 so follow-up
    # searches still fit.
    "A5_dense_rerank_seed": AgentConfig(name="A5_dense_rerank_seed", retrieval="dense_rerank", top_k=3,
                                        budget_chars=4500, max_searches=3, model_filter=False, seed_original=True),
    # A6 (added AFTER the A5 test run, from a UI failure on "MAP 1 là gì"): A5 + exact lookup of every
    # table entry of a category/subcategory code named in the question; budget 6000 so a whole
    # category (MEASURE 2 = 4 chunks) fits. Not part of the frozen test comparison.
    "A6_seed_category_lookup": AgentConfig(name="A6_seed_category_lookup", retrieval="dense_rerank", top_k=3,
                                           budget_chars=6000, max_searches=3, model_filter=False,
                                           seed_original=True, category_lookup=True),
}


def auto_metrics(questions: list[dict[str, Any]], traces: list[dict[str, Any]], chunks_by_id) -> dict[str, Any]:
    by_q = {q["id"]: q for q in questions}
    ok = [t for t in traces if t["status"] != "error"]
    ans_q = [t for t in ok if by_q[t["query_id"]]["answerable"]]
    una_q = [t for t in ok if not by_q[t["query_id"]]["answerable"]]
    ctx_hit = [t["query_id"] for t in ans_q
               if any(is_evidence_hit(chunks_by_id[i], by_q[t["query_id"]]["gold"]) for i in t.get("context_ids", []))]
    searches = Counter(t["n_searches"] for t in ok)
    return {
        "runs": len(traces), "errors": [t["query_id"] for t in traces if t["status"] == "error"],
        "tool_use": f"{sum(t['n_searches'] > 0 for t in ok)}/{len(ok)}",
        "searches_distribution": dict(sorted(searches.items())),
        "mean_searches": round(statistics.mean(t["n_searches"] for t in ok), 2) if ok else None,
        "status_answerable": dict(Counter(t["status"] for t in ans_q)),
        "status_unanswerable": dict(Counter(t["status"] for t in una_q)),
        "context_evidence_rate": f"{len(ctx_hit)}/{len(ans_q)}",
        "context_misses": sorted(set(t["query_id"] for t in ans_q) - set(ctx_hit)),
        "answered_with_citation": f"{sum(bool(t['citations']) for t in ok if t['status'] == 'answered')}/"
                                  f"{sum(t['status'] == 'answered' for t in ok)}",
        "invalid_citation_events": [t["query_id"] for t in ok if any(e["event"] == "invalid_citations" for e in t["events"])],
        "median_latency_s": round(statistics.median(t["elapsed_ms"] for t in ok) / 1000, 2) if ok else None,
        "mean_context_chars": round(statistics.mean(t.get("context_chars", 0) for t in ok)) if ok else None,
        "tokens": {k: sum(t["usage"][k] for t in traces) for k in ("input", "output", "thinking", "calls")},
        "cost_usd_list_price": round(sum(t["cost_usd"] for t in traces), 4),
    }


def main() -> None:
    utf8_stdout()
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", choices=list(CONFIGS), required=True)
    ap.add_argument("--split", choices=("dev", "test"), required=True)
    ap.add_argument("--only", default="", help="comma-separated query ids (debug)")
    args = ap.parse_args()
    cfg = CONFIGS[args.config]
    questions = load_questions(args.split)
    if args.only:
        keep = set(args.only.split(","))
        questions = [q for q in questions if q["id"] in keep]
    retriever = build_retriever(cfg.retrieval, cfg.index)
    agent = make_agent(cfg, retriever)
    traces = []
    for q in questions:
        pq = public_question(q)  # only id, question, user filter reach the agent
        tr = agent.run(pq["id"], pq["question"], pq["filter"])
        traces.append(tr)
        print(f"{q['id']:4s} {tr['status']:9s} searches={tr['n_searches']} {tr['elapsed_ms']/1000:5.1f}s "
              f"cits={tr['citations']} | {(tr['answer'] or tr.get('error') or '')[:110]!r}", flush=True)
    out = RESULTS / "agent" / args.split / cfg.name
    chunks_by_id = {c["id"]: c for c in load_chunks(cfg.index)}
    summary = {"config": cfg.as_dict(), "retriever": retriever.name, "split": args.split,
               "created_at": now_iso(), **auto_metrics(questions, traces, chunks_by_id)}
    if not args.only:
        write_json(out / "traces.json", traces)
        write_json(out / "auto.json", summary)
        write_json(out / "cases.json", [{"id": q["id"], "split": q["split"], "answerable": q["answerable"]}
                                        for q in questions])
    print({k: v for k, v in summary.items() if k not in ("config",)})


if __name__ == "__main__":
    main()
