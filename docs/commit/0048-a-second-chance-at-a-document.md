# 0048 — A second chance at a document

| | |
| --- | --- |
| **Commit** | `feat(backfill): fetch documents for papers already waiting to be read` |
| **Scope** | `pipelines/backfill.py`, `tests/test_backfill.py`, `CLAUDE.md`, `README.md` |
| **Kind** | feature |

## What changed

`python3 -m pipelines.backfill` fetches the document for papers that already have
a reading task pending, no `local_path`, and a `pdf_url` to ask for.

`pdf_fetch` runs inside collection, so it only ever sees papers arriving *this*
run. A paper queued before documents were fetched at all, or on a run where its
host was down, never gets another chance: collection will not offer it again
because `seen.sqlite` remembers it, and nothing else asks. On the archive this
was written for that is **512 unread papers with no document between them** —
every reading in the backlog answered from an abstract, against a rule the same
archive recorded, that a claim resting on a figure is read from the rendered PDF.

This is the first requirement of the dream-mode specification (R1).

## Why it is built this way

**A separate command, not a stage of `run_daily`.** Collection is bounded by what
a day published; this is bounded by what the archive already owes, and the two
numbers have nothing to do with each other. Putting an unbounded backlog behind a
daily cadence means a slow night of backfilling costs a day of collection — the
same split the queue already makes between collecting and reading.

**It collects nothing, scores nothing, queues nothing and reads nothing.** The
only thing it changes about a record is `local_path`, and the only thing that
follows is that the next render puts a path in `attachments.pdf_path`. A test
asserts the negative directly, because a command that fetches documents is one
plausible refactor away from also filing the tasks for them.

**Records are saved one paper at a time, not in a batch at the end.** A pass that
is interrupted keeps every document it paid for, and a re-run skips them. Nothing
here is transactional and nothing needs to be, which is the same self-healing
shape `render.shelve_documents` uses.

**One client for the whole pass**, so the throttle and the give-up circuit apply
across the backlog. That matters more here than in collection: this command asks
one host for hundreds of large files in a row, which is exactly the traffic those
two mechanisms exist to shape.

**Papers that name no PDF are counted, not dropped.** They cannot be helped by
anything mechanical — the answer is a person finding where the document is — so
the count is reported on every run rather than being silently absent from a
number that would otherwise read as "nothing left to do".

### The ordering is not the one the specification asked for

R1 says to order by leverage: the summed source counts of the entities a paper is
evidence for. That is exact, and **undefined for every paper this command can
act on**. Entities take their evidence from summaries; an unread paper has no
summary; so no entity cites it. Every candidate scores zero and the ordering
degenerates to whatever `iter_papers` yields.

What the archive does know about an unread paper is what scoring decided when it
arrived. `leverage()` sums the paper's scores over the topics that *accepted* it,
so a paper several tracked subjects want outranks one a single subject wants
badly. The substitution is named in the function's docstring rather than hidden
behind the word the specification used, and `--by` says `score`, not `sources`,
for the same reason: the flag should not claim a computation the command cannot
do.

The sort key ends in the id in every mode. A bound is applied *after* the sort,
so an unstable order would fetch a different set on each run and the backlog
would drain in no direction at all.

## Trade-offs and rejected alternatives

**`--limit` overrides the configured cap rather than narrowing it.** `--days`
sets the precedent: an explicit number on the command line is a decision, and a
flag silently clamped by a config file is worse than no flag. The consequence is
that `--limit 500` really will ask for 500 documents.

**Considered: ordering by queue age.** Available as `--by age`, not the default.
Fairness to the oldest task is a worse use of a bounded night than relevance —
and the oldest tasks are disproportionately the ones whose host was down, which
is a reason to expect them to fail again rather than to try them first.

**Considered: fetching for papers with no task pending.** Rejected: nobody is
waiting to read them, so it is speculative traffic against a host, and the
record already carries the URL if anyone wants it later.

**It does not extract text.** The specification says not to, and this repository
agrees for its own reasons — `pdf_fetch`'s docstring is explicit that the reader
reads documents, so the figures and tables survive. `data/fulltext/` belongs to a
different fork.

**Nothing reports the backlog except this command.** A deployment that never runs
it has no way to learn that 512 of its readings are abstract-only. That is worth
fixing and is not this commit; `read_from` (note 0044) is the field that will
eventually make it countable.

## What a reviewer should check

- The six properties, each against a deliberate mutation: delete the
  `local_path` guard (re-fetches), the task guard (fetches what nobody is
  reading), the sort key (spends the limit on the wrong papers), the per-paper
  save (buys documents and forgets them), the `unreachable` counter (drops the
  papers a person has to chase), and the `dry_run` branch. Each takes down one or
  two tests and nothing else.
- That `--dry-run` requests nothing *and* writes nothing —
  `test_a_dry_run_requests_nothing_and_writes_nothing` asserts both, because a
  dry run that still saved a record would look identical in the log.
- That `--topic` narrows the `no_pdf_url` count too. Filtering after the scan
  would leave a number that answers a different question from the one beside it.
- `test_running_it_twice_fetches_once`. Re-runnability is the property that makes
  this safe to put in a nightly procedure.

## Downstream impact

New command; nothing existing changes behaviour. A deployment with a long backlog
should expect the first run to be the largest — bound it with `--limit` and read
the `no_pdf_url` count, which is the part no amount of running will reduce.

Documents fetched here are not attached to their tasks until the next
`python3 -m pipelines.render`, which is where `attachments.pdf_path` is written.

## Correction (0052)

> "the only thing that follows is that the next render puts a path in
> `attachments.pdf_path`"

That was false when written. `Queue.enqueue` refused to touch a task that
already existed, so the correct task was rebuilt on every render and discarded
on every render — and every paper this command can help is by definition one
that was already queued. Measured on the archive it was written for: 224
documents fetched, `0 of 512` pending tasks carrying a `pdf_path`.

Fixed in [note 0052](0052-a-task-is-a-function-of-its-record.md), which makes a
waiting task track the record it was built from. The sentence above is true from
that commit onward.
