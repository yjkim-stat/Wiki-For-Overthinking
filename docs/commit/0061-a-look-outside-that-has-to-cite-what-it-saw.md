# 0061 — A look outside that has to cite what it saw

| | |
| --- | --- |
| **Commit** | `feat(enrich): a lookup task, and the reference every answer owes` |
| **Scope** | `pipelines/enrich/lookup.py`, `pipelines/enrich/queue.py`, `pipelines/enrich/apply.py`, `tests/test_lookup.py`, `CLAUDE.md` |
| **Kind** | feature |

## What changed

A fifth task kind, for the questions that are *confirmation* rather than
judgement: how a name is spelled where it was published, whether two names are
one thing, where a paper's PDF lives, whether there is published code.

```bash
python3 -m pipelines.enrich.lookup add --subject spelling --about "C-LAP"
python3 -m pipelines.enrich.lookup add --subject document --paper arxiv:2401.12345
```

Requirement R4, and it sits directly on the reference records from
[note 0049](0049-a-citation-rather-than-a-rumour.md).

## Why it is built this way

**Every answer must cite a recorded reference, and that single rule is the
feature.** A reference carries a URL, a retrieval date and the passage relied
on. Requiring one is the only way this pipeline can distinguish *I looked this
up* from *I remember this* — it calls no model and reaches no network, so there
is no other check available. On a question whose entire value is that somebody
went and looked, that distinction is the thing being bought.

**`unknown` is always available and is the one answer needing no reference.** A
lookup that failed is worth recording: the next session sees what was tried
rather than starting from nothing. Refusing it would push a reader towards
inventing an answer, which is precisely the failure the reference rule guards
against — a validator that leaves only one acceptable answer has stopped
validating and started dictating.

It still needs a `rationale`. "Unknown" with no account of what was tried is
indistinguishable from nobody having looked.

**A confirmed identity or spelling writes nothing.** It files a definition
revision for the entity, and the alias goes in through the validator that owns
aliases with a reader looking at it. This is the rule `CLAUDE.md` already
states about hand-editing `data/`, and the reason is worth repeating: an alias
is a merge mechanism, and a wrong merge does not mislabel an entity — it fuses
two, and the fused note looks perfectly healthy afterwards. The revision reuses
the machinery from [note 0058](0058-a-stale-definition-is-asked-for-again.md),
so the reader sees the existing definition rather than a blank page.

**A document answer writes one field, and only into a blank.** A `pdf_url` is
checkable and inert until `pipelines.backfill` acts on it. A paper that already
names a document is left alone: the reader was answering *where is it*, not
*which is better*.

**An artifact answer needs no application at all.** Its result is the reference,
and the validator already refused the answer unless that reference exists.

**Subject-specific checks happen at submission.** A `document` answer must be an
http(s) URL and an `identity` answer must be yes or no, because both are
checkable and a wrong one is silent later — a non-URL in `pdf_url` fails at fetch
time, days afterwards, in a different command.

## Trade-offs and rejected alternatives

**`validate_result` now takes five context arguments** — topics, attachments,
cfg, store, payload. Each was added for the same reason and each is documented,
but the list has outgrown the shape: they are all facts about the *task*, and
they should be one `task` parameter. That refactor touches every caller and
belongs in its own commit; it is named here rather than left to be rediscovered.

**Considered: letting a confirmed identity write the alias directly.** It is one
line, the answer has already been validated, and it is the one thing this
repository is most careful never to do. The cost of being wrong is not
recoverable by editing.

**Considered: filing lookups automatically** — for the 285 papers with no
`pdf_url`, or for slugs a duplicate report flags. Deliberately not done here.
The reader's night is the scarce resource and an auto-filled backlog of
confirmations would consume it; the report and the queue should meet through a
person deciding which are worth asking.

**Nothing verifies that the cited reference actually supports the answer.** It
must exist and it must be recorded; whether its `quoted` passage says what the
answer claims is a reading, and the pipeline cannot do readings.

## What a reviewer should check

Four mutations, each taking down its own tests: accept an answer with no
reference, accept `unknown` with no rationale, overwrite a `pdf_url` that is
already there, and have the applier write the alias itself.

- `test_an_answer_with_no_reference_is_refused` is the feature.
- `test_a_confirmed_identity_never_writes_an_alias` and
  `test_a_confirmed_identity_asks_for_the_definition_again` are a pair: the
  first says what must not happen, the second says what happens instead. Either
  alone is satisfiable by broken code.
- `test_an_unknown_answer_changes_nothing_and_still_counts` — counted as applied
  rather than skipped, because a recorded failure is a result.

## Downstream impact

New task kind and a new command; nothing existing changes. `validate_result`
gains a `payload` parameter defaulting to `None`, so every existing caller
behaves as before, and `apply` skips unknown kinds with a warning as it already
did — an older reader draining a queue that contains a `lookup` will not fail.
