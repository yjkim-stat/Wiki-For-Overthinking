"""Presentation deck generation.

Produces one self-contained HTML file per topic. A deck is a filter, not a
dump: only summarized papers reach a slide of their own, and every slide is
capped so nothing renders as a wall of eight-point text.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path

from ..common import md
from ..common.config import Config, Topic
from ..common.log import get
from ..common.store import write_text
from . import load_template, render_template
from .material import TopicMaterial, gather

_LOG = get(__name__)

# A slide stops being readable past this many bullets.
_MAX_BULLETS = 6


def _slide(
    body: str = "",
    css_class: str = "",
    *,
    heading: str = "",
    heading_level: int = 2,
    subtitle: str = "",
) -> str:
    """Build one slide.

    The heading and subtitle are passed separately rather than written into the
    Markdown body: ``md.to_html`` escapes everything it is given, which is what
    keeps a paper title containing ``<`` safe, and means raw HTML must never be
    smuggled through it.
    """
    parts: list[str] = []
    if heading:
        parts.append(
            f"<h{heading_level}>{md.inline(heading)}</h{heading_level}>"
        )
    if subtitle:
        parts.append(f'<p class="subtitle">{md.inline(subtitle)}</p>')
    if body.strip():
        parts.append(md.to_html(body))
    classes = f"slide {css_class}".strip()
    return f'<section class="{classes}">\n' + "\n".join(parts) + "\n</section>"


def _title_slide(material: TopicMaterial) -> str:
    topic = material.topic
    return _slide(
        f"{date.today().isoformat()} · {material.source_count} archived source(s)",
        "title-slide",
        heading=topic.name,
        heading_level=1,
        subtitle=topic.description or "Research review",
    )


def _agenda_slide(material: TopicMaterial) -> str:
    items = ["Where the field stands", "Key papers", "Recurring ideas"]
    if material.datasets:
        items.append("Benchmarks")
    if material.videos:
        items.append("Talks")
    items.append("Open problems")
    return _slide("\n".join(f"- {i}" for i in items), heading="Agenda")


def _standing_slide(material: TopicMaterial) -> str:
    grouped = material.by_year()
    lines: list[str] = []
    if grouped:
        for year, entries in list(grouped.items())[:_MAX_BULLETS]:
            lines.append(f"- **{year}** — {len(entries)} paper(s)")
        recent = material.recent(30)
        if recent:
            lines += ["", f"{len(recent)} arrived in the last 30 days."]
    else:
        lines.append("- Nothing archived yet")
    return _slide("\n".join(lines), heading="Where the field stands")


def _paper_slide(entry, slug: str) -> str:
    paper = entry.paper
    summary = entry.summary
    lines: list[str] = []

    who = ", ".join(paper.authors[:3])
    if len(paper.authors) > 3:
        who += " et al."
    meta = " · ".join(x for x in (who, paper.venue, str(paper.year or "")) if x)

    if summary:
        if summary.one_liner:
            lines += [f"> {summary.one_liner}", ""]
        for item in summary.contributions[:4]:
            lines.append(f"- {item}")
        if summary.results:
            lines += ["", f"**Results.** {summary.results}"]
        why = summary.relevance.get(slug, "")
        if why:
            lines += ["", f"**Why it matters.** {why}"]
    return _slide("\n".join(lines), heading=paper.title, subtitle=meta)


def _entity_slide(title: str, concepts: list, definition_chars: int = 140) -> str:
    lines: list[str] = []
    if not concepts:
        lines.append("- Nothing recorded yet")
    for concept in concepts[:_MAX_BULLETS]:
        definition = (concept.definition or "").replace("\n", " ").strip()
        if len(definition) > definition_chars:
            definition = definition[: definition_chars - 3].rstrip() + "..."
        lines.append(
            f"- **{concept.name}**" + (f" — {definition}" if definition else "")
        )
    return _slide("\n".join(lines), heading=title)


def _open_problems_slides(material: TopicMaterial) -> list[str]:
    limitations = material.limitations(limit=_MAX_BULLETS * 2)
    if not limitations:
        return [_slide("- Nothing recorded yet", heading="Open problems")]

    slides = []
    for start in range(0, len(limitations), _MAX_BULLETS):
        chunk = limitations[start : start + _MAX_BULLETS]
        lines = []
        for title, text in chunk:
            trimmed = text if len(text) <= 160 else text[:157].rstrip() + "..."
            lines.append(f"- **{title}** — {trimmed}")
        slides.append(
            _slide(
                "\n".join(lines),
                heading="Open problems" + (" (cont.)" if start else ""),
            )
        )
    return slides


def _talks_slide(material: TopicMaterial) -> str:
    lines = []
    for entry in material.videos[:_MAX_BULLETS]:
        line = f"- **{entry.video.title}** ({entry.video.channel})"
        if entry.summary and entry.summary.one_liner:
            line += f" — {entry.summary.one_liner}"
        lines.append(line)
    return _slide("\n".join(lines), heading="Talks")


def _references_slides(material: TopicMaterial, per_slide: int = 8) -> list[str]:
    entries = material.highlights(limit=24) or material.papers[:24]
    if not entries:
        return []
    slides = []
    for start in range(0, len(entries), per_slide):
        chunk = entries[start : start + per_slide]
        lines = [f"- {entry.paper.citation()}" for entry in chunk]
        slides.append(
            _slide(
                "\n".join(lines),
                heading="References" + (" (cont.)" if start else ""),
            )
        )
    return slides


def build(cfg: Config, topic: Topic, material: TopicMaterial | None = None) -> Path:
    """Write the slide deck for ``topic``."""
    material = material or gather(cfg, topic)
    template = load_template(cfg.layout.templates, "slides", "base.html")

    slides: list[str] = [
        _title_slide(material),
        _agenda_slide(material),
        _standing_slide(material),
    ]
    for entry in material.highlights(limit=8):
        slides.append(_paper_slide(entry, topic.slug))
    slides.append(_entity_slide("Recurring ideas", material.concepts))
    if material.methods:
        slides.append(_entity_slide("Methods", material.methods))
    if material.datasets:
        slides.append(_entity_slide("Benchmarks and datasets", material.datasets))
    slides += _open_problems_slides(material)
    if material.videos:
        slides.append(_talks_slide(material))
    slides += _references_slides(material)
    slides.append(
        _slide(
            "Every claim in this deck traces to a page under `archive/`. "
            "Regenerate with `python -m pipelines.render`.",
            "title-slide",
            heading="Sources",
        )
    )

    html = render_template(
        template,
        {
            "TITLE": f"{topic.name} — research review",
            "SLIDES": "\n".join(slides),
        },
    )

    path = cfg.layout.out_slides / topic.slug / "index.html"
    write_text(path, html)
    _LOG.info("deck written: %s (%d slides)", path, len(slides))
    return path
