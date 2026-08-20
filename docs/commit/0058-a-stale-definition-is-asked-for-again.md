# 0058 — A stale definition is asked for again

| | |
| --- | --- |
| **Commit** | `feat(render): ask again for a definition its evidence has outgrown` |
| **Scope** | `pipelines/render.py`, `pipelines/common/llm.py`, `config/settings.yaml`, `tests/test_stale_refresh.py`, `CLAUDE.md`, `README.md` |
| **Kind** | feature |

## What changed

[Note 0021](0021-report-what-has-gone-stale.md) made staleness visible and
deliberately stopped there. Nothing acted on it, so the only route back was to
clear `definition` in `data/concepts/<slug>.json` and render — which throws the
previous ruling away along with the staleness.

`render` now files a **revision** task for the worst offenders, bounded, once a
definition's evidence has grown past a configured multiple of what it was
written against:

```yaml
wiki:
  refresh_definition_at: 2.0   # ask again once the evidence has doubled; 0 = off
  max_refresh_tasks: 5         # per render
```

The task carries the existing definition back to a reader with the question
*what has changed*. The record keeps that definition throughout.

## Why it is built this way

**The rule it must not break is the one `CLAUDE.md` already states**: a counter
must not discard written work on arithmetic alone. Nothing here rewrites or
clears anything. A refresh nobody answers leaves the archive byte-identical, and
that is the property that makes it safe to file one without being asked —
asserted directly by `test_the_definition_is_not_cleared`.

**A revision, not a blank page.** Somebody read the sources and ruled, and most
of a ruling is usually still right when its evidence grows. The old text goes
into the prompt *and* the payload — the payload copy so that what the reviser
was working from stays recoverable from the archived task afterwards. The prompt
says to keep what still holds, and that returning it unchanged is a real answer
because it records that somebody checked.

**A ratio, not any growth at all.** Staleness is a standing condition rather
than an event, so an unbounded response refills the queue every render. Three
sources standing at nine is describing a third of its evidence; forty standing
at forty-six is not, and re-asking there spends a reader's night on definitions
that are still true.

**A cap per render**, so a long-neglected archive drains over several passes,
worst first, instead of producing a backlog nobody will face. `stale_definitions`
already sorts by how far outgrown, so "worst first" costs nothing.

**Off by default.** A deployment that upgrades should not find its queue has
grown. The reporting has been there since 0021 and stays unconditional; only the
acting on it is opt-in.

**It runs after `queue_missing_definitions`.** An entity with no definition at
all is a worse gap than one whose definition is behind, and they share the
queue's cap.

## Trade-offs and rejected alternatives

**Considered: rewriting the definition automatically from the new sources.**
That is what the pipeline is structurally unable to do — it calls no model — and
would be wrong even if it could. The point of a definition is that somebody
ruled on it.

**Considered: clearing `definition` and letting `queue_missing_definitions` pick
it up.** One line, reuses everything, and it is the route being replaced: the
archive spends the interval between clearing and answering with no definition at
all, and if the task is never answered it has lost one permanently to a counter.

**`written_for` is floored at 1.** A recorded source count of zero would make
any ratio pass. A definition is written against at least one source or it is not
written.

**A refresh in flight suppresses the next one**, because `enqueue` refuses a
second pending task for the same entity — and, since note 0052, refreshes the
one that is there with the current sources. So the reader always sees every
source, including ones that arrived after the task was filed.

**Nothing measures whether revisions actually happen.** `definitions_reasked`
counts what was filed, not what came back. An archive that files five a night
and answers none looks the same in the log as one that answers them all; the
queue depth is where that shows, and `queue stats` already reports it.

## What a reviewer should check

Five mutations, each taking down its own test: remove the ratio (every trivial
growth re-asks), remove the cap (one render refills the queue), remove the
off-by-default guard, stop passing the previous definition (the reader gets a
blank page), and clear `definition` the way the old manual route did.

- `test_the_definition_is_not_cleared` is the one that matters. It is the whole
  difference between this and the route it replaces.
- `test_a_render_files_it_and_reports_it` builds six papers that genuinely name
  the entity, because `render` rebuilds concept records from summaries and a
  hand-made evidence list is replaced before this step ever sees it. The first
  version of that test used one and failed for that reason.

## Downstream impact

**Nothing changes until a deployment sets `refresh_definition_at`.** With it set,
the first render after the upgrade files up to `max_refresh_tasks` revision
tasks and reports them as `definitions_reasked`; the archive's records are
untouched either way.

`Summarizer.define_concept` gains a `previous` keyword with a default, so the
interface an API backend implements is unchanged for anyone not using it.
