"""Assembles everything a topic's outputs are built from.

The lecture note, the deck and the report all answer the same question — what
does the archive know about this topic — and differ only in how much of it they
show. Gathering happens once, here, so the three cannot drift apart.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta

from ..common.config import Config, Topic
from ..common.schema import Concept, Paper, PaperSummary, Video, VideoSummary
from ..common.store import RecordStore


@dataclass
class PaperEntry:
    paper: Paper
    summary: PaperSummary | None = None

    @property
    def score(self) -> float:
        return self.paper.best_score

    @property
    def one_liner(self) -> str:
        return self.summary.one_liner if self.summary else ""


@dataclass
class VideoEntry:
    video: Video
    summary: VideoSummary | None = None


@dataclass
class TopicMaterial:
    """Everything archived under one topic, ordered for presentation."""

    topic: Topic
    papers: list[PaperEntry] = field(default_factory=list)
    videos: list[VideoEntry] = field(default_factory=list)
    concepts: list[Concept] = field(default_factory=list)
    methods: list[Concept] = field(default_factory=list)
    datasets: list[Concept] = field(default_factory=list)

    @property
    def summarized(self) -> list[PaperEntry]:
        return [entry for entry in self.papers if entry.summary is not None]

    @property
    def source_count(self) -> int:
        return len(self.papers) + len(self.videos)

    def recent(self, days: int = 30) -> list[PaperEntry]:
        cutoff = (date.today() - timedelta(days=days)).isoformat()
        return [e for e in self.papers if e.paper.published >= cutoff]

    def by_year(self) -> dict[str, list[PaperEntry]]:
        grouped: dict[str, list[PaperEntry]] = {}
        for entry in self.papers:
            year = str(entry.paper.year or entry.paper.published[:4] or "undated")
            grouped.setdefault(year, []).append(entry)
        return dict(sorted(grouped.items(), reverse=True))

    def highlights(self, limit: int = 10) -> list[PaperEntry]:
        """Summarized papers, most relevant first — the ones worth a slide."""
        ranked = sorted(
            self.summarized,
            key=lambda e: (
                e.paper.scores.get(self.topic.slug, 0.0),
                e.paper.published,
            ),
            reverse=True,
        )
        return ranked[:limit]

    def limitations(self, limit: int = 12) -> list[tuple[str, str]]:
        """``(paper title, stated limitation)`` across summarized papers."""
        out: list[tuple[str, str]] = []
        for entry in self.summarized:
            text = (entry.summary.limitations or "").strip()
            if text and text.lower() not in ("none", "n/a"):
                out.append((entry.paper.title, text))
        return out[:limit]


def gather(cfg: Config, topic: Topic) -> TopicMaterial:
    """Load every record tagged with ``topic``."""
    store = RecordStore(cfg.layout)
    material = TopicMaterial(topic=topic)

    papers = [p for p in store.iter_papers() if topic.slug in p.topics]
    papers.sort(
        key=lambda p: (p.published, p.scores.get(topic.slug, 0.0)), reverse=True
    )
    material.papers = [
        PaperEntry(paper=p, summary=store.load_paper_summary(p.id)) for p in papers
    ]

    videos = [v for v in store.iter_videos() if topic.slug in v.topics]
    videos.sort(key=lambda v: v.published, reverse=True)
    material.videos = [
        VideoEntry(video=v, summary=store.load_video_summary(v.id)) for v in videos
    ]

    buckets = {"concept": material.concepts, "method": material.methods,
               "dataset": material.datasets}
    for concept in store.iter_concepts():
        if topic.slug not in concept.topics:
            continue
        bucket = buckets.get(concept.kind)
        if bucket is not None:
            bucket.append(concept)
    for bucket in buckets.values():
        bucket.sort(key=lambda c: (-c.mention_count, c.name.lower()))

    return material


def citation_list(material: TopicMaterial) -> list[str]:
    """Markdown reference lines, oldest first."""
    entries = sorted(
        material.papers, key=lambda e: (e.paper.published or "", e.paper.title)
    )
    lines = []
    for index, entry in enumerate(entries, start=1):
        paper = entry.paper
        line = f"{index}. {paper.citation()}"
        if paper.url:
            line += f" <{paper.url}>"
        lines.append(line)
    return lines
