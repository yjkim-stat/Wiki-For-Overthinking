"""A paper reading that names no model.

LOCAL: `models` — see docs/LOCAL-DELTAS.md.

The field is optional and stays optional: a paper that evaluates no checkpoint
answers with an empty list, and requiring a non-empty one would force a guess
where the honest answer is silence — the reasoning that keeps `results`
optional too.

The cost is that an omitted list and a genuine "none" produce **identical
records**. Nine consecutive readings went out empty before anybody noticed, and
it was the second time this field had gone missing quietly: the first was an
applier that dropped every `models` a reader submitted, for eighty summaries.

So the cause is addressed where it lives — the reader follows the instructions,
and the instructions never mentioned the field — and the symptom is counted
where this archive already looks for rot.
"""

from __future__ import annotations

import unittest

from pipelines import render
from pipelines.common.llm import paper_instructions
from pipelines.common.schema import Paper, PaperSummary
from pipelines.common.store import RecordStore

from .sandbox import Sandbox

SLUG = "test-topic"
TOPICS = [{"slug": SLUG, "name": "Test Topic", "description": ""}]


class InstructionsTests(unittest.TestCase):
    """The cause: the prose a reader follows never named the field."""

    def test_the_prompt_names_the_field(self):
        self.assertIn("models", paper_instructions(TOPICS))

    def test_the_prompt_says_empty_is_an_answer(self):
        """Requiring a non-empty list would force a guess."""
        text = paper_instructions(TOPICS)
        self.assertIn("empty list", text)
        self.assertIn("real answer", text)

    def test_the_prompt_says_why_leaving_it_out_is_different(self):
        """The whole defect: absent and none are the same record afterwards."""
        self.assertIn("tell the two apart", paper_instructions(TOPICS))

    def test_a_hand_filed_pdf_is_told_too(self):
        from pipelines.common.llm import local_pdf_instructions

        self.assertIn("models", local_pdf_instructions(TOPICS))


class CountTests(unittest.TestCase):
    """The symptom, counted where the archive already looks for rot."""

    def setUp(self):
        self.sandbox = Sandbox()
        self.addCleanup(self.sandbox.close)
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)

    def _read(self, index: int, models: list[str]) -> None:
        paper_id = f"arxiv:2401.0000{index}"
        self.store.save_paper(
            Paper(id=paper_id, title=f"Paper {index}", source="arxiv", topics=[SLUG])
        )
        self.store.save_paper_summary(
            PaperSummary(paper_id=paper_id, one_liner="It does a thing.",
                         relevance={SLUG: "Relevant."}, models=models)
        )

    def test_a_reading_that_named_none_is_counted(self):
        self._read(1, [])
        self.assertEqual(render.readings_without_models(self.cfg),
                         ["arxiv:2401.00001"])

    def test_a_reading_that_named_one_is_not(self):
        self._read(1, ["Qwen3-8B"])
        self.assertEqual(render.readings_without_models(self.cfg), [])

    def test_an_unread_paper_is_not_counted(self):
        """It has no reading to have answered."""
        self.store.save_paper(
            Paper(id="arxiv:2401.00009", title="Unread", source="arxiv",
                  topics=[SLUG])
        )
        self.assertEqual(render.readings_without_models(self.cfg), [])

    def test_render_reports_the_count_beside_the_other_rot(self):
        self._read(1, [])
        self._read(2, ["Qwen3-8B"])
        result = render.run(self.cfg, skip_queueing=True)
        self.assertEqual(result["stale"]["readings_without_models"], 1)

    def test_it_is_a_count_not_a_refusal(self):
        """Empty stays a valid answer; nothing is rejected or rewritten."""
        self._read(1, [])
        before = self.store.load_paper_summary("arxiv:2401.00001").models
        render.run(self.cfg, skip_queueing=True)
        after = RecordStore(self.cfg.layout).load_paper_summary(
            "arxiv:2401.00001"
        ).models
        self.assertEqual(after, before)


if __name__ == "__main__":
    unittest.main()
