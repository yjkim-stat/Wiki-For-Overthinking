# 0039 — Name the deployment root once, and mean it everywhere

| | |
| --- | --- |
| **Commit** | `feat(common): name the deployment root once, for every entry point` |
| **Scope** | `pipelines/common/paths.py`, `pipelines/common/config.py`, `pipelines/run_daily.py`, `pipelines/render.py`, `pipelines/enrich/queue.py`, `pipelines/enrich/findings.py`, `pipelines/migrate.py`, `tests/test_config.py` |
| **Kind** | feature |

## What changed

The tree an archive lives in can be named for a whole session, not per command:

```bash
export RA_WM_ROOT=~/research-archive
python3 -m pipelines.render          # writes there, not here
```

`--root` still wins where it is given, and with neither set everything behaves
exactly as before — the checkout is the archive. `migrate status` now opens with
the two roots it resolved, so the question "which tree am I about to write to"
has a command that answers it.

A root that is named but is not a directory raises `RootError` at load.

## Why it is built this way

`--root` existed already and was documented as being for testing. It is not: it
is the difference between a repository that holds both the code and the archive,
and a deployment that keeps its archive in a repository of its own so that
pulling a new version of the code cannot collide with a month of readings. The
change is mostly an admission of what the flag was already for.

The resolution lives in `paths.resolve_root`, and every entry point reaches it
through the single `config.load` they all already call. That is the property
worth keeping: there is no way to point one stage at a deployment and leave
another pointing at the checkout, because none of them resolves the root itself.
The bug in `scripts/daily.sh` — fixed separately — is exactly what that failure
looks like, and it was possible because the shell script did its own plumbing.

The refusal to fall back is the load-bearing part. A typo in `RA_WM_ROOT` that
quietly resolved to this checkout would collect, read, render and commit an
archive into the code repository, with every step reporting success. Raising is
the only outcome that cannot be mistaken for a clean run.

## Trade-offs and rejected alternatives

**An environment variable is global state**, and a shell that has one exported
from an earlier task will apply it to an unrelated command. That is the cost of
not typing `--root` five times a session. `migrate status` printing the resolved
root is the mitigation, and the harness in `workflows/deployment/harness.md`
says to run it first for this reason.

**Considered: resolving the root inside `Layout` instead.** Rejected because
`Layout` is constructed with an explicit root by tests and by `migrate`, and an
environment variable reaching into those would make the sandbox suite depend on
the ambient environment.

**Considered: making `RootError` a `ConfigError`.** It would read consistently
at the call sites, but `paths` cannot import `config` — `config` imports
`paths`. The message names the variable, which is what a reader needs.

**Not done: pinning.** Nothing relates a code checkout to a deployment; a `git
pull` can still move the code under a running archive. Recording the version is
left to the deployment (`FRAMEWORK.txt` in the workflow), which is discipline
rather than enforcement.

## What a reviewer should check

- Precedence, in `tests/test_config.py::DeploymentRootTests`: flag over
  environment over checkout, and a missing root raising rather than falling
  back. Break it by returning `None` instead of raising and watch
  `test_a_root_that_is_not_there_raises` fail.
- That nothing resolves a root on its own: `grep -rn "RA_WM_ROOT\|resolve_root"
  pipelines/` should show `paths.py` defining it and `config.py` calling it, and
  nothing else.
- That the default is untouched: with the variable unset, `python3 -m
  pipelines.migrate status` prints `code the same tree -- the repository is run
  in place`.

## Downstream impact

None required. A deployment that runs the repository in place sees no change in
behaviour and no new configuration. A deployment that wants the split can adopt
it without editing any record — see `workflows/deployment/`.
