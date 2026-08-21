# 0038 — Collection moves to local cron

| | |
| --- | --- |
| **Commit** | `docs: record that collection now runs from local cron, not from the cloud routine` |
| **Scope** | `docs/commit-local/0038-collection-moves-to-local-cron.md` (the script itself is outside this repository) |
| **Kind** | docs · operational |

## What changed

Nothing in this repository's code. What changed is where collection happens:
`/home/yjkim/bin/w-ot-daily.sh` now runs from this machine's crontab at 07:00
KST and does `run_daily` plus `render`, then commits and pushes. The scheduled
cloud routine still fires at the same minute and still does the reading.

This note exists because a future session will otherwise see commits arriving in
`origin/main` from nowhere, with no code in the repository that produces them.

## Why it is built this way

**Collection is local because the cloud cannot reach arXiv.** The scheduled
environment's egress policy denies `arxiv.org` as well as `export.arxiv.org`, so
the API and the listing fallback both return 403 CONNECT there and the run
collects nothing. This machine reaches both. That was measured on 2026-08-21,
after a session spent some time wrongly attributing the failure to a rate limit.

**Only the collection half moves.** Draining the queue is the agent's job and
cannot be automated here, so the script reads nothing and says so in its own
commit message. The split is not arbitrary: collection is the time-critical
half. The arXiv listing browses announcement days rather than searching a date
range, so a day nobody collected is a day lost for good and `--days N` cannot
reach back through it. Reading is not time-critical, because everything the run
files stays in `data/queue/`, which is tracked.

**The script lives outside the repository.** Every path in it is specific to
this machine — the conda interpreter, the log directory, the checkout root — and
a fresh clone of this archive should not inherit them. It follows the pattern
already established on this host by the sibling deployment's
`/home/yjkim/bin/ra-lrm-daily.sh`, which solved the same problem for the same
reason. Two differences from that script matter here: this deployment runs in
place, so there is no `RA_WM_ROOT` and no `--root` anywhere; and local `master`
tracks `origin/main`, so the push is `git push origin master:main`.

**It refuses to run in a dirty tree.** The sibling deployment's archive root is
only ever written by unattended runs. This root is a live checkout that a person
works in, so `git add -A` in an unattended job could sweep an interactive
session's work-in-progress into a commit nobody wrote. The check is a hard exit,
not a stash.

**It expects to lose the push race.** The cloud routine fires at the same minute
and pushes to the same branch. On rejection the script fetches, rebases once and
retries; a second failure exits non-zero and leaves the commit local rather than
retrying into a loop.

## Trade-offs and rejected alternatives

**07:00 is the same minute as the cloud routine, which is not the best time and
is what was asked for.** Running at, say, 06:30 would be strictly better: the
cloud session would clone a repository that already contains the night's tasks
and could start reading immediately, instead of racing a collector that is still
writing. As it stands the cloud session usually reads the *previous* night's
collection. The rebase-and-retry above makes the arrangement safe; it does not
make it optimal. Changing it is one number in one crontab line.

**Rejected: turning the cloud routine off and doing everything locally.** The
reading is the half only a Claude session can do, and the cloud routine is what
schedules one.

**Rejected: committing the script into `scripts/`.** It would be the only file
there that cannot run on another machine.

**Accepted cost: the script is not version-controlled.** If this host is lost,
the schedule is lost with it and this note is what says it existed. The sibling
deployment accepted the same cost.

## What a reviewer should check

- `crontab -l` — two entries now: `ra-lrm-daily.sh` at 03:00 and
  `w-ot-daily.sh` at 07:00. The system timezone is `Asia/Seoul`, so those fields
  are local time and need no UTC conversion.
- `/home/yjkim/w-ot-logs/<date>.log` — one file per run. The line beginning
  `arxiv:` classifies the run as `listing ok`, `BLOCKED`, or contributed
  nothing, and the same string goes into the commit subject, so the archive's
  own history distinguishes a quiet day from a blocked one.
- The lock: `flock -n` on `/tmp/w-ot-daily.lock`. Two concurrent runs would race
  on `data/index/seen.sqlite`.

## Downstream impact

For any other deployment: none, this is one host's operational arrangement. For
this one: commits with the subject `archive: <date> collect — …` are the cron
job's and were not written by a session. A session that finds the working tree
dirty at 07:00 should expect the night's collection to have been skipped, and
the log will say so.

## Correction (0038)

The "What a reviewer should check" section above says the `arxiv:` line
classifies a run as `listing ok`, `BLOCKED`, or contributed nothing. That was
the script's logic and it was wrong, in a way the first successful run exposed
immediately: it looked only for listing lines, but `arxiv.listing.mode` is
`auto`, so **the listing fires only when the API returned nothing**. A healthy
run in which the API worked produces no listing lines at all, and the first real
run — which collected 39 entries and filed a paper task — was recorded in its own
commit subject as `arxiv contributed nothing`. Commit `26c9c0d0` carries that
wrong subject and is left as it stands rather than rewritten.

The classifier now counts both paths from this run's lines only, and reports
`api ok` / `listing ok (api gave nothing)` / `api ok, listing also ran` /
`BLOCKED` / contributed nothing, with the sweep's outstanding abstract count
appended. Two things this fixes beyond the wording:

- **The log is one file per day and appended to**, so a second run of the day
  was classifying itself on the first run's evidence. The script now records the
  log's length at entry and reads only past it.
- **The API is the normal path and was not being reported at all.** The listing
  is the fallback; a message that names only the fallback cannot distinguish "the
  API worked" from "nothing happened", which is the whole purpose of the line.

## Superseded in part (0040)

This note says the cloud routine "still fires at the same minute and still does
the reading", and lists turning it off as a rejected alternative. As of
2026-08-21 it is disabled — see
[0040](0040-the-cloud-routine-is-turned-off.md). The local cron job described
above is unchanged and is now the only scheduled writer to this repository;
reading happens only when somebody opens a session.
