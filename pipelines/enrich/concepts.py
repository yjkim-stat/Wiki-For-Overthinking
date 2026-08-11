"""Wiki entities, derived from the readings.

Every summary names the concepts, methods and datasets it relied on. This is
where those names become records: accumulated in ``data/concepts/`` with the
evidence behind each one, and promoted to a note of their own once enough
independent sources have mentioned them.

The split this module exists to hold is between *derived* and *authored*. The
evidence, the kind and the links between entities are derived, and are rebuilt
from scratch on every pass so that a deleted or re-read paper leaves no phantom
mention behind. The definition and the aliases are authored -- somebody read the
sources and ruled on what the entity is -- and are carried across every rebuild.
An entity whose evidence has vanished is dropped, unless it carries a
definition, in which case the writing outlives the evidence that prompted it.

Deriving records is not rendering them. This lives under ``enrich/`` with the
rest of the code that writes to ``data/``, so that ``publish/`` can be what it
says it is: a pure function of the archive.
"""

from __future__ import annotations

from ..common.config import Config
from ..common.log import get
from ..common.paths import slugify
from ..common.schema import Concept, utcnow
from ..common.store import RecordStore

_LOG = get(__name__)

KINDS = ("concept", "method", "dataset")
_KIND_RANK = {"concept": 1, "method": 2, "dataset": 3}
_RANK_KIND = {v: k for k, v in _KIND_RANK.items()}


def slug_for(name: str) -> str:
    return slugify(name)


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


def _same(old: Concept, new: Concept) -> bool:
    """Do these describe the same entity, ignoring when it was last written?

    `last_seen` is the one field that would differ on every pass by
    construction, so comparing without it is what turns "the harvest ran" into
    "something actually changed".
    """
    before, after = old.to_dict(), new.to_dict()
    before.pop("last_seen", None)
    after.pop("last_seen", None)
    return before == after


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

    written = 0
    for concept in concepts.values():
        old = previous.get(concept.slug)
        if old is not None and _same(old, concept):
            # Nothing about this entity moved, so nothing about its record
            # should. Writing a fresh `last_seen` here would mean every render
            # rewrote every concept file -- a whole archive's worth of diff
            # that records when the code last ran, not when anything was seen.
            continue
        concept.last_seen = utcnow()
        store.save_concept(concept)
        written += 1

    stale = set(previous) - set(concepts)
    for slug in stale:
        store.concept_path(slug).unlink(missing_ok=True)

    _LOG.info(
        "harvested %d entities from summaries; %d record(s) changed",
        len(concepts),
        written,
    )
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


def undefined_concepts(cfg: Config, live: dict[str, Concept]) -> list[Concept]:
    """Promoted entities still waiting for a definition."""
    return [c for c in live.values() if not c.definition.strip()]


def rebuild(cfg: Config) -> tuple[dict[str, Concept], dict[str, Concept]]:
    """``(every entity, those promoted to a note)``.

    The one call a renderer needs, so that deciding what the wiki contains
    stays here and drawing it stays there.
    """
    concepts = harvest(cfg)
    return concepts, promoted(cfg, concepts)
