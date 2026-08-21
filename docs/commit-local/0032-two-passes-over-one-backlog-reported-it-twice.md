# 0032 — Two passes over one backlog reported it twice

| | |
| --- | --- |
| **Commit** | `fix(render): count summary tasks filed, not passes over the backlog` |
| **Scope** | `pipelines/local/queue_share.py`, `pipelines/render.py`, `tests/test_local.py`, `docs/LOCAL-DELTAS.md` |
| **Kind** | fix · reporting |

## What changed

`render` now measures the pending queue on either side of each
`queue_missing_summaries` call and reports the difference, instead of summing
what the two calls return. New helper: `queue_share.pending_count`.

## The bug

Note 0022 split the pending cap so a reading backlog could not starve the
wiki's definition tasks. It did that by calling `queue_missing_summaries`
twice — once against half the cap, once with the remainder — and adding the
returns:

```python
result["summaries_queued"] = queue_missing_summaries(cfg, summary_cap(cfg))
...
result["summaries_queued"] += queue_missing_summaries(cfg)
```

But that function does not return how many tasks it filed. It walks every
stored record, asks the summarizer for a summary, and counts the ones that come
back `None` — that is, every record that still lacks a summary, whether this
call filed its task, an earlier call did, or the cap dropped it. Both passes
walk the same records, so both return the same number.

A steady backlog of 37 unread papers was reported as `summaries_queued: 74`,
in a render that had filed nothing at all.

## Why it is worth fixing rather than living with

The number is wrong in the direction that hides work. `summaries_queued` is one
of the few figures an unattended nightly run reports back, and this repository
has already had one incident where the only evidence of a silent failure was a
count that looked plausible. A render that files nothing and says it filed 74
is exactly that shape: the reader concludes the queue is being fed.

It also breaks the arithmetic anyone would naturally do. `queue stats` said 37
pending while the render that produced them said 74 — and there is no way to
tell from the outside which one is lying.

## Why counting the queue is the right fix

The field claims to hold *tasks filed by this render*. The queue is the only
place that number exists. Measuring it before and after is exact regardless of
what the underlying function chooses to return, and it stays honest in the case
that motivated the reserve in the first place: when the cap binds and a task is
dropped rather than filed, the delta shows the drop.

`_before` for the second call is taken *after* `queue_missing_definitions`
runs, so definition tasks are already counted and the delta is summaries alone.

## Trade-offs and rejected alternatives

- *Changing `queue_missing_summaries` to return what it filed.* That is the
  cleaner fix and it is not available: the function is the template's, and the
  template wins. Every line we add to it is a line to re-apply by hand on the
  next `src` update. The delta is measured entirely from our own side.
- *Reporting only the second pass's return.* It happens to equal the total
  outstanding backlog, which is a useful number — but it is not the number the
  field is named for, and quietly redefining a field is worse than a wrong one.
- *Dropping the first pass's contribution.* Same objection, and it would report
  zero on the run where the reserve did all the work.

## What a reviewer should check

- `tests/test_local.py::DefinitionQueueShareTests::test_the_two_passes_do_not_double_count_the_same_backlog`
  — five unread papers, one render, `summaries_queued == 5`; a second render
  reports `0` and files nothing.
- `test_only_wiki_still_reports_no_summary_queueing` — `--only wiki` never held
  a reserve, so it must not release one.
- Against the live archive: `render`'s `summaries_queued` and the `pending`
  from `queue stats` must be reconcilable. Before this they were not.
- 348 tests pass.

## Downstream impact

Reporting only; no task, record or file changes. Runs before this commit
over-report `summaries_queued` by roughly a factor of two whenever a backlog
persists across both passes — the archive digests in git history should be read
with that in mind.
