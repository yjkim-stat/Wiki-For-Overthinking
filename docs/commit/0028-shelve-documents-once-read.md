# 0028 — The backlog is what is left in `data/pdfs/`

| | |
| --- | --- |
| **Commit** | `feat(render): move a document to data/pdfs/read/ once its reading is applied` |
| **Scope** | `pipelines/common/paths.py`, `pipelines/render.py`, `.gitignore`, `CLAUDE.md`, `README.md`, `docs/API.html`, `tests/test_store.py` |
| **Kind** | feature |

## What changed

`data/pdfs/` now holds only documents still waiting to be read. Once a paper's
reading has been applied, `render` moves its file to `data/pdfs/read/` and
updates `paper.local_path` to match. Clearing a summary moves the file back.

Two things this does **not** change, because they were already true: the inbox
drains on ingest — `local_pdf` has always used `move` rather than `copy`, or the
next run would ingest the same file again — and PDFs have always been
gitignored.

## Why it is built this way

**The backlog becomes a property of the filesystem.** Before this, one
directory held two populations — ingested-but-unread and read-and-applied — and
the only way to tell them apart was to consult the queue. Now `ls data/pdfs/`
answers "what is still owed", which is the question anyone managing the archive
actually asks.

**Self-healing rather than transactional, and this is the load-bearing
decision.** Moving a file and saving a record cannot be made atomic together, so
the interesting question is not how to avoid a crash between them but what the
next run does about one. Every render re-derives where each document belongs
from the single fact that decides it — does a summary exist — and corrects
whatever it finds:

- File moved, record not saved → the file is found at the other path and the
  pointer is repaired.
- Record saved, file not moved → same, in the other direction.
- Neither → nothing happened; the next run does it.

There is no rollback and no journal, because the desired state is a pure
function of data already on disk.

**A missing file is left alone.** PDFs are not committed, so a fresh clone has
records whose documents are simply not there. Rewriting those paths would turn a
known absence into a broken pointer, so the pass skips them entirely — and a
later run that re-fetches the document files it correctly.

**The move runs both ways.** Clearing a summary is the documented way to
re-request a reading, so a withdrawn reading returns its document to the
backlog. Without that, `data/pdfs/` would be *approximately* the backlog, and an
invariant that is approximately true is one nobody can rely on.

**`read/` is a subdirectory of `pdfs/`, not a sibling.** It therefore inherits
the existing gitignore entry. These are the heaviest files the pipeline touches,
and the cost of one deployment ignoring a new top-level directory and forgetting
the other is a repository nobody can clone. Safety by construction beats a line
in a checklist. The `.gitignore` says so explicitly rather than leaving the
inheritance to be noticed.

**No configuration switch.** This is an internal filing convention, not a policy
a deployment needs to tune, and a switch would permit an archive where half the
documents are filed and half are not — which is worse than either state.

## Trade-offs and rejected alternatives

**Rejected: move on `queue complete` instead of on render.** Completion is not
application: a completed task can be reopened and re-answered, and its result
has not yet reached the records. Filing the document at that point would move it
out from under a task that might still be corrected.

**Rejected: leave the file and record the state in the record only.** The record
already knows. The point of the change is that the directory knows too, for
whoever is looking at disk rather than at JSON.

**Cost: `local_path` churns once per paper.** One extra record write per
document, at the render that applies its reading.

**Cost: an archived task's `attachments.pdf_path` goes stale** after its
document is shelved. Archived tasks cannot be reopened, so nothing reads that
path again — but a person grepping an old task file will find a path that has
moved. The paper record is the current answer.

## What a reviewer should check

The crash cases, which are the reason the pass is shaped this way:

```bash
python3 -m unittest tests.test_store -v -k Shelving
```

`test_a_stale_pointer_is_repaired` simulates the move-without-save crash and
asserts the next run fixes it. `test_a_missing_document_leaves_the_record_alone`
is the fresh-clone case — if that ever fails, the pass has started corrupting
records it cannot see the files for. `test_the_pass_is_idempotent` guards
against a run that keeps moving the same file back and forth.

Then confirm the lifecycle end to end: after ingest the file is in
`data/pdfs/`, after the reading is submitted it is still there, and only after
`render` does it appear under `read/` with `local_path` following.

## Downstream impact

No configuration. On the first render after pulling this, every already-read
document moves to `data/pdfs/read/` and its record is rewritten — expect a
one-off diff across `data/papers/` touching only `local_path`.

Anything outside the pipeline that hard-codes `data/pdfs/<id>.pdf` should read
`paper.local_path` instead.
