"""Folding one stored paper into another, once a person has named the survivor.

`reconcile_identifiers` reports two records claiming one identifier and stops,
because choosing between them is a merge. This is the other side of that line,
and the survivor is an argument — the machine still chooses nothing.

**Why it cannot be automatic**, measured on a real archive: a paper filed by
hand and also collected from arXiv ended up with the *reading* on one record and
the *document* on the other. The arXiv record held the PDF and had no summary,
sitting unread in the queue; the hand-filed record had been read and had no
document. Any rule preferring the richer record, or the older, or the one with
more topics, discards something real.

**`data/concepts/` is deliberately untouched.** Evidence is derived — `harvest`
rebuilds it from the summaries every render — so moving the reading *is* how the
entities are repointed. Editing those records here would write derived data by
hand and be undone by the next pass.
"""

from __future__ import annotations

import unittest

from pipelines import render
from pipelines.common.schema import Paper, PaperSummary
from pipelines.common.store import RecordStore, SeenStore
from pipelines.enrich import findings
from pipelines.enrich.dedupe import merge_records, reconcile_identifiers
from pipelines.enrich.queue import Queue

from .sandbox import Sandbox

SLUG = "test-topic"
ARXIV = "arxiv:2503.20314"
LOCAL = "local:94a30c3706dd3819"
TITLE = "Wan: Open and Advanced Video Foundation Models"


class MergeTests(unittest.TestCase):
    """The Wan shape: the reading on one record, the document on the other."""

    def setUp(self):
        self.sandbox = Sandbox()
        self.addCleanup(self.sandbox.close)
        self.cfg = self.sandbox.config()
        self.cfg.layout.ensure()
        self.store = RecordStore(self.cfg.layout)
        self.queue = Queue(self.cfg.layout, cfg=self.cfg)

        # Collected: has the document, never read, still queued.
        self.store.save_paper(
            Paper(id=ARXIV, title=TITLE, source="seed", arxiv_id="2503.20314",
                  pdf_url="https://arxiv.org/pdf/2503.20314",
                  local_path="data/pdfs/arxiv-2503-20314.pdf", topics=[SLUG])
        )
        self.queue.enqueue(
            kind="paper", item_id=ARXIV, topics=[SLUG], language="en",
            instructions="", output_schema={}, payload={},
        )
        # Filed by hand: read, no document.
        self.store.save_paper(
            Paper(id=LOCAL, title=TITLE, source="local", arxiv_id="2503.20314",
                  topics=[SLUG, "second-topic"])
        )
        self.store.save_paper_summary(
            PaperSummary(paper_id=LOCAL, one_liner="It generates video.",
                         relevance={SLUG: "Relevant."}, concepts=["Video Model"])
        )
        with SeenStore(self.cfg.layout.seen_db) as seen:
            seen.mark(ARXIV, kind="paper", canonical=ARXIV, source="seed")
            seen.mark(LOCAL, kind="paper", canonical=LOCAL, source="local")
            seen.mark("title:d00189e0", kind="paper", canonical=LOCAL, source="local")

    def _merge(self, **kwargs):
        return merge_records(self.cfg, ARXIV, LOCAL, **kwargs)

    # -- the shape that makes it manual --------------------------------------
    def test_the_conflict_is_reported_before_anybody_merges(self):
        self.assertGreater(reconcile_identifiers(self.cfg)["conflicts"], 0)

    def test_a_dry_run_reports_and_changes_nothing(self):
        import hashlib

        data = self.cfg.layout.data
        snapshot = lambda: {  # noqa: E731
            p.relative_to(data).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(data.rglob("*")) if p.is_file()
        }
        before = snapshot()
        plan = self._merge(dry_run=True)
        self.assertTrue(plan["summary_moved"])
        self.assertEqual(snapshot(), before)

    def test_a_record_cannot_absorb_itself(self):
        plan = merge_records(self.cfg, ARXIV, ARXIV)
        self.assertTrue(plan["problems"])

    def test_an_unknown_record_is_refused(self):
        plan = merge_records(self.cfg, ARXIV, "arxiv:9999.99999")
        self.assertTrue(plan["problems"])

    # -- what moves ----------------------------------------------------------
    def test_the_reading_moves_to_the_survivor(self):
        """The half the survivor did not have."""
        self._merge()
        summary = RecordStore(self.cfg.layout).load_paper_summary(ARXIV)
        self.assertIsNotNone(summary)
        self.assertEqual(summary.paper_id, ARXIV)
        self.assertIsNone(RecordStore(self.cfg.layout).load_paper_summary(LOCAL))

    def test_the_absorbed_record_is_gone_and_its_fields_are_kept(self):
        self._merge()
        store = RecordStore(self.cfg.layout)
        self.assertIsNone(store.load_paper(LOCAL))
        survivor = store.load_paper(ARXIV)
        self.assertIn("second-topic", survivor.topics, "the wider tagging survived")
        self.assertEqual(survivor.local_path, "data/pdfs/arxiv-2503-20314.pdf")

    def test_every_key_now_resolves_to_the_survivor(self):
        self._merge()
        with SeenStore(self.cfg.layout.seen_db) as seen:
            self.assertEqual(seen.canonical_for([LOCAL]), ARXIV)
            self.assertEqual(seen.canonical_for(["title:d00189e0"]), ARXIV)

    def test_a_finding_naming_the_absorbed_record_is_repointed(self):
        """It is authored, and its validator would reject a vanished id."""
        findings.record(
            self.cfg,
            {"kind": "fact", "statement": "This paper reports a real number.",
             "papers": [LOCAL], "topics": [SLUG]},
            self.store,
        )
        self._merge()
        settled = next(iter(RecordStore(self.cfg.layout).iter_findings()))
        self.assertEqual(settled.papers, [ARXIV])

    def test_the_dead_task_is_removed(self):
        """The survivor is read once this lands; the task can never apply."""
        self._merge()
        self.assertEqual(self.queue.pending_ids(kind="paper"), [])

    # -- what must not move --------------------------------------------------
    def test_concept_records_are_not_edited_by_the_merge(self):
        """Evidence is derived. Moving the reading is how it repoints."""
        render.run(self.cfg, skip_queueing=True)
        before = self.store.load_concept("video-model")
        self.assertEqual(before.evidence[0]["id"], LOCAL)

        self._merge()
        untouched = RecordStore(self.cfg.layout).load_concept("video-model")
        self.assertEqual(untouched.evidence[0]["id"], LOCAL, "merge left it alone")

        render.run(self.cfg, skip_queueing=True)
        rebuilt = RecordStore(self.cfg.layout).load_concept("video-model")
        self.assertEqual([e["id"] for e in rebuilt.evidence], [ARXIV])

    def test_the_entity_stops_counting_the_paper_twice(self):
        """The damage the whole command exists to undo."""
        self.store.save_paper_summary(
            PaperSummary(paper_id=ARXIV, one_liner="Also read.",
                         relevance={SLUG: "Relevant."}, concepts=["Video Model"])
        )
        render.run(self.cfg, skip_queueing=True)
        self.assertEqual(
            self.store.load_concept("video-model").mention_count, 2, "counted twice"
        )

        merge_records(self.cfg, ARXIV, LOCAL)
        render.run(self.cfg, skip_queueing=True)
        self.assertEqual(
            RecordStore(self.cfg.layout).load_concept("video-model").mention_count, 1
        )

    def test_two_readings_are_not_silently_reconciled(self):
        """Which reading is better is a judgement, and this command has a person
        for identity only. It says so rather than choosing."""
        self.store.save_paper_summary(
            PaperSummary(paper_id=ARXIV, one_liner="A different reading.",
                         relevance={SLUG: "Relevant."})
        )
        plan = self._merge(dry_run=True)
        self.assertTrue(plan["summary_kept_apart"])
        self.assertFalse(plan["summary_moved"])

    def test_the_survivor_keeps_its_own_reading_when_both_have_one(self):
        self.store.save_paper_summary(
            PaperSummary(paper_id=ARXIV, one_liner="A different reading.",
                         relevance={SLUG: "Relevant."})
        )
        self._merge()
        self.assertEqual(
            RecordStore(self.cfg.layout).load_paper_summary(ARXIV).one_liner,
            "A different reading.",
        )

    def test_the_conflict_is_gone_afterwards(self):
        self._merge()
        self.assertEqual(reconcile_identifiers(self.cfg)["conflicts"], 0)


if __name__ == "__main__":
    unittest.main()
