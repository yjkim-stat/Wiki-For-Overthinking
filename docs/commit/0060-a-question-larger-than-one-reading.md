# 0060 — A question larger than one reading

| | |
| --- | --- |
| **Commit** | `feat(enrich): a synthesis task, and the finding it becomes` |
| **Scope** | `pipelines/enrich/synthesis.py`, `pipelines/enrich/queue.py`, `pipelines/enrich/apply.py`, `tests/test_synthesis.py`, `CLAUDE.md`, `README.md` |
| **Kind** | feature |

## What changed

A fourth task kind. The queue had a paper, a talk and an entity, and each is one
record answered from its own material — but the work that moves an archive
forward is the other shape: *read these twelve and tell me whether X*. There was
nowhere to put it, so it happened inside a session, was validated by nothing,
could not be handed to the next night, and survived only in a commit message.

```bash
python3 -m pipelines.enrich.synthesis add \
  --question "Do these agree on what an instrumental variable requires?" \
  --concept instrumental-variable --paper arxiv:2401.12345
```

Requirement R2 of the dream-mode specification.

## Why it is built this way

**A settled synthesis is a finding, through the recorder that owns findings.**
`_apply_synthesis` calls `findings.record`; there is no second path into
`data/findings/`. That matters more than it looks — the queue has already
checked the answer, and routing it around the recorder afterwards would leave
two ways in, one of which nobody maintains.

**The answer is checked as the finding it will become, at submission.**
`validate_result` gains `cfg` and `store`, exactly as it gained `topics`
(note 0016) and `attachments` (note 0044), and for the same reason: whether a
statement names a paper the archive holds is a fact about the archive, not about
the answer. Without them only the shape is checked, which is the same graceful
degradation and the same stated limit.

**Leaving a question open is a real answer.** The evidence often does not settle
things, and a task that demanded a statement would be asking the reader to
invent one. An answer may instead say in `unresolved` what is missing and what
would settle it; nothing is written to `data/findings/`, the task is archived
carrying its reason, and the run counts it as applied rather than skipped. A
sentence hedged until nobody could disagree with it is worse than an open
question, because nothing later can tell the two apart.

**Saying neither is refused**, and that is the only shape of silence there is.

**Evidence is resolved when the question is filed, not when it is answered.** A
question naming a paper the archive does not hold would be answered from memory,
which is the thing this whole arrangement exists to prevent. The excerpt of each
record travels in the task, so the reader meets the archive's own words first.

**Content-addressed on the question**, so a session leaving one for the next
night cannot accumulate duplicates of its own asking.

## Trade-offs and rejected alternatives

**Render does not file these automatically.** The specification suggests one
trigger — an entity promoted on evidence that contradicts itself — and nothing
in the pipeline can detect a contradiction; that is a reading. Implementing a
proxy for it (evidence count, source disagreement about `kind`) would file
questions that are not the question, and the reader's night is the scarce
resource here. Filing by hand covers the specification's other two paths, which
are the same command. **This is the one part of R2 not delivered**, and it is
deferred rather than approximated.

**`Queue` now optionally carries a `Config`.** It is used for nothing but this
validation. The alternative — validating fully at apply time — accepts a bad
answer, archives the task, and fails during a render, which is exactly the
inversion the queue's validator exists to avoid.

**The `synthesis` kind has no unconditionally required field.** `_REQUIRED_FIELDS`
carries an empty list for it, and the alternative is enforced in
`_check_synthesis`, because "either a statement or a reason there is none" is not
a shape that table can express.

## What a reviewer should check

Four mutations, each taking down its own tests: skip the findings validator (a
statement citing a paper nobody collected is accepted), accept an answer with
neither statement nor reason, write a finding for an unresolved answer, and file
a question against evidence the archive lacks.

- `test_an_answer_is_checked_as_the_finding_it_becomes` is the one that keeps
  this from becoming a back door.
- `test_an_open_answer_records_no_finding` asserts both halves: nothing written,
  and counted as applied rather than skipped.
- `test_the_open_question_and_its_reason_survive` — the archived task is where
  the next session picks the question up.

## Downstream impact

New task kind. A deployment sees nothing until somebody files a question; the
three existing kinds are unchanged, and `validate_result`'s two new parameters
default to `None`, so every existing caller behaves as before.

An archive whose queue is drained by an older version of the reader will see a
`synthesis` task it does not recognise. `apply` skips unknown kinds with a
warning rather than failing, which is the existing behaviour.
