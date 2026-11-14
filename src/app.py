"""Local Q&A web UI for the Day 7 agent (standard library HTTP server, no extra dependencies).

Run:  python -m src.app [--port 8077]   then open http://127.0.0.1:8077
Endpoints
  GET  /              the page (src/web/index.html)
  GET  /api/configs   agent configurations that can be chosen in the UI
  POST /api/ask       {"question": str, "config": str, "function": "GOVERN|MAP|MEASURE|MANAGE"|null}
                      -> full agent trace + cited chunk texts
Each answered question is appended to results/ui_log.jsonl (question, config, status, citations,
latency, cost) so UI sessions stay auditable. Binds to 127.0.0.1 only.
"""
from __future__ import annotations

import argparse
import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from .agent import GeminiAgent, make_agent  # noqa: F401  (GeminiAgent: type of cached agents)
from .common import RESULTS, load_chunks, now_iso, utf8_stdout
from .retrievers import build_retriever
from .run_agent import CONFIGS

WEB = Path(__file__).resolve().parent / "web"
FUNCTIONS = {"GOVERN", "MAP", "MEASURE", "MANAGE"}
_lock = threading.Lock()
_run_lock = threading.Lock()
_agents: dict[str, GeminiAgent] = {}
_chunks: dict[str, dict] = {}


def get_agent(name: str) -> GeminiAgent:
    with _lock:  # retrievers/models are loaded once and reused
        if name not in _agents:
            cfg = CONFIGS[name]
            _agents[name] = make_agent(cfg, build_retriever(cfg.retrieval, cfg.index))
        return _agents[name]


def chunk_view(cid: str) -> dict:
    c = _chunks.get(cid)
    if not c:
        return {"id": cid}
    return {"id": cid, "page": c["page"], "section": c["metadata"].get("section"),
            "function": c["metadata"].get("function"), "text": c["text"]}


class Handler(BaseHTTPRequestHandler):
    def _send(self, code: int, body: bytes, ctype: str) -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _json(self, code: int, obj) -> None:
        self._send(code, json.dumps(obj, ensure_ascii=False).encode("utf-8"), "application/json; charset=utf-8")

    def log_message(self, fmt, *args):  # quieter console
        print(f"[ui] {self.address_string()} {fmt % args}", flush=True)

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self._send(200, (WEB / "index.html").read_bytes(), "text/html; charset=utf-8")
        elif self.path == "/api/configs":
            self._json(200, [{"name": n, "retrieval": c.retrieval, "top_k": c.top_k, "budget_chars": c.budget_chars,
                              "max_searches": c.max_searches, "provider": c.provider, "model": c.model}
                             for n, c in CONFIGS.items()])
        else:
            self._json(404, {"error": "not found"})

    def do_POST(self):
        if self.path != "/api/ask":
            return self._json(404, {"error": "not found"})
        try:
            length = int(self.headers.get("Content-Length") or 0)
            if length > 20_000:
                return self._json(413, {"error": "request too large"})
            body = json.loads(self.rfile.read(length) or b"{}")
            question = str(body.get("question") or "").strip()
            name = body.get("config") or "A6_seed_category_lookup"
            func = body.get("function") or None
            if not question or len(question) > 1000:
                return self._json(400, {"error": "Câu hỏi rỗng hoặc dài quá 1000 ký tự."})
            if name not in CONFIGS:
                return self._json(400, {"error": f"Cấu hình không hợp lệ: {name}"})
            if func is not None and func not in FUNCTIONS:
                return self._json(400, {"error": f"Filter không hợp lệ: {func}"})
            agent = get_agent(name)
            with _run_lock:  # GeminiAgent keeps per-run state; answer one question at a time
                trace = agent.run("ui", question, {"function": func} if func else None)
        except Exception as e:  # report, never fake an answer
            return self._json(500, {"error": f"{type(e).__name__}: {e}"})
        trace["cited_chunks"] = [chunk_view(c) for c in trace.get("citations", [])]
        trace["context_chunks"] = [chunk_view(c) for c in trace.get("context_ids", [])]
        trace.pop("context", None)
        with _lock:
            RESULTS.mkdir(parents=True, exist_ok=True)
            with open(RESULTS / "ui_log.jsonl", "a", encoding="utf-8") as f:
                f.write(json.dumps({"at": now_iso(), "question": question, "config": name, "filter": func,
                                    "status": trace["status"], "citations": trace["citations"],
                                    "n_searches": trace["n_searches"], "elapsed_ms": trace["elapsed_ms"],
                                    "cost_usd": trace["cost_usd"], "error": trace.get("error"),
                                    "rejection": trace.get("rejection"),
                                    "markers_appended": any(e["event"] == "citation_markers_appended"
                                                            for e in trace["events"])},
                                   ensure_ascii=False) + "\n")
        self._json(200, trace)


def main() -> None:
    utf8_stdout()
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8077)
    ap.add_argument("--warm", default="A6_seed_category_lookup", help="config to load at start ('' = lazy)")
    args = ap.parse_args()
    _chunks.update({c["id"]: c for c in load_chunks("para800")})
    if args.warm:
        print(f"[ui] loading {args.warm} (embedding model, reranker) ...", flush=True)
        try:
            get_agent(args.warm)
        except Exception as e:  # e.g. missing API key: still serve the page, report on ask
            print(f"[ui] warm-up failed, will retry on first question: {type(e).__name__}: {e}", flush=True)
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    print(f"[ui] ready on http://127.0.0.1:{args.port}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
