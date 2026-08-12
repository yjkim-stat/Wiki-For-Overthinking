# A definition task asks for `related` and the same render throws it away

**Status:** solved 2026-08-12 by **option C** — see [Resolution](#resolution) at the
foot of this file and [note 0045](../commit/0045-a-ruled-link-is-not-derived-away.md).
**Kind:** fix · contract mismatch
**Found:** 2026-08-12, writing the definition for `Cosmos 3` in a deployed archive
**Touches:** `pipelines/common/llm.py`, `pipelines/enrich/queue.py`, `pipelines/enrich/apply.py`, `pipelines/enrich/concepts.py`, `tests/`

A concept task hands the reader an output schema with a `related` field in it.
The validator accepts what comes back, `apply` writes it to the record, and
`harvest` — later in the same `pipelines.render` invocation — rebuilds the record
without it. Every step reports success. Nothing anywhere says the field was
dropped.

This is not "harvest has a bug". Harvest is doing what it was designed to do.
The defect is that two halves of the system disagree about who owns `related`,
and the half that asks is the half a person interacts with.

---

## What you can observe

Answer any queued definition task with a `related` list and render:

```bash
export RA_WM_ROOT=/path/to/an/archive
cd /path/to/this/checkout

python3 -m pipelines.enrich.queue show concept__<slug>      # schema includes `related`
cat > /tmp/def.json <<'JSON'
{"kind": "method",
 "definition": "Two to four sentences.",
 "aliases": ["A Spelling Variant"],
 "related": ["Some Neighbour", "Another Neighbour"]}
JSON
python3 -m pipelines.enrich.queue complete concept__<slug> --file /tmp/def.json
python3 -m pipelines.render

python3 -c "import json; d=json.load(open('$RA_WM_ROOT/data/concepts/<slug>.json')); \
print('definition:', bool(d['definition'])); print('aliases:', d['aliases']); \
print('related has them:', [n for n in ('some-neighbour','another-neighbour') if n in d['related']])"
```

`definition` is written. `aliases` is written. `related` contains neither name —
only whatever co-occurrence had already put there.

**The case that found it.** `concept__cosmos-3` was answered with seven curated
neighbours, six of them the entity's own sibling generations. None survived.
What the note links to instead, because those names happened to appear in the
same summary, includes `Epic-Kitchens`, `Kinetics` and `Jetson Thor`. What it
does not link to is `cosmos-predict1`, `cosmos-reason1`, `cosmos-transfer1` or
`cosmos-policy` — and it never will, because no single paper summary lists two
Cosmos generations in its `concepts`/`methods`/`datasets` arrays, which is the
only thing that can create a link.

---

## Why it happens

Three places, in the order they run.

**1. The schema advertises the field.** `pipelines/common/llm.py:121`, inside
`CONCEPT_OUTPUT_SCHEMA`:

```python
"related": ["string - names of neighbouring entities worth linking"],
```

**2. The validator and `apply` honour it.** `pipelines/enrich/queue.py:59` lists
`related` among the concept task's optional list fields:

```python
"concept": ["aliases", "related"],
```

and `pipelines/enrich/apply.py:172-175` appends each slug to the stored record:

```python
for related in result.get("related") or []:
    related_slug = slug_for(related)
    if related_slug and related_slug not in concept.related:
        concept.related.append(related_slug)
```

At this point the record on disk is correct. `python3 -m pipelines.render`
then continues.

**3. `harvest` rebuilds the record and does not carry `related` over.**
`pipelines/render.py:404` calls `concepts_mod.rebuild(cfg)`, which calls
`harvest(cfg)`. For each entity, `pipelines/enrich/concepts.py:95` constructs a
**fresh** `Concept`, carrying across exactly four things from the stored record:

```python
concept = Concept(
    slug=slug,
    name=name,
    kind=kind,
    definition=old.definition if old else "",
    aliases=list(old.aliases) if old else [],
    first_seen=old.first_seen if old else utcnow(),
)
```

`related` is absent from that list, so it starts empty and is then filled
entirely by `link()` at `pipelines/enrich/concepts.py:117-123`, which connects
names appearing together in one summary:

```python
def link(names: list[str]) -> None:
    slugs = [slug_for(n) for n in names if slug_for(n) in concepts]
    for slug in slugs:
        concept = concepts[slug]
        for other in slugs:
            if other != slug and other not in concept.related:
                concept.related.append(other)
```

`_same()` then compares old against new and writes the file because it changed —
so the discard is committed, not merely computed.

**This is deliberate, and the module says so.** From the docstring at the top of
`pipelines/enrich/concepts.py`:

> The split this module exists to hold is between *derived* and *authored*. The
> evidence, the kind and the links between entities are derived, and are rebuilt
> from scratch on every pass so that a deleted or re-read paper leaves no phantom
> mention behind. The definition and the aliases are authored — somebody read the
> sources and ruled on what the entity is — and are carried across every rebuild.

So `related` is on the derived side on purpose, and rebuilding it from scratch is
the behaviour that keeps a deleted paper from leaving a phantom edge behind.
**The bug is that the task schema asks for a derived field anyway.** Fix the
disagreement, not the harvest.

---

## Why it matters more than a dropped list

`related` is not decoration. It is read in two places in `pipelines/publish/`:

- `wiki.py:140-145` renders the **Related** line on every note.
- `wiki.py:308` builds the edges of `wiki/graph.html`.

Deriving it purely from single-summary co-occurrence gives those two artifacts a
specific and wrong shape: an entity is linked to whatever shared a bibliography
slot with it, and cannot be linked to the thing a reader would actually navigate
to next. Sibling versions of one system, a method and the benchmark it was
designed to defeat, a dataset and its successor — none of these reliably co-occur
inside a single summary's flat name lists, and no amount of reading fixes that.

It also fails in the direction the archive cares least for: silently, and with
every counter looking healthy. The definition task returns success, the render
returns success, and the note renders with a full-looking Related line.

---

## The precedent this repository already set

`kind` had exactly this shape and was solved in
[note 0015](../commit/0015-a-ruled-kind-defends-itself.md): a derived field that
a definition task was also allowed to rule on, where the next harvest overwrote
the ruling. The fix kept the field derived by default and gave the authored
ruling a way to defend itself — the `ruled` set in `harvest`, gated on the entity
having a stored definition (`pipelines/enrich/concepts.py:105-112`):

```python
if old and old.definition:
    concept.kind = old.kind
    ruled.add(slug)
...
if slug not in ruled:
    concept.kind = _upgrade_kind(concept.kind, kind)
```

Whatever is chosen below should be consistent with that precedent rather than
inventing a third pattern for the same problem.

---

## Options

### A. Stop asking. Remove `related` from the concept task.

Delete it from `CONCEPT_OUTPUT_SCHEMA` (`llm.py:121`), from `_LIST_FIELDS`
(`queue.py:59`), and delete the loop in `apply.py:172-175`.

- **For:** smallest change; makes the code match its own documented design; no
  new field, no migration, no merge semantics to get wrong. Nobody is misled
  again.
- **Against:** the navigation problem stays unsolved and becomes explicitly
  out of scope. Notes go on linking to whatever shared a summary with them.
- **Cost if wrong:** none that is silent. A reader who wants to link two
  entities now has no route, and will notice immediately.

### B. Make `related` authored *and* derived, carried like `aliases`.

Add `related=list(old.related) if old else []` to the `Concept(...)` construction
at `concepts.py:95`, so authored links persist and `link()` unions onto them.

- **For:** one line; the task schema becomes truthful immediately.
- **Against:** **it breaks the property the module exists to protect.** Derived
  edges would become permanent too: re-read a paper so that two names no longer
  appear together, and the edge they created survives forever with nothing able
  to remove it. That is the phantom-mention failure the docstring names, moved
  from evidence to edges. Do not take this option without solving that.

### C. Two fields: derived links stay derived, authored links are carried.

Add `related_authored: list[str]` to `Concept`
(`pipelines/common/schema.py:197-214`), have `apply` write the task's answer
there instead of into `related`, carry it across the rebuild the way `definition`
and `aliases` are carried, and have `publish/wiki.py` render the union of the two
(`wiki.py:140` and `wiki.py:308`).

- **For:** keeps the derived/authored split the module is built around, so a
  re-read paper still drops its derived edges while a person's link survives.
  Matches the note-0015 precedent: authored judgement defends itself, derived
  data stays disposable. An authored link can be retracted by answering again.
- **Against:** a schema field, a `SCHEMA_VERSION` decision, and two call sites in
  `publish/` that must union rather than read one list. Records written before
  the change have no such key and must default to `[]` rather than being
  migrated — check how `_Record` handles unknown/missing keys before assuming
  this is free.

**Recommendation: A now, C if the group wants curated links.** A is correct as
it stands — the schema is lying today and that is the whole defect. C is the
right shape for the feature, but it is a feature, and it should not be smuggled
in as a bug fix. B should be rejected outright; it trades a silent discard for a
silent accumulation, which is worse.

---

## Tests

There are none. `grep -rn "related" tests/` returns four hits and every one is
the substring inside `rel="related"`, `Unrelated Chemistry Paper` and
`unrelated nonsense`. **The round-trip has never been covered**, which is why the
mismatch survived. Whichever option is taken, add:

1. **The round-trip, asserted end to end.** Complete a concept task carrying
   `related`, run the full `render`, then assert on the stored record. Under A
   the assertion is that the validator *rejects* an unexpected `related` key, or
   that no such key is accepted; under C it is that the authored slugs are still
   present after the render.
2. **A regression on the derived side.** Two entities that co-occur in one
   summary are linked; remove one from the summary, re-render, and assert the
   edge is gone. This is the property option B would break, and nothing guards it
   today.
3. **Under C only:** an authored link to an entity that has no note is not
   rendered (`wiki.py:141` already filters on `slug in all_concepts`; keep it),
   and answering a second time with `[]` retracts.

`tests/sandbox.py` builds the fixture archive these should run against.

---

## What a reviewer should check

- The chosen option leaves `pipelines/enrich/concepts.py`'s docstring true. If
  the code and that paragraph disagree after the change, one of them is the bug.
- No path can still accept a field it will discard. That is the actual defect;
  a fix that leaves the schema advertising `related` while harvest drops it has
  not fixed anything.
- `python3 -m pipelines.render` twice in a row on an unchanged archive still
  produces no diff. `_same()` at `concepts.py:54-65` and the write block at
  `concepts.py:177-189` exist to guarantee that, and both options touch the
  records they compare.
- Under C, `wiki/graph.html` edge count changes only by the authored links.
  `wiki.update` reports `entities` and `notes`; the graph edge count is logged by
  `publish/graph_page.py`.

## Notes for whoever picks this up

- A deployed archive already contains records whose `related` was written by a
  definition answer and then discarded. Nothing needs migrating — those lists are
  already back to their derived state. Under C they simply start empty.
- The finding is recorded on the archive side as well, so the two repositories
  agree on what was observed: `wiki/findings.md`, entry
  `finding:b184dd02fcd823ce`, established 2026-08-12.

---

## Resolution

**Option C, taken whole.** The group wanted curated links, so the feature was
built rather than the schema trimmed. `Concept.related_authored` holds what a
definition task rules; `related` stays derived and is still rebuilt from nothing
every harvest; `Concept.neighbours` unions the two and both `publish/` call
sites read that instead of `related`.

Commit `feat(enrich): a ruled link is not derived away`, note
[0045](../commit/0045-a-ruled-link-is-not-derived-away.md).

Answers to the questions this document left open:

- **Replace, not accumulate.** `apply` sets `related_authored` to the answer
  rather than appending, so answering again with `[]` retracts. A result that
  omits the key entirely leaves the stored links alone — absent is a different
  answer from empty.
- **`SCHEMA_VERSION` was not bumped.** Nothing in `pipelines/` reads it; a
  record missing the key loads with `[]` through `_Record.from_dict`, which is
  asserted by `test_a_record_written_before_the_field_loads_with_it_empty`.
- **Self-links are dropped** in `neighbours`. Co-occurrence cannot produce one,
  but an answer naming the entity itself can, and it renders as a note linking
  to itself.

All three tests this document asked for exist, in
`tests/test_related_links.py`, and each was checked against a deliberate
mutation. The one that mattered: the first version of the note-rendering test
asserted on a neighbour that *also* co-occurred, so it passed even with the
renderer reading `related` alone. The fixture now carries a fourth entity that
co-occurrence can never reach, which is the only shape that tells the union
apart from the derived list.

The docstring at the top of `pipelines/enrich/concepts.py` was rewritten in the
same commit — it named links as purely derived, and this change made that false.
This document's own reviewer checklist is what caught it.
