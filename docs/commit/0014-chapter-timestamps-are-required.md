# 0014 — A chapter timestamp is required, not defaulted

| | |
| --- | --- |
| **Commit** | `fix(queue): require a real start_s on every submitted chapter` |
| **Scope** | `pipelines/enrich/queue.py`, `pipelines/common/llm.py`, `tests/test_queue.py` |
| **Kind** | fix · breaking (contract) |

## What changed

`validate_result` now rejects a video chapter with no `start_s`, and rejects a
boolean one.

The check read `isinstance(chapter.get("start_s", 0), (int, float))`. The
default meant a chapter object with no `start_s` at all substituted `0`, which
is a number, so the check passed and the missing value rendered as a real
timestamp. A seminar page showed several chapters all starting at `0:00`, and
nothing had failed.

The task instructions in `llm.py` now say the field is required, and say what to
do when the transcript does not supply one.

## Why it is built this way

A chapter exists so a reader can jump to it. A chapter with a wrong timestamp is
worse than no chapter — it costs the reader the trip and their trust in the rest
of them — and `0:00` is the worst possible wrong value, because it is
indistinguishable from a legitimate first chapter. There is nothing to notice.

This is the same principle the reading instructions already state for paper
fields: leave it empty rather than invent it. The validator was quietly doing
the opposite, manufacturing a plausible value for a field the submitter had not
answered. Presence and validity are separate questions and the check now asks
them separately.

`bool` is excluded explicitly because it is a subclass of `int`, so `start_s:
true` satisfied an `isinstance` check against `(int, float)`. The form matches
the one already used for `bibliography.year` a few lines above, rather than the
three-branch version in the issue report — the file already had an idiom for
this exact problem.

An explicit `0` stays valid. It is a legitimate first chapter, and a fix that
rejected it would trade a silent wrong value for a loud wrong rejection. An
empty `chapters` list also stays valid: it is the documented answer for a video
with no transcript.

**The instructions changed with the validator.** A stricter contract that only
exists in the validator produces rejections the submitter cannot anticipate.
`llm.py` now states the requirement and resolves the case it creates — omit the
chapter rather than guess a timestamp — so the rule arrives with the task rather
than with the rejection.

## Trade-offs and rejected alternatives

**Rejected: default to `0` but flag it downstream.** Moves the problem to a
renderer that has no way to distinguish a manufactured zero from a real one,
which is the whole difficulty.

**Rejected: drop chapters missing a timestamp instead of rejecting.** Silently
discards work; a rejection tells the submitter what to fix, which is the point
of validating submissions at all.

**Cost: the contract is stricter, and existing stored summaries are not
revalidated.** Chapters already written with a manufactured `0:00` stay as they
are. This fixes what arrives, not what has landed — a revalidation pass over
stored summaries is a separate change with its own migration question.

## What a reviewer should check

The three cases that must not collapse into each other:

```bash
python3 -c "
from pipelines.enrich.queue import validate_result
v = lambda c: {'one_liner':'x','abstract':'y','key_points':['z'],'chapters':c}
print('missing:', validate_result('video', v([{'title':'t'}])))
print('bool   :', validate_result('video', v([{'title':'t','start_s':True}])))
print('zero   :', validate_result('video', v([{'title':'t','start_s':0}])))"
```

Expected: an error, an error, and `[]`. The third is the one a careless fix
breaks.

## Downstream impact

**The contract becomes stricter.** Any backend or session that emits chapters
without timestamps will start getting rejections, which is the point — a
rejection is recoverable, a plausible wrong timestamp is not. Existing stored
summaries are not revalidated and are unaffected.
