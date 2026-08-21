# Harness — commit and push

Most of this workflow is enforced by nobody. Knowing which parts is the point of
this page.

## Checked mechanically

| Guard | Catches |
| --- | --- |
| `python3 -m unittest discover -s tests -t .` | 416 tests. Run it before every commit, not only when you think you changed behaviour — the layering and churn guards fail on changes that look inert |
| `git push` rejection | Someone else pushed first. Fetch and rebase; never force |
| `git merge --ff-only` | A divergence you have not noticed. It refuses rather than making a merge commit you did not intend |
| `.gitignore` | The heavy, un-redistributable half of the archive. Verify with `git check-ignore -v <path>` when adding a directory |

## Checked only by you

- **That the split is one idea per commit.** Nothing measures this. The test is
  the note: if a section is hard to write, the split is wrong.
- **That `NNNN` is free.** `ls docs/commit/` reads *your* checkout. It is right
  only if you fetched first, and it stays right only until another session
  pushes. There is no lock, no reservation, no check at commit time — the
  collision surfaces at merge.
- **That the note is true.** Notes 0031 and 0037 both record drafts that were
  plausible and false: one about how sessions go stale, one asserting a
  schema-migration rule that does not exist in this codebase. Check the claim
  against the code before you write it down.
- **That the note is staged with its commit.** A note arriving one commit later
  is a note nobody trusts.

## Why there is no hook

A pre-commit hook could refuse a commit with no note. It was considered and
rejected in [`docs/commit/0031`](../../docs/commit/0031-fetch-before-you-start.md):
it would catch the commit but not the hours of work already built on a stale
base, and the cheap moment to notice is before the first edit — when nothing
mechanical is running.

The same reasoning covers numbering. A hook could check `NNNN` is unused
locally, which is exactly the check that already fails, because the problem is
never local.

## Verifying after the fact

```bash
ls docs/commit/ | tail -5                       # the numbers in play
git log --oneline origin/main..HEAD             # what is unpushed
git log --format='%s' -20 | grep -v '^archive:' # commits that should carry a note
grep -c '^| 0' docs/commit/README.md            # index rows, against file count
ls docs/commit/[0-9]*.md | wc -l
```

The last two should agree. They are the cheapest way to spot a note that landed
without its index row, or an index row pointing at a file nobody wrote.
