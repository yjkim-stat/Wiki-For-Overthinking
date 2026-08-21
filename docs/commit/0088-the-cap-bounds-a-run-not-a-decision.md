# 0088 — The cap bounds a run, not a decision

| | |
| --- | --- |
| **Commit** | `fix(render): a hand-filed paper is queued whatever the cap says` |
| **Scope** | `pipelines/local/queue_share.py`, `pipelines/render.py`, `tests/test_local.py` |
| **Kind** | fix |

## What changed

`queue_missing_summaries` builds a second, uncapped queue and routes papers with
`is_local` to it. Both queues' writes are summed into the reported counts.

## Why

`CLAUDE.md` already states the principle one step earlier:

> A PDF in `inbox/` is kept whatever its keywords say: somebody filing it by
> hand is the editorial decision that scoring exists to approximate.

The pending cap is that same argument at the next stage and was not carrying it.
The cap exists so that a busy collection day cannot produce an unreviewable
backlog. A hand-filed paper is not a busy collection day — it is one paper,
chosen, and usually handed over with a question attached to it.

## What it looked like when it bit

This deployment was handed a paper to read while the queue held 40 tasks. The
ingest reported success: the record was archived, the document written to
`data/pdfs/`, and `run complete` said `'papers': 1, 'queued': 1`. No task was
filed. The only signal was one `WARNING` line naming a task id, sitting among
two dozen identical lines about collected papers.

Everything downstream then behaved correctly and unhelpfully. `render` re-checks
for missing summaries on every pass, so the paper would have been queued
eventually — after the other 26 drained. A person who files a PDF and asks about
it does not mean *eventually*.

## Why a second queue rather than a flag

`Queue`'s cap is fixed at construction and consulted inside `add`. Threading a
per-item exemption through `enqueue`, the summarizer protocol and back would
change a contract four backends share in order to exempt one case. Two queues
over one layout is smaller and the exemption stays legible at the call site.

The cost is that the counters live on the queue objects, so both have to be
summed. That is the trap: reporting `queue.filed` alone would file the task and
report zero, which is exactly the class of silent miscount
[0054](0054-the-queue-reports-what-it-wrote.md) was written about. The test
asserts the sum, not just the routing.

## What it does not change

Collected papers still obey the cap — the test pins that with a collected paper
that stays unqueued in the same render. The definition reserve is untouched. And
nothing here bounds how many hand-filed papers can queue at once: dropping fifty
PDFs into `inbox/` will file fifty tasks. That is the intended reading of the
rule above rather than an oversight, and if it ever becomes a problem the fix is
a separate cap on the inbox, not a shared one.
