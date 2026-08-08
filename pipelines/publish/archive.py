"""The human-readable archive.

One Markdown page per paper and per seminar, plus a dated digest of everything
that arrived on a given day. Pages are rewritten from ``data/`` on every render,
so they must never be edited by hand — the wiki is where hand-written notes
belong.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path

from ..common.config import Config
from ..common.log import get
from ..common.paths import Layout, fs_id
from ..common.schema import Paper, PaperSummary, Video, VideoSummary
from ..common.store import RecordStore, write_text
from . import rel_link

_LOG = get(__name__)

GENERATED_BANNER = (
    "<!-- Generated from data/. Do not edit by hand: edits are overwritten on "
    "the next render. Put hand-written notes in the wiki instead. -->"
)


def paper_dir(layout: Layout, paper: Paper) -> Path:
    year = str(paper.year or (paper.published[:4] if paper.published else "unknown"))
    return layout.archive_papers / year / fs_id(paper.id)


def seminar_dir(layout: Layout, video: Video) -> Path:
    return layout.archive_seminars / fs_id(video.id)


def _bullets(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items if item) or "_none recorded_"


def _wiki_links(page: Path, layout: Layout, kind: str, names: list[str]) -> str:
    """Link concept names to their wiki notes, listing unlinked ones plainly."""
    from .wiki import note_path, slug_for  # imported late: wiki imports archive

    parts = []
    for name in names:
        slug = slug_for(name)
        target = note_path(layout, kind, slug)
        if target.exists():
            parts.append(f"[{name}]({rel_link(page, target)})")
        else:
            parts.append(name)
    return ", ".join(parts) if parts else "_none recorded_"


def _timestamp(seconds: float) -> str:
    total = int(seconds)
    hours, remainder = divmod(total, 3600)
    minutes, secs = divmod(remainder, 60)
    if hours:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    return f"{minutes}:{secs:02d}"


# ---------------------------------------------------------------------------
# Papers
# ---------------------------------------------------------------------------


def write_paper_page(
    layout: Layout, paper: Paper, summary: PaperSummary | None
) -> Path:
    page = paper_dir(layout, paper) / "summary.md"
    lines: list[str] = [GENERATED_BANNER, "", f"# {paper.title}", ""]

    authors = ", ".join(paper.authors) or "_unknown_"
    meta = [
        f"- **Authors**: {authors}",
        f"- **Venue**: {paper.venue or (paper.categories[0] if paper.categories else 'arXiv')}",
        f"- **Published**: {paper.published or 'unknown'}",
        f"- **Source**: {paper.source}",
    ]
    if paper.url:
        meta.append(f"- **Link**: <{paper.url}>")
    if paper.pdf_url:
        meta.append(f"- **PDF**: <{paper.pdf_url}>")
    if paper.doi:
        meta.append(f"- **DOI**: {paper.doi}")
    if paper.topics:
        meta.append(f"- **Topics**: {', '.join(paper.topics)}")
    if paper.scores:
        scored = ", ".join(f"{k} {v:.2f}" for k, v in sorted(paper.scores.items()))
        meta.append(f"- **Relevance score**: {scored}")
    lines += meta + [""]

    if summary is None:
        lines += [
            "## Summary",
            "",
            "_Not summarized yet. A task is queued under `data/queue/pending/`._",
            "",
        ]
    else:
        lines += [
            "## In one line",
            "",
            summary.one_liner or "_not recorded_",
            "",
            "## Problem",
            "",
            summary.problem or "_not recorded_",
            "",
            "## Contributions",
            "",
            _bullets(summary.contributions),
            "",
            "## Method",
            "",
            summary.method or "_not recorded_",
            "",
            "## Results",
            "",
            summary.results or "_not recorded_",
            "",
            "## Limitations",
            "",
            summary.limitations or "_not recorded_",
            "",
        ]
        if summary.relevance:
            lines += ["## Why it matters here", ""]
            for slug, why in sorted(summary.relevance.items()):
                lines.append(f"- **{slug}**: {why}")
            lines.append("")

        lines += [
            "## Entities",
            "",
            f"- **Concepts**: {_wiki_links(page, layout, 'concept', summary.concepts)}",
            f"- **Methods**: {_wiki_links(page, layout, 'method', summary.methods)}",
            f"- **Datasets**: {_wiki_links(page, layout, 'dataset', summary.datasets)}",
            "",
        ]
        if summary.tags:
            lines += ["Tags: " + ", ".join(f"`{t}`" for t in summary.tags), ""]

    if paper.abstract:
        lines += ["## Abstract", "", paper.abstract, ""]

    lines += ["---", "", f"Record id: `{paper.id}`"]
    write_text(page, "\n".join(lines))
    return page


# ---------------------------------------------------------------------------
# Seminars
# ---------------------------------------------------------------------------


def write_seminar_page(
    layout: Layout,
    video: Video,
    summary: VideoSummary | None,
    transcript: list[dict] | None = None,
) -> Path:
    directory = seminar_dir(layout, video)
    page = directory / "summary.md"
    lines: list[str] = [GENERATED_BANNER, "", f"# {video.title}", ""]

    meta = [
        f"- **Channel**: {video.channel or 'unknown'}",
        f"- **Published**: {video.published or 'unknown'}",
        f"- **Link**: <{video.url}>",
    ]
    if video.duration_s:
        meta.append(f"- **Duration**: {_timestamp(video.duration_s)}")
    if video.topics:
        meta.append(f"- **Topics**: {', '.join(video.topics)}")
    meta.append(
        "- **Transcript**: "
        + ("available" if video.transcript_available else "not available")
    )
    lines += meta + [""]

    if summary is None:
        lines += [
            "## Summary",
            "",
            "_Not summarized yet. A task is queued under `data/queue/pending/`._",
            "",
        ]
    else:
        lines += [
            "## In one line",
            "",
            summary.one_liner or "_not recorded_",
            "",
            "## Overview",
            "",
            summary.abstract or "_not recorded_",
            "",
        ]
        if summary.chapters:
            lines += ["## Chapters", ""]
            for chapter in summary.chapters:
                start = float(chapter.get("start_s", 0) or 0)
                stamp = _timestamp(start)
                link = f"{video.url}&t={int(start)}s" if video.url else ""
                title = chapter.get("title", "") or "untitled"
                heading = f"- **[{stamp}]({link})** {title}" if link else f"- **{stamp}** {title}"
                lines.append(heading)
                if chapter.get("summary"):
                    lines.append(f"  - {chapter['summary']}")
            lines.append("")

        lines += ["## Key points", "", _bullets(summary.key_points), ""]

        if summary.referenced_papers:
            lines += [
                "## Papers referenced",
                "",
                _bullets(summary.referenced_papers),
                "",
            ]

        lines += [
            "## Entities",
            "",
            f"- **Concepts**: {_wiki_links(page, layout, 'concept', summary.concepts)}",
            f"- **Methods**: {_wiki_links(page, layout, 'method', summary.methods)}",
            f"- **Datasets**: {_wiki_links(page, layout, 'dataset', summary.datasets)}",
            "",
        ]

    if video.description:
        lines += ["## Description", "", video.description, ""]

    lines += ["---", "", f"Record id: `{video.id}`"]
    write_text(page, "\n".join(lines))

    if transcript:
        write_transcript_page(layout, video, transcript)
    return page


def write_transcript_page(layout: Layout, video: Video, transcript: list[dict]) -> Path:
    page = seminar_dir(layout, video) / "transcript.md"
    lines = [GENERATED_BANNER, "", f"# Transcript — {video.title}", ""]
    for segment in transcript:
        lines.append(f"**[{_timestamp(segment.get('start_s', 0))}]** {segment.get('text', '')}")
        lines.append("")
    write_text(page, "\n".join(lines))
    return page


# ---------------------------------------------------------------------------
# Daily digest
# ---------------------------------------------------------------------------


def write_daily_digest(
    cfg: Config,
    day: date,
    *,
    papers: list[Paper],
    videos: list[Video],
    queue_stats: dict[str, int],
    errors: list[str] | None = None,
) -> Path:
    layout = cfg.layout
    page = layout.archive_daily / f"{day.isoformat()}.md"
    lines = [
        GENERATED_BANNER,
        "",
        f"# Research digest — {day.isoformat()}",
        "",
        f"{len(papers)} new paper(s), {len(videos)} new recording(s).",
        "",
    ]

    by_topic: dict[str, list[Paper]] = {}
    for paper in papers:
        for slug in paper.topics or ["unassigned"]:
            by_topic.setdefault(slug, []).append(paper)

    if papers:
        lines += ["## Papers", ""]
        for slug in sorted(by_topic):
            lines += [f"### {slug}", ""]
            entries = sorted(
                by_topic[slug], key=lambda p: p.scores.get(slug, 0.0), reverse=True
            )
            for paper in entries:
                target = paper_dir(layout, paper) / "summary.md"
                score = paper.scores.get(slug, 0.0)
                authors = ", ".join(paper.authors[:3])
                if len(paper.authors) > 3:
                    authors += " et al."
                lines.append(
                    f"- **[{paper.title}]({rel_link(page, target)})** "
                    f"({score:.2f}) — {authors or 'unknown'}"
                )
                if paper.url:
                    lines.append(f"  - <{paper.url}>")
            lines.append("")

    if videos:
        lines += ["## Seminars", ""]
        for video in videos:
            target = seminar_dir(layout, video) / "summary.md"
            lines.append(
                f"- **[{video.title}]({rel_link(page, target)})** — {video.channel}"
            )
            if video.url:
                lines.append(f"  - <{video.url}>")
        lines.append("")

    if not papers and not videos:
        lines += ["Nothing matched today's filters.", ""]

    lines += [
        "## Queue",
        "",
        f"- pending: {queue_stats.get('pending', 0)}",
        f"- completed, awaiting render: {queue_stats.get('done', 0)}",
        f"- applied: {queue_stats.get('archived', 0)}",
        "",
    ]

    if errors:
        lines += ["## Run problems", ""] + [f"- {e}" for e in errors] + [""]

    write_text(page, "\n".join(lines))
    return page


def write_archive_index(cfg: Config) -> Path:
    """Top-level table of contents for the archive."""
    layout = cfg.layout
    store = RecordStore(layout)
    page = layout.archive / "index.md"

    papers = list(store.iter_papers())
    videos = list(store.iter_videos())
    summarized = sum(1 for p in papers if store.paper_summary_path(p.id).exists())

    lines = [
        GENERATED_BANNER,
        "",
        "# Archive",
        "",
        f"- Papers: {len(papers)} ({summarized} summarized)",
        f"- Seminars: {len(videos)}",
        "",
        "## Recent digests",
        "",
    ]

    digests = sorted(layout.archive_daily.glob("*.md"), reverse=True)[:30]
    for digest in digests:
        lines.append(f"- [{digest.stem}]({rel_link(page, digest)})")
    if not digests:
        lines.append("_No digests yet._")
    lines.append("")

    lines += ["## Topics", ""]
    for topic in cfg.topics:
        matched = sum(1 for p in papers if topic.slug in p.topics)
        lines.append(f"- **{topic.name}** (`{topic.slug}`) — {matched} paper(s)")
    if not cfg.topics:
        lines.append(
            "_No topics registered. Add one with `scripts/new_topic.sh \"Name\"`._"
        )
    lines.append("")

    write_text(page, "\n".join(lines))
    return page
