# 0070 — One leverage, beside the scores it sums

| | |
| --- | --- |
| **Commit** | `refactor(enrich): move leverage to the module that computes the scores it sums` |
| **Scope** | `pipelines/enrich/score.py`, `pipelines/backfill.py`, `tests/test_score.py` |
| **Kind** | refactor |

> This note is numbered from a block — 0070 onward — reserved for work done in
> parallel with another session holding 0058 onward. The gap is deliberate and
> is not a missing note.

## What changed

`leverage()` moved from `pipelines/backfill.py` to `pipelines/enrich/score.py`.
Nothing about what it computes changed. `backfill` imports it and re-exports it,
so `backfill.leverage` still resolves and every existing caller is untouched.

It is also now stated to work on any record carrying `topics` and `scores` — a
`Paper` or a `Video` — because the next commit orders a queue that holds both.

## Why it is built this way

**A second caller was about to be a second copy.** The work queue needs the same
number, and the queue lives under `enrich/` while `backfill.py` sits at the top
level and imports `enrich.queue`. Importing the other way round is a cycle, so
the choices were to move the function or to write it again. Two copies of "which
topics count" would be free to disagree, and the disagreement would surface as a
backfill and a queue draining in different orders with nothing to say which was
right — the same argument [note 0055](0055-one-rule-for-what-counts-as-a-mention.md)
makes about what counts as a mention.

**`enrich/score.py` rather than `common/schema.py`.** The function's whole
content is a judgement about scoring: that `topics` (accepted) is the right set
and `scores` (everything that passed the hard rules) is not, and that breadth
across tracked subjects beats depth in one. That judgement belongs next to the
code that produced both fields. `schema.py` is deliberately thin — flat records
and dict conversion — and putting a scoring rationale inside it would put the
argument somewhere nobody reading about scoring would look.

**Not a property on `Paper`.** `Paper.best_score` is the precedent and it was
tempting, but a property would have to be defined twice to cover `Video` as well,
which is the duplication this commit exists to avoid.

**The long docstring moved with it, verbatim in substance.** It records that this
is a deliberate substitution for the leverage the specification asked for, not an
approximation of it: entity source counts are exact and undefined for anything
unread, because entities take their evidence from summaries. A reader who finds
the function in its new home needs that paragraph more than the old caller did,
since there are now two callers with different reasons to want it.

## Trade-offs and rejected alternatives

**A re-export is a second name for one thing**, and someone may reasonably think
`backfill.leverage` is defined there. It is kept because `backfill`'s dry-run log
prints the number and because removing the name would make this refactor a
breaking change to a module's public surface for no gain. The import line says
where it lives.

**Considered: a new `pipelines/common/leverage.py`.** Rejected as a module with
one four-line function in it and no second occupant in sight. `enrich/score.py`
is where somebody looks for "what did scoring decide about this item".

**Considered: leaving it in `backfill.py` and having the queue import it.**
That is the import cycle above — `backfill` → `enrich.queue` → `backfill` — and
Python would have failed at import time rather than quietly.

## What a reviewer should check

- Two mutations, in `leverage` itself:
  - `sum(...)` → `max(...)` takes down three tests:
    `tests.test_score.LeverageTests.test_breadth_across_topics_beats_depth_in_one`,
    `test_a_video_is_read_the_same_way`, and the pre-existing
    `tests.test_backfill.BackfillTests.test_a_paper_wanted_by_two_topics_outranks_one_wanted_badly`
    — which is the point: the old caller's test still guards the moved function.
  - summing `record.scores.values()` instead of the accepted `topics` takes down
    `test_a_score_from_a_topic_that_did_not_accept_it_is_not_counted` and
    `test_an_item_no_topic_accepted_scores_zero`. That mutation is the plausible
    one: `scores` is the fuller-looking field and it is the wrong one.
- That `tests/test_backfill.py` is unchanged by this commit. It calls
  `backfill.leverage` and still passes, which is the evidence that the
  re-export works.

## Downstream impact

None. No command, no config, no record changes. A deployment pulls the code and
`python3 -m pipelines.backfill` behaves identically, including its ordering.
