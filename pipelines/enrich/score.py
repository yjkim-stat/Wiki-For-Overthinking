"""Topic relevance scoring.

Deliberately transparent: a keyword rule you can read and correct beats an
opaque score you cannot argue with. Items below a topic's threshold are still
recorded in the index — the archive keeps a record of what was considered and
rejected, so a threshold can be revisited later without re-collecting.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from ..common.config import Topic
from ..common.text import contains as _find
from ..common.text import matcher as _pattern


@dataclass
class ScoreResult:
    """Outcome of scoring one item against one topic."""

    slug: str
    score: float = 0.0
    matched: list[str] = field(default_factory=list)
    matched_authors: list[str] = field(default_factory=list)
    rejected: str = ""  # non-empty means a hard rule excluded the item

    @property
    def accepted(self) -> bool:
        return not self.rejected


def score_item(
    topic: Topic,
    *,
    title: str,
    body: str = "",
    authors: list[str] | None = None,
    settings: dict | None = None,
) -> ScoreResult:
    """Score one item against one topic.

    ``title`` hits count for more than ``body`` hits, because a term in the
    title is what the work is about while a term in an abstract may be a
    passing reference.
    """
    settings = settings or {}
    weights = settings.get("score", {})
    title_weight = float(weights.get("title_weight", 3.0))
    body_weight = float(weights.get("abstract_weight", 1.0))
    author_bonus = float(weights.get("author_bonus", 2.0))

    title = title or ""
    body = body or ""
    haystack = f"{title}\n{body}"
    result = ScoreResult(slug=topic.slug)

    for term in topic.keywords_none:
        if _find(term, haystack):
            result.rejected = f"excluded by keyword: {term}"
            return result

    for term in topic.keywords_all:
        if not _find(term, haystack):
            result.rejected = f"missing required keyword: {term}"
            return result

    raw = 0.0
    for term in topic.keywords_any:
        if _find(term, title):
            raw += title_weight
            result.matched.append(term)
        elif _find(term, body):
            raw += body_weight
            result.matched.append(term)

    for term in topic.keywords_all:
        # Required terms already matched above; count them toward the score
        # too, otherwise an `all`-only topic would always score zero.
        raw += title_weight if _find(term, title) else body_weight
        result.matched.append(term)

    if not result.matched:
        result.rejected = "no keyword matched"
        return result

    author_blob = " ; ".join(authors or [])
    for name in topic.authors:
        if _find(name, author_blob):
            raw += author_bonus
            result.matched_authors.append(name)

    # Saturating normalization into (0, 1): one title hit lands at 0.5, and
    # further hits add progressively less. Keeps thresholds comparable across
    # topics with very different keyword-list sizes.
    result.score = raw / (raw + title_weight) if raw > 0 else 0.0
    return result


def score_against_topics(
    topics: list[Topic],
    *,
    title: str,
    body: str = "",
    authors: list[str] | None = None,
    settings: dict | None = None,
) -> tuple[dict[str, float], list[str], list[str]]:
    """Score against every topic.

    Returns ``(scores, matched_keywords, accepted_slugs)`` where ``scores``
    holds every topic that passed its hard rules, and ``accepted_slugs`` holds
    only those that also cleared the topic threshold.
    """
    settings = settings or {}
    scores: dict[str, float] = {}
    matched: list[str] = []
    accepted: list[str] = []

    for topic in topics:
        result = score_item(
            topic, title=title, body=body, authors=authors, settings=settings
        )
        if not result.accepted:
            continue
        scores[topic.slug] = round(result.score, 4)
        for term in result.matched + result.matched_authors:
            if term not in matched:
                matched.append(term)
        if result.score >= topic.threshold(settings):
            accepted.append(topic.slug)

    return scores, matched, accepted


def leverage(record) -> float:
    """How much this archive's topics care about an item nobody has read yet.

    Takes any record carrying ``topics`` and ``scores`` — a ``Paper`` or a
    ``Video`` — and sums the scores over the topics that *accepted* it. Summing
    rather than taking the best one prefers an item several tracked subjects
    want over one that a single subject wants badly, which is breadth across
    what the group tracks.

    **This is not the leverage the requirement asked for**, and the
    substitution is deliberate rather than an approximation. The specification
    says to order by the source counts of the entities an item is evidence for
    — which is exact, and undefined for everything unread: entities take their
    evidence from summaries, an unread item has no summary, and so no entity
    cites it. Every candidate would score zero and the ordering would degenerate
    to whatever the store happened to yield.

    What the archive does know before anybody has read an item is what scoring
    decided when it arrived. That is this number, and it lives here — beside the
    scoring that produced the values it sums — because two copies of it would be
    free to disagree about which topics count.
    """
    return sum(float(record.scores.get(slug, 0.0)) for slug in record.topics)
