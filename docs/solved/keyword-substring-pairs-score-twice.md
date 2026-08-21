# A keyword that contains another scores the same words twice

**Status:** solved 2026-08-21 by **option 4** — see [Resolution](#resolution) at
the foot of this file and [note 0098](../commit/0098-a-redundancy-the-author-has-to-see.md).

Four tracked keyword pairs have one term as a substring of the other, so a
single occurrence in a title matches both and contributes twice to the score.

| Topic | Contained | Containing |
| --- | --- | --- |
| `reasoning-training` | `reasoning model` | `large reasoning model` |
| `reasoning-training` | `chain of thought` | `chain of thought distillation` |
| `reasoning-training` | `chain of thought` | `long chain of thought` |
| `test-time-scaling` | `chain of thought` | `chain of thought prompting` |

Reproduce with:

```bash
python3 - <<'PY'
import yaml, glob, pathlib
for p in sorted(glob.glob("config/topics/*.yaml")):
    if pathlib.Path(p).name.startswith("_"): continue
    kw = [str(k) for k in (yaml.safe_load(open(p)).get("keywords") or {}).get("any") or []]
    for a in kw:
        for b in kw:
            if a != b and a in b:
                print(f"{pathlib.Path(p).stem}: {a!r} in {b!r}")
PY
```

## Why it happens

`enrich/score.py` loops over `keywords_any` and adds `title_weight` for each
term that matches, with no notion that two terms might be the same occurrence.
That is a deliberate property of the design — the file's own docstring says a
keyword rule you can read and correct beats an opaque score — and the cost of
that simplicity is that redundancy in the list is the author's problem.

## What it actually costs

Measured when the pairs were found: a paper titled "…long chain of thought…"
scores 0.50 instead of 0.667 — the saturating normalisation
`raw / (raw + title_weight)` compresses the error, and the inflation only ever
pushes a paper *up*. Across the batch checked it **flipped zero acceptance
decisions**, because a paper matching one of these phrases in its title clears
`min_score: 0.35` on the single match alone.

So this is not currently costing the archive papers. It is worth fixing because
the score is also what orders the abstract-fetch budget and the sweep backlog,
and because the same class of bug is the kind that starts mattering the moment
somebody tunes a threshold against numbers that are quietly wrong.

## What it is not

Not the plural bug. [template 0017](../commit/0017-keywords-match-regular-plurals.md)
made `bias` match `biases`, and its note flagged that a redundancy check
"belongs in the test suite or a config check; it is not there yet." It still is
not. This is that gap, with four live instances.

## Options considered

1. **Drop the contained term from the topic file.** Cheapest, and wrong: the
   short term is the one with broader recall, so dropping `chain of thought`
   loses every paper that says only that.
2. **Drop the containing term.** Loses the ability to weight a more specific
   phrase higher, which is presumably why it was added.
3. **Count the longest match only.** Change `score_item` so a term whose match
   span is already covered by a longer term's match does not add again. Correct,
   but it puts span bookkeeping into a function whose whole value is that it can
   be read in one sitting.
4. **Leave scoring alone and check the config.** A test that fails when one
   `keywords.any` entry contains another, so the topic author is told to decide.
   Keeps the scorer simple and puts the judgement where the redundancy was
   introduced.

**Leaning toward 4**, which is also what the 0017 note anticipated. It needs a
decision about whether an intentional pair should be expressible — an
`allow_overlap` flag, or simply a comment in the topic file — before it can be
written as a hard failure rather than a warning.

---

## Resolution

**Option 4, as this document leaned.** `config.overlapping_keywords` reports the
pairs, `run_daily` says them before it collects, and a test pins the set found in
`config/topics/`. Commit `feat(config): report keyword pairs that score the same
words twice`, note [0098](../commit/0098-a-redundancy-the-author-has-to-see.md).

The scorer is untouched, which is option 3 rejected for the reason given here:
span bookkeeping would go into a function whose whole value is that it can be
read in one sitting.

**The four pairs are recorded, not resolved.** Which term to drop is an
editorial decision about what a topic tracks — the short one has broader recall,
the long one is presumably there to weight a specific phrase higher — and
`CLAUDE.md` reserves that decision. The test carries the four as a baseline, so a
**fifth cannot appear without failing the suite**, and removing one is part of
the same edit as the topic file.

**The `allow_overlap` question this document raised did not need answering.** It
was framed as a prerequisite for writing the check as a hard failure rather than
a warning. A pinned baseline is a hard failure that needs no such flag: an
intentional pair is expressed by being in the list, and the comment above it says
it is unresolved rather than approved. If the group later wants a pair marked
intended in the topic file itself, that is a smaller change from here.

**It uses the scorer's own matcher, not a substring test.** The reproduce script
in this document uses `a in b`, which agrees on all four live pairs and would
also flag `ate` inside `state` — a pair the scorer never double-counts, because
`common/text.py` matches on word boundaries. A check disagreeing with the scorer
about what an occurrence is would report pairs that cost nothing and miss pairs
that do.

This closes the gap [note 0017](../commit/0017-keywords-match-regular-plurals.md)
named when it made keywords match plurals: *"a redundancy check belongs in the
test suite or a config check; it is not there yet."*
