# Code Day 7 — Agentic RAG trên vector store Day 6

> Mới học code? Đọc theo [Hướng dẫn đọc mã tiếng Việt](HUONG_DAN_CODE_VI.md). Tài liệu này chỉ rõ nên bắt đầu ở hàm nào, mỗi đoạn kết thúc ở đâu và có liên kết sang bước kế tiếp.

| File | Việc |
|---|---|
| `common.py` | Đường dẫn, `.env`, đọc benchmark, so khớp gold (giống Day 6) |
| `day6_store.py` | Kết nối **read-only** pgvector Day 6 + query embedder EmbeddingGemma-300m (768 chiều) |
| `export_chunks.py` | Xuất chunk từ pgvector ra `data/chunks_<index>.json`, kiểm tra embed lại = vector đã lưu |
| `retrievers.py` | `dense` (pgvector), `bm25`, `hybrid` (RRF), `*_rerank` (cross-encoder) |
| `context.py` | Chọn context: dedup, budget ký tự, chunk lân cận |
| `eval_retrieval.py` | Benchmark retrieval/context (không LLM): Hit@1, Evidence Hit@3, MRR@10, Context Evidence Rate |
| `agent.py` | Agent Gemini function calling: `search_documents`, `submit_answer`; trace mọi lượt gọi |
| `run_agent.py` | Chạy agent theo cấu hình trên dev/test, lưu trace + metric tự động |
| `review_sheet.py` | Tạo bảng đọc tay (câu trả lời + toàn văn chunk được trích) |
| `summarize_agent.py` | Gộp nhãn chấm tay bằng `starter/agent_metrics.py` |

Cách chạy: xem [README gốc](../README_DAY7.md).
