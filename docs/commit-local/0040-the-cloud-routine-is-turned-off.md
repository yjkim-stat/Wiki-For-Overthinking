# 0040 — The cloud routine is turned off

| | |
| --- | --- |
| **Commit** | `docs: the scheduled cloud routine is disabled; collection is cron, reading is a session` |
| **Scope** | `docs/commit-local/0040-the-cloud-routine-is-turned-off.md`; a pointer added to 0038 |
| **Kind** | docs · operational · breaking |

## What changed

The scheduled cloud routine `overthinking-archive-daily`
(`trig_01WEh2UgzPUTjqpvwhD8xgeD`, `0 22 * * *` UTC = 07:00 KST) is set to
`enabled: false`. Nothing else about it is altered — its prompt, environment and
schedule are intact, so re-enabling is one field.

The local cron job stays. **This archive is now collected automatically and read
only when somebody opens a session.**

## Why it is built this way

This reverses a decision [0038](0038-collection-moves-to-local-cron.md) recorded
as rejected, and the reversal is the archive owner's, not an inference from
anything measured here. What can be said for it from the record: the routine's
collection half could not work, because the cloud environment's egress policy
denies both arXiv hosts, and that half is now done locally by cron. What is
genuinely lost is the reading half — a scheduled session that drained the queue
overnight.

**The consequence is stated plainly because it is the whole cost.** Reading
cannot be automated: it is the part the pipeline defers to a person or an agent
by design, and `summarize.backend: queue` is what makes that explicit. With the
routine off, nothing drains the queue between sessions. Tasks will accumulate,
which is not a failure — everything the collector files stays in `data/queue/`,
which is tracked, so nothing is lost by reading late. But the archive's steady
state is now a growing backlog rather than a nightly zero, and a session that
opens after a quiet week should expect one.

**The backlog is visible without opening the queue.** The cron job's commit
subject carries `; N pending`, so `git log --oneline` shows how far behind the
reading is, day by day, without running anything.

**One thing this simplifies.** 0038 recorded that 07:00 was the same minute as
the cloud routine and that the two would race to push, handled by a
rebase-and-retry. There is no longer a second writer on that schedule, so the
race is gone. The retry stays: other sessions still commit to this repository,
and a guard that costs nothing when it is not needed is not worth removing.

## Trade-offs and rejected alternatives

**Rejected: leaving the routine enabled with its collection steps removed**, so
it would only read. It would have kept the nightly drain at the cost of a
scheduled session that starts with no context — every reading made by an agent
that has not seen the archive's own conclusions. The readings made in a session
that has, are better, and this repository's `wiki/topics/overthinking.md`
analysis is the evidence: it was built from the archive's accumulated readings
and then used to judge four new papers the same afternoon.

**Rejected: deleting the routine.** It is disabled, not removed, so its prompt
survives as a record of what an autonomous run was asked to do, and re-enabling
is one field rather than a rewrite.

**Not done: making cron alert on a growing backlog.** Nothing warns when the
queue passes some size. The commit subject is the signal, and it needs a person
to look at it.

## What a reviewer should check

- The routine's `enabled` field is `false`. `next_run_at` may still show a
  timestamp; it is `enabled` that gates firing, not that field.
- `crontab -l` — the 07:00 entry is unchanged and is now the only scheduled
  writer to this repository.
- `git log --oneline --grep="collect —"` — the cron job's commits, each ending
  in `; N pending`. A rising N is the backlog.

## Downstream impact

For anyone reading this repository's history: from 2026-08-21 a stretch of
`archive: <date> collect` commits with no `digest` commit between them means
nobody opened a session, not that the archive was quiet. The two are told apart
by the `pending` count in the subject.
