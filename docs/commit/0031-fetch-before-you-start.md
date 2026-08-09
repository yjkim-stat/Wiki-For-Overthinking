# 0031 — Fetch before you start

| | |
| --- | --- |
| **Commit** | `docs: start the routine by fetching origin/main` |
| **Scope** | `CLAUDE.md` |
| **Kind** | docs |

## What changed

`CLAUDE.md`'s daily routine gains a step 0: `git fetch origin main`, and a check
for whether the session is behind. The commit-note rule now says to pick the
note number against a fetched `origin/main` rather than against the local
checkout.

## Why it is built this way

**More than one session commits to this repository, and a long-lived container
does not notice.** The environment clones fresh at start, which makes staleness
easy to forget — but a session that has been alive for hours is holding whatever
`main` looked like when it began.

The two failure modes are named explicitly because both are quiet, and both
happened here:

- **A duplicate commit-note number.** Numbers are chosen by reading
  `docs/commit/`, so two sessions reading a stale directory both pick `NNNN`.
  Nothing detects it until a merge, and the fix is renumbering a note that has
  already been written and reasoned about.
- **Work built on a reversed decision.** A change landed upstream can invert an
  assumption the current work depends on, and the code cannot say so. In this
  repository a session documented `data/abstracts/` as committed while another
  had already gitignored it — the page was wrong the day it was written.

**Step 0 rather than a rule.** Rules are read once; the routine is read every
time a session starts. This belongs where somebody is already looking, at the
moment it applies.

**It says to rebase, not merge.** The history here is linear and reads as
documentation, and a merge commit in the middle of a sequence of one-idea
commits is noise in the thing the repository is for.

## Trade-offs and rejected alternatives

**Rejected: a git hook, or a check in `scripts/daily.sh`.** A hook would catch
the commit but not the hours of work already built on a stale base, which is the
expensive half. The cheap moment to notice is before the first edit, and nothing
mechanical runs then.

**Rejected: fetching inside `run_daily`.** Collection is a pipeline stage; git
state is not its business, and a collector that quietly moved the checkout would
be worse than a stale one.

**Cost: it is guidance, not enforcement.** A session that skips step 0 gets the
same collisions. The alternative — automating it — has no natural place to hang,
as above.

## What a reviewer should check

That the instruction is actionable as written: the second command prints
nothing when up to date, and prints the missing commits when behind. That is the
whole check, and it needs no interpretation.

## Downstream impact

None to the pipeline. It changes how a session starts, not what the code does.
