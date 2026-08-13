# A queued task never learns that its document arrived

**Status:** solved 2026-08-14 by **option A** — see [Resolution](#resolution) at
the foot of this file and [note 0052](../commit/0052-a-task-is-a-function-of-its-record.md).
**Kind:** fix
**Found:** 2026-08-13, on the first real use of `pipelines.backfill`
**Touches:** `pipelines/enrich/queue.py`, `pipelines/common/llm.py`, `pipelines/render.py`, `tests/`

`backfill` exists so that a paper queued before documents were fetched gets a
second chance at one. It works: on the archive it was written for, 224 of 225
documents arrived and the records now point at them.

The reader never sees any of them. A task filed before the document existed is
still on the queue with the attachments it was filed with, and `enqueue` refuses
to touch a task that already exists — so the whole point of the fetch stops one
step short of the person it was fetched for.

This is the same shape as the defect [note 0048](../commit/0048-a-second-chance-at-a-document.md)
fixed, one stage later. `pdf_fetch` only saw papers arriving on that run; `enqueue`
only sees attachments as they were when the task was first filed.

---

## What you can observe

```bash
export RA_WM_ROOT=/path/to/an/archive
cd /path/to/this/checkout

python3 -m pipelines.backfill --limit 40    # documents land on disk and on the records
python3 -m pipelines.render                 # "puts the paths in front of the reader"

python3 - <<'PY'
import json, glob
tot = doc = 0
for f in glob.glob("$RA_WM_ROOT/data/queue/pending/paper__*.json"):
    t = json.load(open(f)); tot += 1
    if (t.get("attachments") or {}).get("pdf_path"): doc += 1
print(f"{doc} of {tot} pending paper tasks carry a pdf_path")
PY
```

**Measured on the archive this was found on: `0 of 512`.** Meanwhile 224 of those
papers have a `local_path` pointing at a file that exists. A single record and its
task, side by side:

```
record  arxiv:2608.05720   local_path: data/pdfs/arxiv-2608-05720.pdf   (file exists)
task    paper__arxiv-2608-05720
        created_at:  2026-08-08T07:20:27Z
        attachments: {"full_text_path": "...", "full_text_words": 7166}
```

The task predates the document by five days and has no way to hear about it.

---

## Why it happens

**One guard, doing exactly what it says.** `pipelines/enrich/queue.py:243-260`:

```python
def enqueue(self, *, kind, item_id, topics, language,
            instructions, output_schema, payload, attachments=None) -> str:
    task_id = self.task_id(kind, item_id)
    pending = self.pending_path(task_id)

    if pending.exists() or self.done_path(task_id).exists():
        return ""
```

`queue_missing_summaries` (`render.py:87`) calls `summarize_paper` for every
record without a summary on every render — 512 of them here, which is why the log
reports `summaries_queued: 512` every time. The call reaches
`pipelines/common/llm.py:300`, which builds the task correctly:

```python
has_document = bool(paper.local_path)
...
attachments=({"pdf_path": paper.local_path} if paper.local_path else None),
```

and then `enqueue` returns `""` on line 260 without writing it. The right task is
constructed on every render and discarded on every render.

---

## Why it matters

**It is not only the attachment.** `has_document` also selects the instructions
(`llm.py:316`) and the output schema (`llm.py:318`). A task filed without a
document gets prompts written for an abstract and a schema with no `read_from`
field. So a stale task is wrong in three ways at once, and the one a reader
notices last is the one that costs most.

**The validator then turns a fetched document into a recorded lie.**
`_check_reading_basis` (`queue.py:69-103`) refuses `read_from: "document"` when the
task attached none:

> `read_from` says 'document', but this task attached none — a reading cannot be
> based on a document it was never given

That rule is right, and note 0044 built it for good reason. But combined with this
defect it produces the worst available outcome: a reader who opens
`data/pdfs/arxiv-2608-05720.pdf`, reads it properly, and then must record
`abstract` or be rejected. **The archive permanently records a weaker evidence
tier than it actually has**, and the tier is exactly what the reading rules turn
on.

**It makes a documented sequence untrue.** `CLAUDE.md` tells a session:

```bash
python3 -m pipelines.backfill --limit 20    # fetch, best-scoring first
python3 -m pipelines.render                 # puts the paths in front of the reader
```

The third line does not do that for any paper that was already queued — which, for
a command whose entire purpose is a backlog, is every paper it will ever help.

**And it is silent.** `backfill` reports `fetched: 40`, render reports
`summaries_queued: 512`, and both are true. Nothing anywhere compares a record's
`local_path` against its task's attachments, so the gap has no counter.

---

## Options

### A. Refile when the task's inputs have changed.

In `enqueue`, when a pending task exists, compare what would be written against
what is there — attachments, instructions, schema — and rewrite if they differ,
preserving `created_at`.

- **For:** fixes it wherever it arises, not just after `backfill`. A task is then
  a function of the record, which is what every other derived thing in this
  repository already is.
- **Against:** `enqueue` currently has one job and a one-line guard; this gives it
  a diff. It must not touch `done`, and it must not reset `created_at` — a task
  that silently became newer would break any ordering built on it. Comparing
  whole schemas is also broader than the problem: only `attachments` is known to
  go stale today.
- **Cost if wrong:** a rewritten task loses a field a reader was mid-way through
  relying on. Bounded by only rewriting when something actually differs.

### B. Refresh attachments only.

Same trigger, narrower action: if the stored task's `attachments` differ from the
freshly built ones, write only that key back, along with the instructions and
schema that depend on `has_document`.

- **For:** the smallest change that closes the observed hole, and the three fields
  that must move together are exactly the three `has_document` selects.
- **Against:** a rule that names three fields will be wrong the next time a fourth
  becomes derivable. It fixes this instance rather than the class.
- **Cost if wrong:** the same, smaller.

### C. Let `backfill` refile the tasks it changed.

`backfill.run` already knows precisely which records it touched
(`backfill.py:176-177` saves a paper only when `local_path` actually moved). Have
it delete and refile those tasks.

- **For:** the narrowest blast radius — only papers whose document just arrived,
  and the command that caused the change is the one that repairs it. No change to
  `enqueue`'s contract.
- **Against:** it puts queue-writing into a fetch command, and leaves the class of
  defect open: a document arriving any other way (a hand-filed PDF for a paper
  already queued, a `--root` swap, a manual copy) still leaves a stale task. It
  also makes `backfill` no longer true to its own note, which says it "queues
  nothing".

### D. Do nothing in code; document the manual repair.

Deleting the affected pending tasks and re-rendering already works, because
`queue_missing_summaries` exists precisely to refile a task that was "deleted by
hand".

- **For:** zero code. The self-healing path is real and already documented.
- **Against:** it asks a person to delete 224 files to collect a benefit the
  pipeline already paid for, and nothing tells them which 224. As a standing
  answer it is worse than the bug.

**Recommendation: A, with the guard written narrowly.** Rewrite a pending task
when what would be filed differs from what is filed, keep `created_at`, and never
touch `done` or `archive`. B is A with a list that will go stale; C leaves the
class open and costs `backfill` its "queues nothing" property; D is the workaround
to use *today*, not the fix.

Whichever is taken, `backfill`'s own summary should say how many tasks it made
stale, or the next person meets this the same way.

---

## Tests

`tests/test_backfill.py` covers the fetch and stops at the record.
`tests/test_queue.py` has no case where a task already exists and its inputs have
moved. Add:

1. **The round trip that failed here.** A paper with a queued task and no
   document; give the record a `local_path`; render; assert the pending task now
   carries `pdf_path`, and that its `read_from` field is present in the schema.
2. **`created_at` survives.** The refiled task keeps the timestamp it was first
   filed with — otherwise nothing can say how long the backlog has been waiting.
3. **A completed task is never rewritten.** Same setup with the task in `done`:
   assert it is untouched, since a reader may already have answered it.
4. **No write when nothing differs.** Two consecutive renders on an unchanged
   archive leave every task file byte-identical — the same property
   `_same()` protects for concept records, and the reason `render` twice produces
   no diff today.

---

## What a reviewer should check

- A task is a function of its record after the change. If any field can still be
  stale relative to the record it was built from, the class is still open.
- `created_at` is preserved and `done`/`archive` are untouched. Both are load
  bearing: one for backlog age, one because a reader may have answered already.
- `python3 -m pipelines.render` twice on an unchanged archive still produces no
  diff, including under `data/queue/pending/`.
- The documented sequence in `CLAUDE.md` becomes true: after
  `backfill` then `render`, a paper whose document just arrived has a task naming
  it, and a reader who opens that file may honestly record `read_from: "document"`.

## Notes for whoever picks this up

- The measured state on the archive where this was found: 224 documents fetched,
  `0 of 512` pending tasks carrying a `pdf_path`, and 287 further papers that name
  no PDF at all and are out of scope for `backfill` entirely.
- Related, and all the same shape — a value that one half of the pipeline sets and
  another half does not see:
  [`../solved/a-hand-filed-pdf-is-lost-when-its-record-merges.md`](../solved/a-hand-filed-pdf-is-lost-when-its-record-merges.md),
  [`../solved/related-links-are-asked-for-and-discarded.md`](../solved/related-links-are-asked-for-and-discarded.md).
  This one is distinctive in that the correct value is computed on every render
  and thrown away.
- No archive-side finding was recorded. It is a defect in the pipeline, not
  something the group established about the literature.

---

## Resolution

**Option A, with the guard written narrowly**, as recommended. `enqueue` rebuilds
a pending task from its record and rewrites it when the rebuild differs;
`created_at` is carried across and a task in `done/` is never touched. Commit
`fix(enrich): a waiting task learns that its document arrived`, note
[0052](../commit/0052-a-task-is-a-function-of-its-record.md).

Answers to what this document left open:

- **The whole rebuilt task is compared**, not a named list of fields. B's list
  is right today and wrong the next time something becomes derivable; comparing
  everything makes a task a function of its record, which is the property the
  class of defect needs.
- **A refresh is not a new task.** It returns `""`, does not count towards the
  cap, and the cap cannot block it — bounding the backlog is about how much is
  waiting.
- **`backfill` does not yet say how many tasks it made stale**, which this
  document asked for. It no longer makes any: a render after it brings every
  affected task up to date. What is still missing is the counter that would have
  made this visible at all — `render` reports `summaries_queued`, which counts
  records without a summary rather than tasks filed, and reported `512` on every
  pass throughout. That is filed as its own next step rather than smuggled in
  here.

### Two tests that did not bite until they were tightened

Both are the same trap, and this repository has recorded it before:

- **`created_at` compared within one second.** `utcnow()` has second resolution,
  so a re-stamped timestamp was identical to the one it replaced. The test now
  sleeps past a second boundary — the correction `tests/test_layering.py` already
  documents having needed.
- **The no-churn test hashed file contents.** A rewrite with identical bytes is
  invisible to a hash, so writing on every render passed. It now compares
  modification time as well.

The documented sequence in `CLAUDE.md` is true from this commit: after `backfill`
then `render`, a paper whose document just arrived has a task naming it, and a
reader who opens that file may honestly record `read_from: "document"`. The
comment on the render line said "puts the paths in front of the reader" and has
been corrected to say what it does.
