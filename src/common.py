"""Shared paths, config loading, gold matching and small helpers for Day 7.

Gold matching follows Day 6 exactly (starter/src/textmatch.py there): a chunk is an evidence hit
when its source_id and page equal a gold entry AND it contains the whole evidence quote after
normalization (NFKC, lowercase, keep only [a-z0-9]). The `gold` field is only ever read by the
evaluation code, never by retrievers or the agent.
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
BENCH = ROOT / "benchmark" / "questions.json"
RESULTS = ROOT / "results"

_NON_ALNUM = re.compile(r"[^0-9a-z]+")


def load_env() -> None:
    from dotenv import load_dotenv

    load_dotenv(ROOT / ".env")


def setting(name: str, default: str | None = None) -> str:
    load_env()
    value = os.getenv(name) or default
    if value is None:
        raise RuntimeError(f"{name} is not set: copy .env.example to .env and fill it in")
    return value


def utf8_stdout() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def normalize_for_match(text: str) -> str:
    return _NON_ALNUM.sub("", unicodedata.normalize("NFKC", text).lower())


def is_evidence_hit(chunk: dict[str, Any], gold: list[dict[str, Any]]) -> bool:
    text = normalize_for_match(chunk["text"])
    return any(chunk["source_id"] == g["source_id"] and chunk["page"] == g["page"]
               and normalize_for_match(g["evidence"]) in text for g in gold)


def load_questions(split: str) -> list[dict[str, Any]]:
    """split = dev | test | all. Test must only be read after the config is frozen."""
    qs = json.loads(BENCH.read_text(encoding="utf-8"))
    return [q for q in qs if split == "all" or q["split"] == split]


def public_question(q: dict[str, Any]) -> dict[str, Any]:
    """What the system is allowed to see: question text and a user-supplied filter. No gold."""
    return {"id": q["id"], "question": q["question"], "filter": q.get("filter")}


def load_chunks(index: str = "para800") -> list[dict[str, Any]]:
    path = DATA / f"chunks_{index}.json"
    if not path.exists():
        raise FileNotFoundError(f"{path} missing: run `python -m src.export_chunks` first")
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class Timer:
    def __enter__(self):
        self.t0 = time.perf_counter()
        return self

    def __exit__(self, *exc):
        self.ms = (time.perf_counter() - self.t0) * 1000
