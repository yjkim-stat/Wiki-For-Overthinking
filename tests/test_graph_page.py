"""The wiki map.

What these check is that the page keeps the promises the palette validator
extracted from it: kind is carried by shape as well as colour, a table view
exists, and the picture is the same picture every time it is generated.
"""

from __future__ import annotations

import re
import unittest

from pipelines.publish import graph_page

from .sandbox import Sandbox


def node(nid, kind, label, sources=3):
    row = {"id": nid, "label": label, "kind": kind}
    if kind != "topic":
        row["sources"] = sources
    return row


NODES = [
    node("topic:test-topic", "topic", "Test Topic"),
    node("concept:partial-interference", "concept", "Partial Interference", 6),
    node("concept:instrumental-variable", "concept", "Instrumental Variable", 2),
    node("method:two-stage-least-squares", "method", "Two Stage Least Squares", 3),
    node("dataset:psid", "dataset", "PSID", 4),
]
EDGES = [
    {"source": "topic:test-topic", "target": "concept:partial-interference", "type": "covers"},
    {"source": "concept:partial-interference", "target": "dataset:psid", "type": "co-occurs"},
]


class LayoutTests(unittest.TestCase):
    def test_the_same_graph_lays_out_identically(self):
        """Generated files are committed; a moving layout is history noise."""
        self.assertEqual(graph_page.layout(NODES, EDGES),
                         graph_page.layout(NODES, EDGES))

    def test_every_node_lands_inside_the_canvas(self):
        placed = graph_page.layout(NODES, EDGES)
        self.assertEqual(len(placed), len(NODES))
        for x, y in placed.values():
            self.assertTrue(0 <= x <= graph_page.WIDTH)
            self.assertTrue(0 <= y <= graph_page.HEIGHT)

    def test_an_empty_graph_lays_out_to_nothing(self):
        self.assertEqual(graph_page.layout([], []), {})

    def test_more_evidence_is_a_bigger_mark(self):
        big = graph_page._radius(node("c:a", "concept", "A", 12))
        small = graph_page._radius(node("c:b", "concept", "B", 1))
        self.assertGreater(big - small, 6)


class PageTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()

    def tearDown(self):
        self.sandbox.close()

    def _build(self, nodes=NODES, edges=EDGES):
        from pipelines.common.store import write_json

        write_json(self.cfg.layout.wiki_meta / "graph.json",
                   {"generated_at": "x", "nodes": nodes, "edges": edges})
        path = graph_page.build(self.cfg)
        return path.read_text(encoding="utf-8")

    def test_kind_is_carried_by_shape_as_well_as_colour(self):
        """The palette sits in the 6-8 CVD band: colour alone is not legal."""
        page = self._build()
        self.assertIn("<circle", page)   # concept
        self.assertIn("<rect", page)     # method
        self.assertIn("<polygon", page)  # dataset

    def test_a_table_view_is_present(self):
        """Coral is under 3:1 on the light surface -- the relief rule applies."""
        page = self._build()
        self.assertIn("<table>", page)
        for label in ("Partial Interference", "PSID", "Two Stage Least Squares"):
            self.assertIn(label, page)

    def test_a_legend_names_every_kind_present(self):
        page = self._build()
        for word in ("Topic", "Concept", "Method", "Dataset"):
            self.assertIn(f">{word}</span>", page.replace("\n", ""))

    def test_labels_are_escaped(self):
        page = self._build(nodes=[node("concept:x", "concept", "A <b>bold</b> & co")])
        self.assertNotIn("<b>bold</b>", page)
        self.assertIn("&lt;b&gt;bold&lt;/b&gt; &amp; co", page)

    def test_an_empty_wiki_still_renders_a_page(self):
        page = self._build(nodes=[], edges=[])
        self.assertIn("0 entities", page)
        self.assertIn("<svg", page)

    def test_a_huge_graph_is_capped_and_says_so(self):
        many = [node(f"concept:c{i}", "concept", f"C{i}", sources=i % 7 + 1)
                for i in range(graph_page.MAX_NODES + 25)]
        page = self._build(nodes=many, edges=[])
        self.assertIn("not shown", page)
        self.assertEqual(len(re.findall(r'class="node"', page)), graph_page.MAX_NODES)

    def test_the_cap_keeps_the_best_attested(self):
        many = [node(f"concept:c{i}", "concept", f"C{i}", sources=i)
                for i in range(graph_page.MAX_NODES + 5)]
        page = self._build(nodes=many, edges=[])
        self.assertIn(f">C{graph_page.MAX_NODES + 4}<", page)  # most sources kept
        self.assertNotIn(">C0<", page)                          # fewest dropped

    def test_both_modes_ship_their_own_steps(self):
        """Dark is a re-stepping of the same hues, never an automatic flip."""
        page = self._build()
        self.assertIn("#f7958d", page)   # light coral
        self.assertIn("#de6f68", page)   # dark coral
        self.assertIn("prefers-color-scheme: dark", page)


if __name__ == "__main__":
    unittest.main()
