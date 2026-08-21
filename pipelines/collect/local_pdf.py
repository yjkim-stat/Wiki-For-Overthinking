"""Local PDF collector.

The one collector whose source is a person. A PDF dropped into ``inbox/`` is
ingested on the next run: it is hashed, moved into ``data/pdfs/`` under a
content-addressed name, and recorded like any other paper.

Nothing here opens the PDF. Extracting a title, an abstract or a year from a PDF
in pure Python means shipping a parser that is wrong often enough to poison the
archive quietly, and this repository already has a reader that is good at
documents — the session that drains the queue. So the collector records only
what the filesystem can tell it, and the task it files asks whoever answers it
to read the document and supply the bibliography.

Two consequences follow, and both are deliberate:

* **Identity is the file's content**, not its name. Dropping the same PDF twice
  under two names produces one record, and renaming a file before dropping it
  changes nothing.
* **A dropped PDF is never rejected by scoring.** Filing it by hand *is* the
  editorial decision that scoring exists to approximate, so ``run_daily`` keeps
  a local paper whatever its keywords say. Scoring still runs, because the
  topics it matches are worth recording.
"""

from __future__ import annotations

import hashlib
import re
import shutil
from datetime import date
from pathlib import Path

from ..common.config import Config, Topic
from ..common.log import get
from ..common.paths import fs_id
from ..common.schema import Paper

_LOG = get(__name__)

SOURCE = "local"

_FILENAME_NOISE = re.compile(r"[_\-]+")
_WS = re.compile(r"\s+")
_CHUNK = 1 << 20


def content_id(path: Path) -> str:
    """Content-addressed id for a PDF, so identity survives a rename."""
    digest = hashlib.sha1()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(_CHUNK), b""):
            digest.update(chunk)
    return f"{SOURCE}:{digest.hexdigest()[:16]}"


def title_from_filename(path: Path) -> str:
    """Provisional title, replaced by the real one once the PDF is read."""
    stem = _FILENAME_NOISE.sub(" ", path.stem)
    return _WS.sub(" ", stem).strip() or path.name


def _stored_path(cfg: Config, paper_id: str) -> Path:
    return cfg.layout.pdfs / f"{fs_id(paper_id)}.pdf"


def _relative(cfg: Config, path: Path) -> str:
    try:
        return path.relative_to(cfg.layout.root).as_posix()
    except ValueError:
        return path.as_posix()


def collect(
    cfg: Config,
    topics: list[Topic],
    since: date | None = None,
    *,
    dry_run: bool = False,
    errors: list[str] | None = None,
) -> list[Paper]:
    """Ingest every PDF waiting in the inbox.

    ``topics`` and ``since`` are accepted for symmetry with the other
    collectors and deliberately ignored: a file someone put in the inbox today
    is new by definition, and it is kept whether or not it matches a topic.

    ``dry_run`` reports what would be ingested and leaves the inbox untouched.
    This is the only collector for which a dry run means anything beyond "do
    not store": the others read a remote index, while this one moves a file
    someone still expects to find where they put it.
    """
    if not (cfg.sources.get(SOURCE, {}) or {}).get("enabled", True):
        _LOG.debug("local pdf collection disabled")
        return []

    inbox = cfg.layout.inbox
    if not inbox.is_dir():
        return []

    found: list[Paper] = []
    for path in sorted(inbox.rglob("*")):
        if not path.is_file() or path.suffix.lower() != ".pdf":
            continue
        try:
            found.append(_ingest(cfg, path, dry_run=dry_run))
        except OSError as exc:
            _LOG.warning("could not ingest %s: %s", path.name, exc)
            if errors is not None:
                errors.append(f"local: {path.name}: {exc}")

    if found:
        _LOG.info(
            "%s %d PDF(s) in %s",
            "would ingest" if dry_run else "ingested",
            len(found),
            _relative(cfg, inbox),
        )
    return found


def _ingest(cfg: Config, path: Path, *, dry_run: bool = False) -> Paper:
    paper_id = content_id(path)
    target = _stored_path(cfg, paper_id)

    if not dry_run:
        target.parent.mkdir(parents=True, exist_ok=True)
        # `move` rather than `copy`: the inbox must drain, or the next run
        # ingests the same file again. An identical file already in place is
        # the same bytes by construction, so replacing it loses nothing.
        shutil.move(str(path), str(target))

    return Paper(
        id=paper_id,
        title=title_from_filename(path),
        source=SOURCE,
        source_id=path.name,
        local_path=_relative(cfg, target),
    )
