# 0022 — Fetch the document before asking anyone to read it

| | |
| --- | --- |
| **Commit** | `feat(collect): fetch a paper's PDF so the reader gets the paper, not its abstract` |
| **Scope** | `pipelines/collect/pdf_fetch.py`, `pipelines/run_daily.py`, `pipelines/common/llm.py`, `config/settings.yaml`, `CLAUDE.md`, `tests/test_pdf_fetch.py` |
| **Kind** | feature |

## What changed

A paper that has cleared scoring and is about to be queued gets its PDF
fetched into `data/pdfs/`, and the task carries `attachments.pdf_path` — the
same field a hand-filed PDF already used. The paper prompt, when a document is
attached, tells the reader to take `results` and `limitations` from the
experiments section rather than the abstract's framing.

PDF fetching has its own client with a slower floor, its own cap per run, and
its own enable switch under `collect.pdfs`.

## Why it is built this way

An abstract is a claim about a paper, not a record of it. It reports the
headline and rarely the condition under which the headline fails. Measured in a
field archive: **38% of records built from abstracts had an empty `results`
field**, because the abstract carried no numbers to record. Reading bodies
overturned substantive findings — a transfer result that holds only below a
capacity threshold, a headline worse than baseline on three of five real tasks,
a "1 FPS, 16 frames of memory" limitation absent from an abstract that reads as
an interactive simulator.

**The document is handed over, not extracted.** The issue report proposed
running PDFs through `pdftotext` and caching the text. That is not needed here
and costs something real. `local_pdf.py`'s docstring already names the reason
its collector does not open PDFs: *this repository already has a reader that is
good at documents*. That reader reads PDFs directly — figures, tables and all —
and a result table settles what a paper achieved faster than any prose. Text
extraction would discard exactly the part that carries the answer, in exchange
for an external binary dependency the template would have to document, degrade
around, and explain to every deployment.

**This corrects the issue report's premise.** It argues that upstream's task
"gives the reader a file path to a PDF it cannot open", so the hand-filed path
is broken without extraction. That is not true of this repository: `CLAUDE.md`
already instructs the reader to open `attachments.pdf_path` and look at the
figures, and it works. The real gap was the opposite one — *remote* papers,
where the reader had only an abstract and a URL. So the fix is to give remote
papers what hand-filed ones already had, rather than to take the document away
from both and give them text.

**No structured extraction, which is upstream's line and stays.** Nothing here
parses a title, an author list or a year out of a document. The fetcher moves
bytes; every structured field still comes from an index or from a reader who
looked at the page.

**A body served with a 200 is checked for `%PDF-`.** A paywall answers with a
login page and a success status. Storing it would hand the reader a document
that says nothing about the paper, which is worse than handing them nothing.

**PDF hosts get their own politeness budget.** They are the same hosts the
metadata APIs throttle, and a body is a far larger ask than a query. A shared
interval would let document fetching spend the budget the queries need. Default
floor is 5s against the metadata client's 0–3s.

**Failure is ordinary and must stay ordinary.** No `pdf_url`, an unreachable
host, a paywalled venue, the circuit breaker having given up: the paper keeps
its abstract-only task and the run continues. About one paper in twelve has no
obtainable PDF. The fetch is also wrapped at the call site so that no failure
can cost a reading.

## Trade-offs and rejected alternatives

**Rejected: `pdftotext` extraction with `data/fulltext/` caching.** See above —
loses figures and tables, adds an external binary, and solves a problem this
repository's reader does not have.

**Rejected: fetch during collection, before scoring.** Would download the
document for every candidate, including everything scoring rejects. Fetching
after acceptance means the archive downloads what it is about to read.

**Cost: disk.** `data/pdfs/` grows by roughly one paper-sized file per accepted
paper. It is gitignored — a PDF is re-fetchable input rather than an output, and
committing paper bodies to a template repository that gets copied is a
redistribution question nobody needs to inherit.

**Cost: runs get slower.** A 5s floor and up to 40 documents is a few minutes
added to a busy run. `enabled: false` or `max_per_run: 0` turns it off.

**Cost: a partially-fetched archive is now possible.** Some papers have their
document and some do not, so two readings of comparable papers may not be
comparable in depth. The prompt differs between the two cases, which at least
makes it visible in the task rather than silent.

## What a reviewer should check

That every failure mode still produces a task:

```bash
python3 -m unittest tests.test_pdf_fetch -v
```

`test_a_login_page_is_not_stored_as_a_paper` is the one worth reading — a 200
response is not proof of a document. `test_a_hand_filed_pdf_is_never_refetched`
guards the other direction: an inbox PDF is the original and there is nothing
better to download.

Then confirm no structured field derives from a fetched file — `pdf_fetch.py`
should contain no parsing at all, and `_apply_bibliography` should still be
reachable only for `paper.is_local`.

## Downstream impact

`config/settings.yaml` gains a `collect.pdfs` block. A deployment that does not
want document fetching sets `enabled: false` and is back to previous behaviour.

Expect `data/pdfs/` to grow and runs to lengthen. Expect paper tasks to start
carrying `attachments.pdf_path`; a reader that ignored that field for remote
papers will now find a document there.

`CLAUDE.md` changed how it distinguishes the two kinds of PDF task: both now
carry `attachments.pdf_path`, so the marker for a hand-filed one is that its
schema asks for `bibliography`.

This resolves the conflict described in the deployment's issue 0012 in the
opposite direction from its proposal: the boundary upstream drew — no structured
extraction — is kept, and no extraction of any kind is added.
