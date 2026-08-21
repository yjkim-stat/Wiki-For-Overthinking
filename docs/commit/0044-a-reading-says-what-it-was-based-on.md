# 0044 — A reading says what it was based on

| | |
| --- | --- |
| **Commit** | `feat(enrich): a reading records whether it read the document` |
| **Scope** | `pipelines/common/schema.py`, `pipelines/common/llm.py`, `pipelines/enrich/queue.py`, `pipelines/enrich/apply.py`, `tests/test_reading_basis.py` |
| **Kind** | feature |

## What changed

`PaperSummary` gains `read_from`, holding `"document"`, `"abstract"` or empty.
A paper task that attaches a PDF now asks for it and the queue refuses a result
that does not answer; a task that attaches none does not ask, and the applier
records `"abstract"` without troubling anybody for it.

The question this makes answerable is *which of these readings actually opened
the paper* — which, before this, was recoverable only by parsing every file in
`data/queue/archive/` and was displayed nowhere at all.

## Why it is built this way

A summary written from an abstract and one written from the paper are the same
shape, carry the same authority in every artifact built on them, and are not
worth the same. The abstract reports a paper's claims and rarely the condition
under which they fail. A wiki definition drawn from ten readings is a different
object depending on how many of them were abstracts, and nothing could say.

**The reader is the only witness, so the reader is asked.** Nothing in the
pipeline can observe whether a PDF was opened. Inferring it from the file's
presence is what the old arrangement effectively did — `shelve_documents` moves
a paper to `data/pdfs/read/` on the strength of a summary existing, which says
the document was *available*, not that it was *used*.

**What can be checked is checked, in the one direction it works.** A reading
cannot have been based on a document that was never attached, so that claim is
refused. The opposite claim — admitting the abstract when a PDF was there —
cannot be verified and is accepted without complaint, deliberately: the point is
to know, and a reader pushed into claiming otherwise leaves a record nobody can
find again. The prompt says this in as many words.

**The validator is given the task, following note 0016.** `validate_result`
already took `topics` for the same reason — a claim the answer makes about
itself has to be checked against what was handed over, and a validator that
cannot see the task cannot tell a true claim from a false one. `attachments` is
passed as stored, so `None` (no context), `{}` (a task that carried no document)
and a block with `pdf_path` are three distinct states rather than two.

**Empty is a third state and stays one.** A reading applied from a task that
predates this field could have been either, and defaulting it to `"abstract"`
would make an unasked reading indistinguishable from a reader who said so. That
distinction is the whole value of the field, so unknown is recorded as unknown.

## Trade-offs and rejected alternatives

**Existing pending tasks in live deployments will be rejected.** Validation is
by kind, not by the schema stored in the task, so a task queued before this
change that attached a PDF now needs `read_from` on submission. The task itself
does not say so — its stored `output_schema` predates the field. The error names
the field and both values, and re-queueing is not required, but a deployment
draining an old backlog will hit it. This is the cost of validating against one
contract rather than per-task ones, and per-task validation would mean a queue
whose rules are as old as its oldest task.

**Nothing displays it yet.** No renderer reads `read_from`; the archive page,
the wiki and the reports are unchanged. Recording first is deliberate — a
display built on a field that is empty for every existing record shows a column
of blanks and reads as a bug in the renderer.

**Considered: inferring the basis from `local_path`.** Free, no reader
involvement, and wrong: it records what was available. The gap between available
and used is the entire thing being measured.

**Considered: a boolean `read_full_text`.** Rejected because it has no third
state, and the unknown case is the majority of every existing archive.

**Considered: making it required for every paper task.** A task with no document
gives the reader no choice, so asking would be asking them to restate the task.

**Not done: a `full_text` value.** A fork of this repository extracts PDF text
and would want to distinguish reading the extraction from reading the document.
Nothing here extracts text, so a third value would be one this repository cannot
produce. `READING_BASIS` is the one place to add it.

## What a reviewer should check

- That each rule bites. Four mutations, each taking down exactly one test:
  pass `None` instead of `task.get("attachments")` in `complete`; drop the
  `READ_FROM_SCHEMA` update in `_paper_schema`; make `_reading_basis` return
  `"abstract"` unconditionally; delete the "never given" branch.
- That the three attachment states really are three:
  `test_without_the_task_only_the_value_is_checked` against
  `test_no_document_means_nothing_to_ask`. Collapsing `None` and `{}` makes both
  pass individually and the pair meaningless.
- That an old record still loads:
  `test_an_older_record_without_the_field_still_loads`.
- That the prompt asks only where a document exists:
  `python3 -m pipelines.enrich.queue show <id>` on a task with and without one.

## Downstream impact

**Adding the field is safe** — `from_dict` defaults it, so existing summaries
load and read as unknown. Nothing is regenerated differently, because nothing
renders it.

**Draining an existing backlog is not.** A pending task that attached a document
will be refused until its result carries `read_from`. Answer with `"document"`
or `"abstract"` as the case actually is; do not re-queue to avoid the question,
because a re-queued task loses the reading that was already done.
