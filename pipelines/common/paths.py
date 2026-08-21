"""Filesystem layout.

Every directory the pipeline touches is derived here so that the rest of the
code never joins paths by hand.

Two roots, and telling them apart is the whole of this module. **The code root**
is this checkout — where `pipelines/` and the templates it ships live. **The
deployment root** is the tree an archive accumulates in: `config/`, `data/`,
`wiki/`, `archive/`, `outputs/`, `inbox/`. They are the same directory when the
repository is run in place, and different ones when a checkout is pointed at an
archive kept in its own repository, which is what `--root` and `RA_WM_ROOT` are
for.
"""

from __future__ import annotations

import os
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

CONFIG_DIR = REPO_ROOT / "config"
TOPICS_DIR = CONFIG_DIR / "topics"
SETTINGS_FILE = CONFIG_DIR / "settings.yaml"
SOURCES_FILE = CONFIG_DIR / "sources.yaml"

# the `model` kind is this deployment's fourth entity kind, and the
# single source of truth for what kinds exist.
WIKI_KINDS = ("concept", "method", "dataset", "model")

#: Names the deployment root for every entry point at once, so a session that
#: exports it does not have to remember `--root` on each command -- and, more
#: to the point, cannot forget it on one of them.
ROOT_ENV = "RA_WM_ROOT"


class RootError(Exception):
    """The deployment root was named but is not there."""


def resolve_root(explicit: Path | None = None) -> Path | None:
    """The deployment root: the flag, then the environment, then this checkout.

    ``None`` means this checkout, which is what every caller already did before
    the environment variable existed.

    A root named but absent raises rather than falling back. The failure it
    prevents is the quiet one: a typo in `RA_WM_ROOT` would otherwise resolve to
    this checkout and write somebody's archive into the code repository, which
    looks like a successful run at every step.
    """
    if explicit is not None:
        return explicit
    named = os.environ.get(ROOT_ENV, "").strip()
    if not named:
        return None
    root = Path(named).expanduser()
    if not root.is_dir():
        raise RootError(f"{ROOT_ENV} is set to {root}, which is not a directory")
    return root


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
        # Where the templates that ship with the code are. Identical to
        # `templates` when the repository is run in place; the fallback behind
        # it when a checkout is pointed at a deployment elsewhere.
        self.code_templates = REPO_ROOT / "templates"
        # Drop folder for PDFs filed by hand. Outside `data/` because it is an
        # inbox, not a record: everything in it is on its way somewhere else.
        self.inbox = self.root / paths.get("inbox", "inbox")

    @property
    def template_dirs(self) -> list[Path]:
        """Where to look for a template, nearest first.

        The deployment's own directory, then the one the code ships. Resolved
        per file rather than per directory, so a deployment that overrides one
        template keeps receiving every other one from the code it pulls —
        copying the whole directory to change a heading is how a deployment
        stops getting improvements without noticing.

        One entry when the repository is run in place, which is the case the
        rest of the code was written against.
        """
        dirs = [self.templates]
        if self.code_templates != self.templates:
            dirs.append(self.code_templates)
        return dirs

    # -- data ---------------------------------------------------------------
    @property
    def raw(self) -> Path:
        return self.data / "raw"

    @property
    def pdfs(self) -> Path:
        """Documents waiting to be read.

        A PDF lands here on ingest — hand-filed from the inbox, or fetched for a
        paper about to be queued — and leaves for `pdfs_read` once its reading
        has been applied. What is in this directory is the backlog, visible
        without consulting the queue.
        """
        return self.data / "pdfs"

    @property
    def pdfs_read(self) -> Path:
        """Documents whose reading is done.

        A subdirectory of `pdfs` rather than a sibling, so it inherits that
        directory's gitignore entry. These files are the heaviest thing the
        pipeline touches and the cost of one deployment forgetting to ignore a
        new top-level directory is a repository nobody can clone.
        """
        return self.pdfs / "read"

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
    def findings(self) -> Path:
        """What the group settled, as against what its sources said."""
        return self.data / "findings"

    @property
    def references(self) -> Path:
        """Pages checked outside the archive, cited by findings.

        A sibling of `findings` rather than of `papers`, because neither of them
        arrived from a collector and neither is evidence for a wiki entity.
        Keeping these out of `papers/` is what stops a blog post from reaching a
        promotion threshold, a paper count or a topic rollup.
        """
        return self.data / "references"

    # -- requests -----------------------------------------------------------
    @property
    def requests(self) -> Path:
        """Where somebody who is not the archive's owner asks for a change.

        Outside `data/` because nothing in it is a record yet, and a sibling of
        `inbox/` rather than a part of it: a PDF in the inbox is an editorial
        decision already taken, and everything here is a decision still to be
        made by a person.
        """
        return self.root / "requests"

    @property
    def requests_pending(self) -> Path:
        return self.requests / "pending"

    @property
    def requests_approved(self) -> Path:
        return self.requests / "approved"

    @property
    def requests_rejected(self) -> Path:
        return self.requests / "rejected"

    @property
    def requests_done(self) -> Path:
        return self.requests / "done"

    # -- candidates ----------------------------------------------------------

    @property
    def candidates(self) -> Path:
        """A third drop lane, beside `inbox/` and `requests/`.

        What collection finds outside the literature — a repository, today —
        and nobody has yet decided about. It is not under `data/` because it is
        not a record: `data/` holds what arrived from a collector as literature
        or was derived from it, and a candidate is neither until a person
        promotes it. See `pipelines/candidates.py` for why the decision cannot
        be made by the collector.
        """
        return self.root / "candidates"

    @property
    def candidates_pending(self) -> Path:
        return self.candidates / "pending"

    @property
    def candidates_promoted(self) -> Path:
        return self.candidates / "promoted"

    @property
    def candidates_dropped(self) -> Path:
        return self.candidates / "dropped"

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
            self.pdfs_read,
            self.inbox,
            self.papers,
            self.videos,
            self.summaries / "papers",
            self.summaries / "videos",
            self.concepts,
            self.findings,
            self.references,
            self.requests_pending,
            self.requests_approved,
            self.requests_rejected,
            self.requests_done,
            self.candidates_pending,
            self.candidates_promoted,
            self.candidates_dropped,
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
            self.wiki_kind_dir("model"),  # LOCAL
            self.out_lecture_notes,
            self.out_slides,
            self.out_reports,
        ):
            directory.mkdir(parents=True, exist_ok=True)
