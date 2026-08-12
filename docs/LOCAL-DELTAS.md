# Local deltas — what this archive changed in the code it inherited

Everything under `pipelines/` except `pipelines/local/` arrived as a general
template for running a literature archive. This file is the register of every
place this archive has changed that code for reasons of its own.

**Read it before replacing any file under `pipelines/` with a newer version of
itself**, and run the suite after. Each delta is marked at the site with a
`LOCAL` comment, so `grep -rn "LOCAL" pipelines/ .claude/` finds them all and
this table only has to say what to look for.

## Why a register is still needed

This repository is now the only one involved: there is no second checkout and no
`src` remote to pull from — `origin` is the repository the template itself is
developed in, and the archive lives here too. A delta below is therefore not
"our change to somebody else's file" any more. It is simply this repository's
code.

The register survives that change of status for one reason: **these files are
still written as a general template, and a general template gets improved by
replacing a file wholesale.** Every update of that shape — taking a newer
`enrich/queue.py`, copying an improvement in from another deployment, reverting
a file to its shipped state — silently removes any delta inside it. Nothing
fails; the tests that ship with the file still pass, because the delta was never
theirs to test.

That is not hypothetical. On 2026-08-12 three collection fixes were lost exactly
this way, and were noticed only because an agent-memory note claimed they existed
and the claim was checked against the code. They are entry 3 below.

## Why anything is here at all

Three of the four additions live cleanly in `pipelines/local/` and need only a
one-line call site. The fourth cannot: **the `model` wiki kind is a schema
change**, and a schema change is cross-cutting by construction. A fourth entity
kind touches the record, the harvest, the validator, the applier, the reader's
output contract and the directory layout at once. There is no seam to hide it
behind, so it stays spread across the template-shaped files as a marked delta.

Dropping it is not an option — 33 wiki notes and 123 wiki entities depend on it,
and it was a deliberate editorial decision
([0011](commit-local/0011-a-model-is-not-a-dataset.md)). The right long-term
ending is for the template itself to adopt the kind; until then, this.

## The deltas

### 1. The `model` entity kind — 7 files

`src` has `KINDS = ("concept", "method", "dataset")`. This deployment has a
fourth, because a checkpoint is not a corpus.

| File | What to re-apply |
| --- | --- |
| `common/paths.py` | `WIKI_KINDS` tuple (the single source of truth) and `wiki_kind_dir("model")` in `ensure()` |
| `enrich/concepts.py` | `KINDS = WIKI_KINDS`, rank 4 for `model`, and `("model", summary.models)` in both harvest sites |
| `common/schema.py` | `models: list[str]` on `PaperSummary` and `VideoSummary` |
| `common/llm.py` | `models` in both output schemas, the "not models" wording on `datasets`, and `CONCEPT_OUTPUT_SCHEMA["kind"]` built from `WIKI_KINDS` rather than spelled out |
| `enrich/queue.py` | `models` in `_LIST_FIELDS["paper"]`, and the concept-kind check against `WIKI_KINDS` |
| `enrich/apply.py` | `models=list(result.get("models") or [])` in `_apply_paper` **and** `_apply_video`, and `declared in WIKI_KINDS` in `_apply_concept` |
| `publish/graph_page.py` | `model` in `_KINDS`, `_shape`, `_legend` and `_table` |

**Two of those files moved under us**, in the template update adopted on
2026-08-12: the harvest left `publish/wiki.py` for `enrich/concepts.py` and the
appliers left `render.py` for `enrich/apply.py`, because `src` now forbids
`publish/` from writing to `data/` and asserts it in `tests/test_layering.py`.
The delta is the same; only the address changed. A grep for `LOCAL` finds it
either way, which is why the marks are worth more than this table.

`publish/graph_page.py` is new in `src` and had no entry here, so the first
render after the update drew all 123 model nodes as circles **labelled
"Concept"** — the page had no idea a fourth kind existed. Worth remembering as a
shape: a delta list only covers files that existed when it was written, and a
template update that adds a file adds a place for the delta to be missing.

The graph page carries one **known limitation**: the palette validates three
entity hues, so `model` takes the concept hue and is separated by shape and
label alone. Colour does not distinguish the two there. Retiring that needs a
fourth validated step in `templates/wiki/graph.html`, not a guessed colour.

**The reader-facing half is the other one that gets forgotten**, and it failed
the same silent way. The validator was widened to `WIKI_KINDS`; the `kind` line
in `CONCEPT_OUTPUT_SCHEMA` was not, so for every definition task the reader was
offered three kinds and could only ever answer three. Because a stored
definition freezes an entity's kind against re-derivation, one such answer
demotes a correctly harvested model permanently. Fixed in
[0051](commit/0051-a-kind-that-is-accepted-is-offered.md) by enumerating the
tuple instead of writing it out, and guarded by `DefinitionContractTests`.

**The applier line is the one that gets forgotten.** It was omitted when the
kind was first added here, and the failure was silent: `PaperSummary.models`
defaults to `[]`, so every `models` a reader submitted was dropped between the
queue and the store and the field merely looked unused. It went unnoticed for
80-odd summaries. See `docs/commit-local/0021-the-model-kind-reached-half-the-pipeline.md`.
If you re-apply nothing else from this section, re-apply that.

### 2. Call sites for `pipelines/local/` — 3 files, one line each

| File | Line |
| --- | --- |
| `enrich/queue.py` | `errors.extend(placeholders.check(kind, result))` in `validate_result` |
| `collect/conferences.py` | `local_abstracts.fill_missing(...)` at the end of `collect()`, after deduplication |
| `render.py` | `queue_share.summary_cap(cfg)` on the first `queue_missing_summaries` call, and the release of the unused reserve after `queue_missing_definitions` |

`render.py` also carries the `_UNSET` sentinel and the `max_pending` parameter
those two calls need.

Both call sites take `queue_share.pending_count(cfg)` on either side and report
the difference, rather than using the return value. That is not decoration: the
function returns how many records lack a summary, so two passes over one
backlog report it twice. Re-applying the reserve without this reports double
(note 0032).

### 3. Three collection fixes the template does not carry — 2 files

These were made here on 2026-08-09 (notes 0028–0030), **in template-owned files,
and were never written down as deltas.** Adopting a newer template on 2026-08-12
therefore reverted all three silently, and they were only noticed because the
agent-memory note that recorded them was being checked against the tree. That is
the whole argument for this file existing, so the entry is kept even though the
right ending is `src` taking the fixes.

| File | What to re-apply |
| --- | --- |
| `collect/arxiv.py` | the `barren` list, the per-topic `answered` flag, and `targets = topics if mode == "always" else barren` — the listing fallback is gated **per topic**, not on whether the whole run collected anything |
| `collect/arxiv_listing.py` | `Entry.announced`, filled by `parse_days`; `published`/`year` on `_to_paper`; `parse_days` rather than `parse_listing` in `collect()`; and `coverage.record` **before** the abstract backfill as well as after |

`tests/test_local_collection.py` is the guard, and it is ours precisely so a
template update cannot replace it. If it fails after an update, one of the three
has been reverted again — the class name says which.

### 4. This archive's routine state, in the general routine doc — 1 file

| File | What to re-apply |
| --- | --- |
| `docs/daily-routine.md` | the `<!-- LOCAL -->` block at the end of **Scheduling**: the paused Routine, its id, and the three things to settle before re-enabling it |

Deployment state in a general document is not where it would go if there were
somewhere better, and there is not: the trigger's prompt lives in the account,
not in any checkout, so nothing in the repository points at it unless something
here says so. Losing that block means the next session cannot tell a routine that
is *paused* from one that never existed, and re-enabling it blind would advance
a different archive. See `docs/issues/` for defects, which is a different kind of
state and has its own home.

### 5. The commit-notes skill names `docs/commit-local/` — 1 file

`.claude/skills/commit-notes/SKILL.md` is the template's, and the template has
one note directory. This deployment has two, so the skill has to say which.

| File | What to re-apply |
| --- | --- |
| `.claude/skills/commit-notes/SKILL.md` | the `<!-- LOCAL -->` block after the intro, and `docs/commit/` → `docs/commit-local/` in the frontmatter `description`, step 2, step 5 and the step 6 message example |

The block is what carries the part that is not a find-and-replace: both
sequences number from 0000, so a bare ``[0021](0021-…)`` inside a local note
silently points at a different change, and a cross-directory reference needs
`../commit/`. That mistake has already been made once —
`docs/commit-local/0026-a-correlate-is-not-a-mechanism.md` was first written
into `docs/commit/` with template-numbered links, because the skill still said
to put it there. The split landed in
[0024](commit-local/0024-take-the-template-update-and-separate-our-work.md) and
the skill was not updated with it.

**This delta is not applied here, and the entry is kept to say why.** It was
written when `docs/commit/` belonged to somebody else. In this repository that
directory is our own note sequence and `CLAUDE.md` requires a note in it for
every change, so pointing the skill at `docs/commit-local/` would contradict the
contract. `docs/commit-local/` is now imported history: read it, never add to it.
What survives from the paragraph above is the hazard — both sequences number from
0000, so a cross-reference between them must spell the directory out.

## What is *not* a delta

These were never template files, so a file-replacing update never touches them:

- `pipelines/local/` — the extension package itself
- `config/topics/*.yaml` — the five tracked topics
- `scripts/` — `discard.py`, `retopic.py`, `backfill_abstracts.py`, `strip_placeholder_entities.py`, `migrate_model_kind.py`
- `tests/test_local.py`, `tests/test_model_kind.py` — ours, but they call into
  template modules, so a template update that moves a function moves their call
  sites too. That is what they are for: after the 2026-08-12 update they were
  the only thing that failed, and each failure named a delta whose file had
  moved.
- `docs/commit-local/` — the archive's own commit notes, from before it moved here
- everything generated: `archive/`, `outputs/`, `wiki/`, `data/`

`config/sources.yaml` is a merge rather than a delta: four things in it are this
archive's editorial decisions rather than defaults — the arXiv categories,
`openreview.enabled: false`, the venue list, and the `conferences.abstracts`
block. Each is marked `LOCAL` in the file, so a file taken from elsewhere has to
have them re-applied.

## Replacing a template-shaped file

1. `grep -rn "LOCAL" pipelines/ .claude/` on the **current** tree first, so you
   know what you are about to overwrite.
2. Replace the file.
3. Re-apply every row of the tables above that names it.
4. `python3 -m unittest discover -s tests -t .` — `tests/test_local.py`,
   `test_model_kind.py` and `test_local_collection.py` are the files that fail
   if a delta was missed. They are ours and live outside the template's own test
   files for exactly that reason.
5. `python3 -m pipelines.render` against the real archive before committing. The
   suite uses a sandbox; only a real render proves the stored records still load.
6. Update this file in the same commit if the delta moved or changed shape.

## Deltas worth folding into the general template

Each one that becomes ordinary template behaviour is one fewer thing on this
list, and these are not specific to this archive:

- The `model` kind, in full.
- The placeholder rejection — the failure it prevents is not specific to this field.
- The definition-queue reserve — the starvation it fixes affects any deployment with a reading backlog.

The abstract backfill is more arguably specific to this archive: it exists
because DBLP is a heavy source here, and the template moved toward fetching the
PDF instead. The two are complementary — `collect/pdf_fetch.py` feeds the reader,
`local/abstracts.py` feeds the scorer, and the scorer runs first — but the DBLP
dependence that makes it urgent is this archive's, not every archive's.
