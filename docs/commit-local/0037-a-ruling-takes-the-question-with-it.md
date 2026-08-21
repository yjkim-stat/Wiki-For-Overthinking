# 0037 — A ruling takes the question with it

| | |
| --- | --- |
| **Commit** | `fix(scripts): retiring a concept record retires its pending definition task` |
| **Scope** | `scripts/merge_concept_aliases.py`, `tests/test_local_aliases.py` |
| **Kind** | fix |

## What changed

`merge_concept_aliases.py --apply` folded a concept record into its canonical
and left the pending definition task for the retired slug sitting in the queue.
It now drops it, and reports the drop in the dry run first.

It also drops a task whose record is *already* gone — retired by an earlier run
of the same script — because that is the state a deployment actually lands in.

## Why it is built this way

Nothing else could have removed it. `render` files definition tasks and never
retracts one; the applier rejects a slug it cannot find, so answering the task
fails; and `queue` has no `drop`. The task therefore stays pending for ever,
and a pending task is indistinguishable from work somebody owes. Five of them
appeared here in one afternoon, out of a queue of twenty-six — a fifth of the
backlog was for entities that no longer existed.

`discard.py` already does exactly this for a paper: "any pending or done queue
task for it" goes with the record. This is the same rule reaching the other
record type. The asymmetry was the bug.

**A pending task is deleted; a completed one is reported and kept.** They are
not the same object. A pending task holds the question and the source material,
both of which `render` will rebuild for the canonical entity on the next pass.
A done task holds somebody's written answer, and this script's whole design
premise — the record goes to `data/concepts/retired/` before it is removed — is
that authored text is not destroyed quietly. So a done task prints a `!!` line
naming the file and the entity the answer should be given to instead, and is
left where it is.

**The already-retired branch runs before the record lookup, not inside it.**
The natural place to check is beside the retirement, but a script that only
looks at aliases whose record still exists cannot see the orphans a previous
`--apply` made — which is the only way this state is ever reached in practice.

## Trade-offs and rejected alternatives

**Rejected: having `render` drop tasks whose concept is missing.** It would fix
this and one thing more, which is the problem: a task whose record is missing
for some *other* reason — a half-written record, a bad merge — would be deleted
silently on the next pass, and the queue is the one place this repository
guarantees work does not vanish. Retirement is a deliberate act with `--apply`
on it, so the deletion belongs there.

**Rejected: moving the task to `data/queue/archive/`.** Archived tasks are how
`render` reads the source count a definition was written against. Filing an
unanswered question there would make a future staleness calculation read from a
task nobody answered.

## What a reviewer should check

- `tests/test_local_aliases.py::RetireTests` — four new cases: the pending task
  goes, an orphan from an earlier run still goes, a dry run drops nothing, and
  a completed task survives and is reported.
- `python3 scripts/merge_concept_aliases.py` with no flags on a live archive:
  the count line now ends `; N orphaned task(s) to drop`, and `--apply` says
  `dropped`.
- `python3 -m unittest discover -s tests -t .` — 847 tests, green.

## Downstream impact

Any deployment that has ruled on an alias since taking
`scripts/merge_concept_aliases.py` may have orphaned tasks in its queue. Running
the script with no arguments now lists them; nothing else has to change.
