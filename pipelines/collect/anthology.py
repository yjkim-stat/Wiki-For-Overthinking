"""ACL Anthology — the venue's own proceedings, with abstracts already in them.

The `*ACL` conferences have no API worth the name, but they publish a single
page per event that lists every paper the event accepted: title, authors and
**the abstract**, all inline. That last part is what makes this collector
different from `arxiv_listing`, which can only score a title and then spend one
request per match on the abstract it lacks. Here a venue-year costs exactly one
request and every paper is scored on the same evidence a reader would have.

Three consequences of reading a proceedings index rather than querying one.

*It is browsed, not searched.* There is no query string — the page is the whole
programme. So a run fetches once per venue-year and filters locally, and the
cost does not grow with the number of topics.

*An event is not only its conference.* An ACL event page carries the main
tracks, Findings, and every co-located workshop: NAACL 2024 lists 488
`naacl-long` and 297 `findings-naacl` papers alongside roughly eight hundred
from SemEval, WOAH, BEA and a dozen others. A workshop paper is published at
the workshop, not at the conference, so filing one under the venue's name would
put a claim in the archive that is not true. The default keeps the venue's own
tracks and Findings; anything else is opt-in, and **what was left out is
logged** rather than dropped quietly.

*The pages are large.* Four to nineteen megabytes each, growing with the year.
One request is still cheaper than a thousand, but `max_bytes` exists so that a
page which has changed shape into something enormous is refused rather than
parsed.

Identifiers are exact here, which is rare. An entry's anthology id yields its
DOI directly — `10.18653/v1/<id>` — so a paper collected here carries a real
identifier rather than a title fingerprint, and folds against the same work
collected from arXiv through the title key that `dedupe` registers for both.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import date

from ..common.config import Config, Topic
from ..common.http import Client, HTTPError, from_settings
from ..common.log import get
from ..common.schema import Paper, canonical_paper_id, utcnow
from ..enrich.score import score_against_topics

_LOG = get(__name__)

# `<strong><a class=align-middle href=/2024.acl-long.1/>Title</a></strong>` and
# then everything up to the next such anchor. The Anthology serves unquoted
# attributes, so the pattern must not assume quotes -- an earlier draft written
# against `href="..."` matched nothing at all on the live page.
_ENTRY_RE = re.compile(
    r"<strong><a class=align-middle href=/(?P<id>\d{4}\.[a-z0-9\-]+\.\d+)/>"
    r"(?P<title>.*?)</a></strong>(?P<rest>.*?)"
    r"(?=<strong><a class=align-middle href=/\d{4}\.|\Z)",
    re.DOTALL,
)
_PEOPLE_RE = re.compile(r"<a href=/people/[^>]*>(?P<name>[^<]+)</a>")
_ABSTRACT_TMPL = r"id=abstract-{key}\b.*?<div class=\"card-body p-3 small\">(?P<body>.*?)</div>"
_TAG_RE = re.compile(r"<[^>]+>")
# The Anthology wraps letters whose case must survive in `acl-fixed-case`
# spans, mid-word: `<span class=acl-fixed-case>I</span>ns<span
# class=acl-fixed-case>CL</span>:` is "InsCL:". Replacing a tag with a space --
# which is the right default everywhere else, and what `common/html.text` does
# -- turns that into "I ns CL :". So inline tags are removed with no separator
# and only the ones that genuinely end a line become whitespace.
_BREAK_RE = re.compile(r"</?(?:br|p|div|li|ul|ol)\b[^>]*>", re.IGNORECASE)
# `2024.naacl-long.12` -> volume `naacl-long`, index `12`.
_VOLUME_RE = re.compile(r"^\d{4}\.(?P<volume>[a-z0-9\-]+)\.(?P<index>\d+)$")


@dataclass
class Entry:
    """One paper as the proceedings index gives it."""

    anthology_id: str
    volume: str
    title: str
    authors: list[str] = field(default_factory=list)
    abstract: str = ""

    @property
    def doi(self) -> str:
        # Only the dotted id form is matched by `_ENTRY_RE`, and that form and
        # this DOI prefix arrived together. Pre-2020 volumes are numbered
        # `P19-1001` and are deliberately not parsed, so this never guesses.
        return f"10.18653/v1/{self.anthology_id}"


def _settings(cfg: Config) -> dict:
    return (cfg.sources.get("conferences", {}) or {}).get("anthology", {}) or {}


def _clean(fragment: str) -> str:
    """Readable text, without breaking a word that markup runs through."""
    import html as _html

    from ..common import html as html_util

    spaced = _BREAK_RE.sub(" ", html_util.strip_comments(fragment or ""))
    return " ".join(_html.unescape(_TAG_RE.sub("", spaced)).split())


def parse_event(page: str) -> list[Entry]:
    """Every paper listed on one event page.

    Front matter is excluded: each volume opens with an index entry whose title
    is the proceedings' own and which carries no abstract. Including it would
    put a record in the archive for a book rather than a paper.
    """
    entries: list[Entry] = []
    seen: set[str] = set()

    for match in _ENTRY_RE.finditer(page):
        anthology_id = match.group("id")
        if anthology_id in seen:
            continue
        parts = _VOLUME_RE.match(anthology_id)
        if parts is None:
            continue
        if parts.group("index") == "0":
            continue  # front matter

        title = _clean(match.group("title"))
        if not title:
            continue

        rest = match.group("rest")
        pattern = re.compile(
            _ABSTRACT_TMPL.format(key=re.escape(anthology_id.replace(".", "--"))),
            re.DOTALL,
        )
        found = pattern.search(rest)

        seen.add(anthology_id)
        entries.append(
            Entry(
                anthology_id=anthology_id,
                volume=parts.group("volume"),
                title=title,
                authors=[a.strip() for a in _PEOPLE_RE.findall(rest) if a.strip()],
                abstract=_clean(found.group("body")) if found else "",
            )
        )
    return entries


def wanted_volumes(key: str, configured: list[str] | None) -> list[str]:
    """Which volumes of an event belong to the venue that names it.

    An explicit list wins. Otherwise the venue's own tracks and its Findings —
    `acl-long`, `acl-short`, `acl-demo`, `findings-acl` — which is what somebody
    who asked for ACL meant.
    """
    if configured:
        return [str(v).strip().lower() for v in configured if str(v).strip()]
    return [f"{key}-", f"findings-{key}"]


def _keeps(volume: str, prefixes: list[str]) -> bool:
    return any(volume == p.rstrip("-") or volume.startswith(p) for p in prefixes)


def _to_paper(entry: Entry, venue: str, year: int, base_url: str) -> Paper:
    return Paper(
        id=canonical_paper_id(doi=entry.doi),
        title=entry.title,
        source="anthology",
        source_id=entry.anthology_id,
        authors=list(entry.authors),
        abstract=entry.abstract,
        venue=venue,
        year=year,
        url=f"{base_url}/{entry.anthology_id}/",
        pdf_url=f"{base_url}/{entry.anthology_id}.pdf",
        doi=entry.doi,
        first_seen=utcnow(),
        last_seen=utcnow(),
    )


def _years(cfg: Config, venue: dict, since: date | None) -> list[int]:
    explicit = venue.get("anthology_years") or _settings(cfg).get("years")
    if explicit:
        return [int(y) for y in explicit]
    if since is not None:
        return list(range(since.year, date.today().year + 1))
    return [date.today().year]


def collect(
    cfg: Config,
    topics: list[Topic],
    venues: list[dict],
    since: date | None = None,
    client: Client | None = None,
    errors: list[str] | None = None,
) -> list[Paper]:
    """Read each tracked venue's proceedings index and keep what a topic wants.

    Like the programme pages and unlike the queried indexes, this is not called
    per topic: an event page is the same page whoever is asking, so it is
    fetched once and scored against every topic.
    """
    block = _settings(cfg)
    if not block.get("enabled", True):
        return []

    venues = [v for v in (venues or []) if v.get("anthology_key")]
    if not venues or not topics:
        return []

    base_url = str(block.get("base_url", "https://aclanthology.org")).rstrip("/")
    max_bytes = int(block.get("max_bytes", 32 * 1024 * 1024))
    client = client or from_settings(
        cfg.settings, min_interval_s=float(block.get("min_request_interval_s", 3.0))
    )

    collected: dict[str, Paper] = {}
    attempts = failures = 0
    last_error: Exception | None = None

    for venue in venues:
        key = str(venue.get("anthology_key")).strip().lower()
        name = str(venue.get("name") or key.upper())
        prefixes = wanted_volumes(key, block.get("volumes") or venue.get("anthology_volumes"))

        for year in _years(cfg, venue, since):
            url = f"{base_url}/events/{key}-{year}/"
            attempts += 1
            try:
                raw = client.get(url)
            except HTTPError as exc:
                # A venue that did not run in a given year is a 404, not a fault.
                _LOG.debug("anthology %s unavailable: %s", url, exc)
                failures += 1
                last_error = exc
                continue

            if len(raw) > max_bytes:
                _LOG.warning(
                    "anthology %s is %d bytes, over the cap of %d; skipped",
                    url, len(raw), max_bytes,
                )
                continue

            entries = parse_event(raw.decode("utf-8", errors="replace"))
            if not entries:
                _LOG.warning(
                    "anthology %s parsed to no entries; the page shape may have "
                    "changed", url
                )
                continue

            kept = [e for e in entries if _keeps(e.volume, prefixes)]
            skipped = len(entries) - len(kept)
            if skipped:
                # Never a silent cap: the volumes left out are named, because a
                # run that quietly halved its own reach reads like a quiet year.
                others = sorted({e.volume for e in entries if e not in kept})
                _LOG.info(
                    "anthology %s-%d: %d paper(s) in %s; %d left out from %s",
                    key, year, len(kept), ", ".join(prefixes), skipped,
                    ", ".join(others[:8]) + ("…" if len(others) > 8 else ""),
                )
            else:
                _LOG.info("anthology %s-%d: %d paper(s)", key, year, len(kept))

            for entry in kept:
                scores, _, _ = score_against_topics(
                    topics,
                    title=entry.title,
                    body=entry.abstract,
                    authors=entry.authors,
                    settings=cfg.settings,
                )
                if not scores:
                    continue
                paper = _to_paper(entry, name, year, base_url)
                collected.setdefault(paper.id, paper)

    if errors is not None and attempts and failures == attempts:
        errors.append(f"anthology: all {attempts} request(s) failed: {last_error}")

    return list(collected.values())
