# 0081 — One entity, many names

| | |
| --- | --- |
| **Commit** | `feat(enrich): an authored map decides which of an entity's names wins` |
| **Scope** | `pipelines/local/aliases.py`, `config/concept-aliases.yaml`, `pipelines/common/config.py`, `pipelines/enrich/concepts.py`, `tests/test_local_aliases.py` |
| **Kind** | feat |

## What changed

The harvest keys a concept by `slugify(name)`, so two summaries writing *AIME24*
and *AIME 2024* build two records. `config/concept-aliases.yaml` is where
somebody rules that they are one, and `pipelines/local/aliases.py` applies it.

Fifteen redirects are seeded, all of them spelling: punctuation variants of the
same token, and four acronym-expansion pairs. They fold 15 records into 9.

## Why the `aliases` field could not do this

A `Concept` already carries one, and it is already populated — `aime-2024`
listed *AIME24* as an alias while `aime24` existed as a separate record with
three times the evidence. It is tempting to merge on it and it would be wrong.

That field is filled from what a reader wrote in a summary, and readers use it
for two relations at once. Some entries are another spelling. Others are a
neighbour, a parent or a child: *MATH* is declared an alias of `math500`, which
is 500 problems drawn from it; *GPQA* of `gpqa-diamond`, which is its hard
subset; *causal tracing* of `activation-patching`, which this archive's own note
argues measures a different quantity. Merging on that field would not mislabel
records — it would make the archive unable to state distinctions it currently
states, silently, because the merged record reads as complete.

So the map is authored. `scripts/merge_concept_aliases.py --candidates` prints
the 99 unruled collisions; `docs/issues/concept-alias-candidates.md` sorts them.

## What the fragmentation cost

Every record accumulates its own share of the evidence, crosses the promotion
threshold separately, and is handed to a reader as a definition task that sees a
fraction of the sources. Nothing reports it: both records look complete.

`AIME 2024` was spread over three slugs holding 9, 28 and 2 sources — so the
best-informed of its three definitions was written against 28 of 39, and the
worst against 2. `MATH500` over two, at 27 and 12.

## The redirect is not enough on its own

`slug_for` decides which record a name files under. It does not decide what the
record is *called*: `entity()` titles a new `Concept` with the name in hand, so
`AIME24` arriving before `AIME 2024` folds correctly into a note titled
*AIME24*. That is the same arbitrariness the map exists to remove, now invisible
because the merge looks like it worked.

So the map keeps the canonical name as written, and `entity()` prefers it. This
is why the delta is two lines in `enrich/concepts.py` rather than one, and why says restoring only the obvious one is worse than
restoring neither.

## What it refuses

Three malformed maps raise rather than resolving to something:

- **An alias of itself.** Always a typo in one of the two spellings, and
  otherwise a silent no-op.
- **One alias claimed by two entities.** The result would depend on iteration
  order.
- **A chain**, `a → b → c`. Same reason; the fix is always to point the first
  entry at the end of the chain.

## What it costs

Nothing for a deployment with no map: a missing file is an empty map, `slug_for`
is the identity it was, and `test_without_a_map_two_spellings_stay_two_records`
pins that — every other test in the suite was written against that behaviour.

`common/config.py` gains an edge on `pipelines/local/`, imported inside `load()`
so `common` keeps no import-time dependency on `local`. Installing at
config-load time rather than resolving lazily inside `slug_for` is deliberate:
that function is called from four modules with no config to hand, and `--root`
is an argument rather than an environment variable, so a lazy resolver would
read the wrong tree exactly when the two trees differ.

## What it does not do

It does not touch records already on disk. A record written under a name that
has since become an alias keeps its definition, and the harvest's carry-over
rule resurrects it every pass — so declaring an alias without retiring the
orphan changes nothing visible. That is note 0064.

It also does nothing to stop the next fragmentation. The cheapest defence is a
render-time warning when two slugs differ only by punctuation; it is recorded in
`docs/issues/` and not built here.
