"""Folding a finished task back into the records.

The queue validates what a reader submits; this is the step after, where the
answer becomes a record and the task's own bookkeeping becomes provenance. A
mistake here is quiet by construction — the summary is complete and readable,
and only the field describing where it came from is wrong.
"""

from __future__ import annotations

import unittest

from pipelines.common.schema import Paper, Video
from pipelines.common.store import RecordStore
from pipelines.enrich import apply as apply_mod
from pipelines.enrich.queue import Queue

from .sandbox import Sandbox

SLUG = "test-topic"

PAPER_RESULT = {
    "one_liner": "It does a thing.",
    "problem": "The thing was hard.",
    "contributions": ["a"],
    "method": "By doing it.",
    "results": "Better.",
    "limitations": "Slow.",
    "relevance": {SLUG: "Relevant because."},
}

VIDEO_RESULT = {
    "one_liner": "A talk.",
    "abstract": "About a thing.",
    "key_points": ["A point."],
    "chapters": [{"start_s": 0, "title": "Opening", "summary": "Hello."}],
}


class ProvenanceTests(unittest.TestCase):
    """`generated_by` says which backend produced a reading.

    It exists so that a record made by the daily session and one made by an API
    backend can be told apart later, when the two disagree and somebody has to
    decide which to trust.
    """

    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)
        self.queue = Queue(self.cfg.layout)

    def tearDown(self):
        self.sandbox.close()

    def _complete(self, kind: str, item_id: str, result: dict) -> None:
        task_id = self.queue.enqueue(
            kind=kind,
            item_id=item_id,
            topics=[SLUG],
            language="en",
            instructions="",
            output_schema={},
            payload={},
        )
        self.queue.complete(task_id, result)
        apply_mod.completed(self.cfg)

    def test_a_paper_reading_names_the_backend(self):
        """It used to fall back to `task["kind"]`, so every paper read as 'paper'.

        The field was never empty and never obviously wrong, which is why the
        whole of one archive carried the same meaningless value without anyone
        noticing: `generated_by: "paper"` on 242 consecutive readings.
        """
        self.store.save_paper(
            Paper(id="arxiv:2401.00001", title="A Paper", source="arxiv", topics=[SLUG])
        )
        self._complete("paper", "arxiv:2401.00001", PAPER_RESULT)

        summary = self.store.load_paper_summary("arxiv:2401.00001")
        self.assertEqual(summary.generated_by, "queue")
        self.assertNotEqual(summary.generated_by, "paper")

    def test_a_video_reading_names_the_same_backend(self):
        """The video applier never had the extra fallback.

        That asymmetry is what the bug was: two appliers, one field, and only
        one of them putting a backend name in it.
        """
        self.store.save_video(
            Video(id="yt:abc123", title="A Talk", channel="Somewhere", topics=[SLUG])
        )
        self._complete("video", "yt:abc123", VIDEO_RESULT)

        summary = self.store.load_video_summary("yt:abc123")
        self.assertEqual(summary.generated_by, "queue")

    def test_an_explicit_backend_is_kept(self):
        """A backend that names itself outranks the default.

        Nothing writes `completed_by` today, which is exactly why the default
        has to be right — but the field is the contract an API backend fills in,
        and overwriting it would defeat the purpose of having one.
        """
        self.store.save_paper(
            Paper(id="arxiv:2401.00002", title="Another", source="arxiv", topics=[SLUG])
        )
        task_id = self.queue.enqueue(
            kind="paper", item_id="arxiv:2401.00002", topics=[SLUG], language="en",
            instructions="", output_schema={}, payload={},
        )
        self.queue.complete(task_id, PAPER_RESULT)
        done = self.queue.load(task_id)
        done["completed_by"] = "anthropic"
        from pipelines.common.store import write_json

        write_json(self.queue.done_path(task_id), done)
        apply_mod.completed(self.cfg)

        self.assertEqual(
            self.store.load_paper_summary("arxiv:2401.00002").generated_by, "anthropic"
        )


if __name__ == "__main__":
    unittest.main()
