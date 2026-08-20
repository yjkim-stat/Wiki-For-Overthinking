# 0091 — The fourth collision, and a lane that turned out to be two

| | |
| --- | --- |
| **Commit** | `chore: take the upstream update and renumber for the fourth time` |
| **Scope** | merge of `origin/main`; `pipelines/render.py`, `pipelines/enrich/queue.py`, `docs/commit/` renumbering, `docs/commit/README.md` |
| **Kind** | chore |

## What changed

Seven commits from `origin/main`, arriving as one merge of two upstream branches:

- **[0058](0058-a-stale-definition-is-asked-for-again.md)** — a definition whose
  evidence has outgrown it is re-asked as a task that *shows the reader the
  existing text*.
- **[0059](0059-an-identifier-learned-late-is-still-registered.md)** — an
  identifier a record gained after collection is now indexed. It registered 85
  on the first render here, across 63 papers.
- **[0060](0060-a-question-larger-than-one-reading.md)** — a synthesis task, for
  a question no single reading answers.
- **[0061](0061-a-look-outside-that-has-to-cite-what-it-saw.md)** — a lookup
  task, where every answer must cite a recorded reference.
- **[0070](0070-one-leverage-beside-the-scores-it-sums.md)**,
  **[0071](0071-which-end-of-the-backlog-to-drain.md)** — queue ordering by
  leverage, recency or topic, instead of by filename.
- **[0072](0072-two-names-for-one-entity.md)** — a duplicate-slug report that
  suggests and writes nothing.

Our eighteen notes moved from 0058–0075 to 0073–0090, an offset of fifteen.

## The renumbering, for the fourth time

Unchanged rule, unchanged outcome: upstream's numbers are pushed, ours are not.
What is new is that upstream's own sequence now has a gap — it holds 0058–0061
and 0070–0072 with nothing between — because the update is itself a merge of two
branches that numbered independently. Ours could have filled 0062–0069. They do
not: a number that reads as "between two upstream features" but belongs to
neither is worse than a gap, and the gap is upstream's to close.

## Two conflicts, both inside deltas

- **`render.py`** — upstream added `definitions_reasked` in the same region as
  our reserve release. Both survive, and the *order* is the decision: re-asks
  run before the release, because the reserve exists so the wiki is not starved
  by the reading backlog and a re-ask is wiki work like any other. Taking either
  side whole would have dropped the other.
- **`enrich/queue.py`** — an import block. Upstream added `RecordStore`,
  `slug_for` and `leverage`; ours has `placeholders`. Trivial, and worth naming
  only because an import conflict is the shape a delta disappears in most
  quietly.

## Upstream reached our own problem from the other side, twice

**0058 is the better answer to what this session spent the day doing.** We drove
`stale.definitions` from 328 to 0 by clearing each definition and re-deriving it
from a blank page — the documented procedure, via
`scripts/refresh_stale_definitions.py`. Upstream's re-ask shows the reader the
existing definition instead.

Both are defensible and they trade off against each other. `CLAUDE.md` argues
for the blank page: re-deriving against a conclusion you have already been told
tends to satisfy the conclusion rather than the evidence. Upstream argues for
the revision: a definition is authored work and a rewrite that cannot see it
loses whatever it got right. Nothing here is being undone — the 328 are derived
and current — but the next pass should use `definitions_reasked`, and
`refresh_stale_definitions.py` should be read as the bulk instrument it is
rather than the default.

**0061 is the pull half of a lane this session was building the push half of.**
A lookup task asks "is there published code for this?" and the answer must cite
a reference. The GitHub candidate lane, still unlanded, searches for
repositories nobody asked about. They are opposite directions onto one record
type and neither subsumes the other — but they should share the promotion path,
and the candidate lane should be able to answer a pending `artifact` lookup.
That is a wiring job, not a redesign.

## What a reviewer should check

- Every delta named in `docs/LOCAL-DELTAS.md` is still present:
  `grep -rn "LOCAL" pipelines/ .claude/`.
- The suite is 744 tests, up from 640.
- A real render against the archive: `stale` is `{definitions: 0, analysis: 0}`,
  `summaries_unread` 0, `definitions_undefined` 0.
- No note's H1 disagrees with its filename, and nothing in 0062–0069 exists.
