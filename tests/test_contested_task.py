"""A task whose record shares an identifier with another.

`reconcile_identifiers` reports two records claiming one identifier on every
render — to whoever ran the render. The person who then drains the queue is
often not that person and is always looking somewhere else, and reading such a
paper can be exactly the wrong move: the archive gains a second summary of one
paper and counts it twice in every entity that cites it.

Measured on a live archive: `arxiv:2503.20314` sat pending, with its PDF, while
`local:94a3…` already held the reading. A session skipped it by hand and the
queue recorded nothing about why, so the next night's run had no way to know.

A warning rather than a refusal. If neither record has been read, reading either
is fine — a merge carries the summary to whichever survives. It is wrong only
when the other already has one, and the reader can check that from the task.
"""

from __future__ import annotations

import unittest

from pipelines import render
from pipelines.common.schema import Paper, PaperSummary
from pipelines.common.store import RecordStore, SeenStore
from pipelines.enrich.queue import Queue

from .sandbox import Sandbox

SLUG = "test-topic"
ARXIV = "arxiv:2503.20314"
LOCAL = "local:94a30c3706dd3819"
TITLE = "Wan: Open and Advanced Video Foundation Models"


class ContestedTaskTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.addCleanup(self.sandbox.close)
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)
        self.queue = Queue(self.cfg.layout, cfg=self.cfg)

        self.store.save_paper(
            Paper(id=ARXIV, title=TITLE, source="seed", arxiv_id="2503.20314",
                  pdf_url="https://arxiv.org/pdf/2503.20314", topics=[SLUG])
        )
        self.store.save_paper(
            Paper(id=LOCAL, title=TITLE, source="local", arxiv_id="2503.20314",
                  topics=[SLUG])
        )
        self.store.save_paper_summary(
            PaperSummary(paper_id=LOCAL, one_liner="It generates video.",
                         relevance={SLUG: "Relevant."})
        )
        with SeenStore(self.cfg.layout.seen_db) as seen:
            seen.mark(ARXIV, kind="paper", canonical=ARXIV, source="seed")
            seen.mark("arxiv:2503.20314", kind="paper", canonical=LOCAL, source="local")

    def _task(self) -> dict:
        task = self.queue.load(Queue.task_id("paper", ARXIV))
        self.assertIsNotNone(task, "the contested paper should still be offered")
        return task

    def test_the_task_names_the_other_record(self):
        render.run(self.cfg)
        task = self._task()
        self.assertEqual(task["payload"]["contested_with"], LOCAL)
        self.assertIn(LOCAL, task["instructions"])

    def test_the_task_says_what_reading_it_would_cost(self):
        render.run(self.cfg)
        instructions = self._task()["instructions"]
        self.assertIn("Stop and check before reading this", instructions)
        self.assertIn("count it twice", instructions)
        self.assertIn("dedupe merge", instructions)

    def test_it_warns_rather_than_withholding_the_task(self):
        """Reading is not always wrong, so the task is still offered."""
        render.run(self.cfg)
        self.assertIn(Queue.task_id("paper", ARXIV),
                      self.queue.pending_ids(kind="paper"))

    def test_an_uncontested_paper_says_nothing_of_the_kind(self):
        self.store.save_paper(
            Paper(id="arxiv:2401.00001", title="Something Else", source="arxiv",
                  topics=[SLUG])
        )
        render.run(self.cfg)
        task = self.queue.load(Queue.task_id("paper", "arxiv:2401.00001"))
        self.assertEqual(task["payload"]["contested_with"], "")
        self.assertNotIn("Stop and check", task["instructions"])

    def test_a_waiting_task_learns_about_a_conflict_that_arrives_later(self):
        """Tasks track their records since note 0052; this rides on that."""
        self.store.save_paper(
            Paper(id="arxiv:2401.00001", title="Something Else", source="arxiv",
                  topics=[SLUG])
        )
        render.run(self.cfg)
        self.assertNotIn(
            "Stop and check",
            self.queue.load(Queue.task_id("paper", "arxiv:2401.00001"))["instructions"],
        )

        with SeenStore(self.cfg.layout.seen_db) as seen:
            seen.mark("title:collides", kind="paper",
                      canonical="arxiv:2401.00001", source="arxiv")
        clash = Paper(id="local:deadbeef", title="Something Else", source="local",
                      topics=[SLUG])
        self.store.save_paper(clash)
        render.run(self.cfg)

        task = self.queue.load(Queue.task_id("paper", "arxiv:2401.00001"))
        self.assertIn("Stop and check", task["instructions"])

    def test_the_warning_goes_when_the_merge_does(self):
        from pipelines.enrich.dedupe import merge_records

        render.run(self.cfg)
        self.assertIn("Stop and check", self._task()["instructions"])

        merge_records(self.cfg, ARXIV, LOCAL)
        render.run(self.cfg)

        task = self.queue.load(Queue.task_id("paper", ARXIV))
        if task is not None:  # the merge moves the reading across, so it may go
            self.assertNotIn("Stop and check", task["instructions"])


if __name__ == "__main__":
    unittest.main()
