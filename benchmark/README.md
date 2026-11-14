# Benchmark Day 7 — NIST AI RMF 1.0 (NIST AI 100-1)

File: [`questions.json`](questions.json) — 34 câu, JSON array UTF-8.

| Split | Có đáp án | Thiếu evidence | Tổng |
|---|---:|---:|---:|
| dev | 22 (`q01`–`q22`) | 3 (`u01`–`u03`) | 25 |
| test | 8 (`t01`–`t08`) | 3 (`u04`–`u06`) | 11 |

## Nguồn câu hỏi và lý do chia lại split

- `q01`–`q22` lấy nguyên từ benchmark Day 6 (`day6_split` ghi split cũ). Toàn bộ **chuyển sang dev** vì test Day 6 (`q17`–`q22`) đã bị xem kết quả chi tiết trong báo cáo Day 6 và trong bài phụ hybrid (chọn `q18`, `q19` để phân tích BM25/RRF). Dùng lại làm test sẽ không còn độc lập (RULES: "nếu đã xem test để chỉnh, tạo test mới").
- `t01`–`t08` là **test mới**, viết 2026-11-14 *trước mọi lần chạy retrieval/agent Day 7*, từ các trang chưa có câu hỏi nào (p10, 14, 18, 21, 24, 29, 32, 41). Loại câu: direct, conditional, paraphrase, paraphrase_vi (câu hỏi tiếng Việt, tài liệu tiếng Anh), filter (GOVERN, MAP).
- Câu thiếu evidence `u01`–`u06` gần chủ đề (ngưỡng accuracy, số tổ chức góp ý, watermark, EU AI Act, LLM được đánh giá, chi phí triển khai). `absence_check` ghi cách kiểm tra **trên toàn bộ 48 trang PDF** bằng grep (không dựa vào top-k).
- Chốt file trước thí nghiệm: `sha256 = 798f1934bd42f69540f9b4f3a69f0f88d987b7ed0fb516501224d72995081f64` (chỉ sửa ghi chú trang của `u05` từ 43 → 39 trước khi chạy; không đổi câu hỏi/đáp án).

## Schema

- Câu có đáp án: `id, split, day6_split, type, answerable: true, question, expected_answer, gold: [{source_id, page, evidence}], filter`. Các phần tử của `gold` là evidence **thay thế** (q06 có 2 vị trí hợp lệ: p17 và p8). Mỗi evidence nằm trọn trong một chunk `para800` (dev: 22/22, xem `results/day6_connection.json`).
- Câu thiếu evidence: `id, split, type: "unanswerable", answerable: false, expected_behavior: "search_and_abstain", absence_reason, absence_check, filter: null`.
- `page` là trang vật lý PDF (1-based), trùng với cột `page` trong pgvector Day 6.
- `filter` (`{"function": "GOVERN|MAP|MEASURE|MANAGE"}`) là thông tin **người dùng cung cấp trước**, lấy từ chính câu chữ của câu hỏi ("Under the GOVERN function, …"); không suy ra từ gold.

## Cách chấm

- **Hit@1 / Evidence Hit@3**: chunk ở hạng 1 / trong top-3 có `source_id` + `page` khớp một phần tử `gold` **và** chứa trọn câu evidence sau chuẩn hóa (NFKC, chữ thường, chỉ giữ `[a-z0-9]`) — giống hệt Day 6. Mẫu số = số câu có đáp án.
- **Context Evidence Rate**: context cuối gửi cho model chứa ít nhất một chunk evidence hit (mọi câu ở đây cần đúng 1 đoạn evidence).
- Câu thiếu evidence không vào mẫu số retrieval metrics; được chấm bằng abstention.
- Grounded answer 0/1/2, citation support và abstention: chấm tay theo BENCHMARK.md, lưu ở `results/agent/*/reviews.json` kèm lý do.
- `gold` chỉ được đọc trong code đánh giá (`src/eval_retrieval.py`, `src/summarize_agent.py`); retriever và agent chỉ nhận `question` và `filter`.
