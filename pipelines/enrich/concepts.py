"""Wiki entities, derived from the readings.

Every summary names the concepts, methods and datasets it relied on. This is
where those names become records: accumulated in ``data/concepts/`` with the
evidence behind each one, and promoted to a note of their own once enough
independent sources have mentioned them.

The split this module exists to hold is between *derived* and *authored*. The
evidence, the kind and the co-occurrence links are derived, and are rebuilt from
scratch on every pass so that a deleted or re-read paper leaves no phantom
mention behind. The definition, the aliases and the ruled links are authored --
somebody read the sources and said what the entity is and what it sits next to
-- and are carried across every rebuild. An entity whose evidence has vanished
is dropped, unless it carries a definition, in which case the writing outlives
the evidence that prompted it.

Links are the one thing that exists on both sides, in two fields. ``related``
holds what appeared together in one summary and is rebuilt away; the entity a
reader would actually turn to next -- the previous generation of the same
system, the benchmark a method was built to beat -- rarely shares a summary with
it, so ``related_authored`` holds what somebody ruled and nothing derives. Two
fields rather than one because they need opposite lifetimes: merging them would
make every co-occurrence edge permanent, which is the phantom-mention failure
this module is built to prevent, moved from evidence to edges.

Deriving records is not rendering them. This lives under ``enrich/`` with the
rest of the code that writes to ``data/``, so that ``publish/`` can be what it
says it is: a pure function of the archive.
"""

from __future__ import annotations

import re

from ..common.config import Config
from ..common.log import get
from ..common.paths import slugify
from ..common.schema import Concept, utcnow
from ..common.store import RecordStore

_LOG = get(__name__)

KINDS = ("concept", "method", "dataset")
_KIND_RANK = {"concept": 1, "method": 2, "dataset": 3}
_RANK_KIND = {v: k for k, v in _KIND_RANK.items()}

_MERGE_STRIP = re.compile(r"[^a-z0-9]+")
_MERGE_YEAR = re.compile(r"^([a-z]+)(\d{2})$")


def slug_for(name: str) -> str:
    return slugify(name)


def _merge_key(name: str) -> str:
    """A coarser key than ``slug_for``, used only to notice that two spellings
    name the same benchmark instance.

    A reader names an exam sitting however the paper in front of them happens
    to: ``AIME 2024``, ``AIME24``, ``AIME2024``. ``slug_for`` keeps every one
    of those a distinct entity, because it must also keep ``AIME`` (no year)
    and ``AMC`` genuinely apart from each other. This key ignores punctuation
    and spacing and expands a bare two-digit trailing year to four digits, so
    the three spellings above collapse to one key while ``AIME`` and ``AMC``
    -- which carry no year at all -- do not collide with anything.

    Deliberately narrow: it does not attempt to merge a synonym that adds or
    drops a word (``Best-of-N`` vs. ``best-of-N sampling``) or an acronym in
    parentheses (``process reward model`` vs. ``process reward model (PRM)``)
    -- that needs editorial judgement, not a regular expression, and a wrong
    automatic merge would be worse than the fragmented pair it replaced.
    """
    base = _MERGE_STRIP.sub("", name.strip().lower())
    match = _MERGE_YEAR.fullmatch(base)
    if match:
        base = f"{match.group(1)}20{match.group(2)}"
    return base


def _canonical_slugs(previous: dict[str, Concept]) -> dict[str, str]:
    """Which slug speaks for each merge key, among what is already stored.

    A hand-written definition is a person's ruling on what this entity is;
    when several fragments of one entity each carry one, the fragment chosen
    here is preferred over the others on every later render, so evidence
    keeps landing in the same place instead of drifting with iteration order.
    Lacking that, the lexicographically smallest slug wins -- arbitrary, but
    fixed, which is what keeps a render from being an edit.
    """
    groups: dict[str, list[Concept]] = {}
    for concept in previous.values():
        groups.setdefault(_merge_key(concept.name), []).append(concept)
    canonical: dict[str, str] = {}
    for key, group in groups.items():
        defined = [c for c in group if c.definition.strip()]
        pick = min(defined or group, key=lambda c: c.slug)
        canonical[key] = pick.slug
    return canonical


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
    # Which stored slug a merge key already belongs to. Seeded from what is on
    # disk so a fragment merges into its established canonical slug from the
    # first render that knows about the merge, rather than waiting a cycle.
    merge_index = _canonical_slugs(previous)
    concepts: dict[str, Concept] = {}
    # Slugs whose kind was adjudicated by a definition task. A local set rather
    # than a field on Concept: the dataclass is serialized, and a bookkeeping
    # attribute would leak into the stored JSON.
    ruled: set[str] = set()

    def entity(name: str, kind: str) -> Concept | None:
        name = (name or "").strip()
        if len(name) < 2:
            return None
        raw_slug = slug_for(name)
        if not raw_slug:
            return None
        slug = merge_index.setdefault(_merge_key(name), raw_slug)
        concept = concepts.get(slug)
        if concept is None:
            old = previous.get(slug)
            # A merge can hand this call a slug it did not itself mine from
            # `name` -- the canonical spelling belongs to whichever record was
            # already on disk, not to whichever spelling happened to be seen
            # first in this pass.
            concept = Concept(
                slug=slug,
                name=old.name if old else name,
                kind=kind,
                definition=old.definition if old else "",
                aliases=list(old.aliases) if old else [],
                # Carried for the same reason the definition is: somebody ruled
                # on these, and nothing in the summaries can produce them again.
                # `related` is deliberately not carried — rebuilding it from
                # nothing is what stops a re-read paper leaving a phantom edge.
                related_authored=list(old.related_authored) if old else [],
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

    def link(slugs: list[str]) -> None:
        # De-duplicated, not merely filtered: a merge can make two names in
        # one summary's list resolve to the same slug, and that must not
        # count as an entity co-occurring with itself.
        unique = list(dict.fromkeys(s for s in slugs if s in concepts))
        for slug in unique:
            concept = concepts[slug]
            for other in unique:
                if other != slug and other not in concept.related:
                    concept.related.append(other)

    for paper in store.iter_papers():
        summary = store.load_paper_summary(paper.id)
        if summary is None:
            continue
        slugs: list[str] = []
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
                slugs.append(concept.slug)
        link(slugs)

    for video in store.iter_videos():
        summary = store.load_video_summary(video.id)
        if summary is None:
            continue
        slugs = []
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
                slugs.append(concept.slug)
        link(slugs)

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
