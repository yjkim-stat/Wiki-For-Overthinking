# 0047 — A filed document survives its merge

| | |
| --- | --- |
| **Commit** | `fix(enrich): a merge keeps the document the incoming record brought` |
| **Scope** | `pipelines/enrich/dedupe.py`, `tests/test_filed_pdf_merge.py`, `docs/issues/`, `docs/solved/` |
| **Kind** | fix |

## What changed

`merge_papers` folds an incoming paper into the stored one field by field, and
`local_path` was not in the list. Filing a PDF for a paper the archive already
held therefore produced a merged record with no document — and the pipeline then
downloaded the same paper from the internet and left the person's file on disk
under a name no record points at.

Three lines: the incoming path is taken when the stored record has none.

## Why it is built this way

**The stored path wins where both exist, and the rule is written out rather than
derived.** Every other field in `merge_papers` is merged on richness — the longer
abstract, the longer venue string. There is no longer path, and the two values
are not two descriptions of one thing; they are two files. The stored one may
already have been shelved into `data/pdfs/read/` by `render.shelve_documents`,
which rewrites the record to match, so preferring the newcomer would point a
record at a name that is no longer there.

**This restores a guarantee the code already documents.** `pdf_fetch`'s guard
reads `if paper.local_path: continue` under the comment *"A hand-filed PDF is
already on disk, and its file is the original."* The comment was right and the
condition tested the field that had just been dropped, so the branch never fired.
Nothing had to be added to `pdf_fetch`; the field it asks about now survives to
be asked.

**What made it survivable-looking is what makes it worth a note.** `source` *is*
merged, so the record came back reading `arxiv+local` and `Paper.is_local`
returned true. The archive stated that it held a hand-filed paper and could not
state where the file was, which is the shape of every defect this repository has
found: complete-looking, internally consistent, and wrong in the one field
nobody reads.

**The cost is asymmetric, which is why this was taken before the feature work it
was found under.** `migration/README.md` files hand-filed PDFs as
`irreplaceable` — *"Gone permanently. Somebody chose these and put them in the
inbox; no URL was ever recorded."* An orphan is not a wasted download; it is the
one class of file the migration bundle exists to carry, sitting where the bundle
cannot see it.

## Trade-offs and rejected alternatives

**Orphans that already exist are not cleaned up.** Nothing in this repository
deletes a file under `data/` from code, and this change does not start. They are
inert — a duplicate of a document the record already has, or of one it can
re-fetch — and they inflate the `irreplaceable` tier of a migration bundle,
because `migrate.build_plan` cannot establish provenance for a file no record
claims and correctly refuses to treat unknown as disposable.

**Considered: option B from the issue — stage the ingested file and move it once
the record resolves.** Then no duplicate is ever written and the file is named
for the record that owns it. It is the better architecture and the wrong size for
this defect: it inverts `collect/local_pdf.py`, which moves-then-returns and
knows nothing about deduplication, and it would couple `collect/` to `enrich/`.

**Considered: option C — report orphans from `migrate status`.** Worth having and
not a fix. Filed separately as
`docs/issues/an-orphaned-pdf-is-reported-by-nothing.md`,
because it is the thing that would have surfaced this in a day rather than by
inspection, and it stays true for orphans arising any other way.

**The merged record keeps a filename derived from the discarded local id** — a
path like `data/pdfs/local-abc123.pdf` on a record whose id is now `arxiv:…`. It
resolves, shelving moves it by name, and nothing reads meaning out of it. Renaming
it would be option B's job.

## What a reviewer should check

- Both directions, in `tests/test_filed_pdf_merge.py`. Deleting the branch fails
  `test_a_filed_document_survives_the_merge`; widening it to `if
  incoming.local_path:` fails `test_a_stored_document_is_not_replaced`. A fix that
  only carries the field has half the rule.
- `test_a_merged_hand_filed_paper_is_not_fetched` uses a client that raises on any
  request, so the assertion is that no HTTP call happens at all rather than that a
  counter stayed at zero.
- That `test_the_record_still_reads_as_hand_filed` stays beside the others. The
  `source`-merges-but-`local_path`-did-not asymmetry is the reason this looked
  fine; asserting the half that always worked keeps the pair from drifting apart
  again.
- `tests/` had **no** coverage of the local-PDF-meets-existing-record path before
  this. The existing PDF tests exercise a freshly filed paper, which never merges.

## Downstream impact

**Deployments that filed a PDF for a paper they already held have orphans in
`data/pdfs/`.** They are safe to delete once you have checked the record's own
`local_path` points at a file that exists; nothing automatic will do it. On the
archive where this was found, the `irreplaceable` tier went from 7 files /
169.5 MB to 11 / 235.5 MB across one run, 34.5 MB of it exact duplicates.

No record is rewritten by this change, and no re-render is needed. The next merge
of a hand-filed paper keeps its document.
