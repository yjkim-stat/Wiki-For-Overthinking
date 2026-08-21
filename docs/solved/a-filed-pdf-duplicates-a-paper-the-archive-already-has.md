# A filed PDF duplicates a paper the archive already has

**Status:** solved 2026-08-21 by **option D** — see [Resolution](#resolution) at the
foot of this file and [note 0059](../commit/0059-an-identifier-learned-late-is-still-registered.md).
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

## Measured, 2026-08-20 — the exposure is 17 records, not 2

The deployment where this was found now holds **23 `local:` paper records, 22 of
which carry an `arxiv_id`**. Reading `data/index/seen.sqlite` directly:
**17 of those 22 have no `arxiv:<id>` key in the index.** Each is a duplicate the
moment the arXiv collector returns that paper.

```
arXiv:1604.06174  local:4b6b13e0da159f41  Training Deep Nets with Sublinear Memory Cost
arXiv:1712.05889  local:28b320c2aad1635a  Ray: A Distributed Framework for Emerging AI Applications
arXiv:2204.07143  local:174bd98b7aa889bf  Neighborhood Attention Transformer
arXiv:2309.06180  local:4fcaee68c325fe17  Efficient Memory Management ... with PagedAttention
arXiv:2309.14509  local:5d606eda0c329db9  DeepSpeed Ulysses
arXiv:2405.09818  local:17ec96e60712eac3  Chameleon
arXiv:2407.08608  local:367d6bc3d6d1f001  FlashAttention-3
arXiv:2407.11691  local:4eef9a9cfb44d8d3  VLMEvalKit
arXiv:2407.21770  local:0051a2c0d3e14568  MoMa
arXiv:2408.11039  local:7ed4ac3c6652d03a  Transfusion
arXiv:2410.06511  local:2a7ad248aa51f2d4  TorchTitan
arXiv:2411.04996  local:01fe9671afd4344c  Mixture-of-Transformers
arXiv:2504.15247  local:5226f0a5e94acb65  Lance
arXiv:2505.14683  local:0110f2c1a05dcc9c  Emerging Properties in Unified Multimodal Pretraining
arXiv:2509.21797  local:fec30a3d34ddb5a0  MoWM
arXiv:2602.02204  local:0d083b53a61a2f23  vLLM-Omni
arXiv:2602.15922  local:badf8adcf2b6a678  World Action Models are Zero-shot Policies
```

**Why the count is what it is.** `paper_keys` builds `arxiv:`, `doi:` and
`title:` keys, and `Deduplicator.resolve_paper` registers them at *collection*
time. `local_pdf` creates the record before anything opens the PDF — deliberately,
and for a good reason — so at that moment the only available key is
`title:<fingerprint of the filename>`. The identifier arrives at
`queue complete`, and **nothing re-registers the keys afterwards.**

That makes the two existing duplicates ordinary rather than unlucky: `wan.pdf`
fingerprinted as `wan`, and the Any2Any upload was missing its title prefix.
Filing with the full published title as the filename closes the *title* path and
is now the practice in that deployment — but it does nothing for the `arxiv:`
path, which is the one these 17 records are exposed on.

**This sharpens the recommendation.** Option A prevents the *next* one; it leaves
these 17 exposed. What closes them is small and local:

> **D. Re-register keys when a completed reading supplies an identifier the
> record did not have.** `apply` already writes `arxiv_id`, `doi` and the
> corrected `title` onto the stored record. Calling `seen.remember` for the keys
> that changed, at that point, costs one write per new key and makes a later
> arXiv collection fold instead of fork. It also repairs the existing exposure on
> the next render, without a sweep and without touching stored records.

Recorded in the deployment as `finding:0febb8a661019e87`.

---

## Resolution

**Option D, as the measurement sharpened it to.** `enrich/dedupe.reconcile_identifiers`
registers every identifier a stored record carries that nothing in the index
holds, and `render` runs it after applying readings. Commit
`fix(enrich): register an identifier a record gained after collection`, note
[0059](../commit/0059-an-identifier-learned-late-is-still-registered.md).

One adjustment to what this document proposed. Registering at *apply* time — the
literal reading of D — prevents the next duplicate and closes **none of the 17**,
because those readings were applied long ago and nothing re-runs them. So it is a
self-healing pass over the records instead, the same shape as
`render.shelve_documents`: it re-derives what should be registered from `data/`
on every render and needs nothing remembered. That covers both the backlog and
every future case, and makes apply-time registration unnecessary rather than
merely redundant.

- **A key another record already holds is reported, never repointed.** That is a
  duplicate which already exists, and choosing which of the two survives is a
  merge — the one decision this repository is most careful never to make quietly.
  `render` logs each conflicting pair and counts them in `identifiers.conflicts`.
- **The two known duplicates are not merged by this.** `arxiv:2503.20314` against
  `local:94a30c3706dd3819` will now be reported on every render until somebody
  decides. That is the intended outcome: the reading is on the `local:` record
  and the collection metadata on the arXiv one, so the merge is a judgement about
  which fields survive.
- **It writes no record**, only `data/index/seen.sqlite`, and is idempotent — the
  second run of a pass registers nothing.

The 17 close on the first render after this lands.
