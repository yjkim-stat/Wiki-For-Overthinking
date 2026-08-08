"""Lecture note generation.

Turns a topic's archive into teaching material: what the field is trying to do,
which ideas recur, which papers to read in which order, and what is still open.
Everything is traceable to an archived source — nothing is asserted that no
summary supports.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path

from ..common.config import Config, Topic
from ..common.log import get
from ..common.schema import Concept
from ..common.store import write_text
from . import load_template, render_template
from .material import TopicMaterial, citation_list, gather

_LOG = get(__name__)

_EMPTY = "_Nothing archived for this section yet._"


def _scope(material: TopicMaterial) -> str:
    topic = material.topic
    lines = [topic.description or f"Material archived under `{topic.slug}`."]
    lines.append("")

    dates = [e.paper.published for e in material.papers if e.paper.published]
    span = f" spanning {min(dates)} to {max(dates)}" if dates else ""
    lines.append(
        f"Built from {len(material.papers)} paper(s) and "
        f"{len(material.videos)} recording(s){span}. "
        f"{len(material.summarized)} of the papers have been read in full."
    )

    if topic.keywords_any:
        lines.append("")
        lines.append(
            "Tracked terms: " + ", ".join(f"`{k}`" for k in topic.keywords_any) + "."
        )
    return "\n".join(lines)


def _landscape(material: TopicMaterial) -> str:
    grouped = material.by_year()
    if not grouped:
        return _EMPTY

    lines: list[str] = []
    for year, entries in grouped.items():
        lines.append(f"### {year}")
        lines.append("")
        for entry in entries[:12]:
            title = entry.paper.title
            if entry.one_liner:
                lines.append(f"- **{title}** — {entry.one_liner}")
            else:
                lines.append(f"- **{title}** _(not yet summarized)_")
        if len(entries) > 12:
            lines.append(f"- _...and {len(entries) - 12} more._")
        lines.append("")
    return "\n".join(lines).rstrip()


def _concept_section(concepts: list[Concept], limit: int = 12) -> str:
    if not concepts:
        return _EMPTY
    lines: list[str] = []
    for concept in concepts[:limit]:
        lines.append(f"### {concept.name}")
        lines.append("")
        if concept.definition:
            lines.append(concept.definition)
        else:
            lines.append("_Definition pending; a task is queued._")
        lines.append("")
        sources = [e.get("title", "") for e in concept.evidence[:4] if e.get("title")]
        if sources:
            lines.append("Seen in: " + "; ".join(sources) + ".")
            lines.append("")
    return "\n".join(lines).rstrip()


def _compact_table(concepts: list[Concept], header: str, limit: int = 20) -> str:
    if not concepts:
        return _EMPTY
    lines = [f"| {header} | Sources | Summary |", "| --- | ---: | --- |"]
    for concept in concepts[:limit]:
        definition = (concept.definition or "").replace("|", "\\|").replace("\n", " ")
        if len(definition) > 180:
            definition = definition[:177].rstrip() + "..."
        lines.append(
            f"| {concept.name} | {concept.mention_count} | "
            f"{definition or '_pending_'} |"
        )
    return "\n".join(lines)


def _reading_path(material: TopicMaterial) -> str:
    topic = material.topic
    lines: list[str] = []

    if topic.seed_papers:
        lines.append("**Start here** — the anchor papers for this topic:")
        lines.append("")
        for seed in topic.seed_papers:
            lines.append(f"1. {seed}")
        lines.append("")

    highlights = material.highlights(limit=10)
    if highlights:
        lines.append("**Then, in order of relevance:**")
        lines.append("")
        for index, entry in enumerate(highlights, start=1):
            paper = entry.paper
            line = f"{index}. **{paper.title}**"
            if paper.published:
                line += f" ({paper.published[:4]})"
            lines.append(line)
            if entry.one_liner:
                lines.append(f"   - {entry.one_liner}")
            if paper.url:
                lines.append(f"   - <{paper.url}>")
        lines.append("")

    if material.videos:
        lines.append("**Talks worth watching:**")
        lines.append("")
        for entry in material.videos[:5]:
            line = f"- **{entry.video.title}** ({entry.video.channel})"
            if entry.summary and entry.summary.one_liner:
                line += f" — {entry.summary.one_liner}"
            lines.append(line)
        lines.append("")

    return "\n".join(lines).rstrip() or _EMPTY


def _open_problems(material: TopicMaterial) -> str:
    limitations = material.limitations()
    if not limitations:
        return _EMPTY
    lines = [
        "Drawn from the limitations each paper states about itself, so this is "
        "what the field admits it cannot do yet.",
        "",
    ]
    for title, text in limitations:
        lines.append(f"- **{title}** — {text}")
    return "\n".join(lines)


def build(cfg: Config, topic: Topic, material: TopicMaterial | None = None) -> Path:
    """Write the lecture note for ``topic``."""
    material = material or gather(cfg, topic)
    template = load_template(cfg.layout.templates, "lecture-note", "base.md")

    references = citation_list(material)
    content = render_template(
        template,
        {
            "TITLE": topic.name,
            "SUBTITLE": "Lecture note assembled from the research archive",
            "GENERATED_AT": date.today().isoformat(),
            "SOURCE_COUNT": str(material.source_count),
            "SCOPE": _scope(material),
            "LANDSCAPE": _landscape(material),
            "CONCEPTS": _concept_section(material.concepts),
            "METHODS": _compact_table(material.methods, "Method"),
            "DATASETS": _compact_table(material.datasets, "Dataset / benchmark"),
            "READING_PATH": _reading_path(material),
            "OPEN_PROBLEMS": _open_problems(material),
            "REFERENCES": "\n".join(references) if references else _EMPTY,
        },
    )

    path = cfg.layout.out_lecture_notes / topic.slug / "lecture-note.md"
    write_text(path, content)
    _LOG.info("lecture note written: %s", path)
    return path
