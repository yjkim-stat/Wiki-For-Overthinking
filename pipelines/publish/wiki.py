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

from pathlib import Path

from ..common.config import Config
from ..common.log import get
from ..common.paths import Layout, slugify
from ..common.schema import Concept, utcnow
from ..common.store import RecordStore, write_json, write_text
from ..enrich import findings
from . import graph_page, load_template, rel_link, render_template
from .archive import paper_dir, seminar_dir

_LOG = get(__name__)

KINDS = ("concept", "method", "dataset")
_KIND_RANK = {"concept": 1, "method": 2, "dataset": 3}
_RANK_KIND = {v: k for k, v in _KIND_RANK.items()}

DEFAULT_MANUAL_SECTION = """## Notes

_Anything below the marker above is yours. It is never overwritten._
"""


def slug_for(name: str) -> str:
    return slugify(name)


def note_path(layout: Layout, kind: str, slug: str) -> Path:
    return layout.wiki_kind_dir(kind) / f"{slug}.md"


def topic_note_path(layout: Layout, slug: str) -> Path:
    return layout.wiki_kind_dir("topic") / f"{slug}.md"


# ---------------------------------------------------------------------------
# Harvesting entities from summaries
# ---------------------------------------------------------------------------


def _upgrade_kind(current: str, incoming: str) -> str:
    """A name seen as a dataset is a dataset, even if also called a concept."""
    return _RANK_KIND[max(_KIND_RANK.get(current, 1), _KIND_RANK.get(incoming, 1))]


def _add_evidence(concept: Concept, kind: str, item_id: str, title: str, note: str) -> None:
    for existing in concept.evidence:
        if existing.get("kind") == kind and existing.get("id") == item_id:
            return
    concept.evidence.append(
        {"kind": kind, "id": item_id, "title": title, "note": note}
    )


def harvest(cfg: Config) -> dict[str, Concept]:
    """Rebuild the concept records from every stored summary.

    Rebuilt from scratch each time rather than updated in place: evidence is
    derived data, and deriving it fresh keeps a deleted or re-summarized paper
    from leaving a phantom mention behind. Hand-written definitions live in the
    stored record and are carried over.
    """
    layout = cfg.layout
    store = RecordStore(layout)

    previous = {c.slug: c for c in store.iter_concepts()}
    concepts: dict[str, Concept] = {}
    # Slugs whose kind was adjudicated by a definition task. A local set rather
    # than a field on Concept: the dataclass is serialized, and a bookkeeping
    # attribute would leak into the stored JSON.
    ruled: set[str] = set()

    def entity(name: str, kind: str) -> Concept | None:
        name = (name or "").strip()
        if len(name) < 2:
            return None
        slug = slug_for(name)
        if not slug:
            return None
        concept = concepts.get(slug)
        if concept is None:
            old = previous.get(slug)
            concept = Concept(
                slug=slug,
                name=name,
                kind=kind,
                definition=old.definition if old else "",
                aliases=list(old.aliases) if old else [],
                first_seen=old.first_seen if old else utcnow(),
            )
            concepts[slug] = concept
            # A stored definition means somebody ruled on what this entity is,
            # over the whole evidence set. The harvested kind is a side effect
            # of which list each summary happened to put the name in, so it
            # must not overrule that judgement on the next render.
            if old and old.definition:
                concept.kind = old.kind
                ruled.add(slug)
        if slug not in ruled:
            concept.kind = _upgrade_kind(concept.kind, kind)
        if name != concept.name and name not in concept.aliases:
            concept.aliases.append(name)
        concept.last_seen = utcnow()
        return concept

    def link(names: list[str]) -> None:
        slugs = [slug_for(n) for n in names if slug_for(n) in concepts]
        for slug in slugs:
            concept = concepts[slug]
            for other in slugs:
                if other != slug and other not in concept.related:
                    concept.related.append(other)

    for paper in store.iter_papers():
        summary = store.load_paper_summary(paper.id)
        if summary is None:
            continue
        names: list[str] = []
        for kind, values in (
            ("concept", summary.concepts),
            ("method", summary.methods),
            ("dataset", summary.datasets),
        ):
            for name in values:
                concept = entity(name, kind)
                if concept is None:
                    continue
                _add_evidence(
                    concept, "paper", paper.id, paper.title, summary.one_liner
                )
                for slug in paper.topics:
                    if slug not in concept.topics:
                        concept.topics.append(slug)
                names.append(name)
        link(names)

    for video in store.iter_videos():
        summary = store.load_video_summary(video.id)
        if summary is None:
            continue
        names = []
        for kind, values in (
            ("concept", summary.concepts),
            ("method", summary.methods),
            ("dataset", summary.datasets),
        ):
            for name in values:
                concept = entity(name, kind)
                if concept is None:
                    continue
                _add_evidence(
                    concept, "video", video.id, video.title, summary.one_liner
                )
                for slug in video.topics:
                    if slug not in concept.topics:
                        concept.topics.append(slug)
                names.append(name)
        link(names)

    # Drop records whose evidence has disappeared entirely, unless somebody
    # wrote a definition for them by hand.
    for slug, old in previous.items():
        if slug not in concepts and old.definition:
            concepts[slug] = old

    for concept in concepts.values():
        store.save_concept(concept)

    stale = set(previous) - set(concepts)
    for slug in stale:
        store.concept_path(slug).unlink(missing_ok=True)

    _LOG.info("harvested %d entities from summaries", len(concepts))
    return concepts


def promoted(cfg: Config, concepts: dict[str, Concept]) -> dict[str, Concept]:
    """Entities with enough independent evidence to deserve their own note."""
    threshold = int(
        (cfg.settings.get("wiki", {}) or {}).get("promote_after_mentions", 2)
    )
    return {
        slug: concept
        for slug, concept in concepts.items()
        if concept.mention_count >= threshold or concept.definition
    }


# ---------------------------------------------------------------------------
# Note rendering
# ---------------------------------------------------------------------------


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


def _write_note(cfg: Config, path: Path, title: str, auto_body: str) -> Path:
    begin, end = _markers(cfg)
    tail = _preserved_tail(path, end)
    template = load_template(cfg.layout.templates, "wiki", "note.md")
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
        all_concepts[slug] for slug in sorted(set(concept.related)) if slug in all_concepts
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
    return _write_note(cfg, page, concept.name, "\n".join(body))


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
        for slug in concept.related:
            other = live.get(slug)
            if other is None:
                continue
            target = f"{other.kind}:{other.slug}"
            pair = tuple(sorted((source, target)))
            if pair in seen_pairs:
                continue
            seen_pairs.add(pair)
            edges.append({"source": source, "target": target, "type": "co-occurs"})

    path = cfg.layout.wiki_meta / "graph.json"
    write_json(
        path,
        {
            "generated_at": utcnow(),
            "nodes": sorted(nodes, key=lambda n: n["id"]),
            "edges": sorted(edges, key=lambda e: (e["source"], e["target"], e["type"])),
        },
    )
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


def update(cfg: Config) -> dict[str, int]:
    """Harvest entities, refresh every note, rebuild the graph."""
    cfg.layout.ensure()
    store = RecordStore(cfg.layout)

    concepts = harvest(cfg)
    live = promoted(cfg, concepts)
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


def undefined_concepts(cfg: Config, live: dict[str, Concept]) -> list[Concept]:
    """Promoted entities still waiting for a definition."""
    return [c for c in live.values() if not c.definition.strip()]
