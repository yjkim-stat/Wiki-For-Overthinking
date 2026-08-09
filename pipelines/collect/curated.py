"""Curated weekly lists.

An editor who reads a week of output and publishes ten papers is applying a
filter nothing else in this pipeline can reproduce: judgement, over everything
at once, before any keyword sees it. This collector takes such a list as a
source of *pointers*.

What it deliberately does not take is metadata. A list entry names a paper the
way people say it out loud -- an acronym, then a paragraph of what the editor
found interesting -- and neither of those is a bibliography. The title, authors
and abstract come from following the link, so a curated paper enters the
archive with the record it would have had if a collector had found it first,
and dedup merges the two instead of creating a second entity.

The cost of that rule is stated where it lands: an entry whose link is not an
arXiv id is skipped, by name, in the log. `NOOA` is not a title, and a record
carrying it would be wrong in the one field every other record keys on.

A pick that is already in the archive is still emitted, with `source` set to
this collector. Deduplication joins sources with `+`, so the stored record
gains `+curated` and the fact that somebody chose it stops being invisible.

Editorial weight, and what this collector does *not* claim. A hand-filed PDF
bypasses scoring because filing it is the group's own decision. A curated list
is somebody else's decision, over a whole field rather than the group's topics,
so its picks are scored like anything else. Most weeks that means most of the
list is rejected, and that is the correct reading of a general list against a
narrow archive.
"""

from __future__ import annotations

import re
import urllib.parse
from datetime import date

from . import arxiv
from ..common.config import Config, Topic
from ..common.http import Client, HTTPError, from_settings
from ..common.log import get
from ..common.schema import Paper, strip_arxiv_version
from ..common.store import RecordStore

_LOG = get(__name__)

# `- [Top AI Papers of the Week (July 27 - August 2)](years/2026.md#anchor)`.
# Only list items pointing at another markdown file: the same page carries a
# newsletter signup and a back-link, and neither is an issue of the list.
_INDEX_ENTRY = re.compile(r"^[ \t]*[-*][ \t]+\[[^\]]*\]\(([^)\s#]+\.md)(#[^)\s]*)?\)", re.M)

# An issue heading. `##` exactly -- `###` is a subsection inside one.
_HEADING = re.compile(r"^##[ \t]+(.*)$", re.M)

_LINK = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")
_ARXIV_URL = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?", re.I)


def _get_text(client: Client, url: str) -> str:
    return client.get(url).decode("utf-8", "replace")


def _anchor(heading: str) -> str:
    """The fragment a markdown host derives from a heading.

    Lowercase, punctuation dropped, spaces hyphenated. Used to line an issue up
    with the index entry that points at it, so "which issues are the recent
    ones" comes from the index rather than from assuming the page is sorted.
    """
    text = re.sub(r"[^a-z0-9 \-]", "", heading.strip().lower())
    return text.replace(" ", "-")


def _index_entries(text: str, index_url: str) -> list[tuple[str, str]]:
    """``(page_url, anchor)`` for every issue the index links to, in its order."""
    entries = []
    for match in _INDEX_ENTRY.finditer(text):
        page = urllib.parse.urljoin(index_url, match.group(1))
        entries.append((page, (match.group(2) or "").lstrip("#")))
    return entries


def _sections(text: str) -> list[tuple[str, str]]:
    """Split a page into ``(heading, body)`` at its second-level headings."""
    marks = list(_HEADING.finditer(text))
    return [
        (
            mark.group(1).strip(),
            text[mark.end() : (marks[i + 1].start() if i + 1 < len(marks) else len(text))],
        )
        for i, mark in enumerate(marks)
    ]


def _paper_links(body: str, label: str) -> list[str]:
    """Links an issue offers as the paper itself, in the order they appear.

    The labelled link is the precise answer: an issue's commentary can name
    other work in passing, and following that would archive papers the editor
    mentioned rather than the ones they picked. The unlabelled fallback exists
    for a list that does not use the convention at all.
    """
    links = _LINK.findall(body)
    wanted = label.strip().lower()
    urls = [url for text, url in links if text.strip().lower() == wanted]
    if not urls:
        urls = [url for _, url in links if _ARXIV_URL.search(url)]
    out: list[str] = []
    for url in urls:
        if url not in out:
            out.append(url)
    return out


def _read_list(
    client: Client, url: str, max_issues: int, label: str
) -> tuple[list[str], list[str], list[str]]:
    """Read one list. Returns ``(arxiv_ids, other_links, issue_headings)``."""
    pages: dict[str, str] = {url: _get_text(client, url)}
    entries = _index_entries(pages[url], url)

    if entries:
        selected = entries[:max_issues] if max_issues else entries
        anchors = {anchor for _, anchor in selected if anchor}
        page_urls: list[str] = []
        for page, _ in selected:
            if page not in page_urls:
                page_urls.append(page)
    else:
        # No index of issues: the page we fetched is the list.
        anchors, page_urls = set(), [url]

    issues: list[tuple[str, str]] = []
    for page in page_urls:
        if page not in pages:
            pages[page] = _get_text(client, page)
        sections = _sections(pages[page])
        matched = [(h, b) for h, b in sections if _anchor(h) in anchors]
        if not matched:
            if anchors:
                # The index and the page disagree about how issues are named,
                # which means the recency ordering is now a guess. Say so: the
                # quiet version of this reads the same age of issue forever.
                _LOG.warning(
                    "curated: no heading in %s matches the index; falling back "
                    "to page order, which assumes newest first",
                    page,
                )
            matched = sections[:max_issues] if max_issues else sections
        issues.extend(matched)

    if max_issues:
        issues = issues[:max_issues]

    ids: list[str] = []
    others: list[str] = []
    for _, body in issues:
        for link in _paper_links(body, label):
            found = _ARXIV_URL.search(link)
            if found:
                arxiv_id = strip_arxiv_version(found.group(1))
                if arxiv_id not in ids:
                    ids.append(arxiv_id)
            elif link not in others:
                others.append(link)
    return ids, others, [heading for heading, _ in issues]


def collect(
    cfg: Config,
    topics: list[Topic],
    since: date,
    store: RecordStore | None = None,
    client: Client | None = None,
    errors: list[str] | None = None,
) -> list[Paper]:
    """Fetch the configured curated lists and return what they point at.

    Not called per topic: the list is the same whoever is asking, so it is read
    once and scored against every topic afterwards.
    """
    block = cfg.sources.get("curated", {}) or {}
    if not block.get("enabled", True):
        return []

    lists = [entry for entry in (block.get("lists") or []) if entry.get("url")]
    if not lists:
        return []
    if not [t for t in topics if t.source_enabled("curated")]:
        return []

    injected = client
    client = client or from_settings(
        cfg.settings,
        min_interval_s=float(block.get("min_request_interval_s", 1.0)),
    )
    max_issues = int(block.get("max_issues", 4) or 0)
    label = str(block.get("link_label", "Paper") or "Paper")

    picks: list[str] = []
    for entry in lists:
        name = str(entry.get("name") or entry.get("url"))
        try:
            ids, others, issues = _read_list(
                client, str(entry["url"]), max_issues, label
            )
        except HTTPError as exc:
            _LOG.error("curated list '%s' unreachable: %s", name, exc)
            if errors is not None:
                errors.append(f"curated[{name}]: {exc}")
            continue

        if not ids:
            # A curated list that parses to nothing is the failure mode this
            # collector is most exposed to: the page is one editor's markdown
            # and its shape can change without notice. A zero is never quiet.
            _LOG.warning(
                "curated list '%s' yielded no arXiv links across %d issue(s); "
                "the page format may have changed",
                name,
                len(issues),
            )
        else:
            _LOG.info(
                "curated list '%s': %d pick(s) across %d issue(s)",
                name,
                len(ids),
                len(issues),
            )
        for link in others:
            # Not a loss to swallow: these are the picks that are blog posts,
            # journal pages or project sites. There is nowhere to read a
            # bibliography from, so they are named here and left to a human.
            _LOG.info(
                "curated: '%s' picked %s, which carries no arXiv id -- drop it "
                "in inbox/ by hand if the group wants it",
                name,
                link,
            )
        for arxiv_id in ids:
            if arxiv_id not in picks:
                picks.append(arxiv_id)

    if not picks:
        return []

    # A pick already in the archive needs no lookup; re-emitting the stored
    # record is what stamps `+curated` onto it through the ordinary merge.
    held: list[Paper] = []
    lookup: list[str] = []
    for arxiv_id in picks:
        record = store.load_paper(f"arxiv:{arxiv_id}") if store is not None else None
        if record is None:
            lookup.append(arxiv_id)
        else:
            record.source = "curated"
            held.append(record)

    fetched: list[Paper] = []
    if lookup:
        fetched = arxiv.fetch_by_id(
            cfg, lookup, client=injected, errors=errors, source="curated"
        )
        resolved = {paper.id for paper in fetched}
        missing = [i for i in lookup if f"arxiv:{i}" not in resolved]
        if missing:
            # The pick is real and the id is known; only the metadata is out of
            # reach. Recording it from the list's own nickname is the one thing
            # this collector will not do, so it is a gap, and it is reported.
            _LOG.warning(
                "curated: %d pick(s) could not be resolved on arXiv and were "
                "skipped: %s",
                len(missing),
                ", ".join(missing[:10]),
            )

    _LOG.info(
        "curated: %d new, %d already held", len(fetched), len(held)
    )
    return fetched + held
