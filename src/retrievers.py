"""Retrieval methods. Every retriever returns ranked chunks in the Day 7 contract:
{id, text, source_id, source, page, metadata, score, rank, method}.

- DenseRetriever   : EmbeddingGemma query vector -> exact cosine in the Day 6 pgvector store.
- BM25Retriever    : Okapi BM25 (k1=1.5, b=0.75) over the same chunks, exported from that store.
- HybridRetriever  : Reciprocal Rank Fusion of dense + BM25 rankings (rank-based, so the two score
                     scales never need to be compared): score = sum 1/(rrf_k + rank).
- RerankRetriever  : any candidate retriever, then a cross-encoder rescoring (query, chunk) pairs.

Filters are user-supplied metadata (e.g. {"function": "MEASURE"}); all retrievers apply the same
exact-match semantics. No retriever ever sees benchmark gold.
"""
from __future__ import annotations

import math
import re
from collections import Counter
from typing import Any, Protocol

from .common import load_chunks
from .day6_store import Day6Store, QueryEmbedder

TOKEN_RE = re.compile(r"\w+", re.UNICODE)
# Short English stopword list: BM25 idf already down-weights them, this only trims noise.
STOP = set("a an the of to in on for and or is are be by with as at from that this what which who how "
           "does do did should must can may it its into under within about".split())


def tokenize(text: str) -> list[str]:
    return [t for t in TOKEN_RE.findall(text.lower()) if t not in STOP]


def _passes(chunk: dict[str, Any], filters: dict[str, Any] | None) -> bool:
    if not filters:
        return True
    for key, value in filters.items():
        actual = chunk["metadata"].get(key, chunk.get(key))
        if key == "document_id":
            actual = chunk["source_id"]
        if actual != value:
            return False
    return True


def _ranked(rows: list[dict[str, Any]], method: str) -> list[dict[str, Any]]:
    return [{**r, "rank": i, "method": method} for i, r in enumerate(rows, start=1)]


class Retriever(Protocol):
    name: str

    def search(self, query: str, *, filters: dict[str, Any] | None, top_k: int) -> list[dict[str, Any]]:
        ...


class DenseRetriever:
    def __init__(self, index: str = "para800", store: Day6Store | None = None,
                 embedder: QueryEmbedder | None = None):
        self.index = index
        self.store = store or Day6Store()
        self.embedder = embedder or QueryEmbedder.shared()
        self.name = f"dense[{index}]"

    def search(self, query, *, filters=None, top_k=3):
        rows = self.store.dense_search(self.index, self.embedder.embed_query(query), top_k, filters)
        return _ranked(rows, "dense")


class BM25Retriever:
    def __init__(self, index: str = "para800", chunks: list[dict[str, Any]] | None = None,
                 k1: float = 1.5, b: float = 0.75):
        self.chunks = chunks if chunks is not None else load_chunks(index)
        self.k1, self.b = k1, b
        self.tf = [Counter(tokenize(c["text"])) for c in self.chunks]
        self.len = [sum(t.values()) for t in self.tf]
        self.avgdl = sum(self.len) / len(self.len)
        df = Counter(term for t in self.tf for term in t)
        n = len(self.chunks)
        self.idf = {t: math.log(1 + (n - f + 0.5) / (f + 0.5)) for t, f in df.items()}
        self.name = f"bm25[{index}]"

    def scores(self, query: str) -> list[float]:
        terms = [t for t in tokenize(query) if t in self.idf]
        out = []
        for tf, dl in zip(self.tf, self.len):
            s = 0.0
            for t in terms:
                f = tf.get(t, 0)
                if f:
                    s += self.idf[t] * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * dl / self.avgdl))
            out.append(s)
        return out

    def search(self, query, *, filters=None, top_k=3):
        scored = [(s, c) for s, c in zip(self.scores(query), self.chunks) if s > 0 and _passes(c, filters)]
        scored.sort(key=lambda x: (-x[0], x[1]["id"]))
        return _ranked([{**c, "score": s} for s, c in scored[:top_k]], "bm25")


class HybridRetriever:
    def __init__(self, dense: DenseRetriever, bm25: BM25Retriever, depth: int = 50, rrf_k: int = 60):
        self.dense, self.bm25, self.depth, self.rrf_k = dense, bm25, depth, rrf_k
        self.name = f"hybrid_rrf[{dense.index},depth={depth},k={rrf_k}]"

    def search(self, query, *, filters=None, top_k=3):
        lists = {"dense": self.dense.search(query, filters=filters, top_k=self.depth),
                 "bm25": self.bm25.search(query, filters=filters, top_k=self.depth)}
        fused: dict[str, dict[str, Any]] = {}
        for name, rows in lists.items():
            for r in rows:
                entry = fused.setdefault(r["id"], {**{k: v for k, v in r.items()
                                                       if k not in ("score", "rank", "method")},
                                                   "score": 0.0, "components": {}})
                entry["score"] += 1.0 / (self.rrf_k + r["rank"])
                entry["components"][name] = {"rank": r["rank"], "score": round(r["score"], 6)}
        rows = sorted(fused.values(), key=lambda r: (-r["score"], r["id"]))[:top_k]
        return _ranked(rows, "hybrid_rrf")


class CrossEncoderReranker:
    _cache: dict[str, Any] = {}

    def __init__(self, model_name: str = "cross-encoder/mmarco-mMiniLMv2-L12-H384-v1"):
        from sentence_transformers import CrossEncoder

        if model_name not in self._cache:
            self._cache[model_name] = CrossEncoder(model_name, device="cpu", max_length=512)
        self.model = self._cache[model_name]
        self.model_name = model_name

    def score(self, query: str, texts: list[str]) -> list[float]:
        return [float(s) for s in self.model.predict([(query, t) for t in texts], batch_size=16)]


class RerankRetriever:
    def __init__(self, base: Retriever, reranker: CrossEncoderReranker, candidates: int = 20):
        self.base, self.reranker, self.candidates = base, reranker, candidates
        short = reranker.model_name.split("/")[-1]
        self.name = f"rerank[{short}]({base.name},n={candidates})"

    def search(self, query, *, filters=None, top_k=3):
        cands = self.base.search(query, filters=filters, top_k=self.candidates)
        if not cands:
            return []
        scores = self.reranker.score(query, [c["text"] for c in cands])
        rows = []
        for c, s in zip(cands, scores):
            rows.append({**{k: v for k, v in c.items() if k not in ("score", "rank", "method")},
                         "score": s, "first_stage": {"rank": c["rank"], "score": round(c["score"], 6),
                                                     "method": c["method"]}})
        rows.sort(key=lambda r: (-r["score"], r["first_stage"]["rank"]))
        return _ranked(rows[:top_k], "rerank")


def build_retriever(method: str, index: str = "para800", **kw) -> Retriever:
    """Factory used by the CLIs and the agent: dense | bm25 | hybrid | hybrid_rerank | dense_rerank."""
    if method == "dense":
        return DenseRetriever(index)
    if method == "bm25":
        return BM25Retriever(index)
    if method == "hybrid":
        return HybridRetriever(DenseRetriever(index), BM25Retriever(index), depth=kw.get("depth", 50))
    if method in ("hybrid_rerank", "dense_rerank"):
        base = (HybridRetriever(DenseRetriever(index), BM25Retriever(index), depth=kw.get("depth", 50))
                if method == "hybrid_rerank" else DenseRetriever(index))
        return RerankRetriever(base, CrossEncoderReranker(kw.get("reranker", "cross-encoder/mmarco-mMiniLMv2-L12-H384-v1")),
                               candidates=kw.get("candidates", 20))
    raise ValueError(f"unknown retrieval method {method!r}")


# --------------------------------------------------------------------------- structural lookup (A6)
CODE_RE = re.compile(r"\b(GOVERN|MAP|MEASURE|MANAGE)\s*(\d{1,2})(?:\s*\.\s*(\d{1,2}))?\b", re.IGNORECASE)


def parse_codes(text: str) -> list[tuple[str, int, int | None]]:
    """Category / subcategory codes the user wrote, e.g. 'map 1' -> ('MAP', 1, None),
    'MEASURE 2.6' -> ('MEASURE', 2, 6). Read from the question text only (never from gold)."""
    out: list[tuple[str, int, int | None]] = []
    for m in CODE_RE.finditer(text):
        code = (m.group(1).upper(), int(m.group(2)), int(m.group(3)) if m.group(3) else None)
        if code not in out:
            out.append(code)
    return out


class CategoryLookup:
    """Exact lookup of AI RMF Core table entries ('MAP 1:', 'MAP 1.3:') in the Day 6 chunks.

    A category spans several para800 chunks (MAP 1 = 3 chunks, MEASURE 2 = 4), and only the first
    one carries the category title, so similarity search tends to return just that one. This
    returns every chunk holding an entry of the requested category (or the one subcategory), in
    document order. Chunks come from data/chunks_<index>.json, the export of the pgvector table.
    """

    def __init__(self, index: str = "para800", chunks: list[dict[str, Any]] | None = None):
        self.chunks = chunks if chunks is not None else load_chunks(index)
        self.name = f"category_lookup[{index}]"

    def search(self, code: tuple[str, int, int | None]) -> list[dict[str, Any]]:
        func, cat, sub = code
        tail = rf"\.{sub}:" if sub is not None else r"(?:\.\d+)?:"
        pat = re.compile(rf"\b{func} {cat}{tail}")
        rows = [{**c, "score": 1.0} for c in self.chunks if pat.search(c["text"])]
        return _ranked(rows, "category_lookup")
