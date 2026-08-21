"""The self-extending wiki.

Every summary names the concepts, methods and datasets it relies on. Those
names accumulate as evidence in ``data/concepts/``; once an entity has been
seen in enough independent sources it is promoted to a note of its own, and a
definition task is queued so the note gets written properly rather than left as
a stub.

Notes are half generated and half yours. Everything between the auto markers is
rebuilt on every render; everything after them is never touched, so hand-written
analysis survives indefinitely.
"""

from __future__ import annotations

import re

from pathlib import Path

from ..common.config import Config
from ..common.log import get
from ..common.paths import Layout
from ..common.schema import Concept, utcnow
from ..common.store import RecordStore, read_json, write_json, write_text
from ..enrich import findings
from ..enrich.concepts import KINDS, slug_for
from . import graph_page, load_template, rel_link, render_template
from .archive import paper_dir, seminar_dir

_LOG = get(__name__)

DEFAULT_MANUAL_SECTION = """## Notes

_Anything below the marker above is yours. It is never overwritten._
"""


def note_path(layout: Layout, kind: str, slug: str) -> Path:
    return layout.wiki_kind_dir(kind) / f"{slug}.md"


def topic_note_path(layout: Layout, slug: str) -> Path:
    return layout.wiki_kind_dir("topic") / f"{slug}.md"


def _markers(cfg: Config) -> tuple[str, str]:
    block = cfg.settings.get("wiki", {}) or {}
    return (
        block.get("auto_block_begin", "<!-- auto:begin -->"),
        block.get("auto_block_end", "<!-- auto:end -->"),
    )


def _preserved_tail(path: Path, end_marker: str) -> str:
    """Everything a human wrote after the generated block."""
    if not path.exists():
        return DEFAULT_MANUAL_SECTION
    text = path.read_text(encoding="utf-8")
    index = text.find(end_marker)
    if index == -1:
        # No marker: the file predates the convention, or was hand-created.
        # Keep all of it rather than risk destroying someone's notes.
        return text.strip() or DEFAULT_MANUAL_SECTION
    return text[index + len(end_marker) :].lstrip("\n") or DEFAULT_MANUAL_SECTION


ANALYSIS_SOURCES = re.compile(r"<!--\s*analysis-sources:\s*(\d+)\s*-->")


def _outgrown_notice(tail: str, sources_now: int) -> list[str]:
    """A warning about the prose below, placed where the prose is.

    Analysis under `auto:end` can declare what it was written against, and
    `render` reports when the evidence has passed it. A log line is a poor place
    for that: the person who needs it is whoever is *reading the note*, and they
    will never see the run that mentioned it.

    So it is said here, at the foot of the generated block — immediately above
    the prose it is about, and inside the only part of the file this code is
    allowed to write. The prose itself is not touched, reworded or marked up.
    Nothing can revise it but its author.
    """
    match = ANALYSIS_SOURCES.search(tail)
    if match is None:
        return []
    written_for = int(match.group(1))
    if sources_now == written_for:
        return []
    if sources_now > written_for:
        said = (
            f"was written against {written_for} source(s); there are now "
            f"{sources_now}"
        )
    else:
        # The other direction, which `render.stale_analysis` also reports since
        # note 0090: either the author miscounted, or evidence the prose relies
        # on has gone. The second is the worse one and looks identical here.
        said = (
            f"claims {written_for} source(s); this note now holds "
            f"{sources_now}"
        )
    return [
        "",
        f"> **The analysis below {said}.** It may still be right — nothing here "
        "has read it. Revise it, or update its `analysis-sources` marker to say "
        "it was checked.",
    ]


def _write_note(
    cfg: Config, path: Path, title: str, auto_body: str, sources_now: int = 0
) -> Path:
    begin, end = _markers(cfg)
    tail = _preserved_tail(path, end)
    if sources_now:
        auto_body = auto_body.rstrip() + "\n".join(
            _outgrown_notice(tail, sources_now)
        )
    template = load_template(cfg.layout.template_dirs, "wiki", "note.md")
    content = render_template(
        template,
        {
            "TITLE": title,
            "AUTO_BEGIN": begin,
            "BODY": auto_body.strip(),
            "AUTO_END": end,
            "MANUAL": tail.rstrip(),
        },
    )
    write_text(path, content)
    return path


def _evidence_lines(
    cfg: Config, page: Path, concept: Concept, store: RecordStore
) -> list[str]:
    lines: list[str] = []
    for item in concept.evidence:
        title = item.get("title", "") or item.get("id", "")
        note = item.get("note", "")
        target: Path | None = None
        if item.get("kind") == "paper":
            paper = store.load_paper(item.get("id", ""))
            if paper is not None:
                target = paper_dir(cfg.layout, paper) / "summary.md"
        else:
            video = store.load_video(item.get("id", ""))
            if video is not None:
                target = seminar_dir(cfg.layout, video) / "summary.md"
        label = f"[{title}]({rel_link(page, target)})" if target else title
        lines.append(f"- {label}" + (f" — {note}" if note else ""))
    return lines or ["_No sources recorded yet._"]


def _findings_for(slug, index):
    return index.get(slug, []) if index else []


def write_concept_note(
    cfg: Config,
    concept: Concept,
    store: RecordStore,
    all_concepts: dict[str, Concept],
    findings_by_concept: dict[str, list] | None = None,
) -> Path:
    page = note_path(cfg.layout, concept.kind, concept.slug)

    body: list[str] = []
    if concept.definition:
        body += [concept.definition, ""]
    else:
        body += [
            "_No definition yet — a task is queued to write one._",
            "",
        ]

    facts = [f"- **Kind**: {concept.kind}"]
    if concept.aliases:
        facts.append("- **Also called**: " + ", ".join(sorted(set(concept.aliases))))
    if concept.topics:
        topic_links = []
        for slug in sorted(concept.topics):
            target = topic_note_path(cfg.layout, slug)
            topic_links.append(
                f"[{slug}]({rel_link(page, target)})" if target.exists() else slug
            )
        facts.append("- **Topics**: " + ", ".join(topic_links))
    facts.append(f"- **Sources**: {concept.mention_count}")
    body += facts + [""]

    related = [
        all_concepts[slug] for slug in sorted(concept.neighbours) if slug in all_concepts
    ]
    if related:
        links = []
        for other in related:
            target = note_path(cfg.layout, other.kind, other.slug)
            links.append(
                f"[{other.name}]({rel_link(page, target)})"
                if target.exists()
                else other.name
            )
        body += ["**Related**: " + ", ".join(links), ""]

    settled = _findings_for(concept.slug, findings_by_concept)
    if settled:
        # Above the source list on purpose: what the group concluded outranks
        # what any one paper said, and a reader arriving at the note should
        # meet the position before the evidence for it.
        body += ["## What we have settled", ""]
        for finding in settled:
            label = "Decision" if finding.kind == "decision" else "Established"
            body.append(f"- **{label}** — {finding.statement}")
            if finding.rationale:
                body.append(f"  - {finding.rationale}")
        body.append("")

    body += ["## Appears in", ""] + _evidence_lines(cfg, page, concept, store)

    # Below the evidence and under a heading of its own. A reference is not
    # evidence for this entity — it did not put the name in a summary and it
    # cannot promote anything — so putting it in the list above would make the
    # note claim a source it does not have. Which is also why the two are
    # separate records rather than one list with a flag.
    checked = _references_for(settled, store)
    if checked:
        body += ["", "## Checked against", ""] + _reference_lines(checked)

    return _write_note(
        cfg, page, concept.name, "\n".join(body), len(concept.evidence)
    )


def _references_for(settled: list, store: RecordStore) -> list:
    """Every reference cited by the findings that bear on this entity.

    Deduplicated, because two findings that consulted one page should not make
    the note look as though two things were checked.
    """
    seen: set[str] = set()
    out = []
    for finding in settled:
        for ref_id in finding.references:
            if ref_id in seen:
                continue
            seen.add(ref_id)
            reference = store.load_reference(ref_id)
            if reference is not None:
                out.append(reference)
    return sorted(out, key=lambda r: (r.title or r.url).lower())


def _reference_lines(references: list) -> list[str]:
    """One line per page, with the passage that was actually relied on.

    The quotation is carried into the note rather than left in the record. A
    reader deciding whether to trust a settled position should not have to open
    a JSON file to see what the page was found to say — and if the page has
    moved since, this is the only place the words still exist.
    """
    lines: list[str] = []
    for reference in references:
        label = reference.title or reference.url
        meta = " · ".join(
            part
            for part in (
                reference.publisher,
                reference.kind if reference.kind != "other" else "",
                f"retrieved {reference.retrieved_at}" if reference.retrieved_at else "",
            )
            if part
        )
        lines.append(f"- [{label}]({reference.url})" + (f" — {meta}" if meta else ""))
        if reference.quoted:
            lines.append(f"  - _{reference.quoted}_")
    return lines


def write_topic_note(cfg: Config, topic, store: RecordStore) -> Path:
    page = topic_note_path(cfg.layout, topic.slug)

    papers = [p for p in store.iter_papers() if topic.slug in p.topics]
    papers.sort(key=lambda p: (p.published, p.scores.get(topic.slug, 0.0)), reverse=True)
    videos = [v for v in store.iter_videos() if topic.slug in v.topics]

    body: list[str] = []
    if topic.description:
        body += [topic.description, ""]
    body += [
        f"- **Slug**: `{topic.slug}`",
        f"- **Papers**: {len(papers)}",
        f"- **Seminars**: {len(videos)}",
        "- **Tracked keywords**: " + ", ".join(f"`{k}`" for k in topic.keywords_any),
        "",
    ]

    body += ["## Most recent papers", ""]
    if papers:
        for paper in papers[:25]:
            target = paper_dir(cfg.layout, paper) / "summary.md"
            summary = store.load_paper_summary(paper.id)
            line = f"- [{paper.title}]({rel_link(page, target)})"
            if paper.published:
                line += f" ({paper.published})"
            body.append(line)
            if summary and summary.one_liner:
                body.append(f"  - {summary.one_liner}")
    else:
        body.append("_Nothing collected yet._")
    body.append("")

    if videos:
        body += ["## Seminars", ""]
        for video in videos[:25]:
            target = seminar_dir(cfg.layout, video) / "summary.md"
            body.append(f"- [{video.title}]({rel_link(page, target)})")
        body.append("")

    return _write_note(cfg, page, topic.name, "\n".join(body))


def write_index(cfg: Config, concepts: dict[str, Concept], live: dict[str, Concept]) -> Path:
    page = cfg.layout.wiki / "index.md"
    body: list[str] = ["## Topics", ""]

    if cfg.topics:
        for topic in cfg.topics:
            target = topic_note_path(cfg.layout, topic.slug)
            body.append(f"- [{topic.name}]({rel_link(page, target)}) — `{topic.slug}`")
    else:
        body.append(
            '_No topics registered. Add one with `scripts/new_topic.sh "Name"`._'
        )
    body.append("")

    for kind in KINDS:
        entries = sorted(
            (c for c in live.values() if c.kind == kind), key=lambda c: c.name.lower()
        )
        body += [f"## {kind.capitalize()}s ({len(entries)})", ""]
        if entries:
            for concept in entries:
                target = note_path(cfg.layout, kind, concept.slug)
                body.append(
                    f"- [{concept.name}]({rel_link(page, target)}) "
                    f"— {concept.mention_count} source(s)"
                )
        else:
            body.append("_None yet._")
        body.append("")

    emerging = sorted(
        (c for slug, c in concepts.items() if slug not in live),
        key=lambda c: (-c.mention_count, c.name.lower()),
    )[:40]
    body += ["## Emerging", "", ]
    if emerging:
        body.append(
            "_Seen once so far. They get their own note once a second "
            "independent source mentions them._"
        )
        body.append("")
        for concept in emerging:
            body.append(f"- {concept.name} ({concept.kind})")
    else:
        body.append("_Nothing pending._")
    body.append("")

    return _write_note(cfg, page, "Wiki", "\n".join(body))


# ---------------------------------------------------------------------------
# Graph
# ---------------------------------------------------------------------------


def build_graph(
    cfg: Config,
    live: dict[str, Concept],
    settled: dict[str, list] | None = None,
) -> Path:
    """Emit the note graph for external viewers."""
    nodes = []
    edges = []

    for topic in cfg.topics:
        nodes.append(
            {"id": f"topic:{topic.slug}", "label": topic.name, "kind": "topic"}
        )

    for concept in live.values():
        nodes.append(
            {
                "id": f"{concept.kind}:{concept.slug}",
                "label": concept.name,
                "kind": concept.kind,
                "sources": concept.mention_count,
                # A flag, not a fourth category: the palette validates three
                # hues and no more, so "the group has settled something here"
                # is drawn as a mark on the mark rather than a new colour.
                "settled": bool((settled or {}).get(concept.slug)),
            }
        )
        for slug in concept.topics:
            edges.append(
                {
                    "source": f"topic:{slug}",
                    "target": f"{concept.kind}:{concept.slug}",
                    "type": "covers",
                }
            )

    seen_pairs: set[tuple[str, str]] = set()
    for concept in live.values():
        source = f"{concept.kind}:{concept.slug}"
        for slug in sorted(concept.neighbours):
            other = live.get(slug)
            if other is None:
                continue
            target = f"{other.kind}:{other.slug}"
            pair = tuple(sorted((source, target)))
            if pair in seen_pairs:
                continue
            seen_pairs.add(pair)
            # Asked of both ends, not just this one. The pair is recorded on
            # first arrival and the second is dropped, so reading only this
            # concept's list would let dictionary order decide whether an edge
            # is labelled authored — a difference that would appear and vanish
            # between renders with nothing changing in `data/`.
            authored = (
                slug in concept.related_authored
                or concept.slug in other.related_authored
            )
            edges.append(
                {
                    "source": source,
                    "target": target,
                    # `links`, not `co-occurs`: this loop reads the union of the
                    # derived and the ruled, and naming it after one of its two
                    # inputs is what made the graph assert that a person's
                    # deliberate link had merely turned up in a summary.
                    "type": "links",
                    "authored": authored,
                }
            )

    path = cfg.layout.wiki_meta / "graph.json"
    graph = {
        "generated_at": utcnow(),
        "nodes": sorted(nodes, key=lambda n: n["id"]),
        "edges": sorted(edges, key=lambda e: (e["source"], e["target"], e["type"])),
    }
    # Left alone when only the stamp would move. See `unchanged_but_for`.
    existing = read_json(path)
    if isinstance(existing, dict) and existing:
        if {k: v for k, v in existing.items() if k != "generated_at"} == {
            k: v for k, v in graph.items() if k != "generated_at"
        }:
            return path
    write_json(path, graph)
    return path


def write_findings_page(cfg: Config, store: RecordStore) -> Path:
    """The picture the group has drawn for itself, in one place.

    Grouped by topic rather than by date. A chronological log answers "what did
    we say last Tuesday", which nobody asks; grouping by topic answers "where
    have we got to on this", which is the question the page exists for.

    Retired findings are kept, at the bottom, marked. A record of what the
    group used to think is most of what a newcomer needs in order to trust what
    it thinks now.
    """
    rows = sorted(
        store.iter_findings(), key=lambda f: f.established_at, reverse=True
    )
    current = [f for f in rows if f.live]
    retired = [f for f in rows if not f.live]

    names = {topic.slug: topic.name for topic in cfg.topics}
    by_topic: dict[str, list] = {}
    for finding in current:
        for slug in finding.topics or ["(no topic)"]:
            by_topic.setdefault(slug, []).append(finding)

    lines = ["# What we have settled", ""]
    if not rows:
        lines += [
            "_Nothing recorded yet. Findings are added with "
            "`python3 -m pipelines.enrich.findings add`._",
            "",
        ]

    def render(finding) -> list[str]:
        label = "Decision" if finding.kind == "decision" else "Established"
        out = [f"- **{label}** — {finding.statement}"]
        if finding.rationale:
            out.append(f"  - _{finding.rationale}_")
        links = []
        for name in finding.concepts:
            slug = slug_for(name)
            concept = store.load_concept(slug)
            target = note_path(cfg.layout, concept.kind, slug) if concept else None
            links.append(
                f"[{name}]({rel_link(page, target)})"
                if target is not None and target.exists()
                else name
            )
        if links:
            out.append("  - Bears on: " + ", ".join(links))
        if finding.papers:
            out.append(f"  - From: {', '.join(finding.papers)}")
        # Named separately from `From:`, which lists papers in the archive.
        # Conflating the two would let a page somebody read once be counted
        # alongside the literature this group collected and read.
        checked = []
        for ref_id in finding.references:
            reference = store.load_reference(ref_id)
            if reference is None:
                continue
            label = reference.title or reference.url
            when = f", retrieved {reference.retrieved_at}" if reference.retrieved_at else ""
            checked.append(f"[{label}]({reference.url}){when}")
        if checked:
            out.append("  - Checked against: " + "; ".join(checked))
        return out

    page = cfg.layout.wiki / "findings.md"
    for slug in sorted(by_topic, key=lambda s: names.get(s, s)):
        lines += [f"## {names.get(slug, slug)}", ""]
        for finding in by_topic[slug]:
            lines += render(finding)
        lines.append("")

    if retired:
        lines += ["## Superseded", "",
                  "_Kept because why the group used to think otherwise is part of "
                  "understanding where it got to._", ""]
        for finding in retired:
            lines.append(f"- ~~{finding.statement}~~")
            replacement = store.load_finding(finding.superseded_by)
            if replacement is not None:
                lines.append(f"  - Replaced by: {replacement.statement}")
        lines.append("")

    write_text(page, "\n".join(lines))
    return page


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def update(
    cfg: Config,
    concepts: dict[str, Concept],
    live: dict[str, Concept],
) -> dict[str, int]:
    """Refresh every note and rebuild the graph, from entities already derived.

    Takes the entities rather than deriving them: working out what the wiki
    contains is `enrich.concepts`' job, and drawing it is this one's. That is
    also what makes the promise in this package's docstring true -- nothing
    here writes to ``data/``.
    """
    cfg.layout.ensure()
    store = RecordStore(cfg.layout)
    # What the group settled, indexed by the entity it bears on. Retired
    # findings are left out: a note should show the current position, and the
    # superseded one stays readable in `wiki/findings.md` and on disk.
    settled: dict[str, list] = {}
    for finding in findings.live(store):
        for name in finding.concepts:
            settled.setdefault(slug_for(name), []).append(finding)

    # Two passes: the first creates the files so the second can link to them
    # (links are only emitted for notes that exist).
    for _ in range(2):
        for topic in cfg.topics:
            write_topic_note(cfg, topic, store)
        for concept in live.values():
            write_concept_note(cfg, concept, store, live, settled)

    write_index(cfg, concepts, live)
    write_findings_page(cfg, store)
    build_graph(cfg, live, settled)
    # The same graph, drawn. Reads the JSON just written, so the picture
    # cannot disagree with the data behind it.
    graph_page.build(cfg)

    # Remove notes for entities that are no longer promoted, unless a human
    # left content in them.
    removed = 0
    _, end_marker = _markers(cfg)
    for kind in KINDS:
        directory = cfg.layout.wiki_kind_dir(kind)
        for path in directory.glob("*.md"):
            concept = live.get(path.stem)
            if concept is not None and concept.kind == kind:
                continue
            tail = _preserved_tail(path, end_marker).strip()
            if tail and tail != DEFAULT_MANUAL_SECTION.strip():
                continue
            path.unlink(missing_ok=True)
            removed += 1

    stats = {
        "entities": len(concepts),
        "notes": len(live),
        "removed": removed,
        "topics": len(cfg.topics),
        "settled": len(findings.live(store)),
    }
    _LOG.info("wiki updated: %s", stats)
    return stats
