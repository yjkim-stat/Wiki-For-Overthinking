# Issues

A defect or a design question that has been investigated but not yet acted on.
One file per issue, named for the symptom rather than the fix, because the fix
is what is still being decided.

When one is solved it moves to [`../solved/`](../solved/) with a **Resolution**
section appended: which option was taken, what the document left open and how
each of those turned out. The file is not deleted and not rewritten — the
investigation is most of its value, and a reader a year from now needs to see
what was considered and rejected, not only what was built.

## The difference from `docs/commit/`

A commit note explains a change that happened. An issue explains a problem that
has not been fixed yet, usually in more depth than the eventual note will,
because it has to argue that the problem is real before anyone will spend a day
on it. The two point at each other: the resolution names its note, the note
names the issue.

## What belongs in one

Whatever it takes to hand the problem to somebody else:

- **What you can observe** — the commands, and what comes back. A defect nobody
  can reproduce is a rumour.
- **Why it happens** — the specific lines, in the order they run.
- **Why it matters** — especially when the failure is silent, which is the kind
  this repository keeps finding.
- **Options**, each with what it costs if it turns out to be wrong.
- **Tests**, including the honest statement that there are none today.

The reviewer checklist at the foot is not a formality. In the first issue filed
here it was the thing that caught a docstring the fix had made false.
