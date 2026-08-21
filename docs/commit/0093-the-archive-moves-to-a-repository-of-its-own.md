# 0093 — The archive moves to a repository of its own

| | |
| --- | --- |
| **Commit** | `chore: the archive moves to a repository of its own` |
| **Scope** | `data/`, `wiki/`, `archive/`, `outputs/` — removed; `docs/daily-routine.md` |
| **Kind** | chore · breaking |

## What changed

This repository is the code root and nothing else. The archive — 269 papers,
2,907 wiki entities, 571 notes, 851 completed readings, 24 findings — now lives
in `Recipe-for-Reasoning-of-LLM`, and this checkout is run against it:

```bash
export RA_WM_ROOT=/path/to/archive
python3 -m pipelines.migrate status     # confirm before anything else
```

`config/` stays here as the shipped example, because there is no fallback for
it the way there is for `templates/`: `config.load` reads `<root>/config` and a
tree without one cannot start. The deployment has its own copy, which is where
its editorial decisions live.

## This reverses [0076](0076-the-archive-this-repository-keeps.md), and the reason it does

Note 0076 argued for keeping both halves in one tree: the container is
ephemeral, so a scheduled run starts from a fresh clone, and committing `data/`
is what lets it. That argument still holds — and it is satisfied either way,
because the archive repository is also cloned and also commits its `data/`.

What changed is that there are now two repositories being *developed*, not one
repository being deployed. `origin` for this tree advances the program; the
archive advances by reading. Four times in eight days a session here has had to
renumber `docs/commit/` because upstream moved underneath it, and every one of
those merges also had to be careful not to disturb a day of readings sitting in
the same working tree. The two rhythms do not belong in one history.

The decision is the user's and is recorded rather than argued: the routine is to
run against the reasoning archive, and that archive is where the reading
accumulates.

## What was verified before anything was deleted

In this order, and the order is the point — nothing was removed from here until
the other tree had been proved to work:

1. Every record copied and compared by name: `data/papers` 269 = 269,
   `data/concepts` 2,908 = 2,908, `data/summaries/papers` 269 = 269,
   `data/findings` 24 = 24, with **zero** files on either side the other lacked.
2. Two classes of stale record dropped rather than carried: 30 concept records
   this archive had already retired through the alias map — the harvest would
   resurrect them — and 37 pending queue tasks for papers since read.
3. `migrate status` resolving both roots, with `documents: 180 record(s) claim
   one, 0 missing on disk`.
4. A full render from this checkout against the other tree, reproducing 269
   papers, 2,907 entities and 571 notes with `stale` at `{definitions: 0,
   analysis: 0}` — **and leaving this checkout with nothing to commit**, which
   is the check `workflows/deployment/harness.md` says nothing performs
   automatically.
5. Both pushed, before the deletion here.

Afterwards, 94 documents in the deployment's `data/pdfs/` were found to be
byte-identical duplicates of files already under `data/pdfs/read/` — leftovers
from the older tree, which would have read as a 94-paper backlog that does not
exist. All 94 were compared byte for byte before removal, and `migrate status`
now reports no orphan.

## What a reviewer should check

- `python3 -m pipelines.render` **in place** on this checkout succeeds against
  an empty archive: `entities: 0, notes: 0, stale: {definitions: 0, analysis: 0}`.
  That is the fresh-clone case and it must keep working.
- `git ls-files data wiki archive outputs` is empty here.
- The suite is unaffected: it sandboxes, and never touched the real `data/`.
- `docs/daily-routine.md` names the archive repository, and the three things
  that must be settled in the same call that re-enables the routine.
