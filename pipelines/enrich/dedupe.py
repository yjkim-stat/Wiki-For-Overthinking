"""Cross-source deduplication.

The same paper arrives as an arXiv preprint, an OpenReview submission and a
DBLP proceedings entry. All three must collapse onto one record, and the
mapping has to survive across runs — which is why it lives in SQLite rather
than a per-run set.
"""

from __future__ import annotations

from ..common.log import get
from ..common.schema import Paper, Video, strip_arxiv_version, title_fingerprint
from ..common.store import RecordStore, SeenStore

_LOG = get(__name__)


def paper_keys(paper: Paper) -> list[str]:
    """Every identifier this paper could also be known by."""
    keys: list[str] = []
    if paper.arxiv_id:
        keys.append(f"arxiv:{strip_arxiv_version(paper.arxiv_id)}")
    if paper.doi:
        keys.append(f"doi:{paper.doi.strip().lower()}")
    if paper.title:
        keys.append(f"title:{title_fingerprint(paper.title)}")
    if paper.id and paper.id not in keys:
        keys.append(paper.id)
    return keys


def merge_papers(existing: Paper, incoming: Paper) -> Paper:
    """Fold ``incoming`` into ``existing``, preferring richer values.

    A venue from a proceedings entry and an abstract from arXiv both matter, so
    fields are filled in rather than overwritten. The stored record wins on
    identity; the newcomer wins only where the stored record is empty or
    thinner.
    """
    merged = Paper.from_dict(existing.to_dict())

    for field_name in ("abstract", "venue", "doi", "arxiv_id", "pdf_url", "url"):
        current = getattr(merged, field_name) or ""
        candidate = getattr(incoming, field_name) or ""
        if len(candidate) > len(current):
            setattr(merged, field_name, candidate)

    if len(incoming.authors) > len(merged.authors):
        merged.authors = incoming.authors
    if incoming.year and not merged.year:
        merged.year = incoming.year
    if incoming.published and (
        not merged.published or incoming.published < merged.published
    ):
        # The earliest sighting is the real publication date; a proceedings
        # entry should not push a preprint's date forward.
        merged.published = incoming.published
    if incoming.updated > merged.updated:
        merged.updated = incoming.updated

    for category in incoming.categories:
        if category not in merged.categories:
            merged.categories.append(category)

    if incoming.source not in merged.source.split("+"):
        merged.source = f"{merged.source}+{incoming.source}"

    # A document is not merged on richness like every field above. There is no
    # "longer" path, and the two candidates are not two descriptions of one
    # thing — they are two files.
    #
    # The stored path wins when there is one, because it may already have been
    # shelved into `data/pdfs/read/` and replacing it would point the record at
    # a file that is no longer there. Otherwise the newcomer's is taken.
    # Dropping it is what left a hand-filed PDF orphaned on disk while the
    # pipeline downloaded the same paper again, having concluded that the record
    # it had just merged held no document. `source` *is* merged, so the record
    # still read as hand-filed — it simply could not say where the file was.
    if incoming.local_path and not merged.local_path:
        merged.local_path = incoming.local_path

    merged.last_seen = incoming.last_seen
    return merged


class Deduplicator:
    """Resolves incoming records onto canonical stored ones."""

    def __init__(self, seen: SeenStore, store: RecordStore) -> None:
        self.seen = seen
        self.store = store

    def resolve_paper(self, paper: Paper) -> tuple[Paper, bool]:
        """Return ``(record, is_new)`` for ``paper``.

        ``record`` is the canonical, possibly merged paper as it should be
        stored. ``is_new`` is True only the first time the work is seen at all.
        """
        keys = paper_keys(paper)
        canonical = self.seen.canonical_for(keys) or paper.id
        is_new = canonical == paper.id and not self.seen.has(paper.id)

        existing = self.store.load_paper(canonical)
        if existing is not None:
            paper.id = canonical
            record = merge_papers(existing, paper)
            is_new = False
        else:
            paper.id = canonical
            record = paper

        for key in keys:
            self.seen.mark(
                key, kind="paper", canonical=canonical, source=paper.source
            )
        return record, is_new

    def resolve_video(self, video: Video) -> tuple[Video, bool]:
        """Videos have a single stable id, so this only tracks first sighting."""
        existing = self.store.load_video(video.id)
        is_new = self.seen.mark(
            video.id, kind="video", canonical=video.id, source=video.source
        )
        if existing is not None:
            merged = Video.from_dict(existing.to_dict())
            for field_name in ("description", "title", "channel", "url"):
                if not getattr(merged, field_name):
                    setattr(merged, field_name, getattr(video, field_name))
            merged.duration_s = merged.duration_s or video.duration_s
            merged.transcript_available = (
                merged.transcript_available or video.transcript_available
            )
            merged.transcript_chars = max(
                merged.transcript_chars, video.transcript_chars
            )
            merged.last_seen = video.last_seen
            return merged, False
        return video, is_new
