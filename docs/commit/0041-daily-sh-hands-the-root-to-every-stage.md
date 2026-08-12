# 0041 — `daily.sh` hands the root to every stage

| | |
| --- | --- |
| **Commit** | `fix(scripts): daily.sh forwards --root to every stage, not the first` |
| **Scope** | `scripts/daily.sh` |
| **Kind** | fix |

## What changed

`scripts/daily.sh --root <path>` collected into `<path>` and then rendered the
code checkout. The flag reached `run_daily` because the script passed `"$@"`
straight through, and reached nothing after it, because `render` and `queue
stats` were invoked bare.

The script now extracts a `--root <path>` or `--root=<path>` from its arguments
and passes it to every stage.

## Why it is built this way

The failure is silent at both ends. `run_daily` exits 0 having filed tasks in
the deployment; `render` exits 0 having rebuilt an empty archive in the code
checkout; the run reports success twice. What you get is a deployment whose
queue fills up and whose wiki never moves, and a code repository quietly
accumulating an archive it was never meant to hold. Nothing in the output says
so — the paths in the log are the only evidence, and nobody reads a log that
ends in success.

Everything in the pipeline resolves the root through one function, so no Python
entry point can disagree with another. This script was the exception: it did its
own plumbing, and that is precisely where the two halves came apart. The fix
keeps the plumbing but makes it total.

`RA_WM_ROOT` needs none of this — it is read by every entry point already, which
is the better way to run a deployment and the reason the extraction only has to
handle the two spellings argparse accepts.

The local variable renamed from `ROOT` to `CODE_ROOT` because the script now
talks about two roots and the old name meant the one the reader is least
interested in.

## Trade-offs and rejected alternatives

**The extraction is a small parser, and small parsers rot.** It handles
`--root X` and `--root=X`, which is what argparse accepts; it would not handle an
abbreviation like `--roo X`, which argparse also accepts. That is a real gap and
an unlikely one, and closing it would mean re-implementing argparse in bash.

**Considered: exporting `RA_WM_ROOT` from the extracted value** instead of
passing the flag on. Fewer moving parts, but it would leak the setting into
anything else the script ever calls, and the flag is meant to outrank the
variable rather than become it.

**Considered: refusing to run when `--root` is present and telling the caller to
use the variable.** Rejected as unhelpful; the flag is documented on every
command and a script that rejects it is a surprise.

## What a reviewer should check

- The forwarding, with a stub interpreter, which needs no network:
  ```bash
  printf '#!/usr/bin/env bash\necho "PY: $*"\n' > /tmp/fakepy && chmod +x /tmp/fakepy
  PYTHON=/tmp/fakepy scripts/daily.sh --root /tmp/deploy
  ```
  `--root` must appear on `run_daily`, `render` **and** `queue` — and on `queue`
  it must come before the subcommand, where its parser expects it.
- That the no-root case is byte-identical to before: the same command with no
  arguments must print three bare invocations.
- That `--dry-run` still exits before rendering.

## Downstream impact

None. A deployment that runs the repository in place passes no `--root` and sees
no change. Nothing is checked by the test suite here — `daily.sh` is not covered
by it, which is stated in `workflows/deployment/harness.md` under what nothing
checks.
