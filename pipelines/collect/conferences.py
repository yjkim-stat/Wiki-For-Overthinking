"""Conference collector.

Top-tier venues have no single API, so this queries four indexes and lets
deduplication merge the overlap:

* Semantic Scholar — broadest coverage, abstracts included, no key required.
* OpenReview — the review-bearing venues, often months before proceedings.
* DBLP — authoritative bibliographic fallback, but no abstracts.
* The venue's own virtual site — authoritative on the accepted programme the
  day it goes up, and the only one of the four that cannot be wrong about
  whether a paper was accepted. Lives in ``virtual_site.py`` because it is
  fetched per venue-year rather than per query.

Every query is best-effort. These are third-party services with shifting
conventions (OpenReview's venue ids in particular change between years), so a
failure here logs and returns nothing rather than aborting the run.
"""

from __future__ import annotations

import os
from datetime import date

from . import anthology, virtual_site
from ..common.config import Config, Topic
from ..common.http import Client, HTTPError, from_settings
from ..common.log import get
from ..common.schema import Paper, canonical_paper_id, utcnow
from ..local import abstracts as local_abstracts

_LOG = get(__name__)


def _quote(term: str) -> str:
    term = term.strip()
    return f'"{term}"' if " " in term else term


def _venues_for(topic: Topic, all_venues: list[dict]) -> list[dict]:
    wanted = topic.source_option("conferences", "venues", None)
    if not wanted:
        return all_venues
    wanted_lower = {str(v).lower() for v in wanted}
    return [v for v in all_venues if str(v.get("name", "")).lower() in wanted_lower]


# ---------------------------------------------------------------------------
# Semantic Scholar
# ---------------------------------------------------------------------------


def _from_semantic_scholar(item: dict) -> Paper | None:
    title = (item.get("title") or "").strip()
    if not title:
        return None

    external = item.get("externalIds") or {}
    arxiv_id = str(external.get("ArXiv") or "")
    doi = str(external.get("DOI") or "")

    authors = [a.get("name", "") for a in (item.get("authors") or []) if a.get("name")]
    published = str(item.get("publicationDate") or "")
    year = int(item.get("year") or 0)
    open_access = item.get("openAccessPdf") or {}

    return Paper(
        id=canonical_paper_id(arxiv_id=arxiv_id, doi=doi, title=title),
        title=title,
        source="semanticscholar",
        source_id=str(item.get("paperId") or ""),
        authors=authors,
        abstract=(item.get("abstract") or "").strip(),
        url=str(item.get("url") or ""),
        pdf_url=str(open_access.get("url") or ""),
        published=published[:10] or (f"{year}-01-01" if year else ""),
        venue=(item.get("venue") or "").strip(),
        year=year,
        doi=doi,
        arxiv_id=arxiv_id,
        first_seen=utcnow(),
        last_seen=utcnow(),
    )


def _collect_semantic_scholar(
    cfg: Config,
    topic: Topic,
    venues: list[dict],
    since: date,
    client: Client,
    errors: list[str] | None = None,
) -> list[Paper]:
    block = (cfg.sources.get("conferences", {}) or {}).get("semantic_scholar", {}) or {}
    if not block.get("enabled", True):
        return []

    terms = [_quote(t) for t in topic.keywords_any if t.strip()]
    if not terms:
        return []
    query = " | ".join(terms)
    for required in topic.keywords_all:
        query = f"({query}) + {_quote(required)}"

    headers = {}
    key_env = block.get("api_key_env", "SEMANTIC_SCHOLAR_API_KEY")
    api_key = os.environ.get(key_env, "")
    if api_key:
        headers["x-api-key"] = api_key

    limit = int(cfg.settings.get("collect", {}).get("max_items_per_source", 60))
    params = {
        "query": query,
        "fields": (
            "paperId,title,abstract,venue,year,authors,externalIds,url,"
            "publicationDate,openAccessPdf"
        ),
        "year": f"{since.year}-",
        "limit": min(limit, 1000),
    }
    # Opt-in, and off by default. Semantic Scholar records a preprint's venue
    # as "arXiv.org", so filtering by a list of conference names excludes every
    # preprint unconditionally — and for a fast-moving field the preprints are
    # not a supplement to the literature, they are the literature. Off is the
    # right default because the failure mode of `false` is noise, which scoring
    # already filters, while the failure mode of `true` is silent absence,
    # which nothing detects.
    venue_names = [v.get("name", "") for v in venues if v.get("name")]
    if venue_names and block.get("restrict_to_venues", False):
        params["venue"] = ",".join(venue_names)

    try:
        data = client.get_json(
            block.get(
                "api_url",
                "https://api.semanticscholar.org/graph/v1/paper/search/bulk",
            ),
            params,
            headers=headers,
        )
    except HTTPError as exc:
        _LOG.error("semantic scholar query failed for '%s': %s", topic.slug, exc)
        if errors is not None:
            errors.append(f"semanticscholar[{topic.slug}]: {exc}")
        return []

    papers = []
    for item in (data.get("data") or [])[:limit]:
        paper = _from_semantic_scholar(item)
        if paper is not None:
            papers.append(paper)
    _LOG.info("semantic scholar: %d papers for topic '%s'", len(papers), topic.slug)
    return papers


# ---------------------------------------------------------------------------
# OpenReview
# ---------------------------------------------------------------------------


def _openreview_value(content: dict, key: str, default=""):
    """api2 wraps every field as ``{"value": ...}``; api1 did not."""
    node = content.get(key)
    if isinstance(node, dict):
        return node.get("value", default)
    return node if node is not None else default


def _from_openreview(note: dict, venue_name: str) -> Paper | None:
    content = note.get("content") or {}
    title = str(_openreview_value(content, "title") or "").strip()
    if not title:
        return None

    authors = _openreview_value(content, "authors", []) or []
    if isinstance(authors, str):
        authors = [authors]

    note_id = str(note.get("id") or "")
    venue = str(_openreview_value(content, "venue") or venue_name)
    pdf = str(_openreview_value(content, "pdf") or "")
    if pdf and pdf.startswith("/"):
        pdf = f"https://openreview.net{pdf}"

    return Paper(
        id=canonical_paper_id(title=title),
        title=title,
        source="openreview",
        source_id=note_id,
        authors=[str(a) for a in authors],
        abstract=str(_openreview_value(content, "abstract") or "").strip(),
        url=f"https://openreview.net/forum?id={note_id}" if note_id else "",
        pdf_url=pdf,
        venue=venue,
        first_seen=utcnow(),
        last_seen=utcnow(),
    )


def _collect_openreview(
    cfg: Config,
    topic: Topic,
    venues: list[dict],
    since: date,
    client: Client,
    errors: list[str] | None = None,
) -> list[Paper]:
    block = (cfg.sources.get("conferences", {}) or {}).get("openreview", {}) or {}
    if not block.get("enabled", True):
        return []

    api_url = block.get("api_url", "https://api2.openreview.net/notes")
    limit = int(cfg.settings.get("collect", {}).get("max_items_per_source", 60))
    # Accepted papers for a venue land under the current year's id, but a
    # cycle that has not concluded still lives under the previous one.
    years = sorted({since.year, date.today().year}, reverse=True)

    papers: list[Paper] = []
    attempts = failures = 0
    last_error: Exception | None = None
    for venue in venues:
        prefix = str(venue.get("openreview_prefix") or "").strip()
        if not prefix:
            continue
        for year in years:
            venue_id = f"{prefix}/{year}/Conference"
            attempts += 1
            try:
                data = client.get_json(
                    api_url,
                    {"content.venueid": venue_id, "limit": min(limit, 1000), "offset": 0},
                )
            except HTTPError as exc:
                # A single miss is expected: venue ids change between cycles.
                # Every lookup failing is not, and is reported below.
                _LOG.debug("openreview %s unavailable: %s", venue_id, exc)
                failures += 1
                last_error = exc
                continue

            notes = data.get("notes") or []
            if not notes:
                continue
            for note in notes:
                paper = _from_openreview(note, str(venue.get("name") or venue_id))
                if paper is not None:
                    paper.year = year
                    papers.append(paper)
            _LOG.info("openreview: %d notes from %s", len(notes), venue_id)

    if errors is not None and attempts and failures == attempts:
        errors.append(f"openreview: all {attempts} lookup(s) failed: {last_error}")
    return papers


# ---------------------------------------------------------------------------
# DBLP
# ---------------------------------------------------------------------------


def _from_dblp(info: dict) -> Paper | None:
    title = (info.get("title") or "").strip().rstrip(".")
    if not title:
        return None

    authors_node = (info.get("authors") or {}).get("author") or []
    if isinstance(authors_node, dict):
        authors_node = [authors_node]
    authors = [
        a.get("text", "") if isinstance(a, dict) else str(a) for a in authors_node
    ]

    doi = str(info.get("doi") or "")
    year = int(info.get("year") or 0)

    return Paper(
        id=canonical_paper_id(doi=doi, title=title),
        title=title,
        source="dblp",
        source_id=str(info.get("key") or ""),
        authors=[a for a in authors if a],
        url=str(info.get("ee") or info.get("url") or ""),
        venue=str(info.get("venue") or ""),
        year=year,
        published=f"{year}-01-01" if year else "",
        doi=doi,
        first_seen=utcnow(),
        last_seen=utcnow(),
    )


def _collect_dblp(
    cfg: Config,
    topic: Topic,
    venues: list[dict],
    since: date,
    client: Client,
    errors: list[str] | None = None,
) -> list[Paper]:
    block = (cfg.sources.get("conferences", {}) or {}).get("dblp", {}) or {}
    if not block.get("enabled", True):
        return []

    api_url = block.get("api_url", "https://dblp.org/search/publ/api")
    limit = int(cfg.settings.get("collect", {}).get("max_items_per_source", 60))
    # DBLP matches on title words only, so a phrase keyword is used as-is and
    # each venue is queried separately.
    terms = [t.strip() for t in topic.keywords_any if t.strip()][:4]

    papers: list[Paper] = []
    attempts = failures = 0
    last_error: Exception | None = None
    for venue in venues:
        dblp_key = str(venue.get("dblp_key") or "").strip()
        if not dblp_key:
            continue
        for term in terms:
            query = f"{term} venue:{dblp_key}: year:{since.year}:"
            attempts += 1
            try:
                data = client.get_json(
                    api_url, {"q": query, "format": "json", "h": min(limit, 100)}
                )
            except HTTPError as exc:
                _LOG.debug("dblp query '%s' failed: %s", query, exc)
                failures += 1
                last_error = exc
                continue

            hits = ((data.get("result") or {}).get("hits") or {}).get("hit") or []
            for hit in hits:
                paper = _from_dblp(hit.get("info") or {})
                if paper is not None:
                    papers.append(paper)

    if papers:
        _LOG.info("dblp: %d hits for topic '%s'", len(papers), topic.slug)
    if errors is not None and attempts and failures == attempts:
        errors.append(f"dblp: all {attempts} query(s) failed: {last_error}")
    return papers


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def collect(
    cfg: Config,
    topics: list[Topic],
    since: date,
    client: Client | None = None,
    errors: list[str] | None = None,
) -> list[Paper]:
    """Fetch conference papers matching ``topics``, published since ``since``."""
    block = cfg.sources.get("conferences", {}) or {}
    if not block.get("enabled", True):
        _LOG.info("conference collector disabled in config/sources.yaml")
        return []

    all_venues = list(block.get("venues") or [])
    client = client or from_settings(cfg.settings, min_interval_s=1.0)

    collected: dict[str, Paper] = {}
    for topic in topics:
        if not topic.source_enabled("conferences"):
            continue
        venues = _venues_for(topic, all_venues)
        for gather in (
            _collect_semantic_scholar,
            _collect_openreview,
            _collect_dblp,
        ):
            try:
                found = gather(cfg, topic, venues, since, client, errors)
            except Exception as exc:  # noqa: BLE001 - one index must not sink the run
                _LOG.exception(
                    "%s raised for topic '%s'", gather.__name__, topic.slug
                )
                if errors is not None:
                    errors.append(f"{gather.__name__}[{topic.slug}]: {exc}")
                continue
            for paper in found:
                collected.setdefault(paper.id, paper)

    # The virtual sites are fetched once for all topics rather than once per
    # topic: a programme page is the same page whoever is asking, and with
    # several topics tracked the per-topic loop would re-fetch it every time.
    # The venue list is the union of what the topics ask for, so narrowing by
    # one topic never hides a venue from another.
    wanted: list[dict] = []
    for topic in topics:
        if not topic.source_enabled("conferences"):
            continue
        for venue in _venues_for(topic, all_venues):
            if venue not in wanted:
                wanted.append(venue)
    if wanted:
        try:
            found = virtual_site.collect(cfg, topics, wanted, since, client, errors)
        except Exception as exc:  # noqa: BLE001 - one index must not sink the run
            _LOG.exception("virtual site collector raised")
            if errors is not None:
                errors.append(f"virtual_site: {exc}")
        else:
            # Last, so a record that already carries an abstract from one of
            # the indexes above keeps it.
            for paper in found:
                collected.setdefault(paper.id, paper)

        # The Anthology, on the same once-for-all-topics footing and for the
        # same reason. It runs after the programme pages because its entries
        # carry abstracts: `setdefault` keeps whichever record arrived first,
        # and arriving late with a fuller record would waste it. Anything the
        # earlier indexes already have keeps what it has; anything they missed
        # arrives here complete.
        try:
            found = anthology.collect(cfg, topics, wanted, since, client, errors)
        except Exception as exc:  # noqa: BLE001 - one index must not sink the run
            _LOG.exception("anthology collector raised")
            if errors is not None:
                errors.append(f"anthology: {exc}")
        else:
            for paper in found:
                collected.setdefault(paper.id, paper)

    papers = list(collected.values())
    # fill in abstracts the indexes did not carry, after deduplication so
    # a paper two indexes returned is not fetched for a field it already has.
    # See pipelines/local/abstracts.py.
    try:
        local_abstracts.fill_missing(cfg, papers, client, errors)
    except Exception as exc:  # noqa: BLE001 - enrichment must not sink collection
        _LOG.exception("filling in missing abstracts failed")
        if errors is not None:
            errors.append(f"abstracts: {exc}")

    return papers
