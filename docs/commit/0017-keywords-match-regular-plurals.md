# 0017 — Keywords match regular plurals

| | |
| --- | --- |
| **Commit** | `feat(score): match the regular plural of a keyword's head word` |
| **Scope** | `pipelines/enrich/score.py`, `tests/test_score.py` |
| **Kind** | feature |

## What changed

A keyword now matches its regular English plural. `action chunk` matches "action
chunks", `robot policy` matches "robot policies", `VLA` matches "VLAs".

Only the final word inflects. The strict word boundaries are untouched.

## Why it is built this way

The boundaries were right and the inflection was missing. `(?<!\w)…(?!\w)` is
what stops `VLA` matching inside `Vlasov` and `ATE` inside `Water`, and it is
worth keeping — but it also made every keyword list a manual inflection
exercise, with a silent failure mode. A rule one letter off produces "this topic
has nothing to collect", which is indistinguishable from a quiet week. Nothing
is logged, because a non-match is not an event.

**The failure runs both ways**, which is the part that makes it more than a
missed paper. A `keywords.none` entry that misses a plural lets an unwanted item
*through*. So this is not simply a recall improvement; it is a correctness fix
for exclusion rules too.

**Only the head word inflects.** The plural of a phrase is the plural of its
head: `latent action model` should match "latent action models" and must not
match "latent actions model", which is a different phrase. Inflecting every word
would match text that means something else.

**Two rules, not stemming.** The `y → ies` rule with a vowel-y carve-out
(`survey → surveys`, never `survies`), and `es` after a sibilant (`bias →
biases`). That covers the observed failures, stays readable in a file whose
entire design goal is that a person can read a rule and argue with it, and adds
no dependency. Irregular plurals remain the keyword author's problem — the right
place for them, because the author knows the word and the code does not.

## Trade-offs and rejected alternatives

**Rejected: stemming or lemmatization.** More coverage, a dependency, and an
opaque rule. This file's premise is that a transparent rule you can correct
beats an accurate one you cannot argue with; a lemmatizer inverts that.

**Rejected: asking authors to list both forms.** That is the status quo, and it
is what failed three times in one day in the field before being diagnosed as a
class rather than three coincidences.

**Cost: match volume increases, in both directions.** More papers score above
zero, and `none` lists now exclude more. A deployment with tuned thresholds
should re-check them.

**Cost: a few false positives are now reachable.** `bus` matches "buses" but
also, via the sibilant rule, nothing worse — though a term ending in `s` that is
already plural (`analytics`) will now also match `analyticses`, which does not
occur in text. Harmless, and cheaper than special-casing.

## What a reviewer should check

That the boundaries did not loosen while the inflection was added — that is the
regression this change could plausibly cause:

```bash
python3 -m unittest tests.test_score -v -k Plural
```

`test_word_boundaries_still_hold` is the guard: `VLA`/`Vlasov`, `world
model`/"worldly models", `action chunk`/"a chunk of actions". And
`test_only_the_last_word_inflects` is the one that fails if someone later
"simplifies" this by inflecting every word.

Note `_WORD_BOUNDARY_CACHE` is keyed on the term, so a long-lived process picks
up the new patterns only for terms compiled after this lands. Irrelevant to a
run, worth knowing in a test session.

## Downstream impact

**Match volume increases** in both `keywords.any` and `keywords.none`. A
deployment with tuned thresholds should re-check them, and should re-read any
`none` list: entries previously duplicated in singular and plural can be
collapsed to the singular.

This compounds with [0012](0012-venue-filter-is-opt-in.md), which also increases
volume. Together they can grow a run's queue substantially — check
`summarize.max_pending_tasks` before the first run that has both.

Nothing needs migrating; the change is in matching only.
