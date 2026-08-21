---
name: commit-notes
description: Use before every git commit in this repository. Splits pending work into commits that each carry one idea, and writes a reviewer-facing note in docs/commit/ for each one. Triggers on any request to commit, to stage and commit, to push, or to open a PR from uncommitted work.
---

# Writing commit notes

This repository is a template. It gets copied into other projects, and the
people who copy it read the history to decide what to keep, what to rip out,
and what a change was actually for. A commit message is one screen; the note in
`docs/commit/` is the page that survives.

So: **no commit lands without a note.** Run this before `git commit`, every
time, including for small changes.

## Procedure

**1. Read the diff before splitting it.**

```bash
git status --short
git diff
git diff --staged
```

Never split by file type or by directory out of habit. Split by *idea*: one
commit is one decision a reviewer could accept or reject on its own. A rename
plus the behaviour change it enabled are two commits. Three unrelated typo
fixes are one.

If everything genuinely belongs together, one commit is the right answer — say
so in the note rather than inventing a split.

**2. Pick the next number.**

```bash
ls docs/commit/
```

Notes are `docs/commit/NNNN-kebab-slug.md`, numbered in commit order, zero
padded to four digits. The number never changes once pushed; a note that turns
out to be wrong gets a correction section, not a rewrite of history.

**3. Write one note per commit**, using the template below. Write it *before*
committing, so the note is what you commit against — if a section is hard to
fill in, the split is usually wrong.

**4. Stage the note with the commit it describes.** The note and the change it
explains are the same commit. A note that arrives one commit later is a note
nobody trusts.

**5. Add the row to `docs/commit/README.md`.** That index is the only thing
somebody skims before deciding which note to open.

**6. Commit**, with a message whose subject repeats the note's title and whose
body points at the note:

```
feat(enrich): score, deduplicate, and queue what needs reading

<two or three sentences of why>

Notes: docs/commit/0004-scoring-dedup-and-the-queue.md
```

## The note template

```markdown
# NNNN — Title

| | |
| --- | --- |
| **Commit** | `<subject line>` |
| **Scope** | `<paths touched>` |
| **Kind** | feature · fix · refactor · docs · chore · breaking |

## What changed

What a reader gets that they did not have before, in plain terms. Not a
restatement of the diff — the diff is right there.

## Why it is built this way

The design philosophy behind the change: the constraint it respects, the
property it preserves, the thing it deliberately refuses to do. This is the
section the template's users actually need, because it tells them which parts
are load-bearing and which are taste.

## Trade-offs and rejected alternatives

What this costs, and what was considered and not done. Be specific enough that
someone can reopen the decision with new information.

## What a reviewer should check

The two or three things most likely to be wrong, and how to see for yourself —
a command to run, a file to read, an invariant to test.

## Downstream impact

What changes for a project that has already deployed this repository: config
that must be edited, files that will be regenerated differently, nothing at
all. Say "none" when it is none.
```

Sections that have nothing in them get one honest line, not filler. A note with
five paragraphs of hedging is worse than a note with five sentences.

## Rules

- **The note explains, the message announces.** Do not paste the note into the
  commit message, and do not let the message carry reasoning that is missing
  from the note.
- **Write for someone who was not here.** No "as discussed", no "per the
  earlier fix", no unexplained pronouns pointing at this session.
- **State the philosophy, not the compliment.** "Collection never calls a model,
  so a failed reading costs summaries and not a day of collection" is useful.
  "Clean, well-designed separation of concerns" is not.
- **Breaking changes are named in the title.** If a downstream repository has to
  edit a file after pulling, the word "breaking" belongs in the note's Kind row
  and the migration belongs under Downstream impact.
- **Never rewrite a pushed note.** Append a `## Correction (NNNN)` section that
  says what was wrong and links the note that supersedes it.
