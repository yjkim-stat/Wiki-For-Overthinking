"""Telling the reader of a note that the prose below it is behind.

Analysis under `<!-- auto:end -->` can declare what it was written against, and
`render` has reported when the evidence passed that since note 0021. A log line
is a poor place for it: the person who needs to know is whoever is **reading the
note**, and they will never see the run that mentioned it.

Nothing here touches the prose. It cannot: everything after the marker is
preserved for ever, and only its author can revise it. The notice goes at the
foot of the generated block — immediately above the prose it is about, inside
the one part of the file this code is allowed to write.
"""

from __future__ import annotations

import unittest

from pipelines import render
from pipelines.common.schema import Paper, PaperSummary
from pipelines.common.store import RecordStore
from pipelines.publish import wiki

from .sandbox import Sandbox

SLUG = "test-topic"
NAME = "Instrumental Variable"
PROSE = "\n## Notes\n\nMy own reading of this.\n\n<!-- analysis-sources: {n} -->\n"


class OutgrownAnalysisTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.addCleanup(self.sandbox.close)
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)

    def _papers(self, count: int) -> None:
        for index in range(count):
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

    def _note(self):
        return wiki.note_path(self.cfg.layout, "concept", "instrumental-variable")

    def _write_prose(self, declared: int) -> None:
        path = self._note()
        path.write_text(
            path.read_text(encoding="utf-8") + PROSE.format(n=declared),
            encoding="utf-8",
        )

    def test_a_note_whose_prose_is_behind_says_so(self):
        self._papers(3)
        self._write_prose(declared=2)
        render.run(self.cfg, skip_queueing=True)

        text = self._note().read_text(encoding="utf-8")
        self.assertIn("written against 2 source(s); there are now 3", text)

    def test_the_notice_sits_above_the_prose_not_inside_it(self):
        """Inside the generated block, which is the only part this may write."""
        self._papers(3)
        self._write_prose(declared=2)
        render.run(self.cfg, skip_queueing=True)

        text = self._note().read_text(encoding="utf-8")
        _, end = wiki._markers(self.cfg)
        auto, tail = text.split(end, 1)
        self.assertIn("there are now 3", auto)
        self.assertNotIn("there are now 3", tail)

    def test_the_prose_itself_is_untouched(self):
        self._papers(3)
        self._write_prose(declared=2)
        render.run(self.cfg, skip_queueing=True)

        _, end = wiki._markers(self.cfg)
        tail = self._note().read_text(encoding="utf-8").split(end, 1)[1]
        self.assertIn("My own reading of this.", tail)
        self.assertIn("<!-- analysis-sources: 2 -->", tail)

    def test_prose_that_matches_its_evidence_gets_no_notice(self):
        self._papers(3)
        self._write_prose(declared=3)
        render.run(self.cfg, skip_queueing=True)
        self.assertNotIn("there are now", self._note().read_text(encoding="utf-8"))

    def _auto_block(self) -> str:
        _, end = wiki._markers(self.cfg)
        return self._note().read_text(encoding="utf-8").split(end, 1)[0]

    def test_prose_with_no_marker_gets_no_notice(self):
        """The marker is opt-in; some prose genuinely does not depend on a count.

        Asserted on the absence of any blockquote rather than on the notice's
        current wording — the notice is the only thing the generated block ever
        emits as one, and a test looking for a phrase passes against a notice
        that says something else.
        """
        self._papers(3)
        path = self._note()
        path.write_text(
            path.read_text(encoding="utf-8") + "\n## Notes\n\nJust a thought.\n",
            encoding="utf-8",
        )
        render.run(self.cfg, skip_queueing=True)
        self.assertNotIn("\n> ", self._auto_block())

    def test_updating_the_marker_clears_the_notice(self):
        """Saying it was checked is a real answer, and the note stops nagging."""
        self._papers(3)
        self._write_prose(declared=2)
        render.run(self.cfg, skip_queueing=True)
        self.assertIn("there are now 3", self._note().read_text(encoding="utf-8"))

        path = self._note()
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "<!-- analysis-sources: 2 -->", "<!-- analysis-sources: 3 -->"
            ),
            encoding="utf-8",
        )
        render.run(self.cfg, skip_queueing=True)
        self.assertNotIn("there are now", self._note().read_text(encoding="utf-8"))

    def test_the_notice_does_not_accumulate(self):
        self._papers(3)
        self._write_prose(declared=2)
        for _ in range(3):
            render.run(self.cfg, skip_queueing=True)
        text = self._note().read_text(encoding="utf-8")
        self.assertEqual(text.count("there are now 3"), 1)

    def test_an_over_declared_marker_is_shown_too(self):
        """The other direction, which `stale_analysis` reports since note 0090.

        A marker above the note's count means the prose may cite evidence the
        note no longer holds, which is the worse of the two and looks identical
        from here.
        """
        self._papers(2)
        self._write_prose(declared=9)
        render.run(self.cfg, skip_queueing=True)

        text = self._note().read_text(encoding="utf-8")
        self.assertIn("claims 9 source(s); this note now holds 2", text)

    def test_render_still_reports_it_as_well(self):
        """The note tells its reader; the run still tells its operator."""
        self._papers(3)
        self._write_prose(declared=2)
        result = render.run(self.cfg, skip_queueing=True)
        self.assertEqual(result["stale"]["analysis"], 1)


if __name__ == "__main__":
    unittest.main()
