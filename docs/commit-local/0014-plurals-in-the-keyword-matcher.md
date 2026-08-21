# 0014 — Plurals belong in the matcher, not in every keyword list

| | |
| --- | --- |
| **Commit** | `fix(score): match the regular plural of a keyword's final word` |
| **Scope** | `pipelines/enrich/score.py`, `tests/test_score.py` |
| **Kind** | fix · **breaking default** |

## What changed

`_pattern` now compiles the last word of a keyword so it also accepts that
word's regular English plural. `reasoning model` matches "reasoning models",
`circuit` matches "circuits", `reasoning capability` matches "reasoning
capabilities", `search` matches "searches". Ten tests cover the behaviour and
its edges.

Only the final word is inflected, because that is where English puts the plural
of a noun phrase: "reasoning models", never "reasonings model".

## Why it is built this way

**The omission was silent, and that is what made it expensive.** Word-boundary
matching meant `reasoning model` did not match "reasoning models" — the plural
form papers actually write. A paper failing on that produced no log line, no
entry anyone would look at, and no way to tell it apart from a paper that
genuinely did not match. In this deployment the same defect was hit three times
while writing topic files, each time discovered by manually checking a paper
that should obviously have matched and had not: `reasoning model`/`models`,
`linear probe`/`probes`, `circuit`/`circuits`.

**Listing both forms does not scale and was already failing.** An audit of the
five topic files found 41 keywords whose counterpart was absent. Most of the
naive completions are not English — "monitorabilities", "chain of thoughts",
"best of ns" — so a maintainer cannot mechanically fill the gap, and doing it by
judgement means re-deciding for every keyword ever added. The list is also the
arXiv query, so duplicating every noun lengthens every request.

**The rule stops at regular plurals on purpose.** It handles the three regular
cases — bare `s`, `y`→`ies` after a consonant, `es` after a sibilant — and
nothing else. An irregular plural still needs its own entry. Stemming or
lemmatising the whole term would match more, and would also make a keyword file
stop meaning what it says: the value of this scorer is that a reader can look at
a term and predict what it catches.

**It is asymmetric, and that is the right direction.** A singular keyword
matches the plural; a plural keyword does not match the singular. So the
guidance is simply "list the singular". The reverse rule would have `models`
catch `model` and make the two forms interchangeable, which loses the ability to
target a plural deliberately.

## Trade-offs and rejected alternatives

- *Filling in the plurals by hand across all five topics.* Rejected above: 41
  gaps, most with no correct mechanical completion, and the problem returns with
  the next keyword anyone writes.
- *A stemmer (Porter, Snowball) over both keyword and text.* Rejected: it would
  make `train` match "training" and `reason` match "reasoning", which is a much
  larger behaviour change than the bug being fixed, and it breaks the property
  that a keyword file can be read literally.
- *Leaving it and documenting the trap in the topic template.* Rejected: the
  trap had already been documented in this deployment's topic files and was
  still walked into twice afterwards.

## What a reviewer should check

- The suite: `python3 -m unittest discover -s tests -t .` — 159 tests, ten of
  them new in `PluralMatchingTests`.
- That word boundaries survive: `ATE` must still not match "Water heaters", and
  `GRPO` must still match "GRPO training". Both are tested.
- The vowel-`y` case: `cache key` must match "cache keys", not "cache kies".
- What it changes in practice. On this archive, re-scoring the stored 45 papers
  after the fix admitted one paper to a topic it had been missing, and no paper
  lost one.

## Downstream impact

**This changes what every existing topic matches.** Any deployment with topic
files will see more items accepted, because every singular noun keyword now also
catches its plural. That is the intended correction, but it is a scoring change,
so a deployment that has tuned `min_score` against the old behaviour should
re-check its thresholds and its `data/index/rejected.jsonl`.

Deployments that listed both forms already — as this one did in several places —
are unaffected in outcome; the duplicate entries become redundant but stay
harmless, and they still widen the arXiv query, which is a reason to leave them.

To apply the change to an existing archive rather than only to future
collection, run `scripts/retopic.py` (note 0012).

## Correction (0018)

The Downstream impact section above says duplicate keyword entries "become
redundant but stay harmless". **That is wrong.** The scorer counts distinct
matched keywords, so a list carrying both `reasoning model` and `reasoning
models` matches twice on one occurrence and scores double — enough to push a
single abstract mention from 0.25 to 0.40 and over a 0.35 threshold. The first
real collection after this commit accepted roughly a third off-topic papers for
that reason. See [0018](0018-duplicate-keywords-double-count.md), which removes
the duplicates. The advice to leave them in for arXiv query breadth should not
be followed.
