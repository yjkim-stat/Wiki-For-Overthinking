"""A PDF filed by hand for a paper the archive already holds.

Two things are true at once in this path and neither is obvious. The person's
file is the original — `collect/local_pdf.py` says filing it *is* the editorial
decision, and `collect/pdf_fetch.py` says a hand-filed document is never
re-fetched. And the record it belongs to already exists, so deduplication folds
the incoming paper into the stored one.

Folding used to drop `local_path`, which meant the archive knew it held a
hand-filed paper — `source` merges, so `is_local` stayed true — and did not know
where the file was. The document guard in `pdf_fetch` tests exactly the field
that had been dropped, so it did not fire, and the pipeline downloaded the same
paper again and left the filed copy claimed by nobody.

`migration/README.md` files hand-filed PDFs under `irreplaceable`: "Gone
permanently. Somebody chose these and put them in the inbox; no URL was ever
recorded." Orphaning one is the most expensive thing this pipeline can do to a
file, and it did it without a warning anywhere.
"""

from __future__ import annotations

import unittest

from pipelines.collect import pdf_fetch
from pipelines.common.schema import Paper
from pipelines.common.store import RecordStore, SeenStore
from pipelines.enrich.dedupe import Deduplicator, merge_papers

from .sandbox import Sandbox

FILED = "data/pdfs/local-abc123.pdf"
SHELVED = "data/pdfs/read/local-abc123.pdf"


class ExplodingClient:
    """Any request at all is the failure under test."""

    def get(self, url, params=None, headers=None):  # noqa: D102
        raise AssertionError(f"fetched {url} for a paper that already had a document")


class MergeKeepsTheDocumentTests(unittest.TestCase):
    def test_a_filed_document_survives_the_merge(self):
        stored = Paper(id="arxiv:2401.00001", title="A Paper", source="arxiv")
        incoming = Paper(
            id="local:abc123", title="A Paper", source="local", local_path=FILED
        )
        self.assertEqual(merge_papers(stored, incoming).local_path, FILED)

    def test_a_stored_document_is_not_replaced(self):
        """The stored path may already have been shelved.

        `shelve_documents` moves a document to `data/pdfs/read/` once its
        reading is applied and rewrites the record to match. Taking the
        newcomer's path here would point the record back at a file that is no
        longer at that name.
        """
        stored = Paper(
            id="arxiv:2401.00001", title="A Paper", source="arxiv", local_path=SHELVED
        )
        incoming = Paper(
            id="local:abc123", title="A Paper", source="local", local_path=FILED
        )
        self.assertEqual(merge_papers(stored, incoming).local_path, SHELVED)

    def test_a_merge_with_no_document_either_side_stays_empty(self):
        stored = Paper(id="arxiv:2401.00001", title="A Paper", source="arxiv")
        incoming = Paper(id="arxiv:2401.00001", title="A Paper", source="openreview")
        self.assertEqual(merge_papers(stored, incoming).local_path, "")

    def test_the_record_still_reads_as_hand_filed(self):
        """The half that always worked, asserted so the pair cannot drift.

        `source` merging while `local_path` did not is what made the bug look
        survivable: the archive said it held a hand-filed paper and could not
        say where it was.
        """
        stored = Paper(id="arxiv:2401.00001", title="A Paper", source="arxiv")
        incoming = Paper(
            id="local:abc123", title="A Paper", source="local", local_path=FILED
        )
        merged = merge_papers(stored, incoming)
        self.assertTrue(merged.is_local)
        self.assertEqual(merged.source, "arxiv+local")


class NothingIsDownloadedTwiceTests(unittest.TestCase):
    """The consequence, at the guard that was supposed to prevent it."""

    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)

    def tearDown(self):
        self.sandbox.close()

    def test_a_merged_hand_filed_paper_is_not_fetched(self):
        stored = Paper(
            id="arxiv:2401.00001",
            title="A Paper",
            source="arxiv",
            pdf_url="https://arxiv.org/pdf/2401.00001",
        )
        self.store.save_paper(stored)

        incoming = Paper(
            id="local:abc123",
            title="A Paper",
            source="local",
            local_path=FILED,
        )
        with SeenStore(self.cfg.layout.seen_db) as seen:
            seen.mark("arxiv:2401.00001", kind="paper", canonical="arxiv:2401.00001",
                      source="arxiv")
            record, _ = Deduplicator(seen, self.store).resolve_paper(incoming)

        counts = pdf_fetch.fetch_for(self.cfg, [record], ExplodingClient())
        self.assertEqual(counts["fetched"], 0)
        self.assertEqual(record.local_path, FILED)


if __name__ == "__main__":
    unittest.main()
