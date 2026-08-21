# 0073 — A benchmark sitting is one entity, however it was spelled

| | |
| --- | --- |
| **Commit** | `fix(enrich): a benchmark sitting is one entity, however it was spelled` |
| **Scope** | `pipelines/enrich/concepts.py`, `tests/test_concept_merge.py` |
| **Kind** | fix |

## What changed

`harvest` now merges wiki entities whose names are the same benchmark sitting
written differently — `AIME24`, `AIME 2024`, `AIME2024` — into one entity,
instead of giving each spelling its own slug, its own evidence count, and its
own definition task. The merge is narrow: it only collapses punctuation and
casing differences plus a bare two-digit trailing year expanded to four
(`AIME25` → `aime2025`), so `AIME` (no year) and `AMC` stay the genuinely
separate entities they are, and nothing outside that pattern is touched.

Found running this archive's first backfill: a 14-day collection pulled in
145 papers, and by the time they were read, AIME alone had split across eight
separately-spelled wiki notes (`AIME`, `AIME24`, `AIME25`, `AIME2024`,
`AIME2025`, `AIME 2024`, `AIME 2025`, `AIME'25`), MATH-500 across two, and
HMMT 2025 across two — each with its own now-thin evidence count and its own
defined-from-scratch prose repeating the same facts.

## Why it is built this way

`slug_for` (plain `slugify`) has to stay exact — it is also what keeps `AIME`
and `AMC` apart, and a fuzzier slug would merge things that are not the same
claim. So the fix adds a second, coarser key (`_merge_key`) used only to
*route* evidence to the right entity, while `slug_for` keeps deciding what a
brand-new entity's identity is. Two keys, because the same string needs both
answers at once: exact for "is this a new entity", coarse for "does an
existing entity already speak for it".

Which slug survives a merge is decided once per key, from what is already on
disk (`_canonical_slugs`): a fragment somebody wrote a definition for outrank
one that has not, and among equally-defined or equally-undefined fragments the
lexicographically smallest slug wins. Arbitrary, but fixed — a render that
picked the survivor by iteration order would make "which spelling won" drift
between runs over an unchanged archive, which is exactly the property
`test_layering.py` holds every renderer to.

`link()` used to re-derive `slug_for` from the raw name a second time, so
naming two spellings of the merged entity in one summary would silently no-op
instead of linking (the raw slug of a non-canonical spelling is never a key in
`concepts`). It now takes the already-resolved slugs `entity()` computed, so
the merge and the co-occurrence graph agree with each other.

## Trade-offs and rejected alternatives

Deliberately does not attempt the harder fragmentations found in the same
backfill — `Best-of-N` vs. `best-of-N sampling`, `process reward model` vs.
`process reward model (PRM)`, `Overthinking-Adjusted Accuracy (OAA)` vs.
`AUC_OAA`. Those need recognizing an added or dropped word or a parenthetical
acronym, which is editorial judgement about what a name means, not a
formatting difference — a regex confident enough to attempt it would also be
confident enough to merge two things that are not the same. Left as
same-topic wiki entries cross-referenced by hand through `aliases` and
`related` instead.

Considered normalizing at collection time (inside the summarizer's schema)
instead of at harvest time. Rejected: the fragmentation is a routing decision
about entities already named by many independent readings, not something one
reading can get right in isolation, and `harvest` is already the one place
that reconciles a name against everything already known about it.

## What a reviewer should check

- `python3 -m unittest tests.test_concept_merge -v` — five cases: the merge
  itself, that a year-less name does not join a year-specific group, that the
  merged entity still promotes, that an existing definition wins the survivor
  seat over iteration order, and that unrelated numeric suffixes (`MATH-500`,
  `GSM8K`) do not collide.
- `python3 -m unittest discover -s tests -t .` — full suite, unaffected
  elsewhere (574 tests, all green before and after).
- `_merge_key`'s docstring states the boundary directly; the risk worth
  re-checking on any future change is a name whose real trailing digits are
  not a year (`Top-50`, a hypothetical `GPT-4`-style name with a two-digit
  suffix) colliding with an unrelated one. Not observed in this archive's
  data, but worth an eye if the tracked topic changes.

## Downstream impact

None to a deployment's `config/`. A deployment already carrying fragmented
concept records the way this archive was self-heals silently: the next
`render` merges new evidence into the canonical slug per group and, once a
maintainer clears (or has already cleared) the losing fragments' hand-written
`definition` field, the ordinary stale-record cleanup removes their files.
Nothing needs to be edited by hand for the fix itself to take effect.
