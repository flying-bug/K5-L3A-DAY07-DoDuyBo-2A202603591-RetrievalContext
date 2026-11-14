"""Context selection: dedup, budget (characters, including the header line), optional neighbours.

Each block is rendered as
    [chunk-id | source | page N | section]
    text
so every sentence the model sees carries its citation ID and source/page.
Chunks that do not fit the remaining budget are skipped (never truncated), so an evidence quote is
either fully present or absent; the trace records which IDs were dropped.
"""
from __future__ import annotations

from typing import Any


def render(chunk: dict[str, Any]) -> str:
    section = (chunk.get("metadata") or {}).get("section") or ""
    return f"[{chunk['id']} | {chunk['source_id']} | page {chunk['page']} | {section}]\n{chunk['text']}"


def pack(chunks: list[dict[str, Any]], budget: int, sep: str = "\n\n") -> tuple[str, list[str], list[str]]:
    """Greedy in the given order. Returns (context, kept_ids, dropped_ids)."""
    blocks, kept, dropped, seen, used = [], [], [], set(), 0
    for c in chunks:
        if c["id"] in seen:
            continue
        seen.add(c["id"])
        block = render(c)
        extra = len(block) + (len(sep) if blocks else 0)
        if used + extra <= budget:
            blocks.append(block)
            kept.append(c["id"])
            used += extra
        else:
            dropped.append(c["id"])
    return sep.join(blocks), kept, dropped


def with_neighbours(ranked: list[dict[str, Any]], all_chunks: list[dict[str, Any]], top_n: int = 1) -> list[dict[str, Any]]:
    """Insert the next chunk on the same page right after each of the top_n results (para chunks
    can split a list from its lead sentence). Order: r1, r1+1, r2, r2+1, ... then the rest."""
    pos = {c["id"]: i for i, c in enumerate(all_chunks)}
    out: list[dict[str, Any]] = []
    for i, r in enumerate(ranked):
        out.append(r)
        if i < top_n and r["id"] in pos:
            j = pos[r["id"]] + 1
            if j < len(all_chunks):
                nxt = all_chunks[j]
                if nxt["source_id"] == r["source_id"] and nxt["page"] == r["page"]:
                    out.append({**nxt, "neighbour_of": r["id"]})
    return out
