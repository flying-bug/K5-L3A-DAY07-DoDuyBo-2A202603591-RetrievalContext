# Retrieval summary — test (para800), 2026-11-14T08:44:58Z

| Config | Ghi chú | Hit@1 | Evidence Hit@3 | Hit@5 | MRR@10 | Context Evidence Rate | Context TB (ký tự) | Latency trung vị | Miss @3 |
|---|---|---|---|---|---|---|---|---|---|
| dense_f | Day 6 strategy C: + user-supplied function filter | 4/8 = 0.50 | 6/8 = 0.75 | 6/8 | 0.646 | 6/8 = 0.75 | 1946 | 111.2 ms | t05, t06 |
| dense_rerank_f | dense top-20 -> cross-encoder rerank | 6/8 = 0.75 | 6/8 = 0.75 | 6/8 | 0.771 | 6/8 = 0.75 | 2001 | 912.6 ms | t01, t05 |
