# 0021 — The model kind reached half the pipeline

| | |
| --- | --- |
| **Commit** | `fix(render): stop dropping the models a reader submits` |
| **Scope** | `pipelines/render.py`, `pipelines/common/paths.py`, `pipelines/publish/wiki.py`, `pipelines/enrich/queue.py`, `tests/test_render.py`, `tests/test_queue.py` |
| **Kind** | fix · **corrects note 0011** |

## What changed

Note 0011 added `model` as a fourth wiki entity kind. It reached the schema, the
task's output contract and the wiki harvest, and it did not reach three places:

- `_apply_paper` and `_apply_video` never copied `models` out of a completed
  task, so **every `models` list a reader submitted was discarded** between the
  queue and the store.
- `_apply_concept` accepted only `concept`, `method` or `dataset` as a declared
  kind, so a promoted model's definition would have had its kind silently
  ignored.
- `validate_result` rejected `"kind": "model"` outright, so that definition
  could not be submitted at all.

All three are fixed. The kind tuple now lives once, as `WIKI_KINDS` in
`common/paths.py`, and `publish/wiki.py` and the queue validator both read it.

## Why it went unnoticed

The field looked empty by design rather than by omission. `PaperSummary` has a
`models` field with a default of `[]`, so every stored summary had the key and
an empty value — nothing was missing, nothing warned, and the archive pages
rendered fine. Note 0011 shipped with a one-off migration script that moved
model names out of `datasets`, and that script wrote directly to the summaries.
So the archive did have model entities, and they were all from the migration.
The migration made the bug invisible by supplying exactly the data the broken
path would otherwise have produced.

In this deployment the arithmetic is legible: 33 summaries had models, which is
exactly the 33 the migration touched, while 80-odd summaries submitted through
the queue since then had theirs dropped. Recovering them needed no re-reading —
`data/queue/archive/` keeps every completed task with its result, so 67 model
names were restored into 38 summaries from what the readers had already
submitted.

## Why it is built this way

**One tuple, imported twice.** The kinds were declared in `publish/wiki.py` and
re-declared as a literal in the validator, and that duplication is the whole
defect: `model` was added to one copy. Putting it in `common/paths.py` next to
`wiki_kind_dir` means the module that knows where a kind's notes live also
publishes which kinds exist, and nothing else may hold a second list.

**The applier is the narrowest place a field can be lost.** A field can be
absent from the schema (a type error), from the task contract (the reader is
never asked), or from the applier (the reader answers and is ignored). Only the
third is silent, and it is the one that happened. The test added here asserts
the round trip — submit, apply, load — rather than the presence of the
assignment, because the assignment is what was missing and asserting it would
just restate the diff.

## Trade-offs and rejected alternatives

- *Adding a test that every `PaperSummary` field is copied by `_apply_paper`.*
  Tempting, and rejected for now: it would have caught this, and it would also
  fail for fields deliberately not reader-supplied, such as `generated_at`. A
  correct version needs a declared list of reader-owned fields, which is a
  larger change than this fix.
- *Re-reading the 80 papers.* Unnecessary and wasteful — the archived task files
  hold the submitted results verbatim, so the recovery is a data migration, not
  a reading job.
- *Leaving `_apply_concept`'s kind gate alone since no model definition existed
  yet.* Rejected: this commit makes model entities reachable through the queue
  for the first time, so the gate would have started mattering immediately.

## What a reviewer should check

- `python3 -m unittest discover -s tests -t .` — 193 tests. `ModelsRoundTripTests`
  submits a task with `models` and asserts the stored summary has them and that
  they harvest as kind `model`.
- `test_validator_and_wiki_agree_on_the_kinds` asserts `publish.wiki.KINDS` is
  `paths.WIKI_KINDS`. That identity is the guard against this recurring.
- That the recovery worked and did not overwrite: the backfill only wrote where
  the summary's `models` was empty, so the migration's 33 were left alone. In
  this deployment 71 summaries now carry models against 33 before.
- `wiki/models/` should gain notes on the next render — 28 here, up from 21.

## Downstream impact

**A deployment that has been running the queue since note 0011 has lost every
`models` value its readers submitted.** The data is recoverable without
re-reading, because `data/queue/archive/` retains completed tasks: copy
`result.models` into the matching summary in `data/summaries/papers/` where that
field is empty, then re-render. A deployment that has not used `models` is
unaffected.

New model entities may cross the promotion threshold on the first render after
this, which queues definition tasks for them. That is the intended behaviour
arriving late, not a new one.
