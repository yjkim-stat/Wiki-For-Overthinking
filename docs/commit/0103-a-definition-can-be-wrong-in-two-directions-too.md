# 0103 — A definition can be wrong in two directions too

| | |
| --- | --- |
| **Commit** | `fix(render): a definition whose evidence left is stale too` |
| **Scope** | `pipelines/render.py`, `tests/test_render.py`, `tests/test_stale_refresh.py` |
| **Kind** | fix |

## What changed

`stale_definitions` reported a definition whose evidence had *grown* past the
count it was written against — `now > written_for`. It now reports any
disagreement, and each row carries a `direction` of `outgrown` or
`over-declared`. The render log line names the direction.

This is [0090](0090-a-marker-can-be-wrong-in-two-directions.md) applied to the
other counter. That note made the analysis marker symmetric and left the
definition counter as it was; this closes the pair.

## Why the other direction is not harmless

Evidence leaves as well as arrives. A paper is discarded, retopiced, or folded
into another entity by the alias map, and the definition written against it
keeps every sentence it had. What it now describes is material the archive no
longer holds — and unlike a thin definition, nothing about it looks wrong. It
reads as complete, names its sources, and cites numbers. A reader who tries to
follow it finds nothing, and the prose does not say which part has gone.

That is worse than describing too few sources, which is the case the counter
already caught.

## It found two, and they were not hypothetical

`chain-of-thought-distillation` and `out-of-distribution-generalization` both
described a paper called TabRank in circumstantial detail — its training set,
its four evaluation subsets, its metric. TabRank is not in the archive. It is
in the history: discarded in `a2daecfa archive: discard 90 readings that no
overthinking claim rests on`. The definitions were written before that pass and
were never revisited, because nothing counted downward.

Both were cleared by hand, which `CLAUDE.md` sanctions for a definition that is
wrong rather than merely behind. On this archive the new direction surfaces 56
over-declared definitions against 148 outgrown ones — a population that had
been invisible.

## Why it does not also re-ask for them

`queue_stale_definitions` files a refresh task when evidence has grown past
`wiki.refresh_definition_at`. A shrunken row cannot pass that ratio, so it is
reported and never queued, and the change leaves that alone deliberately rather
than by accident — `test_a_definition_whose_evidence_left_is_never_asked_again`
pins it so a later change to the ratio cannot quietly undo it.

The asymmetry is the point. A definition whose sources grew is *behind*, and
handing it back with "what has changed" is a fair question that leaves the
archive unchanged if nobody answers. One whose sources were deleted may be
*wrong*, and the route for wrong is to clear it and re-derive — which destroys
authored text, and so is a person's call and not arithmetic's.

## Trade-offs and rejected alternatives

**Rejected: queue the shrunken ones too.** It would put a reader in front of a
definition whose material is gone and ask "what has changed", which is not the
question. The honest question is "is this still about anything", and that is a
decision to clear, which this repository does not automate.

**Rejected: a separate counter.** `stale.definitions` now mixes the two
directions in one number, as `stale.analysis` already does. A second key would
have to be threaded through the render result, the digest and the daily page for
a distinction the log line already carries.

The cost is that `stale.definitions` jumped on this archive the moment the
change landed, without anything having got worse. That is the same one-off step
0090 paid.

## What a reviewer should check

- `python3 -m pipelines.render` — `stale.definitions` now counts both; the log
  line ends with `(outgrown)` or `(over-declared)`.
- The equal case is still silent: `test_a_definition_still_matching_its_evidence_is_not`.
- An entity with no definition is still never reported, in either direction.
- Sorting still puts the most outgrown first, because `queue_stale_definitions`
  walks the list worst-first under a cap:
  `test_the_outgrown_end_still_sorts_first`.

## Downstream impact

A deployment that pulls this will see `stale.definitions` rise by however many
of its definitions were written against evidence that has since been removed.
Nothing is rewritten and no task is filed for them, so the only action required
is reading the new warnings. No config change.
