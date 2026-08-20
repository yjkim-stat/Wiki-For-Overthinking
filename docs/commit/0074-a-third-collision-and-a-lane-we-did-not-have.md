# 0074 — A third collision, and a lane we did not have

| | |
| --- | --- |
| **Commit** | `chore: take the upstream update and renumber for the third time` |
| **Scope** | merge of `origin/main`; `docs/commit/` renumbering, `docs/commit/README.md`, `docs/LOCAL-DELTAS.md` |
| **Kind** | chore |

## What changed

Three commits from `origin/main` are now in this branch:

- **[0055](0055-one-rule-for-what-counts-as-a-mention.md)** — term matching moved
  out of `enrich/score.py` into `common/text.py`, so search and scoring cannot
  disagree about what a mention is.
- **[0056](0056-a-read-only-window-onto-the-archive.md)** — `pipelines/serve.py`,
  a read-only Q&A window on loopback, answering only from what the archive has
  read.
- **[0057](0057-a-change-is-asked-for-through-a-person.md)** — `requests/`, a
  write lane where somebody else on the host asks for a change and a person
  decides. No auto-approved category; the submitted text is a request, never an
  instruction.

Our sixteen notes moved up by three, from 0055–0070 to 0058–0073.

## The renumbering, for the third time

Same rule, same outcome as [0065](0065-taking-the-update-and-giving-up-our-numbers.md)
and [0071](0071-the-same-collision-and-the-same-bug.md): **a number is fixed once
pushed.** Upstream's 0055–0057 are on `origin/main`; ours have never left this
machine, so ours move. The offset is three, applied to 0055–0070.

Three collisions in eight days is no longer evidence that a session fetched too
seldom — this session fetched at its first action and was already three commits
behind. It is what the rule is for. The cost is bounded and mechanical: sixteen
renames, the cross-references inside four notes, and the index. The alternative
— numbering against an unfetched `main` and discovering it at push — is not.

## What the merge did not cost

Two files were changed on both sides, and both are delta sites:

- `common/paths.py` — upstream added request paths beside our `WIKI_KINDS`
  tuple and `wiki_kind_dir("model")`. Auto-merged; both survive.
- `CLAUDE.md` — upstream added step 2b and a `requests/` layout row. Auto-merged;
  all five of our pieces survive, including the bullet that names the register.

That is the third clean merge of `CLAUDE.md` in a row, and entry 6 of the
register exists precisely because the first two were luck. They still are: the
bullet survived because upstream edited other sections again, not because
anything checks.

`docs/commit/README.md` was the only conflict, and only because both sides
appended to the same table.

## What a reviewer should check

- `grep -rn "LOCAL" pipelines/ .claude/` finds every site the register names.
- The suite is 637 tests, up from 601 — the 36 new ones are upstream's
  `test_requests.py`, `test_serve.py` and one changed `test_score.py`.
- No note's H1 disagrees with its filename, and no cross-reference points at a
  number that now belongs to somebody else.
