# 0039 — A URL the identifier already implies

| | |
| --- | --- |
| **Commit** | `fix(backfill): an arXiv paper that names no PDF still says where its document is` |
| **Scope** | `pipelines/backfill.py`, `tests/test_backfill.py` |
| **Kind** | fix |

## What changed

`backfill` counted a waiting paper with an empty `pdf_url` as one nothing can
reach. When that paper's canonical id is an arXiv id, it now derives
`https://arxiv.org/pdf/<id>` from the id, sets it on the record, and fetches.

## Why it is built this way

**A bibliographic index does not carry documents.** A paper that reaches the
archive through Semantic Scholar or DBLP arrives with that index's landing page
in `url` and, routinely, nothing in `pdf_url` — Semantic Scholar returns
`openAccessPdf` only when it has one. The record still carries the paper's own
arXiv id, because dedup resolved it there. So the archive held a record that
said, in one field, exactly where its document lives, and in another field that
it had none.

**The consequence was permanent, which is why this is worth a fix rather than a
manual fetch.** `pdf_fetch` runs inside collection and only sees papers arriving
that run. Collection will not revisit this paper because `seen.sqlite` remembers
it. `backfill` is the second chance, and it declined. Nothing else fetches. The
reading would have been made from an abstract for good — and this paper's
abstract contains no numbers at all, only "substantially reducing token
consumption and execution time", so the contribution could not have been
established from it.

**Derivation is confined to arXiv.** It is the one identifier scheme in this
archive whose document location is fixed by the identifier rather than
negotiated per publisher: `doi:` resolves through a registry to a page that may
be a paywall, and `local:` and `title:` name no external document at all. A
guess for those would produce failed fetches, and a failed fetch is
indistinguishable in the record from a host being down.

**The derived URL is written to the record, not merely used.** Otherwise every
later run rediscovers it, and the record never says where the document it holds
came from.

**A URL the record already names is never overwritten.** A publisher's own link
outranks a guess from the identifier, even when both point at arXiv.

## Trade-offs and rejected alternatives

**Rejected: deriving at collection time instead.** The collectors that produce
these records are the ones that do not know the document URL; the place that
knows the id has already been resolved is dedup, and putting a network-facing
guess there would mean writing a URL nobody has tried. `backfill` both derives
and immediately tests the guess.

**Rejected: filing a lookup asking where the document is.** That is the right
answer for a `doi:` record and the wrong one here — it asks a person to look up
something the archive can compute.

**Accepted cost: `no_pdf_url` will now report a smaller number**, and a
deployment that was using it as a worklist for lookups will find arXiv records
have left it. That is the intent.

## What a reviewer should check

- Two existing tests encoded the old behaviour by building an unreachable paper
  from an arXiv id with an empty `pdf_url`; both now use a `doi:` id, because an
  arXiv one is no longer unreachable. That is the change, seen from the tests.
- `tests/test_backfill.py` — five new cases: an arXiv record with no URL becomes
  a candidate, the derived URL is persisted, an existing URL wins, a version
  suffix is stripped (`2401.00009v3` → `.../2401.00009`), and nothing is derived
  for `doi:`, `local:`, `title:`, `""` or a bare `arxiv:`.
- `python3 -m unittest discover -s tests -t .` — 852 tests, green.
- On this archive: `arxiv:2607.25825` arrived from Semantic Scholar under
  `cs.MA` with `pdf_url: ''` and was reported as unreachable. After this change
  `backfill --limit 3` fetched it, `render` attached it to the waiting task, and
  the reading was made from the document.

## Downstream impact

Any deployment collecting from Semantic Scholar or DBLP may have arXiv papers
sitting in `no_pdf_url`. Running `python3 -m pipelines.backfill --dry-run` after
taking this change will show them as candidates. Nothing has to be re-collected
and no record is rewritten until its document is actually fetched.
