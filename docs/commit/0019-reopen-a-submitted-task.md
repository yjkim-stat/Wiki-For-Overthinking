# 0019 — A submitted result can be corrected

| | |
| --- | --- |
| **Commit** | `feat(queue): add reopen so a submission can be corrected before render` |
| **Scope** | `pipelines/enrich/queue.py`, `CLAUDE.md`, `tests/test_queue.py` |
| **Kind** | feature |

## What changed

`Queue.reopen(task_id)` and a `reopen <task_id>` subcommand. A completed task
returns to pending with its instructions, schema and source material intact and
its answer dropped, so it can be answered again through the validator.

A task already archived by `render` is refused with an error saying what to do
instead. An unknown id raises `FileNotFoundError`.

## Why it is built this way

Completion was one-way. A reader who spotted their own mistake had two options:
leave a known-wrong record in place, or edit `data/` by hand. Both are worse
than the mistake, and the second is worse than it looks — hand-editing bypasses
the validator, which is the only thing standing between a typo and a structural
error.

That is not hypothetical. An alias filed by hand would have fused two distinct
entities: `RT-X` recorded as an alias of `Open X-Embodiment`, when RT-X names
the models trained on that dataset. Aliases are the merge mechanism, so a wrong
one does not mislabel, it silently merges. **The asymmetry is what makes it
dangerous: a wrong split announces itself as two thin notes, while a wrong
fusion presents as one healthy note with nothing visibly wrong.** A path back
through the validator is cheaper than any amount of care about editing records
directly.

**Refusing an already-archived task is the load-bearing part.** Once `render`
has consumed a result it is folded into the records, and re-answering the task
would not undo that — the reopened answer would apply on top of an archive that
already reflects the old one. So the honest response is to fix the record or
re-collect, and the error message says so rather than making the caller find
out.

**Only the answer is dropped.** `result` and `completed_at` go; everything that
made the task answerable stays. A reopened task is indistinguishable from one
that was never completed, which is what makes re-answering it ordinary rather
than a special path.

**The boundary is documented in `CLAUDE.md`, not enforced.** `reopen` is for a
reader correcting their own fresh mistake. It is not for a retroactive pass over
settled work: a reader re-deriving a record against a conclusion they have
already been told will tend to satisfy the conclusion rather than the evidence,
and that is evidence editing. Code cannot tell those apart — the file operation
is identical — so the distinction is stated where the person doing it will read
it. The archive refusal enforces the one part that *is* mechanical.

## Trade-offs and rejected alternatives

**Rejected: allow reopening an archived task and re-applying.** It would need
`render` to reverse an application — unpicking evidence, concept mentions and
wiki promotions derived from the old answer. That is a much larger change, and
the honest fallback (fix the record, or re-collect) already exists.

**Rejected: a `--force` flag on `complete`.** Same effect with less clarity: the
task's state would silently differ from what its directory says.

**Cost: nothing stops the retroactive use.** The guidance is prose. In the
deployment this came from, both readers who used it drew the line themselves,
which is some evidence the guidance is the right instrument — but it is
guidance, not a guarantee.

## What a reviewer should check

That a correction is still validated — the point is a path back *through* the
validator, not around it:

```bash
python3 -m unittest tests.test_queue -v -k Reopen
```

`test_a_correction_is_still_validated` is that guard. `test_an_applied_task_is_refused_with_advice`
checks the archived case, including that the message names the alternative; an
error that only said "no" would send people straight back to editing `data/`.

The CLI error paths are worth a look too, since they are what a reader actually
meets:

```bash
python3 -m pipelines.enrich.queue reopen paper__nope   # exit 1, names the id
```

## Downstream impact

Purely additive. Existing behaviour is unchanged, no configuration, no
migration.
