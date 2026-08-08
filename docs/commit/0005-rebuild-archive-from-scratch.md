# 0005 — Make `rebuild_archive` actually rebuild

| | |
| --- | --- |
| **Commit** | `fix(render): clear the archive before regenerating it` |
| **Scope** | `pipelines/render.py`, `tests/test_render.py` |
| **Kind** | fix |

## What changed

`rebuild_archive()` now removes `archive/papers/` and `archive/seminars/`
before writing them again. `archive/daily/` is left alone.

## Why it is built this way

**The invariant was false.** The repository's central claim — stated in the
README, in `CLAUDE.md`, in the baseline note — is that `archive/`, `wiki/` and
`outputs/` are derived: delete them, render, and they come back identical. For
the archive that was only true of the *contents* of a page, not of the set of
pages, because a paper's page path contains its year:

```
archive/papers/<year>/<id>/summary.md
```

A year can arrive after the page does. A deduplication merge fills one in from
proceedings; a record can be corrected by hand in `data/`. The page was then
written at the new path and the old one was never removed, leaving two pages for
one paper — both listed in the index, one of them permanently stale. Rendering
twice did not fix it, because nothing ever looked at the old path again.

**Clearing is the honest fix.** The alternative is to track which page belonged
to which record and delete the difference, which means keeping a manifest that
can itself drift. The whole point of a derived tree is that it can be thrown
away, so throwing it away is cheaper and cannot go stale.

**`archive/daily/` is exempt, and that is not an oversight.** A digest is a
dated record of what one run saw — written by `run_daily.py`, never regenerated
from the store, and not reconstructible after the fact. Clearing it would delete
the only copy. This is the one place in `archive/` that is a record rather than a
rendering, and the asymmetry is worth knowing about.

## Trade-offs and rejected alternatives

- *Deleting only the pages that moved.* Rejected: requires a manifest of
  previously-written paths, which is state that can disagree with reality —
  exactly the class of bug being fixed.
- *Clearing the whole of `archive/`.* Rejected: it would take the daily digests
  with it.
- The cost of this fix is that an interrupted render leaves the archive
  incomplete until the next one. That is acceptable for a derived tree, and the
  operation is local and fast.

## What a reviewer should check

- That `archive_daily` is not in the loop. Deleting it would be silent and
  unrecoverable.
- `test_rebuilding_does_not_touch_the_daily_digests` and
  `test_a_corrected_year_leaves_no_stale_page_behind` in `tests/test_render.py`
  pin both halves.
- `run_daily.py` still writes individual pages incrementally without clearing —
  it is not a rebuild, and clearing there would erase the archive on every run
  before the render restored it.

## Downstream impact

None visible, unless a deployment has been hand-editing files under
`archive/` — which `CLAUDE.md` forbids, and which now fails faster: such edits
were already overwritten on every render, and are now deleted outright.
