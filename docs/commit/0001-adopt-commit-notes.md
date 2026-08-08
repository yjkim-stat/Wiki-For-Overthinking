# 0001 — Adopt the commit-note practice

| | |
| --- | --- |
| **Commit** | `chore: adopt the commit-note practice` |
| **Scope** | `.claude/skills/commit-notes/`, `docs/commit/` |
| **Kind** | chore |

## What changed

From here on, no change to this repository lands without a note in
`docs/commit/`, staged in the same commit that it explains. The practice is
carried by three things:

- `.claude/skills/commit-notes/SKILL.md` — the procedure and the note template,
  written to be executable by someone who has never seen this repository.
- `docs/commit/README.md` — the index, which is the only thing anyone skims
  before deciding which note to open.
- `docs/commit/0000-baseline-the-inherited-pipeline.md` — a retroactive note
  covering the pipeline as it stood before this practice existed.

## Why it is built this way

**The history is the documentation, because this repository is a template.** It
gets copied into other projects, and the people who copy it read the log to
decide what to keep, what to rip out, and what a change was actually for. A
commit subject is one line and cannot carry a reason. A README describes the
destination rather than the route. `docs/commit/` carries the route.

**The note is written before the commit, and that is the useful part.** Filling
in "why it is built this way" and "trade-offs and rejected alternatives" for a
change that bundles three unrelated ideas is hard, and the difficulty is the
signal: it means the split is wrong. The template is a thinking tool first and
an artifact second.

**Split by idea, not by directory.** One commit is one decision a reviewer could
accept or reject on its own. A rename and the behaviour change it enables are
two commits; three unrelated typo fixes are one.

**The baseline note exists because a silent eight hundred lines cannot be safely
modified.** Rather than pretend the practice was always there, 0000 states the
inherited design and marks its rationale as reconstructed from the code.

## Trade-offs and rejected alternatives

- *A pre-commit hook that blocks unnoted commits.* Rejected for now: a hook that
  blocks is a hook people learn to bypass with `--no-verify`, and it would fire
  on the routine archive digest commits that legitimately need no note. The
  skill plus the rule in `CLAUDE.md` puts the practice where the work happens. A
  hook stays available if the practice slips.
- *Notes in the commit message body instead of files.* Rejected: messages are
  not linkable, not reviewable as a diff, and cannot be corrected later without
  rewriting history.
- *A `CONTRIBUTING.md`.* Rejected: it is read once. `CLAUDE.md` is read every
  session, and the skill loads in front of whoever is about to commit.
- *Retro-writing one note per historical commit.* Rejected: the history before
  this one is a single squashed baseline commit, so per-commit notes would be
  fiction. One baseline note is honest.

## What a reviewer should check

- `SKILL.md`: whether the procedure works for a small change. If a one-line fix
  produces a six-section note of filler, the template is too heavy and should be
  cut, not ignored.
- `docs/commit/README.md`: every row should describe what the commit
  *establishes*, not what it touched.

## Downstream impact

A project deploying this repository inherits the skill and the rule. If it has
its own commit conventions, delete `.claude/skills/commit-notes/` and
`docs/commit/` — nothing in the pipeline reads either. Note that the skill is
discovered only when this repository is itself the project root; deployed as a
subdirectory, it will not load.
