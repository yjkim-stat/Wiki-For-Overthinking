# 0012 — Applying a topic change to what is already stored

| | |
| --- | --- |
| **Commit** | `feat(scripts): re-score stored records against current topics` |
| **Scope** | `scripts/retopic.py` |
| **Kind** | feature |

## What changed

`scripts/retopic.py` re-scores stored papers and videos against the topics as
they are defined now, and adds any slug that accepts them.

Topics are matched at collection time, which is correct — a run should be
reproducible from what the collectors saw — but it means editing
`config/topics/` only changes what arrives next. Add a topic, or widen a topic's
keywords, and the existing archive keeps describing the previous editorial
decision. Before this the only remedies were re-collecting everything or
hand-editing `data/`, and neither is acceptable.

Two flags shape the operation: `--dry-run` reports without writing, and
`--topic SLUG` (repeatable) restricts it to named slugs.

## Why it is built this way

**It only ever adds.** A slug already on a record is never removed, for two
different reasons that happen to agree. For a hand-filed PDF the topics are the
reader's judgement, and a keyword rule must not overrule an editorial decision —
that is the whole basis on which `inbox/` PDFs bypass scoring in the first place.
For a collected item, removing a slug would silently delete an archive page and
the topic outputs built from it, which is a destructive act that a re-scoring
pass has no business performing. Dropping a topic is done by deleting its file
and letting the renderer clean up, where the effect is visible.

**`--topic` exists because the unrestricted run is usually wrong.** Scoring is
generous by design, so a full re-score attaches slugs no reader ever assigned.
Those records have no `relevance` entry for the new slug, so the topic's report
lists the paper with nothing explaining why it is there — the archive gets wider
and thinner at once. Restricting to the slug that actually changed keeps the
operation reviewable and the outputs honest. On this deployment the difference
was 9 records under a full re-score against 5 under `--topic`, and the 4
additional ones were keyword coincidences.

**It is a script, not a `render` flag.** `render.py` is safe to re-run precisely
because it never fetches and never decides anything; it is a pure function of
`data/`. Re-scoring changes `data/`, so folding it into render would make the
one always-safe command capable of rewriting the source of truth.

## Trade-offs and rejected alternatives

- *Re-scoring automatically inside `run_daily`.* Rejected: a daily run would
  then silently rewrite the topic assignments of old records whenever someone
  edited a keyword, with the change buried in a routine digest commit.
- *Allowing removal behind a `--prune` flag.* Rejected for now: the destructive
  case is rare, the safe path (delete the topic file) already exists, and a flag
  that deletes archive pages deserves its own commit and note if it is ever
  wanted.
- *Rewriting `relevance` for newly added topics.* Out of scope — that is a
  reading, not a scoring decision, and belongs in the queue.

## What a reviewer should check

- `--dry-run` writes nothing: run it twice and confirm `data/papers/` is
  unchanged (`git status`).
- An unknown slug is refused rather than silently ignored:
  `python3 scripts/retopic.py --topic nope --dry-run` exits 2.
- Idempotence: a second run after a real one reports 0 records.
- The suite is unaffected: `python3 -m unittest discover -s tests -t .` — 149
  tests. Note that the script is not covered by it; that gap is real.

## Downstream impact

None until run. The script is additive and off by default, and no existing
command calls it. Deployments that never edit a topic after collection will
never need it.
