# 0011 — A model is not a dataset: the wiki gains a `model` kind

| | |
| --- | --- |
| **Commit** | `feat(wiki): give models their own kind` |
| **Scope** | `pipelines/common/llm.py`, `pipelines/common/schema.py`, `pipelines/common/paths.py`, `pipelines/publish/wiki.py`, `scripts/migrate_model_kind.py`, `data/` |
| **Kind** | feature · **breaking schema** |

## What changed

The summary contract had three entity buckets — `concepts`, `methods`,
`datasets` — and no place for a model. Readers put evaluated checkpoints in
`datasets`, because that is where the schema left room. In this deployment that
produced a `wiki/datasets/` directory that was more than half models: 21 of 39
notes were Qwen, Llama, DeepSeek and GPT checkpoints.

- **New bucket.** `models` joins the paper and video output schemas, with the
  `datasets` description narrowed to say explicitly that a checkpoint belongs in
  `models`. `PaperSummary` and `VideoSummary` gain a `models` field.
- **New wiki kind.** `KINDS` becomes `(concept, method, dataset, model)`, notes
  land in `wiki/models/`, and the directory is created on first run.
- **Rank.** `_KIND_RANK` puts `model` above `dataset`, so a name seen as a model
  anywhere wins over an older summary that called it a dataset.
- **Migration.** `scripts/migrate_model_kind.py` rewrites stored summaries,
  moving matching names from `datasets` to `models`, and strips the sentence
  earlier definitions carried explaining the misfiling. It moved 132 entries
  across 33 of 45 summaries, covering 80 distinct model names, and cleared the
  explanation from 21 definitions.

After migration: `datasets/` 18 notes, `models/` 21, and no note claims to be
misfiled.

## Why it is built this way

**The schema decides what readers can record.** A reader who has just read a
paper evaluating Qwen2.5-Math-7B on MATH-500 has two names and one honest bucket.
Telling them in the routine to "not put models in datasets" would not have
worked, because the schema offered nowhere else. Fixing the contract is the only
fix that holds for readings nobody has done yet.

**Model outranks dataset in the merge.** `_upgrade_kind` resolves a name that
different summaries classify differently by taking the higher rank. Dataset used
to be the top rank on the reasoning that a name seen as a dataset is a dataset.
Model goes above it for a narrower reason: these two are the pair that actually
get conflated in practice, always in the same direction, and the model reading is
the specific one. A name called a model by any summary is a model.

**The migration is a script, not an edit.** `data/summaries/` is pipeline-owned,
and hand-editing 33 files would have left no record of the rule applied. A script
in `scripts/` keeps the classification rule readable, makes the run idempotent,
and lets a future family be added by editing one regex and re-running rather than
by touching records.

**The pattern lists families, not shapes.** It matches on known model families
(`qwen`, `llama`, `deepseek`, …) instead of guessing from capitalisation or
version-number shape. A false positive files a benchmark under models and
corrupts the wiki; a false miss leaves a model in `datasets`, which is the status
quo and visible. The asymmetry justifies the conservative rule — one miss was
found this way and fixed by adding `simplerl` to the list.

## Trade-offs and rejected alternatives

- *Re-answering the affected paper tasks so readers supply `models` directly.*
  Rejected: 33 summaries would need rewriting, at far greater cost than a
  classification rule, and it would not prevent recurrence for the next reader.
- *Adding `model` as an alias that renders into `datasets/`.* Rejected: the point
  is that the wiki's dataset index should list datasets. A cosmetic alias leaves
  the index wrong.
- *A general regex over capitalised alphanumerics with a size suffix.* Rejected
  for the asymmetry above — it would catch `AIME24` and `MATH500`.
- *Leaving the misfiling explanation in the definitions.* Rejected: it was true
  when written and is false now, and a stale caveat is worse than none.

## What a reviewer should check

- Tests pass unchanged: `python3 -m unittest discover -s tests -t .` — 149 tests.
  The suite does not cover the new kind; that gap is real and worth closing.
- The migration is idempotent: run `scripts/migrate_model_kind.py` twice and the
  second run reports 0 moved and 0 cleared.
- `--dry-run` reports without writing, and its list of names is worth reading
  before a first run in another deployment.
- Nothing genuine left `datasets/`: after migration it holds AIME, GSM8K,
  MATH500, the Pile, synthetic task definitions and the like, and no checkpoints.

## Downstream impact

**Breaking for any deployment with existing summaries.** A summary written under
the old schema has no `models` key; the field defaults to empty, so nothing
breaks at read time, but models stay in `datasets` until the migration is run.
Deployments that want the split should run `scripts/migrate_model_kind.py` and
then `python3 -m pipelines.render`; those that do not are unaffected.

New readings are unaffected in any deployment — the task now carries a `models`
field and a `datasets` description that excludes checkpoints.
