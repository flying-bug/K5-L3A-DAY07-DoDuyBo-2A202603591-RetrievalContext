"""Retrieval + context benchmark (no LLM) for several retrieval configurations on one split.

Run:  python -m src.eval_retrieval --split dev [--configs dense,dense_f,bm25,...]
Writes results/retrieval/<split>/summary.json, summary.md and traces_<config>.json.

Every config uses the original question text (no rewriting), the same corpus/index version, the same
labels, and exports its top-10 ranking, so Hit@1 / Evidence Hit@3 use the same cutoff for all.
"""
from __future__ import annotations

import argparse
import statistics
from typing import Any

from .common import RESULTS, Timer, is_evidence_hit, load_chunks, load_questions, now_iso, utf8_stdout, write_json
from .context import pack, with_neighbours
from .retrievers import (BM25Retriever, CrossEncoderReranker, DenseRetriever, HybridRetriever,
                         RerankRetriever)

DEPTH = 10

# name -> (method, use_user_filter, context top_k, context budget chars, neighbours)
CONFIGS: dict[str, dict[str, Any]] = {
    "dense":           {"method": "dense", "filter": False, "ctx_k": 3, "budget": 3000, "neighbours": 0,
                        "note": "Baseline = Day 6 strategy B (pgvector, no filter)"},
    "dense_f":         {"method": "dense", "filter": True, "ctx_k": 3, "budget": 3000, "neighbours": 0,
                        "note": "Day 6 strategy C: + user-supplied function filter"},
    "bm25_f":          {"method": "bm25", "filter": True, "ctx_k": 3, "budget": 3000, "neighbours": 0,
                        "note": "Lexical BM25 on the same chunks"},
    "hybrid_f":        {"method": "hybrid", "filter": True, "ctx_k": 3, "budget": 3000, "neighbours": 0,
                        "note": "RRF(dense, BM25), depth 50, k=60"},
    "hybrid_rerank_f": {"method": "hybrid_rerank", "filter": True, "ctx_k": 3, "budget": 3000, "neighbours": 0,
                        "note": "hybrid top-20 -> multilingual cross-encoder rerank"},
    "dense_rerank_f":  {"method": "dense_rerank", "filter": True, "ctx_k": 3, "budget": 3000, "neighbours": 0,
                        "note": "dense top-20 -> cross-encoder rerank"},
    # context-selection variants (same ranking as their base method)
    "hybrid_rerank_f_k5": {"method": "hybrid_rerank", "filter": True, "ctx_k": 5, "budget": 4500, "neighbours": 0,
                           "note": "context: top-5 within 4500 chars"},
    "hybrid_rerank_f_nb": {"method": "hybrid_rerank", "filter": True, "ctx_k": 3, "budget": 4500, "neighbours": 1,
                           "note": "context: top-3 + next chunk on same page after rank 1, 4500 chars"},
}


def make(method: str, shared: dict[str, Any]):
    if method == "dense":
        return shared["dense"]
    if method == "bm25":
        return shared["bm25"]
    if method == "hybrid":
        return shared["hybrid"]
    if method == "hybrid_rerank":
        return RerankRetriever(shared["hybrid"], shared["reranker"], candidates=20)
    if method == "dense_rerank":
        return RerankRetriever(shared["dense"], shared["reranker"], candidates=20)
    raise ValueError(method)


def run(split: str, names: list[str], index: str = "para800") -> dict[str, Any]:
    questions = load_questions(split)
    chunks = load_chunks(index)
    shared: dict[str, Any] = {"dense": DenseRetriever(index), "bm25": BM25Retriever(index, chunks)}
    shared["hybrid"] = HybridRetriever(shared["dense"], shared["bm25"], depth=50)
    if any("rerank" in CONFIGS[n]["method"] for n in names):
        shared["reranker"] = CrossEncoderReranker()
    out_dir = RESULTS / "retrieval" / split
    summary: dict[str, Any] = {"split": split, "index": index, "created_at": now_iso(), "configs": {}}
    shared["dense"].search("warm up", filters=None, top_k=1)
    for name in names:
        cfg = CONFIGS[name]
        retr = make(cfg["method"], shared)
        traces = []
        for q in questions:
            filters = q.get("filter") if cfg["filter"] else None
            with Timer() as tm:
                ranked = retr.search(q["question"], filters=filters, top_k=DEPTH)
            sel = ranked[:cfg["ctx_k"]]
            if cfg["neighbours"]:
                sel = with_neighbours(sel, chunks, top_n=cfg["neighbours"])
            context, kept, dropped = pack(sel, cfg["budget"])
            row: dict[str, Any] = {"query_id": q["id"], "question": q["question"], "answerable": q["answerable"],
                                   "type": q["type"], "filter": filters, "latency_ms": round(tm.ms, 1),
                                   "results": [{"rank": r["rank"], "id": r["id"], "page": r["page"],
                                                "section": r["metadata"].get("section"),
                                                "function": r["metadata"].get("function"),
                                                "score": round(float(r["score"]), 6),
                                                **({"components": r["components"]} if "components" in r else {}),
                                                **({"first_stage": r["first_stage"]} if "first_stage" in r else {})}
                                               for r in ranked],
                                   "context_ids": kept, "context_dropped": dropped, "context_chars": len(context)}
            if q["answerable"]:
                hits = [is_evidence_hit(r, q["gold"]) for r in ranked]
                by_id = {r["id"]: r for r in ranked + sel}
                first = next((i + 1 for i, h in enumerate(hits) if h), None)
                row.update({"gold_rank": first, "hit1": bool(hits[:1] and hits[0]), "hit3": any(hits[:3]),
                            "hit5": any(hits[:5]), "rr10": 1 / first if first else 0.0,
                            "context_hit": any(is_evidence_hit(by_id[i], q["gold"]) for i in kept)})
            else:
                row["top1_score"] = row["results"][0]["score"] if row["results"] else None
            traces.append(row)
        ans = [t for t in traces if t["answerable"]]
        n = len(ans)
        s = {"note": cfg["note"], "retriever": retr.name, **{k: v for k, v in cfg.items() if k != "note"},
             "N": n, "hit1": sum(t["hit1"] for t in ans), "hit3": sum(t["hit3"] for t in ans),
             "hit5": sum(t["hit5"] for t in ans), "mrr10": round(sum(t["rr10"] for t in ans) / n, 4),
             "context_hit": sum(t["context_hit"] for t in ans),
             "avg_context_chars": round(statistics.mean(t["context_chars"] for t in traces)),
             "median_latency_ms": round(statistics.median(t["latency_ms"] for t in traces), 1),
             "cost_usd": 0.0, "misses_hit3": [t["query_id"] for t in ans if not t["hit3"]],
             "misses_context": [t["query_id"] for t in ans if not t["context_hit"]]}
        summary["configs"][name] = s
        write_json(out_dir / f"traces_{name}.json", traces)
        print(f"{name:20s} Hit@1 {s['hit1']}/{n}  Hit@3 {s['hit3']}/{n}  Hit@5 {s['hit5']}/{n}  "
              f"MRR@10 {s['mrr10']:.3f}  CtxEv {s['context_hit']}/{n}  ctx {s['avg_context_chars']}ch  "
              f"{s['median_latency_ms']}ms  miss@3 {s['misses_hit3']}")
    write_json(out_dir / "summary.json", summary)
    lines = [f"# Retrieval summary — {split} ({index}), {summary['created_at']}", "",
             "| Config | Ghi chú | Hit@1 | Evidence Hit@3 | Hit@5 | MRR@10 | Context Evidence Rate | Context TB (ký tự) | Latency trung vị | Miss @3 |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for name, s in summary["configs"].items():
        n = s["N"]
        lines.append(f"| {name} | {s['note']} | {s['hit1']}/{n} = {s['hit1']/n:.2f} | {s['hit3']}/{n} = {s['hit3']/n:.2f} "
                     f"| {s['hit5']}/{n} | {s['mrr10']:.3f} | {s['context_hit']}/{n} = {s['context_hit']/n:.2f} "
                     f"| {s['avg_context_chars']} | {s['median_latency_ms']} ms | {', '.join(s['misses_hit3']) or '-'} |")
    (out_dir / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return summary


def main() -> None:
    utf8_stdout()
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", choices=("dev", "test"), required=True)
    ap.add_argument("--configs", default=",".join(CONFIGS))
    args = ap.parse_args()
    run(args.split, [c.strip() for c in args.configs.split(",") if c.strip()])


if __name__ == "__main__":
    main()
