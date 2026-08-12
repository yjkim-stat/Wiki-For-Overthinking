"""arXiv listing collector — the way in when the API is not available to you.

``export.arxiv.org`` is the right way to read arXiv and this repository prefers
it. But the API and the website are different hosts, and a host that is blocked
from one is not always blocked from the other: a network policy, a corporate
proxy or an arXiv-side rate limit can leave ``arxiv.org/list/<category>/recent``
readable while the API answers 403 to everything. This collector exists for that
case and no other. ``arxiv.listing.mode`` defaults to ``auto``, which uses it
only when the API returned nothing.

Three things follow from reading a listing rather than querying an index.

*It is browsed, not searched.* There is no query string — the page is every
paper announced in that category over the last few days. So a run fetches the
listing once per category, not once per topic, and filters locally. Categories
are the union of what the topics ask for, so one topic narrowing its list cannot
hide a category from another.

*The listing carries no abstracts.* Titles, authors and subjects only. A title
is scored first and only papers matching something a topic tracks cost a second
request for the abstract. **This is a real loss of recall against the API**,
which searches abstracts too: a paper whose keywords appear only in its abstract
is invisible here. That is the price of the fallback, and it is why the mode
defaults to ``auto`` rather than ``always``.

*Announcements are days, not a date range.* ``/recent`` covers the last few
announcement days as arXiv defines them, so the collector cannot honour a
``--days 90`` backfill. It collects what is announced and lets scoring and
deduplication do the rest; an older paper simply is not there.

Pagination is bounded on purpose. arXiv asks not to be crawled hard, and the
whole point of scoring titles locally is that reading the day's announcements
costs a handful of requests rather than thousands.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import date, datetime

from ..common import html as html_util
from ..common.config import Config, Topic
from ..common.http import Client, HTTPError, from_settings
from ..common.log import get
from ..common.schema import Paper, canonical_paper_id, strip_arxiv_version, utcnow
from ..enrich import coverage
from ..enrich.score import score_against_topics

_LOG = get(__name__)

# The listing is a definition list: one <dt> holding the identifier and links,
# one <dd> holding the metadata. Pairing them is what keeps a paper's title
# attached to its own id.
_ENTRY_RE = re.compile(r"<dt\b[^>]*>(?P<dt>.*?)</dt>\s*<dd\b[^>]*>(?P<dd>.*?)</dd>",
                       re.IGNORECASE | re.DOTALL)
_ABS_RE = re.compile(r"/abs/(?P<id>\d{4}\.\d{4,5})(?:v\d+)?", re.IGNORECASE)
_FIELD_RE = {
    name: re.compile(
        rf"<div\b[^>]*class=[\"'][^\"']*list-{name}[^\"']*[\"'][^>]*>(?P<body>.*?)</div>",
        re.IGNORECASE | re.DOTALL,
    )
    for name in ("title", "authors", "subjects")
}
# "total of 1,234 entries" — the only thing on the page that says how far the
# pagination goes.
_TOTAL_RE = re.compile(r"total of\s+([\d,]+)\s+entries", re.IGNORECASE)
# "Fri, 8 Aug 2025 (showing 50 of 213 entries )" — the announcement day, and
# arXiv's own count of what that day holds. The count is the whole point: it is
# the only number in the system that does not come from our own parsing.
_DAY_RE = re.compile(
    r"<h3\b[^>]*>\s*(?P<day>[A-Za-z]{3},\s*\d{1,2}\s+[A-Za-z]{3}\s+\d{4})"
    r"[^<]*?(?:showing\s+[\d,]+\s+of\s+)?(?P<total>[\d,]+)\s+entries",
    re.IGNORECASE | re.DOTALL,
)
_CATEGORY_RE = re.compile(r"\(([a-z-]+\.[A-Z]{2}|[a-z-]{3,})\)")


@dataclass
class Day:
    """One announcement day on a listing page."""

    day: str  # ISO date, or "" when the page did not label the section
    announced: int
    entries: list["Entry"] = field(default_factory=list)


@dataclass
class Entry:
    """One announcement, as the listing gives it: no abstract."""

    arxiv_id: str
    title: str
    authors: list[str] = field(default_factory=list)
    categories: list[str] = field(default_factory=list)
    abstract: str = ""
    # LOCAL: the announcement day this entry was listed under, ISO, or "" when
    # the page carried no day heading. `parse_listing` cannot know it — the day
    # is a property of the section an entry sits in, not of the entry's own
    # markup — so `parse_days` fills it in and `parse_listing` leaves it empty.
    announced: str = ""


def _settings(cfg: Config) -> dict:
    return (cfg.sources.get("arxiv", {}) or {}).get("listing", {}) or {}


def parse_total(page: str) -> int:
    """How many entries the category's listing holds, or 0 if it does not say."""
    match = _TOTAL_RE.search(page or "")
    return int(match.group(1).replace(",", "")) if match else 0


def _iso_day(label: str) -> str:
    for fmt in ("%a, %d %b %Y", "%A, %d %B %Y"):
        try:
            return datetime.strptime(" ".join(label.split()), fmt).date().isoformat()
        except ValueError:
            continue
    return ""


def parse_days(page: str) -> list[Day]:
    """Split a listing page into its announcement days.

    arXiv heads each day with its date and its own entry count. That count is
    the only number in this pipeline that does not come from our own parsing,
    which makes it the one thing that can tell "nothing was announced" apart
    from "we failed to read what was announced".

    A page with no day headings is returned as a single undated day, so a
    redesign that drops them degrades to what this collector did before rather
    than to nothing.
    """
    clean = html_util.strip_comments(page)
    headings = list(_DAY_RE.finditer(clean))
    if not headings:
        entries = parse_listing(page)
        return [Day(day="", announced=parse_total(page) or len(entries), entries=entries)]

    days: list[Day] = []
    for index, heading in enumerate(headings):
        start = heading.end()
        end = headings[index + 1].start() if index + 1 < len(headings) else len(clean)
        iso = _iso_day(heading.group("day"))  # LOCAL
        entries = parse_listing(clean[start:end])
        for entry in entries:
            entry.announced = iso
        days.append(
            Day(
                day=iso,
                announced=int(heading.group("total").replace(",", "")),
                entries=entries,
            )
        )
    return days


def parse_listing(page: str) -> list[Entry]:
    """Extract the announcements from one listing page.

    Each entry is anchored on the ``/abs/<id>`` link in its ``<dt>``, so a paper
    without an identifier is not an entry — which is what keeps the page's
    navigation, its category description and its "browse context" sidebar from
    contributing rows.
    """
    entries: list[Entry] = []
    seen: set[str] = set()

    for match in _ENTRY_RE.finditer(html_util.strip_comments(page)):
        identifier = _ABS_RE.search(match.group("dt"))
        if identifier is None:
            continue
        arxiv_id = strip_arxiv_version(identifier.group("id"))
        if arxiv_id in seen:
            continue

        body = match.group("dd")
        title_match = _FIELD_RE["title"].search(body)
        title = html_util.field_text(title_match.group("body")) if title_match else ""
        if not title:
            # An entry with an id but no readable title is a shape we do not
            # understand. Recording it would put a blank row in the archive.
            continue

        authors_match = _FIELD_RE["authors"].search(body)
        authors = (
            [a.strip() for a in html_util.field_text(authors_match.group("body")).split(",")]
            if authors_match
            else []
        )

        subjects_match = _FIELD_RE["subjects"].search(body)
        categories = (
            _CATEGORY_RE.findall(html_util.field_text(subjects_match.group("body")))
            if subjects_match
            else []
        )

        seen.add(arxiv_id)
        entries.append(
            Entry(
                arxiv_id=arxiv_id,
                title=title,
                authors=[a for a in authors if a],
                categories=categories,
            )
        )
    return entries


def parse_abstract(page: str) -> str:
    """The abstract from an ``/abs/`` page."""
    tags = html_util.meta(page)
    for name in ("citation_abstract", "og:description", "description"):
        for value in tags.get(name, []):
            if value.strip():
                return value.strip()
    return html_util.abstract_block(page)


def _to_paper(entry: Entry) -> Paper:
    # LOCAL: the announcement day is the only date a listing page offers, and it
    # is close enough to the submission date to be the right value for
    # `published` — arXiv announces the evening after the cutoff. Leaving it
    # empty is not a neutral choice: `publish/archive.py` files a dateless paper
    # under `archive/papers/unknown/` and the flat index sorts it below
    # everything, so a fallback record would be second-class purely because of
    # where it came from. When the page carried no day heading this stays empty,
    # which is the honest answer rather than a guessed one.
    published = entry.announced
    return Paper(
        id=canonical_paper_id(arxiv_id=entry.arxiv_id),
        title=entry.title,
        source="arxiv",
        source_id=entry.arxiv_id,
        authors=list(entry.authors),
        abstract=entry.abstract,
        url=f"https://arxiv.org/abs/{entry.arxiv_id}",
        pdf_url=f"https://arxiv.org/pdf/{entry.arxiv_id}",
        published=published,  # LOCAL
        year=int(published[:4]) if published[:4].isdigit() else 0,  # LOCAL
        categories=list(entry.categories),
        arxiv_id=entry.arxiv_id,
        first_seen=utcnow(),
        last_seen=utcnow(),
    )


def _categories_for(cfg: Config, topics: list[Topic]) -> list[str]:
    """The union of the categories the topics ask for."""
    block = cfg.sources.get("arxiv", {}) or {}
    default = list(block.get("categories") or [])
    wanted: list[str] = []
    for topic in topics:
        if not topic.source_enabled("arxiv"):
            continue
        for category in topic.source_option("arxiv", "categories", default) or []:
            if category not in wanted:
                wanted.append(str(category))
    return wanted


def collect(
    cfg: Config,
    topics: list[Topic],
    since: date | None = None,
    client: Client | None = None,
    errors: list[str] | None = None,
) -> list[Paper]:
    """Read the recent listing for every tracked category.

    ``since`` is accepted for signature symmetry with the other collectors and
    is not used: ``/recent`` is defined by arXiv's announcement schedule, not by
    a date range the caller chooses.
    """
    block = _settings(cfg)
    categories = _categories_for(cfg, topics)
    if not categories:
        return []

    base_url = str(block.get("base_url", "https://arxiv.org/list")).rstrip("/")
    page_size = max(1, int(block.get("page_size", 250)))
    max_pages = max(1, int(block.get("max_pages", 8)))
    client = client or from_settings(
        cfg.settings,
        min_interval_s=float(block.get("min_request_interval_s", 5.0)),
    )

    candidates: dict[str, tuple[Entry, float]] = {}
    attempts = failures = 0
    last_error: Exception | None = None

    for category in categories:
        for page_index in range(max_pages):
            skip = page_index * page_size
            url = f"{base_url}/{category}/recent"
            attempts += 1
            try:
                raw = client.get(url, {"skip": skip, "show": page_size})
            except HTTPError as exc:
                _LOG.debug("arxiv listing %s (skip=%d) failed: %s", url, skip, exc)
                failures += 1
                last_error = exc
                break

            page = raw.decode("utf-8", errors="replace")
            # LOCAL: `parse_days` rather than `parse_listing` — the day heading
            # is what dates an entry, and an entry that arrives without a date is
            # filed under an unknown year for the rest of its life. On a page
            # with no headings this degrades to one undated day holding
            # everything, which is what `parse_listing` returned on its own.
            entries = [e for day in parse_days(page) for e in day.entries]
            if not entries:
                if page_index == 0:
                    _LOG.warning(
                        "arxiv listing for %s parsed to no entries; the page shape "
                        "may have changed", category
                    )
                break

            _LOG.info(
                "arxiv listing: %d announcement(s) for %s (skip=%d)",
                len(entries), category, skip,
            )
            for entry in entries:
                scores, _, _ = score_against_topics(
                    topics,
                    title=entry.title,
                    authors=entry.authors,
                    settings=cfg.settings,
                )
                if not scores:
                    continue
                best = max(scores.values())
                if entry.arxiv_id not in candidates or candidates[entry.arxiv_id][1] < best:
                    candidates[entry.arxiv_id] = (entry, best)

            total = parse_total(page)
            if len(entries) < page_size or (total and skip + page_size >= total):
                break

    if errors is not None and attempts and failures == attempts:
        errors.append(f"arxiv_listing: all {attempts} page(s) failed: {last_error}")

    ranked = [entry for entry, _ in sorted(candidates.values(), key=lambda p: -p[1])]
    if block.get("fetch_abstracts", True):
        cap = int(block.get("max_abstracts_per_run", 60))
        _fill_abstracts(ranked[:cap], client, errors)
        if len(ranked) > cap:
            _LOG.info(
                "arxiv listing: %d match(es) over the abstract cap of %d kept their "
                "titles only",
                len(ranked) - cap, cap,
            )

    return [_to_paper(entry) for entry in ranked]


def _fill_abstracts(
    entries: list[Entry], client: Client, errors: list[str] | None = None
) -> None:
    """Fetch each match's ``/abs/`` page for the abstract the listing omits."""
    for entry in entries:
        if entry.abstract:
            continue
        url = f"https://arxiv.org/abs/{entry.arxiv_id}"
        try:
            raw = client.get(url)
        except HTTPError as exc:
            # An abstract-less record is a true statement about what was read.
            _LOG.debug("arxiv abs %s unavailable: %s", entry.arxiv_id, exc)
            continue
        entry.abstract = parse_abstract(raw.decode("utf-8", errors="replace"))


# ---------------------------------------------------------------------------
# The sweep: know what a day held, and close the gap over time
# ---------------------------------------------------------------------------


def _sweep_settings(cfg: Config) -> dict:
    return (_settings(cfg).get("sweep", {}) or {})


def _row(entry: Entry) -> dict:
    return {
        "id": entry.arxiv_id,
        "title": entry.title,
        "authors": list(entry.authors),
        "categories": list(entry.categories),
        "abstract": entry.abstract,
    }


def sweep(
    cfg: Config,
    topics: list[Topic],
    store,
    client: Client | None = None,
    errors: list[str] | None = None,
) -> dict[str, int]:
    """Record what each announcement day held, and pay down what is missing.

    Two passes, and they are separate because they cost different amounts.

    The **listing pass** walks each category's recent days and files every
    announced identifier — title, authors, subjects, and an empty abstract. It
    costs a handful of requests and it is what turns arXiv's own per-day count
    into something we can be measured against.

    The **backfill pass** fetches the abstracts those rows are missing, ordered
    by how well the title scores against the tracked topics and bounded by a
    per-run budget. Ordering matters more than it looks: it means a run spends
    its budget on what the group is likely to want while still, given enough
    runs, capturing everything. A day's debt is carried in the ledger rather
    than being paid off in one enormous run.
    """
    block = _sweep_settings(cfg)
    counts = {"days": 0, "listed": 0, "captured": 0, "fetched": 0}
    if not block.get("enabled", True):
        return counts

    categories = _categories_for(cfg, topics)
    if not categories:
        return counts

    listing_block = _settings(cfg)
    base_url = str(listing_block.get("base_url", "https://arxiv.org/list")).rstrip("/")
    page_size = max(1, int(listing_block.get("page_size", 250)))
    max_pages = max(1, int(listing_block.get("max_pages", 8)))
    client = client or from_settings(
        cfg.settings,
        min_interval_s=float(listing_block.get("min_request_interval_s", 5.0)),
    )

    ledger: list[coverage.DayCoverage] = []
    pending: list[tuple[str, str, Entry, float]] = []

    for category in categories:
        seen_days: dict[str, coverage.DayCoverage] = {}
        for page_index in range(max_pages):
            url = f"{base_url}/{category}/recent"
            try:
                raw = client.get(url, {"skip": page_index * page_size, "show": page_size})
            except HTTPError as exc:
                _LOG.debug("arxiv sweep %s failed: %s", url, exc)
                if errors is not None:
                    errors.append(f"arxiv_sweep[{category}]: {exc}")
                break

            days = parse_days(raw.decode("utf-8", errors="replace"))
            if not any(day.entries for day in days):
                if page_index == 0:
                    _LOG.warning(
                        "arxiv sweep for %s parsed no entries; the page shape may "
                        "have changed", category
                    )
                break

            for day in days:
                if not day.entries:
                    continue
                held = store.load_abstracts(category, day.day)
                store.save_abstracts(category, day.day, [_row(e) for e in day.entries])
                held = store.load_abstracts(category, day.day)

                row = seen_days.get(day.day) or coverage.DayCoverage(
                    category=category, day=day.day
                )
                row.announced = max(row.announced, day.announced)
                row.listed = len(held)
                row.captured = sum(
                    1 for r in held.values() if str(r.get("abstract", "")).strip()
                )
                seen_days[day.day] = row

                for entry in day.entries:
                    stored = held.get(entry.arxiv_id) or {}
                    if str(stored.get("abstract", "")).strip():
                        continue
                    scores, _, _ = score_against_topics(
                        topics, title=entry.title, authors=entry.authors,
                        settings=cfg.settings,
                    )
                    pending.append(
                        (category, day.day, entry, max(scores.values(), default=0.0))
                    )

            if sum(len(d.entries) for d in days) < page_size:
                break

        ledger.extend(seen_days.values())
        counts["days"] += len(seen_days)

    # LOCAL: record before the backfill, not only after it. The listing pass
    # above is a handful of requests and it is what produces the per-day count —
    # the one number here that is arXiv's rather than ours. The backfill below is
    # up to `max_abstracts_per_run` fetches at the listing's request interval,
    # which is minutes. Holding the ledger until that finishes means an
    # interrupted run records nothing at all, and a run that is always
    # interrupted looks exactly like a sweep that was never enabled.
    # `coverage.record` merges on a high-water mark, so writing twice costs one
    # rewrite and cannot regress.
    if ledger:
        coverage.record(cfg.layout, ledger)

    # Relevance first, then everything else. Both halves matter: the group gets
    # what it wants soonest, and nothing is permanently skipped.
    pending.sort(key=lambda item: -item[3])
    budget = int(block.get("max_abstracts_per_run", 120))
    filled: dict[tuple[str, str], list[dict]] = {}
    for category, day, entry, _score in pending[:budget]:
        url = f"https://arxiv.org/abs/{entry.arxiv_id}"
        try:
            raw = client.get(url)
        except HTTPError as exc:
            _LOG.debug("arxiv abs %s unavailable: %s", entry.arxiv_id, exc)
            continue
        abstract = parse_abstract(raw.decode("utf-8", errors="replace"))
        if not abstract:
            continue
        entry.abstract = abstract
        filled.setdefault((category, day), []).append(_row(entry))
        counts["fetched"] += 1

    for (category, day), rows in filled.items():
        store.save_abstracts(category, day, rows)

    # Re-count after the backfill so the ledger reflects this run's work.
    for row in ledger:
        held = store.load_abstracts(row.category, row.day)
        row.listed = max(row.listed, len(held))
        row.captured = sum(
            1 for r in held.values() if str(r.get("abstract", "")).strip()
        )
        counts["listed"] += row.listed
        counts["captured"] += row.captured

    if ledger:
        coverage.record(cfg.layout, ledger)
    if len(pending) > budget:
        _LOG.info(
            "arxiv sweep: %d abstract(s) still owed; a later run will pay them",
            len(pending) - budget,
        )
    _LOG.info("arxiv sweep: %s", counts)
    return counts
