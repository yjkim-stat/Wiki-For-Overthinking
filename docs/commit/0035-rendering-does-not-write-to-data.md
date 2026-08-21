# 0035 — Rendering does not write to `data/`

| | |
| --- | --- |
| **Commit** | `refactor: move deriving records out of the renderers` |
| **Scope** | `pipelines/enrich/concepts.py`, `pipelines/enrich/apply.py`, `pipelines/publish/wiki.py`, `pipelines/publish/__init__.py`, `pipelines/render.py`, `tests/test_layering.py`, `CLAUDE.md` |
| **Kind** | refactor · breaking (internal API) |

## What changed

Two blocks of code moved down a layer, and the boundary they were crossing is
now enforced by tests.

| Moved from | To | What it is |
| --- | --- | --- |
| `publish/wiki.py` — `harvest`, `promoted`, `undefined_concepts`, `slug_for`, `KINDS` (156 lines) | `enrich/concepts.py` | Deriving wiki entities from the readings and writing them to `data/concepts/` |
| `render.py` — `_apply_*`, `apply_completed` (169 lines) | `enrich/apply.py` | Folding a finished queue result into the records |

`wiki.update(cfg)` becomes `wiki.update(cfg, concepts, live)`: it is handed the
entities instead of deriving them. `render.py` calls `enrich.concepts.rebuild()`
and passes the result on.

The rule that now holds: **only `collect/` and `enrich/` write to `data/`.**
`publish/` is a pure function of it.

## Why it is built this way

**A deployment replaces the code and keeps the archive.** That is the whole
shape of this repository — it is copied into projects that then run it for
months, and the thing that must survive an upgrade is `data/`. The separation
only means anything if it is real at the level of *which module holds the
write*, because that is what a future change edits.

It was not real. `publish/wiki.py::harvest` derived the concept records and
saved them, so the renderer wrote to the source of truth — and `render --only
wiki` would *delete* a record whose evidence had gone:

```
before   : ['orphaned-idea']
after    : []            # render --only wiki
```

Meanwhile `publish/__init__.py` said, in its first line, "Everything here is a
pure function of `data/`". The package's docstring was false about its largest
module, and nothing looked wrong from outside.

**Deriving is not drawing.** `harvest` reads every summary and produces
entities — the same shape of operation `dedupe` performs on papers, and it
belongs in the same place. What is left in `publish/wiki.py` is 440 lines that
turn entities into markdown, which is what a renderer is for.

**The split inside a concept record is what makes this subtle.** A concept is
half derived (evidence, kind, links — rebuilt from scratch every pass) and half
authored (the definition and aliases somebody wrote after reading the sources).
That is why `harvest` cannot simply be deleted or made read-only, and why it
carries authored fields across every rebuild and keeps a record whose evidence
has vanished if it has a definition. Naming the module `enrich/concepts.py` and
saying this in its docstring makes the rule findable; it used to be spread
across three comments in a renderer.

**The boundary is tested, not trusted.** `tests/test_layering.py` snapshots
every file under `data/` by content, runs each renderer, and asserts the
snapshot is unchanged. A static tripwire also fails if any module under
`publish/` so much as mentions `store.save_*`, which catches a write on a path
no fixture reaches. Neither test would have passed before this change.

## Trade-offs and rejected alternatives

**`wiki.update` gained two parameters.** A caller must now derive first. That is
the point — the two steps were fused, and fusing them is what let a render
mutate the archive — but it is a worse signature for a casual caller, and
`enrich.concepts.rebuild()` exists to make the common path one line.

**Rejected: leaving `harvest` where it was and marking it read-only.** It cannot
be read-only. Entities *are* derived data that must be rewritten when the
readings change. The fix is to move the write, not to remove it.

**Rejected: re-exporting `render.apply_completed` and `wiki.harvest` as
aliases.** They would keep the old shape discoverable and reachable, which is
exactly what a boundary is for preventing. The names are internal; the CLI is
the interface and it is unchanged.

**Cost: 329 lines moved, so `git log --follow` on those functions is now two
hops.** The move is verbatim — bodies were extracted programmatically rather
than retyped — so a `git log -S` on any line in them still finds the history.

## What a reviewer should check

- **That the move is behaviour-preserving.** 395 existing tests pass unchanged
  apart from two files that referenced the moved names by their old path.
- **One real regression, which the suite caught.** `_apply_concept` held a
  function-local `from .publish.wiki import slug_for` — a sideways reach that
  existed only to dodge a cycle, and itself evidence of the wrong layering. It
  moved with the body and resolved to `pipelines.enrich.publish`, so every
  definition silently failed to apply. It failed *silently* because
  `completed()` catches `Exception` per task and counts it as `skipped`; only
  `test_definition_reaches_the_note` showed it. That broad catch is deliberate —
  one bad result must not block the rest — but it means an import error in an
  applier looks like a bad task. Worth remembering.
- **`tests/test_layering.py` itself.** Break it deliberately: put
  `store.save_concept(concept)` back in `publish/wiki.py` and both the
  behavioural and the static test should fail.

## Downstream impact

**Breaking for anything importing these by name**, which in practice means
nothing: the CLI (`python3 -m pipelines.render`) is unchanged, and so is every
file under `data/`. If a deployment has its own code calling them:

| Was | Now |
| --- | --- |
| `render.apply_completed(cfg)` | `pipelines.enrich.apply.completed(cfg)` |
| `wiki.harvest(cfg)` | `pipelines.enrich.concepts.harvest(cfg)` |
| `wiki.promoted(cfg, c)` | `pipelines.enrich.concepts.promoted(cfg, c)` |
| `wiki.undefined_concepts(cfg, l)` | `pipelines.enrich.concepts.undefined_concepts(cfg, l)` |
| `wiki.slug_for(name)` | `pipelines.enrich.concepts.slug_for(name)` |
| `wiki.update(cfg)` | `wiki.update(cfg, *concepts.rebuild(cfg))` |

No records change and nothing is regenerated differently. A `render` after
pulling this produces the same archive it would have before.
