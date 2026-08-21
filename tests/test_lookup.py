"""Narrow questions the archive cannot answer about itself.

Much of what sits unresolved is confirmation rather than judgement: the
published spelling, whether two names are one benchmark, where a PDF lives.
Each is one look outside the archive, and there was nowhere to file that look.

**Every answer must cite a recorded reference.** That is the whole mechanism —
a reference carries a URL, a retrieval date and the passage relied on, so
requiring one is the only way this pipeline can tell "I looked this up" from
"I remember this". On a question whose entire value is that somebody checked,
there is nothing else to check.

**`unknown` needs no reference and is always available.** Refusing it would push
a reader towards inventing an answer, which is the failure being guarded.

**A confirmed identity writes nothing.** An alias is a merge mechanism, and a
wrong merge does not mislabel an entity — it fuses two, and the fused note looks
healthy afterwards. So it files a definition revision and a reader puts the
alias in through the validator that owns aliases.
"""

from __future__ import annotations

import unittest

from pipelines import render
from pipelines.common.schema import Concept, Paper, reference_id
from pipelines.common.store import RecordStore
from pipelines.enrich import lookup, references
from pipelines.enrich.queue import Queue

from .sandbox import Sandbox

SLUG = "test-topic"
PAGE = {
    "url": "https://github.com/example/clap",
    "title": "example/clap",
    "kind": "code",
    "retrieved_at": "2026-08-21",
    "quoted": "The repository is named C-LAP throughout.",
}


class LookupTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.addCleanup(self.sandbox.close)
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)
        self.queue = Queue(self.cfg.layout, cfg=self.cfg)
        self.store.save_paper(
            Paper(id="arxiv:2401.00001", title="A Paper", source="arxiv",
                  topics=[SLUG])
        )
        self.store.save_concept(
            Concept(slug="c-lap", name="C-LAP", kind="method",
                    definition="A contrastive latent action policy.",
                    evidence=[{"kind": "paper", "id": "arxiv:2401.00001",
                               "title": "A Paper", "note": ""}],
                    topics=[SLUG])
        )
        self.reference = references.record(self.cfg, PAGE, self.store)

    def _file(self, subject: str, **kwargs) -> str:
        return lookup.file_lookup(
            self.cfg, subject, kwargs.pop("about", "C-LAP"),
            queue=self.queue, **kwargs
        )

    def _answer(self, **extra) -> dict:
        base = {"answer": "C-LAP", "rationale": "Read off the repository.",
                "references": [self.reference.id]}
        base.update(extra)
        return base

    # -- filing --------------------------------------------------------------
    def test_a_lookup_becomes_a_task_naming_its_subject(self):
        task = self.queue.load(self._file("spelling"))
        self.assertEqual(task["kind"], "lookup")
        self.assertEqual(task["payload"]["subject"], "spelling")
        self.assertIn("C-LAP", task["instructions"])

    def test_the_same_question_twice_is_one_task(self):
        self.assertTrue(self._file("spelling"))
        self.assertEqual(self._file("spelling"), "")

    def test_a_lookup_about_a_paper_takes_its_title_and_topics(self):
        task = self.queue.load(
            self._file("document", about="", paper="arxiv:2401.00001")
        )
        self.assertEqual(task["payload"]["about"], "A Paper")
        self.assertEqual(task["topics"], [SLUG])

    def test_a_paper_the_archive_lacks_is_refused(self):
        with self.assertRaises(ValueError):
            self._file("document", paper="arxiv:9999.99999")

    def test_an_unknown_subject_is_refused(self):
        with self.assertRaises(ValueError):
            self._file("vibes")

    # -- the rule that carries the feature -----------------------------------
    def test_an_answer_with_no_reference_is_refused(self):
        """The only mechanical difference between looking it up and recalling it."""
        task_id = self._file("spelling")
        with self.assertRaises(ValueError) as caught:
            self.queue.complete(task_id, self._answer(references=[]))
        self.assertIn("reference", str(caught.exception))

    def test_an_answer_citing_an_unrecorded_reference_is_refused(self):
        task_id = self._file("spelling")
        with self.assertRaises(ValueError):
            self.queue.complete(
                task_id, self._answer(references=["web:deadbeefdeadbeef"])
            )

    def test_an_answer_with_a_reference_is_accepted(self):
        task_id = self._file("spelling")
        self.queue.complete(task_id, self._answer())
        self.assertEqual(self.queue.pending_ids(kind="lookup"), [])

    def test_unknown_needs_no_reference(self):
        task_id = self._file("spelling")
        self.queue.complete(
            task_id,
            {"unknown": True, "rationale": "The venue page is behind a login."},
        )
        self.assertEqual(self.queue.pending_ids(kind="lookup"), [])

    def test_unknown_still_needs_to_say_what_was_tried(self):
        """So the next attempt starts from somewhere rather than nothing."""
        task_id = self._file("spelling")
        with self.assertRaises(ValueError) as caught:
            self.queue.complete(task_id, {"unknown": True})
        self.assertIn("rationale", str(caught.exception))

    def test_unknown_and_an_answer_at_once_is_refused(self):
        task_id = self._file("spelling")
        with self.assertRaises(ValueError):
            self.queue.complete(task_id, self._answer(unknown=True))

    def test_a_document_lookup_must_answer_with_a_url(self):
        task_id = self._file("document", paper="arxiv:2401.00001")
        with self.assertRaises(ValueError) as caught:
            self.queue.complete(task_id, self._answer(answer="on arxiv somewhere"))
        self.assertIn("URL", str(caught.exception))

    def test_an_identity_lookup_answers_yes_or_no(self):
        task_id = self._file("identity", about="C-LAP and CLAP")
        with self.assertRaises(ValueError):
            self.queue.complete(task_id, self._answer(answer="probably"))

    # -- applying ------------------------------------------------------------
    def test_a_document_answer_fills_the_url_backfill_needs(self):
        task_id = self._file("document", about="", paper="arxiv:2401.00001")
        self.queue.complete(
            task_id, self._answer(answer="https://arxiv.org/pdf/2401.00001")
        )
        render.run(self.cfg)
        paper = RecordStore(self.cfg.layout).load_paper("arxiv:2401.00001")
        self.assertEqual(paper.pdf_url, "https://arxiv.org/pdf/2401.00001")

    def test_a_document_answer_does_not_replace_one_already_there(self):
        """The reader answered "where is it", not "which is better"."""
        paper = self.store.load_paper("arxiv:2401.00001")
        paper.pdf_url = "https://example.test/original.pdf"
        self.store.save_paper(paper)

        task_id = self._file("document", about="", paper="arxiv:2401.00001")
        self.queue.complete(task_id, self._answer(answer="https://elsewhere.test/x.pdf"))
        render.run(self.cfg)
        self.assertEqual(
            RecordStore(self.cfg.layout).load_paper("arxiv:2401.00001").pdf_url,
            "https://example.test/original.pdf",
        )

    def test_a_confirmed_identity_never_writes_an_alias(self):
        """A wrong merge fuses two entities and the fused note looks healthy."""
        task_id = self._file("identity", about="C-LAP and CLAP", concept="c-lap")
        self.queue.complete(task_id, self._answer(answer="yes"))
        render.run(self.cfg)

        concept = RecordStore(self.cfg.layout).load_concept("c-lap")
        self.assertEqual(concept.aliases, [], "no alias was written by the applier")

    def test_a_confirmed_identity_asks_for_the_definition_again(self):
        """So the alias goes in through the validator that owns aliases."""
        task_id = self._file("identity", about="C-LAP and CLAP", concept="c-lap")
        self.queue.complete(task_id, self._answer(answer="yes"))
        render.run(self.cfg)

        pending = self.queue.pending_ids(kind="concept")
        self.assertEqual(pending, [Queue.task_id("concept", "C-LAP")])
        task = self.queue.load(pending[0])
        self.assertIn("previous_definition", task["payload"])

    def test_an_unknown_answer_changes_nothing_and_still_counts(self):
        task_id = self._file("document", about="", paper="arxiv:2401.00001")
        self.queue.complete(
            task_id, {"unknown": True, "rationale": "No PDF is published."}
        )
        result = render.run(self.cfg)
        self.assertEqual(result["applied"]["lookup"], 1)
        self.assertEqual(result["applied"]["skipped"], 0)
        self.assertEqual(
            RecordStore(self.cfg.layout).load_paper("arxiv:2401.00001").pdf_url, ""
        )

    def test_what_was_tried_survives_in_the_archived_task(self):
        task_id = self._file("spelling")
        self.queue.complete(
            task_id, {"unknown": True, "rationale": "The venue page is gone."}
        )
        render.run(self.cfg)
        self.assertEqual(
            self.queue.load(task_id)["result"]["rationale"], "The venue page is gone."
        )


if __name__ == "__main__":
    unittest.main()
