# 0063 — A night that collected nothing

| | |
| --- | --- |
| **Commit** | `feat(digest): record what a night of reading did` |
| **Scope** | `pipelines/digest.py`, `tests/test_digest.py`, `CLAUDE.md`, `README.md` |
| **Kind** | feature |

## What changed

`archive/daily/<date>.md` was written by `run_daily` and by nothing else, so a
night that read papers and settled questions but collected none left **no trace
inside the archive**. The work survived in a commit message — outside the thing
it is about, and invisible to anybody browsing it.

`python3 -m pipelines.digest` writes the session's half of that page.
Requirement R8, and the last of the dream-mode specification.

## Why it is built this way

**Derived, not remembered.** The command has no memory of the session and no way
to acquire one: it reads what the records now say and reports the difference a
date makes. That is what lets it be run at any time, twice, or a week later for
a day that has passed — and it is why it can count the tasks answered today and
**cannot** know which wiki note somebody wrote a paragraph in. Nothing records
that, and a guess from a file's modification time would be wrong every time a
render touched the auto block.

So the derived block ends where the derivable facts end, and everything after
`<!-- session:end -->` is preserved for ever, exactly as in a wiki note. That is
where a session says what only it knows. The alternative — having the command
take prose on the command line — would put the archive's reasoning in a shell
history.

**It shares the page rather than taking it.** `run_daily`'s half stays above; a
day with both a collection and a session ends up as one page describing both,
which is what a directory of dates is for. Re-running replaces the block in
place, so a digest cannot stack copies of itself.

**The last section is an input, not a record.** *What was left for the next
night* — the pending queue by kind, how long the oldest has waited, definitions
their evidence has outgrown, findings their subject has outgrown, prose outgrown
by its sources. Those had to be rediscovered by running four commands and
remembering what each number meant. They are owed work whatever produced them,
so they are listed together.

**`archive/daily/` is the one directory a rebuild leaves alone**, which is what
makes writing here safe at all — `rebuild_archive` clears `papers/` and
`seminars/` before regenerating and says in a comment why the digests are
exempt. A test asserts a render does not remove the section.

## Trade-offs and rejected alternatives

**"Notes you wrote prose in" is a named requirement and is not delivered
mechanically.** It cannot be: nothing records when the manual half of a note
changed, and the auto block's rewrite destroys the only filesystem signal. Rather
than approximate it with something wrong, the page leaves the space and the
session writes it. Stated here so it is not rediscovered as a gap.

**It is not run by `render` or `daily.sh`.** A digest is the end of a session,
and a session ends when a person or an agent decides it has — not when a
rebuild finishes. Running it automatically would produce a page every time
anybody regenerated an artifact.

**Reading every archived task to find today's** is O(tasks) per run and the
queue archive grows without bound. Fine at the thousands this holds; if it ever
matters, `completed_at` is in the filename's neighbours and an index would be
the fix, not a cap.

**It writes no record**, only `archive/`. Asserted, because a command that reads
the whole archive to summarise it is one careless line from writing to it.

## What a reviewer should check

Four mutations, each taking down its own test: append instead of replacing the
block (copies stack), drop the branch that keeps existing content (`run_daily`'s
half is lost), stop filtering by date (yesterday's work is reported as
tonight's), and omit the "left for the next night" section.

- `test_prose_after_the_marker_survives_a_rewrite` asserts both halves: the
  prose is kept *and* the block still updates. Either alone is satisfiable by
  broken code.
- `test_a_render_does_not_clear_the_day`, because the whole feature depends on
  that exemption continuing to hold.

## Downstream impact

New command, run by nothing automatically. A deployment that never runs it sees
no change; one that does gets a section added to today's page and nothing else
touched.
