# 0007 — A map of the repository in the README

| | |
| --- | --- |
| **Commit** | `docs: map the directory layout in the README` |
| **Scope** | `README.md` |
| **Kind** | docs |

## What changed

A "Where things live" section: an annotated tree of every directory, and a table
sorting them into the three kinds this repository actually has — yours, the
source of truth, and derived.

## Why it is built this way

**The tree is not the point; the three kinds are.** A newcomer's first
destructive mistake is editing a generated file — a paper page, a wiki auto
block — and losing the work on the next render. `CLAUDE.md` forbids it, but a
rule only helps someone who has already read the rule. A reader who has seen
that `archive/`, `wiki/` and `outputs/` are one kind of thing and `config/`,
`templates/` and `inbox/` are another does not need the rule. So the table comes
first and the tree illustrates it, rather than the other way round.

**Annotations say what a directory is *for*, not what it contains.** The detail
of what each generated artifact holds already exists, one section further down,
and two lists of the same paths is how a README starts disagreeing with itself.
The tree links there instead of repeating it.

**The exceptions are called out where someone will trip over them.** Three
things in this repository look wrong until explained, so each is annotated in
place rather than left for the reader to discover:

- `archive/daily/` sits inside a derived tree but is a record of a run and is
  never regenerated — the one asymmetry in `archive/`.
- `data/index/seen.sqlite` is a committed binary, because a scheduled run
  starts from a fresh clone and dedup state that does not survive the clone is
  not dedup state.
- Generated trees are committed at all, which surprises anyone used to treating
  build output as disposable. Same reason: the container is ephemeral.

**Nothing under `data/`, `archive/`, `wiki/` or `outputs/` exists before the
first run**, which is stated explicitly. Otherwise the tree describes a
repository the reader cannot see, and they go looking for a bug.

## Trade-offs and rejected alternatives

- *Generating the tree from the filesystem.* Rejected: it would list what
  happens to be on one machine after one run, including empty directories and
  whatever the last render left, and it would carry no annotations — which are
  the entire value.
- *Putting the map in `docs/` instead.* Rejected: the question it answers
  ("where do I look?") is asked before anyone opens `docs/`.
- *Dropping the "What it produces" table and folding its detail into the tree.*
  Rejected: the tree would double in size and stop being skimmable. Two
  sections at two levels of detail, with one link between them, is the smaller
  cost.
- This section will drift when a directory is added and the README is not
  touched. Accepted: the alternative is no map at all, and the commit-note
  practice puts a reviewer in front of every structural change.

## What a reviewer should check

- That every path in the tree exists in the code that creates it —
  `common/paths.py` for the directories, `common/store.py` for the filenames
  under `data/`, `publish/wiki.py` for `_meta/graph.json`.
- That the annotations do not restate "What it produces".
- The three-kinds table against `CLAUDE.md`'s rules. If they ever disagree,
  `CLAUDE.md` is the one that is enforced.

## Downstream impact

None. Documentation only.
