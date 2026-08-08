import unittest

from pipelines.common.llm import QueueSummarizer, SummarizerNotConfigured, get_summarizer
from pipelines.common.schema import Paper
from pipelines.enrich.queue import Queue, validate_result

from .sandbox import Sandbox

GOOD_PAPER_RESULT = {
    "one_liner": "It does a thing.",
    "problem": "The thing was hard.",
    "contributions": ["a", "b"],
    "method": "By doing it.",
    "results": "Better.",
    "limitations": "Slow.",
    "relevance": {"test-topic": "Relevant because."},
    "concepts": ["Latent Action Model"],
    "methods": [],
    "datasets": [],
    "tags": ["x"],
}


class ValidationTests(unittest.TestCase):
    def test_valid_paper_result(self):
        self.assertEqual(validate_result("paper", GOOD_PAPER_RESULT), [])

    def test_missing_required_field(self):
        bad = dict(GOOD_PAPER_RESULT, method="")
        self.assertIn("missing or empty required field: method", validate_result("paper", bad))

    def test_wrong_type_for_a_list_field(self):
        bad = dict(GOOD_PAPER_RESULT, contributions="a, b")
        errors = validate_result("paper", bad)
        self.assertTrue(any("must be a list" in e for e in errors))

    def test_relevance_must_be_a_mapping(self):
        bad = dict(GOOD_PAPER_RESULT, relevance=["nope"])
        errors = validate_result("paper", bad)
        self.assertTrue(any("relevance" in e for e in errors))

    def test_non_object_result(self):
        self.assertEqual(validate_result("paper", ["nope"]), ["result must be a JSON object"])

    def test_unknown_kind(self):
        self.assertTrue(validate_result("mystery", {}))

    def test_video_chapter_timestamps_must_be_numeric(self):
        bad = {
            "one_liner": "x",
            "abstract": "y",
            "key_points": ["z"],
            "chapters": [{"start_s": "00:12", "title": "t"}],
        }
        errors = validate_result("video", bad)
        self.assertTrue(any("start_s" in e for e in errors))

    def test_concept_kind_is_constrained(self):
        errors = validate_result("concept", {"definition": "d", "kind": "widget"})
        self.assertTrue(any("kind" in e for e in errors))


class QueueTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.queue = Queue(self.cfg.layout)

    def tearDown(self):
        self.sandbox.close()

    def _enqueue(self, item_id="arxiv:2401.00001") -> str:
        return self.queue.enqueue(
            kind="paper",
            item_id=item_id,
            topics=["test-topic"],
            language="en",
            instructions="Read it.",
            output_schema={"one_liner": "string"},
            payload={"title": "A World Model"},
        )

    def test_enqueue_then_list(self):
        task_id = self._enqueue()
        self.assertEqual(self.queue.pending_ids(), [task_id])
        self.assertEqual(self.queue.stats()["pending"], 1)

    def test_task_is_self_contained(self):
        task = self.queue.load(self._enqueue())
        for key in ("instructions", "output_schema", "payload", "topics", "language"):
            self.assertIn(key, task)

    def test_enqueue_is_idempotent(self):
        self._enqueue()
        self.assertEqual(self._enqueue(), "")
        self.assertEqual(self.queue.stats()["pending"], 1)

    def test_cap_is_enforced(self):
        capped = Queue(self.cfg.layout, max_pending=1)
        self.assertTrue(
            capped.enqueue(
                kind="paper", item_id="a", topics=[], language="en",
                instructions="", output_schema={}, payload={},
            )
        )
        self.assertEqual(
            capped.enqueue(
                kind="paper", item_id="b", topics=[], language="en",
                instructions="", output_schema={}, payload={},
            ),
            "",
        )

    def test_complete_moves_the_task(self):
        task_id = self._enqueue()
        self.queue.complete(task_id, GOOD_PAPER_RESULT)
        self.assertEqual(self.queue.pending_ids(), [])
        self.assertEqual(self.queue.stats()["done"], 1)
        self.assertEqual(self.queue.load(task_id)["result"]["one_liner"], "It does a thing.")

    def test_complete_rejects_an_invalid_result(self):
        task_id = self._enqueue()
        with self.assertRaises(ValueError):
            self.queue.complete(task_id, {"one_liner": "x"})
        self.assertEqual(self.queue.pending_ids(), [task_id])

    def test_complete_unknown_task(self):
        with self.assertRaises(FileNotFoundError):
            self.queue.complete("paper__nope", GOOD_PAPER_RESULT)

    def test_archive_clears_done(self):
        task_id = self._enqueue()
        self.queue.complete(task_id, GOOD_PAPER_RESULT)
        self.queue.archive(task_id)
        self.assertEqual(self.queue.stats()["done"], 0)
        self.assertEqual(self.queue.stats()["archived"], 1)

    def test_completed_task_is_not_requeued(self):
        task_id = self._enqueue()
        self.queue.complete(task_id, GOOD_PAPER_RESULT)
        self.assertEqual(self._enqueue(), "")


class SummarizerTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.queue = Queue(self.cfg.layout)

    def tearDown(self):
        self.sandbox.close()

    def test_queue_backend_defers_and_files_a_task(self):
        summarizer = get_summarizer(self.cfg.settings, enqueue=self.queue.enqueue)
        self.assertIsInstance(summarizer, QueueSummarizer)
        outcome = summarizer.summarize_paper(
            Paper(id="arxiv:1", title="A World Model", source="arxiv"),
            [{"slug": "test-topic", "name": "Test", "description": "d"}],
            "en",
        )
        self.assertIsNone(outcome)
        self.assertEqual(self.queue.stats()["pending"], 1)

    def test_task_instructions_name_every_matched_topic(self):
        summarizer = get_summarizer(self.cfg.settings, enqueue=self.queue.enqueue)
        summarizer.summarize_paper(
            Paper(id="arxiv:1", title="t", source="arxiv"),
            [{"slug": "test-topic", "name": "Test", "description": "d"}],
            "en",
        )
        task = self.queue.load(self.queue.pending_ids()[0])
        self.assertIn("test-topic", task["instructions"])

    def test_unimplemented_backend_raises_a_useful_error(self):
        settings = dict(self.cfg.settings, summarize={"backend": "anthropic"})
        summarizer = get_summarizer(settings, enqueue=self.queue.enqueue)
        with self.assertRaises(SummarizerNotConfigured):
            summarizer.summarize_paper(Paper(id="x", title="t", source="s"), [], "en")

    def test_unknown_backend_raises(self):
        with self.assertRaises(SummarizerNotConfigured):
            get_summarizer({"summarize": {"backend": "magic"}}, enqueue=self.queue.enqueue)


if __name__ == "__main__":
    unittest.main()
