# 0094 — The fifth update, and an index that had drifted

| | |
| --- | --- |
| **Commit** | `chore: take the upstream update; no renumbering, and five index rows restored` |
| **Scope** | merge of `origin/main`; `tests/test_render.py`, `docs/commit/README.md` |
| **Kind** | chore |

## What changed

Five commits from `origin/main`:

- **[0062](0062-a-position-its-subject-has-outgrown.md)** — a finding is now
  checked against its own sources the way a definition is. It sits above the
  evidence and went on reading the same at thirty sources as at three.
- **[0063](0063-a-night-that-collected-nothing.md)** — a night's reading is
  recorded inside the archive rather than only in a commit message.
- **[0064](0064-a-merge-with-a-person-in-it.md)** — fold one paper record into
  another, with the survivor named by a person.
- **[0065](0065-the-validator-takes-the-task.md)** — the result validator takes
  the task rather than five pieces of it.
- **[0066](0066-what-the-archive-was-asked-and-could-not-answer.md)** — `serve`
  leaves an unanswered question for review.

## No renumbering, for the first time in four updates

Upstream filled its own 0062–0066 gap; its highest is still 0072 and ours start
at 0073. Nothing collided.

That is the fourth renumber's decision paying off. It could have filled
0062–0069 and did not, on the grounds that a number reading as "between two
upstream features" but belonging to neither is worse than a gap. The gap was
upstream's to close, and upstream closed it.

## The conflict was a test we had both edited

`test_render.py`: upstream renamed `test_render_reports_both_counts` to
`…_every_count` because its result dict grew a field, in the same hunk as the
three tests [0090](0090-a-marker-can-be-wrong-in-two-directions.md) added for
the bidirectional analysis check. Both sides kept.

Worth noting what upstream's 0062 means for 0090: findings now carry the same
staleness check that definitions and analysis markers do. Three record types,
one rule — *written against N sources, standing at M* — and this repository
argued for the third of them a day before upstream added the second.

## The index had drifted, and nothing checks it

Five notes — 0089 through 0093 — existed on disk with **no row in
`docs/commit/README.md`**. Two lost their rows in the fourth renumber, which
rebuilt the table from the conflict region and silently dropped what fell
outside it; three were simply never added when the notes were written.

Nothing catches this. `CLAUDE.md` requires a note per commit and the skill
requires a row per note, but the row is a hand edit into a hand-maintained
table, and a missing one fails nothing. The index is how somebody decides what
to read; a note absent from it is a note nobody finds.

All five are restored, and both directions were audited — every note has a row,
every row has a note. A check for that is one loop and belongs in the suite;
it is not in this commit.

## What a reviewer should check

- The suite is 800 tests, up from 756.
- `for f in docs/commit/0*.md` finds no note without an index row, and no row
  points at a note that does not exist.
- `stale` in a render result now carries a third key from upstream's 0062.
