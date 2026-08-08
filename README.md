# Recipe for World Action Model

A research archive that maintains itself.

Define a topic once. Every day it collects new papers from arXiv and the major
conference indexes, pulls seminar recordings from tracked YouTube channels,
reads what clears the relevance bar, files each reading in a browsable archive,
grows a wiki that adds a new note whenever a concept starts recurring, and
regenerates lecture notes, slide decks and reports from everything it knows.

Nothing here is specific to one field. The repository is named for the subject
it was built to track, but a topic is a YAML file and that is the only thing
that decides what gets collected.

## Quick start

```bash
pip install -r requirements.txt

scripts/new_topic.sh "Vision-Language-Action Models"
$EDITOR config/topics/vision-language-action-models.yaml   # fill in keywords.any

python3 -m pipelines.run_daily --dry-run     # what would be collected?
python3 -m pipelines.run_daily               # collect and queue
python3 -m pipelines.render                  # rebuild every artifact
```

After the first real run, `archive/daily/<today>.md` is the day's digest and
`data/queue/pending/` holds one task per paper that still needs reading. See
[CLAUDE.md](CLAUDE.md) for how those get answered.

Only `PyYAML` is required; everything else is the standard library.
`youtube-transcript-api` is optional and only affects whether seminar
transcripts are captured.

## How it works

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

## Topics

A topic is `config/topics/<slug>.yaml`. The parts that matter:

```yaml
slug: vision-language-action
name: Vision-Language-Action Models
description: >-
  End-to-end policies that map visual observation and language instruction
  directly to robot action.

keywords:
  any:                      # at least one must appear
    - vision-language-action
    - VLA policy
  all: []                   # every one must appear
  none:                     # any hit rejects the item
    - survey

authors: []                 # tracked authors add a scoring bonus
seed_papers: []             # anchor papers, archived on first run
min_score: 0.35             # below this: recorded, not read
```

Copy [`config/topics/_template.yaml`](config/topics/_template.yaml), or run
`scripts/new_topic.sh "Name"`. Files starting with `_` are ignored.

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
from disk, from an attachment, or from a USB stick in a room with no network.

## The self-extending wiki

Every summary names the concepts, methods and datasets it relies on. Those names
accumulate evidence in `data/concepts/`. Once one has appeared in enough
independent sources — two, by default — it is promoted to a note of its own and
a definition task is queued automatically. The wiki gains a properly written
note exactly when the literature starts converging on a term, without anyone
asking for it.

Notes are half generated and half yours:

```markdown
# Latent Action Model
<!-- auto:begin -->
... rebuilt on every render: definition, sources, backlinks ...
<!-- auto:end -->

## Notes
Anything here is never touched.
```

## Configuration

| File | Purpose |
| --- | --- |
| `config/settings.yaml` | Language, lookback window, scoring weights, summarizer backend, wiki thresholds |
| `config/sources.yaml` | arXiv categories, tracked venues, YouTube channels |
| `config/topics/*.yaml` | The subjects themselves |

## Commands

```bash
python3 -m pipelines.run_daily [--days N] [--topic slug] [--source arxiv] [--dry-run]
python3 -m pipelines.render    [--topic slug] [--only archive|wiki|outputs]
python3 -m pipelines.enrich.queue stats | list | next | show <id> | complete <id> --file r.json
scripts/daily.sh               # collect, then render
python3 -m unittest discover -s tests
```

## Further reading

- [CLAUDE.md](CLAUDE.md) — the routine an agent session follows, and the rules
- [docs/daily-routine.md](docs/daily-routine.md) — each stage in detail, and troubleshooting
