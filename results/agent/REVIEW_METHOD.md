# Cách chấm nhãn agent (áp dụng cho mọi `reviews.json` trong `results/agent/`)

- **Người chấm:** nhãn do trợ lý AI (Claude) soạn bằng cách đọc câu trả lời, đáp án chuẩn và toàn văn chunk được trích (`review_sheet.md`). Sinh viên rà soát lại; chưa có người chấm độc lập thứ hai.
- **Grounded answer** (`answer_grade`, chỉ cho câu có đáp án):
  - 2 = đúng và đủ ý chính.
  - 1 = đúng một phần, hoặc thiếu điều kiện chính.
  - 0 = sai, lạc đề hoặc từ chối.
  - Từ chối một câu có đáp án luôn được 0.
- **Citation hỗ trợ** (`citation_support`, một giá trị cho mỗi citation): `true` khi chunk chứa nội dung của ý được trích **và** ý đó trả lời đúng câu hỏi. Nếu ý chính của câu trả lời sai thì citation tính là `false`, dù chunk có chứa nguyên văn các ý phụ.
- **Abstention đúng** (`abstention_correct`, chỉ cho câu thiếu evidence): `true` khi agent từ chối và không thêm khẳng định vô căn cứ.
- Mỗi nhãn có trường `note` ghi lý do. Các số tổng hợp được tính bằng `starter/agent_metrics.py` của đề (không chỉnh sửa), thông qua `src/summarize_agent.py`.
- `A6_seed_category_lookup` trên dev không được chấm tay. A6 chỉ dùng để kiểm tra thoái lui, bằng metric tự động trong `auto.json`; xem báo cáo.
