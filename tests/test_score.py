import unittest

from pipelines.common.config import Topic
from pipelines.common.text import matcher as _pattern
from pipelines.enrich.score import score_against_topics, score_item

SETTINGS = {
    "score": {
        "title_weight": 3.0,
        "abstract_weight": 1.0,
        "author_bonus": 2.0,
        "default_min_score": 0.35,
    }
}


def topic(**kwargs) -> Topic:
    base = dict(
        slug="t",
        name="T",
        keywords_any=["causal inference"],
        keywords_all=[],
        keywords_none=[],
        authors=[],
    )
    base.update(kwargs)
    return Topic(**base)


class ScoreItemTests(unittest.TestCase):
    def test_title_hit_scores_higher_than_abstract_hit(self):
        in_title = score_item(topic(), title="A causal inference study", settings=SETTINGS)
        in_body = score_item(
            topic(), title="Something", body="a causal inference study", settings=SETTINGS
        )
        self.assertGreater(in_title.score, in_body.score)

    def test_single_title_hit_lands_at_one_half(self):
        result = score_item(topic(), title="Causal Inference at scale", settings=SETTINGS)
        self.assertAlmostEqual(result.score, 0.5, places=6)

    def test_no_match_is_rejected(self):
        result = score_item(topic(), title="Unrelated work", settings=SETTINGS)
        self.assertFalse(result.accepted)
        self.assertEqual(result.rejected, "no keyword matched")

    def test_excluded_keyword_wins_over_a_match(self):
        result = score_item(
            topic(keywords_none=["survey"]),
            title="A survey of causal inference",
            settings=SETTINGS,
        )
        self.assertFalse(result.accepted)
        self.assertIn("survey", result.rejected)

    def test_required_keyword_must_be_present(self):
        result = score_item(
            topic(keywords_all=["panel data"]),
            title="Causal inference for cross-sections",
            settings=SETTINGS,
        )
        self.assertFalse(result.accepted)
        self.assertIn("panel data", result.rejected)

    def test_required_keyword_contributes_to_the_score(self):
        result = score_item(
            topic(keywords_all=["panel data"]),
            title="Causal inference for panel data",
            settings=SETTINGS,
        )
        self.assertTrue(result.accepted)
        self.assertGreater(result.score, 0.5)

    def test_tracked_author_adds_a_bonus(self):
        without = score_item(topic(), title="Causal inference", settings=SETTINGS)
        with_author = score_item(
            topic(authors=["Ada Lovelace"]),
            title="Causal inference",
            authors=["Ada Lovelace", "Someone Else"],
            settings=SETTINGS,
        )
        self.assertGreater(with_author.score, without.score)

    def test_word_boundaries_prevent_substring_matches(self):
        result = score_item(
            topic(keywords_any=["ATE"]), title="Water quality models", settings=SETTINGS
        )
        self.assertFalse(result.accepted)

    def test_hyphen_and_space_are_interchangeable(self):
        result = score_item(
            topic(keywords_any=["causal inference"]),
            title="A causal-inference approach",
            settings=SETTINGS,
        )
        self.assertTrue(result.accepted)

    def test_matching_is_case_insensitive(self):
        self.assertTrue(
            score_item(topic(), title="CAUSAL INFERENCE", settings=SETTINGS).accepted
        )

    def test_score_never_reaches_one(self):
        result = score_item(
            topic(keywords_any=["a", "b", "c", "d", "e"]),
            title="a b c d e",
            settings=SETTINGS,
        )
        self.assertLess(result.score, 1.0)


class MultiTopicTests(unittest.TestCase):
    def test_threshold_separates_scored_from_accepted(self):
        topics = [
            topic(slug="strong", min_score=0.4),
            topic(slug="picky", min_score=0.9),
        ]
        scores, matched, accepted = score_against_topics(
            topics, title="Causal inference", settings=SETTINGS
        )
        self.assertEqual(set(scores), {"strong", "picky"})
        self.assertEqual(accepted, ["strong"])
        self.assertIn("causal inference", matched)

    def test_rejected_topics_are_absent_from_scores(self):
        topics = [topic(slug="a"), topic(slug="b", keywords_any=["nothing here"])]
        scores, _, _ = score_against_topics(
            topics, title="Causal inference", settings=SETTINGS
        )
        self.assertEqual(list(scores), ["a"])


if __name__ == "__main__":
    unittest.main()


class PluralMatchingTests(unittest.TestCase):
    """Regular plurals match, and the boundaries that made them fail still hold.

    Plural blindness cuts both ways: a `keywords.any` miss keeps a wanted paper
    out, and a `keywords.none` miss lets an unwanted one through. Neither is
    logged, because a non-match is not an event.
    """

    def assertMatches(self, term, text):
        self.assertTrue(_pattern(term).search(text), f"{term!r} should match {text!r}")

    def assertNoMatch(self, term, text):
        self.assertIsNone(_pattern(term).search(text), f"{term!r} should not match {text!r}")

    def test_the_observed_failures_now_match(self):
        self.assertMatches("action chunk", "large action chunks (sequences of actions)")
        self.assertMatches("robot policy", "parameterizations of robot policies")
        self.assertMatches("conversational agent", "Multimodal Conversational Agents")
        self.assertMatches("VLA", "VLAs are everywhere")

    def test_the_singular_still_matches(self):
        self.assertMatches("action chunk", "one action chunk")
        self.assertMatches("robot policy", "a robot policy")

    def test_the_vowel_y_carve_out(self):
        self.assertMatches("survey", "two surveys")
        self.assertNoMatch("survey", "survies")

    def test_sibilant_endings_take_es(self):
        self.assertMatches("bias", "known biases")
        self.assertMatches("benchmark", "benchmarks")

    def test_only_the_last_word_inflects(self):
        self.assertMatches("latent action model", "latent action models")
        self.assertNoMatch("latent action model", "latent actions model")

    def test_word_boundaries_still_hold(self):
        self.assertNoMatch("VLA", "Vlasov")
        self.assertNoMatch("world model", "worldly models")
        self.assertNoMatch("action chunk", "a chunk of actions")
        self.assertNoMatch("ATE", "Water")

    def test_hyphen_and_whitespace_tolerance_survives(self):
        self.assertMatches("causal inference", "causal-inference")
        self.assertMatches("causal inference", "causal\n  inferences")
