# 0099 — A spelling, said on the day it splits

| | |
| --- | --- |
| **Commit** | `feat(render): report an entity that has split on a spelling` |
| **Scope** | `pipelines/render.py`, `tests/test_fragmented_entities.py`, `docs/issues/`, `docs/solved/` |
| **Kind** | feature |

## What changed

A term spelled two ways becomes two entity records, and **neither is wrong about
anything**: each holds a fraction of the evidence, each gets a definition
written against that fraction, and nothing looks broken. One pair in the archive
that prompted this was found at 39 sources against 5.

`render` now names such a pair every pass, with both source counts.

## Why it is built this way

**Only the narrowest rule fires here.** `pipelines.duplicates`
([note 0072](0072-two-names-for-one-entity.md)) knows four — variant, plural,
suffix, edit distance — and remains a command somebody runs. This reports
*variants* alone: two slugs identical once punctuation is removed.

Two reasons, and the second matters more. A check that fires on every render and
has false positives becomes noise, and noise is how a real warning stops being
read. And the other three rules are precisely the judgements the issue is about:
`MATH` under `MATH500` is a subset, not a spelling. Merging it would not
mislabel a record — it would make the archive **unable to state a distinction it
currently states**, silently, because the merged record reads as complete.

**Reported, never merged, and the warning says where the ruling goes.** It names
`config/concept-aliases.yaml`, the authored map. The issue's own argument for
that map is a row in the harvested `aliases` field declaring
`Llama-3.3-70B-Instruct` an alias of `llama-3-1-70b` — different releases. The
field is harvested and large; the map is authored and small; only one of them can
be merged on.

**The larger record is named first**, so the line reads the way a merge would be
written and a person can skim for the survivor.

**Beside `stale`, not inside it.** An outgrown definition is a cost of time
passing. A split entity is a defect that appeared in one pass, and the value of
saying it is that it is *fresh*.

## Trade-offs and rejected alternatives

**This fires until somebody rules.** Every render names the pair until it is
resolved in the map or the slugs stop colliding. That is the intended pressure
and it is also how a warning becomes wallpaper; the mitigation is that the
variant rule is narrow enough that the list should be short.

**Considered, and rejected in the issue itself**: showing a reader the existing
entity names — 1,927 of them, needing a filter to plausible neighbours, which is
its own problem — and normalising harder in `slugify`, which would rename every
slug in the archive and merge pairs nobody ruled on. That is this issue's failure
mode applied to every name at once.

**It re-derives the pairs on every render**, an O(n²) walk over concept slugs
with a cheap comparison. At a few thousand entities that is milliseconds; the
`duplicates` command does the same work with three more rules.

## What a reviewer should check

Three mutations: accept every `reason_for` rule rather than `variant` (a subset
pair and a plural pair start being reported), stop ordering the pair by evidence,
and stop counting.

- `test_a_subset_relation_is_not_a_spelling` is the one that keeps this narrow.
- `test_it_merges_nothing`, which snapshots `data/concepts/`.
- **The end-to-end test needed real readings.** `render` rebuilds concept records
  from summaries, so hand-made evidence is replaced before the report runs — the
  third time this session a fixture had to be built from the summaries up.

## Downstream impact

`render`'s result gains a `fragmented` count and the log gains a line per pair.
No record is written, no entity is merged, and an archive with no colliding
spellings sees nothing.
