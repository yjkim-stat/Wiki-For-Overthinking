# 0042 — Two roots, and the workflow that keeps them apart

| | |
| --- | --- |
| **Commit** | `docs: the archive can live in a repository of its own` |
| **Scope** | `CLAUDE.md`, `README.md`, `workflows/deployment/`, `workflows/README.md`, `docs/daily-routine.md`, `migration/README.md`, `workflows/*/harness.md` |
| **Kind** | docs |

## What changed

The documentation stated one premise — the code is replaced, the archive is not
— and then described a single tree in which both live. This says what the split
actually looks like when a deployment takes it.

- `CLAUDE.md` opens with **which tree is the archive in**, before the routine,
  because every rule after it divides along that line. Step 0 and step 4 say
  which repository they mean; the commit-note rule says it is the code
  repository's alone.
- `README.md` gains **Keeping the archive in a repository of its own**, with the
  reason stated as the files that collide rather than as a principle.
- `workflows/deployment/` is new: setting one up, updating the code underneath a
  running archive, and a harness whose first line is the command that says where
  you are.
- `migration/README.md` says which repository the new environment clones.
- `docs/daily-routine.md` gains the two symptoms of a mismatched root.

## Why it is built this way

The reason for splitting is written as a table of the specific files that
conflict — `seen.sqlite` being binary and unmergeable, the wiki graph being
regenerated every render, `config/` being both yours and ours — rather than as
an argument about separation of concerns. Somebody deciding whether to bother
can check each row against their own repository. An argument about concerns is
unfalsifiable and therefore unhelpful.

The deployment workflow says to record the code's commit in the archive
(`FRAMEWORK.txt`) and then says plainly that nothing enforces it. Both halves
matter: the record is the only link between the two repositories, and a reader
who thinks it is a lock will be surprised later. `harness.md` lists it under what
nothing checks for the same reason — a stale `FRAMEWORK.txt` is worse than an
absent one, because it reads as an answer.

`workflows/README.md` requires each workflow to name an authority and never
restate it. The deployment workflow's authority is the new `CLAUDE.md` section,
and the procedure links to it rather than repeating the precedence rules, which
is the practice note 0038 established after a duplicated fact went stale in a
day.

The step order in setup is deliberate: `migrate status` comes before the first
run, not after it. Every failure mode in this workflow is a root that resolved
to the wrong tree, and each one produces a successful-looking run.

## Trade-offs and rejected alternatives

**Two roots is now the first thing `CLAUDE.md` says**, ahead of the daily
routine, and most sessions run the repository in place where the distinction
costs nothing. That is a real tax on the common case, paid because the
alternative — discovering the distinction at step 4, after a digest has been
committed to the wrong repository — is not recoverable by reading further.

**Considered: a separate `docs/deployment.md`** rather than a section in
`CLAUDE.md`. Rejected because an agent session reads `CLAUDE.md` and may read
nothing else, and "which tree am I writing to" is not optional context.

**Not documented: submodules.** Named in the workflow as the answer if you need
the version fixed by git rather than by discipline, and not spelled out, because
nothing in this repository has been run that way and a procedure nobody has
executed is a liability in a file that is meant to be authoritative.

**Config drift is stated, not solved.** `config/` moves to the deployment, so
improvements this repository makes to `settings.yaml` or `sources.yaml` never
reach an existing archive and nothing reports the gap. Naming it in two places
is the whole mitigation.

## What a reviewer should check

- That the anchors resolve: `CLAUDE.md#first-which-tree-is-the-archive-in` is
  linked from `workflows/README.md` and `README.md#keeping-the-archive-in-a-repository-of-its-own`
  from the layout table.
- That the workflow's procedure actually runs. Follow it into a throwaway
  directory and stop at `migrate status`, which must print two different paths.
- That no workflow file restates a rule instead of linking it — the standard
  `workflows/README.md` sets for itself.
- The test count in the harness files (416) against
  `python3 -m unittest discover -s tests -t .`.

## Downstream impact

None mandatory. A deployment running in place needs to change nothing and the
routine it follows is unchanged. A deployment that wants the split follows
`workflows/deployment/`; no record, config file or generated artifact changes
format either way.
