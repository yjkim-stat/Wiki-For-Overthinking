"""Filesystem layout.

Every directory the pipeline touches is derived here so that the rest of the
code never joins paths by hand.
"""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

CONFIG_DIR = REPO_ROOT / "config"
TOPICS_DIR = CONFIG_DIR / "topics"
SETTINGS_FILE = CONFIG_DIR / "settings.yaml"
SOURCES_FILE = CONFIG_DIR / "sources.yaml"

_SLUG_STRIP = re.compile(r"[^a-z0-9]+")


def slugify(text: str, max_length: int = 80) -> str:
    """Lowercase, hyphen-separated, filesystem-safe form of ``text``."""
    slug = _SLUG_STRIP.sub("-", text.strip().lower()).strip("-")
    if len(slug) > max_length:
        slug = slug[:max_length].rstrip("-")
    return slug or "untitled"


def fs_id(canonical_id: str) -> str:
    """Turn a canonical id such as ``arxiv:2401.12345v2`` into a path segment."""
    return _SLUG_STRIP.sub("-", canonical_id.strip().lower()).strip("-") or "unknown"


class Layout:
    """Resolved directories for one repository checkout.

    Built from the ``paths`` block of ``config/settings.yaml`` so the tree can
    be relocated without touching code.
    """

    def __init__(self, paths: dict | None = None, root: Path | None = None) -> None:
        paths = paths or {}
        self.root = root or REPO_ROOT
        self.data = self.root / paths.get("data", "data")
        self.archive = self.root / paths.get("archive", "archive")
        self.wiki = self.root / paths.get("wiki", "wiki")
        self.outputs = self.root / paths.get("outputs", "outputs")
        self.templates = self.root / paths.get("templates", "templates")
        # Drop folder for PDFs filed by hand. Outside `data/` because it is an
        # inbox, not a record: everything in it is on its way somewhere else.
        self.inbox = self.root / paths.get("inbox", "inbox")

    # -- data ---------------------------------------------------------------
    @property
    def raw(self) -> Path:
        return self.data / "raw"

    @property
    def pdfs(self) -> Path:
        """Where a filed PDF is kept once it has been ingested."""
        return self.data / "pdfs"

    @property
    def papers(self) -> Path:
        return self.data / "papers"

    @property
    def videos(self) -> Path:
        return self.data / "videos"

    @property
    def summaries(self) -> Path:
        return self.data / "summaries"

    @property
    def concepts(self) -> Path:
        return self.data / "concepts"

    @property
    def index(self) -> Path:
        return self.data / "index"

    @property
    def abstracts(self) -> Path:
        """Every announced paper's abstract, whether or not a topic wanted it.

        Separate from `papers/` on purpose: `papers/` is what the group tracks,
        and this is what was published. Keeping the second out of the first is
        what lets a threshold be revisited later without re-collecting.
        """
        return self.data / "abstracts"

    @property
    def logs(self) -> Path:
        return self.data / "logs"

    @property
    def seen_db(self) -> Path:
        return self.index / "seen.sqlite"

    # -- queue --------------------------------------------------------------
    @property
    def queue(self) -> Path:
        return self.data / "queue"

    @property
    def queue_pending(self) -> Path:
        return self.queue / "pending"

    @property
    def queue_done(self) -> Path:
        return self.queue / "done"

    @property
    def queue_archive(self) -> Path:
        return self.queue / "archive"

    # -- human-facing -------------------------------------------------------
    @property
    def archive_papers(self) -> Path:
        return self.archive / "papers"

    @property
    def archive_seminars(self) -> Path:
        return self.archive / "seminars"

    @property
    def archive_daily(self) -> Path:
        return self.archive / "daily"

    @property
    def wiki_meta(self) -> Path:
        return self.wiki / "_meta"

    def wiki_kind_dir(self, kind: str) -> Path:
        """Directory for a wiki note kind (``concept``, ``method``, ...)."""
        return self.wiki / f"{kind}s"

    @property
    def out_lecture_notes(self) -> Path:
        return self.outputs / "lecture-notes"

    @property
    def out_slides(self) -> Path:
        return self.outputs / "slides"

    @property
    def out_reports(self) -> Path:
        return self.outputs / "reports"

    def ensure(self) -> None:
        """Create every directory the pipeline writes to."""
        for directory in (
            self.raw,
            self.pdfs,
            self.inbox,
            self.papers,
            self.videos,
            self.summaries / "papers",
            self.summaries / "videos",
            self.concepts,
            self.abstracts,
            self.index,
            self.logs,
            self.queue_pending,
            self.queue_done,
            self.queue_archive,
            self.archive_papers,
            self.archive_seminars,
            self.archive_daily,
            self.wiki,
            self.wiki_meta,
            self.wiki_kind_dir("topic"),
            self.wiki_kind_dir("concept"),
            self.wiki_kind_dir("method"),
            self.wiki_kind_dir("dataset"),
            self.out_lecture_notes,
            self.out_slides,
            self.out_reports,
        ):
            directory.mkdir(parents=True, exist_ok=True)
