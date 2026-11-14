# Thử thách nâng cao — WHO *World health statistics 2023*

Báo cáo kết quả: [report/individual/2A202603591_DoDuyBo.md](../report/individual/2A202603591_DoDuyBo.md#thử-thách-nâng-cao-nếu-thực-hiện).

## Tài liệu

| Mục | Giá trị |
|---|---|
| Tên | *World health statistics 2023: monitoring health for the SDGs, sustainable development goals* — World Health Organization |
| ISBN / phiên bản | 978-92-4-007432-3 (bản điện tử), xuất bản 19/05/2023 |
| Bản gốc | https://www.who.int/publications/i/item/9789240074323 · PDF: https://www.who.int/docs/default-source/gho-documents/world-health-statistic-reports/2023/world-health-statistics-2023_20230519_.pdf |
| Kiểm chứng file | 130 trang PDF (ix + 119 trang in), 13 621 128 byte, SHA-256 `30cbc640d72082c4dec1ae5c0c66b6438686013b2554432d5f5621c9618deb0b` |
| Quyền sử dụng | CC BY-NC-SA 3.0 IGO (dùng phi thương mại, ghi nguồn). **Không commit PDF**; tải lại bằng lệnh bên dưới. Phần trích xuất trong `cache/` và `data/chunks_whs2023.json` là trích dẫn phục vụ học tập, có ghi nguồn |
| Số trang in | = trang PDF − 10 (trang PDF 11–128) |

Nội dung: text (3 chương), **44 hình** (15 biểu đồ đường, 15 biểu đồ cột/cột chồng, 6 bản đồ, dòng thời gian, sơ đồ Venn, biểu đồ vành khuyên, bảng xếp hạng…) và **4 bảng phụ lục** (Annex 1, trang PDF 94–125, 16 cặp trang trái/phải, 819 dòng quốc gia/khu vực).

## Cách chạy lại

```bash
mkdir advanced\source
curl -L -o advanced/source/who_whs2023.pdf "https://www.who.int/docs/default-source/gho-documents/world-health-statistic-reports/2023/world-health-statistics-2023_20230519_.pdf"
.venv\Scripts\python -m pip install pymupdf
.venv\Scripts\python advanced/build_index.py
.venv\Scripts\python advanced/run_bench.py --config W2_hybrid_rerank_images --split dev
```

`build_index.py` kiểm tra SHA-256 của PDF trước khi chạy. Lời gọi vision được cache trong `advanced/cache/`, nên chạy lại không tốn API. Cần Docker pgvector của Day 6 và `OPENAI_API_KEY` trong `.env`.

## Pipeline index

| Nội dung | Cách xử lý | Kiểm chứng với bản gốc |
|---|---|---|
| Text (trang 4–91, 93, 126–129) | Block text của PDF (`pymupdf`), bỏ header/footer/số trang, gom ≤900 ký tự trong từng trang | Lớp text gốc của PDF (không OCR) |
| 44 hình | Vùng hình = từ caption "Figure x.y" (nằm trên hình) đến dòng "Source:"; lưu `bbox` (điểm PDF). Chunk = mô tả JSON do `gpt-4.1-mini` đọc ảnh crop 200 dpi + chữ có sẵn trong vùng hình (trục, chú giải, nhãn số) | `cache/figures/*.json`; mô tả có thể sai nên khi trả lời, agent được gửi **ảnh crop gốc** của hình; mẫu đối chiếu ở mục dưới |
| 4 bảng phụ lục | Giá trị lấy **tất định** từ toạ độ chữ PDF; ghép trang trái (tên nước) với trang phải theo thứ tự dòng, kiểm tra khoảng cách dòng khớp; giữ ký hiệu chú thích. Tên cột do vision đọc dải tiêu đề, bắt buộc khớp số cột | 16/16 cặp trang khớp số dòng và khoảng cách; tên cột của 8 nửa bảng đối chiếu bằng mắt (sửa số hiệu SDG ở trang 111 theo trang 113); dòng Chad, Viet Nam, Global so khớp ảnh trang 95/101 |
| Không index | Trang 1–3, 11, 42, 43, 81, 92, 130: bìa, trang trắng, trang ngăn chương (chỉ ảnh trang trí, không có thông tin) | Ghi trong `results/index_stats.json` |

Lưu trữ: cùng bảng pgvector của Day 6, `index_name='whs2023'`, cùng EmbeddingGemma-300m (768 chiều); bản xuất `data/chunks_whs2023.json` cho BM25. Chỉ các dòng của index này bị thay thế; dữ liệu Day 6 không đổi.

## Benchmark

[`benchmark/questions.json`](benchmark/questions.json), chốt lúc 2026-11-14T10:01Z trước mọi lần chạy agent, SHA-256 `85b844b4fbbc8bcf3e7455fdec6147869a28d7f5016d1d9fae725e374826d0b8`.

| Split | Bảng | Ảnh/sơ đồ | Biểu đồ | Multi-hop | Text | Thiếu bằng chứng | Tổng |
|---|---:|---:|---:|---:|---:|---:|---:|
| dev | 3 | 3 | 3 | 3 | 4 | 4 | 20 |
| test | 6 | 5 | 5 | 4 | 4 | 6 | 30 |

Mỗi câu ghi trang PDF, trang in, vị trí (bảng/dòng/cột, hình/vùng, đoạn text), giá trị và phép tính. Câu thiếu bằng chứng ghi cách kiểm tra trên toàn văn (regex trên cả 130 trang). Đáp án được viết bằng cách đọc **ảnh trang gốc và lớp text gốc**, không dùng nội dung do model trích xuất.

## Chạy và chấm

`run_bench.py` lưu cho từng câu: trace tool call, query, kết quả, context, ảnh đã gửi, câu trả lời, citation, thời gian, token, chi phí và lỗi. Nhãn đạt/không đạt kèm lý do được chấm tay vào `results/<split>/<config>/labels.json`, theo luật của ADVANCED.md.
