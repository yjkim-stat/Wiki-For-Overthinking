# 0016 — A paper's `relevance` is checked against the topics it has

| | |
| --- | --- |
| **Commit** | `fix(queue): validate relevance keys against the task's topics` |
| **Scope** | `pipelines/enrich/queue.py`, `tests/test_queue.py` |
| **Kind** | fix · breaking (contract) |

## What changed

`validate_result` takes an optional `topics` argument — the task's own topic
list — and `Queue.complete` passes it. For a collected paper, `relevance` must
now name exactly those topics, with no blank entries.

Before, the only check was that `relevance` was a dict. `paper_instructions`
tells the reader it must hold one entry per matched topic slug, and the task
carries the list, but the validator never saw it. Three failures all passed: a
key naming a slug the task does not have (renders nowhere), a missing entry for
one it does (topic page with no rationale), and an entry present but blank.

## Why it is built this way

`relevance` decides which topic page a paper renders under, so a wrong key is
structural rather than cosmetic. It is also invisible from inside the record —
everything about the submission is well-formed, and only a comparison against
the task reveals the mismatch. That is exactly the class of error a validator
exists for, and it was the one thing the validator could not see because the
comparison target was never passed in.

`topics` is optional so the two-argument signature keeps working for other
callers and for tests. Without it the validator is blind, as before — which is
the honest behaviour, since there is nothing to compare against.

**Two kinds of paper, and only one of them is authoritative here.** This is the
part the issue report did not account for, and applying its fix as written broke
three existing tests for good reason.

A collected paper was scored, so the task's topics *are* the answer and coverage
can be required. A hand-filed PDF is the opposite case: its task carries **every
tracked topic**, because which ones the document belongs to is the reader's
question rather than the collector's — the list is a menu, not an assignment.
Requiring coverage against it would demand a rationale for every topic the group
tracks. Requiring coverage against the reader's own answer is wrong too, for a
subtler reason: that answer is provisional, filtered against the real topic list
when it is applied, and `test_unknown_topic_slug_is_dropped` exists precisely
because a reader may name a slug that turns out not to exist. Forcing them to
justify it first would break a supported path.

So coverage is required only where the topics are settled. A key outside the
paper's topics is rejected in both cases, because it renders nowhere whoever
chose them.

**`tags` stays unvalidated**, deliberately. An empty `tags` costs nothing; a
wrong `relevance` key costs the paper its place on a topic page.

## Trade-offs and rejected alternatives

**Rejected: require coverage for hand-filed PDFs too.** The version in the issue
report. It rejects the reader's own valid answers and makes `topics: []` — the
documented "belongs to no topic" reading — unexpressible without also inventing
relevance text.

**Rejected: validate relevance at render time instead.** Later, quieter, and by
then the reader has moved on. A rejection at submission is answerable.

**Cost: a hand-filed PDF's relevance coverage is not checked at all.** A reader
can assign three topics and write relevance for one. That gap is real, and is
the price of not blocking the provisional-answer path.

## What a reviewer should check

The blindness-without-topics case first, since it guards every other caller:

```bash
python3 -m unittest tests.test_queue -v -k Relevance
```

`test_without_topics_the_validator_is_blind_as_before` must pass, or this change
has reached further than intended. Then check that the three
`ApplyBibliographyTests` hand-filed cases still complete — they submit no
`relevance` at all, and they are the ones that caught the over-strict first
attempt.

## Downstream impact

**Stricter contract for new submissions on collected papers.** A reader who
omits a topic's rationale, or names a topic the paper was not collected for,
now gets a rejection naming the slug. Hand-filed PDFs are unaffected.

Stored summaries are not revalidated. A deployment that wants to know whether it
already holds malformed records can compare each stored summary's `relevance`
keys against its paper record's `topics` in a few lines.
