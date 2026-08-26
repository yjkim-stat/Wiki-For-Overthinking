# 0044 — Three cron jobs that never started

| | |
| --- | --- |
| **Commit** | `docs(local): the nightly collection has not run since it was installed` |
| **Scope** | `/home/yjkim/bin/w-ot-daily.sh`, `/home/yjkim/*-logs/` (outside the repository); `docs/commit-local/` |
| **Kind** | fix · operational |

## What changed

`w-ot-daily.sh` has two edits and the host gains three directories:

- `ROOT=/home/yjkim/wiki-overthinkg` → `ROOT=/home/yjkim/w-ot`. The old value
  is a path that has never existed on this machine.
- `BRANCH=master` → `BRANCH=main`. The local branch was renamed after
  [`0038`](0038-collection-moves-to-local-cron.md) was written; the push line
  `git push origin "$BRANCH:$REMOTE_BRANCH"` was pushing a ref that is gone.
- `/home/yjkim/w-ot-logs/`, `/home/yjkim/w-mem-logs/` and
  `/home/yjkim/ra-lrm-logs/` now exist.

The comment in the script that described the `master` → `main` mapping is
corrected to match.

Nothing in the pipeline changed. The script lives outside the repository, for
the reasons `0038` gives; this note is the record, since the file itself is not
version controlled anywhere.

## Why it is built this way

**The directories are the actual bug, and they defeat all three jobs, not
one.** Every crontab line has the shape

```
0 7 * * * /home/yjkim/bin/w-ot-daily.sh >> /home/yjkim/w-ot-logs/cron.log 2>&1
```

The shell opens that redirection *before* it execs the script. With the
directory missing the redirection fails, the script never runs, and there is
nowhere for the error to be written — `MAILTO=""` is set at the top of the
crontab, so cron's own report goes nowhere either. Each script does
`mkdir -p "$LOGDIR"` on its first lines, which looks like it covers this and
cannot: that line is inside the process that never starts.

This is why the failure was silent for as long as it was. A job that dies on
its first command still leaves a log; a job whose log could not be opened
leaves nothing at all, and looks identical to a job that was never scheduled.

**The two script edits are ordinary rot.** `wiki-overthinkg` is a typo that was
never exercised, because the missing log directory meant `cd "$ROOT" || …` was
never reached. `master` was correct when `0038` was written. Both were invisible
for the same reason: the outer failure masked the inner ones, so fixing the
directories without also fixing these would have converted a silent failure into
a nightly `FATAL: root missing` — which is better, but not working.

**Nothing was disabled.** The three jobs stay scheduled. Two of them
(`w-mem-daily.sh`, `ra-lrm-daily.sh`) still have wrong or absent targets and
will now fail loudly in their own logs instead of silently in the void, which is
the point of creating their directories.

## Trade-offs and rejected alternatives

**Fixing the script rather than the crontab.** The redirection could have been
dropped from the crontab instead, letting each script's own `mkdir -p` create
its log directory. Rejected: `cron.log` catches what happens *before* the script
can log anything — a missing interpreter, a permission error — which is exactly
the class of failure that produced this note.

**Leaving the two sibling jobs alone.** `w-mem-daily.sh` points at
`/home/yjkim/wiki-mem` while the checkout is `/home/yjkim/w-mem` — a one-word
fix whose target verifiably exists on branch `main`, matching the script.
`ra-lrm-daily.sh` points at `/home/yjkim/Wiki-For-Reasoning` and
`/home/yjkim/ra-lrm`, and **neither exists on this machine**, so it has nothing
to run against and no path edit can repair it. Both are other deployments'
business: repairing them starts an unattended commit-and-push loop on
repositories this archive does not own, which is not a change to make on
somebody's behalf. They are recorded here so the next person does not have to
rediscover them.

**Not verifying by running it.** The script commits and pushes. Its
preconditions were checked individually instead — root present, interpreter
executable, log directory writable, tree clean, not behind `origin/main`,
`main` resolvable, and `ssh -o BatchMode=yes git ls-remote` reaching the remote
without a passphrase prompt. The first real proof is the 07:00 run.

## What a reviewer should check

- **That the redirection now works**: `touch /home/yjkim/w-ot-logs/cron.log`
  succeeds. If it does not, nothing below matters.
- **That the branch mapping is real**: `git -C /home/yjkim/w-ot branch --show-current`
  prints `main`, and `git push origin main:main --dry-run` succeeds under
  `GIT_SSH_COMMAND='ssh -o BatchMode=yes'`.
- **That the dirty-tree guard still bites.** It is the one check standing
  between an interactive session's work-in-progress and an unattended
  `git add -A`. It refused correctly during this repair, when the tree held
  uncommitted synthesis answers.
- **The first log**: `/home/yjkim/w-ot-logs/$(date +%F).log` after 07:00. An
  absent file means the job still is not starting.

## Downstream impact

None for anyone who pulls this repository — the script is not in it and every
path named here is specific to this host. For this deployment: collection
resumes nightly, and the steady state `0040` describes returns, a queue that
grows until somebody reads it.

## Correction (0045)

**"Nothing was disabled. The three jobs stay scheduled."** That held for one
day. `ra-lrm-daily.sh` was stopped on 2026-08-26: creating its log directory
turned its failure from invisible into a nightly `FATAL: root missing`, and
since neither of its two paths exists on this machine there is nothing to point
it at. The line is commented, not deleted.

`w-mem-daily.sh` is still scheduled and still misconfigured, as described above.

See [`0045`](0045-the-job-with-nothing-to-run-against.md).
