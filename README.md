# Recipe for Research Team Management with Claude

The literature work a research group repeats every week, run by Claude instead
of by hand.

Name the topics your group follows. Every day it collects new papers from arXiv
and the major conference indexes, pulls seminar recordings from tracked YouTube
channels, reads what clears the relevance bar, files each reading in a browsable
archive, grows a wiki that adds a new note whenever a concept starts recurring,
and regenerates lecture notes, slide decks and reports from everything it knows.

What is left for people is the part that needs judgement: deciding what the
group tracks, and correcting what it concludes. Everything a new member would
otherwise ask for — what has been published lately, what does this term mean,
where do I start reading — is already written down and current.

Nothing here is tied to a field. A topic is a YAML file, and that file is the
only thing that decides what gets collected, so the same repository serves a
machine learning group, a statistics lab or a reading group in any discipline.

## Quick start

```bash
pip install -r requirements.txt

scripts/new_topic.sh "Causal Inference"
$EDITOR config/topics/causal-inference.yaml   # fill in keywords.any

python3 -m pipelines.run_daily --dry-run     # what would be collected?
python3 -m pipelines.run_daily               # collect and queue
python3 -m pipelines.render                  # rebuild every artifact
```

A topic is whatever the group actually follows — `"Causal Inference"`,
`"Diffusion Models"`, `"Single-Cell Genomics"`, `"Monetary Policy"`. Add one per
subject; they are collected and rendered independently.

After the first real run, `archive/daily/<today>.md` is the day's digest and
`data/queue/pending/` holds one task per paper that still needs reading. See
[CLAUDE.md](CLAUDE.md) for how those get answered.

Only `PyYAML` is required; everything else is the standard library.
`youtube-transcript-api` is optional and only affects whether seminar
transcripts are captured.

## Filing a paper by hand

Not everything a group reads is on arXiv. Drop a PDF into `inbox/` and the next
run ingests it:

```bash
cp ~/Downloads/some-paper.pdf inbox/
python3 -m pipelines.run_daily --source local
```

The file moves to `data/pdfs/` under a content-addressed name — so the same
paper filed twice under two names is one record — and a reading task is queued.
Whoever answers it opens the document, reads it figures and all, and supplies
both the summary and the bibliography, because nothing in the pipeline opens a
PDF. From there it is an ordinary paper: archive page, wiki entities, topic
outputs.

A PDF filed this way is never rejected by keyword scoring. Putting it in the
inbox *is* the editorial decision scoring exists to approximate; which topics it
belongs to is the reader's call. PDFs themselves are not tracked by git — the
records are, so a fresh clone has the whole archive without the weight.

## Following somebody else's reading

A weekly "papers of the week" list is a filter no keyword can reproduce: one
editor reads a field's whole output and picks ten. `config/sources.yaml` takes
any such list that is published as markdown — `curated.lists` ships with
[DAIR.AI's](https://github.com/dair-ai/ML-Papers-of-the-Week), whose LinkedIn
and Substack editions are the same papers behind a login wall.

The list is read for **pointers only**. Its entries name papers the way people
say them out loud — an acronym and a paragraph of commentary — so the title,
authors and abstract come from the arXiv id the entry links to, and a pick that
links to a blog post instead is skipped by name in the log. A pick the archive
already holds is stamped `+curated` rather than duplicated.

Picks are scored like anything else. A PDF you file skips scoring because
filing it is your decision; a curated list is somebody else's, taken over a
whole field rather than over your topics. Expect a general list to be mostly
rejected against a narrow archive — that is the filter working.

## How it works

```
arXiv (API · listing) · OpenReview · Semantic Scholar · DBLP · venue programmes
                      · curated weekly lists · YouTube · inbox/
                      │
                collect ─► score ─► deduplicate ─► data/
                                                    │
                                          ┌─────────┴─────────┐
                                    work queue            render
                                          │                   │
                                    summaries ────────► archive/ wiki/ outputs/
```

Two properties are worth knowing up front, because everything else follows from
them:

**`data/` is the only source of truth.** `archive/`, `wiki/` and `outputs/` are
derived. Delete all three, run `python3 -m pipelines.render`, and they come back
identical — so changing a template or a renderer never means re-collecting
anything.

**No model is called from inside the pipeline.** Collection files a task
describing what needs reading; something else answers it. By default that is the
daily Claude Code session, which is why the system runs with no API key at all.
`pipelines/common/llm.py` holds the prompts and the output schema every backend
must satisfy — pointing it at an API instead means implementing two methods and
changing nothing else.

## Where things live

Every directory here is one of three kinds, and telling them apart is most of
understanding the repository:

| Kind | Which | Rule |
| --- | --- | --- |
| **Yours** | `config/`, `templates/`, `inbox/`, the manual half of `wiki/` | Edit freely. Nothing overwrites them. |
| **The truth** | `data/` | Written by the pipeline, never by hand. Everything else derives from it. |
| **Derived** | `archive/`, `wiki/`, `outputs/` | Delete them, run render, they come back identical. Never edit them. |

Those three are the archive. `pipelines/`, `templates/`, `tests/` and `docs/`
are the program, and the two can live in separate repositories — see
[Keeping the archive in a repository of its own](#keeping-the-archive-in-a-repository-of-its-own).

```
.
├── config/                     ← yours: what gets collected, and how
│   ├── settings.yaml             language, lookback window, scoring weights, wiki thresholds
│   ├── sources.yaml              arXiv categories, venues, curated lists, YouTube, inbox
│   └── topics/<slug>.yaml        one file per tracked subject — the whole editorial decision
│
├── inbox/                      ← yours: drop a PDF here, it drains on the next run
│
├── workflows/                  ← one folder per task: the procedure, and what checks it
│
├── migration/                  ← staging for a move to a new environment; payload
│   └── README.md                 gitignored, instructions tracked
│
├── data/                       ← the source of truth. Committed.
│   ├── papers/<id>.json          one record per paper
│   ├── videos/<id>.json          one per seminar, plus <id>.transcript.json
│   ├── summaries/                the readings: papers/<id>.json, videos/<id>.json
│   ├── concepts/<slug>.json      wiki entities and the evidence behind each one
│   ├── findings/<id>.json        what the group settled in conversation — the one
│   │                             record it authors itself
│   ├── references/<id>.json      pages checked outside the archive, cited by findings;
│   │                             never evidence for a wiki entity
│   ├── queue/                    pending/ → done/ → archive/, one JSON task per unread item
│   ├── index/                    papers.jsonl, videos.jsonl, rejected.jsonl, coverage.jsonl, seen.sqlite
│   ├── abstracts/<cat>/<day>.jsonl  every announced paper, not only the tracked
│   │                             ones — the ledger above is committed, this is not
│   ├── pdfs/                     documents still to be read              (not committed)
│   │   └── read/                 …and those whose reading is done
│   ├── raw/                      collector responses, for replaying a parse bug (not committed)
│   └── logs/                     run logs                                  (not committed)
│
├── archive/                    ← derived: the human-readable record
│   ├── papers/<year>/<id>/       one page per paper
│   ├── seminars/<id>/            talk summary and transcript
│   ├── daily/<date>.md           what arrived that day — a record of a run, not a rendering,
│   │                             so it is the one thing here that is never regenerated
│   └── index.md
│
├── wiki/                       ← derived, except the manual tail of every note
│   ├── topics/ concepts/ methods/ datasets/
│   ├── _meta/graph.json          the backlink graph
│   ├── graph.html                the same graph, drawn — open it in a browser
│   ├── findings.md               the picture the group has drawn for itself
│   └── index.md
│
├── outputs/                    ← derived, one set per topic
│   ├── lecture-notes/<slug>/
│   ├── slides/<slug>/index.html
│   └── reports/<slug>/index.html
│
├── pipelines/                  the code
│   ├── common/                   config, records, storage, HTTP, Markdown, the summarizer contract
│   ├── collect/                  arxiv (+ arxiv_listing) · conferences (+ virtual_site) · youtube · local_pdf · pdf_fetch
│   ├── enrich/                   score · dedupe · queue · coverage · findings
│   ├── publish/                  archive · wiki (+ graph_page) · lecture_note · slides · report
│   ├── run_daily.py              collect and queue
│   └── render.py                 apply and rebuild
│
├── templates/                  ← yours: how the generated artifacts look
├── scripts/                    daily.sh, new_topic.sh
├── tests/
└── docs/
    ├── daily-routine.md          each stage in detail, and troubleshooting
    ├── API.html                  every external request the pipeline makes, and why
    └── commit/                   one note per commit: what changed, why, what it costs
```

`data/`, `archive/`, `wiki/` and `outputs/` do not exist until the first run.
What each generated artifact actually contains is in
[What it produces](#what-it-produces) below.

Almost everything is committed, including the generated trees — a scheduled run
starts from a fresh clone, so anything uncommitted is lost. The exceptions are
the heavy and the reproducible: raw responses, logs, and PDFs. Note that
`data/index/seen.sqlite` **is** committed despite being a binary; deduplication
state that does not survive the clone is not deduplication state.

## Keeping the archive in a repository of its own

Run in place, one repository holds both halves and the quick start above is all
there is. That works until you want to `git pull` a new version of the code
while an archive is accumulating underneath it — and then the two halves collide
in the worst possible files: `seen.sqlite` is binary and unmergeable, the wiki
graph is regenerated on every render, and `config/` has to be edited by you and
keeps evolving here.

So the archive can live in a repository of its own, and a checkout of this one
can be pointed at it:

```bash
export RA_WM_ROOT=~/research-archive     # or --root on any single command
python3 -m pipelines.migrate status      # prints both roots — check before running anything
scripts/daily.sh
```

The archive repository holds `config/`, `data/`, `wiki/`, `archive/`, `outputs/`
and `inbox/`; this one holds the program. Nothing is shared, so nothing
conflicts — `git pull` here and `git commit` there never meet. `templates/` is
the one directory both may hold: a template is resolved from the deployment
first and this repository second, per file, so an archive with no `templates/`
at all renders with the shipped ones and goes on receiving improvements, while
overriding a single file changes exactly that file.

Setting one up, and updating the code underneath a running archive, is
[`workflows/deployment/`](workflows/deployment/).

## Sharing it with people on the same machine

```bash
python3 -m pipelines.serve                       # http://127.0.0.1:8765
curl "http://127.0.0.1:8765/ask?q=causal+inference"
```

Colleagues on the same host can ask the archive what it knows without a clone
and without any way to change what they are reading.

**It answers only from what has been read.** A hit is a record the archive
already wrote — a finding the group settled, a definition somebody authored, a
reading of a paper — ranked in that order, because that is the archive's own
ordering of authority. Nothing here composes a sentence: the pipeline calls no
model, and a plausible invented answer is worse to a colleague than an honest
"nothing here", since they cannot tell it from a real one.

Asking for a *change* is a different channel on purpose:

```bash
cp my-request.md requests/pending/     # anyone on the host
python3 -m pipelines.requests list     # the archive's owner
python3 -m pipelines.requests approve <id> --note "why"
```

Nothing is approved automatically, however harmless it looks, and an approved
request is work for the next maintenance session rather than a change already
made. A rejected one keeps its reason: declined is not deleted.

**The port writes nothing at all** — not to `data/`, not anywhere — and binds to
loopback with no flag to change that. There is no authentication, which is why
the read-only guarantee has to be absolute: on a shared host, loopback means any
local user. A host that wanted to publish its archive would put a proxy in
front and make that decision where it can be seen.

## Topics

A topic is `config/topics/<slug>.yaml`. The parts that matter:

```yaml
slug: causal-inference
name: Causal Inference
description: >-
  Estimating the effect of a treatment from observational data, and the
  assumptions each estimator needs to be credible.

keywords:
  any:                      # at least one must appear
    - causal inference
    - instrumental variable
  all: []                   # every one must appear
  none:                     # any hit rejects the item
    - survey

authors: []                 # tracked authors add a scoring bonus
seed_papers: []             # anchor papers, archived on first run
min_score: 0.35             # below this: recorded, not read
```

Copy [`config/topics/_template.yaml`](config/topics/_template.yaml), or run
`scripts/new_topic.sh "Name"`. Files starting with `_` are ignored.

Deciding what belongs in `keywords` is the one editorial act the system cannot
do for you, and it is where a group's judgement actually goes.

## What it produces

| Path | Contents |
| --- | --- |
| `archive/papers/<year>/<id>/summary.md` | One page per paper: problem, contributions, method, results, limitations |
| `archive/seminars/<id>/` | Talk summary with timestamped chapters, plus the transcript |
| `archive/daily/<date>.md` | What arrived that day, grouped by topic |
| `wiki/` | Notes on concepts, methods and datasets, with a backlink graph |
| `outputs/lecture-notes/<slug>/` | Teaching material: landscape, core ideas, reading path, open problems |
| `outputs/slides/<slug>/index.html` | Self-contained deck — arrow keys, `o` for overview, `p` to print |
| `outputs/reports/<slug>/index.html` | Self-contained report with contents, activity view and full index |

Both HTML artifacts are single files with no external requests, so they open
from disk, from an attachment, or from a USB stick in a room with no network —
which is what makes them usable for a group meeting or a lecture.

## The self-extending wiki

Every summary names the concepts, methods and datasets it relies on. Those names
accumulate evidence in `data/concepts/`. Once one has appeared in enough
independent sources — two, by default — it is promoted to a note of its own and
a definition task is queued automatically. The wiki gains a properly written
note exactly when the literature starts converging on a term, without anyone
asking for it.

Notes are half generated and half yours:

```markdown
# Instrumental Variable
<!-- auto:begin -->
... rebuilt on every render: definition, sources, backlinks ...
<!-- auto:end -->

## Notes
Anything here is never touched.
```

That preserved section is where a group's own reading goes — the objection
someone raised in seminar, the trick that only works on your data.

### Definitions go out of date, and are asked for again

A definition is written once, against the sources that existed then. When the
evidence outgrows it the note reads as complete while describing a subset of
itself — worse than a missing definition, because nothing about it looks wrong.

`render` reports these under `stale`. Set `wiki.refresh_definition_at: 2.0` and
it also asks for them again once the evidence has doubled, a few per pass, worst
first. The existing definition is handed back to be revised rather than
discarded, and a refresh nobody answers changes nothing.

## Configuration

| File | Purpose |
| --- | --- |
| `config/settings.yaml` | Language, lookback window, scoring weights, summarizer backend, wiki thresholds |
| `config/sources.yaml` | arXiv categories, tracked venues, curated lists, YouTube channels |
| `config/topics/*.yaml` | The subjects themselves |

The defaults in `config/sources.yaml` are a general-purpose starting point. Swap
the arXiv categories and the venue list for your field's before the first run —
collecting from the wrong indexes is the most common reason a topic stays empty.

## Commands

```bash
python3 -m pipelines.run_daily [--days N] [--topic slug] [--source arxiv] [--dry-run]
python3 -m pipelines.backfill  [--limit N] [--topic slug] [--by score|age|id] [--dry-run]
python3 -m pipelines.render    [--topic slug] [--only archive|wiki|outputs]
python3 -m pipelines.enrich.queue stats | show <id> | complete <id> --file r.json
python3 -m pipelines.enrich.queue list | next  [--kind paper] [--by id|sources|recency|topic]
python3 -m pipelines.enrich.synthesis add --question "..." --concept <slug>
python3 -m pipelines.enrich.lookup add --subject spelling --about "..."
python3 -m pipelines.duplicates [--json] [--limit N]   # concept slugs that may be one entity
python3 -m pipelines.digest [--date YYYY-MM-DD]        # what a night of reading did
python3 -m pipelines.migrate status   # which roots, and what each channel carries
python3 -m pipelines.serve            # answer questions about the archive, read-only, on 127.0.0.1
scripts/daily.sh               # collect, then render
python3 -m unittest discover -s tests -t .
```

Every one of them takes `--root <path>` and reads `RA_WM_ROOT`, naming the tree
the archive lives in. Unset, that is this checkout.

## Further reading

- [CLAUDE.md](CLAUDE.md) — the routine an agent session follows, and the rules
- [docs/daily-routine.md](docs/daily-routine.md) — each stage in detail, and troubleshooting
