"""The two generated files that changed on every render.

Note 0036 established the rule for records: running the pipeline over an
unchanged archive must change nothing, because a field that restamps itself
every pass buries the real changes in a diff nobody can read.

`wiki/_meta/graph.json` and `wiki/graph.html` carry the time they were
generated, and both are tracked. So every render produced a diff in two files
whatever had or had not happened — the same failure, one directory across, in
artifacts a person is expected to read.

The stamp is kept rather than dropped. Written only when the drawing actually
moved, it says when the graph last *changed*, which is worth more than when
somebody last ran a command.
"""

from __future__ import annotations

import json
import time
import unittest

from pipelines import render
from pipelines.common.schema import Concept, Paper, PaperSummary
from pipelines.common.store import RecordStore

from .sandbox import Sandbox

SLUG = "test-topic"


class GraphChurnTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.addCleanup(self.sandbox.close)
        self.cfg = self.sandbox.config()
        for index in (1, 2):
            paper_id = f"arxiv:2401.0000{index}"
            RecordStore(self.cfg.layout).save_paper(
                Paper(id=paper_id, title=f"Paper {index}", source="arxiv",
                      published="2024-01-15", year=2024, topics=[SLUG])
            )
            RecordStore(self.cfg.layout).save_paper_summary(
                PaperSummary(paper_id=paper_id, one_liner="It does a thing.",
                             relevance={SLUG: "Relevant."},
                             concepts=["Instrumental Variable"])
            )
        render.run(self.cfg, skip_queueing=True)

    def _graph(self):
        return self.cfg.layout.wiki_meta / "graph.json"

    def _page(self):
        return self.cfg.layout.wiki / "graph.html"

    def _state(self) -> dict:
        return {
            "json": self._graph().read_bytes(),
            "json_mtime": self._graph().stat().st_mtime,
            "html": self._page().read_bytes(),
            "html_mtime": self._page().stat().st_mtime,
        }

    def test_a_second_render_rewrites_neither(self):
        """Asserted on mtime as well as bytes.

        A rewrite with an identical stamp would be invisible to a byte
        comparison, and the stamp only moves once a second.
        """
        before = self._state()
        time.sleep(1.1)
        render.run(self.cfg, skip_queueing=True)
        self.assertEqual(self._state(), before)

    def test_a_changed_graph_is_written_with_a_fresh_stamp(self):
        """The stamp still means something, and now it means more."""
        before = json.loads(self._graph().read_text(encoding="utf-8"))["generated_at"]
        time.sleep(1.1)

        RecordStore(self.cfg.layout).save_concept(
            Concept(slug="a-new-entity", name="A New Entity", kind="concept",
                    definition="It is new.", topics=[SLUG],
                    evidence=[{"kind": "paper", "id": "arxiv:2401.00001",
                               "title": "Paper 1", "note": ""},
                              {"kind": "paper", "id": "arxiv:2401.00002",
                               "title": "Paper 2", "note": ""}])
        )
        render.run(self.cfg, skip_queueing=True)

        graph = json.loads(self._graph().read_text(encoding="utf-8"))
        self.assertNotEqual(graph["generated_at"], before)
        self.assertIn("concept:a-new-entity", [n["id"] for n in graph["nodes"]])

    def test_the_drawing_is_rewritten_when_the_graph_moves(self):
        before = self._page().read_bytes()
        time.sleep(1.1)
        RecordStore(self.cfg.layout).save_concept(
            Concept(slug="a-new-entity", name="A New Entity", kind="concept",
                    definition="It is new.", topics=[SLUG],
                    evidence=[{"kind": "paper", "id": "arxiv:2401.00001",
                               "title": "Paper 1", "note": ""},
                              {"kind": "paper", "id": "arxiv:2401.00002",
                               "title": "Paper 2", "note": ""}])
        )
        render.run(self.cfg, skip_queueing=True)
        self.assertNotEqual(self._page().read_bytes(), before)

    def test_the_stamp_is_still_there(self):
        """Kept, not dropped: it now says when the graph last changed."""
        graph = json.loads(self._graph().read_text(encoding="utf-8"))
        self.assertIn("generated_at", graph)
        self.assertIn("Generated ", self._page().read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
