"""Normalized records.

Everything a collector produces is converted into one of these before it is
stored, so downstream stages never care which source an item came from.
Records are intentionally flat: fields are primitives, lists of primitives, or
lists of small plain dicts. That keeps JSON round-tripping trivial and makes
the stored files readable in a diff.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field, fields
from datetime import datetime, timezone
from typing import Any

SCHEMA_VERSION = 1

_WS = re.compile(r"\s+")
_NON_ALNUM = re.compile(r"[^a-z0-9 ]+")
_ARXIV_VERSION = re.compile(r"v\d+$")


def utcnow() -> str:
    """Current UTC time as an ISO-8601 string with a ``Z`` suffix."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def normalize_title(title: str) -> str:
    """Aggressively normalized title, used for cross-source deduplication."""
    lowered = _NON_ALNUM.sub(" ", (title or "").lower())
    return _WS.sub(" ", lowered).strip()


def title_fingerprint(title: str) -> str:
    return hashlib.sha1(normalize_title(title).encode("utf-8")).hexdigest()[:16]


def strip_arxiv_version(arxiv_id: str) -> str:
    """``2401.12345v3`` -> ``2401.12345``. Versions are revisions, not new papers."""
    return _ARXIV_VERSION.sub("", (arxiv_id or "").strip())


class _Record:
    """Mixin giving dataclasses symmetric dict conversion."""

    def to_dict(self) -> dict[str, Any]:
        return {f.name: getattr(self, f.name) for f in fields(self)}

    @classmethod
    def from_dict(cls, data: dict[str, Any]):
        known = {f.name for f in fields(cls)}
        return cls(**{k: v for k, v in data.items() if k in known})


@dataclass
class Paper(_Record):
    """A paper, normalized across arXiv, OpenReview, Semantic Scholar and DBLP."""

    id: str  # canonical: "arxiv:2401.12345" | "doi:10.../x" | "title:<fp>"
    title: str
    source: str  # arxiv | openreview | semanticscholar | dblp | seed
    source_id: str = ""
    authors: list[str] = field(default_factory=list)
    abstract: str = ""
    url: str = ""
    pdf_url: str = ""
    published: str = ""  # ISO date, best effort
    updated: str = ""
    venue: str = ""
    year: int = 0
    categories: list[str] = field(default_factory=list)
    doi: str = ""
    arxiv_id: str = ""
    # Populated by enrich/score.py
    topics: list[str] = field(default_factory=list)
    scores: dict[str, float] = field(default_factory=dict)
    matched_keywords: list[str] = field(default_factory=list)
    # Bookkeeping
    schema_version: int = SCHEMA_VERSION
    first_seen: str = field(default_factory=utcnow)
    last_seen: str = field(default_factory=utcnow)

    @property
    def best_score(self) -> float:
        return max(self.scores.values(), default=0.0)

    def citation(self) -> str:
        """Short human-readable reference line."""
        who = ", ".join(self.authors[:3])
        if len(self.authors) > 3:
            who += " et al."
        where = self.venue or (self.categories[0] if self.categories else "arXiv")
        when = self.year or (self.published[:4] if self.published else "")
        parts = [p for p in (who, f"*{self.title}*", where, str(when)) if p]
        return ". ".join(parts)


@dataclass
class Video(_Record):
    """A seminar or talk recording."""

    id: str  # canonical: "youtube:<video_id>"
    title: str
    source: str = "youtube"
    source_id: str = ""
    channel: str = ""
    channel_id: str = ""
    url: str = ""
    description: str = ""
    published: str = ""
    duration_s: int = 0
    transcript_available: bool = False
    transcript_chars: int = 0
    topics: list[str] = field(default_factory=list)
    scores: dict[str, float] = field(default_factory=dict)
    matched_keywords: list[str] = field(default_factory=list)
    schema_version: int = SCHEMA_VERSION
    first_seen: str = field(default_factory=utcnow)
    last_seen: str = field(default_factory=utcnow)

    @property
    def best_score(self) -> float:
        return max(self.scores.values(), default=0.0)


@dataclass
class PaperSummary(_Record):
    """Structured reading of a paper. Written by whichever summarizer backend runs."""

    paper_id: str
    one_liner: str = ""
    problem: str = ""
    contributions: list[str] = field(default_factory=list)
    method: str = ""
    results: str = ""
    limitations: str = ""
    # topic slug -> why this paper matters for that topic
    relevance: dict[str, str] = field(default_factory=dict)
    concepts: list[str] = field(default_factory=list)
    methods: list[str] = field(default_factory=list)
    datasets: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    generated_by: str = ""
    generated_at: str = field(default_factory=utcnow)
    schema_version: int = SCHEMA_VERSION


@dataclass
class VideoSummary(_Record):
    """Structured reading of a seminar recording."""

    video_id: str
    one_liner: str = ""
    abstract: str = ""
    # [{"start_s": int, "title": str, "summary": str}]
    chapters: list[dict] = field(default_factory=list)
    key_points: list[str] = field(default_factory=list)
    referenced_papers: list[str] = field(default_factory=list)
    concepts: list[str] = field(default_factory=list)
    methods: list[str] = field(default_factory=list)
    datasets: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    generated_by: str = ""
    generated_at: str = field(default_factory=utcnow)
    schema_version: int = SCHEMA_VERSION


@dataclass
class Concept(_Record):
    """A wiki-worthy entity extracted from summaries.

    ``kind`` decides which wiki subdirectory the note lands in.
    """

    slug: str
    name: str
    kind: str = "concept"  # concept | method | dataset | topic
    aliases: list[str] = field(default_factory=list)
    definition: str = ""
    # [{"kind": "paper"|"video", "id": str, "title": str, "note": str}]
    evidence: list[dict] = field(default_factory=list)
    related: list[str] = field(default_factory=list)  # slugs
    topics: list[str] = field(default_factory=list)
    first_seen: str = field(default_factory=utcnow)
    last_seen: str = field(default_factory=utcnow)
    schema_version: int = SCHEMA_VERSION

    @property
    def mention_count(self) -> int:
        return len({(e.get("kind"), e.get("id")) for e in self.evidence})


def canonical_paper_id(
    *, arxiv_id: str = "", doi: str = "", title: str = ""
) -> str:
    """Pick the most stable identifier available.

    arXiv ids win over DOIs because the same work is usually on arXiv first and
    stays there; a title fingerprint is the last resort.
    """
    if arxiv_id:
        return f"arxiv:{strip_arxiv_version(arxiv_id)}"
    if doi:
        return f"doi:{doi.strip().lower()}"
    if title:
        return f"title:{title_fingerprint(title)}"
    raise ValueError("cannot build a paper id without arxiv_id, doi or title")


def canonical_video_id(video_id: str) -> str:
    return f"youtube:{video_id.strip()}"
