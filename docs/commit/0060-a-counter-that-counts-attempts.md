# 0060 — A counter that counts attempts

| | |
| --- | --- |
| **Commit** | `fix(render): definitions_queued counts tasks filed, not attempts` |
| **Scope** | `pipelines/render.py`, `tests/test_local.py`, `docs/LOCAL-DELTAS.md` |
| **Kind** | fix |

## What changed

`queue_missing_definitions` now counts from the queue — `count_pending()` before
and after — instead of counting loop iterations that returned `None`.

## The failure

A render reported `definitions_queued: 4` and filed none.

```python
if summarizer.define_concept(concept.name, sources, cfg.language) is None:
    queued += 1
```

`define_concept` defers to the queue and returns `None`, which the loop reads as
"filed". But `Queue.add` refuses once the queue is at its cap and returns `""`,
and `define_concept` discards that return value. So `None` means *asked*, and
the counter has never been able to tell asked from filed.

It only diverges when the queue is full, which is exactly when the number
matters. Four entities crossed the promotion threshold after an alias merge, the
queue was holding forty freshly collected papers, and the render said the
definitions were queued. The queue said `pending_concepts: 0`. Nothing else
would ever have mentioned it — the refusal is logged at WARNING, once per task,
inside a run that emits one such line per skipped paper.

## Why this is the second time

`summaries_queued` had the same shape and was fixed when the definition-queue
reserve went in (note 0032): the summary path counts `queue_share.pending_count`
on either side rather than trusting a return value, and `docs/LOCAL-DELTAS.md`
records why. That correction was made three lines above this one and not applied
to it.

The two bugs are not the same — one double-counted a backlog across two passes,
this one counts refusals as successes — but the reason both exist is: these
functions return *how much work was found*, and every caller wants *how much
work was filed*. Where those differ, the reporting is wrong in the direction of
looking healthy.

## Why it is a delta

`render.py` is template-shaped and this is a fix to template code, so it is
registered in `docs/LOCAL-DELTAS.md` alongside the reserve it sits next to.
Losing it to a wholesale file replacement would restore a counter that reads
correctly on an idle queue and lies on a busy one — the class of regression the
register exists for.

The test lives in `tests/test_local.py`, next to the summary-counter test it is
a sibling of, for the same reason.

## What it does not fix

The underlying starvation. The reserve holds back half the cap for definitions
*within a render*, but a collection run fills the whole cap with reading first,
and the reserve has nothing to reserve. That is not new and it is not wrong —
reading is the bottleneck and the definitions queue as soon as slots free — but
it does mean `definitions_queued: 0` will be the normal reading after a large
collection, and now it will be the true one.
