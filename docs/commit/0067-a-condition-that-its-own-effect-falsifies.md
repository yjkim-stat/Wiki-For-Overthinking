# 0067 — A condition that its own effect falsifies

| | |
| --- | --- |
| **Commit** | `feat(scripts): retire the records an alias ruling orphans` |
| **Scope** | `scripts/merge_concept_aliases.py`, `tests/test_local_aliases.py`, `docs/issues/concept-alias-candidates.md` |
| **Kind** | feat |

## What changed

A one-off that folds every record `config/concept-aliases.yaml` has orphaned
into its canonical, plus a `--candidates` mode that lists the collisions nobody
has ruled on.

Declaring an alias redirects the harvest (note 0063). It does nothing to the
`data/concepts/aime24.json` already on disk — and that record has a definition,
so the harvest's carry-over rule resurrects it every pass. Two notes, one
benchmark, for ever.

## Why it is a script and not a render step

Retiring a record destroys authored text. `CLAUDE.md` is explicit that a counter
must not discard written work, and a render that quietly deleted definitions
whenever a config file changed would be exactly that. So: `--apply` is required,
every retired record is copied to `data/concepts/retired/` before removal, and
the whole thing is auditable after the fact — the same argument that keeps
`migrate_model_kind.py` and `backfill_summary_models.py` in the tree.

## Why the definition is not carried across

When the retired record has one and the canonical does too, the canonical's is
cleared as well, so the merged entity is re-queued and re-derived against the
union. That is the point: for `AIME 2024`, neither of the three definitions had
seen more than 28 of the 39 sources.

Moving the better definition onto the canonical instead was considered and is
worse than it looks. `render` reads how many sources a definition was written
against from the archived queue task, keyed by the concept's **name**
(`_definition_source_count`). A definition that changes names loses its
staleness count and reads as current for ever — the one failure mode this
archive treats as worse than a missing definition.

## The bug worth recording

The first `--apply` reported five definitions cleared and wrote none of them.

```python
if old.definition and new.definition:
    ...
    new.definition = ""          # cleared here

if apply and (added or (old.definition and new.definition)):
    _write(...)                  # ...and the condition is now False
```

The write condition re-tested `new.definition`, which the clearing two lines
above had just emptied. The clearing succeeded in memory, was announced on
stdout, and falsified its own precondition to be written.

What made it cost time was that the symptom pointed somewhere real: the
definitions were back after `render`, and this repository genuinely does have a
rule that carries a stored definition across a rebuild. Two files were read
before the third. The lesson is narrow and worth the note anyway — **a
side-effecting branch and the condition that persists it must not be the same
expression evaluated twice.** It is now decided once, into `clearing`, before
the mutation.

Five tests cover the script, and the first of them is that one.

## What `--candidates` is for, and is not

It prints 99 names that some reader declared as an alias and that are separate
records here. It is a worklist for a person, and the script says so on its last
line, because acting on the list mechanically is precisely the failure note 0063
describes: readers use `aliases` for spelling variants and for neighbours alike.

`docs/issues/concept-alias-candidates.md` sorts them by evidence at stake and
names the largest group — eleven base/instruct checkpoint pairs, which want one
ruling made once rather than eleven made separately.
