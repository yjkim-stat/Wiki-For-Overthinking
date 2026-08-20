"""Fetch documents for papers that are already waiting to be read.

    python -m pipelines.backfill [--limit N] [--topic slug] [--dry-run]

`pdf_fetch` runs inside collection, so it only ever sees papers arriving *this
run*. A paper that entered the queue before documents were fetched at all, or on
a run where its host was down, never gets another chance: collection will not
revisit it, because `seen.sqlite` remembers it, and nothing else fetches. On the
archive this was written for that is 512 unread papers with no document between
them — an entire backlog the reader has to answer from abstracts, against a rule
the archive itself recorded, that a claim resting on a figure is read from the
rendered PDF.

This is that second chance, and nothing else. It collects nothing, scores
nothing, queues nothing and reads nothing: it takes papers that already have a
task pending, asks for the document each one already names, and lets the next
render put the path in front of the reader.

**A separate command on purpose.** Collection is bounded by what a day published;
this is bounded by what the archive already owes. Running it inside `run_daily`
would put an unbounded backlog behind a daily cadence, and a slow night of
backfilling would cost a day of collection.
"""

from __future__ import annotations

import argparse
import logging
from pathlib import Path

from .collect import pdf_fetch
from .common import config as config_mod
from .common import log
from .common import paths as P
from .common.config import Config
from .common.schema import Paper
from .common.store import RecordStore
from .enrich.queue import Queue
from .enrich.score import leverage

_LOG = log.get(__name__)

ORDERINGS = ("score", "age", "id")


def _sort_key(paper: Paper, order: str):
    """Total and deterministic, whichever ordering is asked for.

    Every key ends in the id. Two papers with equal scores must not swap places
    between runs — a bound is applied after the sort, so an unstable order means
    a different set of documents is fetched each time and the backlog never
    drains in any particular direction.
    """
    if order == "age":
        # Oldest first: a task that has been waiting longest.
        return (paper.first_seen, paper.id)
    if order == "id":
        return (paper.id,)
    return (-leverage(paper), _newest_first(paper.published), paper.id)


def _newest_first(published: str) -> int:
    """An ISO date as a number that sorts descending among ascending keys.

    A paper whose date is missing or unparseable ranks 0, which puts it after
    every real date — all of which are negative — rather than at the front,
    where an empty string would have put it.
    """
    digits = published.replace("-", "")[:8]
    return -int(digits) if digits.isdigit() else 0


def candidates(
    cfg: Config,
    store: RecordStore,
    queue: Queue,
    topic_slugs: list[str] | None = None,
) -> tuple[list[Paper], int]:
    """Papers with a task pending, no document, and somewhere to get one.

    Returns them with the count of papers that are waiting and name no
    `pdf_url` either. Nothing here can reach those, and they are the input to a
    lookup asking where the document is — so the count is reported rather than
    quietly dropped, and it answers the same `--topic` as the rest.
    """
    wanted = set(topic_slugs or [])
    ready: list[Paper] = []
    unreachable = 0
    for paper in store.iter_papers():
        if wanted and not wanted & set(paper.topics):
            continue
        task = queue.pending_path(Queue.task_id("paper", paper.id))
        if not task.exists():
            continue
        if paper.local_path:
            continue
        if (paper.pdf_url or "").strip():
            ready.append(paper)
        else:
            unreachable += 1
    return ready, unreachable


def run(
    cfg: Config,
    *,
    limit: int | None = None,
    topic_slugs: list[str] | None = None,
    order: str = "score",
    dry_run: bool = False,
    client: object | None = None,
) -> dict:
    """Fetch what the backlog is owed. Returns a summary of what happened."""
    cfg.layout.ensure()
    store = RecordStore(cfg.layout)
    queue = Queue(cfg.layout)

    ready, unreachable = candidates(cfg, store, queue, topic_slugs)
    ready.sort(key=lambda p: _sort_key(p, order))

    budget = pdf_fetch.Budget(limit) if limit is not None else pdf_fetch.Budget.from_settings(cfg)
    result = {
        "waiting": len(ready) + unreachable,
        "candidates": len(ready),
        "no_pdf_url": unreachable,
        "limit": budget.limit,
        "fetched": 0,
        "failed": 0,
        "skipped": 0,
    }

    if dry_run:
        _LOG.info(
            "would fetch up to %d of %d candidate(s); %d waiting paper(s) name no PDF",
            budget.limit,
            len(ready),
            unreachable,
        )
        for paper in ready[: budget.limit]:
            _LOG.info("  %-28s %.2f  %s", paper.id, leverage(paper), paper.title[:60])
        return result

    errors: list[str] = []
    # One client for the whole pass, so its throttle and its give-up circuit
    # apply across the backlog rather than being rebuilt for each paper.
    client = client or pdf_fetch.client_for(cfg)
    for paper in ready:
        if budget.exhausted:
            break
        before = paper.local_path
        counts = pdf_fetch.fetch_for(cfg, [paper], client, errors=errors, budget=budget)
        result["fetched"] += counts["fetched"]
        result["failed"] += counts["failed"]
        result["skipped"] += counts["skipped"]
        # Saved one at a time rather than in a batch at the end: a run that is
        # interrupted has still kept every document it paid for, and a re-run
        # skips them. Nothing here is transactional and nothing needs to be.
        if paper.local_path and paper.local_path != before:
            store.save_paper(paper)

    result["errors"] = errors
    _LOG.info("backfill: %s", {k: v for k, v in result.items() if k != "errors"})
    if unreachable:
        _LOG.info(
            "%d waiting paper(s) name no PDF at all; nothing here can reach those",
            unreachable,
        )
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m pipelines.backfill",
        description="Fetch documents for papers already waiting to be read.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="how many documents to fetch (default: collect.pdfs.max_per_run)",
    )
    parser.add_argument(
        "--topic", action="append", dest="topics", help="restrict to a topic slug"
    )
    parser.add_argument(
        "--by",
        choices=ORDERINGS,
        default="score",
        dest="order",
        help="which of the backlog to spend the limit on (default: score)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="list what would be fetched and request nothing",
    )
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help=f"deployment root: the tree the archive lives in (default: ${P.ROOT_ENV}, "
        "else this checkout)",
    )
    args = parser.parse_args(argv)

    cfg = config_mod.load(args.root)
    log.setup(cfg.layout.logs, logging.DEBUG if args.verbose else logging.INFO)
    run(
        cfg,
        limit=args.limit,
        topic_slugs=args.topics,
        order=args.order,
        dry_run=args.dry_run,
    )
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
