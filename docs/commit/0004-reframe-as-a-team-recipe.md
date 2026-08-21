# 0004 — Reframe as a recipe for research team management

| | |
| --- | --- |
| **Commit** | `docs: reframe as a recipe for research team management` |
| **Scope** | `README.md`, `CLAUDE.md`, `docs/daily-routine.md`, repository name |
| **Kind** | docs · **rename** |

## What changed

The repository is renamed from **Recipe for World Action Model** to **Recipe for
Research Team Management with Claude**, and the documentation is rewritten to
match:

- **`README.md`** — the framing moves from "a research archive that maintains
  itself" to what the archive is *for*: the recurring literature work a group
  repeats every week. The running example is a topic the repository is visibly
  not about, and four candidate topics from four different fields are listed.
  The configuration section now tells you to edit `config/sources.yaml` before
  the first run.
- **`CLAUDE.md`** — reworded for a group rather than a single user ("what the
  group tracks is its own editorial decision"), and gains the rule that no
  change to the system lands without a commit note.
- **`docs/daily-routine.md`** — the wiki example note, and a troubleshooting row
  that now names wrong categories or venues as a cause of an empty collection,
  which after 0002 is the likeliest one.
- Also fixes the documented test command. `python3 -m unittest discover -s tests`
  appeared in the README and `CLAUDE.md` and could never have worked: the tests
  import through the `tests` package, so `-t .` is required.

## Why it is built this way

**The name was the last thing tying the repository to one subject.** After 0002
and 0003 nothing in the defaults, the code or the fixtures named a field — but a
repository called *Recipe for World Action Model* is, to anyone who lands on it,
a repository about world action models. The old README said "nothing here is
specific to one field" directly under a title that contradicted it.

**The new name states the job, not the mechanism.** What the system automates is
the recurring work of keeping a group current: watching the literature, writing
it up, onboarding people, preparing seminar material. What is left for people is
what needs judgement — deciding what the group tracks, and correcting what the
system concludes. Framing it as team management rather than as an archive is
what makes the second half legible; "an archive that maintains itself" invites
the reader to think nothing is left for them.

**Three documents, three jobs, no overlap.** The README says what this is and
how to start. `CLAUDE.md` is a contract an agent executes — imperative, and its
rules exist because breaking them destroys work. `docs/daily-routine.md` is the
reference you open when something is wrong. Duplicating content across them is
how they start disagreeing, so the command lists are the only deliberate
repetition and they must be kept identical.

**Every rule in `CLAUDE.md` names the damage it prevents.** A rule without a
stated consequence gets treated as style and eventually as optional. This is why
"leave a field empty rather than inventing content" sits next to the command
that submits a result, and says what an invented value corrupts.

## Trade-offs and rejected alternatives

- *Keeping the old name and relying on the README.* Rejected above.
- *A generic name like "Research Archive Toolkit".* Rejected: it describes the
  mechanism, which the reader can see, and hides the intent, which they cannot.
  Naming Claude in the title is accurate rather than decorative — the default
  summarizer backend is a Claude Code session, and the system's central design
  choice only makes sense once you know that.
- *Renaming the Python package or the module paths.* Rejected: `pipelines/` is
  descriptive and subject-free already, and renaming it would break every
  documented command for no benefit.
- *Placeholder-only examples in the prose.* Rejected: a bad `keywords` list is
  the most common reason a deployment collects nothing, so the README shows a
  concrete topic. The YAML template keeps its placeholders.

## What a reviewer should check

- The three documents agree — particularly the command lists, which appear in
  all three.
- `grep -rn "unittest" README.md CLAUDE.md` — both must carry `-t .`.
- The rename is of the working directory only. The repository's own history,
  remotes and module paths are untouched; if the remote is renamed, the clone
  URL changes and existing checkouts need `git remote set-url`.

## Downstream impact

A project deploying this repository should rewrite the README's framing
paragraphs for its own group. `CLAUDE.md` is meant to be kept close to as-is —
its rules describe invariants of the pipeline, not preferences of a particular
lab — except for the commit-note rule, which can be dropped along with
`docs/commit/` if the project has its own convention.
