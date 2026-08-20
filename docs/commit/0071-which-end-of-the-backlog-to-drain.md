# 0071 — Which end of the backlog to drain

| | |
| --- | --- |
| **Commit** | `feat(enrich): order the work queue by leverage, recency or topic` |
| **Scope** | `pipelines/enrich/queue.py`, `tests/test_queue_order.py`, `CLAUDE.md`, `README.md`, `workflows/knowledge-and-wiki/README.md` |
| **Kind** | feature |

> Numbered from a block — 0070 onward — reserved for work done in parallel with
> another session holding 0058 onward. The gap is deliberate.

## What changed

`queue list` and `queue next` take `--by`:

```bash
python3 -m pipelines.enrich.queue list --by sources --limit 20
python3 -m pipelines.enrich.queue list --by recency
python3 -m pipelines.enrich.queue list --by topic
python3 -m pipelines.enrich.queue next --by sources --kind concept
```

The default is unchanged and is named: `--by id`, the task files sorted by
name.

## Why it is built this way

**The old order was not a priority, it was an artefact.** A task id is
`<kind>__<filesystem-safe item id>`, so listing the pending directory sorts by
kind and then by arXiv number. A session that empties the queue every night
never notices. A session that drains the top twenty is reading the archive
alphabetically, and the twenty it never reaches are the same twenty every
night — which is worse than random, because it is stable.

**The default stays.** A deployment pulls new code and keeps its archive; a flag
that silently changed which items a nightly session read would change what the
archive learns, with nothing in any diff to show it. Choosing an order is a
decision, so it is typed.

**`sources` is two different numbers and says so.** For a concept task the
entity's own evidence count is exact: the term has been seen in *n* readings and
the definition that is missing is missing from all of them. For a paper or a
video that number is zero for every candidate and always will be — entities take
their evidence from summaries, an unread item has no summary, so nothing cites
it. The fallback is `score.leverage`, which is what scoring decided when the item
arrived, and it is the *same function* `backfill` orders by
([note 0070](0070-one-leverage-beside-the-scores-it-sums.md)) so the two commands
cannot rank one paper two ways. This is the substitution
[note 0048](0048-a-second-chance-at-a-document.md) already argued for, applied to
the other command that needed it.

**The two are not commensurable, and the docstring says that in as many words.**
An evidence count is a small integer; a summed score is a fraction per topic. So
concept tasks sort above reading tasks in practice. That happens to be
defensible on its own terms — a definition is read by everything that cites the
term, a reading by whoever wanted that paper — but it is an artefact of unit
scale and not a computed comparison, and `--kind` is the answer when an exact
ordering is wanted. Saying so is better than a number that looks like a
comparison and is not.

**`topic` groups before it weighs.** That is the whole point of it: a drain that
spreads across what the group tracks rather than following one subject to the
bottom of the queue. A task carrying two topics groups under the alphabetically
first, because a list can only show it once. A task carrying none sorts after
every group rather than ahead of all of them, which is where an empty string
would have put it.

**Every key ends in the task id.** A caller that drains the top N has to get the
same N back on the next call. This is `backfill._sort_key`'s rule, for the same
reason and stated the same way.

**Ordering is a read.** The queue lives in `data/`, and a sort that touched the
files would put the whole backlog into every diff and destroy `created_at`, which
is the only record of how long an item has been waiting — the exact thing
[note 0052](0052-a-task-is-a-function-of-its-record.md) went out of its way to
preserve. `render` owns the one legitimate reason to rewrite a pending task and
nothing here competes with it.

**The archive is opened lazily.** Listing by filename must not start depending on
records being readable, and most callers of `pending_ids` never ask for an
ordering.

**A missing record scores zero rather than raising.** An ordering is a
convenience. A queue that refused to list itself because one concept file had
been deleted would be worse than one task in the wrong place. A concept task
falls back to the `source_count` its own payload states, which is a worse answer
than the record and a better one than nothing.

## Trade-offs and rejected alternatives

**Every ordering but the default opens every pending task.** On a 500-task
backlog that is 500 small reads per invocation. Accepted: `list` already loads
each task to print its title, and the alternative — an index file — is a second
copy of the queue that can disagree with it.

**Considered: ranking concept tasks explicitly above reading tasks**, so the
observed behaviour would be intended rather than an accident of units. Rejected
because it makes the accident permanent: with fifty concept tasks pending, no
paper is ever in the top twenty, and the queue starves the reading it exists to
schedule. The unit mismatch at least moves as the numbers move.

**Considered: normalising the two numbers onto one scale.** Rejected on this
repository's own terms — `enrich/score.py` is deliberately transparent because a
rule somebody can read and correct beats a score nobody can argue with, and a
normalised leverage is exactly the second thing.

**No `age` ordering, though `backfill` has one.** `recency` is its mirror and
was what the requirement asked for. Oldest-first is a fairness rule, and the
oldest tasks in this queue are disproportionately the ones whose document could
not be fetched — so they are the tasks a reader can do least with, not most.

**`next`'s help said "the oldest pending task" and was already wrong**: it
printed the first by filename, which is only the oldest by coincidence. It now
says "the first pending task, in the chosen order", and `CLAUDE.md` says the
same. That is a documentation fix riding along with the change that made the old
wording indefensible.

**The output format did not change.** `--by` sorts and nothing else; it does not
print the weight it sorted by. A caller parsing `list` output keeps working.

## What a reviewer should check

Seven mutations, each against the full suite:

- Default `order="id"` → `"sources"`: takes down
  `test_the_default_is_still_filename_order`. This is the one that matters most,
  because the failure would be invisible in any single session.
- Concept weight read from the payload instead of the record: takes down
  `test_a_concept_is_weighed_by_the_record_not_by_the_stale_payload`.
- `-self.sources_for(task)` → `+`: takes down eight tests. Ordering the backlog
  backwards is the loudest possible failure and is loudly caught.
- `_newest_first(created_at)` → the raw string: takes down
  `test_recency_puts_the_newest_task_first` and
  `test_a_task_with_no_timestamp_sorts_after_every_dated_one` — direction and
  the placement of a task with no timestamp, which the numeric form settles
  together.
- Untopiced group `(1, "")` → `(0, "")`: takes down
  `test_a_task_with_no_topic_sorts_after_every_group`.
- `(group, weight, task_id)` → `(weight, group, task_id)`: takes down
  `test_tasks_are_grouped_by_topic_before_they_are_weighed`.
- **Re-writing each task with identical bytes before sorting**: takes down
  `test_listing_in_every_order_changes_no_file_under_data` — *and only because
  the snapshot compares modification time as well as content*. Verified by
  dropping `st_mtime_ns` from the snapshot with the mutation still in place, at
  which point the test passes. This is the trap
  [note 0052](0052-a-task-is-a-function-of-its-record.md) recorded, reproduced
  deliberately.

Also worth checking: **the sleep in `test_recency_puts_the_newest_task_first` is
load-bearing.** `utcnow()` has second resolution, so two tasks filed in the same
second carry the same `created_at`. Remove the `time.sleep(1.1)` and the test
fails against correct code rather than passing against broken code — which is
the safe direction, and is why the assertion is written so that filename order
and recency order are opposites.

## Downstream impact

None unless asked for. No record changes, no file moves, no config. Every
existing invocation of `queue list` and `queue next` returns exactly what it
returned before, and `Queue.pending_ids()` keeps its old signature and its old
answer.

A deployment that wants the new behaviour types `--by`; a session following
`CLAUDE.md` is now told to choose an end when it will not finish the queue.
