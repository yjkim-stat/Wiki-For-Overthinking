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
    "concepts": ["Instrumental Variable"],
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

    @staticmethod
    def _video(chapters):
        return {"one_liner": "x", "abstract": "y", "key_points": ["z"],
                "chapters": chapters}

    def test_video_chapter_timestamps_must_be_numeric(self):
        errors = validate_result("video", self._video([{"start_s": "00:12", "title": "t"}]))
        self.assertTrue(any("start_s" in e for e in errors))

    def test_a_chapter_without_a_timestamp_is_rejected(self):
        """It used to default to 0 and render as a plausible 0:00."""
        errors = validate_result("video", self._video([{"title": "no timestamp"}]))
        self.assertTrue(any("start_s" in e for e in errors))

    def test_a_boolean_timestamp_is_rejected(self):
        """bool is a subclass of int, so isinstance alone lets True through."""
        errors = validate_result("video", self._video([{"start_s": True, "title": "t"}]))
        self.assertTrue(any("start_s" in e for e in errors))

    def test_zero_is_a_legitimate_first_chapter(self):
        self.assertEqual(validate_result("video", self._video([{"start_s": 0, "title": "t"}])), [])

    def test_no_chapters_at_all_is_valid(self):
        """The documented answer for a video with no transcript."""
        self.assertEqual(validate_result("video", self._video([])), [])

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
            payload={"title": "A Causal Estimator"},
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
            Paper(id="arxiv:1", title="A Causal Estimator", source="arxiv"),
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


class RelevanceKeyTests(unittest.TestCase):
    """`relevance` decides which topic page a paper renders under.

    A key naming a slug the paper does not have renders nowhere; a missing one
    leaves a topic page with no rationale. Neither is visible from inside the
    record — only a comparison against the task reveals it.
    """

    @staticmethod
    def _paper(relevance, **extra):
        return {"one_liner": "x", "problem": "y", "contributions": ["z"],
                "method": "m", "relevance": relevance, **extra}

    def test_without_topics_the_validator_is_blind_as_before(self):
        self.assertEqual(validate_result("paper", self._paper({"other": "why"})), [])

    def test_an_unknown_slug_is_rejected(self):
        errors = validate_result("paper", self._paper({"other": "why"}), {"topics": ["test-topic"]})
        self.assertTrue(any("other" in e for e in errors))

    def test_a_missing_entry_is_reported_too(self):
        errors = validate_result("paper", self._paper({"other": "why"}), {"topics": ["test-topic"]})
        self.assertTrue(any("missing an entry for 'test-topic'" in e for e in errors))

    def test_an_exact_match_is_accepted(self):
        self.assertEqual(
            validate_result("paper", self._paper({"test-topic": "why"}), {"topics": ["test-topic"]}),
            [],
        )

    def test_a_blank_entry_is_rejected(self):
        errors = validate_result("paper", self._paper({"test-topic": "  "}), {"topics": ["test-topic"]})
        self.assertTrue(any("is empty" in e for e in errors))

    def test_a_hand_filed_pdf_is_not_required_to_cover_its_own_answer(self):
        """The task lists every tracked topic as a menu; the reader picks.

        Their answer is filtered against the real topic list when applied, so
        there is nothing settled here to require coverage against.
        """
        self.assertEqual(
            validate_result("paper", self._paper({}, topics=["b"]), {"topics": ["a", "b", "c"]}), []
        )

    def test_a_hand_filed_pdf_may_name_a_slug_that_turns_out_not_to_exist(self):
        self.assertEqual(
            validate_result("paper", self._paper({}, topics=["nope"]), {"topics": ["a", "b"]}), []
        )

    def test_a_hand_filed_pdf_belonging_nowhere_needs_no_relevance(self):
        self.assertEqual(
            validate_result("paper", self._paper({}, topics=[]), {"topics": ["a", "b", "c"]}), []
        )

    def test_a_stray_relevance_key_is_still_wrong_on_a_hand_filed_pdf(self):
        """It renders nowhere, whoever chose the topics."""
        errors = validate_result("paper", self._paper({"c": "why"}, topics=["b"]), {"topics": ["a", "b", "c"]})
        self.assertTrue(any("'c'" in e for e in errors))


class ReopenTests(unittest.TestCase):
    """A reader must be able to correct their own answer before render sees it.

    Completion being one-way pushes people toward editing `data/` by hand, which
    bypasses the validator — the mechanism that exists to stop, among other
    things, an alias that would silently fuse two distinct entities.
    """

    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.queue = Queue(self.cfg.layout)
        self.task_id = self.queue.enqueue(
            kind="paper",
            item_id="arxiv:2401.00001",
            topics=["test-topic"],
            language="en",
            instructions="Read it.",
            output_schema={"one_liner": "string"},
            payload={"title": "A Causal Estimator"},
        )
        self.queue.complete(self.task_id, GOOD_PAPER_RESULT)

    def tearDown(self):
        self.sandbox.close()

    def test_a_completed_task_returns_to_pending(self):
        self.queue.reopen(self.task_id)
        self.assertEqual(self.queue.pending_ids(), [self.task_id])
        self.assertEqual(self.queue.stats()["done"], 0)

    def test_the_material_survives_and_the_answer_does_not(self):
        self.queue.reopen(self.task_id)
        task = self.queue.load(self.task_id)
        for key in ("instructions", "output_schema", "payload", "topics", "language"):
            self.assertIn(key, task)
        self.assertNotIn("result", task)
        self.assertNotIn("completed_at", task)

    def test_a_reopened_task_can_be_answered_differently(self):
        self.queue.reopen(self.task_id)
        corrected = dict(GOOD_PAPER_RESULT, one_liner="It does a different thing.")
        self.queue.complete(self.task_id, corrected)
        self.assertEqual(
            self.queue.load(self.task_id)["result"]["one_liner"],
            "It does a different thing.",
        )

    def test_a_correction_is_still_validated(self):
        self.queue.reopen(self.task_id)
        with self.assertRaises(ValueError):
            self.queue.complete(self.task_id, {"one_liner": "x"})

    def test_an_applied_task_is_refused_with_advice(self):
        """Render has folded it into the records; re-answering would not undo that."""
        self.queue.archive(self.task_id)
        with self.assertRaises(ValueError) as caught:
            self.queue.reopen(self.task_id)
        self.assertIn("already been applied", str(caught.exception))

    def test_an_unknown_id_raises(self):
        with self.assertRaises(FileNotFoundError):
            self.queue.reopen("paper__nope")
