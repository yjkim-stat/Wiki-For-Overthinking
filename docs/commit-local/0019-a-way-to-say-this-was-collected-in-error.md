# 0019 — A way to say "this was collected in error"

| | |
| --- | --- |
| **Commit** | `feat(scripts): discard records a scoring mistake let in` |
| **Scope** | `scripts/discard.py`, `tests/test_model_kind.py` |
| **Kind** | feature · **destructive** |

## What changed

`scripts/discard.py` removes stored records, in three modes:

- `--rescore` — every **collected** record that no current topic accepts.
- `--id PAPER_ID` — a named record, repeatable.
- `--orphans` — queue tasks whose record no longer exists.

Dry run is the default; nothing is removed without `--apply`. Five tests cover
the guards.

Applied here, it removed the 13 records that note 0018's scoring regression had
admitted — an analog-circuit design optimizer, a KV-cache eviction scheme, a
music co-creation agent, a physical prompt-injection study on robots — and the
13 stranded tasks that followed them.

## Why this had to exist

The archive had no way to be wrong. Scoring is a keyword rule, keyword rules
misfire, and until now the only responses were to hand-edit `data/` — forbidden,
and leaving no record of the judgement — or to leave the item in, where it
corrupts every topic output built from it. Note 0018's downstream section
recorded the gap; this closes it.

It is the destructive counterpart to `retopic.py` (note 0012), which only ever
adds. The asymmetry between the two is deliberate: adding a topic is cheap to
undo, removing a record is not, so they are separate commands with separate
defaults.

## The guards, and why each one

**Dry run is the default, not a flag.** Every other script here writes when run
and offers `--dry-run`. This one inverts that, because the failure modes are not
symmetric: a discard that should not have happened costs a re-collection at best
and a hand-read PDF at worst.

**`--rescore` never touches a hand-filed PDF.** A PDF in `inbox/` bypasses
scoring by design — filing it *is* the editorial decision scoring exists to
approximate — so a local record with no topics is a reader's judgement, not a
scoring error. Confusing the two would have deleted the two interpretability
papers that sat untopiced for weeks before note 0013 gave them a home. Removing
a local record is still possible, but only by naming its id, where the
intention is explicit.

**`seen.sqlite` is deliberately left alone.** That is the dedup alias map.
Forgetting a discarded id there would let the next run collect the same item
again, and a discarded record should stay discarded. The cost is that a record
discarded in error cannot simply be re-collected; that is the right way round.

**`--orphans` exists because of a bug found while writing this.** The first
version reconstructed the queue task id by hand as
`"paper__" + id.replace(":", "-")`, which missed that dots are replaced too. The
records were removed and their tasks were not, leaving 13 tasks that could never
be completed — `complete` looks the record up to apply the result — and that the
next reader would have tried to answer. The id is now asked of `Queue.task_id`,
and `--orphans` cleans up after any future version of the same mistake.

## Trade-offs and rejected alternatives

- *A `queue discard <task_id>` verb instead.* Rejected: it addresses the symptom.
  The task is downstream of a record that should not be in `data/`, and removing
  the task alone leaves the record to be re-queued on the next render.
- *Moving discarded records to `data/discarded/` rather than deleting.* Tempting,
  and rejected for now: it adds a state to a store whose whole design is that
  `data/` is the truth and everything else derives from it. Git history already
  holds the deleted records, which is the recoverability that matters.
- *Recording the discard in `rejected.jsonl`.* Rejected as misleading — that file
  is the record of what scoring considered and dropped at collection time, and
  writing post-hoc removals into it would corrupt the one artefact for tuning
  thresholds later.
- *A confirmation prompt instead of `--apply`.* Rejected: this has to work
  non-interactively in the scheduled run.

## What a reviewer should check

- `python3 -m unittest discover -s tests -t .` — 178 tests, five new in
  `DiscardScriptTests`.
- That a bare `python3 scripts/discard.py` refuses to run rather than defaulting
  to a mode.
- The safety property that matters most: `--rescore` must never list a record
  whose id starts with `local:`. It is asserted, and it is the assertion to keep
  if the selection logic is ever rewritten.
- That `--apply` is required: running `--rescore` alone must leave
  `git status --porcelain data` unchanged.

## Downstream impact

Additive — no existing command calls it, and a deployment that never mis-scores
never needs it.

For this deployment the effect is already applied: 126 papers remain of 139, all
13 removals were August 2026 arXiv collections from the run that exposed note
0018's regression, and no hand-filed PDF was touched. `archive/` and the topic
outputs are regenerated on the next render, which clears the tree first.
