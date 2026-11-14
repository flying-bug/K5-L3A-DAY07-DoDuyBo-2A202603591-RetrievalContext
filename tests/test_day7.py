"""Offline checks for the Day 7 code (src/). Fakes here only test plumbing, never quality."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.agent import AgentConfig, GeminiAgent  # noqa: E402
from src.common import is_evidence_hit, normalize_for_match  # noqa: E402
from src.context import pack, with_neighbours  # noqa: E402
from src.retrievers import BM25Retriever, CategoryLookup, HybridRetriever, RerankRetriever, parse_codes  # noqa: E402


def chunk(i, text, page=1, function=None):
    return {"id": f"c{i}", "text": text, "source_id": "doc", "source": "doc.pdf", "page": page,
            "metadata": {"function": function, "section": "s"}}


CHUNKS = [chunk(1, "Risk tolerance refers to readiness to bear the risk.", 1),
          chunk(2, "GOVERN accountability: executive leadership takes responsibility.", 2, "GOVERN"),
          chunk(3, "MEASURE: independent assessors and domain experts take part in assessments.", 3, "MEASURE"),
          chunk(4, "Residual risk is risk remaining after treatment.", 3)]


class FakeDense:
    index, name = "fake", "dense[fake]"

    def __init__(self, order):
        self.order = order

    def search(self, query, *, filters=None, top_k=3):
        rows = [c for c in CHUNKS if c["id"] in self.order]
        rows.sort(key=lambda c: self.order.index(c["id"]))
        if filters:
            rows = [c for c in rows if c["metadata"].get("function") == filters.get("function")]
        return [{**c, "score": 1.0 - 0.1 * i, "rank": i + 1, "method": "dense"} for i, c in enumerate(rows[:top_k])]


class FakeReranker:
    model_name = "fake/reranker"

    def score(self, query, texts):
        return [float("assess" in t) for t in texts]


class RetrievalTests(unittest.TestCase):
    def test_bm25_ranks_lexical_match_and_applies_filter(self):
        bm = BM25Retriever(chunks=CHUNKS)
        self.assertEqual(bm.search("risk tolerance", top_k=1)[0]["id"], "c1")
        res = bm.search("risk", filters={"function": "MEASURE"}, top_k=5)
        self.assertTrue(all(r["metadata"]["function"] == "MEASURE" for r in res))
        self.assertEqual(bm.search("zzzz", top_k=3), [])

    def test_rrf_fusion_is_rank_based_and_unique(self):
        hy = HybridRetriever(FakeDense(["c4", "c1", "c2"]), BM25Retriever(chunks=CHUNKS), depth=10)
        res = hy.search("risk tolerance", top_k=3)
        self.assertEqual(len({r["id"] for r in res}), len(res))
        self.assertEqual(res[0]["id"], "c1")  # rank 2 dense + rank 1 bm25 beats rank 1 dense only
        self.assertEqual([r["rank"] for r in res], [1, 2, 3])
        self.assertIn("dense", res[0]["components"])

    def test_rerank_reorders_candidates_and_keeps_first_stage(self):
        rr = RerankRetriever(FakeDense(["c1", "c2", "c3"]), FakeReranker(), candidates=3)
        res = rr.search("who assesses", top_k=2)
        self.assertEqual(res[0]["id"], "c3")
        self.assertEqual(res[0]["first_stage"]["rank"], 3)


TABLE = [chunk("t1", "Table 2. MAP 1: Context is established.\n\nMAP 1.1: Purposes are documented.", 31, "MAP"),
         chunk("t2", "MAP 1.2: Interdisciplinary actors.\n\nMAP 1.5: Risk tolerances are determined.", 31, "MAP"),
         chunk("t3", "MAP 1.6: System requirements.\n\nMAP 2: Categorization is performed.", 31, "MAP"),
         chunk("t4", "MAP 10: not a real category. The MAP function establishes context.", 32, "MAP"),
         chunk("t5", "MEASURE 2.6: The AI system is evaluated regularly for safety risks.", 35, "MEASURE")]


class CategoryLookupTests(unittest.TestCase):
    def test_parse_codes_from_question_text(self):
        self.assertEqual(parse_codes("tất cả thông tin liên quan đến map 1"), [("MAP", 1, None)])
        self.assertEqual(parse_codes("MEASURE 2.6 và GOVERN 2?"), [("MEASURE", 2, 6), ("GOVERN", 2, None)])
        self.assertEqual(parse_codes("Under the MAP function, what ..."), [])

    def test_lookup_returns_whole_category_or_one_subcategory(self):
        lk = CategoryLookup(chunks=TABLE)
        self.assertEqual([r["id"] for r in lk.search(("MAP", 1, None))], ["ct1", "ct2", "ct3"])
        self.assertEqual([r["id"] for r in lk.search(("MAP", 1, 6))], ["ct3"])
        self.assertEqual([r["id"] for r in lk.search(("MEASURE", 2, 6))], ["ct5"])
        self.assertEqual(lk.search(("MAP", 3, None)), [])  # 'MAP 10:' must not match 'MAP 1'


class ContextTests(unittest.TestCase):
    def test_pack_dedups_skips_oversized_and_respects_budget(self):
        ctx, kept, dropped = pack([CHUNKS[0], CHUNKS[0], CHUNKS[1]], budget=90)
        self.assertEqual(kept, ["c1"])
        self.assertEqual(dropped, ["c2"])
        self.assertLessEqual(len(ctx), 90)
        self.assertIn("[c1 | doc | page 1 | s]", ctx)

    def test_neighbour_only_on_same_page(self):
        out = with_neighbours([CHUNKS[2]], CHUNKS, top_n=1)
        self.assertEqual([c["id"] for c in out], ["c3", "c4"])
        self.assertEqual(with_neighbours([CHUNKS[1]], CHUNKS, top_n=1)[-1]["id"], "c2")

    def test_gold_hit_needs_page_and_full_quote(self):
        gold = [{"source_id": "doc", "page": 1, "evidence": "readiness to bear the RISK"}]
        self.assertTrue(is_evidence_hit(CHUNKS[0], gold))
        self.assertFalse(is_evidence_hit({**CHUNKS[0], "page": 2}, gold))
        self.assertEqual(normalize_for_match("Regu-\nlatory’s"), "regulatorys")


class AgentGuardTests(unittest.TestCase):
    def make(self, budget=400):
        agent = object.__new__(GeminiAgent)  # no API client: only deterministic helpers are tested
        agent.cfg = AgentConfig(name="t", top_k=3, budget_chars=budget, max_searches=2, model="none")
        agent.retriever = FakeDense(["c1", "c2", "c3"])
        return agent

    def test_search_dedups_and_enforces_budget(self):
        agent, trace, shown = self.make(budget=200), {"events": []}, {}
        payload, used = agent._search({"query": "q"}, None, shown, 0, trace)
        self.assertLessEqual(used, 200)
        self.assertTrue(trace["events"][0]["dropped_budget"])
        payload, used = agent._search({"query": "q"}, None, shown, used, trace)
        self.assertEqual(payload["results"], [])
        self.assertIn("already shown", payload["note"])

    def test_user_filter_wins_over_model_filter(self):
        agent, trace = self.make(), {"events": []}
        agent._search({"query": "q", "function_filter": "MEASURE"}, {"function": "GOVERN"}, {}, 0, trace)
        self.assertEqual(trace["events"][0]["filter"], {"function": "GOVERN"})

    def test_answer_needs_citations_from_shown_context(self):
        agent = self.make()
        shown = {"c1": CHUNKS[0]}
        ok = {"events": []}
        agent._finish({"status": "answered", "answer": "Readiness [c1]", "citations": ["c1"]}, shown, ok)
        self.assertEqual(ok["status"], "answered")
        for bad, reason in (({"status": "answered", "answer": "x [c9]", "citations": ["c9"]}, "citation_not_in_context"),
                            ({"status": "answered", "answer": "x [doc:p9:c1]", "citations": []}, "citation_not_in_context"),
                            ({"status": "answered", "answer": "Readiness [c1]", "citations": ["c1", "c7"]}, "citation_not_in_context"),
                            ({"status": "answered", "answer": "uncited", "citations": []}, "no_citations")):
            tr = {"events": []}
            agent._finish(bad, shown, tr)
            self.assertEqual(tr["status"], "abstain")
            self.assertEqual(tr["citations"], [])
            self.assertEqual(tr["rejection"]["reason"], reason)

    def test_model_filter_can_be_disabled(self):
        agent, trace = self.make(), {"events": []}
        agent.cfg.model_filter = False
        agent._search({"query": "q", "function_filter": "MEASURE"}, None, {}, 0, trace)
        ev = trace["events"][0]
        self.assertIsNone(ev["filter"])  # model's filter ignored, recorded for audit
        self.assertEqual(ev["model_function_filter"], "MEASURE")

    def test_seed_search_uses_question_verbatim_and_counts(self):
        agent, trace = self.make(budget=2000), {"events": []}
        agent.cfg.seed_original = True
        prompt, shown, used, searches = agent._opening("What is risk tolerance?", None, trace)
        self.assertEqual(searches, 1)
        self.assertEqual(trace["events"][0]["tool"], "seed_original_query")
        self.assertEqual(trace["events"][0]["query"], "What is risk tolerance?")
        self.assertIn("c1", shown)
        self.assertIn('"id": "c1"', prompt)
        agent.cfg.seed_original = False
        _, shown2, _, searches2 = agent._opening("q", None, {"events": []})
        self.assertEqual((searches2, shown2), (0, {}))

    def test_category_lookup_adds_every_entry_before_model_turn(self):
        agent, trace = self.make(budget=5000), {"events": []}
        agent.cfg.category_lookup = True
        agent._category_lookup = CategoryLookup(chunks=TABLE)
        prompt, shown, used, searches = agent._opening("map 1 gồm những gì?", None, trace)
        self.assertEqual(list(shown), ["ct1", "ct2", "ct3"])  # all MAP 1 chunks, document order
        self.assertEqual(searches, 0)  # does not consume the model's search budget
        self.assertEqual(trace["events"][0]["tool"], "category_lookup")
        self.assertIn("All AI RMF Core table entries for MAP 1", prompt)
        _, shown2, _, _ = agent._opening("What is risk?", None, {"events": []})  # no code -> no lookup
        self.assertEqual(shown2, {})

    def test_missing_inline_marker_is_appended_and_logged(self):
        agent = self.make()
        shown = {"c1": CHUNKS[0], "doc:p1:c2": CHUNKS[1]}
        tr = {"events": []}
        agent._finish({"status": "answered", "answer": "Readiness to bear risk.", "citations": ["c1"]}, shown, tr)
        self.assertEqual(tr["status"], "answered")
        self.assertTrue(tr["answer"].endswith("[c1]"))
        self.assertIn("citation_markers_appended", [e["event"] for e in tr["events"]])
        tr = {"events": []}  # "(id)" for an in-context id becomes "[id]", nothing appended
        agent._finish({"status": "answered", "answer": "Accountability (doc:p1:c2).", "citations": ["doc:p1:c2"]},
                      shown, tr)
        self.assertEqual(tr["answer"], "Accountability [doc:p1:c2].")
        self.assertNotIn("citation_markers_appended", [e["event"] for e in tr["events"]])
        tr = {"events": []}  # inline-only citation (not listed) is picked up
        agent._finish({"status": "answered", "answer": "Accountability [doc:p1:c2].", "citations": []}, shown, tr)
        self.assertEqual((tr["status"], tr["citations"]), ("answered", ["doc:p1:c2"]))
        tr = {"events": []}
        agent._finish({"status": "insufficient_evidence", "answer": "not stated", "citations": []}, shown, tr)
        self.assertEqual(tr["status"], "abstain")


if __name__ == "__main__":
    unittest.main()
