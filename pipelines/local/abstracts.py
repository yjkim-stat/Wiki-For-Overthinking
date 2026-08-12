"""Fetch an abstract for a record whose index carried none.

DBLP is a bibliographic index: authors, venue, year, DOI, and no abstract at
all. Everything downstream assumes the abstract is there, and scoring most of
all — a title hit is weighted 3.0 and an abstract hit 1.0, and `min_score: 0.35`
means "in the title once, or in the abstract twice". A record with no abstract
cannot reach the second of those, so whether a paper is archived depends on
which index happened to find it first. That is not a threshold that can be tuned
around, because the two populations are being measured differently.

The reader pays too. A task file is meant to be self-contained; for these it
contained a title, and answering one meant leaving the queue to find the paper
by hand.

This is *not* superseded by the template's `collect/pdf_fetch.py`. That fetches
the document so the reader gets the paper rather than a claim about it, and it
says so itself: on failure "the paper keeps its abstract-only task". It never
fills `abstract`, and `abstract` is what the scorer reads. The two solve
different problems and both are wanted — one feeds the reader, this one feeds
the scorer, and the scorer runs first.

See `docs/commit-local/0023-a-title-is-not-enough-to-score-a-paper.md`.
"""

from __future__ import annotations

import os
import re

from ..common import html as html_mod
from ..common.config import Config
from ..common.http import Client, HTTPError
from ..common.log import get
from ..common.schema import Paper

_LOG = get(__name__)

# The ACL Anthology DOI prefix. Its suffix *is* the Anthology identifier, so the
# page URL is derivable without a lookup — which is why this venue gets a
# resolver of its own rather than going through the general one.
_ACL_DOI_PREFIX = "10.18653/"

# `html.abstract_block` returns the block including its own "Abstract" heading,
# because the heading is inside the labelled card. Strip the label, not the text.
_LEADING_LABEL = re.compile(r"^\s*abstract\b[:.\s]*", re.IGNORECASE)


def _acl(doi: str, client: Client, base_url: str) -> str:
    # DBLP reports DOIs uppercased — "10.18653/V1/2026.ACL-LONG.1034". A DOI is
    # case-insensitive by spec, so that is valid of DBLP, and an Anthology URL
    # *path* is not: the uppercase form 404s. The first version of this omitted
    # the lowercasing and did not fail loudly — every ACL paper simply fell
    # through to the general resolver, filling 16 of 60 instead of erroring.
    anthology_id = doi.lower().split("/")[-1]
    if not anthology_id:
        return ""
    raw = client.get(f"{base_url.rstrip('/')}/{anthology_id}/")
    page = raw.decode("utf-8", errors="replace") if isinstance(raw, bytes) else str(raw)
    return _LEADING_LABEL.sub("", html_mod.abstract_block(page)).strip()


def _semantic_scholar(doi: str, client: Client, headers: dict[str, str]) -> str:
    data = client.get_json(
        f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}",
        {"fields": "abstract"},
        headers=headers,
    )
    return str((data or {}).get("abstract") or "").strip()


def fill_missing(
    cfg: Config,
    papers: list[Paper],
    client: Client,
    errors: list[str] | None = None,
) -> int:
    """Fetch an abstract for every paper here that arrived without one.

    Best-effort, like every other query in the collectors: a lookup that fails
    leaves the abstract empty, which is exactly the state before the attempt.
    """
    block = (cfg.sources.get("conferences", {}) or {}).get("abstracts", {}) or {}
    if not block.get("enabled", True):
        return 0

    missing = [p for p in papers if not (p.abstract or "").strip() and p.doi]
    if not missing:
        return 0

    # Each lookup is one throttled request, so this is the slowest step in a
    # run. The cap bounds a single run rather than the backlog: what is not
    # filled today is still missing tomorrow and gets another attempt, and the
    # backlog only grows by a day's collection at a time.
    cap = int(block.get("max_lookups", 100))
    if len(missing) > cap:
        _LOG.info(
            "%d paper(s) need an abstract; fetching %d this run", len(missing), cap
        )
        missing = missing[:cap]

    acl_url = block.get("acl_anthology_url", "https://aclanthology.org")
    headers: dict[str, str] = {}
    key_env = (
        (cfg.sources.get("conferences", {}) or {}).get("semantic_scholar", {}) or {}
    ).get("api_key_env", "SEMANTIC_SCHOLAR_API_KEY")
    api_key = os.environ.get(key_env, "")
    if api_key:
        headers["x-api-key"] = api_key

    filled = failures = 0
    last_error: Exception | None = None
    for paper in missing:
        resolvers = []
        if paper.doi.lower().startswith(_ACL_DOI_PREFIX):
            resolvers.append(lambda p=paper: _acl(p.doi, client, acl_url))
        resolvers.append(lambda p=paper: _semantic_scholar(p.doi, client, headers))

        for resolve in resolvers:
            try:
                abstract = resolve()
            except HTTPError as exc:
                last_error = exc
                continue
            except Exception as exc:  # noqa: BLE001 - one paper must not sink the run
                _LOG.debug("abstract lookup for %s raised: %s", paper.id, exc)
                last_error = exc
                continue
            if abstract:
                paper.abstract = abstract
                filled += 1
                break
        else:
            failures += 1

    if filled:
        _LOG.info("filled in %d missing abstract(s)", filled)
    if failures:
        _LOG.warning("could not find an abstract for %d paper(s)", failures)
    # Only a total failure is worth the run's error list: partial misses are
    # normal, since not every venue publishes an abstract anywhere machine
    # readable.
    if errors is not None and missing and failures == len(missing):
        errors.append(f"abstracts: all {failures} lookup(s) failed: {last_error}")
    return filled
