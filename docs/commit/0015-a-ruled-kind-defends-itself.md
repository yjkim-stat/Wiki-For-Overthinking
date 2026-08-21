# 0015 — A ruled `kind` defends itself against the next harvest

| | |
| --- | --- |
| **Commit** | `fix(wiki): stop harvest reverting a kind a definition task ruled on` |
| **Scope** | `pipelines/publish/wiki.py`, `tests/test_render.py` |
| **Kind** | fix |

## What changed

`harvest` no longer applies `_upgrade_kind` to an entity whose stored record
carries a definition. The ruling in that record wins; everything without a
definition behaves exactly as before.

A definition task rules that an entity is a `concept` rather than a `method`.
The result validated, applied, and the note moved to `wiki/concepts/`. On the
next render it was back under `wiki/methods/`, with nothing logged.

## Why it is built this way

The two values are not the same kind of claim, and the weaker one was winning.

`harvest` derives `kind` from which of a summary's three lists (`concepts`,
`methods`, `datasets`) each name happened to land in, then takes the highest
rank across every summary that mentions it. That is a majority vote over a
field-placement side effect. The definition task's `kind` is a judgement made
once, deliberately, over the whole evidence set, by someone who was asked that
exact question. Rebuilding from scratch each render is right — evidence is
derived data and deriving it fresh keeps phantom mentions out — but a ruling is
not derived data, and it was being rebuilt along with everything else.

**The presence of a definition is the marker**, rather than a new flag. A
definition only exists because a definition task was completed, and that task is
the only thing in the system that asks the kind question directly. Using it
avoids a second source of truth that could disagree with the first.

**A local set, not a field on `Concept`.** The dataclass is serialized to
`data/concepts/`, so a bookkeeping attribute would leak into stored JSON and
become schema. The set lives for one `harvest` call, which is exactly as long as
the fact is needed.

**Without a definition, `_upgrade_kind` still wins.** That is the useful default
for the large majority of entities nobody has adjudicated, and this change must
not quietly alter them.

## Trade-offs and rejected alternatives

**Rejected: make the definition task's kind sticky via a new `kind_ruled`
field.** Explicit, and adds a schema field plus a migration for existing
records, to express something the existing data already implies.

**Rejected: log the disagreement and keep harvesting.** A warning per render for
a decision that was already made correctly is noise that trains people to ignore
the log.

**Cost: a ruling can now go stale.** If an entity is genuinely reclassified by
later evidence — a concept that turns out to name a dataset — the harvest can no
longer correct it, and the definition task has to be re-answered. That is the
right direction for the trade: a human ruling that persists until a human
changes it beats one that silently reverts.

**Known consequence not fixed here:** when a note does move directory,
`_preserved_tail` reads at the *new* path, finds nothing, and substitutes the
default manual section — so hand-written analysis is lost. This commit removes
the most common cause of a move; it does not make moves safe. That is a separate
problem in the note writer.

## What a reviewer should check

That the tests fail without the fix:

```bash
git stash push pipelines/publish/wiki.py
python3 -m unittest tests.test_render   # 1 failure
git stash pop
```

`test_a_ruled_kind_survives_a_further_render` harvests twice on purpose — the
revert was observed on the *second* render in the field, and a fix that only
holds for one pass would pass a single-harvest test.

`test_an_entity_without_a_definition_still_takes_the_harvested_kind` is the one
guarding the default. If it ever fails, this change has stopped being narrow.

## Downstream impact

Deployments that made kind corrections and watched them revert should re-apply
the correction once after pulling; it will then hold. No migration — the fix
reads data that is already there.
