"""Fetch the PDF of a paper that is about to be read.

An abstract is a claim about a paper, not a record of it. Reading bodies rather
than abstracts overturned substantive findings in a live archive — a transfer
result that only holds below a capacity threshold, a headline that is worse than
baseline on three of five real tasks, a "1 FPS, 16 frames of memory" limitation
absent from an abstract that reads as an interactive simulator. Measured there:
**38% of records built from abstracts had an empty `results` field**, because
the abstract carried no numbers to record.

So a paper that has cleared scoring and is about to be queued gets its PDF
fetched, and the task carries the path — exactly as a hand-filed PDF already
does. The two paths converge: whatever a paper's provenance, if there is a
document on disk the reader is told where it is.

**Nothing here opens the file.** That is `local_pdf`'s rule and it holds for the
same reason: extracting a title or a year from a PDF in pure Python means
shipping a parser that is wrong often enough to poison the archive quietly. Nor
is the text extracted and cached — this repository's reader reads documents, so
handing it the document preserves the figures and tables, which usually settle
what a paper achieved faster than the prose does. There is no external
extractor, and therefore no dependency to install and nothing to degrade to.

Failure is ordinary. No `pdf_url`, an unreachable host, a paywalled venue: the
paper keeps its abstract-only task and the run carries on. Roughly one paper in
twelve has no obtainable PDF, and that is a normal outcome rather than an error.
"""

from __future__ import annotations

from ..common.config import Config
from ..common.http import Client, HTTPError, from_settings
from ..common.log import get
from ..common.paths import fs_id
from ..common.schema import Paper

_LOG = get(__name__)

# A PDF that is not a PDF is a login page or an interstitial. Storing it would
# hand the reader a document that says nothing about the paper.
_MAGIC = b"%PDF-"


def _settings(cfg: Config) -> dict:
    return (cfg.settings.get("collect", {}) or {}).get("pdfs", {}) or {}


def client_for(cfg: Config) -> Client:
    """A slower client than the metadata one.

    PDF hosts are the same hosts the metadata APIs throttle, and a body is a
    much larger ask than a query. The interval is separate and slower so that
    fetching documents cannot spend the politeness budget the queries need.
    """
    block = _settings(cfg)
    return from_settings(
        cfg.settings,
        min_interval_s=float(block.get("min_request_interval_s", 5.0)),
    )


class Budget:
    """How many documents a run may still fetch.

    The cap in settings is per *run*, and a run fetches one paper at a time —
    collection calls ``fetch_for`` with a single paper as it files that paper's
    task. A counter local to the call therefore started again on every paper and
    bounded nothing. Handing the same budget to every call is what makes "per
    run" mean the run.

    A caller that passes none gets a fresh one, which is one call's worth. That
    is the only reading under which the old behaviour was correct, so it is the
    one the default keeps.
    """

    def __init__(self, limit: int) -> None:
        # 0 means fetch nothing, as it always has. A negative cap is treated the
        # same rather than as unlimited: a bound that switches off by going
        # below zero is not one anybody can reason about.
        self.limit = max(0, int(limit))
        self.spent = 0

    @classmethod
    def from_settings(cls, cfg: Config) -> "Budget":
        return cls(int(_settings(cfg).get("max_per_run", 40)))

    @property
    def exhausted(self) -> bool:
        return self.spent >= self.limit

    def charge(self) -> None:
        self.spent += 1


def fetch_for(
    cfg: Config,
    papers: list[Paper],
    client: Client | None = None,
    errors: list[str] | None = None,
    budget: Budget | None = None,
) -> dict[str, int]:
    """Download a PDF for each paper that has one and does not already.

    Mutates ``paper.local_path`` in place; the caller saves. Returns counts.

    ``budget`` bounds the run rather than this call — see ``Budget``.
    """
    block = _settings(cfg)
    counts = {"fetched": 0, "skipped": 0, "failed": 0}
    if not block.get("enabled", True):
        return counts

    budget = budget if budget is not None else Budget.from_settings(cfg)
    client = client or client_for(cfg)

    for paper in papers:
        if budget.exhausted:
            counts["skipped"] += 1
            continue
        # A hand-filed PDF is already on disk, and its file is the original.
        if paper.local_path:
            continue
        url = (paper.pdf_url or "").strip()
        if not url:
            counts["skipped"] += 1
            continue

        target = cfg.layout.pdfs / f"{fs_id(paper.id)}.pdf"
        if target.exists():
            paper.local_path = _relative(cfg, target)
            continue

        try:
            body = client.get(url)
        except HTTPError as exc:
            # Unreachable, paywalled, or the host has been given up on. The
            # paper keeps its abstract and the reader is told nothing false.
            _LOG.debug("no PDF for %s: %s", paper.id, exc)
            counts["failed"] += 1
            if errors is not None:
                errors.append(f"pdf[{paper.id}]: {exc}")
            continue

        if not body.startswith(_MAGIC):
            _LOG.debug("%s served something that is not a PDF; skipping", url)
            counts["failed"] += 1
            continue

        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(body)
        paper.local_path = _relative(cfg, target)
        counts["fetched"] += 1
        budget.charge()

    if counts["fetched"] or counts["failed"]:
        _LOG.info("pdfs: %s", counts)
    return counts


def _relative(cfg: Config, path) -> str:
    try:
        return path.relative_to(cfg.layout.root).as_posix()
    except ValueError:
        return path.as_posix()
