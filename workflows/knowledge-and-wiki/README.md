# Knowledge and wiki

The loop the whole repository exists to run. Authority is
[`CLAUDE.md`](../../CLAUDE.md); this is the command sequence and where each step
can go wrong. The harness is in [`harness.md`](harness.md).

## The shape

```
collect ──► score ──► dedupe ──► data/ ──► queue ──► YOU read ──► complete
                                   ▲                                  │
                                   └────────── render ◄───────────────┘
                                                 │
                                    archive/ · wiki/ · outputs/
```

Two halves. The pipeline is deterministic Python and calls no model. The
reading is judgement and only you can do it. They meet at a file-backed queue,
which is why a slow or failed reading never costs a day of collection.

## Procedure

**0. Start from what is on `main`.**

```bash
git fetch origin main
git log --oneline HEAD..origin/main     # anything here means you are behind
```

**1. Collect.**

```bash
python3 -m pipelines.run_daily
```

An unreachable source is logged and skipped — that is not a failed run. Narrow
it while debugging: `--dry-run`, `--topic <slug>`, `--source local`, `--days 30`.

**2. Drain the queue.** The part only you can do.

```bash
python3 -m pipelines.enrich.queue stats
python3 -m pipelines.enrich.queue list [--by id|sources|recency|topic] [--kind paper]
python3 -m pipelines.enrich.queue show <task_id>
python3 -m pipelines.enrich.queue complete <task_id> --file /tmp/result.json
```

`list` and `next` default to filename order, which is alphabetical. If the
queue will not be emptied tonight, choose the end you are draining — `--by
sources` first, and `--by topic` when the drain should spread across subjects
instead of following one to the bottom. The rule each ordering uses, and why
the two `sources` numbers are not the same unit, is in
[`CLAUDE.md`](../../CLAUDE.md#the-daily-routine).

The task carries the instructions, the schema and the source material. Three
rules decide whether the result is worth having:

- **Open `attachments.pdf_path` when the task has one.** The abstract is a
  summary of the paper's claims; `results` and `limitations` come from the
  experiments section.
- **Leave a field empty rather than inventing content.** An empty `results` is a
  true statement about what you know.
- **A schema asking for `bibliography` is a hand-filed PDF.** Nothing has read
  it. Fill the bibliography from the document — the filename is not evidence —
  and choose the topics yourself; an empty list is a valid answer.

Caught a mistake? `queue reopen <task_id>` before rendering. Never hand-edit
`data/`.

**3. Render.**

```bash
python3 -m pipelines.render
```

Folds results into records, rebuilds everything derived, and queues definition
tasks for entities that just crossed the promotion threshold. **New tasks appear
here** — drain them the same way and render again.

**4. Record what got settled.**

```bash
python3 -m pipelines.enrich.findings add --file /tmp/finding.json
```

```json
{"kind": "decision",
 "statement": "One sentence somebody could disagree with.",
 "rationale": "What settled it.",
 "concepts": ["Partial Interference"],
 "papers": ["arxiv:2401.12345"],
 "topics": ["<slug>"]}
```

A decision that changes is never edited — record the new one with `supersedes`
set to the old id. Why the group used to think otherwise is most of what a
newcomer needs to trust what it thinks now.

**5. Commit.** Generated files are tracked on purpose; the container is
ephemeral. A routine digest needs no commit note — anything touching code,
config, templates or docs does, see [commit-and-push](../commit-and-push/).

```bash
git add -A && git commit -m "archive: <date> digest"
```

## The three ways this goes quietly wrong

**An empty queue means nothing is *unwritten*. It does not mean nothing is *out
of date*.** Read the `stale` block in render's result. A definition written
against three sources and now standing at nine reads as complete while
describing a third of its evidence — worse than a missing one, because nothing
about it looks wrong. Nothing is rewritten automatically. To re-queue one, clear
`definition` in `data/concepts/<slug>.json` and render again.

**A generic entity name merges two things.** The wiki keys entities by the exact
string you write, so "three benchmarks (unnamed in abstract)" from two unrelated
papers becomes one entity that fabricates its own corroboration. Name one
specific thing per entry, or leave the list empty and say it in prose.

**One thing named two ways splits into two entities.** The same key rule, in the
other direction: "world model" in one reading and "world models" in the next are
two records, each with its own evidence and its own march towards promotion, and
neither is wrong about anything — which is why nothing catches it. The archive
ends up saying half of what it knows about a term, twice.

```bash
python3 -m pipelines.duplicates            # pairs that are probably one entity
python3 -m pipelines.duplicates --json     # the same, for something else to read
```

It suggests and stops: it merges nothing and writes nothing, because which of
two names survives is a judgement and folding one record into another cannot be
undone. Worth running when the wiki has grown, not nightly. To act on a pair,
decide which name the group keeps and record the other as an alias when that
concept's definition task is answered — through the validator, like every other
answer.
