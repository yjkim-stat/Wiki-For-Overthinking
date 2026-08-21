# 0025 — Re-queue what the evidence outgrew

| | |
| --- | --- |
| **Commit** | `feat(scripts): re-queue wiki definitions their evidence has outgrown` |
| **Scope** | `scripts/refresh_stale_definitions.py` |
| **Kind** | feature |

## What changed

`scripts/refresh_stale_definitions.py` clears the `definition` field of concepts
whose source count has grown since the definition was written, so the next render
files a task to write them again. It thresholds on **growth** rather than on
staleness, sorts largest first, and defaults to a dry run.

Applied here with `--min-growth 6`: 32 of 100 stale definitions re-queued and
rewritten, leaving 68 below the threshold untouched.

## Why this exists

The template reports staleness and deliberately refuses to act on it — its own
docstring says re-deriving a definition means reading its sources, so a counter
must not discard written work on arithmetic alone. It documents the manual route:
clear `definition` in `data/concepts/<slug>.json` and render again.

That is the correct division and it does not scale. This archive reached 100
stale definitions in a single day's reading, and clearing 100 files by hand is
both tedious and the kind of thing that gets done carelessly. The script does the
mechanical half and leaves the judgement — which ones, and whether to rewrite at
all — with the threshold.

## Why growth is the right threshold

Staleness is a boolean and it is nearly useless at this size: 100 of 219
definitions were stale, which says only that the archive is growing. The
distribution is what matters, and it is very skewed.

| growth | count | what it means |
| --- | --- | --- |
| +1 to +2 | 42 | written against 2 sources, now 3 — almost certainly still correct |
| +3 to +5 | 26 | worth revisiting eventually |
| +6 and up | 32 | a different claim about a different body of evidence |
| +17 to +19 | 6 | `chain of thought` written against 3 sources, now 20 |

A definition written for 3 sources when 20 now exist is not out of date, it is
about a different thing. Sorting by `sources_now - written_for` puts those first,
and `--min-growth` is how a maintainer declines the long tail rather than being
forced to rewrite it or leave the report permanently red.

## Why it clears only `definition`

Aliases and related links accumulate rather than go stale — a name a paper used
is still a name that paper used. The `kind` is left alone for a stronger reason:
the template defends a kind that a definition task ruled on against being
reverted by harvest, and clearing it here would throw away exactly that decision.
Only the prose summary of the evidence is re-derived, because only it makes a
claim about a body of sources that has since changed.

## Trade-offs and rejected alternatives

- *Having `render` re-queue automatically above some threshold.* Rejected for the
  reason the template gives: a definition is written work, and a render that
  silently discards it on a counter would make every render destructive. Keeping
  this a separate, explicit, dry-run-by-default command preserves that.
- *Archiving the old definition before clearing it.* Tempting, and unnecessary —
  git already holds it, and adding a graveyard field to the record would put a
  second definition in a store whose value is that it holds one.
- *Thresholding on a ratio rather than a difference.* Considered: 2 to 4 sources
  doubles, 3 to 20 does not. But doubling from a small base is exactly the case
  that does not need rewriting, so the ratio ranks the wrong things first.
- *Rewriting all 100.* Rejected on judgement, not effort: 42 of them changed by
  one or two sources, and rewriting a correct definition risks losing a good
  phrasing for no gain.

## What a reviewer should check

- `python3 -m unittest discover -s tests -t .` — 337 tests, unchanged. This adds
  a script and no library code.
- That a bare run prints a plan and writes nothing, and that `--apply` is needed.
- That `stale` in the next render's output falls by exactly the number cleared —
  100 to 68 here.
- The property worth preserving if this is rewritten: it must not touch `kind`,
  `aliases` or `related`. Only `definition` is re-derivable from sources.

## Downstream impact

Additive; nothing calls it. A deployment that has never re-read its wiki will
find a large stale count on first run — that is the backlog becoming visible, not
a new problem. Re-queued definitions occupy the queue like any other task, so
running it with a low `--min-growth` on a large archive can fill the queue at the
expense of unread papers; the definition-queue reserve (note 0022) bounds that in
the other direction.
