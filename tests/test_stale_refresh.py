"""Asking again for a definition its evidence has outgrown.

`stale_definitions` has reported this for a while and nothing acted on it, so a
definition written against three sources sat at nine reading as complete —
which is worse than a missing one, because nothing about it looks wrong.

The rule this must not break is stated in `CLAUDE.md`: **a counter must not
discard written work on arithmetic alone.** So nothing here rewrites or clears
anything. The concept keeps its definition, a task carries that definition back
to a reader asking what has changed, and a refresh nobody answers leaves the
archive exactly as it was. That last property is what makes it safe to file one
without being asked.
"""

from __future__ import annotations

import unittest

from pipelines import render
from pipelines.common.schema import Concept, Paper, PaperSummary
from pipelines.common.store import RecordStore
from pipelines.enrich.queue import Queue

from .sandbox import Sandbox

SLUG = "test-topic"
NAME = "Instrumental Variable"
TASK = Queue.task_id("concept", NAME)
DEFINITION = "A variable that shifts treatment but not the outcome."


class StaleRefreshTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.addCleanup(self.sandbox.close)
        self.cfg = self.sandbox.config()
        self.cfg.settings.setdefault("wiki", {})
        self.cfg.settings["wiki"]["refresh_definition_at"] = 2.0
        self.cfg.settings["wiki"]["max_refresh_tasks"] = 5
        self.store = RecordStore(self.cfg.layout)
        self.queue = Queue(self.cfg.layout)

    def _concept(self, *, sources: int, definition: str = DEFINITION) -> Concept:
        concept = Concept(
            slug="instrumental-variable",
            name=NAME,
            kind="concept",
            definition=definition,
            evidence=[
                {"kind": "paper", "id": f"arxiv:{i}", "title": f"Paper {i}", "note": ""}
                for i in range(sources)
            ],
            topics=[SLUG],
        )
        self.store.save_concept(concept)
        return concept

    def _written_against(self, count: int) -> None:
        """Stand in for the archived task the original definition came from."""
        from pipelines.common.store import write_json

        write_json(
            self.queue.archive_path(TASK),
            {
                "task_version": 1, "task_id": TASK, "kind": "concept",
                "item_id": NAME, "topics": [SLUG], "language": "en",
                "created_at": "2026-01-01T00:00:00Z", "instructions": "",
                "output_schema": {}, "payload": {"name": NAME, "source_count": count},
                "attachments": {}, "result": {"definition": DEFINITION},
            },
        )

    def _pending(self) -> dict | None:
        path = self.queue.pending_path(TASK)
        if not path.exists():
            return None
        from pipelines.common.store import read_json

        return read_json(path)

    # -- when it asks --------------------------------------------------------
    def test_a_doubled_evidence_base_is_asked_again(self):
        self._concept(sources=6)
        self._written_against(3)
        counts = render.queue_stale_definitions(self.cfg)
        self.assertEqual(counts["queued"], 1)
        self.assertIsNotNone(self._pending())

    def test_growth_below_the_ratio_is_left_alone(self):
        """A definition written against forty and standing at forty-six is fine.

        Re-asking on every new mention would spend a reader's night on
        definitions that are still true.
        """
        self._concept(sources=5)
        self._written_against(3)
        counts = render.queue_stale_definitions(self.cfg)
        self.assertEqual(counts["stale"], 1, "it is stale")
        self.assertEqual(counts["eligible"], 0, "but not by enough to re-ask")
        self.assertIsNone(self._pending())

    def test_a_definition_whose_evidence_left_is_never_asked_again(self):
        """Reported, but not automatically re-asked, and the asymmetry is meant.

        A definition whose sources grew is *behind*, and handing it back with
        "what has changed" is a fair question. One whose sources were deleted
        may be simply *wrong* — its prose cites material the archive no longer
        holds — and CLAUDE.md's route for wrong is to clear it, which is a
        person's call. The ratio test happens to enforce this on its own; this
        pins it so a later change to the ratio cannot quietly undo it.
        """
        self._concept(sources=2)
        self._written_against(7)
        counts = render.queue_stale_definitions(self.cfg)
        self.assertEqual(counts["stale"], 1, "it is reported")
        self.assertEqual(counts["eligible"], 0, "but never eligible")
        self.assertEqual(counts["queued"], 0)
        self.assertIsNone(self._pending())

    def test_a_definition_matching_its_evidence_is_not_stale_at_all(self):
        self._concept(sources=3)
        self._written_against(3)
        self.assertEqual(render.queue_stale_definitions(self.cfg)["stale"], 0)

    def test_it_is_off_unless_asked_for(self):
        """Upgrading must not grow anybody's queue."""
        self.cfg.settings["wiki"]["refresh_definition_at"] = 0
        self._concept(sources=99)
        self._written_against(1)
        self.assertEqual(render.queue_stale_definitions(self.cfg)["queued"], 0)
        self.assertIsNone(self._pending())

    def test_the_cap_bounds_one_render(self):
        for index in range(4):
            slug = f"entity-{index}"
            self.store.save_concept(
                Concept(slug=slug, name=f"Entity {index}", kind="concept",
                        definition="A definition.",
                        evidence=[{"kind": "paper", "id": f"a{i}", "title": "t",
                                   "note": ""} for i in range(10)],
                        topics=[SLUG])
            )
            from pipelines.common.store import write_json
            task = Queue.task_id("concept", f"Entity {index}")
            write_json(self.queue.archive_path(task), {
                "task_version": 1, "task_id": task, "kind": "concept",
                "item_id": f"Entity {index}", "topics": [SLUG], "language": "en",
                "created_at": "2026-01-01T00:00:00Z", "instructions": "",
                "output_schema": {}, "payload": {"source_count": 1},
                "attachments": {}, "result": {},
            })
        self.cfg.settings["wiki"]["max_refresh_tasks"] = 2
        counts = render.queue_stale_definitions(self.cfg)
        self.assertEqual(counts["eligible"], 4)
        self.assertEqual(counts["queued"], 2)

    # -- what it must not do -------------------------------------------------
    def test_the_definition_is_not_cleared(self):
        """The whole point. Clearing it is the manual route this replaces.

        A refresh nobody answers must leave the archive exactly as it was —
        otherwise a counter has discarded written work on arithmetic alone.
        """
        self._concept(sources=6)
        self._written_against(3)
        render.queue_stale_definitions(self.cfg)
        again = RecordStore(self.cfg.layout).load_concept("instrumental-variable")
        self.assertEqual(again.definition, DEFINITION)

    def test_the_reader_is_handed_what_is_already_there(self):
        """A revision, not a blank page: most of the old ruling is usually right."""
        self._concept(sources=6)
        self._written_against(3)
        render.queue_stale_definitions(self.cfg)
        task = self._pending()
        self.assertEqual(task["payload"]["previous_definition"], DEFINITION)
        self.assertIn(DEFINITION, task["instructions"])
        self.assertIn("Revise", task["instructions"])

    def test_the_task_carries_every_source_including_the_new_ones(self):
        self._concept(sources=6)
        self._written_against(3)
        render.queue_stale_definitions(self.cfg)
        self.assertEqual(len(self._pending()["attachments"]["sources"]), 6)
        self.assertEqual(self._pending()["payload"]["source_count"], 6)

    def test_an_entity_with_no_definition_is_not_this_step_s_business(self):
        self._concept(sources=6, definition="")
        self._written_against(3)
        self.assertEqual(render.queue_stale_definitions(self.cfg)["queued"], 0)

    def test_asking_twice_does_not_make_two_tasks(self):
        self._concept(sources=6)
        self._written_against(3)
        render.queue_stale_definitions(self.cfg)
        render.queue_stale_definitions(self.cfg)
        self.assertEqual(len(self.queue.pending_ids(kind="concept")), 1)

    def test_a_render_files_it_and_reports_it(self):
        """End to end, against evidence a harvest will actually derive.

        `render` rebuilds concept records from the summaries, so a hand-made
        evidence list is replaced before this step ever sees it. Six papers
        that genuinely name the entity is the only fixture that survives the
        pass under test.
        """
        for index in range(6):
            paper_id = f"arxiv:2401.0000{index}"
            self.store.save_paper(
                Paper(id=paper_id, title=f"Paper {index}", source="arxiv",
                      published="2024-01-15", year=2024, topics=[SLUG])
            )
            self.store.save_paper_summary(
                PaperSummary(paper_id=paper_id, one_liner="It does a thing.",
                             relevance={SLUG: "Relevant."}, concepts=[NAME])
            )
        self._concept(sources=6)
        self._written_against(3)

        result = render.run(self.cfg)

        self.assertEqual(result["definitions_reasked"], 1)
        self.assertIsNotNone(self._pending())
        self.assertEqual(
            RecordStore(self.cfg.layout).load_concept(
                "instrumental-variable"
            ).definition,
            DEFINITION,
            "the render must not have cleared it",
        )


if __name__ == "__main__":
    unittest.main()
