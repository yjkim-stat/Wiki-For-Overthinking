"""Repositories that may be worth citing — collected as candidates, never as papers.

GitHub is not a source of literature and this collector does not pretend it is.
A repository cannot enter `data/papers/`, and nothing it produces is ever
evidence for a wiki entity: `Concept.evidence` counts papers and talks the
archive has *read*, and that count is what promotes an entity to a note of its
own. If a repository could contribute to it, nothing afterwards could say what
the wiki grew from, and deleting the repository would not undo it.

What a repository can be is a **reference** — "a published implementation" is
the first example `CLAUDE.md` gives — cited by a finding, with the date it was
read and the passage relied on.

**So why not write references directly?** Because of what the two required
fields mean. `retrieved_at` records that somebody went and looked; `quoted`
records the passage they *relied on*. A collector filling `quoted` with a
scraped repository description writes a citation nobody made: the field would
hold a blurb rather than evidence, and the record type would quietly stop being
a citation. The friction in those two fields is deliberate, and a daily job that
routes around it is worse than no daily job.

Hence a lane, in the shape this archive already uses twice — `inbox/` for a PDF
somebody filed, `requests/` for a change somebody asked for. Collection fills
`candidates/pending/`; a session reads one and decides. Only
`candidates promote` writes a reference, and it demands the quotation, because
that is the step where somebody actually relied on something.

A candidate is not a record. It lives at the deployment root beside the other
two lanes and never under `data/`, which is the source of truth and holds only
what arrived from a collector or was derived from it.
"""

from __future__ import annotations

import json
import urllib.parse
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Any

from ..common.config import Config, Topic
from ..common.http import Client, from_settings
from ..common.log import get
from ..common.schema import normalize_url, reference_id, utcnow
from ..enrich.score import score_against_topics

_LOG = get(__name__)

SEARCH_URL = "https://api.github.com/search/repositories"

#: Anonymous search is 10 requests/minute. One query per topic per run sits well
#: inside that, and the collector gives up rather than sleeping — a daily job
#: that blocks on a rate limit is a daily job that does not finish.
_ACCEPT = "application/vnd.github+json"


@dataclass
class Candidate:
    """One repository, scored, waiting for somebody to decide about it."""

    id: str
    url: str
    full_name: str
    description: str = ""
    homepage: str = ""
    stars: int = 0
    pushed_at: str = ""
    language: str = ""
    license: str = ""
    topics: list[str] = field(default_factory=list)
    scores: dict[str, float] = field(default_factory=dict)
    matched: list[str] = field(default_factory=list)
    accepted_topics: list[str] = field(default_factory=list)
    found_at: str = field(default_factory=utcnow)
    query: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Candidate":
        known = {f for f in cls.__dataclass_fields__}
        return cls(**{k: v for k, v in data.items() if k in known})


def _settings(cfg: Config) -> dict:
    return (cfg.sources.get("github") or {}) if isinstance(cfg.sources, dict) else {}


def enabled(cfg: Config) -> bool:
    return bool(_settings(cfg).get("enabled", False))


def _query(topic: Topic, pushed_since: str) -> str:
    """One query per topic, from the topic's own keywords.

    `keywords_any` is what the topic is about; the first few of them are enough
    to make a query that GitHub's relevance ranking can work with, and the
    archive's own scorer decides what survives. Sending every keyword produces a
    query GitHub answers with nothing.
    """
    terms = [t for t in topic.keywords_any[:4] if t]
    if not terms:
        terms = [topic.name]
    phrase = " ".join(f'"{t}"' if " " in t else t for t in terms)
    return f"{phrase} in:name,description,readme pushed:>{pushed_since}"


def _to_candidate(item: dict, topics: list[Topic], settings: dict, query: str) -> Candidate | None:
    url = normalize_url(str(item.get("html_url") or "").strip())
    if not url:
        return None
    description = str(item.get("description") or "")
    # The README is not fetched. Scoring the name and description is enough to
    # reject the bulk, and fetching a README per hit would spend the core rate
    # limit on items most of which are about to be dropped.
    scores, matched, accepted = score_against_topics(
        topics,
        title=str(item.get("full_name") or ""),
        body=" ".join([description] + [str(t) for t in (item.get("topics") or [])]),
        settings=settings,
    )
    if not accepted:
        return None
    licence = item.get("license") or {}
    return Candidate(
        id=reference_id(url),
        url=url,
        full_name=str(item.get("full_name") or ""),
        description=description,
        homepage=str(item.get("homepage") or ""),
        stars=int(item.get("stargazers_count") or 0),
        pushed_at=str(item.get("pushed_at") or ""),
        language=str(item.get("language") or ""),
        license=str(licence.get("spdx_id") or "") if isinstance(licence, dict) else "",
        topics=[str(t) for t in (item.get("topics") or [])],
        scores=scores,
        matched=matched,
        accepted_topics=accepted,
        query=query,
    )


def collect(
    cfg: Config,
    topics: list[Topic] | None = None,
    *,
    client: Client | None = None,
) -> list[Candidate]:
    """Search GitHub once per topic and return the candidates worth filing.

    Nothing is written here. `pipelines.candidates.file_new` decides what is
    new, so that a candidate somebody has already dropped is never offered
    again — the decision is the record, not the repository.
    """
    settings = _settings(cfg)
    if not settings.get("enabled", False):
        _LOG.debug("github: disabled in config/sources.yaml")
        return []

    topics = [t for t in (topics or cfg.topics) if t.source_enabled("github")]
    if not topics:
        return []

    days = int(settings.get("pushed_within_days", 30))
    since = (datetime.now(timezone.utc) - timedelta(days=days)).date().isoformat()
    min_stars = int(settings.get("min_stars", 0))
    per_topic = int(settings.get("per_topic_results", 15))

    client = client or from_settings(cfg.settings, min_interval_s=float(settings.get("min_interval_s", 6.0)))

    found: dict[str, Candidate] = {}
    for topic in topics:
        query = _query(topic, since)
        params = {"q": query, "sort": "stars", "order": "desc", "per_page": per_topic}
        url = f"{SEARCH_URL}?{urllib.parse.urlencode(params)}"
        try:
            data = client.get_json(url, headers={"Accept": _ACCEPT})
        except Exception as exc:  # a source that is unreachable is skipped, not fatal
            _LOG.warning("github: %s unreachable (%s)", topic.slug, exc)
            continue
        if not isinstance(data, dict):
            continue
        items = data.get("items") or []
        _LOG.info("github: %s returned %d repo(s) for %s", topic.slug, len(items), topic.slug)
        for item in items:
            if int(item.get("stargazers_count") or 0) < min_stars:
                continue
            if item.get("archived") or item.get("fork"):
                continue
            candidate = _to_candidate(item, topics, cfg.settings, query)
            if candidate is None:
                continue
            # One repository can answer two topics; keep the first, whose
            # `accepted_topics` already lists every topic it cleared.
            found.setdefault(candidate.id, candidate)

    cap = int(settings.get("max_candidates_per_run", 20))
    ranked = sorted(found.values(), key=lambda c: (-max(c.scores.values(), default=0.0), -c.stars))
    if cap and len(ranked) > cap:
        _LOG.info("github: %d candidate(s) over the cap of %d, keeping the best", len(ranked), cap)
        ranked = ranked[:cap]
    return ranked
