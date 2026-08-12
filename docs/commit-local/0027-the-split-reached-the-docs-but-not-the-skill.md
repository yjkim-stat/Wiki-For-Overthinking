# 0027 — The directory split reached the docs but not the skill

| | |
| --- | --- |
| **Commit** | `fix(skill): commit notes go in docs/commit-local/, not the template's mirror` |
| **Scope** | `.claude/skills/commit-notes/SKILL.md`, `docs/LOCAL-DELTAS.md` |
| **Kind** | fix · docs |

## What changed

The `commit-notes` skill said to write notes into `docs/commit/` and to take the
next number from there. [0024](0024-take-the-template-update-and-separate-our-work.md)
moved this deployment's notes to `docs/commit-local/` and updated `CLAUDE.md`,
but left the skill alone — so the procedure has pointed at the template's
read-only mirror ever since.

The skill now names `docs/commit-local/` in its frontmatter description, its
numbering step, its index step and its commit-message example, and carries a
`<!-- LOCAL -->` block that names both directories, gives the rule for each, and
states the cross-reference hazard. `docs/LOCAL-DELTAS.md` gains the file as
delta 3, and its two `grep` hints widen from `pipelines/` to `pipelines/
.claude/`.

## Why it is built this way

**The instruction and the layout table disagreed, and the instruction won.**
`CLAUDE.md` has said "do not add to this directory" about `docs/commit/` since
0024. That was not enough, and the reason is structural rather than a lapse: a
skill is loaded at the moment of acting and is read as a procedure to execute,
while a layout table is consulted by someone who has stopped to wonder where
something goes. When the two conflict the procedure wins and nothing announces
it. The fix therefore belongs in the skill; restating the rule more firmly in
the table would not have caught it.

**The delta is a find-and-replace plus one block, on purpose.** The template
wins on every future update, so the cost of any delta is paid again at each one.
Four path substitutions and a single marked block is close to the smallest
change that can carry the difference, and it leaves the note template, the rules
and the splitting procedure — the parts worth inheriting — untouched.

**The block carries what a substitution cannot.** Both sequences number from
0000 and both have passed 0025 with unrelated content, so a bare
`[0021](0021-....md)` written inside a local note does not fail. It resolves, to
a different change. There is no path to correct because the reference looks
correct, which is why this has to be prose and not a rule about slashes.

**It reuses the marker convention rather than inventing one.**
`docs/LOCAL-DELTAS.md` already told a reader to find deltas by grepping for
`LOCAL`. Extending that grep to `.claude/` costs one word in the doc; a second
convention for markdown would cost a reader knowing about both.

## Trade-offs and rejected alternatives

- *Leave the skill and rely on `CLAUDE.md`.* Rejected — that is precisely the
  arrangement that just failed. Note
  [0026](0026-a-correlate-is-not-a-mechanism.md) was first written into
  `docs/commit/` as 0027, with links numbered against the template's sequence,
  and was caught only because an unrelated commit from the scheduled routine
  happened to show the right directory in the log.
- *Rewrite the skill around this deployment.* Rejected: a large delta on a file
  `src` also edits, re-merged by hand at every update, bought with phrasing.
- *Collapse the two directories into one.* Rejected, and 0024 already gives the
  reason: the two histories number from 0000 independently, so a shared
  directory collides on every future template update.
- *Add a second, local-only skill instead of editing this one.* Rejected. Two
  skills with overlapping triggers is a worse failure mode than one skill with a
  wrong path, because which of them fires is not predictable from the prompt.
- The cost accepted: the next `src` change to this file needs a hand merge, and
  **nothing detects a missed re-application**. The failure is a note filed in
  the wrong directory, which no test can see.

## What a reviewer should check

- `grep -n "docs/commit/" .claude/skills/commit-notes/SKILL.md` — every
  surviving hit should be describing the template's directory, and none should
  be an instruction to write into it.
- The frontmatter `description` counts as much as the body: it is what is read
  when deciding whether to load the skill, and it named the wrong directory too.
- `docs/LOCAL-DELTAS.md` delta 3 lists each edited location. If that list is
  incomplete, the next template update silently drops whatever it omits — the
  same failure this note is about, one level up.

## Downstream impact

Nothing in the pipeline changes. For whoever applies the next `src` update:
one more row in the re-apply tables, and the grep in step 4 of "Applying the
next update" now covers `.claude/` as well as `pipelines/`.
