# Retrieval summary — dev (para800), 2026-11-14T07:22:11Z

| Config | Ghi chú | Hit@1 | Evidence Hit@3 | Hit@5 | MRR@10 | Context Evidence Rate | Context TB (ký tự) | Latency trung vị | Miss @3 |
|---|---|---|---|---|---|---|---|---|---|
| dense | Baseline = Day 6 strategy B (pgvector, no filter) | 17/22 = 0.77 | 19/22 = 0.86 | 19/22 | 0.837 | 19/22 = 0.86 | 2098 | 120.5 ms | q11, q18, q22 |
| dense_f | Day 6 strategy C: + user-supplied function filter | 17/22 = 0.77 | 19/22 = 0.86 | 19/22 | 0.837 | 19/22 = 0.86 | 2098 | 123.0 ms | q11, q18, q22 |
| bm25_f | Lexical BM25 on the same chunks | 17/22 = 0.77 | 20/22 = 0.91 | 20/22 | 0.847 | 20/22 = 0.91 | 2063 | 0.6 ms | q02, q19 |
| hybrid_f | RRF(dense, BM25), depth 50, k=60 | 18/22 = 0.82 | 20/22 = 0.91 | 21/22 | 0.875 | 20/22 = 0.91 | 2108 | 122.4 ms | q02, q18 |
| hybrid_rerank_f | hybrid top-20 -> multilingual cross-encoder rerank | 17/22 = 0.77 | 22/22 = 1.00 | 22/22 | 0.886 | 22/22 = 1.00 | 2121 | 968.4 ms | - |
| dense_rerank_f | dense top-20 -> cross-encoder rerank | 17/22 = 0.77 | 22/22 = 1.00 | 22/22 | 0.886 | 22/22 = 1.00 | 2152 | 941.6 ms | - |
| hybrid_rerank_f_k5 | context: top-5 within 4500 chars | 17/22 = 0.77 | 22/22 = 1.00 | 22/22 | 0.886 | 22/22 = 1.00 | 3454 | 955.6 ms | - |
| hybrid_rerank_f_nb | context: top-3 + next chunk on same page after rank 1, 4500 chars | 17/22 = 0.77 | 22/22 = 1.00 | 22/22 | 0.886 | 22/22 = 1.00 | 2567 | 851.2 ms | - |
