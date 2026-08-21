# 0022 — A reading backlog starved the wiki

| | |
| --- | --- |
| **Commit** | `fix(render): reserve queue slots so definitions are not crowded out` |
| **Scope** | `pipelines/render.py`, `tests/test_render.py` |
| **Kind** | fix |

## What changed

`render` queues paper summaries first and wiki definitions second, against one
shared `max_pending_tasks` cap. Summaries now take at most half the cap on that
first pass; definitions are queued next against the full cap; whatever the
definitions did not use is handed back to summaries immediately afterwards.

## Why this had to exist

With any reading backlog at all, summaries consumed every slot and no definition
task was ever filed. In this deployment, one render generated 82 definition
tasks and queued none of them — the log said so 82 times, at WARNING level,
inside a run that otherwise reported success:

```
queue is at its cap of 40 pending tasks; skipping concept__token-selection
...
render complete: {... 'definitions_queued': 82 ...}
```

The count in the result is what was *generated*, not what was filed, so the run
looked like it had queued 82 definitions while the queue held zero.

The failure is worst exactly when it matters most. A repository collecting
actively always has unread papers, so the wiki stops extending itself precisely
during the periods it is accumulating the most evidence — and the self-extending
wiki is the feature the promotion threshold exists to serve. It only recovered
here because the reading queue was drained to zero by hand.

## Why it is built this way

**A reserve, not a reordering.** Queueing definitions first would invert the
starvation: a large definition backlog would then stop papers being read. Both
kinds of work have to make progress, so the cap is split rather than reordered.

**The reserve is returned, so it costs nothing when unused.** Half the cap is
withheld and then given straight back if definitions did not want it. A render
with no pending definitions queues exactly as many summaries as before this
change, which is what makes the reserve safe to set generously.

**Rounded in favour of reading.** `(cap + 1) // 2` gives the odd slot to
summaries. Definitions are generated *from* completed summaries, so the
definition backlog is bounded by work already done and drains; the reading
backlog is fed by collection and does not. The bounded queue can afford to wait.

**No new configuration.** A `max_definition_tasks` setting would be a second
number that has to be kept consistent with the first, and the useful behaviour —
neither starves — does not need tuning.

## Trade-offs and rejected alternatives

- *Raising `max_pending_tasks` instead.* Rejected: it delays the collision
  rather than removing it, and the cap exists to keep a reader's queue
  answerable in one sitting.
- *Queueing definitions before summaries.* Rejected above — it swaps which kind
  of work starves.
- *Making the skip an error rather than a warning.* Rejected: hitting the cap is
  normal and expected. The defect was that one kind of work could never reach
  it, not that the cap was reported quietly.
- *A single interleaved pass over both kinds of work.* Cleaner in principle and
  a larger change: the two are produced by different stages of `render` with the
  archive rebuild between them, and merging them would couple those stages.

## What a reviewer should check

- `python3 -m unittest discover -s tests -t .` — 193 tests, with
  `DefinitionQueueShareTests` covering the split, the odd-cap rounding and the
  no-cap case.
- `render --only wiki` must still work. An earlier version of this change added
  the returned reserve unconditionally and raised `KeyError: 'summaries_queued'`
  under `--only wiki`, where the archive stage never ran to withhold anything.
  An existing test caught it; that test is the one to keep.
- The invariant worth confirming by hand: with no definitions pending, the
  number of summaries queued by a render is unchanged from before this commit.

## Downstream impact

None to configure. A deployment with a standing reading backlog will start
filing definition tasks it was silently dropping, so the first render after
pulling may queue a batch of wiki definitions that had accumulated — in this
deployment that backlog had reached 82.
