"""Run a configuration of the WHO agent on the bonus benchmark and save full traces.

    python advanced/run_bench.py --config W2_hybrid_rerank_images --split dev
Writes advanced/results/<split>/<config>/traces.json and auto.json. Pass/fail labels are written by
hand to labels.json in the same folder (see advanced/README.md); this script never grades answers.
Automatic metric: page coverage = every gold evidence page is covered by some chunk in the final context
(table rows cover both pages of their spread).
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "advanced"))
from agent_whs import WHSAgent, WHSConfig  # noqa: E402
from src.common import load_chunks, now_iso, utf8_stdout, write_json  # noqa: E402
from src.retrievers import build_retriever  # noqa: E402

BENCH = ROOT / "advanced" / "benchmark" / "questions.json"
OUT = ROOT / "advanced" / "results"

CONFIGS = {
    # baseline: dense pgvector only, model's own queries, text only
    "W0_dense_text": WHSConfig(name="W0_dense_text", retrieval="dense", top_k=5, budget_chars=14000, max_searches=3,
                               model_filter=False, attach_images=0, model="gpt-4.1-mini"),
    # + hybrid (dense+BM25 RRF) and cross-encoder rerank, first search = question verbatim, text only
    "W1_hybrid_rerank_text": WHSConfig(name="W1_hybrid_rerank_text", retrieval="hybrid_rerank", top_k=5,
                                       budget_chars=14000, max_searches=3, model_filter=False, seed_original=True,
                                       attach_images=0, model="gpt-4.1-mini"),
    # + figure images attached to the answering model
    "W2_hybrid_rerank_images": WHSConfig(name="W2_hybrid_rerank_images", retrieval="hybrid_rerank", top_k=5,
                                         budget_chars=14000, max_searches=3, model_filter=False, seed_original=True,
                                         attach_images=4, model="gpt-4.1-mini"),
    # same as W2 with a stronger answering model
    "W3_hybrid_rerank_images_4.1": WHSConfig(name="W3_hybrid_rerank_images_4.1", retrieval="hybrid_rerank", top_k=5,
                                             budget_chars=14000, max_searches=3, model_filter=False, seed_original=True,
                                             attach_images=4, model="gpt-4.1"),
    # after dev round 1: hybrid+rerank lost the Thailand annex row (D10) because BM25/rerank favour figure
    # chunks when the query names a figure; dense kept it. W4/W5 = dense retrieval + images, two models.
    "W4_dense_images_4.1": WHSConfig(name="W4_dense_images_4.1", retrieval="dense", top_k=5, budget_chars=14000,
                                     max_searches=3, model_filter=False, attach_images=4, model="gpt-4.1"),
    "W5_dense_images_mini": WHSConfig(name="W5_dense_images_mini", retrieval="dense", top_k=5, budget_chars=14000,
                                      max_searches=3, model_filter=False, attach_images=4, model="gpt-4.1-mini"),
}
PRICES ={"gpt-4.1-mini": (0.40, 1.60), "gpt-4.1": (2.00, 8.00)}


def chunk_pages(c) -> set[int]:
    return set(c["metadata"].get("pages") or [c["page"]])


def main() -> None:
    utf8_stdout()
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", choices=list(CONFIGS), required=True)
    ap.add_argument("--split", choices=("dev", "test"), required=True)
    ap.add_argument("--only", default="")
    args = ap.parse_args()
    cfg = CONFIGS[args.config]
    qs = [q for q in json.loads(BENCH.read_text(encoding="utf-8")) if q["split"] == args.split]
    if args.only:
        qs = [q for q in qs if q["id"] in set(args.only.split(","))]
    chunks = {c["id"]: c for c in load_chunks("whs2023")}
    agent = WHSAgent(cfg, build_retriever(cfg.retrieval, cfg.index))
    p_in, p_out = PRICES[cfg.model]
    traces = []
    for q in qs:
        t = agent.run(q["id"], q["question"], None)  # only the question text reaches the agent
        u = t["usage"]
        t["cost_usd"] = round((u["input"] * p_in + (u["output"] + u["thinking"]) * p_out) / 1e6, 6)
        ctx_pages = set().union(*[chunk_pages(chunks[i]) for i in t.get("context_ids", [])]) if t.get("context_ids") else set()
        if q["answerable"]:
            need = {e["page"] for e in q["evidence"]}
            t["gold_pages"] = sorted(need)
            t["context_covers_gold_pages"] = need <= ctx_pages
        traces.append(t)
        print(f"{q['id']} {q['group']:12s} {t['status']:8s} s={t['n_searches']} {t['elapsed_ms']/1000:5.1f}s "
              f"cov={t.get('context_covers_gold_pages', '-')} | {(t['answer'] or t.get('error') or '')[:150]!r}", flush=True)
    ok = [t for t in traces if t["status"] != "error"]
    ans = [t for t in ok if "gold_pages" in t]
    auto = {"config": {k: v for k, v in cfg.as_dict().items()}, "split": args.split, "created_at": now_iso(),
            "n": len(traces), "errors": [t["query_id"] for t in traces if t["status"] == "error"],
            "status": dict(Counter(t["status"] for t in traces)),
            "context_page_coverage": f"{sum(t['context_covers_gold_pages'] for t in ans)}/{len(ans)}",
            "coverage_misses": [t["query_id"] for t in ans if not t["context_covers_gold_pages"]],
            "searches": dict(Counter(t["n_searches"] for t in ok)),
            "images": sum(len(e["ids"]) for t in traces for e in t["events"] if e["event"] == "images_attached"),
            "median_latency_s": round(statistics.median(t["elapsed_ms"] for t in traces) / 1000, 2),
            "tokens_in": sum(t["usage"]["input"] for t in traces), "tokens_out": sum(t["usage"]["output"] for t in traces),
            "cost_usd": round(sum(t["cost_usd"] for t in traces), 4)}
    if not args.only:
        d = OUT / args.split / cfg.name
        write_json(d / "traces.json", traces)
        write_json(d / "auto.json", auto)
    print(json.dumps({k: v for k, v in auto.items() if k != "config"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
