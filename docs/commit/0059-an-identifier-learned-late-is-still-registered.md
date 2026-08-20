# 0059 — An identifier learned late is still registered

| | |
| --- | --- |
| **Commit** | `fix(enrich): register an identifier a record gained after collection` |
| **Scope** | `pipelines/enrich/dedupe.py`, `pipelines/render.py`, `tests/test_identifier_reconcile.py`, `docs/issues/`, `docs/solved/` |
| **Kind** | fix |

## What changed

Deduplication resolves an incoming paper against keys recorded at *collection*
time. A hand-filed PDF has none worth having then: `local_pdf` creates the record
before anything opens the document — deliberately, because a Python parser
guessing at a title poisons the archive quietly — so the only key available is a
fingerprint of the filename.

The arXiv id arrives later, at `queue complete`, and **nothing re-registered the
keys**. So a record sat in the archive holding `arxiv_id: 2503.20314` with no
`arxiv:2503.20314` key, and the day the collector returned that paper it forked
instead of folding: two records for one paper, two archive pages, and every
entity counting it twice. Nothing errored at any step.

`reconcile_identifiers` now registers, on every render, every identifier a stored
record carries that nothing in the index holds.

## Why it is built this way

**Self-healing rather than event-driven.** The issue proposed doing this at apply
time, where the reading writes the identifier onto the record. That prevents the
next duplicate and closes **none of the ones already waiting** — measured on one
deployment, 17 of 22 hand-filed papers carrying an arXiv id were in that state,
and their readings were applied weeks ago. Re-deriving from `data/` every pass
costs a handful of indexed lookups, needs nothing remembered, and covers the
backlog and the future case with one mechanism. It is the same shape
`shelve_documents` uses, for the same reason.

**A key another record already holds is reported, never repointed.** `SeenStore.mark`
updates the canonical of an existing key, so calling it unconditionally would
silently re-map one record's identifier onto another — a merge, performed by a
counter, on the archive's own identity. Where two records claim one identifier
the duplicate already exists, and which of them survives is a judgement about
which fields matter: in the case that found this, the reading is on the `local:`
record and the collection metadata on the arXiv one.

**It writes no record.** `data/index/seen.sqlite` only. The duplicates it finds
stay exactly as they are, reported on every render until somebody decides.

## Trade-offs and rejected alternatives

**Conflicts are reported for ever.** A duplicate nobody merges is logged on every
pass, which is the standing-condition problem the archive keeps running into. It
is left that way on purpose here: unlike a stale definition, a duplicate is a
defect rather than a cost of time passing, and it should not become quiet.

**Considered: merging the pair automatically**, taking the richer record. The
records disagree about which fields are better — one has the reading, one has the
collection metadata — and a merge rule that picked wrong would be unrecoverable
and silent. `merge_papers` exists and is deliberately not called from here.

**Considered: fixing `local_pdf` to key on content instead.** The file's hash is
already the record id; the problem is not that the filename key is weak but that
the *arXiv id* was never registered. Nothing about the ingest path is wrong.

**It runs on every render over every paper.** For an archive of a few thousand
that is a few thousand indexed SELECTs and no writes after the first pass, which
`test_it_is_idempotent` pins.

## What a reviewer should check

Four mutations, each taking down its own tests: register unconditionally (three
fail, including the one asserting the existing owner keeps its key), register
nothing (five), swallow the conflict count, and drop the call from `render`.

- `test_without_the_pass_it_forks` asserts the defect itself, so the fix cannot
  be mistaken for a no-op against a fixture that never reproduced it.
- `test_it_repairs_a_backlog_not_only_the_next_one` is the difference between
  this and the literal reading of the issue's option D.
- `test_it_writes_no_record` — the index moves, the records do not.

## Downstream impact

**On the first render after this lands, a deployment with hand-filed papers will
register identifiers in bulk and may log conflicts.** Each conflict names two
records that are the same paper; merging them is manual and this change
deliberately does not do it. Nothing else moves: no record is rewritten and no
artifact is regenerated differently.
