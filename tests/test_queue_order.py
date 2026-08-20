"""Which end of the backlog a session drains first.

`list` and `next` used to answer in one order only: the task files, sorted by
name. A task id begins with its kind and continues with a filesystem-safe form
of the item id, so that is alphabetical order — and a session that drains the
top twenty every night was reading the archive alphabetically, which is not a
priority anybody chose.

The properties worth defending are that the default did not move, that every
ordering is total, and that sorting a queue does not touch it. The last one is
asserted the way `tests/test_layering.py` asserts its boundary — by content and
by modification time, because a rewrite with identical bytes is invisible to a
hash.
"""

from __future__ import annotations

import contextlib
import hashlib
import io
import json
import time
import unittest
from pathlib import Path

from pipelines.common.schema import Concept, Paper, Video
from pipelines.common.store import RecordStore, read_json
from pipelines.enrich.queue import Queue, main

from .sandbox import Sandbox

ALPHA = "alpha-topic"
OMEGA = "omega-topic"


def _snapshot(directory: Path) -> dict[str, tuple[str, int]]:
    """Every file under ``directory``, by content *and* by modification time.

    The content hash alone would miss a rewrite that produced identical bytes,
    which is exactly what re-serialising an unchanged task would do.
    """
    return {
        path.relative_to(directory).as_posix(): (
            hashlib.sha256(path.read_bytes()).hexdigest(),
            path.stat().st_mtime_ns,
        )
        for path in sorted(directory.rglob("*"))
        if path.is_file()
    }


class OrderingTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox({ALPHA: "Alpha", OMEGA: "Omega"})
        self.addCleanup(self.sandbox.close)
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)
        self.queue = Queue(self.cfg.layout)

    # -- fixtures ------------------------------------------------------------
    @staticmethod
    def _quiet(argv: list[str]) -> int:
        """Run the command line without its output in the test log."""
        with contextlib.redirect_stdout(io.StringIO()):
            return main(argv)

    def _enqueue(self, kind: str, item_id: str, topics: list[str], payload=None) -> str:
        return self.queue.enqueue(
            kind=kind,
            item_id=item_id,
            topics=topics,
            language="en",
            instructions="",
            output_schema={},
            payload=payload or {},
        )

    def _paper(self, index: int, scores: dict[str, float]) -> str:
        paper = Paper(
            id=f"arxiv:2401.0000{index}",
            title=f"Paper {index}",
            source="arxiv",
            published="2024-01-15",
            topics=sorted(scores),
            scores=scores,
        )
        self.store.save_paper(paper)
        return self._enqueue("paper", paper.id, sorted(scores))

    def _video(self, index: int, scores: dict[str, float]) -> str:
        video = Video(
            id=f"youtube:vid{index}",
            title=f"Talk {index}",
            topics=sorted(scores),
            scores=scores,
        )
        self.store.save_video(video)
        return self._enqueue("video", video.id, sorted(scores))

    def _concept(self, name: str, sources: int, topics: list[str], *, record=True) -> str:
        if record:
            self.store.save_concept(
                Concept(
                    slug=name.lower().replace(" ", "-"),
                    name=name,
                    topics=topics,
                    evidence=[
                        {"kind": "paper", "id": f"arxiv:9999.{n:05d}", "title": "x",
                         "note": ""}
                        for n in range(sources)
                    ],
                )
            )
        return self._enqueue(
            "concept", name, topics, payload={"name": name, "source_count": sources}
        )

    # -- the default did not move --------------------------------------------
    def test_the_default_is_still_filename_order(self):
        """Existing callers must get exactly what they got before."""
        self._paper(2, {ALPHA: 0.9})
        self._paper(1, {ALPHA: 0.1})
        self._concept("Zeta Term", 9, [ALPHA])
        by_name = sorted(
            p.stem for p in self.cfg.layout.queue_pending.glob("*.json")
        )
        self.assertEqual(self.queue.pending_ids(), by_name)
        self.assertEqual(self.queue.pending_ids(order="id"), by_name)

    def test_the_command_line_defaults_to_filename_order(self):
        self._paper(2, {ALPHA: 0.9})
        self._paper(1, {ALPHA: 0.1})
        self.assertEqual(self._quiet(["--root", str(self.sandbox.root), "list"]), 0)

    # -- sources -------------------------------------------------------------
    def test_a_concept_is_weighed_by_its_own_evidence(self):
        heavy = self._concept("Alpha Term", 9, [ALPHA])
        light = self._concept("Beta Term", 2, [ALPHA])
        self.assertEqual(
            self.queue.pending_ids(kind="concept", order="sources"), [heavy, light]
        )

    def test_a_concept_is_weighed_by_the_record_not_by_the_stale_payload(self):
        """The task states what it was built from; the record states what is
        true now. A concept that has gained sources since its task was filed
        must sort by what it has, not by what it had."""
        grown = self._concept("Alpha Term", 2, [ALPHA])
        self.store.save_concept(
            Concept(
                slug="alpha-term",
                name="Alpha Term",
                topics=[ALPHA],
                evidence=[
                    {"kind": "paper", "id": f"arxiv:8888.{n:05d}", "title": "x",
                     "note": ""}
                    for n in range(20)
                ],
            )
        )
        other = self._concept("Beta Term", 9, [ALPHA])
        self.assertEqual(
            self.queue.pending_ids(kind="concept", order="sources"), [grown, other]
        )

    def test_a_concept_whose_record_is_gone_falls_back_to_its_task(self):
        """An ordering is a convenience; it must not fail on a missing record."""
        orphan = self._concept("Alpha Term", 9, [ALPHA], record=False)
        light = self._concept("Beta Term", 2, [ALPHA])
        self.assertEqual(
            self.queue.pending_ids(kind="concept", order="sources"), [orphan, light]
        )

    def test_a_paper_falls_back_to_the_leverage_backfill_uses(self):
        """An unread paper cites nothing, so its entity-evidence sum is zero for
        every candidate. What is left is what scoring decided when it arrived."""
        broad = self._paper(1, {ALPHA: 0.4, OMEGA: 0.4})
        narrow = self._paper(2, {ALPHA: 0.7})
        self.assertEqual(
            self.queue.pending_ids(kind="paper", order="sources"), [broad, narrow]
        )

    def test_a_video_is_weighed_the_same_way_as_a_paper(self):
        broad = self._video(1, {ALPHA: 0.4, OMEGA: 0.4})
        narrow = self._video(2, {ALPHA: 0.7})
        self.assertEqual(
            self.queue.pending_ids(kind="video", order="sources"), [broad, narrow]
        )

    def test_a_paper_whose_record_is_gone_sorts_last_rather_than_raising(self):
        orphan = self._enqueue("paper", "arxiv:2401.00009", [ALPHA])
        real = self._paper(1, {ALPHA: 0.5})
        self.assertEqual(
            self.queue.pending_ids(kind="paper", order="sources"), [real, orphan]
        )

    def test_equal_weights_break_the_same_way_every_call(self):
        second = self._paper(2, {ALPHA: 0.5})
        first = self._paper(1, {ALPHA: 0.5})
        self.assertEqual(
            self.queue.pending_ids(kind="paper", order="sources"), [first, second]
        )

    # -- recency -------------------------------------------------------------
    def test_recency_puts_the_newest_task_first(self):
        """Deliberately slept through. `utcnow()` has second resolution, so two
        tasks filed in the same second carry the same `created_at` and this
        passes whether or not the ordering reads the field at all."""
        older = self._paper(1, {ALPHA: 0.5})
        time.sleep(1.1)
        newer = self._paper(2, {ALPHA: 0.5})
        # Filename order is the other way round, so a test that passed by
        # accident would fail here.
        self.assertEqual(self.queue.pending_ids(kind="paper"), [older, newer])
        self.assertEqual(
            self.queue.pending_ids(kind="paper", order="recency"), [newer, older]
        )

    def test_a_task_with_no_timestamp_sorts_after_every_dated_one(self):
        dated = self._paper(1, {ALPHA: 0.5})
        undated = self._paper(2, {ALPHA: 0.5})
        path = self.queue.pending_path(undated)
        task = read_json(path)
        task["created_at"] = ""
        path.write_text(json.dumps(task), encoding="utf-8")
        self.assertEqual(
            self.queue.pending_ids(kind="paper", order="recency"), [dated, undated]
        )

    # -- topic ---------------------------------------------------------------
    def test_tasks_are_grouped_by_topic_before_they_are_weighed(self):
        """Grouping outranks weight: the point of `--by topic` is a drain that
        spreads across what the group tracks rather than following one subject
        to the bottom."""
        alpha_light = self._paper(1, {ALPHA: 0.1})
        omega_heavy = self._paper(2, {OMEGA: 0.9})
        self.assertEqual(
            self.queue.pending_ids(kind="paper", order="topic"),
            [alpha_light, omega_heavy],
        )

    def test_within_a_group_the_heavier_task_comes_first(self):
        light = self._paper(1, {ALPHA: 0.1})
        heavy = self._paper(2, {ALPHA: 0.9})
        self.assertEqual(
            self.queue.pending_ids(kind="paper", order="topic"), [heavy, light]
        )

    def test_a_task_belonging_to_two_topics_groups_under_the_first(self):
        both = self._paper(1, {ALPHA: 0.5, OMEGA: 0.5})
        omega_only = self._paper(2, {OMEGA: 0.9})
        self.assertEqual(
            self.queue.pending_ids(kind="paper", order="topic"), [both, omega_only]
        )

    def test_a_task_with_no_topic_sorts_after_every_group(self):
        """An empty slug string would have put it in front of everything."""
        homeless = self._enqueue("concept", "Alpha Term", [])
        placed = self._enqueue("concept", "Zeta Term", [OMEGA])
        self.assertEqual(
            self.queue.pending_ids(kind="concept", order="topic"), [placed, homeless]
        )

    # -- the flag reaches the command line -----------------------------------
    def test_kind_still_narrows_under_every_ordering(self):
        self._paper(1, {ALPHA: 0.5})
        self._concept("Alpha Term", 9, [ALPHA])
        self._video(1, {ALPHA: 0.5})
        for order in ("id", "sources", "recency", "topic"):
            with self.subTest(order=order):
                ids = self.queue.pending_ids(kind="paper", order=order)
                self.assertEqual(len(ids), 1)
                self.assertTrue(ids[0].startswith("paper__"))

    def test_next_returns_the_first_task_of_the_chosen_ordering(self):
        self._paper(1, {ALPHA: 0.1})
        heavy = self._paper(2, {ALPHA: 0.9})
        chosen = self.queue.pending_ids(order="sources")[0]
        self.assertEqual(chosen, heavy)

    def test_the_command_line_accepts_by_on_list_and_next(self):
        self._paper(1, {ALPHA: 0.5})
        root = str(self.sandbox.root)
        for order in ("id", "sources", "recency", "topic"):
            with self.subTest(order=order):
                self.assertEqual(
                    self._quiet(["--root", root, "list", "--by", order]), 0
                )
                self.assertEqual(
                    self._quiet(["--root", root, "next", "--by", order]), 0
                )


class OrderingWritesNothing(unittest.TestCase):
    """Sorting is a read. The queue is `data/`, and this is that boundary."""

    def setUp(self):
        self.sandbox = Sandbox({ALPHA: "Alpha", OMEGA: "Omega"})
        self.addCleanup(self.sandbox.close)
        self.cfg = self.sandbox.config()
        store = RecordStore(self.cfg.layout)
        queue = Queue(self.cfg.layout)
        for index in (1, 2):
            paper = Paper(
                id=f"arxiv:2401.0000{index}",
                title=f"Paper {index}",
                source="arxiv",
                topics=[ALPHA],
                scores={ALPHA: 0.1 * index},
            )
            store.save_paper(paper)
            queue.enqueue(kind="paper", item_id=paper.id, topics=[ALPHA],
                          language="en", instructions="", output_schema={},
                          payload={})
        store.save_concept(
            Concept(slug="alpha-term", name="Alpha Term", topics=[ALPHA],
                    evidence=[{"kind": "paper", "id": "arxiv:2401.00001",
                               "title": "x", "note": ""}])
        )
        queue.enqueue(kind="concept", item_id="Alpha Term", topics=[ALPHA],
                      language="en", instructions="", output_schema={},
                      payload={"name": "Alpha Term", "source_count": 1})
        self.queue = queue
        self.data = self.cfg.layout.data

    def test_listing_in_every_order_changes_no_file_under_data(self):
        before = _snapshot(self.data)
        time.sleep(1.1)
        for order in ("id", "sources", "recency", "topic"):
            for kind in (None, "paper", "video", "concept"):
                self.queue.pending_ids(kind=kind, order=order)
        self.assertEqual(_snapshot(self.data), before)

    def test_an_ordering_never_changes_what_a_task_says(self):
        before = {
            task_id: read_json(self.queue.pending_path(task_id))
            for task_id in self.queue.pending_ids()
        }
        for order in ("sources", "recency", "topic"):
            self.queue.pending_ids(order=order)
        after = {
            task_id: read_json(self.queue.pending_path(task_id))
            for task_id in self.queue.pending_ids()
        }
        self.assertEqual(after, before)


if __name__ == "__main__":
    unittest.main()
