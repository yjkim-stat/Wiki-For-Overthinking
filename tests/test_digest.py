"""What a night of reading did, written where the archive keeps its days.

`archive/daily/<date>.md` is written by `run_daily`, so a night that collected
nothing left no trace inside the archive: the reading, the definitions, the
questions settled — the actual work — survived only in a commit message, which
is outside the thing it is about.

Three properties carry this.

**It is derived, not remembered.** The command has no memory of the session and
cannot acquire one. It reads what the records now say and reports the difference
a date makes, which is why it can count tasks answered today and cannot know
which note somebody wrote a paragraph in.

**It shares the page rather than taking it.** `run_daily`'s half stays above.

**Anything after `<!-- session:end -->` is preserved for ever**, as in a wiki
note. That is where a session says what only it knows, and re-running must not
touch it.
"""

from __future__ import annotations

import unittest
from datetime import date, timedelta

from pipelines import digest, render
from pipelines.common.schema import Concept, Paper, PaperSummary
from pipelines.common.store import RecordStore
from pipelines.enrich import findings, references
from pipelines.enrich.queue import Queue

from .sandbox import Sandbox

SLUG = "test-topic"
TODAY = date(2026, 8, 21)
RESULT = {
    "one_liner": "It does a thing.", "problem": "Hard.",
    "contributions": ["a"], "method": "By doing it.",
    "relevance": {SLUG: "Relevant."},
}


class DigestTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.addCleanup(self.sandbox.close)
        self.cfg = self.sandbox.config()
        self.cfg.layout.ensure()
        self.store = RecordStore(self.cfg.layout)
        self.queue = Queue(self.cfg.layout, cfg=self.cfg)

    def _paper(self, index: int = 1) -> str:
        paper_id = f"arxiv:2401.0000{index}"
        self.store.save_paper(
            Paper(id=paper_id, title=f"Paper {index}", source="arxiv", topics=[SLUG])
        )
        return self.queue.enqueue(
            kind="paper", item_id=paper_id, topics=[SLUG], language="en",
            instructions="", output_schema={}, payload={},
        )

    def _answer_today(self, task_id: str) -> None:
        """Complete a task and stamp it as answered on the day under test."""
        self.queue.complete(task_id, RESULT)
        from pipelines.common.store import write_json

        task = self.queue.load(task_id)
        task["completed_at"] = f"{TODAY.isoformat()}T09:00:00Z"
        write_json(self.queue.done_path(task_id), task)

    def _page(self) -> str:
        return (self.cfg.layout.archive_daily / f"{TODAY.isoformat()}.md").read_text(
            encoding="utf-8"
        )

    # -- what it derives -----------------------------------------------------
    def test_a_night_that_answered_nothing_still_leaves_a_page(self):
        digest.write(self.cfg, TODAY)
        self.assertIn("No task was answered.", self._page())

    def test_tasks_answered_today_are_counted_by_kind(self):
        self._answer_today(self._paper(1))
        self._answer_today(self._paper(2))
        digest.write(self.cfg, TODAY)
        self.assertIn("Answered 2 task(s): 2 paper.", self._page())

    def test_a_task_answered_on_another_day_is_not_counted(self):
        task_id = self._paper(1)
        self.queue.complete(task_id, RESULT)
        from pipelines.common.store import write_json

        task = self.queue.load(task_id)
        task["completed_at"] = f"{(TODAY - timedelta(days=3)).isoformat()}T09:00:00Z"
        write_json(self.queue.done_path(task_id), task)

        digest.write(self.cfg, TODAY)
        self.assertIn("No task was answered.", self._page())

    def test_what_was_settled_today_is_named(self):
        findings.record(
            self.cfg,
            {"kind": "decision", "statement": "The group prefers one thing to another.",
             "topics": [SLUG]},
            self.store,
        )
        recorded = next(iter(self.store.iter_findings()))
        recorded.established_at = f"{TODAY.isoformat()}T10:00:00Z"
        self.store.save_finding(recorded)

        digest.write(self.cfg, TODAY)
        self.assertIn("The group prefers one thing to another.", self._page())

    def test_what_was_checked_outside_is_named(self):
        recorded = references.record(
            self.cfg,
            {"url": "https://example.test/x", "title": "A page", "kind": "docs",
             "retrieved_at": TODAY.isoformat(), "quoted": "It says a thing."},
            self.store,
        )
        digest.write(self.cfg, TODAY)
        self.assertIn(recorded.url, self._page())

    # -- the section that is an input ---------------------------------------
    def test_what_is_left_is_the_last_section(self):
        self._paper(1)
        self._paper(2)
        digest.write(self.cfg, TODAY)
        page = self._page()
        self.assertIn("**Left for the next night**", page)
        self.assertIn("2 paper task(s) waiting", page)

    def test_an_empty_queue_says_so(self):
        digest.write(self.cfg, TODAY)
        self.assertIn("nothing is unread", self._page())

    def test_staleness_is_carried_into_the_same_list(self):
        """It is owed work, whatever produced it."""
        self.store.save_concept(
            Concept(slug="x", name="X", kind="concept", definition="A definition.",
                    evidence=[{"kind": "paper", "id": f"a{i}", "title": "t", "note": ""}
                              for i in range(9)], topics=[SLUG])
        )
        from pipelines.common.store import write_json

        task = Queue.task_id("concept", "X")
        write_json(self.queue.archive_path(task), {
            "task_version": 1, "task_id": task, "kind": "concept", "item_id": "X",
            "topics": [SLUG], "language": "en", "created_at": "2026-01-01T00:00:00Z",
            "instructions": "", "output_schema": {}, "payload": {"source_count": 2},
            "attachments": {}, "result": {},
        })
        digest.write(self.cfg, TODAY)
        self.assertIn("1 definition(s) their evidence has outgrown", self._page())

    # -- how it shares the page ---------------------------------------------
    def test_it_keeps_what_run_daily_wrote(self):
        page = self.cfg.layout.archive_daily / f"{TODAY.isoformat()}.md"
        page.write_text("# Research digest — 2026-08-21\n\n3 new paper(s).\n",
                        encoding="utf-8")
        digest.write(self.cfg, TODAY)
        self.assertIn("3 new paper(s).", self._page())
        self.assertIn("## Session", self._page())

    def test_prose_after_the_marker_survives_a_rewrite(self):
        digest.write(self.cfg, TODAY)
        page = self.cfg.layout.archive_daily / f"{TODAY.isoformat()}.md"
        page.write_text(
            page.read_text(encoding="utf-8") + "\n## What I actually thought\n\nMine.\n",
            encoding="utf-8",
        )
        self._answer_today(self._paper(1))
        digest.write(self.cfg, TODAY)

        page_text = self._page()
        self.assertIn("What I actually thought", page_text)
        self.assertIn("Mine.", page_text)
        self.assertIn("Answered 1 task(s)", page_text, "and the block did update")

    def test_running_it_twice_does_not_stack_copies(self):
        digest.write(self.cfg, TODAY)
        digest.write(self.cfg, TODAY)
        self.assertEqual(self._page().count(digest.BEGIN), 1)
        self.assertEqual(self._page().count("## Session"), 1)

    def test_it_writes_no_record(self):
        import hashlib

        self._answer_today(self._paper(1))
        data = self.cfg.layout.data
        snapshot = lambda: {  # noqa: E731
            p.relative_to(data).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(data.rglob("*")) if p.is_file()
        }
        before = snapshot()
        digest.write(self.cfg, TODAY)
        self.assertEqual(snapshot(), before)

    def test_a_render_does_not_clear_the_day(self):
        """`archive/daily/` is the one thing a rebuild leaves alone."""
        digest.write(self.cfg, TODAY)
        render.run(self.cfg, skip_queueing=True)
        self.assertIn("## Session", self._page())


if __name__ == "__main__":
    unittest.main()
