# 0015 — Cover the model kind and the two maintenance scripts

| | |
| --- | --- |
| **Commit** | `test: cover the model wiki kind and the maintenance scripts` |
| **Scope** | `tests/test_model_kind.py` |
| **Kind** | test |

## What changed

`tests/test_model_kind.py` closes the coverage gap that notes 0011 and 0012 each
recorded against themselves. Eight tests in three groups:

- **The kind.** `model` is in `KINDS`; a name harvested from a summary's `models`
  field lands in `wiki/models/` and not in `wiki/datasets/`; a name that one
  summary calls a dataset and another calls a model resolves to a model; and a
  genuine dataset is left alone.
- **The migration's classification.** `is_model` recognises the model families
  the deployment actually saw, and does not fire on the benchmarks it sits next
  to — `AIME24`, `MATH500`, `GSM8K`, `OlympiadBench`, `the Pile`, `MT-Bench`.
- **The retopic script's guarantees.** An unknown slug exits 2 rather than being
  ignored, and `--dry-run` leaves `data/` untouched.

## Why it is built this way

**The rank rule is the part most worth a test.** `_upgrade_kind` decides what
happens when two summaries disagree about what a name is, and that resolution is
invisible in normal use — nothing reports it, and the only symptom of getting it
wrong is a note quietly appearing in the wrong directory months later. It is
also the rule most likely to be changed by someone adding a sixth kind.

**The classification tests assert both directions.** A migration that moves too
little is visible; one that moves too much silently files benchmarks as models
and corrupts the wiki. Note 0011 chose a conservative family list for exactly
that asymmetry, so the negative cases are the ones that protect the choice — and
they are drawn from names that sat in the same `datasets` fields as the models.

**The script tests are behavioural, not unit.** They run the scripts as
subprocesses and check the two properties a user relies on: that a typo in a slug
stops the run, and that `--dry-run` is honest. Testing the internals would couple
the suite to argument plumbing that is allowed to change; testing the contract
does not.

**`--dry-run` is checked against `git status`, not against a fixture.** That is
the property that actually matters — the script is pointed at the real `data/`
by design, so the guarantee worth asserting is that a dry run leaves the working
tree exactly as it found it.

## Trade-offs and rejected alternatives

- *Testing the migration end to end on a sandbox `data/`.* Rejected: the moving
  parts worth protecting are the classification rule and the wiki routing, both
  covered directly, and a full-corpus fixture would need maintaining alongside
  the real one.
- *Asserting the exact set of names the migration moved in this deployment.*
  Rejected: that encodes one archive's contents into the suite, and the suite is
  meant to be readable by a deployment in another field.
- *Skipping the script tests because scripts are not library code.* Rejected —
  they write to the source of truth, which is precisely why their guarantees
  deserve assertions.

## What a reviewer should check

- `python3 -m unittest discover -s tests -t .` — 167 tests, eight new.
- That the new tests use `Sandbox` and so never touch the real `data/`, except
  the two script tests, which run against the repository deliberately and assert
  that nothing changes.
- That `test_a_real_dataset_stays_a_dataset` would fail if `_KIND_RANK` were
  reordered to put `model` below `dataset` — it is the guard on note 0011's
  central decision.

## Downstream impact

None. Tests only.
