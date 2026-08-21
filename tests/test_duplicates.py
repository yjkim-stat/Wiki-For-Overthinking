"""Concept slugs that are probably the same entity — and the promise not to act.

Two halves, deliberately, the same way `tests/test_layering.py` is two halves.

**Behavioural.** Every file under `data/` is snapshotted by content *and* by
modification time, the report runs over every code path, and the snapshot must
be unchanged. A content hash alone would miss a rewrite that produced identical
bytes, which is what re-serialising an unchanged record does.

**Static.** The module may not so much as mention a write. That catches a write
that has merely been written down, on a path no fixture reaches — which is the
plausible failure here, because a report that names duplicate entities is one
small refactor away from also merging them.
"""

from __future__ import annotations

import contextlib
import hashlib
import io
import re
import unittest
from pathlib import Path

from pipelines import duplicates
from pipelines.common import log as log_mod
from pipelines.common.paths import REPO_ROOT
from pipelines.common.schema import Concept
from pipelines.common.store import RecordStore

from .sandbox import Sandbox

SLUG = "test-topic"


def _snapshot(directory: Path) -> dict[str, tuple[str, int]]:
    return {
        path.relative_to(directory).as_posix(): (
            hashlib.sha256(path.read_bytes()).hexdigest(),
            path.stat().st_mtime_ns,
        )
        for path in sorted(directory.rglob("*"))
        if path.is_file()
    }


class RuleTests(unittest.TestCase):
    """Each rule against the pair it exists for, and against a pair it must not
    claim. A report tuned for recall still has to be a report."""

    def assertReason(self, a: str, b: str, expected: str) -> None:
        self.assertEqual(duplicates.reason_for(a, b), expected)
        # Symmetric: which slug is asked about first must not decide anything.
        self.assertEqual(duplicates.reason_for(b, a), expected)

    def test_a_separator_that_is_not_there_is_a_variant(self):
        self.assertReason("world-model", "worldmodel", "variant")

    def test_a_regular_plural_is_recognised(self):
        self.assertReason("world-model", "world-models", "plural")

    def test_the_plural_rule_is_the_one_topic_scoring_uses(self):
        """`common/text.py`, not a second copy: policy/policies and bias/biases
        are its two written-down rules and they have to hold here as well."""
        self.assertReason("policy", "policies", "plural")
        self.assertReason("bias", "biases", "plural")

    def test_only_the_head_word_pluralises(self):
        """"latent actions model" is not the plural of "latent action model" —
        `common/text.py` decides that, and this is the assertion that it still
        reaches the wiki."""
        self.assertNotEqual(
            duplicates.reason_for("latent-action-model", "latent-actions-model"),
            "plural",
        )

    def test_one_extra_trailing_word_is_a_suffix_pair(self):
        self.assertReason("world", "world-model", "suffix")

    def test_two_extra_words_are_not(self):
        """Two words on the end is usually a narrower thing, not the same thing
        named longer."""
        self.assertEqual(duplicates.reason_for("world", "world-model-search"), "")

    def test_an_extra_word_in_the_middle_is_not_a_suffix_pair(self):
        self.assertEqual(
            duplicates.reason_for("causal-effect", "causal-average-effect"), ""
        )

    def test_a_typo_is_within_reach(self):
        self.assertReason("transformer", "transfomer", "near")

    def test_a_transposition_of_two_letters_is_within_reach(self):
        self.assertReason("attention", "attnetion", "near")

    def test_three_edits_apart_is_not(self):
        """Two is the bound. Three starts relating terms that merely rhyme."""
        self.assertEqual(duplicates.reason_for("attention", "attemtiomx"), "")

    def test_short_slugs_are_not_compared_by_edit_distance(self):
        """On four characters an edit distance of two relates almost everything
        to almost everything, and a report that suggests every pair suggests
        nothing."""
        self.assertEqual(duplicates.reason_for("bert", "bart"), "")

    def test_short_slugs_are_still_compared_by_the_other_rules(self):
        """The length guard is about edit distance only. `gan`/`gans` is a real
        duplicate and one of the likeliest in any archive."""
        self.assertReason("gan", "gans", "plural")

    def test_a_slug_is_not_a_duplicate_of_itself(self):
        self.assertEqual(duplicates.reason_for("world-model", "world-model"), "")

    def test_two_unrelated_terms_are_not_paired(self):
        self.assertEqual(
            duplicates.reason_for("instrumental-variable", "behaviour-cloning"), ""
        )

    def test_precedence_reports_the_most_specific_rule(self):
        """A plural pair is also one edit apart. It is reported as a plural,
        because that is the rule that says what to do about it."""
        self.assertReason("world-model", "world-models", "plural")


class ReportTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.addCleanup(self.sandbox.close)
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)

    def _concept(self, slug: str, sources: int, *, definition: str = "") -> Concept:
        concept = Concept(
            slug=slug,
            name=slug.replace("-", " ").title(),
            topics=[SLUG],
            definition=definition,
            evidence=[
                {"kind": "paper", "id": f"arxiv:2401.{n:05d}", "title": "x", "note": ""}
                for n in range(sources)
            ],
        )
        self.store.save_concept(concept)
        return concept

    def test_a_pair_carries_both_source_counts_and_both_definitions(self):
        self._concept("world-model", 9, definition="A model of the world.")
        self._concept("world-models", 2)
        pair = duplicates.candidates(self.store)[0]
        self.assertEqual(pair["reason"], "plural")
        self.assertEqual(pair["a"]["sources"], 9)
        self.assertTrue(pair["a"]["defined"])
        self.assertEqual(pair["b"]["sources"], 2)
        self.assertFalse(pair["b"]["defined"])

    def test_the_better_evidenced_side_is_named_first(self):
        """It is the likelier survivor of a merge, so it is what a reader wants
        to see first."""
        self._concept("world-model", 2)
        self._concept("world-models", 9)
        pair = duplicates.candidates(self.store)[0]
        self.assertEqual(pair["a"]["slug"], "world-models")
        self.assertEqual(pair["b"]["slug"], "world-model")

    def test_the_pair_with_the_most_at_stake_comes_first(self):
        """Eighteen sources between them outranks two, whichever rule paired
        them: the report is skimmed from the top."""
        self._concept("policy", 1)
        self._concept("policies", 1)
        self._concept("world-model", 9)
        self._concept("world-models", 9)
        pairs = duplicates.candidates(self.store)
        self.assertEqual(
            [pairs[0]["a"]["slug"], pairs[0]["b"]["slug"]],
            ["world-model", "world-models"],
        )
        self.assertEqual(
            [pairs[1]["a"]["slug"], pairs[1]["b"]["slug"]], ["policies", "policy"]
        )

    def test_the_same_archive_produces_the_same_list_twice(self):
        for slug in ("policy", "policies", "world-model", "world-models"):
            self._concept(slug, 3)
        self.assertEqual(
            duplicates.candidates(self.store), duplicates.candidates(self.store)
        )

    def test_an_archive_with_no_duplicates_reports_none(self):
        self._concept("instrumental-variable", 4)
        self._concept("behaviour-cloning", 4)
        report = duplicates.run(self.cfg)
        self.assertEqual(report["candidates"], 0)
        self.assertEqual(report["pairs"], [])

    def test_the_report_counts_what_it_looked_at(self):
        self._concept("world-model", 2)
        self._concept("world-models", 2)
        self._concept("behaviour-cloning", 2)
        report = duplicates.run(self.cfg)
        self.assertEqual(report["concepts"], 3)
        self.assertEqual(report["candidates"], 1)
        self.assertEqual(report["by_reason"]["plural"], 1)

    def test_limit_bounds_the_pairs_shown_but_not_the_count(self):
        """A limit that also shrank the total would answer a different question
        from the one printed beside it."""
        for slug in ("policy", "policies", "world-model", "world-models"):
            self._concept(slug, 3)
        report = duplicates.run(self.cfg, limit=1)
        self.assertEqual(report["candidates"], 2)
        self.assertEqual(len(report["pairs"]), 1)

    def test_the_text_report_names_both_slugs_and_says_nothing_was_merged(self):
        self._concept("world-model", 9)
        self._concept("world-models", 2)
        text = duplicates.format_report(duplicates.run(self.cfg))
        self.assertIn("world-model", text)
        self.assertIn("world-models", text)
        self.assertIn("Nothing was merged", text)


class TheReportWritesNothing(unittest.TestCase):
    """The property the whole design rests on, asserted rather than believed."""

    def setUp(self):
        self.sandbox = Sandbox()
        self.addCleanup(self.sandbox.close)
        self.cfg = self.sandbox.config()
        store = RecordStore(self.cfg.layout)
        for slug, sources in (
            ("world-model", 9),
            ("world-models", 2),
            ("worldmodel", 1),
            ("behaviour-cloning", 4),
        ):
            store.save_concept(
                Concept(
                    slug=slug,
                    name=slug,
                    topics=[SLUG],
                    evidence=[
                        {"kind": "paper", "id": f"arxiv:2401.{n:05d}", "title": "x",
                         "note": ""}
                        for n in range(sources)
                    ],
                )
            )
        self.data = self.cfg.layout.data

    def test_every_path_through_the_report_leaves_the_archive_untouched(self):
        before = _snapshot(self.data)
        root = str(self.sandbox.root)
        duplicates.run(self.cfg)
        duplicates.run(self.cfg, limit=1)
        duplicates.format_report(duplicates.run(self.cfg))
        with contextlib.redirect_stdout(io.StringIO()):
            duplicates.main(["--root", root])
            duplicates.main(["--root", root, "--json"])
            duplicates.main(["--root", root, "--limit", "1"])
        self.assertEqual(_snapshot(self.data), before)

    def test_it_creates_no_file_anywhere_under_the_root(self):
        """Not only `data/`: a log file or a cached result would be a write too,
        and `data/logs/` is not the only place one could land.

        `common.log.setup` configures the root logger once per *process*, so by
        the time this runs another test has usually already configured it and a
        `log.setup` slipped into the command line would be a no-op here — the
        test would pass against exactly the mutation it exists to catch. The
        flag is cleared and restored so the check is a real one.
        """
        configured = log_mod._CONFIGURED
        log_mod._CONFIGURED = False
        self.addCleanup(setattr, log_mod, "_CONFIGURED", configured)

        before = _snapshot(self.sandbox.root)
        with contextlib.redirect_stdout(io.StringIO()):
            duplicates.main(["--root", str(self.sandbox.root), "--json"])
        self.assertEqual(_snapshot(self.sandbox.root), before)


class TheModuleHoldsNoWrite(unittest.TestCase):
    """A tripwire, cheaper than the behavioural tests and easier to read.

    Those catch a write that happens; this catches one that has merely been
    written down, including on a path no fixture reaches.
    """

    WRITERS = re.compile(
        r"\.save_(paper|video|concept|finding|abstracts|transcript)"
        r"|write_json|write_text|write_bytes|\.unlink\(|\.replace\(.*Path"
    )

    def test_the_module_mentions_no_write_at_all(self):
        path = REPO_ROOT / "pipelines" / "duplicates.py"
        offenders = [
            f"{path.name}:{number}: {line.strip()}"
            for number, line in enumerate(
                path.read_text(encoding="utf-8").splitlines(), 1
            )
            if self.WRITERS.search(line)
        ]
        self.assertEqual(
            offenders,
            [],
            "the duplicate report suggests and merges nothing; it must not write",
        )


if __name__ == "__main__":
    unittest.main()
