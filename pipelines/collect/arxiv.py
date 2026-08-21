"""arXiv collector.

Queries the public Atom API, one request per topic (split into several when a
topic has many keywords, since the query string is not unbounded). Results are
restricted server-side by submission date so a daily run stays small.

Note that the date filter is on *submission*, not revision: a v2 of an older
paper will not resurface. That is deliberate — the archive tracks new work, and
revisions of already-archived papers are picked up by the merge in
``enrich/dedupe.py`` when they appear through another source.
"""

from __future__ import annotations

import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta

from . import arxiv_listing
from ..common.config import Config, Topic
from ..common.http import Client, HTTPError, from_settings
from ..common.log import get
from ..common.schema import Paper, canonical_paper_id, strip_arxiv_version, utcnow

_LOG = get(__name__)

_NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}

# arXiv rejects very long query strings; keep each request to a handful of terms.
_TERMS_PER_QUERY = 8


def _text(node: ET.Element | None, default: str = "") -> str:
    if node is None or node.text is None:
        return default
    return " ".join(node.text.split())


def _quote(term: str) -> str:
    """Quote multi-word terms so arXiv treats them as a phrase."""
    term = term.strip()
    return f'"{term}"' if " " in term else term


def _build_queries(topic: Topic, categories: list[str]) -> list[str]:
    """One arXiv ``search_query`` per chunk of keywords."""
    terms = [_quote(t) for t in topic.keywords_any if t.strip()]
    if not terms:
        return []

    category_clause = ""
    if categories:
        category_clause = "(" + " OR ".join(f"cat:{c}" for c in categories) + ")"

    required = [_quote(t) for t in topic.keywords_all if t.strip()]
    required_clause = "".join(f" AND all:{t}" for t in required)

    queries = []
    for start in range(0, len(terms), _TERMS_PER_QUERY):
        chunk = terms[start : start + _TERMS_PER_QUERY]
        any_clause = "(" + " OR ".join(f"all:{t}" for t in chunk) + ")"
        parts = [p for p in (category_clause, any_clause) if p]
        queries.append(" AND ".join(parts) + required_clause)
    return queries


def _date_clause(since: date, until: date) -> str:
    return (
        f"submittedDate:[{since.strftime('%Y%m%d')}0000 TO "
        f"{until.strftime('%Y%m%d')}2359]"
    )


def _parse_entry(entry: ET.Element) -> Paper | None:
    raw_id = _text(entry.find("atom:id", _NS))
    if not raw_id:
        return None
    arxiv_id = raw_id.rsplit("/abs/", 1)[-1] if "/abs/" in raw_id else raw_id
    bare_id = strip_arxiv_version(arxiv_id)

    title = _text(entry.find("atom:title", _NS))
    if not title:
        return None

    authors = [
        _text(node.find("atom:name", _NS))
        for node in entry.findall("atom:author", _NS)
    ]
    categories = [
        node.attrib["term"]
        for node in entry.findall("atom:category", _NS)
        if "term" in node.attrib
    ]

    pdf_url = ""
    for link in entry.findall("atom:link", _NS):
        if link.attrib.get("title") == "pdf" or link.attrib.get("type") == "application/pdf":
            pdf_url = link.attrib.get("href", "")
            break

    published = _text(entry.find("atom:published", _NS))
    updated = _text(entry.find("atom:updated", _NS))
    doi = _text(entry.find("arxiv:doi", _NS))
    journal_ref = _text(entry.find("arxiv:journal_ref", _NS))

    return Paper(
        id=canonical_paper_id(arxiv_id=bare_id),
        title=title,
        source="arxiv",
        source_id=arxiv_id,
        authors=[a for a in authors if a],
        abstract=_text(entry.find("atom:summary", _NS)),
        url=f"https://arxiv.org/abs/{bare_id}",
        pdf_url=pdf_url or f"https://arxiv.org/pdf/{bare_id}",
        published=published[:10],
        updated=updated[:10],
        venue=journal_ref,
        year=int(published[:4]) if published[:4].isdigit() else 0,
        categories=categories,
        doi=doi,
        arxiv_id=bare_id,
        first_seen=utcnow(),
        last_seen=utcnow(),
    )


def collect(
    cfg: Config,
    topics: list[Topic],
    since: date,
    until: date | None = None,
    client: Client | None = None,
    errors: list[str] | None = None,
) -> list[Paper]:
    """Fetch arXiv submissions matching ``topics`` in the date window.

    Failures are appended to ``errors`` as well as logged: a source that is
    blocked or down returns an empty list, and without this the run would
    report a quiet day rather than a broken one.
    """
    block = cfg.sources.get("arxiv", {}) or {}
    if not block.get("enabled", True):
        _LOG.info("arxiv collector disabled in config/sources.yaml")
        return []

    # Remembered before the default is filled in: when a caller injects a
    # client it is standing in for the network, so the fallback must use it
    # too. Left to itself the listing builds its own, because it talks to a
    # different host and is held to a slower interval than the API.
    injected = client
    until = until or date.today() + timedelta(days=1)
    api_url = block.get("api_url", "https://export.arxiv.org/api/query")
    default_categories = list(block.get("categories") or [])
    max_results = int(cfg.settings.get("collect", {}).get("max_items_per_source", 60))

    client = client or from_settings(
        cfg.settings,
        min_interval_s=float(block.get("min_request_interval_s", 3.0)),
    )

    collected: dict[str, Paper] = {}
    # topics the API answered with nothing. Tracked per topic rather than
    # in aggregate because that is the unit the fallback can actually act on:
    # the listing is read per category and filtered by the topics it is given.
    barren: list[Topic] = []
    for topic in topics:
        if not topic.source_enabled("arxiv"):
            continue
        categories = topic.source_option("arxiv", "categories", default_categories)
        queries = _build_queries(topic, list(categories or []))
        if not queries:
            _LOG.warning("topic '%s' produced no arXiv query", topic.slug)
            continue

        # whether *this topic's* queries returned anything, not whether
        # the shared dict grew: topics overlap, so a topic whose every result was
        # already contributed by an earlier one has still been answered by the
        # API and must not be sent to the fallback.
        answered = False
        for query in queries:
            search_query = f"{query} AND {_date_clause(since, until)}"
            try:
                root = client.get_xml(
                    api_url,
                    {
                        "search_query": search_query,
                        "start": 0,
                        "max_results": max_results,
                        "sortBy": "submittedDate",
                        "sortOrder": "descending",
                    },
                )
            except HTTPError as exc:
                _LOG.error("arxiv query failed for topic '%s': %s", topic.slug, exc)
                if errors is not None:
                    errors.append(f"arxiv[{topic.slug}]: {exc}")
                continue

            entries = root.findall("atom:entry", _NS)
            _LOG.info(
                "arxiv: %d entries for topic '%s'", len(entries), topic.slug
            )
            for entry in entries:
                paper = _parse_entry(entry)
                if paper is not None:
                    answered = True
                    collected.setdefault(paper.id, paper)

        if not answered:
            barren.append(topic)

    # The website is a different host from the API, and a host blocked from one
    # is not always blocked from the other. `auto` reaches for the listing only
    # where the API produced nothing, because the listing cannot search abstracts
    # and so sees strictly less.
    # "where", not "when" — the gate is per topic. Gating on the whole run
    # meant one topic returning a single paper suppressed the fallback for every
    # other topic, so the topics that most needed it — the ones the API answered
    # with nothing — were exactly the ones that never got it. That is not a rare
    # case: with five topics sharing four categories, some topic almost always
    # matches something, and the fallback had never fired in a scheduled run.
    mode = str((block.get("listing", {}) or {}).get("mode", "auto")).lower()
    targets = topics if mode == "always" else (barren if mode == "auto" else [])
    if targets:
        if mode == "auto":
            _LOG.info(
                "arxiv API returned nothing for %d topic(s) (%s); falling back to "
                "the listing pages",
                len(targets),
                ", ".join(t.slug for t in targets),
            )
        try:
            found = arxiv_listing.collect(
                cfg, targets, since, client=injected, errors=errors
            )
        except Exception as exc:  # noqa: BLE001 - a fallback must not sink the run
            _LOG.exception("arxiv listing collection failed")
            if errors is not None:
                errors.append(f"arxiv_listing: {exc}")
        else:
            for paper in found:
                collected.setdefault(paper.id, paper)

    return list(collected.values())


def fetch_by_id(
    cfg: Config,
    arxiv_ids: list[str],
    client: Client | None = None,
    errors: list[str] | None = None,
    source: str = "seed",
) -> list[Paper]:
    """Fetch specific arXiv papers by id.

    Used wherever something already knows which paper it wants and needs the
    bibliography: a topic's seed papers, and a curated list that gives a link
    and a nickname. ``source`` is what the resulting records are attributed to,
    since how a paper came to our attention is not the same fact as which
    endpoint answered for it.
    """
    block = cfg.sources.get("arxiv", {}) or {}
    api_url = block.get("api_url", "https://export.arxiv.org/api/query")
    client = client or from_settings(
        cfg.settings,
        min_interval_s=float(block.get("min_request_interval_s", 3.0)),
    )

    ids = [strip_arxiv_version(i) for i in arxiv_ids if i.strip()]
    if not ids:
        return []

    papers: list[Paper] = []
    for start in range(0, len(ids), 25):
        chunk = ids[start : start + 25]
        try:
            root = client.get_xml(
                api_url, {"id_list": ",".join(chunk), "max_results": len(chunk)}
            )
        except HTTPError as exc:
            _LOG.error("arxiv id lookup failed: %s", exc)
            if errors is not None:
                errors.append(f"arxiv[{source}]: {exc}")
            continue
        for entry in root.findall("atom:entry", _NS):
            paper = _parse_entry(entry)
            if paper is not None:
                paper.source = source
                papers.append(paper)
    return papers


def parse_since(days: int) -> date:
    """Start of the collection window, ``days`` before today."""
    return (datetime.now() - timedelta(days=max(1, days))).date()
