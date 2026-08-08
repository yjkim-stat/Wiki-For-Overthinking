"""Hand-filed PDFs: ingestion, and the reading that fills in the blanks.

The collector never opens a PDF, so these tests use a few bytes with a PDF
header rather than a real document — everything under test is about identity,
where the file ends up, and what the reader is allowed to change afterwards.
"""

from __future__ import annotations

import unittest

from pipelines import render
from pipelines.collect import local_pdf
from pipelines.common.schema import Paper
from pipelines.common.store import RecordStore
from pipelines.enrich.queue import Queue, validate_result

from .sandbox import Sandbox

SLUG = "test-topic"
PDF_BYTES = b"%PDF-1.4\n1 0 obj\n<< /Type /Catalog >>\nendobj\ntrailer\n%%EOF\n"


class IngestTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()

    def tearDown(self):
        self.sandbox.close()

    def _drop(self, name: str, data: bytes = PDF_BYTES):
        path = self.cfg.layout.inbox / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return path

    def _collect(self, **kwargs):
        return local_pdf.collect(self.cfg, self.cfg.topics, **kwargs)

    def test_inbox_drains_into_the_store(self):
        dropped = self._drop("some-paper.pdf")
        papers = self._collect()

        self.assertEqual(len(papers), 1)
        self.assertFalse(dropped.exists(), "the inbox must drain, or the next run re-ingests")
        stored = self.cfg.layout.pdfs / f"{papers[0].id.replace(':', '-')}.pdf"
        self.assertTrue(stored.exists())
        self.assertEqual(stored.read_bytes(), PDF_BYTES)

    def test_identity_is_the_content_not_the_name(self):
        self._drop("one-name.pdf")
        first = self._collect()[0]
        self._drop("a-completely-different-name.pdf")
        second = self._collect()[0]
        self.assertEqual(first.id, second.id)

    def test_different_content_is_a_different_paper(self):
        self._drop("a.pdf")
        first = self._collect()[0]
        self._drop("b.pdf", PDF_BYTES + b"more")
        second = self._collect()[0]
        self.assertNotEqual(first.id, second.id)

    def test_record_carries_the_filename_and_the_stored_path(self):
        self._drop("latent_confounding-and-more.pdf")
        paper = self._collect()[0]
        self.assertEqual(paper.title, "latent confounding and more")
        self.assertEqual(paper.source, "local")
        self.assertEqual(paper.source_id, "latent_confounding-and-more.pdf")
        self.assertTrue(paper.local_path.startswith("data/pdfs/"))
        self.assertTrue(paper.is_local)

    def test_dry_run_leaves_the_inbox_alone(self):
        dropped = self._drop("keep-me.pdf")
        papers = self._collect(dry_run=True)
        self.assertEqual(len(papers), 1)
        self.assertTrue(dropped.exists(), "a dry run must not move somebody's file")
        self.assertFalse(any(self.cfg.layout.pdfs.glob("*.pdf")))

    def test_non_pdf_files_are_left_where_they_are(self):
        note = self.cfg.layout.inbox / "notes.txt"
        note.write_text("not a paper", encoding="utf-8")
        self.assertEqual(self._collect(), [])
        self.assertTrue(note.exists())

    def test_nested_folders_are_searched(self):
        self._drop("2024/reading-group/paper.pdf")
        self.assertEqual(len(self._collect()), 1)

    def test_disabled_source_ingests_nothing(self):
        self.cfg.sources["local"] = {"enabled": False}
        dropped = self._drop("untouched.pdf")
        self.assertEqual(self._collect(), [])
        self.assertTrue(dropped.exists())

    def test_missing_inbox_is_not_an_error(self):
        for path in self.cfg.layout.inbox.iterdir():
            path.unlink()
        self.cfg.layout.inbox.rmdir()
        self.assertEqual(self._collect(), [])


class LocalPaperTests(unittest.TestCase):
    def test_is_local_survives_a_merge(self):
        self.assertTrue(Paper(id="x", title="t", source="local+arxiv").is_local)
        self.assertFalse(Paper(id="x", title="t", source="arxiv").is_local)

    def test_citation_does_not_invent_arxiv_for_a_local_paper(self):
        citation = Paper(id="local:abc", title="A Paper", source="local").citation()
        self.assertNotIn("arXiv", citation)

    def test_citation_still_says_arxiv_for_an_arxiv_paper(self):
        citation = Paper(
            id="arxiv:2401.1", title="A Paper", source="arxiv", arxiv_id="2401.1"
        ).citation()
        self.assertIn("arXiv", citation)


class ResultContractTests(unittest.TestCase):
    def _result(self, **extra) -> dict:
        base = {
            "one_liner": "It does a thing.",
            "problem": "The thing was hard.",
            "contributions": ["One"],
            "method": "By doing the thing.",
        }
        base.update(extra)
        return base

    def test_bibliography_is_optional(self):
        self.assertEqual(validate_result("paper", self._result()), [])

    def test_bibliography_must_be_an_object(self):
        errors = validate_result("paper", self._result(bibliography="Smith 2024"))
        self.assertTrue(any("bibliography" in e for e in errors))

    def test_year_must_be_an_integer(self):
        errors = validate_result(
            "paper", self._result(bibliography={"year": "2024"})
        )
        self.assertTrue(any("year" in e for e in errors))

    def test_topics_must_be_a_list(self):
        errors = validate_result("paper", self._result(topics=SLUG))
        self.assertTrue(any("topics" in e for e in errors))


class ApplyBibliographyTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)
        self.queue = Queue(self.cfg.layout)
        self.paper = Paper(
            id="local:0123456789abcdef",
            title="scan 3 final",  # what the filename said
            source="local",
            local_path="data/pdfs/local-0123456789abcdef.pdf",
        )
        self.store.save_paper(self.paper)

    def tearDown(self):
        self.sandbox.close()

    def _apply(self, **extra):
        result = {
            "one_liner": "It does a thing.",
            "problem": "The thing was hard.",
            "contributions": ["One"],
            "method": "By doing the thing.",
        }
        result.update(extra)
        self.queue.enqueue(
            kind="paper",
            item_id=self.paper.id,
            topics=[],
            language="en",
            instructions="",
            output_schema={},
            payload={},
        )
        task_id = Queue.task_id("paper", self.paper.id)
        self.queue.complete(task_id, result)
        render.apply_completed(self.cfg)
        return self.store.load_paper(self.paper.id)

    def test_reader_supplies_the_bibliography(self):
        paper = self._apply(
            bibliography={
                "title": "Doubly Robust Estimation Under Interference",
                "authors": ["Ada Lovelace"],
                "year": 2024,
                "venue": "JASA",
                "doi": "10.1000/xyz",
            }
        )
        self.assertEqual(paper.title, "Doubly Robust Estimation Under Interference")
        self.assertEqual(paper.authors, ["Ada Lovelace"])
        self.assertEqual(paper.year, 2024)
        self.assertEqual(paper.venue, "JASA")
        self.assertEqual(paper.published[:4], "2024")

    def test_a_guessed_title_is_replaced_by_the_documents_own(self):
        paper = self._apply(bibliography={"title": "The Real Title"})
        self.assertEqual(paper.title, "The Real Title")

    def test_index_metadata_outranks_a_reading(self):
        # Once the same work has also arrived from arXiv, its metadata is
        # better evidence than anything recovered by reading the PDF.
        self.paper.source = "local+arxiv"
        self.paper.title = "Title From arXiv"
        self.paper.venue = "NeurIPS"
        self.store.save_paper(self.paper)
        paper = self._apply(bibliography={"title": "Misread Title", "venue": "JASA"})
        self.assertEqual(paper.title, "Title From arXiv")
        self.assertEqual(paper.venue, "NeurIPS")

    def test_a_reading_still_fills_blanks_on_a_merged_record(self):
        self.paper.source = "local+arxiv"
        self.store.save_paper(self.paper)
        paper = self._apply(bibliography={"doi": "10.1000/xyz"})
        self.assertEqual(paper.doi, "10.1000/xyz")

    def test_reader_assigns_topics(self):
        paper = self._apply(topics=[SLUG])
        self.assertEqual(paper.topics, [SLUG])

    def test_unknown_topic_slug_is_dropped(self):
        paper = self._apply(topics=["not-a-real-topic"])
        self.assertEqual(paper.topics, [])

    def test_a_collected_paper_keeps_its_scored_topics(self):
        remote = Paper(
            id="arxiv:2401.00001",
            title="Real Title",
            source="arxiv",
            topics=[SLUG],
        )
        self.store.save_paper(remote)
        self.queue.enqueue(
            kind="paper",
            item_id=remote.id,
            topics=[SLUG],
            language="en",
            instructions="",
            output_schema={},
            payload={},
        )
        self.queue.complete(
            Queue.task_id("paper", remote.id),
            {
                "one_liner": "x",
                "problem": "y",
                "contributions": ["z"],
                "method": "w",
                "bibliography": {"title": "Hijacked Title"},
                "topics": ["not-a-real-topic"],
            },
        )
        render.apply_completed(self.cfg)
        after = self.store.load_paper(remote.id)
        self.assertEqual(after.title, "Real Title", "bibliography is for local PDFs only")
        self.assertEqual(after.topics, [SLUG])


if __name__ == "__main__":
    unittest.main()
