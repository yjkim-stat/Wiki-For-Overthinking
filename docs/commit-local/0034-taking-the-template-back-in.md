# 0074 — Taking the template back in

| | |
| --- | --- |
| **Commit** | `merge: take the template's 0058-0072 into this deployment` |
| **Scope** | merge of `src/main` into `master`; `docs/commit/README.md`, `config/settings.yaml`, note 0058 renumbered to 0073 |
| **Kind** | chore |

## What changed

This deployment was forked from the template repository (the `src` remote) at
`5809d32` and had since grown one code change of its own. The template had grown
thirteen. This merge takes them in.

Arriving from upstream: `pipelines/duplicates.py` (report concept slugs that are
probably one entity), `pipelines/digest.py`, `pipelines/enrich/lookup.py`,
`pipelines/enrich/synthesis.py`, queue ordering by leverage/recency/topic,
definition-refresh tasks, finding-staleness reporting, paper-record merging with
a human-named survivor, late-identifier registration, and the validator
refactor. Their notes are 0058-0066 and 0070-0072 and say why each exists.

Two things were decided here rather than upstream, and this note exists for
them.

## Why it is built this way

**Our note 0058 became 0073.** Both sides had written an 0058 against the same
fetched `origin/main`, which is exactly the collision `CLAUDE.md` step 0
describes. Upstream's was pushed first and upstream's block is contiguous
(0058-0066, then 0070-0072 reserved for a parallel session), so this side
renumbered. A number is fixed once pushed; the session that duplicates one is
the session that moves.

**`concepts.py` keeps this deployment's year-variant merge, and upstream's
`duplicates.py` arrives alongside it.** These two answer the same question in
opposite directions, so the divergence is deliberate and worth stating.

Note 0073 auto-merges entity names differing only in punctuation, spacing, or a
bare two-digit trailing year (`AIME24` / `AIME 2024` / `AIME2024`). Note 0072
argues against automatic merging in general: merging is irreversible in the
direction that matters, and "attention"/"attentions" and "GAN"/"GAN inversion"
are the same shape to a string rule while being different answers.

That argument is right, and 0073 does not contradict it — 0073 merges only where
the two names denote the same *dated instance of one benchmark*, which is the
one case where the shape does settle it. Everything 0072 warns about (plurals,
separators, edit distance) is left to `duplicates.py`, which reports and writes
nothing. The two are complementary: one closes a case with no judgement in it,
the other surfaces the cases that have.

The alternative — reverting 0073 to match upstream exactly — was rejected because
its merge has already been applied to this archive's records. Reverting the code
would not un-merge the data; it would only let the next year-variant split again
and disagree with what is already there.

**`wiki.refresh_definition_at` is set to `2.0` rather than upstream's `0`.**
Upstream ships it off so that upgrading grows nobody's queue. This deployment
has thirty-six definitions its evidence has already outgrown, produced by a
single day that took the archive from 9 papers to 278. The manual route in use
until now — clearing `definition` and rendering — throws the previous ruling away
along with the staleness, and most of a ruling is usually still right. Turning
this on is the whole reason the merge happened when it did.

## Trade-offs and rejected alternatives

Merging a template into a deployment that has diverged is not free: every future
pull now has to reason about `concepts.py` again, because it is the one file the
two histories disagree about. The alternative was to keep cherry-picking, which
spreads that cost over every future pull instead of paying it once.

`max_refresh_tasks` is left at upstream's `5`. With thirty-six outgrown
definitions that is seven renders' worth, which is the intended behaviour: worst
first, drained over several passes, rather than a backlog nobody can face.

## What a reviewer should check

- `python3 -m unittest discover -s tests -t .` — 722 tests, green after the
  merge. The `ERROR pipelines.migrate: verify:` lines are a test asserting on
  corrupt-bundle handling, not failures.
- `grep -n "_merge_key" pipelines/enrich/concepts.py` — 0073's logic survived the
  merge; upstream never touched this file, so git kept our side without a
  conflict. Worth confirming by eye rather than trusting that.
- `python3 -m pipelines.duplicates` — the new report, against a wiki that now
  holds 228 notes. On this archive it returns 249 candidates (plural 6, suffix
  168, near 75) and writes nothing, which was confirmed by snapshotting
  `data/` and `wiki/` across a run.

  **Read its output as candidates, not as a worklist.** Its top hits here are
  `aime-2025` / `aime-2024` and `aime-2024` / `aime-2026`, flagged `near`
  because they are one edit apart — and those are the one family that must
  *not* be merged, since a different sitting of an exam is a different
  benchmark. That is 0072's argument arriving as evidence rather than as
  prose: the rule cannot tell "same thing, spelled twice" from "adjacent
  things, named alike", and it is right not to try. The families actually
  worth acting on here are the ones 0073 cannot reach — `grpo` /
  `group-relative-policy-optimization`, the `accuracy-*-tradeoff` group,
  `arc` / `arc-challenge` — and each still needs somebody to decide.
- `docs/commit/` has no duplicate number and no dangling link to the old
  `0058-a-benchmark-...` filename.

## Downstream impact

For this deployment: the next `render` will file up to five definition-revision
tasks, which did not exist before. Nothing else changes without being asked for
— `duplicates`, `digest`, `lookup` and `synthesis` are all commands somebody
runs.

For the template: none. Nothing was pushed to `src`, and nothing here asks it to
change. If the year-variant merge is wanted upstream it should be proposed there
as its own note, against 0072's reasoning rather than around it.
