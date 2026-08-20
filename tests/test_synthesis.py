"""Questions that span more readings than any one of them answers.

The queue had three kinds and each is one record answered from its own
material. The work that moves an archive forward is the other shape — *read
these twelve and tell me whether X* — and there was nowhere to put it, so it
happened inside a session, was validated by nothing, and survived in a commit
message.

Two properties carry this.

**A settled synthesis is a finding**, recorded through the validator that owns
findings rather than a second path to the same directory. If it were not, a
statement naming a paper nobody collected would reach `data/findings/` by the
back door, and the refusal `enrich/findings.py` performs would be decorative.

**Leaving a question open is a real answer.** Evidence often does not settle
things, and a task demanding a statement asks the reader to invent one. A
hedged sentence is worse than an honest open question, because nothing later can
tell the two apart.
"""

from __future__ import annotations

import unittest

from pipelines import render
from pipelines.common.schema import Concept, Paper, PaperSummary
from pipelines.common.store import RecordStore
from pipelines.enrich import synthesis
from pipelines.enrich.queue import Queue, validate_result

from .sandbox import Sandbox

SLUG = "test-topic"
QUESTION = "Do these readings agree on what an instrumental variable requires?"

SETTLED = {
    "kind": "fact",
    "statement": "The readings agree on exclusion but not on monotonicity.",
    "rationale": "Two state it explicitly; the third assumes it silently.",
    "papers": ["arxiv:2401.00001"],
    "topics": [SLUG],
}
OPEN = {"unresolved": "None of the three states its monotonicity assumption."}


class SynthesisTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.addCleanup(self.sandbox.close)
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)
        self.queue = Queue(self.cfg.layout, cfg=self.cfg)

        self.store.save_paper(
            Paper(id="arxiv:2401.00001", title="A Paper", source="arxiv",
                  abstract="An abstract.", topics=[SLUG])
        )
        self.store.save_paper_summary(
            PaperSummary(paper_id="arxiv:2401.00001",
                         one_liner="It estimates an effect.",
                         relevance={SLUG: "Relevant."})
        )
        self.store.save_concept(
            Concept(slug="instrumental-variable", name="Instrumental Variable",
                    kind="concept", definition="A variable that shifts treatment.",
                    topics=[SLUG])
        )

    def _file(self, **kwargs) -> str:
        return synthesis.file_question(
            self.cfg, QUESTION, queue=self.queue, **kwargs
        )

    # -- filing --------------------------------------------------------------
    def test_a_question_becomes_a_task_carrying_its_evidence(self):
        task_id = self._file(concepts=["instrumental-variable"],
                             papers=["arxiv:2401.00001"])
        task = self.queue.load(task_id)
        self.assertEqual(task["kind"], "synthesis")
        self.assertEqual(task["payload"]["question"], QUESTION)
        kinds = [e["kind"] for e in task["attachments"]["evidence"]]
        self.assertEqual(sorted(kinds), ["concept", "paper"])
        self.assertIn(SLUG, task["topics"], "topics derived from the evidence")

    def test_evidence_the_archive_does_not_have_is_refused(self):
        """A question answered from evidence that does not exist is answered
        from memory, which is what this whole arrangement prevents."""
        with self.assertRaises(ValueError) as caught:
            self._file(papers=["arxiv:9999.99999"])
        self.assertIn("not in the archive", str(caught.exception))

    def test_the_same_question_twice_is_one_task(self):
        first = self._file(papers=["arxiv:2401.00001"])
        second = self._file(papers=["arxiv:2401.00001"])
        self.assertTrue(first)
        self.assertEqual(second, "", "content-addressed on the question")

    def test_a_question_too_short_to_argue_with_is_refused(self):
        with self.assertRaises(ValueError):
            synthesis.file_question(self.cfg, "why?", queue=self.queue)

    # -- answering -----------------------------------------------------------
    def test_a_settled_answer_is_accepted(self):
        task_id = self._file(papers=["arxiv:2401.00001"])
        self.queue.complete(task_id, SETTLED)
        self.assertEqual(self.queue.pending_ids(kind="synthesis"), [])

    def test_an_open_answer_is_accepted(self):
        task_id = self._file(papers=["arxiv:2401.00001"])
        self.queue.complete(task_id, OPEN)
        self.assertEqual(self.queue.pending_ids(kind="synthesis"), [])

    def test_saying_nothing_at_all_is_refused(self):
        """Silence is the one answer carrying no information."""
        task_id = self._file(papers=["arxiv:2401.00001"])
        with self.assertRaises(ValueError) as caught:
            self.queue.complete(task_id, {"rationale": "hmm"})
        self.assertIn("unresolved", str(caught.exception))

    def test_settling_and_not_settling_at_once_is_refused(self):
        task_id = self._file(papers=["arxiv:2401.00001"])
        with self.assertRaises(ValueError):
            self.queue.complete(task_id, {**SETTLED, **OPEN})

    def test_an_answer_is_checked_as_the_finding_it_becomes(self):
        """Not a laxer copy of the rule — the findings validator itself."""
        task_id = self._file(papers=["arxiv:2401.00001"])
        with self.assertRaises(ValueError) as caught:
            self.queue.complete(
                task_id, {**SETTLED, "papers": ["arxiv:9999.99999"]}
            )
        self.assertIn("not in the archive", str(caught.exception))

    def test_a_topic_nobody_tracks_is_refused(self):
        task_id = self._file(papers=["arxiv:2401.00001"])
        with self.assertRaises(ValueError):
            self.queue.complete(task_id, {**SETTLED, "topics": ["invented"]})

    def test_without_the_archive_only_the_shape_is_checked(self):
        """The same graceful degradation `topics` and `attachments` have."""
        self.assertEqual(
            validate_result("synthesis", {**SETTLED, "papers": ["arxiv:9999"]}), []
        )
        self.assertTrue(validate_result("synthesis", {"rationale": "x"}))

    # -- applying ------------------------------------------------------------
    def test_a_settled_answer_becomes_a_finding(self):
        task_id = self._file(papers=["arxiv:2401.00001"])
        self.queue.complete(task_id, SETTLED)
        render.run(self.cfg)

        statements = [f.statement for f in self.store.iter_findings()]
        self.assertIn(SETTLED["statement"], statements)

    def test_an_open_answer_records_no_finding(self):
        """And that is a success, not a skipped task."""
        task_id = self._file(papers=["arxiv:2401.00001"])
        self.queue.complete(task_id, OPEN)
        result = render.run(self.cfg)

        self.assertEqual(list(self.store.iter_findings()), [])
        self.assertEqual(result["applied"]["synthesis"], 1)
        self.assertEqual(result["applied"]["skipped"], 0)

    def test_the_open_question_and_its_reason_survive(self):
        """Where the next session finds them, which a deleted task would not."""
        task_id = self._file(papers=["arxiv:2401.00001"])
        self.queue.complete(task_id, OPEN)
        render.run(self.cfg)

        archived = self.queue.load(task_id)
        self.assertEqual(archived["payload"]["question"], QUESTION)
        self.assertEqual(archived["result"]["unresolved"], OPEN["unresolved"])

    def test_the_finding_reaches_the_wiki(self):
        task_id = self._file(papers=["arxiv:2401.00001"])
        self.queue.complete(
            task_id, {**SETTLED, "concepts": ["Instrumental Variable"]}
        )
        render.run(self.cfg)
        page = (self.cfg.layout.wiki / "findings.md").read_text(encoding="utf-8")
        self.assertIn(SETTLED["statement"], page)


if __name__ == "__main__":
    unittest.main()
