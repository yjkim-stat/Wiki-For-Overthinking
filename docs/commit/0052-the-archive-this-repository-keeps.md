# 0052 — The archive this repository keeps

| | |
| --- | --- |
| **Commit** | `archive: the LLM-reasoning archive moves into this repository` |
| **Scope** | `config/`, `data/`, `wiki/`, `archive/`, `outputs/`, `inbox/` |
| **Kind** | feature · breaking |

## What changed

This repository now holds a literature archive as well as the program that runs
one. It tracks five topics — `reasoning-training`, `test-time-scaling`,
`reasoning-faithfulness`, `reasoning-evaluation`, `reasoning-interpretability` —
and arrives with 183 paper records, 146 readings, 1399 wiki entities of which 242
carry a written definition, 249 wiki notes, 186 archive pages, and 37 reading
tasks still queued.

`config/topics/` gains the five topic files. `config/sources.yaml` is edited for
this literature rather than the generic default: arXiv categories led by `cs.CL`,
OpenReview disabled, this group's venue list, and the `conferences.abstracts`
block. Each of those four is marked `LOCAL` in the file.

## Why it is built this way

The repository previously described two roots — the code root that `git pull`
replaces, and the deployment root an archive accumulates in — and supported them
being different directories so that pulling code could never collide with a month
of readings. **They are the same directory here**, which is the documented
default and what a fresh clone does; `pipelines/migrate status` reports it as
"the same tree — the repository is run in place".

The consequence is worth stating because a rule elsewhere reads oddly under it:
`CLAUDE.md` warns that a digest commit landing in the code repository is the sign
that `--root` was not set. Here it is the intended arrangement, not the mistake.
Every other rule about the two roots is unaffected, because they were written for
the run-in-place case first.

`data/` is committed on purpose, including `data/index/seen.sqlite`. A scheduled
run starts from a fresh clone, so deduplication state that is not committed means
every run re-processes everything it has already seen. PDFs, announced-paper
abstracts, raw collector responses and logs stay gitignored: heavy, re-fetchable,
and in the case of documents not ours to redistribute. The **records** of all 94
documents are here, so the archive is complete in a fresh clone even though the
bytes are not.

## Trade-offs and rejected alternatives

**57 of the 94 PDFs were filed by hand and cannot be re-fetched.** They are
referenced by `local_path` on their records and exist only on the machine that
holds them. That is the one population a clone genuinely cannot reconstruct, and
it is why `pipelines/migrate` exists at all.

The alternative was keeping the archive in a repository of its own, which the
code fully supports and which this archive previously did. It was rejected by the
person who owns the archive. What it costs: this repository's history now
interleaves system changes with archive digests, and anyone copying the template
out of it gets an archive they did not ask for unless they delete these
directories. What it buys: one tree, one clone, and no possibility of the two
halves drifting or of a run writing to the wrong one.

Reading depth is not recoverable for what arrived. `PaperSummary.read_from`
(note [0044](0044-a-reading-says-what-it-was-based-on.md)) postdates all 146
readings, so every one of them records the basis as unknown rather than guessing
`abstract`. New readings will carry it.

## What a reviewer should check

- `python3 -m pipelines.render` twice in a row: the second run must change no
  record under `data/`. That is the strongest single proof the source of truth
  arrived intact, and it holds because a render is not an edit (note
  [0036](0036-a-render-is-not-an-edit.md)).
- Referential integrity: every `local_path` on a paper record names a file that
  exists. 94 records, 94 files.
- No absolute path anywhere in `data/` — every `local_path` and every task
  `attachments.pdf_path` is repository-relative, which is what lets the tree move
  at all.

## Downstream impact

**Breaking for anyone using this repository as a template.** `config/topics/`,
`config/sources.yaml`, `data/`, `wiki/`, `archive/` and `outputs/` now contain
real content rather than empty scaffolding. A project adopting the code should
delete those and run `scripts/new_topic.sh` rather than inherit somebody else's
literature. Nothing under `pipelines/` assumes any of it.
