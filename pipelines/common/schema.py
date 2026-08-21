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

    id: str  # canonical: "arxiv:2401.12345" | "doi:10.../x" | "title:<fp>" | "local:<fp>"
    title: str
    source: str  # arxiv | openreview | semanticscholar | dblp | virtualsite | seed | local
    source_id: str = ""
    authors: list[str] = field(default_factory=list)
    abstract: str = ""
    url: str = ""
    pdf_url: str = ""
    # Repository-relative path to a PDF held on disk. Set only by the local
    # collector; a remote paper is referenced by `pdf_url` and never copied.
    local_path: str = ""
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

    @property
    def is_local(self) -> bool:
        """True when this paper was filed by hand from the inbox.

        Membership, not equality: deduplication joins the sources a record has
        been seen from with ``+``, so a paper that arrived both by hand and
        from arXiv reads as ``local+arxiv`` and is still local.
        """
        return "local" in (self.source or "").split("+")

    def citation(self) -> str:
        """Short human-readable reference line."""
        who = ", ".join(self.authors[:3])
        if len(self.authors) > 3:
            who += " et al."
        # "arXiv" is only a sensible fallback for something that came from
        # arXiv. A hand-filed PDF with no venue yet says nothing rather than
        # claiming a venue it never had.
        fallback = "arXiv" if (self.arxiv_id or "arxiv" in self.source) else ""
        where = self.venue or (self.categories[0] if self.categories else fallback)
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
    models: list[str] = field(default_factory=list)  # LOCAL
    tags: list[str] = field(default_factory=list)
    # What this reading was based on: ``document`` when the reader opened the
    # PDF attached to the task, ``abstract`` when they worked from the payload
    # alone. Which one it was decides what the record is worth -- an abstract
    # reports a paper's claims and rarely the condition under which they fail.
    # Empty means unknown, which is not the same as ``abstract``: a reading
    # written before this field existed had a document as often as not, and
    # defaulting one to the other would make them indistinguishable for ever.
    read_from: str = ""
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
    models: list[str] = field(default_factory=list)  # LOCAL
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
    # Slugs, derived: two names that appeared in one summary's lists. Rebuilt
    # from scratch every harvest, so re-reading a paper drops the edges it made.
    related: list[str] = field(default_factory=list)
    # Slugs somebody ruled on when they wrote the definition. Carried across a
    # rebuild the way `definition` and `aliases` are, because a person's link is
    # not evidence of anything and cannot be re-derived from the summaries.
    # Kept apart from `related` rather than merged into it so that each list
    # keeps the property it needs: derived edges stay disposable, authored ones
    # survive. Merging would make a re-read paper's edge permanent.
    related_authored: list[str] = field(default_factory=list)
    topics: list[str] = field(default_factory=list)
    first_seen: str = field(default_factory=utcnow)
    last_seen: str = field(default_factory=utcnow)
    schema_version: int = SCHEMA_VERSION

    @property
    def mention_count(self) -> int:
        return len({(e.get("kind"), e.get("id")) for e in self.evidence})

    @property
    def neighbours(self) -> set[str]:
        """Every entity this one links to, however the link got there.

        A union rather than a precedence: the two lists answer different
        questions — what turned up alongside this, and what somebody said to
        read next — and a note is worth more for carrying both. Self-links are
        dropped; co-occurrence cannot produce one, but an authored answer can.
        """
        return {
            slug
            for slug in (*self.related, *self.related_authored)
            if slug and slug != self.slug
        }


@dataclass
class Finding(_Record):
    """Something the group settled, rather than something a paper said.

    Every other record here arrives from a collector. This one arrives from a
    conversation — a decision taken, or a judgement reached across several
    sources — and it is the only record whose author is the group itself.

    ``supersedes`` is what keeps that honest. A group's decisions change, and a
    log that only ever appends becomes a pile in which the current answer
    cannot be found. A new finding may retire an older one; the older one stays
    on disk, marked, because why the group used to think otherwise is part of
    what a newcomer needs.
    """

    id: str  # "finding:<fingerprint>"
    kind: str  # decision | fact
    statement: str
    rationale: str = ""
    # Names, not slugs, for the same reason summaries carry names: the wiki
    # slugifies on the way in, so a finding can name an entity the wiki has not
    # harvested yet without inventing a link that resolves to nothing.
    concepts: list[str] = field(default_factory=list)
    papers: list[str] = field(default_factory=list)  # canonical paper ids
    # Ids of `Reference` records: things checked outside the archive. Kept apart
    # from `papers` because they are apart in kind — a paper is evidence the
    # archive collected and can re-read, a reference is a page somebody looked
    # at once. Nothing derived from this list ever reaches entity promotion.
    references: list[str] = field(default_factory=list)
    topics: list[str] = field(default_factory=list)
    supersedes: str = ""
    superseded_by: str = ""
    established_at: str = field(default_factory=utcnow)
    # How much evidence existed on this subject when the finding was recorded:
    # the distinct sources behind the entities it names. The direct analogue of
    # a definition's `source_count`, and it exists for the same reason — a
    # judgement reached across three papers reads with the same confidence at
    # thirty, and nothing could say which it was.
    # 0 means unknown, which is what a finding recorded before this field says.
    # Not "none": a finding is not recorded against nothing.
    established_against: int = 0
    schema_version: int = SCHEMA_VERSION

    @property
    def live(self) -> bool:
        return not self.superseded_by


@dataclass
class Reference(_Record):
    """Something checked outside the archive, cited by a finding.

    The archive can answer a great deal about itself and nothing at all about
    what is not in it. A published implementation, a model card, a proceedings
    page: a session that consults one of these and records what it learned
    leaves the fact inside a finding's prose, where the next person can neither
    verify it nor find it again without repeating the search.

    This is where that citation goes, and the fields are chosen so it is a
    citation rather than a rumour:

    ``retrieved_at`` because the web changes, and a claim about a page with no
    date attached cannot be checked against anything. ``quoted`` because a URL
    alone says a page was visited, not what it was found to say — and a page
    that has since moved leaves the quotation as the only surviving evidence.

    **A reference is not evidence for an entity.** `Concept.evidence` counts
    papers and talks the archive has read, and that count is what promotes an
    entity to a note of its own. Two blog posts must never promote anything: if
    they could, nothing could later say what the wiki grew from, and that damage
    cannot be undone by deleting the posts. Nothing in `enrich/concepts.py`
    reads this record, and `tests/test_references.py` asserts it stays that way.
    """

    id: str  # "web:<fingerprint of the normalized url>"
    url: str
    title: str = ""
    publisher: str = ""  # a domain, or whoever published it
    kind: str = "other"
    retrieved_at: str = ""
    # The passage actually relied on. Not the page — the part of it that was
    # used as evidence, which is the part worth being able to check.
    quoted: str = ""
    # Optional path to a local copy. Nothing writes one today; the field exists
    # so that a deployment which starts taking snapshots has somewhere to say so
    # without a schema change.
    snapshot: str = ""
    first_seen: str = field(default_factory=utcnow)
    schema_version: int = SCHEMA_VERSION


def finding_id(statement: str) -> str:
    """Content-addressed, so recording the same sentence twice is one finding."""
    return f"finding:{title_fingerprint(statement)}"


def normalize_url(url: str) -> str:
    """The form two spellings of one page agree on.

    Deliberately timid, because the two failure directions are not symmetric.
    Under-normalising leaves two records for one page: visible, and fixed by
    citing the other one. Over-normalising fuses two pages into one record, and
    the result is a citation pointing at something the reader never read — the
    same shape of damage as a wrong alias, which this repository already treats
    as the expensive kind because a fused record looks perfectly healthy.

    So: case is folded on the scheme and the host, where it is not significant;
    a default port is dropped; a fragment is dropped, because it selects a place
    within a document rather than a document; and one trailing slash goes. The
    query string is left exactly alone — for a great many sites it is what
    chooses the page.
    """
    from urllib.parse import urlsplit, urlunsplit

    parts = urlsplit((url or "").strip())
    host = parts.hostname or ""
    if parts.port and not (
        (parts.scheme == "http" and parts.port == 80)
        or (parts.scheme == "https" and parts.port == 443)
    ):
        host = f"{host}:{parts.port}"

    path = parts.path
    if len(path) > 1 and path.endswith("/"):
        path = path[:-1]

    return urlunsplit((parts.scheme.lower(), host, path, parts.query, ""))


def reference_id(url: str) -> str:
    """Content-addressed, so the same page cited twice is one record."""
    digest = hashlib.sha1(normalize_url(url).encode("utf-8")).hexdigest()[:16]
    return f"web:{digest}"


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
