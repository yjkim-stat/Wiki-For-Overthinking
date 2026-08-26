# 0045 — The job with nothing to run against

| | |
| --- | --- |
| **Commit** | `docs(local): stop the 03:00 job whose deployment is not on this machine` |
| **Scope** | this host's crontab (outside the repository); `docs/commit-local/` |
| **Kind** | chore · operational |

## What changed

The 03:00 `ra-lrm-daily.sh` line is commented out. Two active jobs remain:
`w-ot-daily.sh` at 07:00 and `w-mem-daily.sh` at 09:00.

The stale path in the `w-ot` block's own comment — it still said
`/home/yjkim/wiki-overthinkg`, the root [`0044`](0044-three-cron-jobs-that-never-started.md)
corrected in the script — is fixed at the same time, so the crontab and the
script now name the same directory.

## Why it is built this way

**The job has no target, and no path edit can give it one.**
`ra-lrm-daily.sh` names `CODE=/home/yjkim/Wiki-For-Reasoning` and
`ARCHIVE=/home/yjkim/ra-lrm`. Neither exists on this machine, and neither is a
near-miss for something that does — unlike `w-mem-daily.sh`, whose
`/home/yjkim/wiki-mem` is one word away from the real `/home/yjkim/w-mem`. A
job pointing at a deployment that is not here is not misconfigured; it is
scheduled on the wrong host.

**Commented, not deleted.** The schedule, the log path and the redirection are
the parts worth keeping: if those checkouts are restored, uncommenting one line
is the whole repair, and the reason it was stopped is written directly above it.
A deleted line leaves the next person to reconstruct both.

**Now rather than later.** `0044` created `/home/yjkim/ra-lrm-logs/`, which
changed this job's failure from invisible to nightly: from tonight it would have
reached `FATAL: root missing` and written that line every day into a log nobody
would read, on a host where a real failure needs to stand out. The alternative
was to delete the log directory again and restore the silence, which trades a
harmless daily line for the exact condition that hid three broken jobs for as
long as it did.

## Trade-offs and rejected alternatives

**Repairing it instead of stopping it** would mean cloning
`Wiki-For-Reasoning` and creating an archive root for a deployment this archive
does not own, then letting an unattended job commit and push to it. That is a
decision for whoever owns that archive.

**Leaving it running and ignoring the log** was the other option, and it is what
the state before this change amounts to. Rejected because a log that always
contains a FATAL is a log that stops being read, and `w-ot-logs/` and
`w-mem-logs/` sit beside it.

**`w-mem-daily.sh` is still not touched.** Its target exists — `/home/yjkim/w-mem`,
branch `main`, remote `Wiki-For-Memory-of-Agent` — and its `ROOT=/home/yjkim/wiki-mem`
is a one-word fix. It is left alone for the reason `0044` gives: repairing it
starts an unattended commit-and-push loop on a repository this archive does not
own. It will now fail loudly in `/home/yjkim/w-mem-logs/` every night at 09:00
until somebody decides.

## What a reviewer should check

- `crontab -l | grep -E '^[0-9]'` lists exactly two jobs, 07:00 and 09:00.
- The commented line is still present with its explanation, so
  `crontab -l | grep ra-lrm` finds it.
- `/home/yjkim/ra-lrm-logs/` still exists and stays empty — if a dated log
  appears there, the job is still firing and this change did not take.

## Downstream impact

None for anyone who pulls this repository; the crontab is not in it. On this
host, the reasoning archive collects nothing from tonight — which is the state
it was already in, now stated rather than discovered.
