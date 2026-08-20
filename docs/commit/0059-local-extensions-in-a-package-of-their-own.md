# 0059 — Local extensions in a package of their own

| | |
| --- | --- |
| **Commit** | `feat(pipelines): reject placeholders, backfill abstracts, reserve queue slots` |
| **Scope** | `pipelines/local/`, `enrich/queue.py`, `collect/conferences.py`, `render.py`, `tests/test_local.py`, `scripts/` |
| **Kind** | feature |

## What changed

Three additions, each with one call site:

- **`local/placeholders.py`** — a submitted `concepts`/`methods`/`datasets`/
  `models` entry that describes a *set* of things rather than naming one
  ("three reasoning benchmarks (unnamed in abstract)") is rejected by the queue
  validator.
- **`local/abstracts.py`** — a paper that arrived from a bibliographic index with
  no abstract gets one fetched by DOI, after deduplication, before scoring reads
  it.
- **`local/queue_share.py`** — `render` holds back half the pending-task cap on
  its first pass so definition tasks are not crowded out by a reading backlog,
  and releases the unused reserve afterwards.

Also the operator scripts this archive uses: `discard.py`, `retopic.py`,
`backfill_abstracts.py`, `strip_placeholder_entities.py`,
`migrate_model_kind.py`, `refresh_stale_definitions.py`.

## Why it is built this way

The rest of `pipelines/` is written as a general template, and a general
template is improved by replacing a file wholesale. Keeping additions in a
package of their own makes that cheap: the file is replaced and only its
one-line call site has to be re-checked. That is the entire reason the package
exists, and it is why each of these is a function call rather than an edit
inside the function it affects.

Each one fixes a failure that reported success:

- A placeholder phrase is *keyed on* by the wiki, so two unrelated papers that
  phrase their ignorance identically merge into one entity, count each other as
  independent evidence, and cross the promotion threshold as a concept that does
  not exist. The threshold exists to require corroboration; a generic phrase
  manufactures it.
- Scoring weights a title hit 3.0 and an abstract hit 1.0 against a 0.35
  threshold, so "in the abstract twice" is a real path to acceptance — and a
  record with no abstract cannot take it. Whether a paper is archived was
  therefore decided by which index happened to find it first, which is not a
  threshold that can be tuned around because the two populations are being
  measured differently.
- Summaries and definitions shared one cap, summaries were filed first, and any
  reading backlog at all took every slot. The wiki stopped extending itself
  exactly while it was accumulating the most evidence.

**The reserve is a reserve, not a reordering.** Queueing definitions first would
only invert which kind of work starves. The reserve is handed back if
definitions do not want it, so a render with no pending definitions files
exactly as many summaries as before.

**The counts are measured, not returned.** Both `render` call sites take
`queue_share.pending_count(cfg)` on either side and report the difference,
because `queue_missing_summaries` returns records-lacking-a-summary rather than
tasks-filed — summing two passes over one backlog reports it twice.

## Trade-offs and rejected alternatives

The placeholder matcher is two regexes and will have both false positives and
false negatives. Requiring *both* a leading quantifier and a collection noun is
what keeps real names — "ten-fold cross-validation", "Mixture-of-Experts" — out
of the net; the cost is that a bare "several benchmarks" with no disclaimer is
caught while an inventive phrasing is not. Prose fields are deliberately not
checked: "evaluated on three benchmarks (unnamed in the abstract)" is a true and
useful sentence in `results`, and only becomes a problem when offered as a name.

The abstract backfill is not superseded by `collect/pdf_fetch.py`. That fetches
the document so the reader gets the paper; it never fills `abstract`, and
`abstract` is what the scorer reads. One feeds the reader, the other feeds the
scorer, and the scorer runs first.

## What a reviewer should check

- `python3 -m unittest tests.test_local` — all three, including that the reserve
  is released and that the reported count is not doubled.
- The call sites are still one line each:
  `grep -rn "pipelines.local\|from ..local\|from .local" pipelines/`.
- That a lookup failure is survivable: `local/abstracts.py` leaves the abstract
  empty, which is the state before the attempt.

## Downstream impact

A deployment that pulls this gets stricter queue validation: a result naming a
placeholder is now rejected where it previously stored a false entity. Existing
stored placeholders are not removed — `scripts/strip_placeholder_entities.py`
does that on request, using the same rule so the two cannot drift.

`conferences.abstracts` in `config/sources.yaml` gates the backfill and defaults
to enabled.
