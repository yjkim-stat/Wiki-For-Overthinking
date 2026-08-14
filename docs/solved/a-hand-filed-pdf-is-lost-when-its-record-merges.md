# A hand-filed PDF is re-downloaded and orphaned when its record merges

**Status:** solved 2026-08-13 by **option A** — see [Resolution](#resolution) at the
foot of this file and [note 0047](../commit/0047-a-filed-document-survives-its-merge.md).
**Kind:** fix
**Found:** 2026-08-12, filing two PDFs into `inbox/` for papers the archive already held
**Touches:** `pipelines/enrich/dedupe.py`, `pipelines/collect/pdf_fetch.py`, `pipelines/run_daily.py`, `tests/`

Drop a PDF into `inbox/` for a paper the archive already knows about. The
collector ingests it, deduplication correctly folds it onto the existing record —
and then the pipeline downloads the same document again from the internet, and
leaves the copy the person filed sitting on disk under a name no record points at.

Nothing reports a problem. The collector logs an ingest, `pdf_fetch` logs a
fetch, the reading task gets a document, and the answer validates. The only
visible trace is a file in `data/pdfs/` that never moves and never gets read.

---

## What you can observe

```bash
export RA_WM_ROOT=/path/to/an/archive
cd /path/to/this/checkout

# pick a paper the archive already has, put its PDF in the inbox under any name
# whose title normalises to the stored title
cp ~/some-paper.pdf "$RA_WM_ROOT/inbox/Some Paper, With A Comma For The Colon.pdf"

python3 -m pipelines.run_daily --source local
python3 -m pipelines.render

# the record claims a document…
python3 -c "import json,glob;[print(json.load(open(f))['id'], json.load(open(f))['local_path']) \
  for f in glob.glob('$RA_WM_ROOT/data/papers/*.json') if json.load(open(f)).get('local_path')]"

# …and there is a second, identical file nobody claims
sha1sum $RA_WM_ROOT/data/pdfs/*.pdf
```

**The case that found it.** Two PDFs were filed for `arxiv:2503.15558` and
`arxiv:2601.16163`. Both merged onto the right records — no duplicate papers, the
title fingerprints matched exactly. Both were then re-downloaded from arXiv, and
both filed copies remain at `data/pdfs/local-ba6b91360ccccfd7.pdf` and
`data/pdfs/local-e1042da4004da8b2.pdf`, claimed by no record and never shelved.
The downloaded bytes were SHA-1 identical to the filed ones, so nothing was
corrupted — this run was lucky, see *Why it matters* below.

---

## Why it happens

**1. `merge_papers` does not carry `local_path`.** In
`pipelines/enrich/dedupe.py:32-69`, an incoming record is folded into the stored
one field by field. The list is explicit:

```python
for field_name in ("abstract", "venue", "doi", "arxiv_id", "pdf_url", "url"):
```

followed by `authors`, `year`, `published`, `updated`, `categories` and `source`.
`local_path` (`pipelines/common/schema.py:71`) is not among them, so the merged
record comes back with the stored record's value — empty — and the incoming
record's path is discarded. The local collector has already moved the file out of
`inbox/` to `data/pdfs/<fs_id(paper_id)>.pdf` by then
(`pipelines/collect/local_pdf.py:62`, `:123`), and that name is derived from the
*local* id, which the merge has just thrown away.

Note the asymmetry that makes this survivable-looking: `source` **is** merged, so
the record reads `seed+local` and `Paper.is_local` (`schema.py:93`) returns True.
The archive says it holds a hand-filed paper. It just does not say where.

**2. The guard that would have caught it tests the field that was dropped.**
`pipelines/collect/pdf_fetch.py:84-86`:

```python
# A hand-filed PDF is already on disk, and its file is the original.
if paper.local_path:
    continue
```

That comment is exactly right and the condition is exactly the one that no longer
holds. With `local_path` empty, the branch does not fire, `pdf_fetch` falls
through to `client.get(paper.pdf_url)`, writes the body to
`data/pdfs/<fs_id(record.id)>.pdf` and sets `local_path` to *that*. So the record
ends up pointing at a downloaded copy while the filed one is orphaned.

**3. Nothing downstream can notice.** `run_daily.py:271-282` only reaches the
fetch when the paper has no summary yet, then saves the record if `local_path` is
set — which it now is, so the run looks clean. `shelve_documents`
(`pipelines/render.py:171`) files documents *by record*, so a file no record
points at is never moved, never shelved, and never reported.

---

## Why it matters more than a duplicate file

**The failure mode is the opposite of what the design promises.** `local_pdf.py`'s
module docstring says filing a PDF by hand *is* the editorial decision, and
`pdf_fetch`'s comment says the person's file is the original. Both are correct
statements of intent, and in this path the pipeline does the reverse: it prefers
a network copy over the one it was handed.

**The lucky case hides the unlucky one.** In the run that found this, the arXiv
*API* was returning HTTP 429 throughout while the PDF host happened to answer. If
the fetch had failed, `pdf_fetch` would have counted it under `failed`, the record
would have carried no document, and the reading task would have been filed with an
abstract and no attachment — with the document sitting two directories away. The
queue's own contract then makes it worse rather than better:
`enrich/queue._check_reading_basis` **refuses** a reading that declares
`read_from: "document"` when the task attached none, so a reader who had opened the
filed PDF would have had to record `abstract` or be rejected. The archive would
have permanently recorded a weaker evidence tier than the one it actually had.

**It inflates the tier the migration guarantees to carry.** `migrate._hand_filed`
(`pipelines/migrate.py:162-176`) builds `recorded` from `paper.local_path`, so an
orphan is in neither `hand_filed` nor `recorded`, and `build_plan` reaches the
fallback at `migrate.py:213-221`:

> On disk with no record pointing at it. Its provenance cannot be established, so
> it cannot be shown to be re-fetchable — and the safe reading of "unknown" is the
> one that does not throw the file away.

That rule is right; the bug is that it is being asked a question that should never
arise. Measured on the archive where this was found, the `irreplaceable` tier went
from **7 files / 169.5 MB** to **11 files / 235.5 MB** across one run — and 34.5 MB
of that is two exact duplicates of files the bundle is already carrying.

---

## Options

### A. Carry `local_path` through the merge, preferring the stored one.

Add to `merge_papers`, after the existing field loop:

```python
if incoming.local_path and not merged.local_path:
    merged.local_path = incoming.local_path
```

- **For:** three lines, at the site of the defect, and it makes the `pdf_fetch`
  guard fire as its comment already claims. A filed document beats a download,
  which is the stated intent everywhere else.
- **Against:** `merge_papers` elsewhere prefers the *longer* or *richer* value; this
  field needs a different rule (prefer the existing path if there is one, because
  a stored path may already have been shelved into `data/pdfs/read/` and
  overwriting it would strand the record). Write the condition, not
  `max(len(...))`.
- **Leaves behind:** nothing new, but does not clean up orphans created before the
  fix.

### B. As A, plus have the local collector not move the file until its record resolves.

Ingest into a staging path, resolve the record, then move once to the canonical
`fs_id(record.id)` name.

- **For:** no duplicate is ever written, so there is nothing to reconcile and the
  file is named for the record that actually owns it from the start.
- **Against:** the collector currently moves-then-returns and knows nothing about
  deduplication; this inverts that and couples `collect/` to `enrich/`. The
  module docstring's promise that "identity is the file's content" would need
  re-reading, since the stored name would become identity-of-record rather than
  identity-of-content.

### C. Report orphans rather than fixing the cause.

Have `migrate status` (or `render`) list PDFs in `data/pdfs/` that no record
claims.

- **For:** cheap, and useful independently — an orphan can arise other ways.
- **Against:** it is a smoke detector, not a fix. Taken alone it leaves the
  re-download, the wrong-file-preferred behaviour, and the `read_from` trap in
  place.

**Recommendation: A, and C as a separate follow-up.** A is the defect; it is small
and local and restores a guarantee the code already documents. C is worth having
anyway and would have surfaced this in a day rather than by inspection, but it
should not be mistaken for the repair. B is the cleaner architecture and the wrong
size for this bug — propose it separately if the collector is being touched for
other reasons.

Whichever is taken, decide explicitly what happens to orphans that already exist.
Deleting a file under `data/` from code is not something this repository does
anywhere else, so the safe answer is probably to report them and let a person
remove them.

---

## Tests

`tests/` has no coverage of the local-PDF-meets-existing-record path at all; the
existing PDF tests exercise a fresh hand-filed paper, which never merges. Add:

1. **The merge preserves the document.** Store a paper with an arXiv id and no
   `local_path`; ingest a PDF whose filename normalises to the same title; assert
   the merged record's `local_path` points at the ingested file, and that
   `data/pdfs/` contains exactly one PDF for that paper.
2. **`pdf_fetch` does not download for a merged hand-filed paper.** Same setup
   with a fake HTTP client that raises if called; assert no request is made and
   `counts["fetched"] == 0`.
3. **The stored path wins when both exist.** A record already pointing at
   `data/pdfs/read/<id>.pdf` must not have its path overwritten by a newly
   ingested duplicate — this is the case that would strand a shelved document.
4. **Regression on identity.** Dropping the same PDF twice under two names still
   produces one record (`local_pdf.py`'s content-addressed id), and now also one
   file.

`tests/sandbox.py` builds the fixture archive these should run against.

---

## What a reviewer should check

- `pdf_fetch.py:84` and its comment agree after the change. Today the comment
  describes behaviour the code does not have on this path, which is the clearest
  single symptom.
- No path can prefer a downloaded copy over a filed one. That is the actual
  defect; a fix that merely stops the orphan while still re-downloading has not
  fixed it.
- The `read_from` contract is exercised end to end: file a PDF for a known paper,
  render, and confirm the queued task carries `attachments.pdf_path`, so a reader
  who opened the document can honestly record `document`. That is the consequence
  that reaches the archive's evidence tiers, and it is why this is a fix rather
  than a tidy-up.
- `python3 -m pipelines.migrate status` reports the same `irreplaceable` count
  before and after ingesting a PDF for a paper that already has one.

## Notes for whoever picks this up

- The two orphans that prompted this are still on disk in the archive where it was
  found, deliberately left rather than deleted by hand.
- Related, and already solved:
  [`../solved/related-links-are-asked-for-and-discarded.md`](../solved/related-links-are-asked-for-and-discarded.md).
  Both are the same shape — a field that one half of the pipeline sets and another
  half silently drops — and both were invisible because every step reported
  success. That one was fixed by giving the authored value its own field with its
  own lifetime (`related_authored`, note
  [0045](../commit/0045-a-ruled-link-is-not-derived-away.md)); this one does not
  need a second field, because `local_path` has only ever had one writer and the
  merge simply forgets it.
- The finding is recorded on the archive side as `finding:9158ccf5f73fc5b8` in
  `wiki/findings.md`, established 2026-08-12.

---

## Resolution

**Option A, as recommended.** `merge_papers` takes the incoming `local_path` when
the stored record has none, and keeps the stored one when it has. Commit
`fix(enrich): a merge keeps the document the incoming record brought`, note
[0047](../commit/0047-a-filed-document-survives-its-merge.md).

The decisions this document asked for:

- **The stored path wins**, written as an explicit condition rather than the
  richness rule the rest of `merge_papers` uses — as the document warned. A
  stored path may already have been shelved into `data/pdfs/read/`, and taking
  the newcomer's would point the record at a name that is no longer there.
- **Existing orphans are not deleted.** Nothing here removes a file under `data/`
  from code and this did not start. They are inert, and they inflate the
  `irreplaceable` tier of a migration bundle, which is a cost worth stating
  rather than a corruption.
- **Option C was split out**, not dropped:
  [`an-orphaned-pdf-is-reported-by-nothing.md`](an-orphaned-pdf-is-reported-by-nothing.md).
  It is the thing that would have found this in a day rather than by inspection.
- **Option B was not taken.** It is the better architecture and the wrong size
  for this defect; it is recorded in the note as the thing to do if
  `collect/local_pdf.py` is opened for other reasons.

`tests/test_filed_pdf_merge.py` covers the path, which had none. Both directions
of the rule were checked against a deliberate mutation: removing the branch fails
the survival test, widening it to `if incoming.local_path:` fails the
stored-wins test. The test asserting that the record still reads as hand-filed is
kept beside them on purpose — `source` merging while `local_path` did not is what
made this look survivable.
