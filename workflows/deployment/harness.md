# Harness — deployment

What tells you the roots are what you think they are, and where nothing will.

## The one command that answers "where am I"

```bash
python3 -m pipelines.migrate status
```

```
roots
  deployment /home/you/research-archive
  code       /home/you/ra-wm
```

Run it **before** collecting, not after. Every failure mode in this workflow is
a root that resolved to the wrong tree, and each one looks like a successful run
at every other step:

| It prints | It means |
| --- | --- |
| `code  the same tree -- the repository is run in place` when you expected two | The variable did not take. `run_daily` is about to write into the code checkout. |
| A deployment path you did not expect | A stale `RA_WM_ROOT` from an earlier session, or a shell that did not inherit the export. |
| `WARNING branch '' has no upstream` | The archive repository has no remote. Nothing is being backed up — the container is ephemeral. |
| `records ... papers 0` against an archive you know is populated | The right tree is not where you think it is; check `deployment` against the paths in the `documents` line. |

A root that is named but absent does not reach any of this: `RA_WM_ROOT` is
refused at load with `RootError`, before a single file is written. That is
deliberate — the fallback it replaces was "quietly use the code checkout".

## The tests

```bash
python3 -m unittest tests.test_config -v      # root resolution
python3 -m unittest tests.test_templates -v   # the search order, and render without templates/
```

`tests/test_config.py::DeploymentRootTests` pins the precedence: flag, then
environment, then this checkout, and a named-but-missing root raises rather than
falling back.

`tests/test_templates.py` pins the other half: a deployment with no `templates/`
renders end to end from the shipped ones, and a deployment that overrides one
file gets that file and inherits the rest.

## Prove it bites

```bash
# the fallback: strip the deployment's templates, render must still work
mv ~/research-archive/templates /tmp/bak 2>/dev/null
RA_WM_ROOT=~/research-archive python3 -m pipelines.render     # expect success

# the override: change one, see it used
mkdir -p ~/research-archive/templates/wiki
sed 's/^# /# [mine] /' templates/wiki/note.md > ~/research-archive/templates/wiki/note.md
RA_WM_ROOT=~/research-archive python3 -m pipelines.render
head -1 ~/research-archive/wiki/topics/*.md                   # expect [mine]
```

```bash
# every stage honours the root: a stub interpreter shows what daily.sh forwards
printf '#!/usr/bin/env bash\necho "PY: $*"\n' > /tmp/fakepy && chmod +x /tmp/fakepy
PYTHON=/tmp/fakepy scripts/daily.sh --root /tmp/deploy
# expect --root on run_daily AND render AND queue
```

That last one is the check for the bug this workflow was written around:
`daily.sh` used to pass `--root` to the collection step alone, so a run
collected into the deployment and rebuilt the code checkout. Both commands
exited 0.

## What nothing checks

- **That the code checkout stayed clean.** No test and no command notices that a
  run wrote a digest into the code repository. `git status --short` in the code
  root after a run is the only thing that will tell you, and you have to think
  to run it.
- **That `FRAMEWORK.txt` is current.** It is a file somebody writes by hand.
  Nothing compares it to `git rev-parse HEAD`, and a stale one is worse than an
  absent one because it reads as an answer.
- **That the archive repository has a remote, or that anything was pushed.**
  `migrate status` warns, and warning is all it does.
- **That a new version of the code did not change what a render produces.** The
  suite runs against fixtures, not against your archive. The diff after
  `render` under a new version is the evidence, and reading it is manual.
- **Config drift.** `config/` lives in the deployment now, so improvements the
  code makes to `settings.yaml` or `sources.yaml` never arrive and nothing
  reports the gap.
