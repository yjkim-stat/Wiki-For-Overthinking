# 0008 — The layout table in `CLAUDE.md`, rewritten as write permissions

| | |
| --- | --- |
| **Commit** | `docs: turn the CLAUDE.md layout into a write-permission table` |
| **Scope** | `CLAUDE.md` |
| **Kind** | docs |

## What changed

`CLAUDE.md`'s eight-row "what it is" table becomes a fourteen-row table with a
**Write?** column, covering the paths an agent actually touches — the four
record directories under `data/`, the queue, the index, the ignored trees, the
three generated trees, the inbox, both config files, the code, the templates,
the scripts and tests, and `docs/commit/`.

The first rule also gains one clause: under `archive/`, edits are now *deleted*
rather than merely overwritten, because [0005](0005-rebuild-archive-from-scratch.md)
made a rebuild clear the tree first.

## Why it is built this way

**`CLAUDE.md` is a contract, not a tour.** The README's map answers "where do I
look?" for a person arriving at the repository. An agent about to act has a
different question — "may I write here, and what happens if I do" — and the
old table did not answer it. Two documents, two questions, one link between
them; the README section is referenced rather than repeated.

**The permission is the first column because it is the first thing needed.**
Reading a row to the end to discover that a directory is generated is one step
too late. `never` and `required` are the only two values in bold, because they
are the two that cause damage when missed.

**Every row states the consequence, not just the status.** "Generated" is a
category; "rewritten from `data/` on every render, and now cleared first, so an
edit here is deleted" is a reason. The rules section of this file already works
that way, and a table that did not would read as the softer, ignorable version
of the same information.

**The rows are more granular than the tree.** `data/` as a single row was
accurate and useless: its subdirectories have four different permissions —
pipeline-only records, a queue answered through a CLI, an index that is never
touched, and ignored scratch space. That distinction is the whole reason an
agent misfiles something.

## Trade-offs and rejected alternatives

- *Leaving the short table and relying on the Rules section.* Rejected: the
  rules cover the prohibitions but say nothing about the directories where
  writing is expected, so the absence of a rule reads as permission.
- *Copying the README's tree into `CLAUDE.md`.* Rejected outright — two copies
  of one tree is how the two documents start disagreeing, and the tree does not
  answer the question this file exists to answer.
- The table is now long enough to skim past. Accepted: it is a reference
  consulted mid-task, not prose read top to bottom, and the alternative is
  splitting one lookup across two places.

## What a reviewer should check

- That the **Write?** column agrees with the Rules section above it. If they
  ever disagree, the rules win and the table is the bug.
- That `wiki/` says "after `<!-- auto:end -->`" and not simply "yes". That
  single row is the difference between preserved analysis and lost analysis.
- The README link anchor still resolves: `README.md#where-things-live`.

## Downstream impact

None. Documentation only — though a deployment that has customised `CLAUDE.md`
will want to carry the `data/` granularity across, since the four
subdirectories genuinely differ.
