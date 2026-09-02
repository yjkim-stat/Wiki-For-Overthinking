"""The `model` wiki kind, and the migration that introduced it.

Covers what notes 0011 and 0012 recorded as untested: models get their own
wiki directory, a name seen as a model outranks the same name called a dataset,
and the two maintenance scripts do what their notes claim.
"""

from __future__ import annotations

import importlib.util
import subprocess
import sys
import unittest

from pipelines.common import llm
from pipelines.common.paths import REPO_ROOT, WIKI_KINDS
from pipelines.common.schema import Paper, PaperSummary
from pipelines.common.store import RecordStore
from pipelines.enrich import concepts as concepts_mod
from pipelines.enrich import queue as queue_mod
from pipelines.publish import wiki

from .sandbox import Sandbox

SLUG = "test-topic"


def paper(index: int, title: str) -> Paper:
    return Paper(
        id=f"arxiv:2401.0000{index}",
        title=title,
        source="arxiv",
        authors=["Ada Lovelace"],
        abstract="We estimate effects with an instrumental variable.",
        published="2024-01-15",
        year=2024,
        topics=[SLUG],
        scores={SLUG: 0.8},
    )


class ModelKindTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)

    def tearDown(self):
        self.sandbox.close()

    def _save(self, index: int, **fields) -> Paper:
        item = paper(index, f"Paper {index}: causal inference")
        self.store.save_paper(item)
        self.store.save_paper_summary(
            PaperSummary(paper_id=item.id, one_liner=f"Paper {index} does a thing.", **fields)
        )
        return item

    def test_model_is_a_recognised_kind(self):
        self.assertIn("model", wiki.KINDS)

    def test_models_get_their_own_wiki_directory(self):
        # Two sources so the entity clears the promotion threshold.
        self._save(1, models=["Qwen2.5-7B"])
        self._save(2, models=["Qwen2.5-7B"])
        wiki.update(self.cfg, *concepts_mod.rebuild(self.cfg))
        note = self.cfg.layout.wiki_kind_dir("model") / "qwen2-5-7b.md"
        self.assertTrue(note.exists(), "model note should land in wiki/models/")
        self.assertFalse(
            (self.cfg.layout.wiki_kind_dir("dataset") / "qwen2-5-7b.md").exists()
        )

    def test_model_outranks_dataset_for_the_same_name(self):
        # One summary calls it a dataset, the other a model: model wins.
        self._save(1, datasets=["Qwen2.5-7B"])
        self._save(2, models=["Qwen2.5-7B"])
        wiki.update(self.cfg, *concepts_mod.rebuild(self.cfg))
        self.assertTrue(
            (self.cfg.layout.wiki_kind_dir("model") / "qwen2-5-7b.md").exists()
        )

    def test_a_real_dataset_stays_a_dataset(self):
        self._save(1, datasets=["Open X-Embodiment"])
        self._save(2, datasets=["Open X-Embodiment"])
        wiki.update(self.cfg, *concepts_mod.rebuild(self.cfg))
        self.assertTrue(
            (self.cfg.layout.wiki_kind_dir("dataset") / "open-x-embodiment.md").exists()
        )


class DefinitionContractTests(unittest.TestCase):
    """What a definition task offers the reader, against what it accepts.

    The two are written in different files, and they drifted: the validator was
    widened to `WIKI_KINDS` when the `model` kind was added, while the schema
    string handed to the reader still enumerated three kinds. Nothing failed —
    a reader following the schema simply never answers `model`, and because a
    stored definition freezes the kind against re-derivation, a correctly
    harvested model entity is demoted permanently the first time it is defined.
    """

    def test_the_schema_offers_every_kind_the_validator_accepts(self):
        offered = llm.CONCEPT_OUTPUT_SCHEMA["kind"]
        for kind in WIKI_KINDS:
            self.assertIn(
                kind, offered, f"the concept schema never offers '{kind}'"
            )

    def test_the_validator_accepts_every_kind_the_schema_offers(self):
        for kind in WIKI_KINDS:
            errors = queue_mod.validate_result(
                "concept", {"definition": "A definition.", "kind": kind}
            )
            self.assertEqual(errors, [], f"'{kind}' was offered but refused")

    def test_a_kind_outside_the_tuple_is_still_refused(self):
        errors = queue_mod.validate_result(
            "concept", {"definition": "A definition.", "kind": "benchmark"}
        )
        self.assertTrue(errors, "an unknown kind must not be accepted")


class MigrationScriptTests(unittest.TestCase):
    """`scripts/migrate_model_kind.py` classification, exercised directly."""

    def setUp(self):
        spec = importlib.util.spec_from_file_location(
            "migrate_model_kind", REPO_ROOT / "scripts" / "migrate_model_kind.py"
        )
        self.mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.mod)

    def test_known_model_families_are_recognised(self):
        for name in ("Qwen2.5-Math-7B", "DeepSeek-R1-Distill-Qwen-7B", "Llama-3.1-8B",
                     "Mistral-7B", "Pythia-410M", "QwQ-32B", "gpt-oss-20b"):
            self.assertTrue(self.mod.is_model(name), name)

    def test_benchmarks_are_not_mistaken_for_models(self):
        for name in ("AIME24", "MATH500", "GSM8K", "OlympiadBench", "the Pile",
                     "GPQA-Diamond", "LiveCodeBench", "MT-Bench"):
            self.assertFalse(self.mod.is_model(name), name)


class RetopicScriptTests(unittest.TestCase):
    """`scripts/retopic.py` refuses unknown slugs and writes nothing when asked."""

    def test_unknown_slug_is_refused(self):
        proc = subprocess.run(
            [sys.executable, str(REPO_ROOT / "scripts" / "retopic.py"),
             "--topic", "definitely-not-a-topic", "--dry-run"],
            capture_output=True, text=True, cwd=REPO_ROOT,
        )
        self.assertEqual(proc.returncode, 2)
        self.assertIn("unknown topic", proc.stdout.lower())

    def test_dry_run_leaves_the_working_tree_clean(self):
        before = subprocess.run(
            ["git", "status", "--porcelain", "data"],
            capture_output=True, text=True, cwd=REPO_ROOT,
        ).stdout
        subprocess.run(
            [sys.executable, str(REPO_ROOT / "scripts" / "retopic.py"), "--dry-run"],
            capture_output=True, text=True, cwd=REPO_ROOT,
        )
        after = subprocess.run(
            ["git", "status", "--porcelain", "data"],
            capture_output=True, text=True, cwd=REPO_ROOT,
        ).stdout
        self.assertEqual(before, after, "--dry-run must not write to data/")


class DiscardScriptTests(unittest.TestCase):
    """`scripts/discard.py` is destructive, so its guards are what matter."""

    def _run(self, *args):
        return subprocess.run(
            [sys.executable, str(REPO_ROOT / "scripts" / "discard.py"), *args],
            capture_output=True, text=True, cwd=REPO_ROOT,
        )

    def test_a_mode_must_be_chosen(self):
        proc = self._run()
        self.assertNotEqual(proc.returncode, 0)

    def test_modes_are_mutually_exclusive(self):
        proc = self._run("--rescore", "--orphans")
        self.assertNotEqual(proc.returncode, 0)

    def test_an_unknown_id_is_refused(self):
        proc = self._run("--id", "arxiv:0000.00000", "--apply")
        self.assertEqual(proc.returncode, 2)
        self.assertIn("unknown paper id", proc.stdout.lower())

    def test_dry_run_is_the_default(self):
        before = subprocess.run(
            ["git", "status", "--porcelain", "data"],
            capture_output=True, text=True, cwd=REPO_ROOT,
        ).stdout
        self._run("--rescore")
        after = subprocess.run(
            ["git", "status", "--porcelain", "data"],
            capture_output=True, text=True, cwd=REPO_ROOT,
        ).stdout
        self.assertEqual(before, after, "discard must not write without --apply")

    def test_a_merged_hand_filed_record_is_still_hand_filed(self):
        """`source` is a `+`-joined set after `dedupe merge`, not a single word.

        A PDF filed in `inbox/` and later also collected from the ACL Anthology
        reads as `local+anthology`. The old equality test missed exactly those,
        so the hand-filed records with the *most* provenance were the ones a
        rescore proposed discarding -- against the archive's own rule that a
        reader's filing outranks any keyword score.
        """
        from types import SimpleNamespace

        import importlib.util

        spec = importlib.util.spec_from_file_location(
            "discard_mod", REPO_ROOT / "scripts" / "discard.py"
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        for source in ("local", "local+anthology", "anthology+local"):
            with self.subTest(source=source):
                self.assertTrue(module._hand_filed(SimpleNamespace(source=source)))
        for source in ("arxiv", "anthology", "", None, "nonlocal"):
            with self.subTest(source=source):
                self.assertFalse(module._hand_filed(SimpleNamespace(source=source)))

    def test_hand_filed_pdfs_are_never_selected_by_rescore(self):
        # The archive holds local records with no topics on purpose; a scoring
        # pass must not treat a reader's judgement as a scoring error.
        proc = self._run("--rescore")
        self.assertNotIn("local:", proc.stdout)


if __name__ == "__main__":
    unittest.main()
