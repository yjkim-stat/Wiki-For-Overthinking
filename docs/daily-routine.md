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

## Running it from cron instead

If you would rather run collection on a plain schedule and read the queue when
convenient, `scripts/daily.sh` is safe to run from cron. The queue simply grows
until someone drains it.

`scripts/install-cron.sh` writes the entry for you:

```
scripts/install-cron.sh --root /srv/archive --print     # show it, change nothing
scripts/install-cron.sh --root /srv/archive             # install it
scripts/install-cron.sh --root /srv/archive --remove
```

The entry is tagged with its deployment root, so re-running replaces that root's
line rather than adding a second one, two archives on one host get a line each,
and every job the installer did not write is carried through untouched. A
crontab that could not be *read* is never *written* — the failure worth guarding
against is not a wrong entry, it is somebody else's backup job disappearing.

Two things it does that are easy to forget by hand. It pins the interpreter to
an absolute path, because cron's `PATH` is not a login shell's and a bare
`python3` fails every night into a log nobody has started reading yet. And it
refuses a `%` anywhere in a path or schedule, which cron reads as a newline and
would silently truncate the command at.

**What cron cannot do is read.** It schedules collect, score, store and render;
the reading step needs a model in the loop. Drain the queue when it suits you
and run `daily.sh` once more to fold the results in.

When the archive lives in a repository of its own, the scheduled job has two
clones to keep current and must say which tree it works in — `RA_WM_ROOT` in the
environment, or `--root`, which `daily.sh` forwards to every stage. The commit
at the end of the run belongs to the archive's repository, not the code's.
[`workflows/deployment/`](../workflows/deployment/) has the full procedure.

## When a scheduled run goes wrong

Three failure shapes worth knowing before you rely on a schedule. None of them
announce themselves.

**"No new commit" is ambiguous.** It means either a quiet collection day or a
run that died, and those have to be told apart rather than assumed. A run that
leaves its only commit until the end loses everything it collected when it runs
out of time — including the collection. Committing after every step is what
fixes it, and it is safe precisely because `data/queue/` and `seen.sqlite` are
tracked.

**A pause does not create duplicate work, and does not backfill either.**
`collect.lookback_days` is what the next run sees regardless of how long the
gap was. Widen it once with `run_daily --days N` to cover the gap, then let it
fall back.

**The sweep caps are tuned to a topic count.** `sweep.max_abstracts_per_run` and
`virtual_site.max_details_per_run` in `config/sources.yaml` bound one run's
requests, and a deployment tracking more topics than the defaults assume will
quietly leave more owed each night. Read what the first unattended run reports
rather than assuming the defaults fit.

If the schedule is a Claude Code Routine rather than cron, one more: **the prompt
lives in the trigger, not in any checkout**, so editing a repository does not
reach it. A Routine that clones two trees has to be told about both — export
`RA_WM_ROOT` at the archive clone and commit the digest there. A digest landing
in the code repository is the sign the variable did not take.
