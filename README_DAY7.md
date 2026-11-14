# Day 7 — Bài làm: Agentic RAG trên NIST AI RMF (Day 6 pgvector)

Đỗ Duy Bộ · 2A202603591 · Báo cáo: [report/individual/2A202603591_DoDuyBo.md](report/individual/2A202603591_DoDuyBo.md)

## Thành phần

| Thành phần | Giá trị |
|---|---|
| Corpus | NIST AI 100-1 *AI RMF 1.0* (01/2023), tài liệu công khai của NIST; 48 trang vật lý, 41 trang nội dung được index (Day 6) |
| Vector store | Day 6: PostgreSQL 16.16 + pgvector 0.8.7, bảng `chunks`, exact cosine; index `para800` (186 chunk, dùng chính) và `fixed800o100` (157 chunk) |
| Embedding | `embeddinggemma-300m` local CPU, 768 chiều, chuẩn hóa, prompt query `task: search result \| query: ` — cùng model với index Day 6 (embed lại 8 chunk/index cho cosine = 1.000000 với vector đã lưu) |
| Reranker | `cross-encoder/mmarco-mMiniLMv2-L12-H384-v1` (đa ngữ, local CPU) |
| Agent model | `gpt-4.1-mini` (OpenAI, function calling, temperature 0). Hỗ trợ cả `gemini-2.5-flash`, nhưng free tier chỉ 20 request/ngày nên benchmark dùng OpenAI |
| Kết quả chính | Cấu hình chọn **A5** (dense+rerank, chỉ filter người dùng, lượt đầu = câu hỏi gốc): test grounded 1.88/2 so với baseline 1.12; Context Evidence 7/8 so với 4/8; từ chối đúng 3/3 |
| Benchmark | [benchmark/](benchmark/README.md): dev 22 + 3 thiếu evidence; test **mới** 8 + 3 thiếu evidence |

## Cách chạy lại

Yêu cầu: Python 3.12, Docker, repo Day 6 (`K5-L3A-DAY06-DoDuyBo-2A202603591-DataIngestion`) đã ingest (`python -m src.run --ingest-only` trong `starter/` của Day 6), thư mục model `../models/embeddinggemma-300m` (hoặc đặt `EMBEDDING_MODEL`), OpenAI API key (hoặc Gemini).

```bash
python -m venv .venv
.venv\Scripts\python -m pip install torch --index-url https://download.pytorch.org/whl/cpu
.venv\Scripts\python -m pip install -r requirements.txt
Copy-Item .env.example .env   # điền OPENAI_API_KEY
```

Bật vector store Day 6 (trong `starter/` của repo Day 6):

```bash
docker compose -p day6_student_starter up -d --wait
```

```bash
.venv\Scripts\python -m unittest discover -s tests -v
.venv\Scripts\python -m src.export_chunks
.venv\Scripts\python -m src.eval_retrieval --split dev
.venv\Scripts\python -m src.run_agent --config A0_dense --split dev
.venv\Scripts\python -m src.run_agent --config A1_dense_rerank --split dev
.venv\Scripts\python -m src.run_agent --config A2_hybrid_rerank --split dev
.venv\Scripts\python -m src.run_agent --config A3_dense_rerank_1shot_k5 --split dev
.venv\Scripts\python -m src.run_agent --config A4_dense_rerank_userfilter --split dev
.venv\Scripts\python -m src.run_agent --config A5_dense_rerank_seed --split dev
.venv\Scripts\python -m src.review_sheet --split dev --config A5_dense_rerank_seed
.venv\Scripts\python -m src.summarize_agent --split dev --configs A0_dense,A1_dense_rerank,A2_hybrid_rerank,A3_dense_rerank_1shot_k5,A4_dense_rerank_userfilter,A5_dense_rerank_seed
```

`summarize_agent` cần `reviews.json` (nhãn chấm tay) trong thư mục của từng cấu hình. Tiêu chí chọn: `benchmark/SELECTION.md`; quyết định: `results/selection.json`. Test chỉ chạy sau khi chốt cấu hình:

```bash
.venv\Scripts\python -m src.eval_retrieval --split test --configs dense_f,dense_rerank_f
.venv\Scripts\python -m src.run_agent --config A0_dense --split test
.venv\Scripts\python -m src.run_agent --config A5_dense_rerank_seed --split test
.venv\Scripts\python -m src.summarize_agent --split test --configs A0_dense,A5_dense_rerank_seed
```

Cải tiến sau khi đã chốt (A6, tra cứu theo mã mục) và bộ kiểm tra riêng:

```bash
.venv\Scripts\python -m src.eval_probe --configs A5_dense_rerank_seed,A6_seed_category_lookup
```

## Giao diện hỏi đáp

Điền `OPENAI_API_KEY` (hoặc `GEMINI_API_KEY`) vào `.env`, bật Docker Day 6, rồi chạy:

```bash
.venv\Scripts\python -m src.app --port 8077
```

Mở http://127.0.0.1:8077. Có thể chọn cấu hình agent (A0–A6; mặc định A6 = A5 + tra cứu theo mã mục như `MAP 1`) và filter theo function. Kết quả hiển thị câu trả lời, citation bấm được, toàn văn đoạn được trích, trace từng lượt tìm kiếm, token và chi phí ước tính. Mỗi câu hỏi được ghi vào `results/ui_log.jsonl` (không commit, đã có trong `.gitignore`). Provider: `AGENT_PROVIDER=openai|gemini`; nếu để trống thì dùng OpenAI khi có key. Model đặt bằng `OPENAI_MODEL` (mặc định `gpt-4.1-mini`).

## Thử thách nâng cao (bonus)

Đã làm trên WHO *World health statistics 2023* (130 trang PDF, có bảng, biểu đồ, bản đồ, sơ đồ). Kết quả **29/30 câu test đạt = 96.7%** (ngưỡng 90%). Xem [advanced/README.md](advanced/README.md) và mục cuối của báo cáo.

## Kết quả nằm ở đâu

- `results/agent/REVIEW_METHOD.md`: quy ước chấm nhãn tay; `results/provider_errors.md`: lỗi provider (Gemini hết quota).
- `results/day6_connection.json`: phiên bản pgvector, số chunk, kiểm tra tương thích embedding.
- `results/retrieval/<split>/`: `summary.md|json`, `traces_<config>.json` (top-10 có ID, trang, section, score, rank, thành phần RRF/rerank, context đã chọn).
- `results/agent/<split>/<config>/`: `traces.json` (mọi model call, tool call, tham số, kết quả, context cuối, câu trả lời, citation, token, chi phí, lỗi), `auto.json`, `reviews.json` (nhãn chấm tay + lý do), `review_sheet.md`, `summary.json`; `results/agent/<split>/summary.md`.
- `data/chunks_para800.json` là bản xuất index `para800` từ pgvector (văn bản công khai của NIST) để chạy BM25; tái tạo bằng `src.export_chunks`.

Không commit `.env`. Mật khẩu trong `DAY6_DATABASE_URL` là mật khẩu Docker local của lab Day 6.
