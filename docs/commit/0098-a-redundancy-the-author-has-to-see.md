# 0098 — A redundancy the author has to see

| | |
| --- | --- |
| **Commit** | `feat(config): report keyword pairs that score the same words twice` |
| **Scope** | `pipelines/common/config.py`, `pipelines/run_daily.py`, `tests/test_keyword_overlap.py`, `docs/issues/`, `docs/solved/` |
| **Kind** | feature |

## What changed

Four tracked keyword pairs have one term inside another — `chain of thought`
inside `long chain of thought`, and three more — so a single occurrence in a
title matches both and adds to the score twice.

`config.overlapping_keywords` reports them, `run_daily` says them before it
collects, and a test pins the set. This closes the gap
[note 0017](0017-keywords-match-regular-plurals.md) named: *"a redundancy check
belongs in the test suite or a config check; it is not there yet."*

## Why it is built this way

**The scorer is untouched.** Making it count the longest match only is correct
and puts span bookkeeping into a function whose whole value is that it can be
read in one sitting. `enrich/score.py` says so in its first paragraph, and the
cost of that simplicity — redundancy is the author's problem — is a cost worth
paying if somebody tells the author.

**The check uses the scorer's own matcher.** The obvious version is `short in
long`, which agrees on all four live pairs and would also flag `ate` inside
`state` — a pair that never double-counts, because `common/text.py` matches on
word boundaries. A check that disagreed with the scorer about what an occurrence
is would report pairs costing nothing and miss pairs that cost. That is the
whole reason the matcher was moved to one place in
[note 0055](0055-one-rule-for-what-counts-as-a-mention.md).

**The four pairs are recorded, not resolved.** Which term to drop is an
editorial decision about what a topic tracks, and `CLAUDE.md` reserves those. The
short term has broader recall; the long one is presumably there to weight a
specific phrase higher. Dropping either loses something real, so the test carries
them as a baseline and **a fifth fails the suite**.

**Both a run warning and a test.** The warning reaches whoever just edited a
topic file, at the moment they run a collection. The test is the gate, because —
as this repository worked out one issue earlier the same day — a warning in a log
nobody reads is barely better than nothing.

## Trade-offs and rejected alternatives

**A baseline list is a known-issues list**, and those rot if nobody revisits
them. Its comment names the issue and the date, and removing a row is part of the
same edit as the topic file, so it cannot drift from `config/` without the suite
saying so.

**`allow_overlap` was not added.** The issue framed it as a prerequisite for a
hard failure. A pinned baseline is a hard failure needing no flag: a pair is
expressed by being in the list, and the comment says it is unresolved rather than
approved. A per-topic flag is a smaller change from here if the group wants one.

**Nothing measures the actual inflation.** The issue did: a paper titled "…long
chain of thought…" scores 0.50 instead of 0.667, and across the batch checked it
flipped **zero** acceptance decisions, because one match already clears
`min_score`. The reason to fix it is that the score also orders the
abstract-fetch budget and the sweep backlog, and that this class of bug starts
mattering the moment somebody tunes a threshold against numbers that are quietly
wrong.

## What a reviewer should check

Three mutations: use `short in long` instead of the matcher (the `ate`/`state`
test fails), add a fifth pair to a topic file (the baseline fails, plus three
tests that score against those keywords), and remove the run warning.

- `test_it_uses_the_scorer_s_matcher_not_a_substring_test` is the one that keeps
  this honest about what double-counting means.
- `test_no_overlap_has_appeared_that_nobody_recorded` is the gate.

## Downstream impact

A deployment whose topics contain an overlapping pair sees a warning at the top
of every collection run. No score changes, no paper is accepted or rejected
differently, and no topic file is edited.
