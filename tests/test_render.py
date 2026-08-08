"""End-to-end: records in, artifacts out."""

from __future__ import annotations

import unittest
from pathlib import Path

from pipelines import render
from pipelines.common.schema import Concept, Paper, PaperSummary, Video
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


class RuledKindTests(unittest.TestCase):
    """A definition task's `kind` is a ruling; harvest must not overrule it.

    `harvest` derives kind from which of a summary's three lists a name landed
    in, taking the highest rank across every summary. That is a side effect of
    field placement; the definition task's kind is a deliberate judgement made
    once over the whole evidence set. Before this was fixed the side effect won
    on every render, and the note moved directory each time -- which also lost
    the hand-written section, because the prose does not follow the note.
    """

    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)
        paper = Paper(
            id="arxiv:2401.09999",
            title="A paper about a family of models",
            source="arxiv",
            topics=[SLUG],
            scores={SLUG: 0.9},
        )
        self.store.save_paper(paper)
        self.store.save_paper_summary(
            PaperSummary(
                paper_id=paper.id,
                one_liner="It surveys a family.",
                methods=["Vision Language Action Model"],
                concepts=["Undecided Thing"],
            )
        )

    def tearDown(self):
        self.sandbox.close()

    def _harvest_kind(self, slug: str) -> str:
        return wiki.harvest(self.cfg)[slug].kind

    def test_a_ruled_kind_survives_a_further_render(self):
        self.store.save_concept(
            Concept(
                slug="vision-language-action-model",
                name="Vision Language Action Model",
                kind="concept",
                definition="A family whose instances are the methods.",
            )
        )
        self.assertEqual(self._harvest_kind("vision-language-action-model"), "concept")
        # The revert was observed on the *second* render, so harvest twice.
        self.store.save_concept(wiki.harvest(self.cfg)["vision-language-action-model"])
        self.assertEqual(self._harvest_kind("vision-language-action-model"), "concept")

    def test_an_entity_without_a_definition_still_takes_the_harvested_kind(self):
        self.store.save_concept(
            Concept(
                slug="vision-language-action-model",
                name="Vision Language Action Model",
                kind="concept",
                definition="",
            )
        )
        self.assertEqual(self._harvest_kind("vision-language-action-model"), "method")

    def test_an_unseen_entity_is_unaffected(self):
        self.assertEqual(self._harvest_kind("undecided-thing"), "concept")


class StalenessTests(unittest.TestCase):
    """An empty queue means nothing is unwritten, not that nothing is stale.

    A definition is written once against N sources and never revisited, however
    far its evidence outgrows it. The note then reads as complete while
    describing a subset of its own evidence -- not thin, but wrong.
    """

    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)
        self.queue = Queue(self.cfg.layout)

    def tearDown(self):
        self.sandbox.close()

    def _concept(self, definition="A definition.", sources=5):
        concept = Concept(
            slug="instrumental-variable",
            name="Instrumental Variable",
            kind="concept",
            definition=definition,
            evidence=[
                {"kind": "paper", "id": f"arxiv:{i}", "title": f"P{i}", "note": ""}
                for i in range(sources)
            ],
        )
        self.store.save_concept(concept)
        return concept

    def _definition_task(self, written_for: int):
        task_id = self.queue.enqueue(
            kind="concept",
            item_id="Instrumental Variable",
            topics=[SLUG],
            language="en",
            instructions="Define it.",
            output_schema={"definition": "string"},
            payload={"name": "Instrumental Variable", "source_count": written_for},
        )
        self.queue.complete(task_id, {"definition": "A definition."})
        self.queue.archive(task_id)

    def test_a_definition_outgrown_by_its_evidence_is_reported(self):
        self._concept(sources=6)
        self._definition_task(written_for=5)
        rows = render.stale_definitions(self.cfg)
        self.assertEqual([r["slug"] for r in rows], ["instrumental-variable"])
        self.assertEqual(rows[0]["written_for"], 5)
        self.assertEqual(rows[0]["sources_now"], 6)

    def test_a_definition_still_matching_its_evidence_is_not(self):
        self._concept(sources=5)
        self._definition_task(written_for=5)
        self.assertEqual(render.stale_definitions(self.cfg), [])

    def test_an_entity_with_no_definition_is_never_reported(self):
        self._concept(definition="", sources=9)
        self._definition_task(written_for=2)
        self.assertEqual(render.stale_definitions(self.cfg), [])

    def test_reporting_never_rewrites_the_definition(self):
        """The property that keeps this safe: a counter must not discard work."""
        self._concept(sources=9)
        self._definition_task(written_for=2)
        render.report_staleness(self.cfg)
        self.assertEqual(
            self.store.load_concept("instrumental-variable").definition, "A definition."
        )

    def _note(self, body: str) -> Path:
        path = wiki.note_path(self.cfg.layout, "concept", "instrumental-variable")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            f"# Instrumental Variable\n\n<!-- auto:begin -->\ngenerated\n"
            f"<!-- auto:end -->\n\n{body}\n",
            encoding="utf-8",
        )
        return path

    def test_analysis_declaring_fewer_sources_is_reported(self):
        self._concept(sources=9)
        self._note("## Notes\n\nMy reading.\n\n<!-- analysis-sources: 4 -->")
        rows = render.stale_analysis(self.cfg)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["written_for"], 4)
        self.assertEqual(rows[0]["sources_now"], 9)

    def test_analysis_without_the_marker_is_not_checked(self):
        """Opt-in: some prose genuinely does not depend on the count."""
        self._concept(sources=9)
        self._note("## Notes\n\nMy reading, with no declared dependency.")
        self.assertEqual(render.stale_analysis(self.cfg), [])

    def test_analysis_still_matching_is_not_reported(self):
        self._concept(sources=4)
        self._note("## Notes\n\nMy reading.\n\n<!-- analysis-sources: 4 -->")
        self.assertEqual(render.stale_analysis(self.cfg), [])

    def test_reporting_never_rewrites_the_analysis(self):
        self._concept(sources=9)
        path = self._note("## Notes\n\nMy reading.\n\n<!-- analysis-sources: 4 -->")
        before = path.read_text(encoding="utf-8")
        render.report_staleness(self.cfg)
        self.assertEqual(path.read_text(encoding="utf-8"), before)

    def test_render_reports_both_counts(self):
        self._concept(sources=9)
        self._definition_task(written_for=2)
        self._note("## Notes\n\nMine.\n\n<!-- analysis-sources: 4 -->")
        result = render.run(self.cfg, skip_queueing=True)
        self.assertEqual(result["stale"], {"definitions": 1, "analysis": 1})
