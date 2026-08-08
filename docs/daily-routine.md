# The daily routine

How the automation actually runs, and what to check when it misbehaves.

## The two halves

The system splits cleanly at the work queue.

```
                        deterministic                    judgement
                 ┌──────────────────────────┐   ┌──────────────────────┐

  arXiv ─┐
  venues ─┼─► collect ─► score ─► dedupe ─► store ─► queue ─► read ─► complete
  YouTube ┘                                   │                          │
                                              ▼                          ▼
                                            data/                  data/queue/done/
                                              │                          │
                                              └──────► render ◄──────────┘
                                                         │
                                          archive/ · wiki/ · outputs/
```

Everything left of the queue is reproducible: same inputs, same records. Everything
right of it needs a reader. Keeping them apart means a slow or failed reading step
costs you summaries, never a day of collection, and that changing how things are
rendered never requires re-fetching anything.

## Scheduling

The intended trigger is a Claude Code Routine that wakes a session on a schedule
and hands it the routine from `CLAUDE.md`. A Routine is used rather than a cron
job because step 2 — reading the papers — needs a model in the loop, and a
plain cron job has no way to do it.

To register one, ask Claude to create a Routine whose prompt is:

> Run the daily routine in CLAUDE.md: collect, drain the summarization queue,
> render, and commit.

Two things to know:

- **The container is ephemeral.** Each firing starts from a fresh clone. State
  that must survive lives in `data/` and has to be committed at the end of the
  run — which is why `data/index/seen.sqlite` is tracked despite being a binary.
- **A firing that does nothing is normal.** Quiet days happen; the digest will
  say so.

If you would rather run collection on a plain schedule and read the queue when
convenient, `scripts/daily.sh` is safe to run from cron. The queue simply grows
until someone drains it.

## Stage by stage

### Collect

`pipelines/run_daily.py` asks each collector for items in the lookback window.

| Source | How | Failure mode |
| --- | --- | --- |
| arXiv | Atom API, one query per topic per keyword chunk | 3s minimum between requests; long queries are rejected, hence the chunking |
| Semantic Scholar | bulk search, optional API key | anonymous requests are rate limited; set `SEMANTIC_SCHOLAR_API_KEY` if it bites |
| OpenReview | `content.venueid` lookup per venue per year | venue ids change between cycles; a miss is silent by design |
| DBLP | keyword + venue search | no abstracts, so scoring sees the title only |
| YouTube | channel Atom feed, no key | feeds carry no duration, so short videos cannot be filtered out |

The date filter is on submission, not revision. A v2 of an older paper does not
resurface; if it reaches the archive through another index, the merge in
`enrich/dedupe.py` folds it into the existing record.

### Score

`enrich/score.py` is a keyword rule, on purpose — you can read it, disagree with
it, and fix it in the topic's YAML.

For each topic: any `keywords.none` hit rejects the item; every `keywords.all`
term must appear; at least one `keywords.any` term must appear. Surviving hits
are weighted (title hits count triple by default), tracked authors add a bonus,
and the total is squashed into `(0, 1)` so one title hit lands at `0.50` and
further hits add progressively less. Items below `min_score` are recorded in
`data/index/rejected.jsonl` and go no further — the record of what was
considered and dropped is what lets you tune the threshold later without
re-collecting.

### Deduplicate

The same paper arrives from three indexes. Identity is arXiv id, then DOI, then
a normalized-title fingerprint, and all known aliases for a work map to one
canonical id in `data/index/seen.sqlite`. Merging fills empty fields rather than
overwriting: an abstract from arXiv and a venue from proceedings both survive.

### Queue and read

One task per unsummarized item, in `data/queue/pending/`. Each is self-contained
— instructions, output schema, source material — so it can be answered with no
other context. Results are validated on submission and land in
`data/queue/done/`.

`summarize.backend` in `config/settings.yaml` selects who answers:

- `queue` (default) — the daily session. No API key, no cost.
- `anthropic` / `ollama` — interface only. The prompts and schemas in
  `pipelines/common/llm.py` are the contract; implementing either backend means
  filling in two methods, and nothing else in the pipeline changes.

### Render

`pipelines/render.py` applies finished tasks, rewrites every page, updates the
wiki, and regenerates the outputs. It never fetches and never calls a model, so
it is always safe to rerun.

The wiki step is where the archive extends itself. Entities named in summaries
accumulate evidence in `data/concepts/`; once one has been seen in enough
independent sources (`wiki.promote_after_mentions`, default 2) it is promoted to
a note of its own and a definition task is queued. So the wiki grows a new,
properly written note whenever the literature starts converging on a term —
without anyone asking for it.

Notes are half generated, half yours:

```markdown
# Instrumental Variable
<!-- auto:begin -->
... regenerated on every render ...
<!-- auto:end -->

## Notes
Everything here is preserved forever.
```

A note whose entity stops appearing is deleted — unless you wrote something in
the manual section, in which case it stays.

## Troubleshooting

| Symptom | Cause | Fix |
| --- | --- | --- |
| `no topics to run` | no topic files, or all are `_`-prefixed | `scripts/new_topic.sh "Name"` |
| Collection returns nothing | keywords too narrow, wrong arXiv categories or venues, or window too short | `--dry-run --days 30` to check, then widen `config/sources.yaml` |
| `queue is at its cap` | more matches than `max_pending_tasks` | drain the queue, or raise the cap |
| Result rejected on submit | a required field is empty | the error names the field |
| Wiki note lost its text | it was written inside the auto block | put it after `<!-- auto:end -->` |
| Everything looks stale | records fine, renders old | `python3 -m pipelines.render` |

To rebuild every generated file from scratch:

```bash
rm -rf archive wiki outputs
python3 -m pipelines.render
```

`data/` is untouched by that, so nothing is re-fetched.
