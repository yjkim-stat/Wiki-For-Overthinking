# The daily routine

How the automation actually runs, and what to check when it misbehaves.

## The two halves

The system splits cleanly at the work queue.

```
                        deterministic                    judgement
                 ┌──────────────────────────┐   ┌──────────────────────┐

  arXiv ──┐
  venues ─┤
  curated ┼─► collect ─► score ─► dedupe ─► store ─► queue ─► read ─► complete
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

When the archive lives in a repository of its own, the scheduled job has two
clones to keep current and must say which tree it works in — `RA_WM_ROOT` in the
environment, or `--root`, which `daily.sh` forwards to every stage. The commit
at the end of the run belongs to the archive's repository, not the code's.
[`workflows/deployment/`](../workflows/deployment/) has the full procedure.

<!-- LOCAL: this archive's actual routine state. See LOCAL-DELTAS.md -->
### This archive's routine — currently paused

A Routine did run nightly for this archive and **is disabled as of 2026-08-09,
at the user's request, for resource reasons. Do not re-enable it without being
asked.** The cron expression and prompt are intact, so resuming is a one-field
update rather than a re-creation.

| | |
| --- | --- |
| ID | `trig_018yxS27DM2m7HbgLP7MfvZ7` |
| Name | ra-lrm daily literature archive |
| Schedule | `0 22 * * *` UTC = 07:00 KST |
| State | `enabled: false` |

Three things to settle in the same call that re-enables it:

- **Which repository it clones.** The prompt lives in the trigger's `job_config`,
  not in any checkout, so editing a repository does not reach it. It was written
  to clone the archive's own repository; this tree is a different one. Point it
  at whichever is authoritative, or it will advance the other archive and the two
  will diverge from the same starting point.
- **Where it writes commit notes.** Its step 7 names `docs/commit/NNNN-slug.md`,
  which is correct for this repository and was not for the one it was written
  against. See [`LOCAL-DELTAS.md`](LOCAL-DELTAS.md).
- **The sweep caps.** `max_abstracts_per_run: 120` and
  `virtual_site.max_details_per_run: 60` in `config/sources.yaml` were tuned for
  a three-topic archive and this one tracks five. Consider halving them for the
  first unattended night and reading what the run reports.

On the first run back, `collect.lookback_days` is **2**, so it sees two days
regardless of how long the pause lasted. Widen it once with
`run_daily --days N` to cover the gap, then let it fall back — `seen.sqlite` is
tracked, so a pause creates a gap in collection, never duplicate work.

And once it is running, **"no new commit" means either a quiet collection day or
a failed run, and those must be told apart rather than assumed.** This routine
has failed silently before: on 2026-08-08 it collected for thirty minutes, left
its only commit until the end, ran out of session, and the archive gained
nothing — including the collection. Committing after every step is what fixed
it, and it is safe because `data/queue/` and `seen.sqlite` are tracked.
<!-- /LOCAL -->

## Stage by stage

### Collect

`pipelines/run_daily.py` asks each collector for items in the lookback window.

| Source | How | Failure mode |
| --- | --- | --- |
| `inbox/` | Any PDF in the folder, hashed and moved to `data/pdfs/` | none worth speaking of; a file it cannot move is logged and left in place |
| arXiv | Atom API, one query per topic per keyword chunk | 3s minimum between requests; long queries are rejected, hence the chunking |
| Semantic Scholar | bulk search, optional API key | anonymous requests are rate limited; set `SEMANTIC_SCHOLAR_API_KEY` if it bites |
| OpenReview | `content.venueid` lookup per venue per year | venue ids change between cycles; a miss is silent by design |
| DBLP | keyword + venue search | no abstracts, so scoring sees the title only |
| curated lists | a weekly editor's picks, read as markdown; the arXiv id it links to is looked up for the bibliography | the page is one editor's markdown and can be reshaped without notice, so a parse of zero warns |
| YouTube | channel Atom feed, no key | feeds carry no duration, so short videos cannot be filtered out |

The date filter is on submission, not revision. A v2 of an older paper does not
resurface; if it reaches the archive through another index, the merge in
`enrich/dedupe.py` folds it into the existing record.

### Score

`enrich/score.py` is a keyword rule, on purpose — you can read it, disagree with
it, and fix it in the topic's YAML.

A PDF from `inbox/` is exempt: it is scored, so the topics it happens to match
are recorded, but it is never rejected. Filing it by hand is the decision that
scoring approximates, and the reader assigns its topics afterwards.

A curated pick is **not** exempt. Filing a PDF is the group's own editorial
decision; a weekly list is somebody else's, taken over a whole field rather than
over the group's topics. Most of a general list being rejected is the filter
working as intended.

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
| A dropped PDF never appeared | it is still in `inbox/`; collection has not run | `--source local`, or check `local.enabled` in `config/sources.yaml` |
| A dropped PDF is titled like a filename | it has been ingested but not read yet | drain the queue: the reading supplies the real title |
| Result rejected on submit | a required field is empty | the error names the field |
| Wiki note lost its text | it was written inside the auto block | put it after `<!-- auto:end -->` |
| Everything looks stale | records fine, renders old | `python3 -m pipelines.render` |
| Collected records the render cannot see | the two stages ran against different roots | `python3 -m pipelines.migrate status` — it prints the deployment root it resolved |
| An archive appeared in the code checkout | `RA_WM_ROOT` was unset for that run | see [`workflows/deployment/`](../workflows/deployment/) |

To rebuild every generated file from scratch:

```bash
rm -rf archive wiki outputs
python3 -m pipelines.render
```

`data/` is untouched by that, so nothing is re-fetched.
