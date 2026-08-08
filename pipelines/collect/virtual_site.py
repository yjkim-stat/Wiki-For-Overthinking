"""Conference virtual-site collector.

ICML, NeurIPS and ICLR each publish the accepted programme for a year at
``https://<host>/virtual/<year>/papers.html``. That page is the venue's own
answer to "what was accepted", which is worth having next to the three indexes
in ``conferences.py``: Semantic Scholar lags, OpenReview's venue ids drift
between cycles, and DBLP arrives with the proceedings months later. The virtual
site is authoritative on the day the programme goes up.

Two things shape the design.

*The listing is per year, not per query.* There is no search endpoint — the page
is the whole programme. So a run fetches one page per venue-year and filters
locally, and the same page is never fetched twice in a run no matter how many
topics are tracked.

*The listing carries titles only.* Abstracts and authors live on each paper's
own page. Fetching all of them would be thousands of requests per venue, so a
title is scored first and only the papers that match something a topic tracks
cost a second request. Because adding text can only ever add keyword matches, a
title-only score is a lower bound on the final one: nothing that would have
cleared a threshold is dropped by the gate. What the gate cannot see is a paper
whose keywords appear only in its abstract — that one is left to the other three
indexes, which do search abstracts.

The parsers below are written against the URL shape rather than the markup,
because ``/virtual/<year>/poster/<id>`` has outlived several redesigns of the
page around it. A structural change still shows up: a page that fetches but
yields nothing is logged as a warning rather than passed off as an empty
programme.
"""

from __future__ import annotations

import html as html_mod
import json
import re
from dataclasses import dataclass, field
from datetime import date

from ..common.config import Config, Topic
from ..common.http import Client, HTTPError
from ..common.log import get
from ..common.schema import Paper, canonical_paper_id, utcnow
from ..enrich.score import score_against_topics

_LOG = get(__name__)

# The presentation kinds a paper can appear under. Anything else on the page
# (sessions, workshops, socials) is programme furniture, not a paper.
_PAPER_KINDS = ("poster", "oral", "spotlight", "paper")

_ENTRY_RE = re.compile(
    r"href=[\"'](?P<href>/virtual/(?P<year>\d{4})/"
    r"(?P<kind>" + "|".join(_PAPER_KINDS) + r")/(?P<site_id>\d+))[\"']"
    r"(?P<attrs>[^>]*)>(?P<label>.*?)</a>",
    re.IGNORECASE | re.DOTALL,
)

_TAG_RE = re.compile(r"<[^>]+>")
_META_RE = re.compile(r"<meta\b(?P<attrs>[^>]*)>", re.IGNORECASE)
_ATTR_RE = re.compile(
    r"(?P<key>[a-zA-Z_:][-\w:.]*)\s*=\s*(\"(?P<dq>[^\"]*)\"|'(?P<sq>[^']*)')"
)


def _text(fragment: str) -> str:
    """Anchor labels wrap the title in whatever markup the theme uses."""
    return " ".join(html_mod.unescape(_TAG_RE.sub(" ", fragment)).split())


def _attrs(blob: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for match in _ATTR_RE.finditer(blob):
        value = match.group("dq")
        if value is None:
            value = match.group("sq") or ""
        out[match.group("key").lower()] = html_mod.unescape(value)
    return out


@dataclass
class Listing:
    """One paper as the programme page lists it: a title and a link."""

    title: str
    url: str
    site_id: str
    kind: str = ""
    year: int = 0
    venue: str = ""
    authors: list[str] = field(default_factory=list)
    abstract: str = ""


# ---------------------------------------------------------------------------
# Listing page
# ---------------------------------------------------------------------------


def _parse_embedded_json(page: str, base: str) -> list[Listing]:
    """Some builds ship the programme as a JSON blob inside a script tag.

    Matched structurally — an array of objects carrying a title and an id —
    rather than by variable name, which is theme-specific and changes.
    """
    found: list[Listing] = []
    for blob in re.findall(r"\[\s*\{.*?\}\s*\]", page, re.DOTALL):
        try:
            rows = json.loads(blob)
        except (json.JSONDecodeError, ValueError):
            continue
        if not isinstance(rows, list):
            continue
        for row in rows:
            if not isinstance(row, dict):
                continue
            title = str(row.get("name") or row.get("title") or "").strip()
            site_id = str(row.get("id") or row.get("paper_id") or "").strip()
            if not title or not site_id:
                continue
            authors = row.get("authors") or row.get("speakers") or []
            if isinstance(authors, str):
                authors = [a.strip() for a in authors.split(";") if a.strip()]
            found.append(
                Listing(
                    title=title,
                    url=f"{base}/virtual/paper/{site_id}",
                    site_id=site_id,
                    kind=str(row.get("eventtype") or row.get("type") or "").lower(),
                    abstract=str(row.get("abstract") or "").strip(),
                    authors=[str(a) for a in authors if str(a).strip()],
                )
            )
        if found:
            break
    return found


def _parse_anchors(page: str, base: str) -> list[Listing]:
    """The durable shape: links to ``/virtual/<year>/<kind>/<id>``."""
    found: list[Listing] = []
    for match in _ENTRY_RE.finditer(page):
        title = _text(match.group("label"))
        if not title:
            # An icon-only link to the same paper; the titled one is elsewhere
            # in the page and will be picked up on its own.
            continue
        found.append(
            Listing(
                title=title,
                url=f"{base}{match.group('href')}",
                site_id=match.group("site_id"),
                kind=match.group("kind").lower(),
                year=int(match.group("year")),
            )
        )
    return found


def parse_listing(page: str, base: str) -> list[Listing]:
    """Extract the papers from a programme page.

    Tries the embedded programme data first because it carries authors, and
    falls back to the anchors. Duplicates are collapsed on the site id: a paper
    is routinely linked more than once from the same page.
    """
    entries = _parse_embedded_json(page, base) or _parse_anchors(page, base)
    unique: dict[str, Listing] = {}
    for entry in entries:
        unique.setdefault(entry.site_id or entry.title.lower(), entry)
    return list(unique.values())


# ---------------------------------------------------------------------------
# Paper page
# ---------------------------------------------------------------------------


def parse_detail(page: str) -> tuple[str, list[str]]:
    """Pull ``(abstract, authors)`` off a paper's own page.

    Highwire ``citation_*`` meta tags are read first: they are emitted for
    Google Scholar, which makes them the one part of these pages under outside
    pressure to stay put.
    """
    abstract = ""
    authors: list[str] = []

    for match in _META_RE.finditer(page):
        attrs = _attrs(match.group("attrs"))
        name = (attrs.get("name") or attrs.get("property") or "").lower()
        content = (attrs.get("content") or "").strip()
        if not content:
            continue
        if name in ("citation_abstract", "og:description", "description"):
            if len(content) > len(abstract):
                abstract = content
        elif name == "citation_author":
            if content not in authors:
                authors.append(content)

    if not abstract:
        # Fall back to a block that announces itself as the abstract.
        block = re.search(
            r"<(?P<tag>div|section|p)\b[^>]*\b(?:id|class)=[\"'][^\"']*abstract"
            r"[^\"']*[\"'][^>]*>(?P<body>.*?)</(?P=tag)>",
            page,
            re.IGNORECASE | re.DOTALL,
        )
        if block:
            abstract = _text(block.group("body"))

    return abstract, authors


# ---------------------------------------------------------------------------
# Collection
# ---------------------------------------------------------------------------


def _years(block: dict, since: date, today: date) -> list[int]:
    """Which programme years to sweep.

    The backfill window decides the floor — ``--days 400`` should reach last
    year's programme — and ``years_back`` guarantees a minimum sweep so that a
    routine two-day run still notices a programme posted in January.
    """
    years_back = max(1, int(block.get("years_back", 2)))
    span = {today.year - offset for offset in range(years_back)}
    span.update(range(min(since.year, today.year), today.year + 1))
    return sorted((y for y in span if y > 2000), reverse=True)


def _listing_urls(venue: dict, years: list[int]) -> list[tuple[str, str, int]]:
    """``(base, url, year)`` for every programme page of one venue.

    A venue that splits a year across locations lists them under
    ``/virtual/<year>/loc/<city>/``; NeurIPS 2025 is the first to need it.
    """
    host = str(venue.get("virtual_host") or "").strip().strip("/")
    if not host:
        return []
    base = host if host.startswith("http") else f"https://{host}"
    base = base.rstrip("/")

    locations = venue.get("virtual_locations") or {}
    urls: list[tuple[str, str, int]] = []
    for year in years:
        cities = locations.get(year) or locations.get(str(year)) or []
        if isinstance(cities, str):
            cities = [cities]
        if cities:
            for city in cities:
                slug = str(city).strip().strip("/")
                urls.append((base, f"{base}/virtual/{year}/loc/{slug}/papers.html", year))
        else:
            urls.append((base, f"{base}/virtual/{year}/papers.html", year))
    return urls


def _to_paper(entry: Listing) -> Paper:
    return Paper(
        id=canonical_paper_id(title=entry.title),
        title=entry.title,
        source="virtualsite",
        source_id=f"{entry.venue.lower()}-{entry.year}-{entry.site_id}",
        authors=list(entry.authors),
        abstract=entry.abstract,
        url=entry.url,
        venue=entry.venue,
        year=entry.year,
        published=f"{entry.year}-01-01" if entry.year else "",
        first_seen=utcnow(),
        last_seen=utcnow(),
    )


def collect(
    cfg: Config,
    topics: list[Topic],
    venues: list[dict],
    since: date,
    client: Client,
    errors: list[str] | None = None,
) -> list[Paper]:
    """Fetch the programme pages and return the papers a topic might want.

    Unlike the other indexes this is not called per topic: the page is the same
    whoever is asking, so it is fetched once and scored against every topic.
    """
    block = (cfg.sources.get("conferences", {}) or {}).get("virtual_site", {}) or {}
    if not block.get("enabled", True):
        return []

    tracked = [t for t in topics if t.source_enabled("conferences")]
    if not tracked:
        return []

    years = _years(block, since, date.today())
    candidates: dict[str, tuple[Listing, float]] = {}
    attempts = failures = 0
    last_error: Exception | None = None

    for venue in venues:
        name = str(venue.get("name") or "")
        for base, url, year in _listing_urls(venue, years):
            attempts += 1
            try:
                raw = client.get(url)
            except HTTPError as exc:
                # A programme that does not exist yet is a 404, and that is the
                # normal state of next year's page. Only a clean sweep of
                # failures is worth reporting.
                _LOG.debug("virtual site %s unavailable: %s", url, exc)
                failures += 1
                last_error = exc
                continue

            entries = parse_listing(raw.decode("utf-8", errors="replace"), base)
            if not entries:
                _LOG.warning(
                    "virtual site %s returned no papers; the page shape may have "
                    "changed", url
                )
                continue
            _LOG.info("virtual site: %d papers listed at %s", len(entries), url)

            for entry in entries:
                entry.venue = entry.venue or name
                entry.year = entry.year or year
                scores, _, _ = score_against_topics(
                    tracked,
                    title=entry.title,
                    body=entry.abstract,
                    authors=entry.authors,
                    settings=cfg.settings,
                )
                if not scores:
                    continue
                best = max(scores.values())
                key = entry.title.strip().lower()
                if key not in candidates or candidates[key][1] < best:
                    candidates[key] = (entry, best)

    if errors is not None and attempts and failures == attempts:
        errors.append(f"virtual_site: all {attempts} page(s) failed: {last_error}")

    ranked = [entry for entry, _ in sorted(candidates.values(), key=lambda p: -p[1])]

    if block.get("fetch_details", True):
        cap = int(block.get("max_details_per_run", 40))
        _fill_details(ranked[:cap], client)
        if len(ranked) > cap:
            _LOG.info(
                "virtual site: %d candidate(s) over the detail cap of %d kept their "
                "titles only",
                len(ranked) - cap,
                cap,
            )

    return [_to_paper(entry) for entry in ranked]


def _fill_details(entries: list[Listing], client: Client) -> None:
    """Fetch each paper's own page for the abstract and authors."""
    for entry in entries:
        if entry.abstract and entry.authors:
            continue
        try:
            raw = client.get(entry.url)
        except HTTPError as exc:
            # The record still stands without them; the reader fetches the
            # paper itself when the abstract will not settle the question.
            _LOG.debug("virtual site detail %s unavailable: %s", entry.url, exc)
            continue
        abstract, authors = parse_detail(raw.decode("utf-8", errors="replace"))
        entry.abstract = entry.abstract or abstract
        entry.authors = entry.authors or authors
