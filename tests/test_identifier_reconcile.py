"""Identifiers a record gains after it was first registered.

Deduplication resolves an incoming paper against keys recorded at *collection*
time. A hand-filed PDF has none worth having then — the record is created before
anything opens the document, deliberately, so the only key is a fingerprint of
the filename. The arXiv id arrives at `queue complete`, and nothing re-registered
the keys.

So a record sat in the archive holding `arxiv_id: 2503.20314` with no
`arxiv:2503.20314` key, and the day the collector returned that paper it forked
instead of folding: two records for one paper, two archive pages, and every
entity counting it twice. Nothing errored. On the deployment where this was
found, 17 of 22 hand-filed papers carrying an arXiv id were in that state.

The two halves that matter are that a missing key is registered, and that a key
another record already holds is **reported and never repointed** — that is a
duplicate which already exists, and choosing which of the two survives is a
merge decision with a person in it.
"""

from __future__ import annotations

import unittest

from pipelines import render
from pipelines.common.schema import Paper
from pipelines.common.store import RecordStore, SeenStore
from pipelines.enrich.dedupe import Deduplicator, reconcile_identifiers

from .sandbox import Sandbox

SLUG = "test-topic"


class ReconcileTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.addCleanup(self.sandbox.close)
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)

    def _filed(self, **extra) -> Paper:
        """A hand-filed paper as it looks once its reading has been applied."""
        fields = {
            "id": "local:94a30c3706dd3819",
            "title": "Wan: Open and Advanced Video Foundation Models",
            "source": "local",
            "arxiv_id": "2503.20314",
            "local_path": "data/pdfs/local-94a30c3706dd3819.pdf",
            "topics": [SLUG],
        }
        fields.update(extra)
        paper = Paper(**fields)
        self.store.save_paper(paper)
        return paper

    def _keys(self) -> dict[str, str | None]:
        with SeenStore(self.cfg.layout.seen_db) as seen:
            return {
                key: seen.canonical_for([key])
                for key in ("arxiv:2503.20314", "doi:10.1000/x")
            }

    # -- the gap that was open ----------------------------------------------
    def test_an_identifier_learned_from_a_reading_is_registered(self):
        paper = self._filed()
        self.assertIsNone(self._keys()["arxiv:2503.20314"], "nothing knows it yet")

        counts = reconcile_identifiers(self.cfg)

        self.assertEqual(counts["registered"], 3)  # arxiv, title, own id
        self.assertEqual(self._keys()["arxiv:2503.20314"], paper.id)

    def test_the_collector_then_folds_instead_of_forking(self):
        """The consequence, end to end. This is the duplicate that used to appear."""
        filed = self._filed()
        reconcile_identifiers(self.cfg)

        incoming = Paper(
            id="arxiv:2503.20314",
            title="Wan: Open and Advanced Video Foundation Models",
            source="arxiv",
            arxiv_id="2503.20314",
            pdf_url="https://arxiv.org/pdf/2503.20314",
        )
        with SeenStore(self.cfg.layout.seen_db) as seen:
            record, is_new = Deduplicator(seen, self.store).resolve_paper(incoming)

        self.assertFalse(is_new)
        self.assertEqual(record.id, filed.id, "folded onto the record with the reading")
        self.assertEqual(record.local_path, filed.local_path, "and kept its document")

    def test_without_the_pass_it_forks(self):
        """The defect, asserted, so the fix above cannot be mistaken for a no-op."""
        self._filed()
        incoming = Paper(
            id="arxiv:2503.20314", title="Something Else Entirely",
            source="arxiv", arxiv_id="2503.20314",
        )
        with SeenStore(self.cfg.layout.seen_db) as seen:
            _, is_new = Deduplicator(seen, self.store).resolve_paper(incoming)
        self.assertTrue(is_new, "a second record for one paper")

    def test_it_repairs_a_backlog_not_only_the_next_one(self):
        """The readings for these were applied long ago; nothing re-runs them.

        A fix that only registered keys at apply time would prevent the next
        duplicate and close none of the ones already waiting to happen.
        """
        for index in range(5):
            self._filed(
                id=f"local:{index:016x}",
                title=f"A Filed Paper {index}",
                arxiv_id=f"2503.2031{index}",
            )
        counts = reconcile_identifiers(self.cfg)
        self.assertEqual(counts["papers"], 5)

    # -- what it must not do -------------------------------------------------
    def test_a_key_another_record_holds_is_reported_never_repointed(self):
        """Two records already share an identifier. Merging them is a decision."""
        with SeenStore(self.cfg.layout.seen_db) as seen:
            seen.mark("arxiv:2503.20314", kind="paper",
                      canonical="arxiv:2503.20314", source="arxiv")
        self._filed()

        counts = reconcile_identifiers(self.cfg)

        self.assertEqual(counts["conflicts"], 1)
        self.assertEqual(
            self._keys()["arxiv:2503.20314"], "arxiv:2503.20314",
            "the existing owner keeps the key",
        )

    def test_it_is_idempotent(self):
        self._filed()
        first = reconcile_identifiers(self.cfg)
        second = reconcile_identifiers(self.cfg)
        self.assertGreater(first["registered"], 0)
        self.assertEqual(second["registered"], 0)
        self.assertEqual(second["conflicts"], 0)

    def test_it_writes_no_record(self):
        """It touches the index and nothing else."""
        import hashlib

        self._filed()
        papers = self.cfg.layout.papers
        before = {
            p.name: hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(papers.glob("*.json"))
        }
        reconcile_identifiers(self.cfg)
        after = {
            p.name: hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(papers.glob("*.json"))
        }
        self.assertEqual(after, before)

    def test_a_render_runs_it_and_reports_it(self):
        self._filed()
        result = render.run(self.cfg)
        self.assertGreater(result["identifiers"]["registered"], 0)
        self.assertEqual(self._keys()["arxiv:2503.20314"], "local:94a30c3706dd3819")


if __name__ == "__main__":
    unittest.main()
