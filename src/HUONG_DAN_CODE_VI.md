# Hướng dẫn đọc code Day 7 cho người mới

Đây là bản **chú giải theo luồng chạy**, không phải bản sao của mã nguồn. Mỗi mục nói rõ: bắt đầu đọc tại hàm/phương thức nào, đọc đến đâu, dữ liệu đổi thành gì, rồi bấm **Tiếp theo** để sang bước kế tiếp. Các liên kết tên tệp mở đúng tệp nguồn; liên kết “Tiếp theo” cuộn trong tài liệu này.

## Chọn lộ trình trước khi đọc

Day 7 có ba chương trình độc lập. Đừng đọc các tệp theo thứ tự chữ cái.

| Muốn làm gì? | Điểm bắt đầu | Luồng chính |
|---|---|---|
| Hỏi đáp với mô hình AI | [`app.main`](app.py#L113) hoặc [`run_agent.main`](run_agent.py#L77) | cấu hình → retriever → agent → kết quả |
| Đo chất lượng tìm kiếm, chưa gọi LLM | [`eval_retrieval.main`](eval_retrieval.py#L128) | câu hỏi → search → context → metric |
| Chuẩn bị dữ liệu từ Day 6 | [`export_chunks.main`](export_chunks.py) | PostgreSQL → JSON chunks |

Nếu đây là lần đầu đọc, đi theo lộ trình **Hỏi đáp** bên dưới. `main()` là điểm Python chạy khi gõ `python -m src.<tên_tệp>`.

## Bản đồ dữ liệu tối thiểu

```text
question + filter
       ↓
Retriever.search() → [chunk đã xếp hạng]
       ↓
context.pack() → text context + kept_ids + dropped_ids
       ↓
Agent gọi LLM / tool → answer + citations + trace
       ↓
run_agent hoặc app lưu/hiển thị kết quả
```

`chunk` luôn là một `dict` có các khóa quan trọng: `id`, `text`, `source_id`, `page`, `metadata`, `score`, `rank`. Đây là “hợp đồng” chung giữa các tệp; nắm nó trước sẽ bớt rối.

---

## Lộ trình 1 — Chạy agent hỏi đáp

### 1. [`run_agent.main`](run_agent.py#L77) — điểm bắt đầu khi chạy benchmark agent

**Đọc từ:** dòng `def main()` trong `run_agent.py`. **Dừng khi:** biến `traces` đã chứa kết quả của toàn bộ câu hỏi.

- `argparse` nhận `--config` và `--split` từ terminal.
- `CONFIGS[args.config]` lấy một `AgentConfig`: nó quy định cách truy hồi, số chunk, ngân sách context và số lượt tìm tối đa.
- `load_questions()` đọc câu hỏi. `public_question()` cố ý bỏ `gold`; agent không được nhìn đáp án chuẩn.
- Vòng `for q in questions` gọi `agent.run(...)` từng câu. Sau đó `write_json()` lưu trace và metric.

Ví dụ, `A6_seed_category_lookup` không phải tên ma thuật: đó chỉ là một cấu hình bật `seed_original` và `category_lookup`.

**Tiếp theo:** [`2. common.load_questions và public_question`](#2-commonload_questions-và-public_question).

### 2. [`common.load_questions`](common.py#L63) và [`common.public_question`](common.py#L69) — nạp input an toàn

**Đọc từ:** `load_questions(split)`. **Dừng khi:** có danh sách câu hỏi chỉ thuộc `dev` hoặc `test`.

- `load_questions` đọc JSON tại `benchmark/questions.json`, rồi lọc theo `split`.
- Mỗi câu đầy đủ có `gold` dùng để chấm điểm, nhưng `public_question` chỉ trả `id`, `question`, `filter`.
- Vì thế, retriever và LLM chỉ nhận thứ mà người dùng có thể cung cấp; điều này tránh “lộ đáp án” khi đánh giá.

Các hàm nền trong cùng tệp: `setting()` đọc biến môi trường, `load_chunks()` đọc bản xuất JSON, `write_json()` ghi kết quả. `is_evidence_hit()` chỉ dùng sau khi chạy để đối chiếu với `gold`.

**Tiếp theo:** [`3. retrievers.build_retriever`](#3-retrieversbuild_retriever--chọn-công-cụ-tìm-kiếm).

### 3. [`retrievers.build_retriever`](retrievers.py#L155) — chọn công cụ tìm kiếm

**Đọc từ:** `build_retriever(method, index, **kw)`. **Dừng khi:** nhận về một đối tượng có phương thức `search(query, filters, top_k)`.

- `dense` tạo `DenseRetriever`: tìm bằng vector trong PostgreSQL.
- `bm25` tạo `BM25Retriever`: tìm bằng từ khóa.
- `hybrid` ghép hai bảng xếp hạng bằng RRF.
- `*_rerank` lấy nhiều ứng viên trước, rồi dùng cross-encoder sắp lại.

`Retriever` là `Protocol`, nghĩa là một “giao kèo kiểu dữ liệu”: bất kỳ lớp nào có `name` và `search` đúng dạng đều dùng được.

**Tiếp theo:** [`4. các retriever.search`](#4-các-retrieversearch--tạo-danh-sách-chunk-đã-xếp-hạng).

### 4. Các `retriever.search` — tạo danh sách chunk đã xếp hạng

**Đọc từ:** một trong các phương thức `search`. **Dừng khi:** kết quả có `score`, `rank`, `method`.

1. [`DenseRetriever.search`](retrievers.py#L64) biến câu hỏi thành vector rồi gọi `Day6Store.dense_search`. Độ giống cosine cao hơn thì đứng trước.
2. [`BM25Retriever.__init__`](retrievers.py#L72) chuẩn bị chỉ mục từ: token, tần suất (`tf`), IDF và độ dài chunk. [`BM25Retriever.scores`](retrievers.py#L84) tính điểm; [`search`](retrievers.py#L96) lọc rồi sắp giảm dần.
3. [`HybridRetriever.search`](retrievers.py#L105) gọi cả Dense lẫn BM25. Mỗi chunk nhận `1 / (rrf_k + rank)` từ mỗi danh sách; cộng lại thì không cần ép hai loại điểm về cùng thang đo.
4. [`RerankRetriever.search`](retrievers.py#L142) xin nhiều ứng viên từ retriever gốc, dùng [`CrossEncoderReranker.score`](retrievers.py#L129) chấm cặp `(query, text)`, rồi chỉ giữ `top_k`.

Hàm nhỏ cần biết: `tokenize()` bỏ stopword cho BM25; `_passes()` áp filter như `{"function": "MAP"}`; `_ranked()` gắn số hạng nhất quán.

**Tiếp theo (nhánh dense):** [`5. day6_store`](#5-day6_store--nối-với-vector-store-day-6).  
**Tiếp theo (sau khi đã có chunk):** [`6. agent.GeminiAgent.run`](#6-agentgeminiagentrun--một-phiên-trả-lời-hoàn-chỉnh).

### 5. [`day6_store.Day6Store.dense_search`](day6_store.py#L103) — nối với vector store Day 6

**Đọc từ:** `QueryEmbedder.shared()` trước, sau đó `Day6Store.dense_search()`. **Dừng khi:** hàng cơ sở dữ liệu được đổi thành chunk Day 7.

- `QueryEmbedder` tải EmbeddingGemma một lần và cache nó. `embed_query(text)` trả danh sách 768 số (vector) đã chuẩn hóa.
- `_vec()` đổi danh sách số thành cú pháp vector PostgreSQL.
- `dense_search()` chỉ cho phép các filter nằm trong `FILTER_COLUMNS`; nó ghép điều kiện SQL có tham số, tìm `top_k` gần nhất với toán tử pgvector `<=>`.
- `to_chunk(row)` là ranh giới quan trọng: chuyển một hàng SQL thành schema chunk mà phần còn lại hiểu.

Không có kết quả giả ở đây: lỗi database/model được ném lên để trace của agent ghi trạng thái `error`.

**Tiếp theo:** [`6. agent.GeminiAgent.run`](#6-agentgeminiagentrun--một-phiên-trả-lời-hoàn-chỉnh).

### 6. [`agent.GeminiAgent.run`](agent.py#L172) — một phiên trả lời hoàn chỉnh

**Đọc từ:** `run(qid, question, user_filter)`. **Dừng khi:** hàm trả về `trace`.

- Hàm tạo `trace` ngay đầu tiên. Trace giữ input, event, câu trả lời, citation, token, chi phí và thời gian; nhờ vậy chạy lỗi vẫn có dữ liệu để kiểm tra.
- `try: self._loop(...)` là phần làm việc chính. Nếu provider/database lỗi, `except` đổi trạng thái thành `error`, chứ không bịa câu trả lời.
- Cuối hàm tính chi phí ước lượng, tổng lượt search và thời gian, rồi `return trace`.

Trước khi vào vòng lặp, đọc `AgentConfig`: đây là gói tham số truyền xuyên suốt. `provider()`, `default_model()`, `prices()` lấy cấu hình từ `.env`; `system_prompt()` tạo luật cho mô hình; `tool_declarations()` khai báo hai “nút” LLM được phép bấm: `search_documents` và `submit_answer`.

**Tiếp theo:** [`7. GeminiAgent._loop`](#7-geminiagent_loop--vòng-lặp-llm--tool).

### 7. [`GeminiAgent._loop`](agent.py#L199) — vòng lặp LLM ↔ tool

**Đọc từ:** `_loop(question, user_filter, trace)`. **Dừng khi:** mô hình gọi `submit_answer`, hoặc vòng lặp ném lỗi.

1. `_opening()` tạo prompt đầu tiên và có thể tìm trước một lượt nếu bật `seed_original`/`category_lookup`.
2. `contents` là lịch sử hội thoại gửi cho API.
3. Mỗi lượt, `allowed` chỉ cho search khi chưa chạm `max_searches`; sau đó LLM buộc phải submit đáp án.
4. `_generate()` gọi model, ghi token và event `model_call` vào trace.
5. Nếu tool là `submit_answer`, gọi `_finish()` rồi kết thúc. Nếu là `search_documents`, gọi `_search()`, đóng gói phản hồi tool vào `contents`, và lặp lại.

Đây là lý do agent không trả lời tự do ngay từ đầu: cấu hình function calling buộc nó lấy bằng chứng trước.

**Tiếp theo:** [`8. _opening, _search và context.pack`](#8-_opening-_search-và-contextpack--đưa-bằng-chứng-vào-llm).

### 8. `_opening`, `_search` và [`context.pack`](context.py#L20) — đưa bằng chứng vào LLM

**Đọc từ:** `_opening()` rồi `_search()` trong `agent.py`. **Dừng khi:** một phản hồi `search_documents` được thêm vào lịch sử hội thoại.

- `_opening()` tạo lời nhắc “hãy dùng tool”. Nếu cấu hình bật tra mã như `MAP 1`, nó gọi `CategoryLookup.search()` để lấy toàn bộ mục đúng mã; nếu bật `seed_original`, nó tìm bằng chính câu hỏi trước lượt LLM đầu tiên.
- `_search()` gộp filter người dùng với `function_filter` do model đề nghị, gọi `retriever.search()`, rồi tự áp ngân sách context lên các kết quả mới. (Hàm này không gọi `pack()` vì nó cần giữ `shown` và ngân sách cộng dồn giữa nhiều lượt tìm.)
- [`context.render`](context.py#L15) in chunk với header chứa `id`, nguồn, trang và section; nhờ vậy mô hình có thể trích dẫn chính xác.
- `pack()` dùng cho benchmark retrieval: duyệt theo thứ hạng, bỏ ID trùng, cộng số ký tự và **không cắt nửa chunk**. Nó trả `(context, kept_ids, dropped_ids)`.
- `with_neighbours()` chỉ được benchmark context dùng: chèn đoạn ngay sau cùng trang để tránh mất phần tiếp của một ý.

**Tiếp theo:** [`9. _generate và _finish`](#9-_generate-và-_finish--gọi-api-và-kiểm-tra-citation).

### 9. `_generate` và `_finish` — gọi API và kiểm tra citation

**Đọc từ:** `_generate(contents, allowed)` trong `GeminiAgent`, sau đó `_finish(args, shown, trace)`. **Dừng khi:** `trace["status"]`, `answer` và `citations` đã được chốt.

- `_generate()` gửi system prompt, tool declaration và danh sách tool được phép. Khi lỗi 429/500/503, nó retry có thời gian chờ tăng dần nhưng dừng nếu phải chờ quá lâu.
- `_finish()` không đánh giá ngữ nghĩa câu trả lời. Nó chỉ kiểm tra quy tắc máy có thể kiểm tra chắc chắn: trạng thái hợp lệ, có citation khi `answered`, citation đã từng xuất hiện trong context, và marker `[chunk-id]` có trong câu trả lời.
- Citation hợp lệ bị thiếu marker sẽ được thêm marker và ghi event; citation không nằm trong context sẽ biến câu trả lời thành trạng thái `abstain` với lý do từ chối trong trace.

`OpenAIAgent` có cùng giao diện với `GeminiAgent`; [`make_agent`](agent.py#L464) chọn lớp đúng theo `config.provider`. Vì cùng trả trace, các phần gọi phía trên không phải đổi.

**Tiếp theo:** [`10. auto_metrics và lưu kết quả`](#10-auto_metrics-và-lưu-kết-quả).

### 10. [`run_agent.auto_metrics`](run_agent.py#L50) và `write_json` — chấm tự động, không chấm “hay/dở”

**Đọc từ:** `auto_metrics(questions, traces, chunks_by_id)`. **Dừng khi:** `summary` được ghi vào `results/agent/...`.

- Hàm chỉ đếm trạng thái, lượt tool, token, chi phí và bằng chứng có xuất hiện trong context hay không.
- `is_evidence_hit()` mới được phép đọc `gold` ở giai đoạn này.
- Chất lượng lập luận/câu văn vẫn cần người chấm qua `review_sheet.py` và `summarize_agent.py`.

**Kết thúc lộ trình agent.** Có thể quay về [`Chọn lộ trình`](#chọn-lộ-trình-trước-khi-đọc) hoặc xem lộ trình benchmark dưới đây.

---

## Lộ trình 2 — Benchmark retrieval, không gọi LLM

### 1. [`eval_retrieval.main`](eval_retrieval.py#L128) → `run`

`main()` nhận split/cấu hình rồi gọi [`run`](eval_retrieval.py#L58). `run()` tải câu hỏi + chunks, tạo các retriever dùng chung, warm-up dense model, và lặp qua từng config/câu hỏi.

**Tiếp theo:** [`2. truy hồi và chọn context`](#2-truy-hồi-và-chọn-context).

### 2. Truy hồi và chọn context

Trong mỗi câu hỏi, `retr.search(...)` trả top 10, `sel = ranked[:ctx_k]` chọn số chunk định đưa vào context, tùy chọn `with_neighbours`, rồi `pack(sel, budget)` áp giới hạn ký tự. Xem diễn giải của các hàm này tại [Lộ trình agent, bước 4](#4-các-retrieversearch--tạo-danh-sách-chunk-đã-xếp-hạng) và [bước 8](#8-_opening-_search-và-contextpack--đưa-bằng-chứng-vào-llm).

**Tiếp theo:** [`3. metric và tệp kết quả`](#3-metric-và-tệp-kết-quả).

### 3. Metric và tệp kết quả

Chỉ với câu `answerable`, `is_evidence_hit()` tạo `hit1`, `hit3`, `hit5`, `rr10`, `context_hit`. Với câu không trả lời được, code chỉ ghi `top1_score`. Cuối mỗi config, `run()` tính tổng, ghi `traces_<config>.json`, `summary.json` và bảng `summary.md`.

**Kết thúc lộ trình benchmark.**

---

## Lộ trình 3 — Web UI cục bộ

### 1. [`app.main`](app.py#L113) → khởi động server

`main()` đọc tham số port, tải chunks vào `_chunks`, có thể warm-up một agent, rồi tạo `ThreadingHTTPServer` chỉ lắng nghe `127.0.0.1`. Chạy bằng `python -m src.app`.

**Tiếp theo:** [`2. Handler.do_GET và do_POST`](#2-handlerdo_get-và-do_post).

### 2. `Handler.do_GET` và `do_POST`

- `do_GET` trả HTML hoặc danh sách cấu hình.
- `do_POST` kiểm tra JSON input, giới hạn độ dài câu hỏi, xác nhận tên config/filter, rồi gọi `agent.run()`.
- Sau khi có trace, `chunk_view()` thêm text cho các citation/context ID để giao diện hiển thị; log tóm tắt được nối vào `results/ui_log.jsonl`.

`get_agent()` cache agent theo config; `_run_lock` bảo đảm một instance agent chỉ chạy một lượt tại một thời điểm.

**Tiếp theo:** [`3. quay lại agent.run`](#6-agentgeminiagentrun--một-phiên-trả-lời-hoàn-chỉnh).

---

## Các tệp hỗ trợ chưa nằm trên đường chạy chính

| Tệp | Bắt đầu đọc | Nó làm gì |
|---|---|---|
| [`export_chunks.py`](export_chunks.py) | `main()` | Xuất chunks từ `Day6Store.all_chunks()` ra JSON; cần làm trước BM25/CategoryLookup. |
| [`eval_probe.py`](eval_probe.py) | `main()` | Đo riêng câu hỏi dạng mã category/subcategory. |
| [`review_sheet.py`](review_sheet.py) | `main()` | Biến trace thành bảng Markdown để người chấm đọc bằng chứng. |
| [`summarize_agent.py`](summarize_agent.py) | `main()` | Gộp các nhãn chấm tay thành tóm tắt. |

## Gợi ý đọc thực hành

Đặt hai cửa sổ cạnh nhau: bên trái là tài liệu này, bên phải là tệp nguồn được liên kết. Đọc đúng một mục, đặt breakpoint/`print` ở hàm đó, chạy với `--only` một `query_id`, rồi mới bấm **Tiếp theo**. Cách này giúp thấy dữ liệu thực tế thay đổi thay vì chỉ đọc lý thuyết.
