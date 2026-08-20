# 0078 — A kind that is accepted is offered

| | |
| --- | --- |
| **Commit** | `fix(enrich): the definition schema offers every kind the validator takes` |
| **Scope** | `pipelines/common/llm.py`, `tests/test_model_kind.py`, `docs/LOCAL-DELTAS.md` |
| **Kind** | fix |

## What changed

`CONCEPT_OUTPUT_SCHEMA["kind"]` is now built from `WIKI_KINDS` instead of
spelling the kinds out, so the list a reader is offered is the list the
validator accepts, by construction.

It had drifted. When the `model` kind was added here, `enrich/queue.py` was
widened to check against `WIKI_KINDS` — but the schema string handed to whoever
answers a definition task still said *"one of: concept, method, dataset"*. For
every one of the 41 model entities this archive has promoted, the reader was
shown three kinds and could only ever answer three.

`DefinitionContractTests` in `tests/test_model_kind.py` now asserts both
directions — every kind in the tuple appears in the offered string, and every
kind in the offered string survives the validator — plus that an invented kind
is still refused.

## Why it matters

The failure is silent and it is not recoverable by a later pass.

A model entity is harvested with `kind: "model"` correctly: `_upgrade_kind`
ranks `model` above `dataset`, and `test_model_outranks_dataset_for_the_same_name`
covers that. The damage happens one step later. Once the entity crosses the
promotion threshold a definition task is filed, the reader follows the schema
and answers `dataset`, the validator accepts it because `dataset` is a real
kind, and `_apply_concept` writes it over the harvested value.

Then it sets. `enrich/concepts.py` treats a stored definition as somebody having
ruled on what the entity is, and stops applying `_upgrade_kind` to it:

```python
if old and old.definition:
    concept.kind = old.kind
    ruled.add(slug)
```

That rule is right — a person's judgement should outrank a side effect of which
list a summary happened to use. It is only wrong when the person was never
shown the option. The note moves out of `wiki/models/`, the wiki cleanup deletes
the file it left behind, and no counter reports anything, because from the
pipeline's point of view a reader ruled and the ruling was honoured.

## What it costs

Nothing at runtime; the string is built once at import. `common/llm.py` now
imports from `common/paths.py`, which is a new edge between two modules in the
same package and does not cycle — `paths` imports only the standard library.

The wider cost is that this is a fourth site for the `model` delta in a file
that already carried two, and `docs/LOCAL-DELTAS.md` gains a row for it. A
template update that replaces `common/llm.py` wholesale now silently reverts
three things rather than two.

## What it does not do

It does not repair entities already misfiled this way. Nothing here searches for
a `model` that was defined as something else — the kind is authored data at that
point, and re-deriving it against a counter is the thing this repository
declines to do everywhere else. `scripts/migrate_model_kind.py` moves names out
of `datasets` on *summaries*; the equivalent for a ruled concept record would be
a different tool and is not written.

It also does not address the same shape in the other direction: a reader can
still omit `models` from a paper reading entirely, and nothing complains,
because the field is optional and empty is a legitimate answer. That one is a
real gap and is left alone deliberately — a required-field rule would force a
guess where the honest answer is silence.
