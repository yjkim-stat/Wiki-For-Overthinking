# A filed PDF duplicates a paper the archive already has

**Status:** open
**Found:** 2026-08-14, filing the Wan technical report into a deployment that had
already collected it from arXiv.

## What happens

Drop `wan.pdf` into `inbox/` for a paper the archive already holds as
`arxiv:2503.20314`. After `run_daily --source local`, the reading, and `render`,
there are **two paper records for one paper**:

```
data/papers/arxiv-2503-20314.json      id arxiv:2503.20314   (collected, no reading)
data/papers/local-94a30c3706dd3819.json id local:94a30c3706dd3819 (the reading)
```

Both carry the same `title`, both carry `arxiv_id: 2503.20314`, and both get a
`summary.md` under `archive/papers/2025/`. The wiki then lists the paper twice,
and every entity it feeds counts it twice.

Nothing errors. The run reports success at every step.

## Why

`pipelines/enrich/dedupe.py` resolves an incoming paper against stored records on
`paper_keys()`:

```python
def paper_keys(paper: Paper) -> list[str]:
    keys: list[str] = []
    if paper.arxiv_id:
        keys.append(f"arxiv:{strip_arxiv_version(paper.arxiv_id)}")
    if paper.doi:
        keys.append(f"doi:{paper.doi.strip().lower()}")
    if paper.title:
        keys.append(f"title:{title_fingerprint(paper.title)}")
    ...
```

That is correct and it fires at the right moment — `run_daily.py:269`,
`deduper.resolve_paper(paper)`, during collection.

The problem is what the local collector can supply at that moment.
`pipelines/collect/local_pdf.py` says so in its own docstring: *"Nothing here
opens the PDF. […] the collector records only what the filesystem can tell it,
and the task it files asks whoever answers it to read the document and supply the
bibliography."*

So at collection time the record has **no `arxiv_id`, no `doi`, and a `title`
taken from the filename**. For `wan.pdf` the title is `wan`, whose fingerprint
matches nothing. All three keys miss, a new record is created, and it is correct
to create one — the collector genuinely does not know.

The bibliography arrives later, through `queue complete`. At that point
`arxiv_id: 2503.20314` lands on the record and the key that would have matched now
exists. **Nothing re-runs the resolution.** `run_daily` only deduplicates papers
it is currently collecting, and the inbox is empty by then.

## Why it has not bitten before

The collector's title-from-filename is load-bearing and undocumented as such. A
PDF filed under its full title *does* merge, because `title_fingerprint` matches:

```
data/papers/arxiv-2607-00310.json
  local_path: data/pdfs/read/local-eff6f0b355d90294.pdf   ← merged correctly
```

That file was dropped in as
`RetailSMV, Exocentric vs. Egocentric Adaptation of Foundation Video World Models in Retail.pdf`.
The Wan one was shortened to `wan.pdf`. Same pipeline, opposite outcome, and the
only difference is a filename nobody was told mattered.

## What to change

The defect is that identity is resolved **once, before the identifying
information exists**, and never revisited when it arrives. Three options.

**Option A — re-resolve when a reading supplies identifiers.** In the queue's
paper-completion path, after the bibliography is applied, run `paper_keys()`
against the store; if it now matches a *different* stored record, fold the two
with the existing `merge_papers()` and repoint the document. This puts the fix
where the missing information actually arrives. It needs a rule for which id
survives — the arXiv one should, since it is the citable identity — and the
`local:` record's queue task is already `done`, so nothing needs replaying.

**Option B — a `dedupe` sweep over stored records.** A standalone pass that groups
stored papers by `paper_keys()` and merges collisions, run from `render` or by
hand. Catches this case and any other route to a duplicate, at the cost of
touching records outside the run that created them. Safer to ship as a
`--dry-run`-first command than to wire into `render`.

**Option C — make the collector's dependence on the filename explicit.** Have
`local_pdf` log the fingerprint it derived and warn when a filename looks
unlikely to be a title (very short, no spaces, a bare slug). Does not fix
anything, but it turns a silent duplicate into a visible one at the moment it is
created. Reasonable *alongside* A or B, not instead of them.

Recommendation: **A**, with **C** as a cheap guard. B is the more general fix but
it repairs damage rather than preventing it, and a sweep that merges stored
records is a bigger thing to get right.

## Repair for an archive already holding a duplicate

There is no supported command. `pipelines.migrate` carries records between
environments and does not merge them, and hand-editing `data/` is against the
deployment's own rules. Until A or B exists, the honest options are to leave the
duplicate and note it, or to have whoever owns the archive decide.

The affected pair in the deployment where this was found is
`arxiv:2503.20314` and `local:94a30c3706dd3819`, the Wan technical report. The
reading is on the `local:` record; the arXiv record has the richer collection
metadata (`categories`, `pdf_url`, `published`, `url`).
