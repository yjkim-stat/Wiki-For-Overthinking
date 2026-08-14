"""A waiting task is a function of the record it was built from.

`backfill` fetches a document for a paper that has been queued for weeks. The
record gains a `local_path`; the task does not hear about it, because `enqueue`
refused to touch a task that already existed. The correct task — with the
document attached, the prompt that points at the experiments, and the schema
field for saying which you read — was rebuilt on every render and thrown away on
every render.

The cost is not the missing attachment. `_check_reading_basis` refuses
`read_from: "document"` when the task attached none, so a reader who opened the
PDF sitting on disk had to record `abstract` or be rejected: **the archive
permanently recording a weaker evidence tier than it actually had**, and the
tier is what the reading rules turn on.

What must *not* move is equally specific: a task that has been answered, and the
date a task was first filed.
"""

from __future__ import annotations

import hashlib
import time
import unittest

from pipelines import render
from pipelines.common.schema import Paper, Video
from pipelines.common.store import RecordStore
from pipelines.enrich.queue import Queue

from .sandbox import Sandbox

SLUG = "test-topic"
TASK = "paper__arxiv-2401-00001"

RESULT = {
    "one_liner": "It does a thing.",
    "problem": "The thing was hard.",
    "contributions": ["a"],
    "method": "By doing it.",
    "results": "Better.",
    "limitations": "Slow.",
    "relevance": {SLUG: "Relevant."},
}


class TaskRefreshTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)
        self.queue = Queue(self.cfg.layout)
        self.paper = Paper(
            id="arxiv:2401.00001",
            title="A Paper",
            source="arxiv",
            abstract="An abstract.",
            published="2024-01-15",
            year=2024,
            topics=[SLUG],
            scores={SLUG: 0.8},
        )
        self.store.save_paper(self.paper)

    def tearDown(self):
        self.sandbox.close()

    def _give_it_a_document(self) -> None:
        """What `backfill` does: the file lands and the record points at it."""
        target = self.cfg.layout.pdfs / "arxiv-2401-00001.pdf"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(b"%PDF-1.7\n")
        self.paper.local_path = "data/pdfs/arxiv-2401-00001.pdf"
        self.store.save_paper(self.paper)

    def _task(self) -> dict:
        task = self.queue.load(TASK)
        self.assertIsNotNone(task, "the task should still be pending")
        return task

    # -- the round trip that failed -----------------------------------------
    def test_a_document_arriving_late_reaches_the_waiting_task(self):
        render.run(self.cfg)
        self.assertEqual((self._task().get("attachments") or {}), {})

        self._give_it_a_document()
        render.run(self.cfg)

        attachments = self._task().get("attachments") or {}
        self.assertEqual(attachments.get("pdf_path"), self.paper.local_path)

    def test_the_refreshed_task_asks_the_question_the_document_allows(self):
        """Three things move together, and two are easy to forget.

        `has_document` picks the attachment, the instructions and the output
        schema. A task refreshed with only the first would hand over a PDF while
        asking abstract questions and offering nowhere to record that it was
        read.
        """
        render.run(self.cfg)
        self._give_it_a_document()
        render.run(self.cfg)

        task = self._task()
        self.assertIn("read_from", task["output_schema"])
        self.assertIn("attachments.pdf_path", task["instructions"])

    def test_the_reader_may_then_honestly_say_they_read_it(self):
        """The end of the sequence `CLAUDE.md` documents.

        Before this, opening the file and saying so was refused, and the only
        accepted answer was the untrue one.
        """
        render.run(self.cfg)
        self._give_it_a_document()
        render.run(self.cfg)

        self.queue.complete(TASK, dict(RESULT, read_from="document"))
        self.assertEqual(self.queue.pending_ids(kind="paper"), [])

    # -- what must not move --------------------------------------------------
    def test_created_at_survives_the_refresh(self):
        """It is the only record of how long this item has been waiting.

        Sleeps past a second boundary first. `utcnow()` has second resolution,
        so within one second a re-stamped timestamp is identical to the one it
        replaced and this passes whether or not the bug is present — which it
        did when first written.
        """
        render.run(self.cfg)
        before = self._task()["created_at"]

        self._give_it_a_document()
        time.sleep(1.1)
        render.run(self.cfg)

        self.assertEqual(self._task()["created_at"], before)

    def test_an_answered_task_is_never_rewritten(self):
        """A reader may have worked from the version they were handed.

        Asserted against the summarizer directly rather than through `render`,
        which would apply the answer and move the task on to `archive/` before
        the guard could be observed.
        """
        render.run(self.cfg)
        self.queue.complete(TASK, RESULT)
        done = self.queue.done_path(TASK)
        before = done.read_bytes()

        self._give_it_a_document()
        _, summarizer = _summarizer_with(self.cfg, self.queue)
        summarizer.summarize_paper(self.paper, self.cfg.topic_context([SLUG]), "en")

        self.assertEqual(done.read_bytes(), before)
        self.assertFalse(
            self.queue.pending_path(TASK).exists(),
            "an answered task must not be re-filed as pending",
        )

    def test_an_applied_task_stays_applied(self):
        """End to end: once render has folded the answer in, nothing reopens it."""
        render.run(self.cfg)
        self.queue.complete(TASK, RESULT)
        render.run(self.cfg)

        archived = self.queue.archive_path(TASK)
        self.assertTrue(archived.exists())
        before = archived.read_bytes()

        self._give_it_a_document()
        render.run(self.cfg)

        self.assertEqual(archived.read_bytes(), before)
        self.assertEqual(self.queue.pending_ids(kind="paper"), [])

    def test_a_render_over_an_unchanged_archive_rewrites_no_task(self):
        """The same property `_same` protects for concept records.

        A refresh that fired on every pass would put the whole queue in every
        diff, which is how a real change stops being visible.

        Asserted on modification time, not content. A rewrite with identical
        bytes is invisible to a hash, so the first version of this test passed
        against a mutation that wrote on every render.
        """
        render.run(self.cfg)
        before = self._snapshot()
        time.sleep(1.1)
        render.run(self.cfg)
        self.assertEqual(self._snapshot(), before)

    def test_the_cap_does_not_block_a_refresh(self):
        """A refresh adds nothing to the backlog, so the bound does not apply."""
        self.store.save_video(
            Video(id="yt:abc", title="A Talk", channel="Somewhere", topics=[SLUG])
        )
        render.run(self.cfg)
        self._give_it_a_document()

        capped = Queue(self.cfg.layout, max_pending=1)
        _, summarizer = _summarizer_with(self.cfg, capped)
        summarizer.summarize_paper(
            self.paper, self.cfg.topic_context([SLUG]), "en"
        )
        self.assertEqual(
            (self._task().get("attachments") or {}).get("pdf_path"),
            self.paper.local_path,
        )

    # -- what the run reports ------------------------------------------------
    def test_the_first_render_reports_what_it_filed(self):
        result = render.run(self.cfg)
        self.assertEqual(result["summaries_queued"], 1)
        self.assertEqual(result["summaries_refreshed"], 0)
        self.assertEqual(result["summaries_unread"], 1)

    def test_a_second_render_reports_that_it_filed_nothing(self):
        """The number that used to read the same on every pass.

        `summaries_queued` counted records without a summary, because a queue
        backend defers every item it is handed and the count was taken from
        that. It therefore reported the whole backlog every render however
        little was filed — which is how a defect that filed nothing for weeks
        went unnoticed.
        """
        render.run(self.cfg)
        result = render.run(self.cfg)
        self.assertEqual(result["summaries_queued"], 0)
        self.assertEqual(result["summaries_refreshed"], 0)
        self.assertEqual(result["summaries_unread"], 1, "the backlog is still there")

    def test_a_refresh_is_reported_as_a_refresh(self):
        render.run(self.cfg)
        self._give_it_a_document()
        result = render.run(self.cfg)
        self.assertEqual(result["summaries_queued"], 0)
        self.assertEqual(result["summaries_refreshed"], 1)

    def test_a_read_paper_leaves_the_backlog(self):
        render.run(self.cfg)
        self.queue.complete(TASK, RESULT)
        result = render.run(self.cfg)
        self.assertEqual(result["summaries_unread"], 0)
        self.assertEqual(result["summaries_queued"], 0)

    def _snapshot(self) -> dict[str, tuple[str, float]]:
        """Content and mtime. The second is what catches a rewrite that changes
        nothing — identical bytes leave a hash untouched."""
        return {
            path.name: (
                hashlib.sha256(path.read_bytes()).hexdigest(),
                path.stat().st_mtime,
            )
            for path in sorted(self.cfg.layout.queue_pending.glob("*.json"))
        }


def _summarizer_with(cfg, queue):
    from pipelines.common.llm import get_summarizer

    return queue, get_summarizer(cfg.settings, enqueue=queue.enqueue)


if __name__ == "__main__":
    unittest.main()
