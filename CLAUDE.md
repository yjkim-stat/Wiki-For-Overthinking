# Working in this repository

This repository runs a research group's literature workflow: it collects papers
and seminar recordings for a set of tracked topics, reads them, keeps a wiki
that extends itself as concepts recur, and generates lecture notes, slide decks
and reports. The topics are the group's own; nothing here assumes a field.

The pipeline is deterministic Python. The reading is yours. Those two halves
meet at a file-backed work queue, and the whole contract is below.

## The daily routine

Run this when a scheduled session wakes you, or when asked to bring the archive
up to date.

**1. Collect.**

```bash
python3 -m pipelines.run_daily
```

Fetches from arXiv, the conference indexes and YouTube, scores everything
against every topic, stores what cleared the bar, and files a task per item
that still needs reading. A source that is unreachable is logged and skipped —
that is not a failure of the run.

**2. Drain the queue.** This is the part only you can do.

```bash
python3 -m pipelines.enrich.queue stats
python3 -m pipelines.enrich.queue list
```

For each pending task:

```bash
python3 -m pipelines.enrich.queue show <task_id>
```

The task carries everything you need: the instructions, the exact output schema
and the source material. Read it, write the JSON it asks for, and submit:

```bash
python3 -m pipelines.enrich.queue complete <task_id> --file /tmp/result.json
```

Submission is validated. A rejected result means a required field is missing or
mistyped — fix it and resubmit; do not work around the validator.

For a paper task, read the abstract supplied in the task. If the paper's
contribution cannot be established from it, fetch the linked PDF or abstract
page rather than guessing. **Leave a field empty rather than inventing
content** — an empty `results` field is a true statement about what you know; a
plausible invented one corrupts everything built on top of it, including the
lecture notes and the wiki.

**3. Render.**

```bash
python3 -m pipelines.render
```

Folds the completed tasks into the records, rewrites the archive and the wiki,
queues definition tasks for any concept that has just crossed the promotion
threshold, and regenerates the outputs. New concept tasks appear here — drain
them the same way and render again.

**4. Commit.** Generated files are tracked on purpose: the container is
ephemeral, so anything uncommitted is lost.

```bash
git add -A && git commit -m "archive: <date> digest"
```

A routine digest commit needs no commit note. Any commit that changes code,
config, templates or documentation does — see the rule below.

## Rules

- **Never hand-edit anything under `archive/`, `outputs/`, `data/index/` or a
  wiki auto block.** All of it is regenerated; your edits will disappear. In a
  wiki note, everything *after* `<!-- auto:end -->` is preserved forever —
  that is where analysis belongs.
- **`data/` is the source of truth.** Everything else is derived and can be
  deleted and rebuilt with `python3 -m pipelines.render`.
- **Do not add topics on your own initiative.** What the group tracks is its
  own editorial decision. When asked, use `scripts/new_topic.sh "Name"` and fill
  in the keywords.
- **Do not invent sources.** Every paper and video in the archive arrived from
  a collector. If something belongs in the archive that a collector missed, say
  so rather than writing a record by hand.
- **No change to the system lands without a commit note.** Before committing
  anything other than a routine archive digest, follow the `commit-notes` skill
  in `.claude/skills/commit-notes/`: split the work into commits that each carry
  one idea, and write `docs/commit/NNNN-slug.md` for each, staged in the same
  commit. This repository is deployed into other projects and its history is
  read as documentation.

## Layout

| Path | What it is |
| --- | --- |
| `config/topics/*.yaml` | The tracked subjects. Adding a file is all it takes. |
| `pipelines/` | The code. `run_daily.py` collects, `render.py` rebuilds. |
| `data/` | Source of truth: records, summaries, the queue, dedup state. |
| `archive/` | Generated page per paper and seminar, plus dated digests. |
| `wiki/` | Generated notes with hand-written sections preserved. |
| `outputs/` | Lecture notes, decks and reports, per topic. |
| `templates/` | How the generated artifacts look. |

## Common commands

```bash
python3 -m pipelines.run_daily --dry-run          # see what would be collected
python3 -m pipelines.run_daily --topic <slug>     # one topic only
python3 -m pipelines.run_daily --days 30          # backfill a wider window
python3 -m pipelines.render --only wiki           # rebuild one stage
python3 -m pipelines.enrich.queue next            # the oldest pending task
scripts/daily.sh                                  # collect + render
python3 -m unittest discover -s tests -t . -v      # tests
```
