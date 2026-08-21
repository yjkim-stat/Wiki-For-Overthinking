"""Keyword pairs where one term occurs inside another.

A single occurrence in a title then matches both and adds to the score twice.
`enrich/score.py` loops over the terms with no notion that two of them might be
the same words — deliberately, because a rule you can read and correct beats an
opaque score — and the cost of that simplicity is that redundancy in the list is
the author's problem.

Note 0017 said so when it made keywords match plurals: a redundancy check
"belongs in the test suite or a config check; it is not there yet". This is that
gap, closed.

**The four live pairs are recorded, not resolved.** Which term to drop is an
editorial decision about what a topic tracks: the short one has broader recall
and the long one is presumably there to weight a specific phrase higher, so
neither is obviously wrong. What this stops is a *fifth* appearing without
anybody noticing.
"""

from __future__ import annotations

import unittest

from pipelines.common import config as config_mod
from pipelines.common.config import Topic, overlapping_keywords

# Every overlap in `config/topics/` as of 2026-08-21, unresolved. Removing one
# is an editorial decision and this list moves with it; a pair appearing here
# that nobody added on purpose is the thing being caught.
# See docs/solved/keyword-substring-pairs-score-twice.md
# Overlaps that a person has looked at and decided to keep, as
# (topic slug, shorter term, longer term). A deployment adds a row here in the
# same edit that decides to live with the double count, and deletes the row in
# the same edit that resolves it. This repository ships no topics, so the list
# is empty and any overlap at all fails the test below.
KNOWN: list[tuple[str, str, str]] = []


def _topic(slug: str, *terms: str) -> Topic:
    return Topic(slug=slug, name=slug, keywords_any=list(terms))


class DetectionTests(unittest.TestCase):
    def test_a_contained_term_is_reported_with_its_container(self):
        found = overlapping_keywords([_topic("t", "chain of thought",
                                             "long chain of thought")])
        self.assertEqual(found, [("t", "chain of thought",
                                  "long chain of thought")])

    def test_unrelated_terms_are_not(self):
        self.assertEqual(
            overlapping_keywords([_topic("t", "causal inference", "diffusion")]), []
        )

    def test_it_uses_the_scorer_s_matcher_not_a_substring_test(self):
        """A check that disagreed with the scorer would report the wrong pairs.

        `ate` is inside `state` as a substring and is not an occurrence of it:
        `common/text.py` matches on word boundaries, so scoring never counts
        that twice and neither does this.
        """
        self.assertEqual(overlapping_keywords([_topic("t", "ate", "state")]), [])

    def test_a_plural_container_still_counts(self):
        """The matcher inflects the head word, so the scorer counts it twice."""
        found = overlapping_keywords([_topic("t", "reasoning model",
                                             "large reasoning models")])
        self.assertEqual(len(found), 1)

    def test_a_term_does_not_overlap_itself(self):
        self.assertEqual(overlapping_keywords([_topic("t", "chain of thought")]), [])


class ShippedConfigTests(unittest.TestCase):
    """What the tracked topics actually contain."""

    def test_no_overlap_has_appeared_that_nobody_recorded(self):
        """The point of the test: an unrecorded overlap fails here.

        A pair that somebody has weighed and accepted goes in `KNOWN`; one that
        nobody has seen yet does not, and that is the difference this asserts.
        The list moves in the same edit as the topic file, in both directions.
        """
        found = overlapping_keywords(config_mod.load().topics)
        self.assertEqual(found, KNOWN)

    def test_a_run_says_so_before_it_collects(self):
        """Where somebody who has just edited a topic file will see it."""
        import inspect

        from pipelines import run_daily

        source = inspect.getsource(run_daily.run)
        self.assertIn("overlapping_keywords", source)
        self.assertIn("scores twice", source)


if __name__ == "__main__":
    unittest.main()
