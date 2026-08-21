# 0020 — A placeholder is not a name

| | |
| --- | --- |
| **Commit** | `fix(queue): reject entity entries that describe a set instead of naming one` |
| **Scope** | `pipelines/enrich/queue.py`, `scripts/strip_placeholder_entities.py`, `tests/test_queue.py` |
| **Kind** | fix · **breaking for readers who wrote placeholders** |

## What changed

`validate_result` now refuses a `concepts`, `methods`, `datasets` or `models`
entry that names no specific thing — "three GREC benchmarks (unnamed in
abstract)", "several open-weight models", "unspecified". The reader is told to
leave the field empty instead, which is what the task instructions already ask
for. `scripts/strip_placeholder_entities.py` removes such entries from summaries
already stored, sharing the detector with the validator so the two cannot drift.

`models` was also missing from `_LIST_FIELDS`, so it was never type-checked;
that is fixed here as the smallest part of the same edit.

Applied to this deployment, the script removed 27 entries from 25 summaries.

## Why this had to exist

A reader who cannot establish which benchmark a paper used is supposed to leave
`datasets` empty. Writing a description of the benchmarks instead feels like the
cautious choice and is strictly worse, because `publish/wiki.py` keys wiki
entities by their string.

Two unrelated papers that phrase a placeholder identically therefore merge into
one entity, count each other as independent evidence, and cross the promotion
threshold. That is not hypothetical: `five reasoning benchmarks (unnamed in
abstract)` reached two sources from FoE and SeLaR — different benchmark sets,
neither named — and was queued for a definition. The promotion threshold exists
to require independent corroboration, and a generic phrase manufactures exactly
the corroboration it is checking for.

An empty field is a true statement about what the reader knows. A placeholder is
a false entity.

## Why it is built this way

**Rejected at submission, not filtered at harvest.** The wiki could skip
placeholder-looking strings when harvesting, and the bad data would still be in
`data/`, which is the source of truth. Refusing it at the door keeps the store
clean and tells the reader immediately, while they still have the paper open.

**Two signals, and the second requires both halves.** An explicit disclaimer —
"unnamed", "not specified", "n/a" — is enough on its own. For a reader who omits
the disclaimer and writes only "several math benchmarks", the rule demands a
bare leading quantifier *and* a word for a collection of things. Requiring both
is what keeps real names out of the net: an earlier version tested the
quantifier alone and rejected `ten-fold cross-validation` and `two-phase
reasoning structure`, flagging 34 entries where 27 were wrong. The quantifier
must be a whole word followed by a space, because a hyphenated one is an
adjective and not a count.

**Prose fields are untouched.** "Evaluated on three benchmarks (unnamed in the
abstract)" is a true and useful sentence in `results`, and the honest thing to
write there. It is only a problem when offered as a name, so only the four
harvested fields are checked.

## Trade-offs and rejected alternatives

- *Silently dropping the entry instead of erroring.* Rejected: the reader would
  not learn, and would keep writing them. The error names the entry and says
  what to do instead.
- *A curated stopword list of known placeholder phrases.* Rejected: the phrasing
  is free text and varies per reader. A rule about shape generalizes; a list of
  strings is a list of the ones already seen.
- *Deduplicating identical entity strings across papers in the wiki instead.*
  Rejected: it treats the symptom and would also merge genuine shared names,
  which is the behaviour the wiki is supposed to have.
- *Stemming or normalizing entity names before keying.* Rejected as a much
  larger change to wiki identity, and orthogonal — a placeholder is wrong even
  when only one paper writes it.

## What a reviewer should check

- `python3 -m unittest discover -s tests -t .` — 193 tests, with
  `PlaceholderEntityTests` covering both directions.
- The false-positive test is the one to keep if the rule is ever rewritten:
  `ten-fold cross-validation`, `Mixture-of-Experts`, `two-phase reasoning
  structure`, `best-of-n` and `pass@k` must all survive. Real dataset and model
  names are the cost of getting this wrong.
- That `scripts/strip_placeholder_entities.py` defaults to a dry run, and that
  it and the validator call the same `looks_like_placeholder`.
- That a placeholder inside `results` or `limitations` is still accepted.

## Downstream impact

**A deployment whose readers have written placeholders will see submissions
start failing.** That is the correction, but it is a behaviour change: run
`scripts/strip_placeholder_entities.py` to see what is already stored, then
`--apply` and re-render. Stripping an entry can drop an entity below the
promotion threshold, and `pipelines.render` removes notes whose evidence is
gone; anything written after an `<!-- auto:end -->` marker is preserved as
always.

A deployment with no placeholders is unaffected, and the type check newly
applied to `models` is a strictly better error message for a mistake that
previously passed validation and failed later.
