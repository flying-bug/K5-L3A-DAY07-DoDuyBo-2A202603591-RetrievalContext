"""Connect to the Day 6 pgvector store, export its chunks for BM25/evaluation, and prove that the
Day 7 query embedder is compatible with the stored document vectors.

Run:  python -m src.export_chunks
Writes data/chunks_para800.json (the index all retrievers use) and results/day6_connection.json;
fixed800o100 is only checked for compatibility, not exported.
"""
from __future__ import annotations

import random

import numpy as np

from .common import DATA, RESULTS, Timer, load_questions, normalize_for_match, now_iso, utf8_stdout, write_json
from .day6_store import Day6Store, QueryEmbedder

INDEXES = ("para800", "fixed800o100")


def main() -> None:
    utf8_stdout()
    store = Day6Store()
    with Timer() as t_db:
        versions = store.versions()
    print("Day 6 store:", versions)
    with Timer() as t_model:
        emb = QueryEmbedder.shared()
    report = {"created_at": now_iso(), "store": versions, "embedder": emb.info(),
              "db_ms": round(t_db.ms, 1), "model_load_ms": round(t_model.ms, 1), "indexes": {}}
    if emb.dimensions != int(versions["embedding_column"].strip("vector()")):
        raise RuntimeError(f"embedder dims {emb.dimensions} != store {versions['embedding_column']}")

    questions = load_questions("dev")  # test gold is not inspected before the config is frozen
    for index in INDEXES:
        chunks = store.all_chunks(index)
        if index == "para800":  # only index used by BM25 / lookup / evaluation
            write_json(DATA / f"chunks_{index}.json", chunks)
        # Compatibility: re-embed 8 random stored chunks with the document prompt -> cosine to stored.
        rng = random.Random(7)
        sample = rng.sample(chunks, 8)
        stored = store.stored_vectors(index, [c["id"] for c in sample])
        fresh = emb.embed_documents([c["text"] for c in sample])
        cos = [float(np.dot(fresh[i], np.asarray(stored[c["id"]]))) for i, c in enumerate(sample)]
        # Ceiling check (evaluation only): can each gold evidence fit inside one chunk of this index?
        containable = {}
        for q in questions:
            if q["answerable"]:
                containable[q["id"]] = any(
                    c["source_id"] == g["source_id"] and c["page"] == g["page"]
                    and normalize_for_match(g["evidence"]) in normalize_for_match(c["text"])
                    for g in q["gold"] for c in chunks)
        report["indexes"][index] = {
            "chunks": len(chunks), "pages": len({c["page"] for c in chunks}),
            "chars_total": sum(len(c["text"]) for c in chunks),
            "reembed_cosine_min": round(min(cos), 6), "reembed_cosine_mean": round(float(np.mean(cos)), 6),
            "evidence_containable": f"{sum(containable.values())}/{len(containable)}",
            "not_containable": [k for k, v in containable.items() if not v],
        }
        print(index, report["indexes"][index])
    write_json(RESULTS / "day6_connection.json", report)


if __name__ == "__main__":
    main()
