# 0062 — Taking the update, and giving up our numbers

| | |
| --- | --- |
| **Commit** | `chore: take the upstream update and renumber our notes around it` |
| **Scope** | merge of `origin/main`; `docs/commit/` renumbering, `docs/commit/README.md`, `docs/LOCAL-DELTAS.md` |
| **Kind** | chore |

## What changed

Three commits from `origin/main` are now in this branch:

- **[0046](0046-the-pdf-cap-bounds-a-run.md)** — `pdf_fetch`'s `max_per_run`
  restarted on every paper, because collection fetches one document at a time as
  each task is filed. A `Budget` now carries the allowance across calls.
- **[0047](0047-a-filed-document-survives-its-merge.md)** — `merge_papers` did
  not carry `local_path`, so filing a PDF for a paper the archive already held
  produced a record that knew it was hand-filed and not where its file was.
- **[0048](0048-a-second-chance-at-a-document.md)** — `pipelines.backfill`, a
  bounded, re-runnable command that fetches documents for papers already queued
  and unread, which collection will never offer again because deduplication has
  seen them.

And our seven notes moved up by three, from 0046–0052 to 0049–0055, so that both
sequences fit in one directory. (They moved again on 2026-08-14, by a further
six, to 0055–0061 — see [0068](0068-the-same-collision-and-the-same-bug.md).
The account below is of the first move.) `docs/LOCAL-DELTAS.md` follows the one
cross-reference; nothing else pointed at a moved number. The index also gained
rows for the two notes that had been written without one.

## Why it is built this way

The collision is the one `CLAUDE.md` describes under step 0: two sessions each
numbered a note against a `docs/commit/` they had already read, and neither was
wrong at the time. It surfaced at the merge, exactly as predicted, as a conflict
in the index and three duplicated filename prefixes.

**The rule decides who moves: a number is fixed once pushed.** Upstream's
0046–0048 are on `origin/main`; ours were seven local commits that had never
left this machine. So ours move. That is not a courtesy — a pushed number may
already be cited from somewhere this repository cannot see, and a local one
cannot.

**The notes are renamed rather than rewritten, and history is left alone.**
Seven commit messages still carry a `Notes:` line naming the old filename, and
those lines are now wrong. Fixing them would mean rebasing thirty-five commits,
most of them large archive digests, in a repository other sessions are committing
to. Rewriting shared history to correct a filename is a much worse trade than a
stale path in a log message, and this note is the record that makes the old
paths followable: subtract three.

**The merge is a merge, not a cherry-pick.** Cherry-picking would have copied
the three commits under new hashes and left this branch permanently reported as
behind `origin/main`, so the next fetch would offer them again.

## Trade-offs and rejected alternatives

Renumbering upstream's three instead was rejected on the pushed-number rule
above, and would also have meant editing files that `docs/solved/` and
`docs/issues/` already link to by number.

Leaving both sequences as they were — two files starting `0046-`, two `0047-`,
two `0048-` — was rejected because the index cannot then be read at a glance and
a bare numeric reference resolves to whichever file sorts first, which is the
failure `docs/commit-local/README.md` already warns about for the other pair of
sequences in this repository.

The renumber is done inside the merge commit rather than after it, because the
intermediate state — a merged tree with a duplicated index — is not a state
worth committing.

## What a reviewer should check

- `ls docs/commit/ | cut -c1-4 | uniq -d` prints nothing.
- Every row in `docs/commit/README.md` links to a file that exists, and every
  file has a row.
- Each renamed note's `# NNNN —` heading matches its filename.
- `python3 -m unittest discover -s tests -t .` — the upstream commits add
  `tests/test_backfill.py` and `tests/test_filed_pdf_merge.py`, and none of the
  three touches a file carrying a `LOCAL` mark, so no delta from
  `docs/LOCAL-DELTAS.md` needed re-applying.

## Downstream impact

A deployment that had already pulled 0046–0048 from upstream sees only the
renumbering, which is documentation. A deployment tracking this branch gains
`pipelines/backfill.py` as a new entry point; `CLAUDE.md` documents it in the
daily routine, before draining a long-standing backlog.
