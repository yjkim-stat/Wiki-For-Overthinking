# 0038 — One folder per task, and its harness

| | |
| --- | --- |
| **Commit** | `docs: a workflows/ folder, one per task, each with its harness` |
| **Scope** | `workflows/`, `CLAUDE.md`, `README.md` |
| **Kind** | docs |

## What changed

`workflows/`, five folders and nine files: knowledge-and-wiki, commit-and-push,
migration, schedule, development. Each holds the ordered commands and — the part
that is not written down anywhere else — the **harness**: what checks each step,
what failure looks like, and where nothing is checking at all.

`workflows/schedule/` is new material rather than reorganised material. Nothing
in this repository described how a scheduled run differs from a manual one, and
the rule that matters most — push before you read anything — existed only inside
a Routine prompt stored on somebody's account.

## Why it is built this way

**The existing docs are organised by audience; this one is organised by task.**
`README.md` is for somebody deciding whether to deploy the repository.
`CLAUDE.md` is the contract. `docs/commit/` is why each decision was taken.
`docs/API.html` is a reference for one subsystem. None of them answers "I am
about to do X — what is the sequence, and what will tell me if I got it wrong?"

**"Harness" is the reason the folder earns its place.** A procedure is mostly
already written somewhere. What is nowhere is the inventory of guards: which
validator rejects, which test fails, which report you have to read yourself, and
— stated explicitly in every `harness.md` — **what nothing checks**. That last
section is the one worth having. An unchecked step you know about is safer than
one you assume is covered, and the list is uncomfortable to write, which is a
sign it is the useful part:

> The validator checks shape, not fidelity. A confident, plausible, invented
> `results` field passes everything.

**Every file names who is authoritative, and links rather than copies.** This
repository has already lost a document to duplication: `docs/API.html` described
`data/abstracts/` as committed while another session was gitignoring it, and was
wrong the day it was written. Five places saying the same thing means four of
them are wrong eventually. So `workflows/migration/README.md` does not restate
the migration procedure — that lives in `migration/README.md`, where the
freshly-cloned environment can reach it — and says so in its first line.

**A disagreement is a bug in the workflow file, not in the authority.** Stated
in `workflows/README.md` so that whoever finds one knows which side to fix.

## Trade-offs and rejected alternatives

**Nine more files to keep current, in a repository that has demonstrated it
cannot keep four in sync.** That is the real cost and the mitigation is
structural rather than diligent: the workflow files carry commands and guards,
both of which fail visibly when they drift — a renamed command produces an
error, a deleted test produces a missing name. Prose restating a rule would rot
silently, so there is deliberately very little of it.

**Rejected: `docs/workflows/`.** These are things you *do*, and `docs/` in this
repository has come to mean things you *read for reference*. Top level, next to
`migration/`, which is the same kind of thing.

**Rejected: folding the harness into each procedure file.** They have different
readers. The procedure is read while working; the harness is read when something
looks wrong, or when deciding whether a change is safe. Splitting them keeps the
procedure short enough to follow.

**Rejected: pinning the current Routine inventory into `workflows/schedule/`.**
Trigger ids and cron times belong to one account, and this repository is
deployed into others. The page describes the mechanism and the two properties
that are not obvious — that an agent can only modify a Routine it created, and
that the prompt lives outside the repository so a change here does not reach it
— and leaves the inventory where it lives.

## What a reviewer should check

- **Every relative link resolves, including anchors.** Checked programmatically
  across all nine files; zero broken at the time of writing. Re-run it after any
  rename.
- **The numbers are real.** 403 tests, and the per-file counts in
  `knowledge-and-wiki/harness.md` were measured, not estimated. The
  index-versus-files check in `commit-and-push/harness.md` was run: 38 and 38.
- **The claims about what is *not* checked.** Those are the load-bearing ones
  and the easiest to get wrong by optimism. `grep -rlE "\.save_(paper|video|
  concept|finding|abstracts|transcript)" pipelines/publish/` returning nothing
  is the one that backs the layering claim.
- **That `workflows/schedule/` matches how the deployment is actually wired.**
  It is the only page describing something outside this repository, so it is the
  one that can drift without any local change.

## Downstream impact

Documentation only. No code, no records, nothing regenerated.

A deployment gains `workflows/` on the next pull. The `schedule/` page assumes
the Routine-driven arrangement this family uses; a deployment driven by cron or
CI should replace that file rather than read around it.
