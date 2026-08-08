# 0000 — Baseline: the pipeline as inherited

| | |
| --- | --- |
| **Commit** | `baseline: the research archive pipeline` — the root commit |
| **Scope** | the whole repository as it stood before the commit-note practice |
| **Kind** | reference |

This note describes the commit before it rather than its own. The pipeline was
built before this practice existed, and a template whose first eight hundred
lines have no recorded reasoning is a template nobody can safely modify. So the
design is written down here, once, as the baseline that every later note is a
delta against. Where it states a rationale, that rationale is reconstructed
from the code and its docstrings, not from the original author's notes — this
is the only note in `docs/commit/` that was not written by the author of the
change it explains.

## The shape of the system

```
arXiv · OpenReview · Semantic Scholar · DBLP · YouTube
                      │
                collect ─► score ─► deduplicate ─► data/
                                                    │
                                          ┌─────────┴─────────┐
                                    work queue            render
                                          │                   │
                                    summaries ────────► archive/ wiki/ outputs/
```

| Layer | Where | What it owns |
| --- | --- | --- |
| Core | `pipelines/common/` | Config, normalized records, storage, HTTP, Markdown, the summarizer contract |
| Collect | `pipelines/collect/` | arXiv, three conference indexes, YouTube channel feeds |
| Enrich | `pipelines/enrich/` | Keyword scoring, cross-source dedup, the work queue |
| Publish | `pipelines/publish/` | Archive pages, the wiki, lecture notes, decks, reports |
| Entry points | `pipelines/run_daily.py`, `render.py` | The two commands, and nothing else |

## The load-bearing decisions

**`data/` is the only source of truth.** `archive/`, `wiki/` and `outputs/` are
derived and disposable — delete all three, run render, and they come back
identical. Every other decision is downstream of this one: changing a template,
a renderer or a summary format never means re-fetching anything, and a broken
render is repaired by deleting the output and running again.

**No model is called from inside the pipeline.** Collection files a task
describing what needs reading; something else answers it. By default that is a
Claude Code session draining `data/queue/pending/`, which is why the system runs
with no API key and no cost. `pipelines/common/llm.py` holds the prompts and the
output schema every backend must satisfy, so two backends cannot drift into
producing incomparable summaries. The Anthropic and Ollama backends exist as
interface only; filling either in is two methods and changes nothing else.

**The queue is a filesystem, and each task is self-contained.** Instructions,
output schema and all the source material in one file, so whoever picks it up
needs no other context. Consequences worth stating: a slow or failed reading
step costs summaries and never a day of collection; reading can happen hours
later, elsewhere, by a different backend or by a person; and when something
goes wrong at 4am the debugging tool is `cat`.

**Leave a field empty rather than inventing content.** The single most important
instruction in the repository, enforced socially in `CLAUDE.md` and structurally
by a validator that names the missing field. An empty `results` field is a true
statement about what is known; a plausible invented one propagates into the
wiki, the lecture notes and the deck, where nobody will trace it back.

**Topics are data, not code.** A subject is a YAML file, and nothing in the
pipeline knows what field it is being used for. Adding `config/topics/<slug>.yaml`
is the entire procedure for tracking something new.

**Scoring is a keyword rule on purpose.** An opaque relevance model would be
better at the margins and impossible to argue with. Title hits count triple,
tracked authors add a bonus, and the total is squashed into `(0, 1)` so one
title hit lands at exactly `0.50` and thresholds stay comparable across topics
with very different keyword lists. Below-threshold items are recorded in
`data/index/rejected.jsonl` rather than discarded, so a threshold can be
revisited later without re-collecting the window.

**An unreachable source is not a failed run.** Collectors log and return what
they have. These are third-party services with no uptime obligation; a run that
aborts because DBLP was slow produces nothing instead of most things. The risk
this accepts is quiet under-collection — an OpenReview venue id that changed
between cycles yields zero hits and no error, by design.

**Three overlapping indexes beat one correct one.** The same paper arrives as a
preprint, a submission and a proceedings entry, each carrying different fields.
Dedup merges by filling empty fields rather than overwriting, so the abstract
from arXiv and the venue from proceedings both survive. Identity is arXiv id,
then DOI, then a normalized-title fingerprint, and the alias map lives in
SQLite because deduplication that forgets between runs is not deduplication —
which is also why `data/index/seen.sqlite` is committed despite being a binary.

**Half of every wiki note is inviolable.** Everything between the auto markers
is regenerated; everything after `<!-- auto:end -->` is preserved forever. A
note whose entity stops appearing is deleted *unless* someone wrote in the
manual section. The system may garbage-collect its own output and never a
person's.

**The wiki grows on evidence, not on instruction.** Entities named in summaries
accumulate in `data/concepts/`; once one has appeared in enough independent
sources (two by default) it is promoted to a note *and a definition task is
queued*, so the note gets written properly rather than left as a stub.

**One gathering, three artifacts.** `publish/material.py` assembles what a topic
knows once; the lecture note, the deck and the report differ only in how much of
it they show. Three independent gatherings would drift, and the drift would show
up as a deck disagreeing with the report handed out at the same meeting.

**Single-file HTML with no external requests.** Decks and reports open from
disk, from an attachment, or from a USB stick in a room with no network. This is
why `common/md.py` exists instead of a client-side Markdown renderer, and why
there is no CDN link in `templates/`.

**One dependency.** `PyYAML` is required; `youtube-transcript-api` is optional
and only decides whether transcripts are captured. Everything else is the
standard library, including the HTTP client, the XML parsing, the Markdown
converter and the dedup database. Every dependency is a thing that can fail to
install at 4am in a container nobody is watching.

**`render.py` never fetches and never calls a model.** It is therefore always
safe to rerun, and rerunning is the entire recovery procedure. There is no
repair mode, no `--force`, no cache to invalidate.

## Known trade-offs carried forward

- **Hand-rolled `http.py` and `md.py`** must be maintained here. `md.py` covers
  only the Markdown the generators emit and will mangle anything else.
- **No golden-file tests for rendered HTML** — render tests assert structural
  properties instead, so a visually broken template can still pass.
- **No contract tests against live APIs.** Recorded payloads catch a misread
  schema but not a changed one; an upstream shape change surfaces as a quiet
  drop in collected items.
- **YouTube channel feeds carry no duration**, so `min_duration_s` can only
  reject videos whose length is known. Unknown-length videos are kept and
  flagged.
- **New work appears during render.** Promoting a concept queues a definition
  task, so a full cycle is collect → drain → render → drain → render.

## What a reviewer should check first

- `common/schema.py: canonical_paper_id()` — identity precedence decides what
  merges with what; a wrong precedence collapses two distinct papers.
- `common/llm.py` vs `render.py` — the output schema and its consumer drifting
  apart is the most likely future bug in the repository.
- `publish/wiki.py: _preserved_tail()` — a bug here destroys hand-written text,
  the one class of content that cannot be regenerated.
- `enrich/queue.py: validate_result()` — the rejection message must name the
  field, or whoever drains the queue learns to guess.
