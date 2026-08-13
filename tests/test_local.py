"""Tests for `pipelines/local/` — this archive's own extensions.

Kept apart from the general test files for the same reason the code is: a
template-shaped file gets improved by being replaced wholesale, and anything of
ours living inside one would be lost without a word. See
`docs/LOCAL-DELTAS.md`.
"""

from __future__ import annotations

import unittest

from pipelines import render
from pipelines.enrich import apply as apply_mod
from pipelines.enrich import concepts as concepts_mod
from pipelines.common.http import HTTPError
from pipelines.common.schema import Paper, PaperSummary
from pipelines.common.store import RecordStore
from pipelines.enrich.queue import Queue, validate_result
from pipelines.local import abstracts as local_abstracts
from pipelines.local import placeholders
from pipelines.local import queue_share
from pipelines.publish import wiki

from .sandbox import Sandbox

SLUG = "test-topic"

GOOD_PAPER_RESULT = {
    "one_liner": "It does a thing.",
    "problem": "The thing was hard.",
    "contributions": ["a", "b"],
    "method": "By doing it.",
    "results": "Better.",
    "limitations": "Slow.",
    "relevance": {SLUG: "Relevant because."},
    "concepts": ["Instrumental Variable"],
    "methods": [],
    "datasets": [],
    "tags": ["x"],
}


def result_for(title: str) -> dict:
    return dict(GOOD_PAPER_RESULT, one_liner=f"{title} does a thing.")



class PlaceholderEntityTests(unittest.TestCase):
    """A wiki entity has to be a name, not a description of a set of names.

    `publish/wiki.py` keys entities by their string, so "five reasoning
    benchmarks (unnamed in abstract)" written by two unrelated papers merges
    into one entity that counts them as independent evidence and gets promoted.
    That happened before this guard existed.
    """

    def test_disclaimer_entry_is_rejected(self):
        bad = dict(
            GOOD_PAPER_RESULT,
            datasets=["three GREC benchmarks (unnamed in abstract)"],
        )
        errors = validate_result("paper", bad)
        self.assertTrue(any("describes a set of things" in e for e in errors))

    def test_quantified_collection_is_rejected_without_a_disclaimer(self):
        bad = dict(GOOD_PAPER_RESULT, models=["several open-weight models"])
        errors = validate_result("paper", bad)
        self.assertTrue(any("describes a set of things" in e for e in errors))

    def test_every_harvested_field_is_checked(self):
        for field in ("concepts", "methods", "datasets", "models"):
            with self.subTest(field=field):
                bad = dict(GOOD_PAPER_RESULT, **{field: ["unspecified"]})
                self.assertTrue(
                    any("describes a set of things" in e
                        for e in validate_result("paper", bad))
                )

    def test_real_names_survive(self):
        # Each of these tripped an earlier, blunter version of the rule.
        ok = dict(
            GOOD_PAPER_RESULT,
            datasets=["GSM8K", "AIME 24", "Mini-ARC", "WebInstruct-verified"],
            models=["Qwen2.5-VL-7B", "GPT-4o", "Maia-1100", "Falcon-hybrid"],
            methods=["ten-fold cross-validation", "Mixture-of-Experts", "best-of-n"],
            concepts=["two-phase reasoning structure", "pass@k"],
        )
        self.assertEqual(validate_result("paper", ok), [])

    def test_an_empty_list_is_the_intended_answer(self):
        ok = dict(GOOD_PAPER_RESULT, datasets=[], models=[])
        self.assertEqual(validate_result("paper", ok), [])

    def test_prose_fields_are_left_alone(self):
        # "three benchmarks (unnamed in abstract)" is a true and useful
        # sentence in `results`; it is only a problem offered as a name.
        ok = dict(
            GOOD_PAPER_RESULT,
            results="Evaluated on three benchmarks (unnamed in abstract).",
        )
        self.assertEqual(validate_result("paper", ok), [])

    def test_the_script_shares_the_validator_rule(self):
        import importlib.util

        from pipelines.common.paths import REPO_ROOT

        spec = importlib.util.spec_from_file_location(
            "strip_placeholder_entities",
            REPO_ROOT / "scripts" / "strip_placeholder_entities.py",
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        from pipelines.local import placeholders as queue_mod

        self.assertIs(module.looks_like_placeholder, placeholders.looks_like_placeholder)


class WikiKindTests(unittest.TestCase):
    """`model` was added to the wiki by note 0011 and not to this validator."""

    def test_model_is_an_accepted_definition_kind(self):
        self.assertEqual(
            validate_result("concept", {"definition": "A checkpoint.", "kind": "model"}),
            [],
        )

    def test_unknown_kind_is_still_rejected(self):
        errors = validate_result("concept", {"definition": "x", "kind": "gadget"})
        self.assertTrue(any("must be one of" in e for e in errors))

    def test_validator_and_wiki_agree_on_the_kinds(self):
        from pipelines.common.paths import WIKI_KINDS
        from pipelines.publish.wiki import KINDS

        self.assertEqual(KINDS, WIKI_KINDS)


class ModelsRoundTripTests(unittest.TestCase):
    """`models` reached the schema and the wiki but not the applier.

    Note 0011 added the field to `PaperSummary`, to the task's output schema and
    to the wiki harvest, and `_apply_paper` went on ignoring it — so every
    `models` list a reader submitted was dropped between the queue and the
    store, and the field looked empty by design rather than by omission.
    """

    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)
        self.queue = Queue(self.cfg.layout)

        self.paper = Paper(
            id="arxiv:2401.55555",
            title="A paper that names its checkpoints",
            source="arxiv",
            abstract="We evaluate several checkpoints.",
            topics=[SLUG],
        )
        self.store.save_paper(self.paper)

    def _enqueue(self) -> str:
        return self.queue.enqueue(
            kind="paper",
            item_id=self.paper.id,
            topics=[SLUG],
            language="en",
            instructions="",
            output_schema={},
            payload={"title": self.paper.title},
        )

    def tearDown(self):
        self.sandbox.close()

    def test_submitted_models_reach_the_stored_summary(self):
        result = dict(result_for(self.paper.title), models=["Qwen2.5-7B", "GPT-4o"])
        task_id = self._enqueue()
        self.queue.complete(task_id, result)
        apply_mod.completed(self.cfg)

        summary = self.store.load_paper_summary(self.paper.id)
        self.assertEqual(summary.models, ["Qwen2.5-7B", "GPT-4o"])

    def test_models_become_wiki_entities_of_kind_model(self):
        result = dict(result_for(self.paper.title), models=["Qwen2.5-7B"])
        task_id = self._enqueue()
        self.queue.complete(task_id, result)
        apply_mod.completed(self.cfg)

        harvested = concepts_mod.harvest(self.cfg)
        match = [c for c in harvested.values() if c.name == "Qwen2.5-7B"]
        self.assertEqual(len(match), 1)
        self.assertEqual(match[0].kind, "model")


class DefinitionQueueShareTests(unittest.TestCase):
    """A reading backlog used to starve the wiki's own definition tasks.

    `render` queued summaries first and definitions second against one shared
    cap, so while any paper was unread every slot went to summaries and the
    self-extending wiki stopped extending — logged only at WARNING level.
    """

    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()

    def tearDown(self):
        self.sandbox.close()

    def test_summaries_may_not_take_the_whole_cap_on_the_first_pass(self):
        self.cfg.settings["summarize"] = {"max_pending_tasks": 40}
        self.assertEqual(queue_share.pending_cap(self.cfg), 40)
        self.assertEqual(queue_share.summary_cap(self.cfg), 20)

    def test_an_odd_cap_rounds_in_favour_of_reading(self):
        self.cfg.settings["summarize"] = {"max_pending_tasks": 7}
        self.assertEqual(queue_share.summary_cap(self.cfg), 4)

    def test_no_cap_configured_means_no_reserve(self):
        self.cfg.settings["summarize"] = {}
        self.assertIsNone(queue_share.pending_cap(self.cfg))
        self.assertIsNone(queue_share.summary_cap(self.cfg))

    def test_the_two_passes_do_not_double_count_the_same_backlog(self):
        """`summaries_queued` counts tasks filed, not passes over the backlog.

        Splitting the cap made `render` call `queue_missing_summaries` twice,
        and each call returns how many records lack a summary rather than how
        many tasks it filed. Summing them reported a steady backlog of 37 as
        74 — inside a run that otherwise looked healthy, in the number an
        unattended routine reports back.
        """
        store = RecordStore(self.cfg.layout)
        for i in range(5):
            store.save_paper(
                Paper(
                    id=f"arxiv:2401.0000{i}",
                    title=f"Unread paper {i}",
                    source="arxiv",
                    abstract="Nobody has read this yet.",
                    topics=[SLUG],
                )
            )

        before = queue_share.pending_count(self.cfg)
        result = render.run(self.cfg)
        after = queue_share.pending_count(self.cfg)

        self.assertEqual(after - before, 5)
        self.assertEqual(result["summaries_queued"], 5)

        # And a second render files nothing, because the tasks already exist.
        again = render.run(self.cfg)
        self.assertEqual(again["summaries_queued"], 0)
        self.assertEqual(queue_share.pending_count(self.cfg), after)

    def test_only_wiki_still_reports_no_summary_queueing(self):
        """The reserve is released only when the archive stage held it back."""
        result = render.run(self.cfg, only="wiki")
        self.assertNotIn("summaries_queued", result)

    def test_definitions_queued_counts_tasks_filed_not_attempts(self):
        """The same lesson as the test above, in the other counter.

        `queue.add` returns "" once the queue is at its cap; `define_concept`
        discards that and returns None either way; and the loop read None as
        "deferred to the queue". So a render that filed nothing reported four
        definitions queued — and the reserve exists precisely because the queue
        being full of reading is the normal state, which is when this counter
        is read and when it is wrong.
        """
        self.cfg.settings["summarize"] = {"max_pending_tasks": 2}
        store = RecordStore(self.cfg.layout)

        # Two summaries naming one entity: promoted, undefined, so a definition
        # task is owed.
        for i in range(2):
            paper = Paper(
                id=f"arxiv:2401.0000{i}",
                title=f"Read paper {i}",
                source="arxiv",
                abstract="Already summarized.",
                topics=[SLUG],
                scores={SLUG: 0.9},
            )
            store.save_paper(paper)
            store.save_paper_summary(
                PaperSummary(
                    paper_id=paper.id,
                    one_liner=f"Paper {i} does a thing.",
                    concepts=["Instrumental Variable"],
                )
            )

        # Fill every slot with reading, the way a collection run does.
        queue = Queue(self.cfg.layout)
        for i in range(2):
            queue.enqueue(
                kind="paper",
                item_id=f"arxiv:2409.0000{i}",
                topics=[SLUG],
                language="en",
                instructions="Read it.",
                output_schema={},
                payload={},
            )
        self.assertEqual(queue_share.pending_count(self.cfg), 2)

        result = render.run(self.cfg)

        self.assertEqual(queue_share.pending_count(self.cfg), 2, "nothing fitted")
        self.assertEqual(result["definitions_queued"], 0)


ACL_PAGE = """<!doctype html><html><head><title>A Paper - ACL Anthology</title></head>
<body><div class="row acl-paper-details">
<div class="card bg-light"><div class="card-body acl-abstract">
<h5 class="card-title">Abstract</h5><span>We study <b>reasoning</b> in language
models &amp; report a 12&#37; gain.</span></div></div></div></body></html>"""


class AbstractClient:
    """Serves an ACL page over `get` and a Semantic Scholar record over `get_json`."""

    def __init__(self, page: str = ACL_PAGE, abstract: str = "", fail: bool = False):
        self.page = page
        self.abstract = abstract
        self.fail = fail
        self.gets: list[str] = []
        self.jsons: list[str] = []

    def get(self, url, params=None, headers=None):
        self.gets.append(url)
        if self.fail:
            raise HTTPError("simulated outage")
        return self.page.encode("utf-8")

    def get_json(self, url, params=None, headers=None, **kw):
        self.jsons.append(url)
        if self.fail:
            raise HTTPError("simulated outage")
        return {"abstract": self.abstract}


def _paper(doi: str = "10.18653/v1/2026.acl-long.1034", abstract: str = "") -> Paper:
    return Paper(
        id=f"doi:{doi}",
        title="A paper DBLP knew about",
        source="dblp",
        abstract=abstract,
        doi=doi,
    )


class MissingAbstractTests(unittest.TestCase):
    """DBLP is bibliographic and carries no abstracts at all.

    Before this, every DBLP-only paper was stored, scored and queued on its
    title alone — scored on strictly less evidence than the same paper from an
    index that supplies one, and handed to a reader with no source material.
    """

    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()

    def tearDown(self):
        self.sandbox.close()

    def test_an_acl_doi_is_resolved_from_the_anthology(self):
        paper = _paper()
        client = AbstractClient()
        filled = local_abstracts.fill_missing(self.cfg, [paper], client)

        self.assertEqual(filled, 1)
        self.assertIn("We study reasoning in language", paper.abstract)
        # Markup stripped, entities decoded.
        self.assertNotIn("<b>", paper.abstract)
        self.assertIn("12% gain", paper.abstract)
        # The Anthology id is the DOI suffix, so no lookup is needed to build
        # the URL, and Semantic Scholar is never consulted.
        self.assertEqual(client.gets, ["https://aclanthology.org/2026.acl-long.1034/"])
        self.assertEqual(client.jsons, [])

    def test_dblp_uppercases_dois_and_anthology_urls_are_lowercase(self):
        # DBLP reports "10.18653/V1/2026.ACL-LONG.1034". A DOI is
        # case-insensitive, an Anthology URL path is not, and the uppercase
        # form 404s — which silently sent every ACL paper to the fallback.
        paper = _paper(doi="10.18653/V1/2026.ACL-LONG.1034")
        client = AbstractClient()
        filled = local_abstracts.fill_missing(self.cfg, [paper], client)

        self.assertEqual(filled, 1)
        self.assertEqual(
            client.gets, ["https://aclanthology.org/2026.acl-long.1034/"]
        )
        self.assertEqual(client.jsons, [])

    def test_a_non_acl_doi_falls_back_to_semantic_scholar(self):
        paper = _paper(doi="10.1109/ICCV.2026.12345")
        client = AbstractClient(abstract="A different abstract.")
        filled = local_abstracts.fill_missing(self.cfg, [paper], client)

        self.assertEqual(filled, 1)
        self.assertEqual(paper.abstract, "A different abstract.")
        self.assertEqual(client.gets, [])
        self.assertEqual(len(client.jsons), 1)

    def test_a_paper_that_already_has_an_abstract_is_left_alone(self):
        paper = _paper(abstract="Already here.")
        client = AbstractClient()
        self.assertEqual(
            local_abstracts.fill_missing(self.cfg, [paper], client), 0
        )
        self.assertEqual(paper.abstract, "Already here.")
        self.assertEqual(client.gets, [])

    def test_a_paper_with_no_doi_is_skipped(self):
        paper = Paper(id="title:something", title="No identifier", source="dblp")
        client = AbstractClient()
        self.assertEqual(
            local_abstracts.fill_missing(self.cfg, [paper], client), 0
        )
        self.assertEqual(client.gets, [])

    def test_a_failed_lookup_leaves_the_abstract_empty(self):
        paper = _paper()
        errors: list[str] = []
        filled = local_abstracts.fill_missing(
            self.cfg, [paper], AbstractClient(fail=True), errors
        )
        self.assertEqual(filled, 0)
        self.assertEqual(paper.abstract, "")
        self.assertTrue(any("abstracts:" in e for e in errors))

    def test_an_acl_miss_falls_through_to_semantic_scholar(self):
        # The Anthology answered, and the page carried no abstract card.
        paper = _paper()
        client = AbstractClient(page="<html><body>nothing here</body></html>",
                                abstract="From Semantic Scholar.")
        filled = local_abstracts.fill_missing(self.cfg, [paper], client)
        self.assertEqual(filled, 1)
        self.assertEqual(paper.abstract, "From Semantic Scholar.")
        self.assertEqual(len(client.gets), 1)
        self.assertEqual(len(client.jsons), 1)

    def test_max_lookups_bounds_one_run_not_the_backlog(self):
        papers = [_paper(doi=f"10.18653/v1/2026.acl-long.{n}") for n in range(5)]
        self.cfg.sources["conferences"]["abstracts"] = {"max_lookups": 2}
        filled = local_abstracts.fill_missing(
            self.cfg, papers, AbstractClient()
        )
        self.assertEqual(filled, 2)
        # The rest keep their empty abstract and are retried on the next run.
        self.assertEqual(sum(1 for p in papers if not p.abstract), 3)

    def test_the_step_can_be_turned_off(self):
        paper = _paper()
        self.cfg.sources["conferences"]["abstracts"] = {"enabled": False}
        client = AbstractClient()
        self.assertEqual(
            local_abstracts.fill_missing(self.cfg, [paper], client), 0
        )
        self.assertEqual(client.gets, [])
