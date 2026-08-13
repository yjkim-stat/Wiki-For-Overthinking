# 0052 — A field with no validator is a field that goes missing

| | |
| --- | --- |
| **Commit** | `fix(scripts): backfill the models field on nine readings` |
| **Scope** | `scripts/backfill_summary_models.py`, `docs/LOCAL-DELTAS.md` |
| **Kind** | fix |

## What changed

A one-off script fills `models` on nine paper summaries whose reader left it
empty, from a table transcribed out of each paper's experimental setup.

The readings were otherwise complete and correct. `models` is optional, carries
no validator, and is not mentioned in the task's `instructions` — only in the
`output_schema` block, which a reader who works from the instructions will not
read line by line. Nine consecutive readings omitted it, `render` applied all
nine without a warning, and `reopen` refuses a task once render has consumed
it. `CLAUDE.md` leaves two options for that case, fixing the record or
re-collecting the item; this is the first.

## Why a table rather than a rule

The obvious version of this script was written first and thrown away, and the
reason is the useful part of this note.

Model names are already present in the summaries — a reading's `method` field
routinely enumerates the backbones — so extracting them by pattern looks like a
clean derivation with the rule in the file, exactly as
`migrate_model_kind.py` does. It is not clean. A reading legitimately
abbreviates: *"Experiments use Qwen2.5-3B-Instruct and 7B-Instruct"*. A pattern
over that text yields `Qwen2.5-Instruct`, which appears in no paper and is not
a model.

That failure is not a tuning problem. Prose is not a controlled vocabulary, and
the abbreviation is good writing — the expansion lives in the reader's head and
in the document, not in the sentence. Any rule strong enough to recover the
second name is strong enough to invent names elsewhere.

The cost of getting it wrong is asymmetric and permanent. A missing model keeps
the status quo. An invented one becomes a harvested entity, and an entity that
later receives a definition has its kind frozen, because `enrich/concepts.py`
stops applying `_upgrade_kind` once a definition exists. So the mapping is
transcribed from the documents, every name appears in its paper, and entries
where the transcription was uncertain are deliberately short.

## Why it is kept after running

It has no reason to run twice — it refuses any summary whose `models` is
already populated, so a fresh reading of the same paper overrides nothing. It
stays for the same reason `migrate_model_kind.py` does: it is the record of an
edit made to `data/` outside the queue, and the alternative is nine files that
changed with no account of who changed them or from what.

## What it does not fix

The hole is still open. `models` remains optional with no validator, and the
next reader who works from `instructions` rather than `output_schema` will omit
it again in the same silence. Two candidate defences were considered and
neither is taken here:

- **Requiring the field.** Rejected — empty is a legitimate answer for a paper
  that evaluates nothing, and a required-field rule forces a guess where the
  honest answer is silence. This is the same reasoning that keeps `results`
  optional.
- **Warning when a paper reading returns no models.** Plausible, and cheap: the
  applier could log it the way `_apply_bibliography` logs an unknown topic
  slug. Not done here because it belongs in `enrich/apply.py` rather than in a
  one-off script, and a warning nobody reads is not obviously better than
  nothing. Recorded in `docs/issues/` instead.

Two model names known to be in the source documents are also omitted — the two
judge models in one paper — because they were not transcribed at the time and
re-opening the document to recover them was not worth another pass. A miss is
the cheap failure here; that is the whole argument above.
