# 0043 — `generated_by` names the backend, not the task kind

| | |
| --- | --- |
| **Commit** | `fix(enrich): generated_by names the backend, not the task kind` |
| **Scope** | `pipelines/enrich/apply.py`, `tests/test_apply.py` |
| **Kind** | fix |

## What changed

One fallback:

```python
-generated_by=task.get("completed_by", task.get("kind", "")) or "queue",
+generated_by=task.get("completed_by") or "queue",
```

`completed_by` is written by nothing in this repository — it is the field an API
backend would fill in, and the queue backend does not. So the fallback always
fired, and because it fell through `task["kind"]` first, every paper reading was
stamped `generated_by: "paper"`.

The video applier one screen below never had the extra fallback and always
produced `"queue"`. Two appliers, one field, and only one of them putting a
backend name in it.

## Why it is built this way

`generated_by` answers "which backend produced this reading", and it exists for
the moment two readings of the same paper disagree and somebody has to decide
which to trust. `"paper"` does not answer that question — it is the task kind,
which is already recoverable from the record's own type.

The failure is the kind this repository keeps running into: the field was never
empty and never obviously wrong. A live archive carried `"paper"` on 242
consecutive readings with nothing anywhere reporting a problem, because a
plausible value in a field nobody reads is indistinguishable from a correct one.

The fix takes the video applier's shape rather than inventing a third. Where two
paths through the same field disagree, the one that was never wrong is the
specification.

## Trade-offs and rejected alternatives

**Existing records keep their wrong value.** Nothing rewrites a summary that has
already been applied; `render` is not allowed to write to `data/`, and a
migration that rewrote provenance would be asserting something about readings it
did not witness. Deployments that care can re-derive from
`data/queue/archive/`, where the tasks are kept.

**Considered: dropping the field.** It has one real consumer — a future
non-queue backend — and no reader today. Removing it would destroy the value on
every existing record, which the layout rules name as the one unsafe schema
change. Fixing a field costs nothing; removing one cannot be undone.

**Considered: making the queue write `completed_by: "queue"` at completion.**
Then the default would never fire and the bug could not recur. Rejected as
redundant: the task already records that a human-in-the-loop queue answered it
by virtue of being in the queue, and writing the same constant into every task
file is state that can drift from the code that reads it.

## What a reviewer should check

- `tests/test_apply.py::ProvenanceTests`. Restore the old fallback and
  `test_a_paper_reading_names_the_backend` fails while the video one passes —
  which is exactly the asymmetry that hid this.
- That an explicit backend still wins: `test_an_explicit_backend_is_kept`. The
  default has to be right *and* stay out of the way.
- `grep -rn "completed_by" pipelines/` — two reads, no writes. If that ever
  gains a write, this note's premise changes.

## Downstream impact

Readings applied from now on carry `"queue"` where they used to carry `"paper"`.
No artifact renders the field, so nothing regenerates differently and no page
changes. Existing records are left as they are; a deployment that wants them
corrected has to re-derive from its archived tasks, and nothing does that
automatically.
