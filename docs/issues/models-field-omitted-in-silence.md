# A paper reading can omit `models` and nothing notices

**Status**: open, not acted on.
**Found**: 2026-08-13, by making the mistake — nine consecutive readings.

## The defect

`models` on a paper reading is optional, has no validator, and appears only in
the task's `output_schema`. The `instructions` field — which is what a reader
actually follows — never mentions it. A reading that omits it entirely is
accepted by `queue complete`, applied by `render`, and archived, with no
warning at any stage. `PaperSummary.models` defaults to `[]`, so the record
looks the same as one for a paper that genuinely evaluates nothing.

This is the second time the `model` kind has failed this way. The first was
`docs/commit-local/0021`, where the applier line was missing and every
`models` a reader submitted was dropped between the queue and the store, for
80-odd summaries. That was a pipeline bug; this is a contract bug, and the
symptom is identical: a field that silently stays empty.

## Why the obvious fix is wrong

Requiring the field would force a guess where the honest answer is silence — a
paper that evaluates no checkpoint should return an empty list, and the archive
holds several. That is the same reasoning that keeps `results` optional, and it
should not be given up.

## Options, with a leaning

1. **Warn in the applier.** `_apply_paper` logs when a paper reading returns no
   models, as `_apply_bibliography` already logs an unknown topic slug. Cheap,
   local, and does not change the contract. **Leaning here** — but a warning in
   a render log nobody reads is only marginally better than nothing, and the
   render already emits stale-definition warnings that are routinely ignored.
2. **Name the field in `paper_instructions`.** Addresses the actual cause: the
   reader follows the prose and the prose does not mention it. One sentence,
   and it touches `common/llm.py`, which already carries three deltas.
3. **Count it in the render result.** Report `readings_without_models` beside
   `stale`, so the number is visible in the same place the archive already
   looks for rot. More useful than a warning and harder to ignore.
4. **Nothing.** The field is a local delta; the template does not have it, and
   every defence added here is another thing an update can revert.

2 and 3 compose, and together they address cause and detection. Not done
because it is a change to the reading contract, and the archive should decide
whether a reading that omits `models` is a defect or a permitted answer before
the code asserts one.

## Damage so far

Nine readings, repaired by `scripts/backfill_summary_models.py` from the source
documents. See `docs/commit/0061`.
