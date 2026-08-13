"""The authored concept-alias map, and the harvest honouring it.

**Ours, not the template's**, in a file of its own for the reason
`docs/LOCAL-DELTAS.md` gives: the delta's call sites are one line each in
`common/config.py` and `enrich/concepts.py`, and a template update that replaces
either would revert it without failing any test the template owns.

Two properties are load-bearing and each has a class here. The map must refuse
anything whose result would depend on iteration order or on which of two
spellings a reader happened to write — a silently wrong merge is worse than the
fragmentation it fixes, because it collapses two entities into one record with
no trace. And a deployment with no map must behave exactly as it did before the
delta existed, since that is what every other test in the suite assumes.
"""

from __future__ import annotations

import textwrap
import unittest
from pathlib import Path

from pipelines.common.schema import Paper, PaperSummary
from pipelines.common.store import RecordStore
from pipelines.enrich import concepts as concepts_mod
from pipelines.local import aliases as aliases_mod

from .sandbox import Sandbox

SLUG = "test-topic"


def paper(index: int) -> Paper:
    return Paper(
        id=f"arxiv:2401.0000{index}",
        title=f"Paper {index}: causal inference",
        source="arxiv",
        authors=["Ada Lovelace"],
        abstract="We estimate effects with an instrumental variable.",
        published="2024-01-15",
        year=2024,
        topics=[SLUG],
        scores={SLUG: 0.8},
    )


class AliasFileTests(unittest.TestCase):
    """Parsing, and what the parser refuses."""

    def setUp(self):
        self.sandbox = Sandbox()
        self.path = self.sandbox.root / "config" / aliases_mod.FILENAME

    def tearDown(self):
        self.sandbox.close()
        aliases_mod.reset()

    def _write(self, body: str) -> Path:
        self.path.write_text(textwrap.dedent(body).lstrip(), encoding="utf-8")
        return self.path

    def test_a_missing_file_is_an_empty_map(self):
        # The normal case for a deployment that has never needed a ruling.
        self.assertEqual(aliases_mod.load(self.path), {})

    def test_names_and_slugs_are_both_accepted(self):
        # Whichever the person ruling had in front of them.
        self._write(
            """
            merge:
              AIME 2024:
                - AIME24
              math500:
                - MATH-500
            """
        )
        self.assertEqual(
            aliases_mod.load(self.path),
            {"aime24": "aime-2024", "math-500": "math500"},
        )

    def test_an_alias_of_itself_is_refused(self):
        # Always a typo in one of the two spellings, and silently a no-op.
        self._write(
            """
            merge:
              AIME 2024:
                - aime 2024
            """
        )
        with self.assertRaises(aliases_mod.AliasError):
            aliases_mod.load(self.path)

    def test_one_alias_claimed_by_two_entities_is_refused(self):
        self._write(
            """
            merge:
              AIME 2024:
                - AIME24
              AIME 2025:
                - AIME24
            """
        )
        with self.assertRaises(aliases_mod.AliasError):
            aliases_mod.load(self.path)

    def test_a_chain_is_refused(self):
        # a -> b -> c resolves differently depending on iteration order, and
        # the fix is always to point the first entry at the end of the chain.
        self._write(
            """
            merge:
              MATH500:
                - MATH-500
              MATH-500:
                - math 500 subset
            """
        )
        with self.assertRaises(aliases_mod.AliasError):
            aliases_mod.load(self.path)


class HarvestTests(unittest.TestCase):
    """Two spellings, one record — and no change when nothing is declared."""

    def setUp(self):
        self.sandbox = Sandbox()

    def tearDown(self):
        self.sandbox.close()
        aliases_mod.reset()

    def _declare(self, body: str) -> None:
        (self.sandbox.root / "config" / aliases_mod.FILENAME).write_text(
            textwrap.dedent(body).lstrip(), encoding="utf-8"
        )

    def _harvest(self, *spellings: str) -> dict:
        cfg = self.sandbox.config()  # installs whatever map is on disk
        store = RecordStore(cfg.layout)
        for index, name in enumerate(spellings, start=1):
            item = paper(index)
            store.save_paper(item)
            store.save_paper_summary(
                PaperSummary(
                    paper_id=item.id,
                    one_liner=f"Paper {index} does a thing.",
                    datasets=[name],
                )
            )
        return concepts_mod.harvest(cfg)

    def test_without_a_map_two_spellings_stay_two_records(self):
        # The behaviour every other test in the suite was written against.
        harvested = self._harvest("AIME24", "AIME 2024")
        self.assertIn("aime24", harvested)
        self.assertIn("aime-2024", harvested)

    def test_a_declared_alias_folds_the_evidence_into_one_record(self):
        self._declare(
            """
            merge:
              AIME 2024:
                - AIME24
            """
        )
        harvested = self._harvest("AIME24", "AIME 2024")
        self.assertNotIn("aime24", harvested)
        concept = harvested["aime-2024"]
        self.assertEqual(len(concept.evidence), 2, "both papers are evidence")
        self.assertIn("AIME24", concept.aliases, "the folded spelling is recorded")

    def test_the_canonical_name_wins_even_when_the_alias_is_seen_first(self):
        # `name` is what the wiki note is titled, and the harvest takes it from
        # whichever summary it reaches first — so the redirect has to decide it.
        self._declare(
            """
            merge:
              AIME 2024:
                - AIME24
            """
        )
        # The alias spelling arrives first, so without the ruling the record
        # would be called *AIME24* while living at slug `aime-2024`.
        harvested = self._harvest("AIME24", "AIME 2024")
        concept = harvested["aime-2024"]
        self.assertEqual(concept.name, "AIME 2024")
        self.assertIn("AIME24", concept.aliases)

    def test_an_unruled_entity_still_takes_its_name_from_its_evidence(self):
        self._declare(
            """
            merge:
              AIME 2024:
                - AIME24
            """
        )
        harvested = self._harvest("GRPO Variant", "AIME24")
        self.assertEqual(harvested["grpo-variant"].name, "GRPO Variant")

    def test_related_edges_point_at_the_canonical(self):
        # A dangling edge is not visible in any note; it just fails to render.
        self._declare(
            """
            merge:
              AIME 2024:
                - AIME24
            """
        )
        cfg = self.sandbox.config()
        store = RecordStore(cfg.layout)
        item = paper(1)
        store.save_paper(item)
        store.save_paper_summary(
            PaperSummary(
                paper_id=item.id,
                one_liner="Paper 1 does a thing.",
                datasets=["AIME24"],
                methods=["GRPO"],
            )
        )
        harvested = concepts_mod.harvest(cfg)
        self.assertIn("aime-2024", harvested["grpo"].related)
        self.assertNotIn("aime24", harvested["grpo"].related)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
