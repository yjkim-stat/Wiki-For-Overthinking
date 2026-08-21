# 0031 — The migration payload must never be committed

| | |
| --- | --- |
| **Commit** | `chore: keep the migration payload out of git` |
| **Scope** | `.gitignore` |
| **Kind** | chore · safety |

## What changed

`migration/` is ignored. It holds a hand-built payload for moving this archive
to a new machine: the un-tracked half of `data/`, plus a `git bundle` of the
repository, plus the documents that explain how to unpack them.

## Why this exists

The daily routine's third step is `git add -A && git commit && git push`, run
unattended. `migration/` is roughly 291 MB and consists almost entirely of PDFs
and a second copy of the repository's own history. Committing it once would be
close to irreversible in practice: the objects stay in the history whether or
not a later commit removes the files, and the repository is cloned fresh by
every scheduled run, so the cost is paid nightly and forever.

Nothing about the folder announces this risk. It is untracked, it sits at the
top level beside `data/` and `wiki/`, and `git add -A` does not ask. The one
line here is the entire defence, which is why it is worth a note.

## Why the payload exists at all rather than a plain copy

The tree splits cleanly in two and only one half travels through git. The
tracked half — `data/papers`, `data/summaries`, `data/concepts`, `data/queue`,
`data/index`, and every generated tree — reaches a new machine by cloning. The
un-tracked half does not reach it at all: 94 PDFs, the fetched abstracts, the
raw collector responses, the run logs.

Of those, **57 PDFs are irreplaceable** — they were filed by hand into
`inbox/`, so no collector can produce them again. That is the number that makes
this a migration rather than a re-clone.

## Trade-offs and rejected alternatives

- *Un-ignoring `data/pdfs/` instead, so the PDFs travel with the repository.*
  Rejected for the reason the existing ignore rule already gives: they are heavy
  and not ours to redistribute. Migration is a one-off; the nightly cost is not.
- *Naming the folder something already ignored, e.g. `build/`.* Rejected —
  relying on an unrelated rule to cover it is how the rule gets removed later by
  someone who checks only what it was written for.
- *Putting the payload outside the repository.* Reasonable, and the documents
  support it: nothing in `migration/` assumes it lives inside a checkout, and
  `verify.sh` takes the repository root as an argument. It sits here because a
  folder next to the thing it describes is the one people find.

## What a reviewer should check

- `git status --porcelain` is empty with `migration/` present and populated.
- `git check-ignore -v migration/payload/repo.bundle` names this rule.
- The property to preserve: the rule matches the directory, not the file types
  inside it. A future payload with different contents must stay ignored.

## Downstream impact

None on the pipeline. `migration/` is not read by any code; it is built by
`migration/build.sh`, which only reads the repository and writes under itself.
