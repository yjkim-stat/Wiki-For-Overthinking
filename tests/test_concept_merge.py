"""Two spellings of one benchmark sitting must not become two entities.

A reader names an exam sitting however the paper in front of them happens to:
"AIME 2024", "AIME24", "AIME2024". Left alone, ``slug_for`` treats each as a
distinct entity, and the wiki fragments one benchmark into several near-empty
notes -- discovered when a real backfill collected 145 papers and split AIME
across eight separately-spelled wiki entries. See docs/commit/0058.
"""

from __future__ import annotations

import unittest

from pipelines.common.schema import Paper, PaperSummary
from pipelines.common.store import RecordStore
from pipelines.enrich import concepts as concepts_mod

from .sandbox import Sandbox

SLUG = "test-topic"


def summary_for(paper_id: str, *, datasets: list[str]) -> PaperSummary:
    return PaperSummary(
        paper_id=paper_id,
        one_liner="It does a thing.",
        problem="The thing was hard.",
        method="By reweighting.",
        results="Beats the baseline.",
        relevance={SLUG: "Moves the topic forward."},
        datasets=datasets,
    )


class MergeFixture(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)

    def tearDown(self):
        self.sandbox.close()

    def _paper(self, index: int, dataset_name: str) -> None:
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
        self.store.save_paper_summary(summary_for(paper_id, datasets=[dataset_name]))


class SpellingVariantsMergeTests(MergeFixture):
    def test_year_spellings_collapse_to_one_entity(self):
        for index, spelling in enumerate(["AIME24", "AIME 2024", "AIME2024"], start=1):
            self._paper(index, spelling)
        concepts, live = concepts_mod.rebuild(self.cfg)

        matches = [c for c in concepts.values() if c.slug.startswith("aime")]
        self.assertEqual(len(matches), 1, [c.slug for c in matches])
        self.assertEqual(matches[0].mention_count, 3)

    def test_year_less_spelling_stays_a_separate_entity(self):
        """AIME (no year) is not the same claim as any one sitting of it."""
        self._paper(1, "AIME24")
        self._paper(2, "AIME")
        concepts, live = concepts_mod.rebuild(self.cfg)

        slugs = {c.slug for c in concepts.values()}
        self.assertIn("aime24", slugs)
        self.assertIn("aime", slugs)
        self.assertEqual(len(slugs), 2, "the year-bearing and year-less names must not merge")

    def test_the_merged_entity_still_promotes(self):
        for index, spelling in enumerate(["AIME24", "AIME 2024"], start=1):
            self._paper(index, spelling)
        _, live = concepts_mod.rebuild(self.cfg)
        self.assertIn("aime24", live, "first-seen spelling wins the slug absent a prior ruling")

    def test_a_defined_fragment_is_the_survivor(self):
        """Whichever fragment a person already ruled on wins the merge.

        Without this, which slug speaks for the group would depend on
        dictionary/iteration order rather than on what somebody wrote.
        """
        self._paper(1, "AIME24")
        concepts, _ = concepts_mod.rebuild(self.cfg)
        concept = concepts["aime24"]
        concept.definition = "The 2024 AIME, written by hand."
        self.store.save_concept(concept)

        self._paper(2, "AIME 2024")
        concepts, _ = concepts_mod.rebuild(self.cfg)

        matches = [c for c in concepts.values() if c.slug.startswith("aime")]
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0].slug, "aime24")
        self.assertEqual(matches[0].mention_count, 2)

    def test_unrelated_numeric_datasets_do_not_collide(self):
        """The merge is scoped to a trailing two-digit year, not any digits."""
        self._paper(1, "MATH-500")
        self._paper(2, "MATH500")
        self._paper(3, "GSM8K")
        concepts, _ = concepts_mod.rebuild(self.cfg)

        math_matches = [c for c in concepts.values() if "math" in c.slug]
        self.assertEqual(len(math_matches), 1, [c.slug for c in math_matches])
        self.assertIn("gsm8k", {c.slug for c in concepts.values()})


if __name__ == "__main__":
    unittest.main()
