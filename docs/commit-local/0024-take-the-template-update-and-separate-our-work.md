# 0024 — Take the template update, and put our work somewhere it survives the next one

| | |
| --- | --- |
| **Commit** | `feat: adopt the src template update and split local work into pipelines/local` |
| **Scope** | `pipelines/`, `tests/`, `config/sources.yaml`, `CLAUDE.md`, `docs/` |
| **Kind** | feature · refactor · **breaking layout** |

## What changed

The `src` remote — the upstream template — moved 24 commits. All of it is now
here, and this deployment's own work has been moved out of the template files
into `pipelines/local/` so the next update does not have to negotiate with it.

New from the template: arXiv listing-page collection when the API is
unavailable, venue programme-page collection from the conference virtual sites,
PDF fetching so a reader gets the document rather than a claim about it, a
coverage ledger that records what arXiv says it announced, `queue reopen`,
staleness reporting, and shared HTML reading. 29 files that did not exist here,
plus 7 the template changed and we had never touched.

New from us: `pipelines/local/` holding the placeholder validator, the abstract
backfill and the definition-queue reserve; `docs/LOCAL-DELTAS.md` listing what
could not be moved; `tests/test_local.py`; and `docs/commit-local/` for these
notes.

## Why `git pull` was never an option

The two repositories have **no commit in common** — 33 commits on `src/main`
against 32 here, two independent histories. `git pull` refuses, and
`--allow-unrelated-histories` would merge two unrelated trees: 2,169 files exist
only here, being the entire archive, the wiki, the outputs and the topic
definitions.

So an update is applied path by path. That is not a workaround; it is what the
relationship is. The template is a starting point that keeps improving, not a
branch we diverged from.

## Why it is built this way

**The template wins, and that had to be made cheap rather than painful.** The
instruction was that `src` takes priority in a conflict. Taken literally on a
per-file basis it would have deleted working code this deployment depends on —
the `models` field plumbing, the placeholder validator, the definition-queue
reserve, the DBLP abstract backfill, none of which exist upstream. Moving those
into their own package is what lets both things be true: a template file can be
replaced wholesale, and nothing of ours goes with it.

**One-line call sites, not clever indirection.** The template has no plugin
system and inventing one would be a larger change than the thing being
protected. So `validate_result` gains one `errors.extend(placeholders.check(...))`
and `collect()` gains one `local_abstracts.fill_missing(...)`. The next update
has to re-check three lines instead of three functions.

**The `model` kind stayed in the template files, and the note says why.** It is
a schema change — a fourth entity kind touches the record, the harvest, the
validator, the applier, the reader's output contract and the directory layout at
once. There is no seam to hide that behind. Pretending otherwise would have
produced a `local/` package that reaches into template internals, which is worse
than an honest marked delta. It is marked `# LOCAL` at every site and tabulated
in `docs/LOCAL-DELTAS.md`, and `grep -rn "LOCAL" pipelines/ --include=*.py`
finds all of them.

**Our commit notes kept their numbers.** Both histories number from 0000 and
both reached 0009 with different content, so the directory had to split. Within
`docs/commit-local/` the numbers are unchanged — 0018 corrects 0014 and 0014
carries the matching correction section, and the rule that a pushed note is
never rewritten outranks a tidy sequence starting at 0001.

**Our own regex gave way to theirs.** The abstract backfill parsed the ACL
Anthology page with a hand-rolled pattern. The template now ships
`common/html.py` with `abstract_block()`, which does the same job for every
collector, so the local module calls that and strips only the heading label the
Anthology leaves attached.

## Trade-offs and rejected alternatives

- *Keeping our changes in the template files and merging per-file each update.*
  Rejected: that is the situation this update was painful because of. The cost
  is paid once here and avoided every time after.
- *A patch series applied over a pristine template tree.* Considered seriously.
  It keeps the template byte-identical, which is the strongest possible
  guarantee, and it makes the working tree not directly runnable and every edit
  a patch-refresh. Too high a tax for a repository whose whole point is that a
  reader can open it and work.
- *Dropping the `model` kind to match upstream exactly.* Rejected: 28 wiki notes
  and 71 summaries depend on it, and it was an editorial decision, not an
  accident.
- *Renumbering our notes from 0001.* Rejected above — it breaks the
  cross-references.
- *Splitting this into three commits — move the notes, take the update, add the
  local package.* Rejected, and worth saying why since the rule is one idea per
  commit: taking the update alone leaves a tree with our features deleted and
  the suite red, so a reviewer cannot accept or reject the middle commit on its
  own. The three steps are one decision.
- *Taking the template's venue list.* Rejected: theirs is AISTATS and JMLR, ours
  is the ACL family. But their `virtual_host` fields were adopted, which is what
  lets the new programme-page collector see ICML, ICLR and NeurIPS at all.

## What a reviewer should check

- `python3 -m unittest discover -s tests -t .` — 337 tests, of which 24 are
  `tests/test_local.py`. That file is the tripwire: it is what fails if a future
  template update overwrites a delta.
- `python3 -m pipelines.render` against the real archive, which is the check the
  sandboxed suite cannot make. It should report 126 papers and 198 wiki notes,
  unchanged, and now also `stale: {definitions: 83}` from the template's new
  reporting.
- `git diff --name-only src/main -- pipelines/ | grep -v pipelines/local` should
  list exactly the six files in the LOCAL-DELTAS table plus `conferences.py`.
  Anything else has drifted.
- That `config/sources.yaml` kept all four local edits — arXiv categories,
  OpenReview off, the venue list, the `abstracts` block — while gaining the
  template's `arxiv.listing` and `conferences.virtual_site`.

## Downstream impact

**The layout changed and `CLAUDE.md` now says so.** New work goes in
`pipelines/local/`, new notes in `docs/commit-local/`. `docs/commit/` is the
template's and must not be added to.

Collection behaviour changes materially, all from the template: arXiv falls back
to listing pages when the API is unavailable — which is the failure this host
already has — the conference virtual sites are read for the first time, and each
paper that clears scoring gets its PDF fetched before it is queued. Runs will be
slower and the reader will be handed documents rather than abstracts. The new
`data/abstracts/` directory is gitignored by the template on purpose; the
coverage ledger beside it is not.

`config/settings.yaml` gained the template's new blocks unchanged, having never
been customised here.
