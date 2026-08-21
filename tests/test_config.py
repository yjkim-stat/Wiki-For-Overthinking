import os
import unittest
from pathlib import Path
from unittest import mock

from pipelines.common import config as config_mod
from pipelines.common.paths import (
    REPO_ROOT,
    ROOT_ENV,
    RootError,
    fs_id,
    resolve_root,
    slugify,
)

from .sandbox import Sandbox


class SlugTests(unittest.TestCase):
    def test_slugify(self):
        self.assertEqual(slugify("Doubly-Robust Estimation!"), "doubly-robust-estimation")

    def test_slugify_never_returns_empty(self):
        self.assertEqual(slugify("!!!"), "untitled")

    def test_fs_id_is_path_safe(self):
        self.assertEqual(fs_id("arxiv:2401.12345"), "arxiv-2401-12345")
        self.assertNotIn("/", fs_id("doi:10.1000/xyz"))


class TopicLoadingTests(unittest.TestCase):
    def test_loads_a_topic(self):
        with Sandbox({"my-topic": "My Topic"}) as sandbox:
            cfg = sandbox.config()
            self.assertEqual([t.slug for t in cfg.topics], ["my-topic"])
            self.assertEqual(cfg.topic("my-topic").name, "My Topic")

    def test_underscore_prefixed_files_are_skipped(self):
        with Sandbox() as sandbox:
            (sandbox.root / "config" / "topics" / "_draft.yaml").write_text(
                "slug: _draft\nname: Draft\nkeywords:\n  any: [x]\n", encoding="utf-8"
            )
            self.assertEqual(len(sandbox.config().topics), 1)

    def test_slug_must_match_filename(self):
        with Sandbox() as sandbox:
            (sandbox.root / "config" / "topics" / "wrong.yaml").write_text(
                "slug: other\nname: N\nkeywords:\n  any: [x]\n", encoding="utf-8"
            )
            with self.assertRaises(config_mod.ConfigError):
                sandbox.config()

    def test_topic_without_any_keywords_is_rejected(self):
        with Sandbox() as sandbox:
            (sandbox.root / "config" / "topics" / "empty.yaml").write_text(
                "slug: empty\nname: E\nkeywords:\n  any: []\n", encoding="utf-8"
            )
            with self.assertRaises(config_mod.ConfigError):
                sandbox.config()

    def test_no_topics_is_not_an_error(self):
        with Sandbox() as sandbox:
            for path in (sandbox.root / "config" / "topics").glob("*.yaml"):
                path.unlink()
            self.assertEqual(sandbox.config().topics, [])

    def test_unknown_topic_lookup_raises(self):
        with Sandbox() as sandbox:
            with self.assertRaises(KeyError):
                sandbox.config().topic("nope")


class TopicBehaviourTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.topic = self.cfg.topics[0]

    def tearDown(self):
        self.sandbox.close()

    def test_threshold_prefers_the_topic_value(self):
        self.assertAlmostEqual(self.topic.threshold(self.cfg.settings), 0.3)

    def test_threshold_falls_back_to_settings(self):
        self.topic.min_score = None
        self.assertAlmostEqual(self.topic.threshold(self.cfg.settings), 0.35)

    def test_source_enabled_defaults_to_true(self):
        self.assertTrue(self.topic.source_enabled("anything-unlisted"))

    def test_empty_source_list_does_not_narrow(self):
        # An empty `venues:` list means "all venues", not "no venues".
        self.assertEqual(
            self.topic.source_option("conferences", "venues", ["ICLR"]), ["ICLR"]
        )

    def test_outputs_default_to_enabled(self):
        self.assertTrue(self.topic.wants("report"))


class RealConfigTests(unittest.TestCase):
    """The configs shipped in the repository must be loadable as-is."""

    def test_repository_config_loads(self):
        cfg = config_mod.load(REPO_ROOT)
        self.assertEqual(cfg.language, "en")
        self.assertIn("arxiv", cfg.sources)
        self.assertIn("venues", cfg.sources["conferences"])

    def test_template_topic_is_not_loaded(self):
        cfg = config_mod.load(REPO_ROOT)
        self.assertNotIn("my-topic", [t.slug for t in cfg.topics])


class DeploymentRootTests(unittest.TestCase):
    """Which tree an entry point writes to, and how it is chosen.

    The archive can live in a repository of its own, so that pulling a new
    version of the code cannot collide with a month of readings. That only
    holds if every entry point agrees on where the archive is.
    """

    def test_no_root_and_no_environment_means_this_checkout(self):
        with mock.patch.dict(os.environ, {}, clear=False):
            os.environ.pop(ROOT_ENV, None)
            self.assertIsNone(resolve_root())

    def test_the_environment_names_the_root(self):
        with Sandbox() as sandbox:
            with mock.patch.dict(os.environ, {ROOT_ENV: str(sandbox.root)}):
                self.assertEqual(resolve_root(), sandbox.root)

    def test_an_explicit_root_outranks_the_environment(self):
        with Sandbox() as sandbox:
            with mock.patch.dict(os.environ, {ROOT_ENV: "/somewhere/else"}):
                self.assertEqual(resolve_root(sandbox.root), sandbox.root)

    def test_a_root_that_is_not_there_raises(self):
        """The failure this prevents is the quiet one.

        A typo would otherwise fall back to this checkout and write the
        deployment's archive into the code repository, which looks like a
        successful run from every angle until somebody reads the diff.
        """
        with mock.patch.dict(os.environ, {ROOT_ENV: "/no/such/deployment"}):
            with self.assertRaises(RootError):
                resolve_root()

    def test_config_loads_from_the_environment_named_root(self):
        with Sandbox({"env-topic": "Env Topic"}) as sandbox:
            with mock.patch.dict(os.environ, {ROOT_ENV: str(sandbox.root)}):
                cfg = config_mod.load()
            self.assertEqual([t.slug for t in cfg.topics], ["env-topic"])
            self.assertEqual(cfg.layout.root, sandbox.root)
            self.assertEqual(cfg.layout.papers, sandbox.root / "data" / "papers")

    def test_a_home_relative_root_is_expanded(self):
        with mock.patch.dict(os.environ, {ROOT_ENV: "~"}):
            self.assertEqual(resolve_root(), Path.home())


if __name__ == "__main__":
    unittest.main()
