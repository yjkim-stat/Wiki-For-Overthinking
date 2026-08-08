import unittest

from pipelines.common.config import Topic
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
        keywords_any=["world model"],
        keywords_all=[],
        keywords_none=[],
        authors=[],
    )
    base.update(kwargs)
    return Topic(**base)


class ScoreItemTests(unittest.TestCase):
    def test_title_hit_scores_higher_than_abstract_hit(self):
        in_title = score_item(topic(), title="A world model", settings=SETTINGS)
        in_body = score_item(
            topic(), title="Something", body="a world model", settings=SETTINGS
        )
        self.assertGreater(in_title.score, in_body.score)

    def test_single_title_hit_lands_at_one_half(self):
        result = score_item(topic(), title="World Model scaling", settings=SETTINGS)
        self.assertAlmostEqual(result.score, 0.5, places=6)

    def test_no_match_is_rejected(self):
        result = score_item(topic(), title="Unrelated work", settings=SETTINGS)
        self.assertFalse(result.accepted)
        self.assertEqual(result.rejected, "no keyword matched")

    def test_excluded_keyword_wins_over_a_match(self):
        result = score_item(
            topic(keywords_none=["survey"]),
            title="A survey of world models",
            settings=SETTINGS,
        )
        self.assertFalse(result.accepted)
        self.assertIn("survey", result.rejected)

    def test_required_keyword_must_be_present(self):
        result = score_item(
            topic(keywords_all=["manipulation"]),
            title="A world model for navigation",
            settings=SETTINGS,
        )
        self.assertFalse(result.accepted)
        self.assertIn("manipulation", result.rejected)

    def test_required_keyword_contributes_to_the_score(self):
        result = score_item(
            topic(keywords_all=["manipulation"]),
            title="A world model for manipulation",
            settings=SETTINGS,
        )
        self.assertTrue(result.accepted)
        self.assertGreater(result.score, 0.5)

    def test_tracked_author_adds_a_bonus(self):
        without = score_item(topic(), title="World model", settings=SETTINGS)
        with_author = score_item(
            topic(authors=["Ada Lovelace"]),
            title="World model",
            authors=["Ada Lovelace", "Someone Else"],
            settings=SETTINGS,
        )
        self.assertGreater(with_author.score, without.score)

    def test_word_boundaries_prevent_substring_matches(self):
        result = score_item(
            topic(keywords_any=["VLA"]), title="Vlasov equations", settings=SETTINGS
        )
        self.assertFalse(result.accepted)

    def test_hyphen_and_space_are_interchangeable(self):
        result = score_item(
            topic(keywords_any=["world model"]),
            title="A world-model approach",
            settings=SETTINGS,
        )
        self.assertTrue(result.accepted)

    def test_matching_is_case_insensitive(self):
        self.assertTrue(
            score_item(topic(), title="WORLD MODEL", settings=SETTINGS).accepted
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
            topics, title="World model", settings=SETTINGS
        )
        self.assertEqual(set(scores), {"strong", "picky"})
        self.assertEqual(accepted, ["strong"])
        self.assertIn("world model", matched)

    def test_rejected_topics_are_absent_from_scores(self):
        topics = [topic(slug="a"), topic(slug="b", keywords_any=["nothing here"])]
        scores, _, _ = score_against_topics(
            topics, title="World model", settings=SETTINGS
        )
        self.assertEqual(list(scores), ["a"])


if __name__ == "__main__":
    unittest.main()
