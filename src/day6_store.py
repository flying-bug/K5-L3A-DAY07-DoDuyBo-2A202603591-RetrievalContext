"""Read-only connection to the Day 6 vector store (PostgreSQL 16 + pgvector) and its embedder.

Day 6 table `chunks` (see Day 6 starter/src/store.py):
    index_name, chunk_id, document_id, source, page, part, section, function, text,
    content_sha256, metadata jsonb, embedding_model, embedding vector(768)
Two indexes live in that table: `para800` (paragraph chunks, Day 6 strategy B/C) and
`fixed800o100` (fixed windows, strategy A).

The query embedder must match the index: EmbeddingGemma-300m, normalized vectors, query prompt
"task: search result | query: " (sentence-transformers `encode_query`). `check_compatibility`
re-embeds stored chunks and compares them with the stored vectors to prove this.
Errors (DB down, wrong dims) are raised, never replaced with fake results.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from .common import ROOT, setting

FILTER_COLUMNS = {"function", "part", "section", "page", "document_id"}


def default_model_path() -> str:
    return setting("EMBEDDING_MODEL", str(ROOT.parent / "models" / "embeddinggemma-300m"))


class QueryEmbedder:
    _cache: dict[str, "QueryEmbedder"] = {}

    def __init__(self, model_path: str | None = None):
        from sentence_transformers import SentenceTransformer

        self.model_path = model_path or default_model_path()
        self.model = SentenceTransformer(self.model_path, device="cpu")
        get_dims = getattr(self.model, "get_embedding_dimension", None) or \
            getattr(self.model, "get_sentence_embedding_dimension")
        self.dimensions = int(get_dims())
        self.name = Path(self.model_path).name

    @classmethod
    def shared(cls) -> "QueryEmbedder":
        key = default_model_path()
        if key not in cls._cache:
            cls._cache[key] = cls(key)
        return cls._cache[key]

    def embed_query(self, text: str) -> list[float]:
        return self.model.encode_query([text], normalize_embeddings=True, convert_to_numpy=True)[0].tolist()

    def embed_documents(self, texts: list[str]):
        return self.model.encode_document(texts, normalize_embeddings=True, convert_to_numpy=True)

    def info(self) -> dict[str, Any]:
        import sentence_transformers
        import torch

        return {"model": self.name, "path": self.model_path, "dimensions": self.dimensions,
                "query_prompt": self.model.prompts.get("query"),
                "document_prompt": self.model.prompts.get("document"),
                "sentence_transformers": sentence_transformers.__version__, "torch": torch.__version__}


def _vec(v: list[float]) -> str:
    return "[" + ",".join(f"{x:.7g}" for x in v) + "]"


class Day6Store:
    def __init__(self, database_url: str | None = None):
        self.database_url = database_url or setting("DAY6_DATABASE_URL")

    def _connect(self):
        import psycopg

        return psycopg.connect(self.database_url, connect_timeout=5)

    def versions(self) -> dict[str, Any]:
        with self._connect() as conn:
            pg = conn.execute("SELECT current_setting('server_version')").fetchone()[0]
            ext = conn.execute("SELECT extversion FROM pg_extension WHERE extname='vector'").fetchone()[0]
            dims = conn.execute("SELECT format_type(atttypid, atttypmod) FROM pg_attribute "
                                "WHERE attrelid='chunks'::regclass AND attname='embedding'").fetchone()[0]
            rows = conn.execute("SELECT index_name, count(*), count(DISTINCT chunk_id), "
                                "array_agg(DISTINCT embedding_model) FROM chunks GROUP BY index_name "
                                "ORDER BY index_name").fetchall()
        return {"postgresql": pg, "pgvector": ext, "embedding_column": dims,
                "indexes": {r[0]: {"rows": r[1], "distinct_ids": r[2], "embedding_model": r[3]} for r in rows}}

    def all_chunks(self, index: str) -> list[dict[str, Any]]:
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT chunk_id, document_id, source, page, part, section, function, text, metadata "
                "FROM chunks WHERE index_name = %s ORDER BY document_id, page, chunk_id", (index,)).fetchall()
        if not rows:
            raise RuntimeError(f"index {index!r} is empty in the Day 6 database")
        return [to_chunk(r) for r in rows]

    def stored_vectors(self, index: str, chunk_ids: list[str]) -> dict[str, list[float]]:
        import json

        with self._connect() as conn:
            rows = conn.execute("SELECT chunk_id, embedding::text FROM chunks WHERE index_name=%s "
                                "AND chunk_id = ANY(%s)", (index, chunk_ids)).fetchall()
        return {r[0]: json.loads(r[1]) for r in rows}

    def dense_search(self, index: str, qvec: list[float], top_k: int,
                     filters: dict[str, Any] | None = None) -> list[dict[str, Any]]:
        """Exact cosine search in pgvector (same SQL ordering as Day 6)."""
        where, params = ["index_name = %s"], [index]
        for key, value in (filters or {}).items():
            if key not in FILTER_COLUMNS:
                raise ValueError(f"filter on {key!r} is not allowed")
            where.append(f"{key} = %s")
            params.append(value)
        q = _vec(qvec)
        sql = ("SELECT chunk_id, document_id, source, page, part, section, function, text, metadata, "
               f"1 - (embedding <=> %s::vector) AS score FROM chunks WHERE {' AND '.join(where)} "
               "ORDER BY embedding <=> %s::vector, chunk_id LIMIT %s")
        with self._connect() as conn:
            rows = conn.execute(sql, [q, *params, q, top_k]).fetchall()
        return [{**to_chunk(r[:9]), "score": float(r[9])} for r in rows]


def to_chunk(row) -> dict[str, Any]:
    """DB row -> Day 7 chunk contract (id, text, source_id, source, page, metadata)."""
    chunk_id, document_id, source, page, part, section, function, text, metadata = row
    meta = dict(metadata or {})
    meta.update({"part": part, "section": section, "function": function})
    return {"id": chunk_id, "text": text, "source_id": document_id, "source": source,
            "page": page, "metadata": meta}
