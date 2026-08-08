"""Topic relevance scoring.

Deliberately transparent: a keyword rule you can read and correct beats an
opaque score you cannot argue with. Items below a topic's threshold are still
recorded in the index — the archive keeps a record of what was considered and
rejected, so a threshold can be revisited later without re-collecting.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from ..common.config import Topic

_WORD_BOUNDARY_CACHE: dict[str, re.Pattern] = {}


def _pattern(term: str) -> re.Pattern:
    """Case-insensitive matcher for ``term``.

    Word boundaries keep "ATE" from matching inside "Water"; multi-word terms
    tolerate any run of whitespace or hyphens between words so that "causal
    inference", "causal-inference" and a line-wrapped abstract all match.
    """
    cached = _WORD_BOUNDARY_CACHE.get(term)
    if cached is None:
        parts = [re.escape(p) for p in re.split(r"[\s\-_]+", term.strip()) if p]
        if not parts:
            parts = [re.escape(term.strip())]
        body = r"[\s\-_]+".join(parts)
        cached = re.compile(rf"(?<!\w){body}(?!\w)", re.IGNORECASE)
        _WORD_BOUNDARY_CACHE[term] = cached
    return cached


def _find(term: str, text: str) -> bool:
    return bool(text) and _pattern(term).search(text) is not None


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
