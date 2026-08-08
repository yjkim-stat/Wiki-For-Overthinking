"""End-to-end: records in, artifacts out."""

from __future__ import annotations

import unittest

from pipelines import render
from pipelines.common.schema import Paper, Video
from pipelines.common.store import RecordStore
from pipelines.enrich.queue import Queue
from pipelines.publish import wiki
from pipelines.publish.archive import paper_dir

from .sandbox import Sandbox

SLUG = "test-topic"


def result_for(title: str) -> dict:
    return {
        "one_liner": f"{title} does a thing.",
        "problem": "The thing was hard.",
        "contributions": ["First contribution", "Second contribution"],
        "method": "By reweighting with an estimated propensity score.",
        "results": "Beats the baseline by 12 points.",
        "limitations": "Only evaluated in simulation.",
        "relevance": {SLUG: "Moves the topic forward."},
        "concepts": ["Instrumental Variable"],
        "methods": ["Behaviour Cloning"],
        "datasets": ["Open X-Embodiment"],
        "tags": ["causal-inference"],
    }


class RenderPipelineTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)
        self.queue = Queue(self.cfg.layout)

        self.papers = []
        for index in (1, 2):
            paper = Paper(
                id=f"arxiv:2401.0000{index}",
                title=f"Paper {index}: causal inference",
                source="arxiv",
                authors=["Ada Lovelace", "Alan Turing"],
                abstract="We estimate effects with an instrumental variable.",
                url=f"https://arxiv.org/abs/2401.0000{index}",
                published="2024-01-15",
                year=2024,
                categories=["stat.ML"],
                arxiv_id=f"2401.0000{index}",
                topics=[SLUG],
                scores={SLUG: 0.8},
            )
            self.store.save_paper(paper)
            self.papers.append(paper)

        self.video = Video(
            id="youtube:abc123",
            title="A talk about causal inference",
            source_id="abc123",
            channel="Research Seminar",
            url="https://www.youtube.com/watch?v=abc123",
            published="2024-02-01",
            topics=[SLUG],
            scores={SLUG: 0.6},
        )
        self.store.save_video(self.video)

    def tearDown(self):
        self.sandbox.close()

    def _complete_paper_tasks(self):
        for paper in self.papers:
            task_id = self.queue.enqueue(
                kind="paper",
                item_id=paper.id,
                topics=[SLUG],
                language="en",
                instructions="Read it.",
                output_schema={},
                payload={"title": paper.title},
            )
            self.queue.complete(task_id, result_for(paper.title))

    # -- archive ------------------------------------------------------------
    def test_unsummarized_paper_still_gets_a_page(self):
        render.run(self.cfg)
        page = paper_dir(self.cfg.layout, self.papers[0]) / "summary.md"
        self.assertTrue(page.exists())
        self.assertIn("Not summarized yet", page.read_text(encoding="utf-8"))

    def test_completed_task_reaches_the_archive_page(self):
        self._complete_paper_tasks()
        render.run(self.cfg)
        text = (paper_dir(self.cfg.layout, self.papers[0]) / "summary.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("does a thing", text)
        self.assertIn("First contribution", text)
        self.assertIn("Only evaluated in simulation", text)

    def test_applied_task_is_archived_not_reapplied(self):
        self._complete_paper_tasks()
        render.run(self.cfg)
        stats = self.queue.stats()
        self.assertEqual(stats["done"], 0)
        self.assertEqual(stats["archived"], 2)

    def test_digest_index_and_records_index_are_written(self):
        render.run(self.cfg)
        self.assertTrue((self.cfg.layout.archive / "index.md").exists())
        self.assertTrue((self.cfg.layout.index / "papers.jsonl").exists())

    # -- wiki ---------------------------------------------------------------
    def test_entity_seen_twice_is_promoted_to_a_note(self):
        self._complete_paper_tasks()
        render.run(self.cfg)
        note = wiki.note_path(self.cfg.layout, "concept", "instrumental-variable")
        self.assertTrue(note.exists(), "concept with two sources should get a note")
        self.assertIn("Paper 1", note.read_text(encoding="utf-8"))

    def test_entity_seen_once_is_not_promoted(self):
        task_id = self.queue.enqueue(
            kind="paper", item_id=self.papers[0].id, topics=[SLUG], language="en",
            instructions="", output_schema={}, payload={},
        )
        result = result_for("Paper 1")
        result["concepts"] = ["Something Mentioned Once"]
        self.queue.complete(task_id, result)
        render.run(self.cfg)
        self.assertFalse(
            wiki.note_path(self.cfg.layout, "concept", "something-mentioned-once").exists()
        )

    def test_promotion_queues_a_definition_task(self):
        self._complete_paper_tasks()
        render.run(self.cfg)
        pending = self.queue.pending_ids(kind="concept")
        self.assertTrue(pending, "a promoted concept should have a definition task")

    def test_definition_reaches_the_note(self):
        self._complete_paper_tasks()
        render.run(self.cfg)
        # Several entities are promoted at once, so pick the one under test
        # rather than whichever sorts first.
        task_id = next(
            t
            for t in self.queue.pending_ids(kind="concept")
            if self.queue.load(t)["item_id"] == "Instrumental Variable"
        )
        self.queue.complete(
            task_id,
            {"definition": "A variable that shifts treatment but not the outcome.", "kind": "concept"},
        )
        render.run(self.cfg)
        note = wiki.note_path(self.cfg.layout, "concept", "instrumental-variable")
        self.assertIn("shifts treatment but not the outcome", note.read_text(encoding="utf-8"))

    def test_manual_section_survives_a_rerender(self):
        self._complete_paper_tasks()
        render.run(self.cfg)
        note = wiki.note_path(self.cfg.layout, "concept", "instrumental-variable")
        note.write_text(
            note.read_text(encoding="utf-8") + "\n\nMY OWN ANALYSIS\n", encoding="utf-8"
        )
        render.run(self.cfg)
        self.assertIn("MY OWN ANALYSIS", note.read_text(encoding="utf-8"))

    def test_auto_block_is_regenerated_not_duplicated(self):
        self._complete_paper_tasks()
        render.run(self.cfg)
        render.run(self.cfg)
        text = wiki.note_path(self.cfg.layout, "concept", "instrumental-variable").read_text(
            encoding="utf-8"
        )
        self.assertEqual(text.count("<!-- auto:begin -->"), 1)
        self.assertEqual(text.count("<!-- auto:end -->"), 1)

    def test_topic_note_and_graph_are_written(self):
        render.run(self.cfg)
        self.assertTrue(wiki.topic_note_path(self.cfg.layout, SLUG).exists())
        self.assertTrue((self.cfg.layout.wiki_meta / "graph.json").exists())

    # -- outputs ------------------------------------------------------------
    def test_all_three_outputs_are_generated(self):
        self._complete_paper_tasks()
        render.run(self.cfg)
        self.assertTrue(
            (self.cfg.layout.out_lecture_notes / SLUG / "lecture-note.md").exists()
        )
        self.assertTrue((self.cfg.layout.out_slides / SLUG / "index.html").exists())
        self.assertTrue((self.cfg.layout.out_reports / SLUG / "index.html").exists())

    def test_html_outputs_are_self_contained(self):
        self._complete_paper_tasks()
        render.run(self.cfg)
        for path in (
            self.cfg.layout.out_slides / SLUG / "index.html",
            self.cfg.layout.out_reports / SLUG / "index.html",
        ):
            html = path.read_text(encoding="utf-8")
            self.assertNotIn("src=\"http", html)
            self.assertNotIn("<link rel=\"stylesheet\"", html)
            self.assertNotIn("cdn.", html)

    def test_report_contains_the_summary_content(self):
        self._complete_paper_tasks()
        render.run(self.cfg)
        html = (self.cfg.layout.out_reports / SLUG / "index.html").read_text(
            encoding="utf-8"
        )
        self.assertIn("First contribution", html)
        self.assertIn("Full index", html)

    def test_no_raw_html_leaks_as_visible_text(self):
        # Markup built by a generator must reach the page as markup. If it is
        # routed through the Markdown converter it comes out escaped and the
        # reader sees the tag itself.
        self._complete_paper_tasks()
        render.run(self.cfg)
        for path in (
            self.cfg.layout.out_slides / SLUG / "index.html",
            self.cfg.layout.out_reports / SLUG / "index.html",
        ):
            html = path.read_text(encoding="utf-8")
            for leaked in ("&lt;p ", "&lt;div", "&lt;section", "&lt;h1", "&lt;h2"):
                self.assertNotIn(leaked, html, f"{leaked} leaked into {path.name}")

    def test_titles_containing_markup_are_escaped(self):
        self.papers[0].title = "Policies with <script>alert(1)</script> tokens"
        self.store.save_paper(self.papers[0])
        self._complete_paper_tasks()
        render.run(self.cfg)
        html = (self.cfg.layout.out_slides / SLUG / "index.html").read_text(
            encoding="utf-8"
        )
        self.assertNotIn("<script>alert(1)</script>", html)
        self.assertIn("&lt;script&gt;", html)

    def test_deck_has_one_section_per_slide(self):
        self._complete_paper_tasks()
        render.run(self.cfg)
        html = (self.cfg.layout.out_slides / SLUG / "index.html").read_text(
            encoding="utf-8"
        )
        self.assertGreaterEqual(html.count('<section class="slide'), 5)

    def test_lecture_note_has_no_unfilled_placeholders(self):
        self._complete_paper_tasks()
        render.run(self.cfg)
        text = (self.cfg.layout.out_lecture_notes / SLUG / "lecture-note.md").read_text(
            encoding="utf-8"
        )
        self.assertNotIn("{{", text)

    # -- rebuild ------------------------------------------------------------
    def test_generated_trees_rebuild_from_data_alone(self):
        import shutil

        self._complete_paper_tasks()
        render.run(self.cfg)
        before = (self.cfg.layout.out_reports / SLUG / "index.html").read_text(
            encoding="utf-8"
        )

        for directory in (self.cfg.layout.archive, self.cfg.layout.wiki, self.cfg.layout.outputs):
            shutil.rmtree(directory)
        render.run(self.cfg)

        after = (self.cfg.layout.out_reports / SLUG / "index.html").read_text(
            encoding="utf-8"
        )
        self.assertEqual(before, after)

    def test_a_corrected_year_leaves_no_stale_page_behind(self):
        # A paper's page path contains its year, and a year can arrive after
        # the page does — a deduplication merge fills one in, and a hand-filed
        # PDF has none until it has been read. The page written under the old
        # year must not survive as a second copy.
        paper = self.papers[0]
        paper.year = 0
        paper.published = ""
        self.store.save_paper(paper)
        render.rebuild_archive(self.cfg)
        stale = paper_dir(self.cfg.layout, paper)
        self.assertTrue(stale.exists())

        paper.year = 2024
        self.store.save_paper(paper)
        render.rebuild_archive(self.cfg)

        self.assertFalse(stale.exists(), "archive/ must be a pure function of data/")
        self.assertTrue(paper_dir(self.cfg.layout, paper).exists())

    def test_rebuilding_does_not_touch_the_daily_digests(self):
        # Digests are dated records of a run, not derived from the store, so
        # nothing regenerates them and clearing them would lose them.
        digest = self.cfg.layout.archive_daily / "2024-01-01.md"
        digest.parent.mkdir(parents=True, exist_ok=True)
        digest.write_text("# a day", encoding="utf-8")
        render.rebuild_archive(self.cfg)
        self.assertTrue(digest.exists())

    def test_only_flag_limits_the_stage(self):
        result = render.run(self.cfg, only="wiki")
        self.assertIn("wiki", result)
        self.assertNotIn("outputs", result)


if __name__ == "__main__":
    unittest.main()
