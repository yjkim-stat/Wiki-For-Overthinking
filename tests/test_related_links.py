"""Links between wiki entities: the derived ones and the ruled ones.

Two names in one summary's lists produce an edge. That is all co-occurrence can
do, and it is not enough to navigate by — sibling versions of one system, a
method and the benchmark built to defeat it, a dataset and its successor rarely
turn up inside a single summary's flat name lists, and no amount of reading
changes that.

So a definition task may also rule on neighbours. The two kinds of link are kept
in separate fields because they need opposite lifetimes: a derived edge has to
vanish when the paper that made it is re-read, and a ruled one has to survive
exactly that. Merging them buys a truthful schema at the price of edges nothing
can ever remove.

Before this, the task asked for `related`, the validator accepted it, `apply`
wrote it, and `harvest` — later in the same render — rebuilt the record without
it. Every step reported success. See docs/commit/0045.
"""

from __future__ import annotations

import unittest

from pipelines import render
from pipelines.common.schema import Concept, Paper, PaperSummary
from pipelines.common.store import RecordStore
from pipelines.enrich import concepts as concepts_mod
from pipelines.enrich.queue import Queue
from pipelines.publish import wiki

from .sandbox import Sandbox

SLUG = "test-topic"
IV = "instrumental-variable"
BC = "behaviour-cloning"
DR = "doubly-robust-estimation"


def summary_for(paper_id: str, *, concepts: list[str], methods: list[str]) -> PaperSummary:
    return PaperSummary(
        paper_id=paper_id,
        one_liner="It does a thing.",
        problem="The thing was hard.",
        method="By reweighting.",
        results="Beats the baseline.",
        relevance={SLUG: "Moves the topic forward."},
        concepts=concepts,
        methods=methods,
    )


class LinkFixture(unittest.TestCase):
    """Two papers, each naming two entities, so both clear the promotion bar."""

    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)
        self.queue = Queue(self.cfg.layout)

        # Papers 1-2 name both entities, so each clears the promotion bar and
        # the pair is linked by co-occurrence.
        #
        # Papers 3-4 name only a third entity. It gets a note of its own and can
        # never be a derived neighbour of the first two, because nothing names
        # it alongside them — which is the case the whole feature is for, and
        # the only shape of test that can tell the union apart from `related`.
        for index in (1, 2):
            self._paper(index, ["Instrumental Variable"], ["Behaviour Cloning"])
        for index in (3, 4):
            self._paper(index, ["Doubly Robust Estimation"], [])

    def _paper(self, index: int, concepts: list[str], methods: list[str]) -> None:
        paper_id = f"arxiv:2401.0000{index}"
        self.store.save_paper(
            Paper(
                id=paper_id,
                title=f"Paper {index}",
                source="arxiv",
                published="2024-01-15",
                year=2024,
                topics=[SLUG],
            )
        )
        self.store.save_paper_summary(summary_for(paper_id, concepts=concepts, methods=methods))

    def tearDown(self):
        self.sandbox.close()

    def _rule(self, slug: str, related: list[str] | None, *, name: str) -> None:
        """Answer this entity's definition task the way a reader would."""
        result: dict = {"definition": "Two to four sentences.", "kind": "concept"}
        if related is not None:
            result["related"] = related
        self.queue.complete(self._pending_for(slug, name), result)
        render.run(self.cfg)

    def _pending_for(self, slug: str, name: str) -> str:
        """The outstanding definition task, asking for one if there is none.

        Render queues these itself on promotion, so a test cannot enqueue its
        own — the queue refuses a duplicate. Answering twice needs the same
        route a person has: clear the definition and render, which is what
        CLAUDE.md says and the only way back to a task once one is archived.
        """
        found = self._find(name)
        if found:
            return found
        concept = self._concept(slug)
        concept.definition = ""
        self.store.save_concept(concept)
        render.run(self.cfg)
        found = self._find(name)
        self.assertTrue(found, f"render did not re-queue a definition for {name}")
        return found

    def _find(self, name: str) -> str:
        for task_id in self.queue.pending_ids(kind="concept"):
            if (self.queue.load(task_id) or {}).get("item_id") == name:
                return task_id
        return ""

    def _concept(self, slug: str) -> Concept:
        concept = self.store.load_concept(slug)
        self.assertIsNotNone(concept, f"no record for {slug}")
        return concept


class AuthoredLinksSurviveTests(LinkFixture):
    def test_a_ruled_link_survives_the_render_that_applied_it(self):
        """The defect, stated as a test.

        `apply` wrote the answer and `harvest`, later in the same
        `render.run`, rebuilt the record without it.
        """
        render.run(self.cfg)
        self._rule(IV, ["A Distant Neighbour"], name="Instrumental Variable")
        self.assertIn("a-distant-neighbour", self._concept(IV).related_authored)

    def test_a_ruled_link_survives_later_renders(self):
        render.run(self.cfg)
        self._rule(IV, ["A Distant Neighbour"], name="Instrumental Variable")
        render.run(self.cfg)
        render.run(self.cfg)
        self.assertIn("a-distant-neighbour", self._concept(IV).related_authored)

    def test_a_ruled_link_is_not_written_into_the_derived_list(self):
        """Which field it lands in is the whole fix.

        In `related` it would be rebuilt away; it would also become permanent
        for every derived edge that shares the list.
        """
        render.run(self.cfg)
        self._rule(IV, ["A Distant Neighbour"], name="Instrumental Variable")
        self.assertNotIn("a-distant-neighbour", self._concept(IV).related)

    def test_answering_again_with_an_empty_list_retracts(self):
        render.run(self.cfg)
        self._rule(IV, ["A Distant Neighbour"], name="Instrumental Variable")
        self._rule(IV, [], name="Instrumental Variable")
        self.assertEqual(self._concept(IV).related_authored, [])

    def test_an_answer_that_omits_the_key_leaves_the_links_alone(self):
        """Absent is not the same answer as `[]`."""
        render.run(self.cfg)
        self._rule(IV, ["A Distant Neighbour"], name="Instrumental Variable")
        self._rule(IV, None, name="Instrumental Variable")
        self.assertEqual(self._concept(IV).related_authored, ["a-distant-neighbour"])

    def test_an_entity_cannot_be_ruled_its_own_neighbour(self):
        render.run(self.cfg)
        self._rule(IV, ["Instrumental Variable"], name="Instrumental Variable")
        self.assertEqual(self._concept(IV).related_authored, [])


class DerivedLinksStayDisposableTests(LinkFixture):
    """The property option B would have broken, and nothing guarded before."""

    def test_co_occurrence_creates_an_edge(self):
        render.run(self.cfg)
        self.assertIn(BC, self._concept(IV).related)

    def test_re_reading_a_paper_removes_the_edge_it_made(self):
        render.run(self.cfg)
        self.assertIn(BC, self._concept(IV).related)

        # Both readings change their mind about the method. Nothing now names
        # the two entities together.
        for index in (1, 2):
            self.store.save_paper_summary(
                summary_for(
                    f"arxiv:2401.0000{index}",
                    concepts=["Instrumental Variable"],
                    methods=["Some Other Method"],
                )
            )
        concepts_mod.rebuild(self.cfg)
        self.assertNotIn(BC, self._concept(IV).related)

    def test_a_ruled_link_survives_the_same_re_read(self):
        """The two lifetimes, side by side in one test."""
        render.run(self.cfg)
        self._rule(IV, ["Behaviour Cloning"], name="Instrumental Variable")

        for index in (1, 2):
            self.store.save_paper_summary(
                summary_for(
                    f"arxiv:2401.0000{index}",
                    concepts=["Instrumental Variable"],
                    methods=["Some Other Method"],
                )
            )
        concepts_mod.rebuild(self.cfg)

        concept = self._concept(IV)
        self.assertNotIn(BC, concept.related, "the derived edge should be gone")
        self.assertIn(BC, concept.related_authored, "the ruling should not be")
        self.assertIn(BC, concept.neighbours)


class RenderedOutputTests(LinkFixture):
    def test_the_note_links_to_a_ruled_neighbour(self):
        """Ruled to an entity co-occurrence can never reach.

        Asserting this against a neighbour that is also derived would pass
        whether or not the renderer reads the authored list at all — which is
        how the first version of this test failed to bite.
        """
        render.run(self.cfg)
        self._rule(IV, ["Doubly Robust Estimation"], name="Instrumental Variable")
        note = wiki.note_path(self.cfg.layout, "concept", IV).read_text(encoding="utf-8")
        self.assertIn("**Related**", note)
        self.assertIn("Doubly Robust Estimation", note)
        self.assertNotIn(DR, self._concept(IV).related, "must not be derivable")

    def test_a_ruled_link_to_an_entity_with_no_note_is_not_rendered(self):
        """`neighbours` may name anything; the renderer still filters."""
        render.run(self.cfg)
        self._rule(IV, ["Nothing Has Ever Mentioned This"], name="Instrumental Variable")
        note = wiki.note_path(self.cfg.layout, "concept", IV).read_text(encoding="utf-8")
        self.assertNotIn("Nothing Has Ever Mentioned This", note)

    def test_the_graph_gains_an_edge_for_a_ruled_link(self):
        render.run(self.cfg)
        before = len(_edges(self.cfg))
        self._rule(IV, ["Doubly Robust Estimation"], name="Instrumental Variable")
        self.assertEqual(len(_edges(self.cfg)), before + 1)

    def test_a_ruling_that_agrees_with_the_evidence_does_not_double_an_edge(self):
        render.run(self.cfg)
        before = len(_edges(self.cfg))
        self._rule(IV, ["Behaviour Cloning"], name="Instrumental Variable")
        self.assertEqual(len(_edges(self.cfg)), before)

    def test_a_render_over_an_unchanged_archive_still_changes_no_record(self):
        """The churn guard, re-asserted over the new field.

        `_same` compares whole records, so a field that arrived empty on every
        pass would be invisible here — and one that did not would rewrite every
        concept file on every render.
        """
        render.run(self.cfg)
        self._rule(IV, ["Behaviour Cloning"], name="Instrumental Variable")
        before = _snapshot(self.cfg)
        render.run(self.cfg)
        self.assertEqual(_snapshot(self.cfg), before)


def _edges(cfg) -> list[dict]:
    import json

    graph = json.loads(
        (cfg.layout.wiki_meta / "graph.json").read_text(encoding="utf-8")
    )
    return [e for e in graph["edges"] if e.get("type") != "covers"]


def _snapshot(cfg) -> dict[str, str]:
    import hashlib

    return {
        path.name: hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(cfg.layout.concepts.glob("*.json"))
    }


class RecordCompatibilityTests(unittest.TestCase):
    def test_a_record_written_before_the_field_loads_with_it_empty(self):
        """Adding a field is safe; this is the assertion that says so."""
        raw = Concept(slug="x", name="X").to_dict()
        raw.pop("related_authored")
        self.assertEqual(Concept.from_dict(raw).related_authored, [])

    def test_neighbours_unions_both_lists(self):
        concept = Concept(
            slug="x", name="X", related=["a", "b"], related_authored=["b", "c"]
        )
        self.assertEqual(concept.neighbours, {"a", "b", "c"})

    def test_neighbours_drops_a_self_link(self):
        concept = Concept(slug="x", name="X", related_authored=["x", "a"])
        self.assertEqual(concept.neighbours, {"a"})


if __name__ == "__main__":
    unittest.main()
