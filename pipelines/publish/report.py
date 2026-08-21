"""Report generation.

One self-contained HTML file per topic: the full state of the archive, with a
table of contents, an activity view and the complete index. Where the deck
filters, the report is exhaustive — it is the artifact you send to someone who
wants everything.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path

from ..common import md
from ..common.config import Config, Topic
from ..common.log import get
from ..common.paths import slugify
from ..common.store import write_text
from . import load_template, render_template
from .material import TopicMaterial, citation_list, gather

_LOG = get(__name__)

_EMPTY = "_Nothing archived for this section yet._"


class _Sections:
    """Collects ``(anchor, title, markdown)`` so the TOC cannot fall out of sync."""

    def __init__(self) -> None:
        self.items: list[tuple[str, str, str]] = []

    def add(self, title: str, body: str) -> None:
        self.items.append((slugify(title), title, body))

    def content_html(self) -> str:
        parts = []
        for anchor, title, body in self.items:
            parts.append(f'<h2 id="{anchor}">{md.escape(title)}</h2>')
            parts.append(md.to_html(body))
        return "\n".join(parts)

    def toc_html(self) -> str:
        if not self.items:
            return ""
        links = "\n".join(
            f'<li><a href="#{anchor}">{md.escape(title)}</a></li>'
            for anchor, title, _ in self.items
        )
        return f'<nav class="toc"><h2>Contents</h2><ol>\n{links}\n</ol></nav>'


def _overview(material: TopicMaterial) -> str:
    topic = material.topic
    lines = []
    if topic.description:
        lines += [topic.description, ""]

    dates = [e.paper.published for e in material.papers if e.paper.published]
    lines += [
        f"- **Papers archived**: {len(material.papers)}",
        f"- **Papers read in full**: {len(material.summarized)}",
        f"- **Recordings**: {len(material.videos)}",
        f"- **Concepts tracked**: {len(material.concepts)}",
        f"- **Methods tracked**: {len(material.methods)}",
        f"- **Datasets tracked**: {len(material.datasets)}",
    ]
    if dates:
        lines.append(f"- **Coverage**: {min(dates)} to {max(dates)}")
    return "\n".join(lines)


def _activity(material: TopicMaterial) -> str:
    grouped = material.by_year()
    if not grouped:
        return _EMPTY

    lines = ["| Year | Papers | Read | Share |", "| --- | ---: | ---: | --- |"]
    total = len(material.papers) or 1
    for year, entries in grouped.items():
        read = sum(1 for e in entries if e.summary is not None)
        share = len(entries) / total
        bar = "█" * max(1, round(share * 20))
        lines.append(f"| {year} | {len(entries)} | {read} | {bar} {share:.0%} |")

    recent = material.recent(30)
    lines += ["", f"{len(recent)} paper(s) arrived in the last 30 days."]
    return "\n".join(lines)


def _highlights(material: TopicMaterial) -> str:
    entries = material.highlights(limit=15)
    if not entries:
        return _EMPTY

    lines: list[str] = []
    for entry in entries:
        paper, summary = entry.paper, entry.summary
        lines.append(f"### {paper.title}")
        lines.append("")

        who = ", ".join(paper.authors[:4])
        if len(paper.authors) > 4:
            who += " et al."
        meta = " · ".join(
            x for x in (who, paper.venue, paper.published, paper.source) if x
        )
        lines += [f"_{meta}_", ""]
        if paper.url:
            lines += [f"<{paper.url}>", ""]

        if summary is None:
            lines += ["_Not summarized yet._", ""]
            continue

        if summary.one_liner:
            lines += [f"> {summary.one_liner}", ""]
        if summary.problem:
            lines += [f"**Problem.** {summary.problem}", ""]
        if summary.contributions:
            lines += ["**Contributions.**", ""]
            lines += [f"- {c}" for c in summary.contributions]
            lines.append("")
        if summary.method:
            lines += [f"**Method.** {summary.method}", ""]
        if summary.results:
            lines += [f"**Results.** {summary.results}", ""]
        if summary.limitations:
            lines += [f"**Limitations.** {summary.limitations}", ""]
        why = summary.relevance.get(material.topic.slug, "")
        if why:
            lines += [f"**Relevance.** {why}", ""]
    return "\n".join(lines).rstrip()


def _entities(material: TopicMaterial) -> str:
    blocks: list[str] = []
    for label, concepts in (
        ("Concepts", material.concepts),
        ("Methods", material.methods),
        ("Datasets and benchmarks", material.datasets),
    ):
        blocks.append(f"### {label}")
        blocks.append("")
        if not concepts:
            blocks += ["_None recorded yet._", ""]
            continue
        blocks += ["| Name | Sources | Definition |", "| --- | ---: | --- |"]
        for concept in concepts[:40]:
            definition = (concept.definition or "").replace("|", "\\|").replace("\n", " ")
            blocks.append(
                f"| {concept.name} | {concept.mention_count} | "
                f"{definition or '_pending_'} |"
            )
        blocks.append("")
    return "\n".join(blocks).rstrip()


def _seminars(material: TopicMaterial) -> str:
    if not material.videos:
        return _EMPTY
    lines: list[str] = []
    for entry in material.videos:
        video, summary = entry.video, entry.summary
        lines.append(f"### {video.title}")
        lines += ["", f"_{video.channel} · {video.published}_", ""]
        if video.url:
            lines += [f"<{video.url}>", ""]
        if summary is None:
            lines += ["_Not summarized yet._", ""]
            continue
        if summary.one_liner:
            lines += [f"> {summary.one_liner}", ""]
        if summary.key_points:
            lines += [f"- {p}" for p in summary.key_points[:8]] + [""]
    return "\n".join(lines).rstrip()


def _full_index(material: TopicMaterial) -> str:
    if not material.papers:
        return _EMPTY
    lines = ["| Published | Title | Venue | Read |", "| --- | --- | --- | :-: |"]
    for entry in material.papers:
        paper = entry.paper
        title = paper.title.replace("|", "\\|")
        if paper.url:
            title = f"[{title}]({paper.url})"
        lines.append(
            f"| {paper.published or '—'} | {title} | "
            f"{(paper.venue or '—').replace('|', '')} | "
            f"{'yes' if entry.summary else 'no'} |"
        )
    return "\n".join(lines)


def build(cfg: Config, topic: Topic, material: TopicMaterial | None = None) -> Path:
    """Write the HTML report for ``topic``."""
    material = material or gather(cfg, topic)
    template = load_template(cfg.layout.template_dirs, "report", "base.html")

    sections = _Sections()
    sections.add("Overview", _overview(material))
    sections.add("Activity", _activity(material))
    sections.add("Highlights", _highlights(material))
    sections.add("Concepts, methods and datasets", _entities(material))
    sections.add("Seminars", _seminars(material))
    sections.add("Full index", _full_index(material))
    references = citation_list(material)
    sections.add("References", "\n".join(references) if references else _EMPTY)

    meta = [
        f"<span>Topic <code>{md.escape(topic.slug)}</code></span>",
        f"<span>{len(material.papers)} papers</span>",
        f"<span>{len(material.videos)} recordings</span>",
        f"<span>Generated {date.today().isoformat()}</span>",
    ]

    html = render_template(
        template,
        {
            "TITLE": f"{topic.name} — research report",
            "SUBTITLE": topic.description or "State of the archive",
            "META": "\n".join(meta),
            "TOC": sections.toc_html(),
            "CONTENT": sections.content_html(),
            "FOOTER": (
                "Generated from the research archive. Every entry links back to "
                "its source; regenerate with <code>python -m pipelines.render</code>."
            ),
        },
    )

    path = cfg.layout.out_reports / topic.slug / "index.html"
    write_text(path, html)
    _LOG.info("report written: %s", path)
    return path
