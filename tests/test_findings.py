"""What the group settled.

Every other record here comes from a collector. This one comes from a
conversation, which is exactly why it goes through a validator: a finding that
can quietly name a topic that does not exist, or a paper nobody collected, is
worse than no finding at all.
"""

from __future__ import annotations

import unittest

from pipelines.common.schema import Paper, PaperSummary
from pipelines.common.store import RecordStore
from pipelines.enrich import findings

from .sandbox import Sandbox

STATEMENT = ("We track partial interference rather than the general case, "
             "because every usable identification result assumes it.")


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)

    def tearDown(self):
        self.sandbox.close()

    def _errors(self, **extra):
        payload = {"kind": "decision", "statement": STATEMENT}
        payload.update(extra)
        return findings.validate(self.cfg, payload, self.store)

    def test_a_well_formed_finding_passes(self):
        self.assertEqual(self._errors(topics=["test-topic"]), [])

    def test_an_unknown_topic_is_rejected(self):
        """Topics are a closed set in config, so a wrong slug is a typo."""
        self.assertTrue(any("not a tracked topic" in e
                            for e in self._errors(topics=["nope"])))

    def test_a_paper_not_in_the_archive_is_rejected(self):
        errors = self._errors(papers=["arxiv:9999.99999"])
        self.assertTrue(any("not in the archive" in e for e in errors))

    def test_a_concept_the_wiki_has_not_seen_is_allowed(self):
        """The wiki harvests concepts from summaries; a finding may lead them."""
        self.assertEqual(self._errors(concepts=["Something Nobody Wrote Up Yet"]), [])

    def test_a_label_is_not_a_finding(self):
        self.assertTrue(any("too short" in e for e in self._errors(statement="nope")))

    def test_the_kind_is_constrained(self):
        self.assertTrue(any("kind" in e for e in self._errors(kind="opinion")))

    def test_superseding_an_unknown_finding_is_rejected(self):
        errors = self._errors(supersedes="finding:doesnotexist")
        self.assertTrue(any("unknown finding" in e for e in errors))

    def test_a_non_object_is_rejected(self):
        self.assertEqual(findings.validate(self.cfg, ["nope"], self.store),
                         ["finding must be a JSON object"])


class RecordTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)

    def tearDown(self):
        self.sandbox.close()

    def _add(self, statement=STATEMENT, **extra):
        payload = {"kind": "decision", "statement": statement}
        payload.update(extra)
        return findings.record(self.cfg, payload, self.store)

    def test_an_invalid_finding_raises_rather_than_storing(self):
        with self.assertRaises(ValueError):
            self._add(topics=["nope"])
        self.assertEqual(list(self.store.iter_findings()), [])

    def test_the_same_statement_twice_is_one_finding(self):
        first = self._add()
        second = self._add(concepts=["Partial Interference"])
        self.assertEqual(first.id, second.id)
        self.assertEqual(len(list(self.store.iter_findings())), 1)
        self.assertEqual(self.store.load_finding(first.id).concepts,
                         ["Partial Interference"])

    def test_a_supersede_retires_the_old_one_without_deleting_it(self):
        old = self._add()
        new = self._add(statement="We now also track the general case, since "
                                  "runnable estimators exist for it.",
                        supersedes=old.id)
        stored_old = self.store.load_finding(old.id)
        self.assertEqual(stored_old.superseded_by, new.id)
        self.assertFalse(stored_old.live)
        self.assertIsNotNone(stored_old.statement)

    def test_live_excludes_what_was_retired(self):
        old = self._add()
        self._add(statement="A different settled thing entirely, at length.",
                  supersedes=old.id)
        self.assertEqual([f.live for f in findings.live(self.store)], [True])

    def test_a_finding_cannot_supersede_itself(self):
        one = self._add()
        with self.assertRaises(ValueError):
            findings.retire(self.cfg, one.id, one.id, self.store)

    def test_retiring_an_unknown_finding_raises(self):
        one = self._add()
        with self.assertRaises(FileNotFoundError):
            findings.retire(self.cfg, "finding:nope", one.id, self.store)

    def test_a_collected_paper_may_be_cited(self):
        self.store.save_paper(Paper(id="arxiv:2401.1", title="A paper", source="arxiv"))
        self.assertEqual(self._add(papers=["arxiv:2401.1"]).papers, ["arxiv:2401.1"])


class RenderTests(unittest.TestCase):
    """A finding has to reach the wiki, or recording it changes nothing."""

    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)
        for i in range(2):
            pid = f"arxiv:2401.0000{i}"
            self.store.save_paper(Paper(id=pid, title=f"Paper {i}", source="arxiv",
                                        topics=["test-topic"], scores={"test-topic": 0.8}))
            self.store.save_paper_summary(
                PaperSummary(paper_id=pid, one_liner="x.",
                             concepts=["Partial Interference"])
            )
        findings.record(self.cfg, {
            "kind": "decision", "statement": STATEMENT,
            "rationale": "Settled after reading the bounds literature.",
            "concepts": ["Partial Interference"], "topics": ["test-topic"],
        }, self.store)

    def tearDown(self):
        self.sandbox.close()

    def _render(self):
        from pipelines import render

        return render.run(self.cfg, skip_queueing=True)

    def test_the_concept_note_carries_what_was_settled(self):
        self._render()
        note = (self.cfg.layout.wiki / "concepts" / "partial-interference.md").read_text()
        self.assertIn("What we have settled", note)
        self.assertIn(STATEMENT, note)
        self.assertIn("bounds literature", note)

    def test_the_big_picture_page_is_grouped_by_topic(self):
        self._render()
        page = (self.cfg.layout.wiki / "findings.md").read_text()
        self.assertIn("## Test Topic", page)
        self.assertIn(STATEMENT, page)

    def test_a_retired_finding_leaves_the_note_but_stays_on_the_page(self):
        findings.record(self.cfg, {
            "kind": "decision",
            "statement": "We now also track the general case, since runnable "
                         "estimators exist for it.",
            "concepts": ["Partial Interference"], "topics": ["test-topic"],
            "supersedes": findings.live(self.store)[0].id,
        }, self.store)
        self._render()
        note = (self.cfg.layout.wiki / "concepts" / "partial-interference.md").read_text()
        page = (self.cfg.layout.wiki / "findings.md").read_text()
        self.assertNotIn(STATEMENT, note)      # the note shows the current position
        self.assertIn("Superseded", page)      # the page keeps the history
        self.assertIn(STATEMENT, page)

    def test_the_map_flags_a_settled_entity(self):
        self._render()
        graph = (self.cfg.layout.wiki / "graph.html").read_text()
        self.assertIn('class="settled', graph)

    def test_render_reports_how_many_are_live(self):
        self.assertEqual(self._render()["wiki"]["settled"], 1)


if __name__ == "__main__":
    unittest.main()
