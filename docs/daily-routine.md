# The daily routine

How the automation actually runs, and what to check when it misbehaves.

## The two halves

The system splits cleanly at the work queue.

```
                        deterministic                    judgement
                 ┌──────────────────────────┐   ┌──────────────────────┐

  arXiv ──┐
  venues ─┤
  curated ┼─► collect ─► score ─► dedupe ─► store ─► queue ─► read ─► complete
  YouTube ┘                                   │                          │
                                              ▼                          ▼
                                            data/                  data/queue/done/
                                              │                          │
                                              └──────► render ◄──────────┘
                                                         │
                                          archive/ · wiki/ · outputs/
```

Everything left of the queue is reproducible: same inputs, same records. Everything
right of it needs a reader. Keeping them apart means a slow or failed reading step
costs you summaries, never a day of collection, and that changing how things are
rendered never requires re-fetching anything.

## Scheduling

The intended trigger is a Claude Code Routine that wakes a session on a schedule
and hands it the routine from `CLAUDE.md`. A Routine is used rather than a cron
job because step 2 — reading the papers — needs a model in the loop, and a
plain cron job has no way to do it.

To register one, ask Claude to create a Routine whose prompt is:

> Run the daily routine in CLAUDE.md: collect, drain the summarization queue,
> render, and commit.

Two things to know:

- **The container is ephemeral.** Each firing starts from a fresh clone. State
  that must survive lives in `data/` and has to be committed at the end of the
  run — which is why `data/index/seen.sqlite` is tracked despite being a binary.
- **A firing that does nothing is normal.** Quiet days happen; the digest will
  say so.

If you would rather run collection on a plain schedule and read the queue when
convenient, `scripts/daily.sh` is safe to run from cron. The queue simply grows
until someone drains it.

When the archive lives in a repository of its own, the scheduled job has two
clones to keep current and must say which tree it works in — `RA_WM_ROOT` in the
environment, or `--root`, which `daily.sh` forwards to every stage. The commit
at the end of the run belongs to the archive's repository, not the code's.
[`workflows/deployment/`](../workflows/deployment/) has the full procedure.

<!-- LOCAL: this archive's actual routine state. See LOCAL-DELTAS.md -->
### This archive's routine — currently paused, and now two trees

A Routine did run nightly and **is disabled as of 2026-08-09, at the user's
request, for resource reasons. Do not re-enable it without being asked.** The
cron expression and prompt are intact, so resuming is a field update rather
than a re-creation.

| | |
| --- | --- |
| ID | `trig_018yxS27DM2m7HbgLP7MfvZ7` |
| Name | ra-lrm daily literature archive |
| Schedule | `0 22 * * *` UTC = 07:00 KST |
| State | `enabled: false` |

**Since 2026-08-21 the archive is in a repository of its own**
([0093](commit/0093-the-archive-moves-to-a-repository-of-its-own.md)), so the
job has two clones to keep current and must say which tree it works in:

| | |
| --- | --- |
| code | `Recipe-for-Research-Team-Management-with-Claude` — the program |
| archive | `Recipe-for-Reasoning-of-LLM` — `RA_WM_ROOT`, and where the digest is committed |

Three things to settle in the same call that re-enables it. The prompt lives in
the trigger's `job_config`, not in any checkout, so **editing a repository does
not reach it**:

- **Which repository it clones — now both.** It was written to clone one. It
  must clone the code repository *and* the archive repository, export
  `RA_WM_ROOT` at the archive clone, and commit the day's digest **there**. A
  digest appearing in the code repository is the sign the variable did not
  take; `migrate status` prints both roots and is the check.
- **Where it writes commit notes — nowhere, now.** Its step 7 names
  `docs/commit/NNNN-slug.md`. That directory belongs to the code repository and
  a scheduled reading run does not change the program: everything it commits is
  a digest, and a digest needs no note. Numbering notes from a nightly job would
  advance a sequence this repository's sessions also advance, which is the
  collision that has already had to be unpicked four times.
- **The sweep caps.** `max_abstracts_per_run: 120` and
  `virtual_site.max_details_per_run: 60` in `config/sources.yaml` were tuned for
  a three-topic archive; this one tracks five. Consider halving them for the
  first unattended night and reading what the run reports.

On the first run back, `collect.lookback_days` is **2**, so it sees two days
regardless of how long the pause lasted. Widen it once with `run_daily --days N`
to cover the gap, then let it fall back — `seen.sqlite` is tracked, so a pause
creates a gap in collection, never duplicate work.

And once it is running, **"no new commit" means either a quiet collection day or
a failed run, and those must be told apart rather than assumed.** This routine
has failed silently before: on 2026-08-08 it collected for thirty minutes, left
its only commit until the end, ran out of session, and the archive gained
nothing — including the collection. Committing after every step is what fixed
it, and it is safe because `data/queue/` and `seen.sqlite` are tracked.
