# Commit and push

Authority is the [`commit-notes` skill](../../.claude/skills/commit-notes/SKILL.md);
this is the sequence and the two failure modes that have actually happened here.
The harness is in [`harness.md`](harness.md).

**This repository is deployed into other projects and its history is read as
documentation.** That is the whole reason for the ceremony below: a commit
message is one screen, and the note in `docs/commit/` is the page that survives.

## When a note is required

| Change | Note? |
| --- | --- |
| A routine archive digest — records, summaries, wiki, outputs | No |
| Code, config, templates, documentation, tests, skills | **Yes** |

## Procedure

**0. Fetch first. Before the first edit, and again before merging.**

```bash
git fetch origin main
git log --oneline HEAD..origin/main     # anything here means you are behind
```

More than one session commits here, and a container that has been alive a while
holds a `main` that has moved underneath it. If you are behind, rebase now —
resolving one collision is cheaper than unpicking a branch later.

**1. Read the diff before splitting it.**

```bash
git status --short && git diff && git diff --staged
```

Split by **idea**, never by file type or directory. One commit is one decision
a reviewer could accept or reject on its own. A rename and the behaviour change
it enabled are two commits; three unrelated typo fixes are one. If it genuinely
belongs together, one commit is right — say so in the note.

**2. Pick the number against the fetched `origin/main`.**

```bash
ls docs/commit/
```

`docs/commit/NNNN-kebab-slug.md`, four digits, commit order. **A number is fixed
once pushed**, so the session that duplicates one is the session that renumbers.

**3. Write the note before committing.** Template in the skill. If a section is
hard to fill in, the split is usually wrong. Sections with nothing in them get
one honest line, not filler.

**4. Add the row to [`docs/commit/README.md`](../../docs/commit/README.md).**
That index is the only thing anyone skims before deciding which note to open.

**5. Run the suite.**

```bash
python3 -m unittest discover -s tests -t .
```

**6. Commit — note staged in the same commit.** The message announces; the note
explains. Do not paste one into the other.

```
feat(collect): follow curated weekly lists as a source of pointers

<two or three sentences of why>

Notes: docs/commit/0032-following-somebody-elses-reading.md
```

**7. Push.**

```bash
git push -u origin <branch>
```

On a network failure retry up to four times with exponential backoff (2s, 4s,
8s, 16s). Only network failures — a rejected push means fetch and rebase.

## Merging to `main`

Fetch, confirm you are not behind, fast-forward, push, then go back to the work
branch so the next edit does not land on `main` by accident.

```bash
git fetch origin main && git log --oneline HEAD..origin/main   # must be empty
git checkout main && git merge --ff-only <branch>
git push -u origin main
git checkout <branch>
```

## The two failure modes, both of which happened here

**A duplicate note number.** Two sessions each read a stale `docs/commit/` and
both wrote `NNNN`. It surfaces only at merge. Note 0026 collided and had to
become 0027 — which is why step 0 exists and why step 2 says *fetched*.

**Work built on a reversed decision.** `docs/API.html` documented
`data/abstracts/` as committed while another session was gitignoring it. The
page was wrong the day it was written, and nothing in the code said so.

## Never rewrite a pushed note

Append a `## Correction (NNNN)` section saying what was wrong and linking the
note that supersedes it. Same principle as a superseded finding: why the
repository used to think otherwise is part of the record.
