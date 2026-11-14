# Lỗi provider khi chạy agent

## Gemini free tier hết quota (2026-11-14, khoảng 07:30–07:40 UTC)

- **Model:** `gemini-2.5-flash` qua Google AI Studio, endpoint `v1beta`.
- **Triệu chứng:** lượt chạy dev đầu tiên đứng lại. Agent nhận lỗi 429 và chờ theo `retryDelay` do server trả về (khoảng 21 phút), nên tôi dừng lượt chạy. Lượt đó **không** sinh kết quả nào trong `results/`.
- **Thông báo lỗi** (rút gọn, không chứa key):
  `429 RESOURCE_EXHAUSTED … Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 20, model: gemini-2.5-flash … Generate content requests per day limit exceeded on Free Tier … Please retry in 21m35s`
- **Xử lý:**
  - Thêm giới hạn chờ: nếu provider yêu cầu chờ quá 90 giây thì ghi `status: error` thay vì treo (`MAX_RETRY_WAIT_S` trong `src/agent.py`).
  - Thêm provider OpenAI (`OpenAIAgent`) và chạy toàn bộ benchmark bằng `gpt-4.1-mini`.
  - Không dùng kết quả Gemini nào để so sánh.
- `gemini-3.5-flash` cũng được thử một lần và trả `RemoteProtocolError: Server disconnected without sending a response`, nên cũng không dùng.

## OpenAI `gpt-4.1-mini`

Không có lỗi provider nào trong các lượt chạy dev, test và bộ kiểm tra riêng (`errors: []` trong mọi `auto.json`).
