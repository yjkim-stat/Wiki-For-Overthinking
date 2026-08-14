# 0054 — The queue reports what it wrote

| | |
| --- | --- |
| **Commit** | `fix(render): report tasks filed, not records considered` |
| **Scope** | `pipelines/enrich/queue.py`, `pipelines/render.py`, `tests/test_task_refresh.py` |
| **Kind** | fix |

## What changed

`render` reported `summaries_queued: 512` on every pass of an archive whose queue
gained nothing. The number came from counting items the summarizer deferred —
and a queue backend defers *every* item it is handed, whether or not a task was
filed for it. So it counted records without a summary: the backlog, under a name
that says the opposite.

`Queue` now counts what it actually wrote, and both queueing steps report three
numbers where there was one wrong one:

```
summaries_queued      tasks newly filed
summaries_refreshed   tasks brought up to date
summaries_unread      records with no reading  ← what the old number meant
```

`definitions_queued` had the same defect and gets the same treatment.

## Why it is built this way

**This is the number that hid [note 0052](0052-a-task-is-a-function-of-its-record.md).**
For as long as `enqueue` was refusing to touch a pending task, the log said 512
tasks were being queued every render. Both statements were false in the same
direction and neither could be checked against the other. A counter that reads
the same whatever happens is worse than no counter, because it answers the
question you would otherwise go and ask.

**The count moved to the queue rather than being derived at the call site.** The
caller cannot learn what was written from `enqueue`'s return value: a summarizer
sits between them and reports only whether it deferred, which is a fact about the
backend and not about the queue. Putting the counters where the writes happen is
the only place the two cannot drift.

**The old number is kept, renamed.** It was mislabelled, not useless — "how many
records still have no reading" is the backlog, and it is worth reporting. Deleting
it would have thrown away real information to fix a name.

**Three numbers rather than a nested dict.** `result` is printed as one line at
the end of a run and read by eye. `summaries_queued` keeps its name and now means
what it says, so a reader who knew the old output learns the change by seeing two
new keys beside a number that suddenly moves.

## Trade-offs and rejected alternatives

**`Queue` is now stateful.** Two counters that only ever increase, on an object
built fresh for each step, which is the smallest version of that. The alternative
— returning a richer value from `enqueue` and threading it back through the
summarizer protocol — would change a contract that four backends share in order
to report on one of them.

**A task blocked by the cap is still invisible in these numbers.** It is filed
under neither `queued` nor `refreshed`, and `unread` counts it the same as a
record that got a task. `enqueue` already logs a warning per skip, which is the
existing signal; making the cap countable here would be a third thing and it has
not bitten anybody yet.

**Nothing renames the log line's history.** Deployments have run logs saying
"re-queued 512 missing summary task(s)" that were never true. They are not
rewritten, and this note is the record of what they meant.

## What a reviewer should check

- `test_a_second_render_reports_that_it_filed_nothing`. The second render of an
  unchanged archive must report `queued: 0` while `unread` stays at the backlog
  size. Restoring the old derivation — `"queued": unread` — fails it.
- That a refresh is reported as a refresh and not as a filing
  (`test_a_refresh_is_reported_as_a_refresh`), which is what makes the numbers
  usable after `backfill`.
- That both counters are incremented at the write, not near it: removing either
  `self.filed += 1` or `self.refreshed += 1` takes down exactly one test.

## Downstream impact

`render`'s result dict gains four keys and two existing ones change meaning:
`summaries_queued` and `definitions_queued` now count tasks written, so a
deployment used to seeing its whole backlog there will see a much smaller
number — usually zero, which is correct on a render that queued nothing.

`queue_missing_summaries` and `queue_missing_definitions` return a dict rather
than an int. Both are internal to `render`.
