# 0067 — The log line said seventy-six

| | |
| --- | --- |
| **Commit** | `fix(render): the summary log line reports tasks filed` |
| **Scope** | `pipelines/render.py`, `docs/LOCAL-DELTAS.md` |
| **Kind** | fix |

> **Superseded on 2026-08-14.** `origin/main` reached the same defect
> independently in [0054](0054-the-queue-reports-what-it-wrote.md), by a better
> route — counters inside `Queue`, and three numbers where there had been one
> wrong one. The template's implementation is the one that survived the merge,
> so the code this note describes is no longer in the tree. The note stays
> because the commit does, and because the convergence is the useful part:
> [0068](0068-the-same-collision-and-the-same-bug.md).

## What changed

`queue_missing_summaries` logs how many tasks it filed rather than how many
records it found lacking a summary. The return value is untouched.

## Why the split

Note 0066 fixed the same shape in `queue_missing_definitions` and stopped one
line short. The very next render printed:

```
re-queued 76 missing summary task(s)
...
'summaries_queued': 0
```

Both numbers are in the same output, three lines apart, and they disagree
because the reserve wrapper in `run` counts the queue on either side while the
function's own log line counts iterations. The result dict was already honest;
the line a person actually reads during a run was not.

The return value keeps its old meaning deliberately. The LOCAL reserve does not
use it — `docs/LOCAL-DELTAS.md` records that it counts the queue instead,
because the function reports records lacking a summary and two passes over one
backlog would report it twice. Changing the return value would make that comment
wrong and would silently alter what a template update is being compared against.
So the two numbers stay distinct and the comment now says which is which.

## What it is not

Not a behaviour change. Nothing about which tasks are filed moves; only the
count in one INFO line. It is worth a note because the number appears in the
output of every scheduled run, and a routine that reports 76 tasks re-queued on
a run that filed none is the kind of healthy-looking output this repository has
already been caught by twice.
