"""What a reading was based on, and why the task is the one that knows.

A summary written from an abstract and a summary written from the paper are the
same shape and carry the same authority in every artifact built on top of them.
They are not worth the same. An abstract reports a paper's claims and rarely the
condition under which they fail, so a record that cannot say which it came from
cannot say how much to trust it.

Nothing in the pipeline can observe whether a PDF was opened, so the reader has
to say. What the task *can* do is check the one direction that is checkable: a
reading cannot have been based on a document that was never attached to it.
"""

from __future__ import annotations

import unittest

from pipelines.common.llm import QueueSummarizer
from pipelines.common.schema import Paper, PaperSummary
from pipelines.common.store import RecordStore
from pipelines.enrich import apply as apply_mod
from pipelines.enrich.queue import Queue, validate_result

from .sandbox import Sandbox

SLUG = "test-topic"

RESULT = {
    "one_liner": "It does a thing.",
    "problem": "The thing was hard.",
    "contributions": ["a", "b"],
    "method": "By doing it.",
    "results": "Better.",
    "limitations": "Slow.",
    "relevance": {SLUG: "Relevant because."},
    "concepts": [],
    "methods": [],
    "datasets": [],
    "tags": [],
}

WITH_DOCUMENT = {"pdf_path": "data/pdfs/abc123.pdf"}
NO_DOCUMENT: dict = {}


class ValidationTests(unittest.TestCase):
    """The rules, at the boundary where a result is accepted or refused."""

    def test_a_task_that_attached_a_document_requires_an_answer(self):
        errors = validate_result("paper", RESULT, {"topics": [SLUG], "attachments": WITH_DOCUMENT})
        self.assertTrue(any("read_from" in e for e in errors), errors)

    def test_declaring_the_document_satisfies_it(self):
        result = dict(RESULT, read_from="document")
        self.assertEqual(validate_result("paper", result, {"topics": [SLUG], "attachments": WITH_DOCUMENT}), [])

    def test_admitting_the_abstract_satisfies_it_too(self):
        """The point is to know, not to force the document open.

        A reader who could not use the PDF and says so leaves a record that can
        be redone later. One who is pushed into claiming otherwise leaves a
        record nobody can find again.
        """
        result = dict(RESULT, read_from="abstract")
        self.assertEqual(validate_result("paper", result, {"topics": [SLUG], "attachments": WITH_DOCUMENT}), [])

    def test_a_reading_cannot_claim_a_document_it_was_never_given(self):
        result = dict(RESULT, read_from="document")
        errors = validate_result("paper", result, {"topics": [SLUG], "attachments": NO_DOCUMENT})
        self.assertTrue(any("never given" in e for e in errors), errors)

    def test_no_document_means_nothing_to_ask(self):
        self.assertEqual(validate_result("paper", RESULT, {"topics": [SLUG], "attachments": NO_DOCUMENT}), [])

    def test_an_unknown_value_is_refused(self):
        result = dict(RESULT, read_from="skimmed")
        errors = validate_result("paper", result, {"topics": [SLUG], "attachments": WITH_DOCUMENT})
        self.assertTrue(any("must be one of" in e for e in errors), errors)

    def test_the_value_must_be_a_string(self):
        result = dict(RESULT, read_from=True)
        errors = validate_result("paper", result, {"topics": [SLUG], "attachments": WITH_DOCUMENT})
        self.assertTrue(any("must be a string" in e for e in errors), errors)

    def test_without_the_task_only_the_value_is_checked(self):
        """A task that says nothing about attachments asks nothing.

        An absent `attachments` key is no context, which is not the same as an
        empty one: a task that carried no document refuses a claim to have read
        one, and a task that does not say either way cannot. So nothing is
        required and nothing is refused except a value wrong on its face.
        """
        self.assertEqual(validate_result("paper", RESULT, {"topics": [SLUG]}), [])
        self.assertEqual(
            validate_result("paper", dict(RESULT, read_from="document"), {"topics": [SLUG]}), []
        )
        self.assertTrue(
            validate_result("paper", dict(RESULT, read_from="skimmed"), {"topics": [SLUG]})
        )

    def test_a_video_is_not_asked(self):
        video = {"one_liner": "x", "abstract": "y", "key_points": ["z"]}
        self.assertEqual(validate_result("video", video, {"attachments": WITH_DOCUMENT}), [])


class TaskTests(unittest.TestCase):
    """A task asks for the basis exactly when it hands over a document."""

    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.queue = Queue(self.cfg.layout)
        self.topics = [{"slug": SLUG, "name": "Test Topic", "description": ""}]

    def tearDown(self):
        self.sandbox.close()

    def _enqueue(self, *, local_path: str = "") -> dict:
        paper = Paper(
            id="arxiv:2401.00001",
            title="A Paper",
            source="arxiv",
            abstract="An abstract.",
            topics=[SLUG],
            local_path=local_path,
        )
        RecordStore(self.cfg.layout).save_paper(paper)
        summarizer = QueueSummarizer(
            lambda **kwargs: self.queue.enqueue(**kwargs)
        )
        summarizer.summarize_paper(paper, self.topics, "en")
        return self.queue.load(self.queue.pending_ids()[0])

    def test_a_task_with_a_document_asks_for_the_basis(self):
        task = self._enqueue(local_path="data/pdfs/abc123.pdf")
        self.assertIn("read_from", task["output_schema"])
        self.assertIn("read_from", task["instructions"])

    def test_a_task_without_one_does_not(self):
        task = self._enqueue()
        self.assertNotIn("read_from", task["output_schema"])
        self.assertNotIn("read_from", task["instructions"])

    def test_the_queue_refuses_a_silent_answer_when_it_gave_a_document(self):
        task = self._enqueue(local_path="data/pdfs/abc123.pdf")
        with self.assertRaises(ValueError) as caught:
            self.queue.complete(task["task_id"], RESULT)
        self.assertIn("read_from", str(caught.exception))
        self.assertEqual(self.queue.pending_ids(), [task["task_id"]])

    def test_the_queue_accepts_it_once_answered(self):
        task = self._enqueue(local_path="data/pdfs/abc123.pdf")
        self.queue.complete(task["task_id"], dict(RESULT, read_from="document"))
        self.assertEqual(self.queue.pending_ids(), [])


class AppliedRecordTests(unittest.TestCase):
    """What ends up in the record, which is the only part that lasts."""

    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)
        self.store.save_paper(
            Paper(id="arxiv:2401.00001", title="A Paper", source="arxiv", topics=[SLUG])
        )

    def tearDown(self):
        self.sandbox.close()

    def _apply(self, attachments, result) -> PaperSummary:
        queue = Queue(self.cfg.layout)
        task_id = queue.enqueue(
            kind="paper",
            item_id="arxiv:2401.00001",
            topics=[SLUG],
            language="en",
            instructions="",
            output_schema={},
            payload={},
            attachments=attachments,
        )
        queue.complete(task_id, result)
        apply_mod.completed(self.cfg)
        summary = self.store.load_paper_summary("arxiv:2401.00001")
        self.assertIsNotNone(summary)
        return summary

    def test_the_declared_basis_is_what_is_stored(self):
        summary = self._apply(WITH_DOCUMENT, dict(RESULT, read_from="document"))
        self.assertEqual(summary.read_from, "document")

    def test_an_admitted_abstract_is_stored_as_one(self):
        summary = self._apply(WITH_DOCUMENT, dict(RESULT, read_from="abstract"))
        self.assertEqual(summary.read_from, "abstract")

    def test_no_document_is_recorded_as_the_abstract_without_asking(self):
        """Not an assumption about the reader: the only thing the task allowed."""
        summary = self._apply(None, RESULT)
        self.assertEqual(summary.read_from, "abstract")

    def test_a_reading_from_before_the_field_stays_unknown(self):
        """Empty is a third state, and it has to survive as one.

        Defaulting a silent answer to `abstract` would make a reading nobody
        asked indistinguishable from a reader who said so, and the difference
        is the entire value of the field.
        """
        queue = Queue(self.cfg.layout)
        task_id = queue.enqueue(
            kind="paper", item_id="arxiv:2401.00001", topics=[SLUG], language="en",
            instructions="", output_schema={}, payload={}, attachments=WITH_DOCUMENT,
        )
        # Bypass `complete`, which would now refuse this: the task predates the
        # field, and what is being tested is what the applier does with one.
        task = queue.load(task_id)
        task["result"] = RESULT
        task["completed_at"] = "2026-01-01T00:00:00Z"
        from pipelines.common.store import write_json

        write_json(queue.done_path(task_id), task)
        queue.pending_path(task_id).unlink()

        apply_mod.completed(self.cfg)
        self.assertEqual(self.store.load_paper_summary("arxiv:2401.00001").read_from, "")

    def test_the_field_survives_a_round_trip_through_disk(self):
        self._apply(WITH_DOCUMENT, dict(RESULT, read_from="document"))
        reloaded = RecordStore(self.cfg.layout).load_paper_summary("arxiv:2401.00001")
        self.assertEqual(reloaded.read_from, "document")

    def test_an_older_record_without_the_field_still_loads(self):
        """Adding a field is safe; this is the assertion that says so."""
        summary = PaperSummary(paper_id="arxiv:2401.00001", one_liner="x")
        raw = summary.to_dict()
        raw.pop("read_from")
        self.assertEqual(PaperSummary.from_dict(raw).read_from, "")


if __name__ == "__main__":
    unittest.main()
