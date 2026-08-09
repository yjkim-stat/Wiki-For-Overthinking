"""Persistence.

``data/`` is the single source of truth. Everything under ``archive/``,
``wiki/`` and ``outputs/`` is regenerated from it, so a change to the rendering
or summarizing logic never requires re-collecting anything.
"""

from __future__ import annotations

import json
import os
import sqlite3
import tempfile
from pathlib import Path
from typing import Any, Iterable, Iterator

from .paths import Layout, fs_id
from .schema import Concept, Paper, PaperSummary, Video, VideoSummary, utcnow


# ---------------------------------------------------------------------------
# JSON helpers
# ---------------------------------------------------------------------------


def write_json(path: Path, data: Any) -> None:
    """Write JSON atomically, so an interrupted run never leaves half a file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, tmp_name = tempfile.mkstemp(dir=str(path.parent), suffix=".tmp")
    try:
        with os.fdopen(handle, "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False, indent=2, sort_keys=True)
            fh.write("\n")
        os.replace(tmp_name, path)
    except BaseException:
        Path(tmp_name).unlink(missing_ok=True)
        raise


def read_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return default


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8")


def read_jsonl(path: Path) -> Iterator[dict]:
    if not path.exists():
        return
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                try:
                    yield json.loads(line)
                except json.JSONDecodeError:
                    continue


def append_jsonl(path: Path, rows: Iterable[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def rewrite_jsonl(path: Path, rows: Iterable[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, tmp_name = tempfile.mkstemp(dir=str(path.parent), suffix=".tmp")
    try:
        with os.fdopen(handle, "w", encoding="utf-8") as fh:
            for row in rows:
                fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
        os.replace(tmp_name, path)
    except BaseException:
        Path(tmp_name).unlink(missing_ok=True)
        raise


# ---------------------------------------------------------------------------
# Seen-state
# ---------------------------------------------------------------------------


class SeenStore:
    """Tracks which items have already been processed.

    Deduplication has to survive across runs and across sources, so it lives in
    SQLite rather than in a rebuilt-every-time in-memory set.
    """

    _SCHEMA = """
    CREATE TABLE IF NOT EXISTS seen (
        key         TEXT PRIMARY KEY,
        kind        TEXT NOT NULL,
        canonical   TEXT NOT NULL,
        source      TEXT NOT NULL DEFAULT '',
        first_seen  TEXT NOT NULL,
        last_seen   TEXT NOT NULL
    );
    CREATE INDEX IF NOT EXISTS seen_canonical ON seen (canonical);
    """

    def __init__(self, db_path: Path) -> None:
        db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(db_path))
        self.conn.executescript(self._SCHEMA)
        self.conn.commit()

    def __enter__(self) -> "SeenStore":
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()

    def has(self, key: str) -> bool:
        cur = self.conn.execute("SELECT 1 FROM seen WHERE key = ?", (key,))
        return cur.fetchone() is not None

    def canonical_for(self, keys: Iterable[str]) -> str | None:
        """Return the canonical id already associated with any of ``keys``."""
        keys = [k for k in keys if k]
        if not keys:
            return None
        placeholders = ",".join("?" * len(keys))
        cur = self.conn.execute(
            f"SELECT canonical FROM seen WHERE key IN ({placeholders}) LIMIT 1",
            tuple(keys),
        )
        row = cur.fetchone()
        return row[0] if row else None

    def mark(
        self, key: str, *, kind: str, canonical: str, source: str = ""
    ) -> bool:
        """Record ``key``. Returns True the first time it is seen."""
        now = utcnow()
        cur = self.conn.execute(
            "UPDATE seen SET last_seen = ?, canonical = ? WHERE key = ?",
            (now, canonical, key),
        )
        if cur.rowcount:
            return False
        self.conn.execute(
            "INSERT INTO seen (key, kind, canonical, source, first_seen, last_seen)"
            " VALUES (?, ?, ?, ?, ?, ?)",
            (key, kind, canonical, source, now, now),
        )
        return True

    def commit(self) -> None:
        self.conn.commit()

    def close(self) -> None:
        self.conn.commit()
        self.conn.close()


# ---------------------------------------------------------------------------
# Record stores
# ---------------------------------------------------------------------------


class RecordStore:
    """Reads and writes the normalized records under ``data/``."""

    # Transcripts live beside the video records they belong to, so their names
    # match the same `*.json` glob. The suffix is defined once and both
    # `transcript_path` and `iter_videos` are derived from it, so the writer
    # and the reader cannot drift apart.
    TRANSCRIPT_SUFFIX = ".transcript.json"

    def __init__(self, layout: Layout) -> None:
        self.layout = layout

    # -- papers -------------------------------------------------------------
    def paper_path(self, paper_id: str) -> Path:
        return self.layout.papers / f"{fs_id(paper_id)}.json"

    def save_paper(self, paper: Paper) -> Path:
        path = self.paper_path(paper.id)
        write_json(path, paper.to_dict())
        return path

    def load_paper(self, paper_id: str) -> Paper | None:
        data = read_json(self.paper_path(paper_id))
        return Paper.from_dict(data) if data else None

    def iter_papers(self) -> Iterator[Paper]:
        for path in sorted(self.layout.papers.glob("*.json")):
            data = read_json(path)
            if data:
                yield Paper.from_dict(data)

    # -- videos -------------------------------------------------------------
    def video_path(self, video_id: str) -> Path:
        return self.layout.videos / f"{fs_id(video_id)}.json"

    def save_video(self, video: Video) -> Path:
        path = self.video_path(video.id)
        write_json(path, video.to_dict())
        return path

    def load_video(self, video_id: str) -> Video | None:
        data = read_json(self.video_path(video_id))
        return Video.from_dict(data) if data else None

    def iter_videos(self) -> Iterator[Video]:
        for path in sorted(self.layout.videos.glob("*.json")):
            if path.name.endswith(self.TRANSCRIPT_SUFFIX):
                continue
            data = read_json(path)
            # A record is an object. Anything else in this directory is not one
            # of ours, and skipping it beats taking down every entry point.
            if isinstance(data, dict) and data:
                yield Video.from_dict(data)

    # -- abstracts ----------------------------------------------------------
    def abstracts_path(self, category: str, day: str) -> Path:
        """One file per category-day, so a gap can be filled without a rewrite."""
        safe_day = fs_id(day or "undated")
        return self.layout.abstracts / fs_id(category) / f"{safe_day}.jsonl"

    def load_abstracts(self, category: str, day: str) -> dict[str, dict]:
        return {
            str(row.get("id", "")): row
            for row in read_jsonl(self.abstracts_path(category, day))
            if row.get("id")
        }

    def save_abstracts(self, category: str, day: str, rows: Iterable[dict]) -> int:
        """Merge ``rows`` into the day's file. Returns how many are held after.

        A row is only replaced by one that carries an abstract it lacked. The
        listing pass files every announced identifier with an empty abstract --
        that is what makes the file the day's identifier list as well as its
        abstract store -- and the backfill pass fills them in later.
        """
        held = self.load_abstracts(category, day)
        for row in rows:
            identifier = str(row.get("id", ""))
            if not identifier:
                continue
            existing = held.get(identifier)
            if existing is None:
                held[identifier] = row
            elif not str(existing.get("abstract", "")).strip():
                held[identifier] = {**existing, **row}
        rewrite_jsonl(
            self.abstracts_path(category, day),
            [held[k] for k in sorted(held)],
        )
        return len(held)

    # -- transcripts --------------------------------------------------------
    def transcript_path(self, video_id: str) -> Path:
        return self.layout.videos / f"{fs_id(video_id)}{self.TRANSCRIPT_SUFFIX}"

    def save_transcript(self, video_id: str, segments: list[dict]) -> Path:
        path = self.transcript_path(video_id)
        write_json(path, segments)
        return path

    def load_transcript(self, video_id: str) -> list[dict]:
        return read_json(self.transcript_path(video_id), default=[]) or []

    # -- summaries ----------------------------------------------------------
    def paper_summary_path(self, paper_id: str) -> Path:
        return self.layout.summaries / "papers" / f"{fs_id(paper_id)}.json"

    def save_paper_summary(self, summary: PaperSummary) -> Path:
        path = self.paper_summary_path(summary.paper_id)
        write_json(path, summary.to_dict())
        return path

    def load_paper_summary(self, paper_id: str) -> PaperSummary | None:
        data = read_json(self.paper_summary_path(paper_id))
        return PaperSummary.from_dict(data) if data else None

    def video_summary_path(self, video_id: str) -> Path:
        return self.layout.summaries / "videos" / f"{fs_id(video_id)}.json"

    def save_video_summary(self, summary: VideoSummary) -> Path:
        path = self.video_summary_path(summary.video_id)
        write_json(path, summary.to_dict())
        return path

    def load_video_summary(self, video_id: str) -> VideoSummary | None:
        data = read_json(self.video_summary_path(video_id))
        return VideoSummary.from_dict(data) if data else None

    # -- concepts -----------------------------------------------------------
    def concept_path(self, slug: str) -> Path:
        return self.layout.concepts / f"{slug}.json"

    def save_concept(self, concept: Concept) -> Path:
        path = self.concept_path(concept.slug)
        write_json(path, concept.to_dict())
        return path

    def load_concept(self, slug: str) -> Concept | None:
        data = read_json(self.concept_path(slug))
        return Concept.from_dict(data) if data else None

    def iter_concepts(self) -> Iterator[Concept]:
        for path in sorted(self.layout.concepts.glob("*.json")):
            data = read_json(path)
            if data:
                yield Concept.from_dict(data)

    # -- indexes ------------------------------------------------------------
    def _index_path(self, name: str) -> Path:
        return self.layout.index / f"{name}.jsonl"

    def rebuild_indexes(self) -> dict[str, int]:
        """Regenerate the flat indexes from the stored records."""
        papers = [
            {
                "id": p.id,
                "title": p.title,
                "authors": p.authors[:6],
                "venue": p.venue,
                "published": p.published,
                "url": p.url,
                "topics": p.topics,
                "score": round(p.best_score, 4),
                "summarized": self.paper_summary_path(p.id).exists(),
            }
            for p in self.iter_papers()
        ]
        papers.sort(key=lambda r: (r["published"], r["id"]), reverse=True)
        rewrite_jsonl(self._index_path("papers"), papers)

        videos = [
            {
                "id": v.id,
                "title": v.title,
                "channel": v.channel,
                "published": v.published,
                "url": v.url,
                "topics": v.topics,
                "score": round(v.best_score, 4),
                "summarized": self.video_summary_path(v.id).exists(),
            }
            for v in self.iter_videos()
        ]
        videos.sort(key=lambda r: (r["published"], r["id"]), reverse=True)
        rewrite_jsonl(self._index_path("videos"), videos)

        return {"papers": len(papers), "videos": len(videos)}
