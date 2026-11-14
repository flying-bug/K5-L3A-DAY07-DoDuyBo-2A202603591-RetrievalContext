# Tiêu chí chọn cấu hình (ghi 2026-11-14, trước khi xem kết quả agent trên dev và trước mọi lần chạy test)

## Retrieval (không LLM, đã chạy trên dev lúc 07:22 UTC)

Thứ tự ưu tiên: (1) Evidence Hit@3 trên dev cao hơn → (2) Context Evidence Rate → (3) MRR@10 → (4) ít thành phần hơn / latency thấp hơn.

Kết quả dev: `hybrid_rerank_f` và `dense_rerank_f` hòa ở (1)–(3) (22/22, 22/22, 0.886). Theo (4), chọn **`dense_rerank_f`**: không cần BM25, latency trung vị 942 ms so với 968 ms. Cấu hình này làm retrieval tool cho các agent A1/A3. A2 giữ biến thể hybrid để đo trên agent.

## Agent (chạy trên dev với cùng model `gpt-4.1-mini`, temperature 0)

Đây là thứ tự áp dụng cho A0–A3:

1. **Grounded answer trung bình /2** trên các câu dev có đáp án, chấm tay theo BENCHMARK.md: cao hơn là tốt hơn.
2. **Abstention đúng** trên câu thiếu evidence (cao hơn), rồi **từ chối nhầm** trên câu có đáp án (thấp hơn).
3. **Context Evidence Rate** của context cuối: cao hơn là tốt hơn.
4. **Latency trung vị**, rồi **chi phí**: thấp hơn là tốt hơn.

Chênh lệch nhỏ hơn hoặc bằng 1 câu ở một tiêu chí được coi là hòa; khi đó xét tiêu chí tiếp theo.
Baseline cố định là **A0_dense**, tức chiến lược C của Day 6 dùng làm tool. Test chỉ chạy **A0 và cấu hình được chọn**, mỗi cấu hình đúng một lần, sau khi `results/selection.json` đã được ghi.
