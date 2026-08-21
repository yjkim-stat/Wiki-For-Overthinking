# 0052 — A task is a function of its record

| | |
| --- | --- |
| **Commit** | `fix(enrich): a waiting task learns that its document arrived` |
| **Scope** | `pipelines/enrich/queue.py`, `tests/test_task_refresh.py`, `CLAUDE.md`, `docs/commit/0048`, `docs/issues/`, `docs/solved/` |
| **Kind** | fix |

## What changed

`Queue.enqueue` returned `""` the moment a pending task existed, so a task was
whatever its record looked like on the day it was filed, for ever. A document
fetched afterwards never reached the reader it was fetched for.

A pending task is now rebuilt from its record and rewritten when the rebuild
differs. `created_at` is carried across; an answered task is never touched.

This is the defect [note 0048](0048-a-second-chance-at-a-document.md) created and
did not notice — a correction is appended there. Measured on the archive where it
was found: `backfill` fetched 224 documents and **0 of 512** pending tasks
carried a `pdf_path`.

## Why it is built this way

**The missing attachment was the least of it.** `has_document` also selects the
instructions and the output schema, so a stale task handed over an abstract
prompt and a schema with no `read_from` field. Then `_check_reading_basis` — note
0044, and right — refuses `read_from: "document"` when the task attached none.
A reader who opened the PDF sitting on disk had to record `abstract` or be
rejected, so the archive **permanently recorded a weaker evidence tier than it
actually had**, and that tier is exactly what the reading rules turn on. Three
wrongs, and the one noticed last cost the most.

**Option A from the issue: refresh whenever the rebuild differs, not when a
named field does.** The narrower version — refresh `attachments` plus the two
fields that move with it — is a rule that is right today and wrong the next time
something becomes derivable. Comparing the whole rebuilt task makes a waiting
task a function of its record, which is what every other derived thing in this
repository already is.

**Two exceptions, both load-bearing.** `created_at` is the only record of how
long an item has been waiting, and a task that quietly became newer would
corrupt any ordering built on it — `backfill --by age` reads exactly that field.
And a task in `done/` is never rewritten, because a reader may have worked from
the version they were handed and replacing its material would make their answer
describe something else.

**A refresh is not a new task**, so it returns `""`, it does not count towards
the queue cap, and the cap cannot block it. Bounding the backlog is about how
much is waiting, and a refresh changes nothing about that.

**A rebuild that is identical writes nothing.** The same property `_same`
protects for concept records, for the same reason: a pass that rewrites the whole
queue puts it in every diff, and a real change stops being visible.

## Trade-offs and rejected alternatives

**Option C — have `backfill` refile the tasks it touched — was rejected**
although it has the narrowest blast radius. It leaves the class open: a document
arriving any other way, a hand-filed PDF for a paper already queued, a record
edited by hand, still leaves a stale task. It would also cost `backfill` the
"queues nothing" property its own note claims.

**Option D — delete the affected tasks by hand — is the workaround for an
archive on the old code**, and it works, because `queue_missing_summaries`
exists precisely to refile a task deleted by hand. As a standing answer it asks a
person to delete 224 files to collect a benefit the pipeline already paid for,
and nothing tells them which 224.

**A task now changes under a reader who is looking at it.** If a document
arrives between `queue show` and `queue complete`, the material moved. The
answer is still validated against the task as it now stands, so the failure mode
is a rejected submission rather than a wrong record — and the alternative is the
status quo, where the material is stale on purpose.

**Concept tasks are refreshed too**, since their payload carries the sources that
mention the entity. That is correct — a definition task should list the evidence
as it now stands — and it means a concept task legitimately churns as papers
accumulate. It is a change, not churn.

**Nothing counts refreshes yet.** `render` reports `summaries_queued`, which
counts records without a summary rather than tasks actually filed, and reported
`512` on every pass throughout this defect's life. That number is why this was
silent, and fixing it is the next commit rather than this one.

## What a reviewer should check

Four mutations, two of which needed the tests tightening before they bit:

- Restore the `if pending.exists(): return ""` guard — three tests fail.
- Remove the `done_path` guard — an answered task gets overwritten.
- **Re-stamp `created_at`.** The first version of that test compared timestamps
  taken within one second of each other, and `utcnow()` has second resolution, so
  it passed either way. It now sleeps past a second boundary, which is the same
  correction `tests/test_layering.py` records having needed.
- **Write on every render regardless.** The first version hashed the task files;
  a rewrite with identical bytes is invisible to a hash. It now compares
  modification time as well.

Also: `python3 -m pipelines.render` twice over an unchanged archive still leaves
`data/queue/pending/` untouched, and the sequence in `CLAUDE.md` is now true end
to end — `backfill`, `render`, and a reader who opens the file may honestly
record `read_from: "document"`.

## Downstream impact

**On the first render after this lands, every pending task whose record has moved
since it was filed is rewritten.** For an archive that has run `backfill` that is
most of the queue, and the diff is large and one-off. Nothing is lost: `created_at`
is preserved, answers are untouched, and the material only ever moves closer to
the record.

A deployment that worked around this by deleting tasks by hand needs to do
nothing further.
