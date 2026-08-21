"""Settled positions their subject has outgrown.

A finding is the group's own judgement, reached across whatever the archive held
that day. It then sits at the top of every note it bears on — `publish/wiki.py`
puts it above the sources deliberately, in the place reserved for what outranks
them — and it goes on sitting there at thirty sources reading exactly as it did
at three.

That placement is right and is also what makes this the most expensive thing in
the archive to have quietly outgrown.

**Reported, never touched, and unlike a definition it cannot be re-asked.** A
definition is derived from its sources, so a task can hand it back asking what
changed. A finding is a position somebody took; only the group can revisit it,
and a queue task inviting a reader to revise the group's mind would produce
something that is not a finding at all.
"""

from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from pipelines import render
from pipelines.common.schema import Finding, Paper, PaperSummary
from pipelines.common.store import RecordStore
from pipelines.enrich import findings

from .sandbox import Sandbox

SLUG = "test-topic"
NAME = "Instrumental Variable"
STATEMENT = "The group prefers instrumental variables to matching here."


class StaleFindingTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.addCleanup(self.sandbox.close)
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)

    def _papers(self, count: int, *, start: int = 0) -> None:
        for index in range(start, start + count):
            paper_id = f"arxiv:2401.{index:05d}"
            self.store.save_paper(
                Paper(id=paper_id, title=f"Paper {index}", source="arxiv",
                      published="2024-01-15", year=2024, topics=[SLUG])
            )
            self.store.save_paper_summary(
                PaperSummary(paper_id=paper_id, one_liner="It does a thing.",
                             relevance={SLUG: "Relevant."}, concepts=[NAME])
            )
        render.run(self.cfg, skip_queueing=True)

    def _settle(self) -> Finding:
        return findings.record(
            self.cfg,
            {"kind": "decision", "statement": STATEMENT,
             "rationale": "Matching cannot address unobserved confounding.",
             "concepts": [NAME], "topics": [SLUG]},
            self.store,
        )

    # -- recording what it was settled against -------------------------------
    def test_a_finding_records_the_evidence_it_was_settled_against(self):
        self._papers(3)
        self.assertEqual(self._settle().established_against, 3)

    def test_two_entities_sharing_a_paper_count_it_once(self):
        """A union, not a sum. One reading established both."""
        self.store.save_paper(
            Paper(id="arxiv:2401.00001", title="P", source="arxiv", topics=[SLUG])
        )
        self.store.save_paper_summary(
            PaperSummary(paper_id="arxiv:2401.00001", one_liner="x",
                         relevance={SLUG: "y"}, concepts=[NAME, "Another Thing"])
        )
        self.store.save_paper(
            Paper(id="arxiv:2401.00002", title="Q", source="arxiv", topics=[SLUG])
        )
        self.store.save_paper_summary(
            PaperSummary(paper_id="arxiv:2401.00002", one_liner="x",
                         relevance={SLUG: "y"}, concepts=[NAME, "Another Thing"])
        )
        render.run(self.cfg, skip_queueing=True)

        recorded = findings.record(
            self.cfg,
            {"kind": "fact", "statement": "Both entities rest on the same readings.",
             "concepts": [NAME, "Another Thing"], "topics": [SLUG]},
            self.store,
        )
        self.assertEqual(recorded.established_against, 2, "two papers, not four")

    def test_a_finding_naming_no_entity_records_nothing_to_measure(self):
        self._papers(3)
        recorded = findings.record(
            self.cfg,
            {"kind": "decision", "statement": "A decision about nothing in the wiki.",
             "topics": [SLUG]},
            self.store,
        )
        self.assertEqual(recorded.established_against, 0)

    # -- reporting -----------------------------------------------------------
    def test_a_subject_that_has_grown_is_reported(self):
        self._papers(3)
        self._settle()
        self._papers(4, start=3)

        rows = render.stale_findings(self.cfg)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["established_against"], 3)
        self.assertEqual(rows[0]["sources_now"], 7)

    def test_a_finding_still_matching_its_evidence_is_not_reported(self):
        self._papers(3)
        self._settle()
        self.assertEqual(render.stale_findings(self.cfg), [])

    def test_a_finding_recorded_before_the_field_reports_nothing(self):
        """0 means unknown, not none. A finding is not settled against nothing."""
        self._papers(3)
        recorded = self._settle()
        recorded.established_against = 0
        self.store.save_finding(recorded)
        self._papers(4, start=3)
        self.assertEqual(render.stale_findings(self.cfg), [])

    def test_a_retired_finding_is_not_reported(self):
        """It has already been superseded; reporting it would ask twice."""
        self._papers(3)
        first = self._settle()
        second = findings.record(
            self.cfg,
            {"kind": "decision", "statement": "The group now prefers matching after all.",
             "concepts": [NAME], "topics": [SLUG], "supersedes": first.id},
            self.store,
        )
        self._papers(4, start=3)

        reported = [row["id"] for row in render.stale_findings(self.cfg)]
        self.assertNotIn(first.id, reported)
        self.assertIn(second.id, reported)

    def test_re_recording_the_same_statement_moves_the_count(self):
        """Recording it again is a revision; otherwise it reports stale on arrival."""
        self._papers(3)
        self._settle()
        self._papers(4, start=3)
        again = self._settle()
        self.assertEqual(again.established_against, 7)
        self.assertEqual(render.stale_findings(self.cfg), [])

    def test_render_counts_it_in_the_stale_block(self):
        self._papers(3)
        self._settle()
        self._papers(4, start=3)
        result = render.run(self.cfg, skip_queueing=True)
        self.assertEqual(result["stale"]["findings"], 1)

    # -- what it must not do -------------------------------------------------
    def test_reporting_changes_no_record(self):
        """It reports. Only the group revisits its own position."""
        self._papers(3)
        self._settle()
        self._papers(4, start=3)

        data = self.cfg.layout.data
        snapshot = lambda: {  # noqa: E731
            p.relative_to(data).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(data.rglob("*")) if p.is_file()
        }
        before = snapshot()
        render.stale_findings(self.cfg)
        render.report_staleness(self.cfg)
        self.assertEqual(snapshot(), before)

    def test_nothing_queues_a_finding_for_revision(self):
        """A task inviting a reader to revise the group's mind is not a finding."""
        self._papers(3)
        self._settle()
        self._papers(4, start=3)
        render.run(self.cfg)

        from pipelines.enrich.queue import Queue

        kinds = {t.split("__")[0] for t in Queue(self.cfg.layout).pending_ids()}
        self.assertNotIn("finding", kinds)
        self.assertNotIn("synthesis", kinds)


if __name__ == "__main__":
    unittest.main()
