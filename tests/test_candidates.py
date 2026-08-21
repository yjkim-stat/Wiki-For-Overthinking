"""The candidate lane: what a collector may decide, and what it may not.

These are ours ( if the lane is ever taken upstream).
They touch neither the network nor the real archive.
"""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from pipelines import candidates as C
from pipelines.collect import github
from pipelines.common import config as config_mod


def _repo(name="acme/thing", stars=100, description="chain-of-thought reasoning toolkit"):
    return {
        "html_url": f"https://github.com/{name}",
        "full_name": name,
        "description": description,
        "stargazers_count": stars,
        "pushed_at": "2026-08-01T00:00:00Z",
        "language": "Python",
        "license": {"spdx_id": "MIT"},
        "topics": [],
    }


class _Root(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        (self.root / "config" / "topics").mkdir(parents=True)
        (self.root / "config" / "settings.yaml").write_text("language: en\n", encoding="utf-8")
        (self.root / "config" / "sources.yaml").write_text(
            "github:\n  enabled: true\n  min_stars: 25\n", encoding="utf-8"
        )
        (self.root / "config" / "topics" / "t.yaml").write_text(
            "slug: t\nname: T\nmin_score: 0.1\nkeywords:\n  any:\n    - chain-of-thought\n", encoding="utf-8"
        )
        self.addCleanup(self._tmp.cleanup)
        self.cfg = config_mod.load(root=self.root)
        self.cfg.layout.ensure()

    def _candidate(self, **kw):
        return github.Candidate(
            id=kw.get("id", "web:abc"),
            url=kw.get("url", "https://github.com/acme/thing"),
            full_name=kw.get("full_name", "acme/thing"),
            scores=kw.get("scores", {"t": 1.0}),
        )


class CollectorWritesNothingTests(_Root):
    def test_collect_returns_candidates_and_writes_no_record(self):
        class _Client:
            def get_json(self, url, headers=None):
                return {"items": [_repo()]}

        found = github.collect(self.cfg, client=_Client())
        self.assertEqual(len(found), 1)
        # Not a record, and not filed either: filing is a separate decision.
        self.assertEqual(list(self.cfg.layout.candidates_pending.glob("*.json")), [])
        self.assertEqual(list(self.cfg.layout.papers.glob("*.json")), [])
        self.assertEqual(list(self.cfg.layout.references.glob("*.json")), [])

    def test_a_repository_below_the_star_floor_is_not_offered(self):
        class _Client:
            def get_json(self, url, headers=None):
                return {"items": [_repo(stars=3)]}

        self.assertEqual(github.collect(self.cfg, client=_Client()), [])

    def test_a_repository_no_topic_accepts_is_not_offered(self):
        class _Client:
            def get_json(self, url, headers=None):
                return {"items": [_repo(description="a static site generator")]}

        self.assertEqual(github.collect(self.cfg, client=_Client()), [])

    def test_an_unreachable_search_is_skipped_not_fatal(self):
        class _Client:
            def get_json(self, url, headers=None):
                raise OSError("no route to host")

        self.assertEqual(github.collect(self.cfg, client=_Client()), [])


class PromotionTests(_Root):
    def test_promote_writes_a_reference_carrying_the_quotation(self):
        C.file_new(self.cfg, [self._candidate()])
        reference = C.promote(self.cfg, "web:abc", quoted="the README's claim we relied on")
        self.assertIsNotNone(reference)
        self.assertEqual(reference.quoted, "the README's claim we relied on")
        self.assertEqual(reference.publisher, "github.com")
        self.assertTrue(reference.retrieved_at)
        stored = json.loads(
            (self.cfg.layout.references / f"{reference.id.replace(':', '-')}.json").read_text()
        )
        self.assertEqual(stored["url"], "https://github.com/acme/thing")

    def test_promotion_never_touches_an_entity(self):
        """A reference is not evidence. The lane must not be a way around that."""
        C.file_new(self.cfg, [self._candidate()])
        C.promote(self.cfg, "web:abc", quoted="q")
        self.assertEqual(list(self.cfg.layout.concepts.glob("*.json")), [])
        self.assertEqual(list(self.cfg.layout.papers.glob("*.json")), [])

    def test_a_promoted_candidate_leaves_pending(self):
        C.file_new(self.cfg, [self._candidate()])
        C.promote(self.cfg, "web:abc", quoted="q")
        self.assertEqual(list(self.cfg.layout.candidates_pending.glob("*.json")), [])
        self.assertEqual(len(list(self.cfg.layout.candidates_promoted.glob("*.json"))), 1)


class DecisionsAreRememberedTests(_Root):
    def test_a_dropped_candidate_is_never_offered_again(self):
        """The decision is the record. A daily run must not re-file a refusal."""
        C.file_new(self.cfg, [self._candidate()])
        self.assertTrue(C.drop(self.cfg, "web:abc", reason="a wrapper, not a method"))
        refiled = C.file_new(self.cfg, [self._candidate()])
        self.assertEqual(refiled, [])
        self.assertEqual(C.pending(self.cfg), [])

    def test_a_promoted_candidate_is_never_offered_again(self):
        C.file_new(self.cfg, [self._candidate()])
        C.promote(self.cfg, "web:abc", quoted="q")
        self.assertEqual(C.file_new(self.cfg, [self._candidate()]), [])

    def test_a_drop_keeps_its_reason(self):
        C.file_new(self.cfg, [self._candidate()])
        C.drop(self.cfg, "web:abc", reason="a wrapper, not a method")
        stored = json.loads((self.cfg.layout.candidates_dropped / "web:abc.json").read_text())
        self.assertEqual(stored["reason"], "a wrapper, not a method")
        self.assertEqual(stored["decision"], "dropped")


class DryRunTests(_Root):
    def test_a_dry_run_of_the_daily_collector_files_nothing(self):
        """`--dry-run` reports what would be collected. It writes no lane file."""
        from unittest import mock

        from pipelines import run_daily

        with mock.patch.object(
            run_daily.github, "collect", return_value=[self._candidate()]
        ), mock.patch.object(run_daily.github, "enabled", return_value=True):
            result = run_daily.run(self.cfg, sources=["github"], dry_run=True)
        self.assertEqual(result["candidates_filed"], 1)
        self.assertEqual(list(self.cfg.layout.candidates_pending.glob("*.json")), [])


class CLIContractTests(_Root):
    def test_promote_without_a_quotation_is_refused(self):
        """The friction is the feature: no quotation, no citation."""
        with self.assertRaises(SystemExit):
            C.main(["--root", str(self.root), "promote", "web:abc"])


if __name__ == "__main__":
    unittest.main()
