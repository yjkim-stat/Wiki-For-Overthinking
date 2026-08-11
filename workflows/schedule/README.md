# Schedule

Two different jobs: **answering** a scheduled wake-up, and **wiring one up**.

Scheduling lives outside this repository. There is no cron file here and no
workflow under `.github/` — a deployment is driven by a Routine on the owner's
Claude account, which fires a prompt into a session with this repository
checked out. That separation is deliberate and it is the same one the rest of
the design rests on: the schedule is environment state, the repository is code.

---

## Answering a scheduled run

A scheduled session is an ordinary run of
[knowledge-and-wiki](../knowledge-and-wiki/) with one rule stacked on top.

### Never leave the only commit until the end

The container is ephemeral. Anything unpushed when the session ends is gone —
**including the collection**, which is the slow part.

This is safe to do incrementally because `data/queue/` and
`data/index/seen.sqlite` are both tracked on purpose. A commit after any step
preserves real progress: the records collected, the dedup state that stops
tomorrow re-collecting them, and every task answer already submitted.

```bash
python3 -m pipelines.run_daily
git add -A && git commit -m "archive: <date> collection" && git push
#   ^ this is the commit that must not be skipped
```

**If that push fails, stop and put it at the top of your report.** Everything
after it is wasted effort if the credentials are broken, and the problem has to
be fixed before the next firing.

Then drain the queue in batches, committing and pushing after each. **A partial
day that is pushed beats a complete day that is not.**

### Stopping early is a normal outcome

`render` re-files a task for any record that still lacks a summary, so anything
left pending is picked up on the next run. Leaving tasks unread is ordinary;
losing work is not. If the session starts feeling long, stop at a batch
boundary — commit, push, and say in your report how much is left.

### What the report must contain

Whether every push succeeded · how many items were collected and queued · how
many you read · **how many remain pending and why** · which entities were
promoted · any source that was unreachable.

A quiet day with nothing collected is a correct outcome — say so plainly. If a
topic returns nothing several days running, flag it: that has meant a scoring
bug more often than a quiet week.

---

## Wiring one up, pausing, resuming

Routines are created and edited by their owner in the Claude web UI. Two
properties matter and neither is obvious:

- **An agent can only modify a Routine it created itself.** One created through
  the web UI reports `created_via: "http_api"`, and an attempt to disable it
  from a session is refused. If you need a schedule paused, the owner has to do
  it — ask, do not report it as done.
- **A Routine fires a prompt, and that prompt is not in this repository.** It is
  stored with the Routine. So a change here that alters the routine — a new
  step, a renamed command — does not reach the scheduled run until somebody
  edits the Routine text. Keep the prompt thin and let it say *read `CLAUDE.md`
  first*, so the contract stays in one place.

### Writing the prompt

Thin, and pointing at the repository rather than duplicating it:

```
Run the daily routine for this archive. Read CLAUDE.md first — it is the
contract and it is authoritative; this prompt only adds what a scheduled run
needs to know.

<the push-early rule above>
<which branch to push to>
<what the report must contain>
```

Everything else belongs in `CLAUDE.md` and `workflows/`, where it can be
changed by a commit rather than by editing a Routine nobody can see from here.

### Cron

Expressions are evaluated in **UTC**. Convert local times first, and if the
conversion crosses midnight shift the day fields too — weekdays at 17:00 in
UTC−07:00 is `0 0 * * 2-6`, not `0 0 * * 1-5`.

## What nothing checks

- **That the schedule fired at all.** A Routine that is paused, suspended, or
  whose container failed to start produces no run and no error here. The only
  evidence is `archive/daily/<date>.md` not existing for a date — check it
  against the calendar, not against your memory of runs.
- **That the prompt still matches the repository.** Nothing compares the two.
  After changing the routine in `CLAUDE.md`, re-read the Routine prompt.
- **That two schedules are not fighting.** Several sessions committing to one
  repository is exactly the condition step 0 of every workflow exists for.
