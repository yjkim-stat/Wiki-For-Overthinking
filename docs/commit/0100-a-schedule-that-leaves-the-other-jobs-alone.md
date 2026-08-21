# 0100 — A schedule that leaves the other jobs alone

| | |
| --- | --- |
| **Commit** | `feat(scripts): install the scheduled collection job` |
| **Scope** | `scripts/install-cron.sh`, `tests/test_install_cron.py`, `docs/daily-routine.md` |
| **Kind** | feature |

## What changed

`scripts/install-cron.sh` writes, replaces or removes the crontab entry that
runs `scripts/daily.sh` for one deployment root. `--print` emits the line
without touching anything, for hosts whose cron is managed by configuration
management rather than by hand.

Until now the documentation said `daily.sh` "is safe to run from cron" and left
the entry to the reader. That sentence is true and it is not enough: the two
ways such an entry usually fails are invisible at install time.

## Why it is built this way

**The risk being managed is not our entry, it is everybody else's.** A crontab
is shared state holding jobs this repository knows nothing about. So the
script's central rule is that a crontab which could not be *read* is never
*written*: `crontab -l` exiting non-zero is ordinary when no crontab exists yet
and means something entirely different otherwise, and the two are told apart by
the message, with `LC_ALL=C` forced so the match does not depend on the host's
locale. Anything unrecognised aborts and says to use `--print`. Without that
distinction a transient read failure replaces the user's crontab with one line.

**The entry is tagged with its deployment root**, which is what makes re-running
idempotent and what lets one host serve two archives. Keying on the script path
instead would collapse those two into one; keying on nothing at all would append
a duplicate every time somebody re-ran the installer to change the hour.

**The interpreter is resolved at install time and pinned absolutely.** cron's
`PATH` is not a login shell's. A bare `python3` installs cleanly, fails every
night, and writes the failure into a log nobody has started reading — which is
the worst available shape for a scheduling bug, because the archive simply looks
quiet. Pinning has a real cost: a virtualenv rebuilt at a new path needs the
installer re-run. That is a visible failure against an invisible one.

**A `%` in a path or schedule is refused.** cron reads an unescaped `%` as a
newline and hands the command only what precedes it. Escaping it correctly is
possible; refusing is honest, and the case is rare enough that a clear error
beats a subtly truncated command.

**Collecting into the code checkout warns but does not refuse.** The single-tree
layout is supported and is what a fresh clone does. But it is the choice that
mixes an archive into the repository framework updates are pulled into, so it is
never made silently.

**What it deliberately does not do is read.** The scheduled job stops at render.
Reading needs a model, cron has none, and pretending otherwise by scheduling
something that half-works would be worse than the queue growing — which is the
intended shape, not a backlog.

## Trade-offs and rejected alternatives

- *A systemd timer instead.* Rejected for now: cron is available everywhere the
  repository already assumes a POSIX shell, and a timer needs two unit files
  plus a privileged install path. `--print` leaves the door open — a host that
  wants a timer can take the command line and wrap it.
- *Editing the crontab file in place.* Rejected. `crontab -` is the interface
  that validates and reloads; writing `/var/spool/cron/...` directly is
  implementation-specific and skips the validation.
- *Refusing to schedule a root that does not exist.* Softened to a refusal that
  `--force` overrides, because scheduling ahead of a tree that a later step
  creates is a legitimate order of operations.
- *Validating the cron expression properly.* Only the field count is checked.
  A real validator would duplicate cron's own parser; the field count catches
  the mistake people actually make, and cron rejects the rest.

## What a reviewer should check

The suite drives a stub `crontab` through `RA_WM_CRONTAB_CMD`, so it never
touches the real one:

```bash
python3 -m unittest tests.test_install_cron -v
```

The assertion worth reading first is
`test_a_crontab_that_cannot_be_read_is_never_written`. Four mutations were
confirmed to fail the suite: treating any `crontab -l` failure as an empty
crontab, dropping the tag-based de-duplication, emitting a bare `python3`, and
writing the new entry without carrying the existing lines through.

## Downstream impact

None required. `daily.sh` is unchanged and a deployment that already has a
hand-written crontab entry keeps working; the installer only touches lines
carrying its own tag, so it will not adopt or remove an entry written by hand.
