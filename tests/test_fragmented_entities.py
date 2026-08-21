"""A term spelled two ways, said on the day it happens.

Two records, neither wrong about anything: each holds a fraction of the
evidence, each gets a definition written against that fraction, and nothing
looks broken. One pair in this archive was found at 39 sources against 5.

`pipelines.duplicates` reports four kinds of near-collision and is a command
somebody has to remember to run. Only the narrowest kind is reported at render —
two slugs identical once punctuation is removed — because this fires every pass
and a rule with false positives becomes noise, and because the other three are
judgements rather than spellings: `MATH` under `MATH500` is a subset, and
merging it would make the archive unable to state a distinction it states now.

Reported and never merged. Which name survives is editorial, and
`config/concept-aliases.yaml` is the authored place for it — `Concept.aliases`
is harvested and holds at least one claim that is simply false.
"""

from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from pipelines import render
from pipelines.common.schema import Concept
from pipelines.common.store import RecordStore

from .sandbox import Sandbox

SLUG = "test-topic"


class FragmentedEntityTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.addCleanup(self.sandbox.close)
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)

    def _entity(self, slug: str, name: str, sources: int) -> None:
        self.store.save_concept(
            Concept(slug=slug, name=name, kind="concept", topics=[SLUG],
                    evidence=[{"kind": "paper", "id": f"arxiv:{i}",
                               "title": f"P{i}", "note": ""}
                              for i in range(sources)])
        )

    def test_two_spellings_of_one_name_are_reported(self):
        self._entity("if-eval", "IF-Eval", 3)
        self._entity("ifeval", "IFEval", 1)
        found = render.fragmented_entities(self.cfg)
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0]["slugs"], ["if-eval", "ifeval"])

    def test_the_bigger_record_is_named_first(self):
        """The likelier survivor, so the warning reads the way a merge would."""
        self._entity("if-eval", "IF-Eval", 1)
        self._entity("ifeval", "IFEval", 9)
        found = render.fragmented_entities(self.cfg)
        self.assertEqual(found[0]["slugs"], ["ifeval", "if-eval"])
        self.assertEqual(found[0]["sources"], [9, 1])

    def test_unrelated_entities_are_not_reported(self):
        self._entity("instrumental-variable", "Instrumental Variable", 3)
        self._entity("diffusion-policy", "Diffusion Policy", 3)
        self.assertEqual(render.fragmented_entities(self.cfg), [])

    def test_a_subset_relation_is_not_a_spelling(self):
        """`MATH` under `MATH500` is a distinction the archive states.

        `duplicates` reports it under a different rule, for a person to judge.
        This pass reports spellings only, because it fires every render.
        """
        self._entity("math", "MATH", 12)
        self._entity("math500", "MATH500", 4)
        self.assertEqual(render.fragmented_entities(self.cfg), [])

    def test_a_plural_is_not_reported_here_either(self):
        self._entity("reward-model", "Reward Model", 5)
        self._entity("reward-models", "Reward Models", 2)
        self.assertEqual(render.fragmented_entities(self.cfg), [])

    def _read(self, index: int, entity: str) -> None:
        """A paper whose reading names an entity, which is what harvest sees.

        `render` rebuilds concept records from the summaries, so a hand-made
        evidence list is replaced before the report ever runs. Only readings
        that genuinely name the two spellings survive the pass under test.
        """
        from pipelines.common.schema import Paper, PaperSummary

        paper_id = f"arxiv:2401.0000{index}"
        self.store.save_paper(
            Paper(id=paper_id, title=f"Paper {index}", source="arxiv",
                  published="2024-01-15", year=2024, topics=[SLUG])
        )
        self.store.save_paper_summary(
            PaperSummary(paper_id=paper_id, one_liner="It does a thing.",
                         relevance={SLUG: "Relevant."}, datasets=[entity])
        )

    def test_a_render_counts_them(self):
        self._read(1, "IF-Eval")
        self._read(2, "IF-Eval")
        self._read(3, "IFEval")
        result = render.run(self.cfg, skip_queueing=True)
        self.assertEqual(result["fragmented"], 1)

    def test_an_archive_with_no_fragmentation_reports_zero(self):
        self._read(1, "Instrumental Variable")
        self._read(2, "Diffusion Policy")
        result = render.run(self.cfg, skip_queueing=True)
        self.assertEqual(result["fragmented"], 0)

    def test_it_merges_nothing(self):
        """Which name survives is editorial; this only says there is a choice."""
        self._entity("if-eval", "IF-Eval", 3)
        self._entity("ifeval", "IFEval", 1)
        data = self.cfg.layout.concepts
        snapshot = lambda: {  # noqa: E731
            p.name: hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(data.glob("*.json"))
        }
        before = snapshot()
        render.fragmented_entities(self.cfg)
        self.assertEqual(snapshot(), before)
        self.assertIsNotNone(RecordStore(self.cfg.layout).load_concept("ifeval"))


if __name__ == "__main__":
    unittest.main()
