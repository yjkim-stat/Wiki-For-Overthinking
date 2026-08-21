# 0096 — A task says when its record is contested

| | |
| --- | --- |
| **Commit** | `fix(enrich): a reading task warns when its record shares an identifier` |
| **Scope** | `pipelines/enrich/dedupe.py`, `pipelines/common/llm.py`, `pipelines/render.py`, `tests/test_contested_task.py` |
| **Kind** | fix |

## What changed

[Note 0059](0059-an-identifier-learned-late-is-still-registered.md) reports two
records claiming one identifier on every render. It reports to **whoever ran the
render**. The person who then drains the queue is often not that person and is
always looking somewhere else — and reading such a paper can be exactly the
wrong move.

A paper task whose record is in a conflict now says so, names the other record,
and says what reading it would cost.

## Why it is built this way

**Measured, and it nearly happened.** On a live archive `arxiv:2503.20314` sat
pending *with its PDF* while `local:94a3…` already held the reading. Reading it
would have produced a second summary of one paper, counted twice in every entity
citing it. A session skipped it by hand and **the queue recorded nothing about
why**, so the next night's run had no way to know — which is a defect in this
repository, not in that session.

**A warning, not a refusal.** The reading is not always wrong: if neither record
has been read, reading either is fine, because
[a merge](0064-a-merge-with-a-person-in-it.md) carries the summary to whichever
record survives. It is wrong only when the other record has one already, and the
reader can check that from the task. Withholding the task would strand a paper
nobody had read behind a decision nobody was making.

**It rides on tasks tracking their records.** Since
[note 0052](0052-a-task-is-a-function-of-its-record.md) a pending task is rebuilt
from its record every render, so a conflict that arises *after* a task was filed
reaches it on the next pass with no extra machinery. A test asserts exactly that.

**`reconcile_identifiers` now returns who, not just how many.** The count
answered an operator's question; the pairs answer the reader's.

## Trade-offs and rejected alternatives

**Considered: not filing the task at all while contested.** Simpler and wrong in
the common case — a contested pair where neither side has been read would then be
unreadable until somebody merged, and merging is a decision that can wait.

**Considered: deciding for the reader** by checking whether the other record has
a summary and refusing only then. That is knowable here, and it was left to the
reader on purpose: the interesting case is a *partial* reading, or a summary
that is wrong, and a rule that hides the task hides the judgement too.

**The warning names one other record**, not all of them. A three-way collision
would report the first found. Three-way collisions have not been seen; two-way
ones have.

## What a reviewer should check

Four mutations, each taking down four tests: stop recording which records
conflict, drop the warning from the instructions, empty the warning text, and —
**the one worth repeating** — stop passing the conflict to the *second* queueing
pass.

That last is not hypothetical. `render` files reading tasks twice, the second
time to release a reserve held back for the wiki, and the first version of this
change wired only the first call. The task was filed by the second and carried
no warning. The test caught it; reading the code had not.

## Downstream impact

Paper tasks gain a `contested_with` payload field, empty for every record not in
a conflict, and contested ones gain a section in their instructions. An archive
with no duplicate identifiers sees no change.
