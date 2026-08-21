# 0065 — The validator takes the task

| | |
| --- | --- |
| **Commit** | `refactor(enrich): the result validator takes the task, not five pieces of it` |
| **Scope** | `pipelines/enrich/queue.py`, `tests/test_queue.py`, `tests/test_reading_basis.py` |
| **Kind** | refactor |

## What changed

```python
-def validate_result(kind, result, topics=None, attachments=None,
-                    cfg=None, store=None, payload=None)
+def validate_result(kind, result, task=None, *, cfg=None, store=None)
```

No behaviour changes and no caller's result moves; the suite is identical either
side. This is the tidy-up [note 0061](0061-a-look-outside-that-has-to-cite-what-it-saw.md)
named rather than left to be rediscovered.

## Why it is built this way

**They were always one thing.** `topics`, `attachments` and `payload` are each a
fact about *the task*, and each was added by a different note for the same
reason: an answer cannot be checked against itself. A paper's `relevance` naming
a slug the task does not have renders nowhere. A reading claiming `read_from:
"document"` when none was attached is a claim only the task can refute. A lookup
answering with a bare string is wrong only if the task asked for a URL.

Three notes, three parameters, and by the fifth the shape was the argument list
rather than the idea. Passing the task says what the rule actually is.

**`cfg` and `store` did not move into it**, and are now keyword-only. They are
the archive, not the task — what makes a synthesis answer checkable as the
finding it becomes. Collapsing them in would have made `task` mean "everything
the validator might want", which is not a thing.

**A stale caller fails loudly.** The third positional was a list and is now a
dict; passing the old shape raises `AttributeError` on `task.get`, immediately,
rather than silently validating against nothing. That is why the parameter was
replaced rather than added alongside — an overload accepting both would have let
a missed call site keep passing while checking less.

**The three-state distinction survives inside the task.** An absent
`attachments` key still means no context and an empty one still means a task
that carried no document, which is the difference between "cannot say" and
"nothing was attached". A test asserts each separately.

## Trade-offs and rejected alternatives

**Nineteen test call sites were rewritten mechanically**, by splitting each
call's arguments and rebuilding it. They were reviewed as a diff rather than
individually; the suite passing at the same count either side is the evidence
the rewrite was faithful.

**Considered: keeping the old parameters as deprecated aliases.** It would have
avoided touching the tests and left two ways to call one function, one of which
nobody would maintain — the same argument note 0064 makes about two paths into
`data/findings/`.

**`validate_result` still takes `kind` separately** although the task carries
it. Callers that have a kind and no task — most of the tests, checking a shape —
would otherwise have to invent one.

## What a reviewer should check

- That each context is still consulted: setting `topics`, `attachments` or
  `payload` to `None` after unpacking takes down two or three tests each. All
  three were run.
- That the diff to `queue.py` is a signature, an unpack and a docstring, with no
  change to any rule below it.
- The test count: 711 before and after.

## Downstream impact

`validate_result` is internal to the queue. `Queue.complete` is the only
production caller and passes the task it already had. A deployment sees no
difference in what is accepted or refused.
