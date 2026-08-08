# Commit notes

One note per commit, in commit order. Each explains what changed, why it is
built that way, what it costs, and what a reviewer should check.

This repository is meant to be deployed into other projects. These notes are
how someone decides what to keep and what to replace without having to
reconstruct the reasoning from the code.

The practice is enforced by the `commit-notes` skill in
[`.claude/skills/commit-notes/`](../../.claude/skills/commit-notes/SKILL.md):
before any commit, the pending work is split into commits that each carry one
idea, and each gets a note here, staged in the same commit. Routine archive
digest commits are exempt — they change data, not the system.

Note 0000 is the exception to "one note per commit": it is a retroactive
reference for everything built before the practice existed.

## Index

| # | Note | Kind | What it establishes |
| --- | --- | --- | --- |
| 0000 | [Baseline: the pipeline as inherited](0000-baseline-the-inherited-pipeline.md) | reference | The load-bearing decisions of the original system, written down after the fact |
| 0001 | [Adopt the commit-note practice](0001-adopt-commit-notes.md) | chore | No change to the system lands without a note |
| 0002 | [Retire the subject-specific defaults and identifiers](0002-field-neutral-defaults.md) | refactor | Defaults are what people run; none of them name a field any more |
| 0003 | [Field-neutral fixtures and examples](0003-field-neutral-fixtures.md) | refactor | A test should be readable by someone who does not know the field |
| 0004 | [Reframe as a recipe for research team management](0004-reframe-as-a-team-recipe.md) | docs | The repository states the job it does, not the subject it was first used on |
| 0005 | [Make `rebuild_archive` actually rebuild](0005-rebuild-archive-from-scratch.md) | fix | `archive/` really is a pure function of `data/`, stale pages and all |
| 0006 | [Hand-filed PDFs](0006-hand-filed-pdfs.md) | feature | A person is a source too: drop a PDF in `inbox/` and it becomes an ordinary paper |
