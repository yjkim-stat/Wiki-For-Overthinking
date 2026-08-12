# 0050 — Everything the archive needs is in the repository

| | |
| --- | --- |
| **Commit** | `docs: the repository stops referring to trees it cannot see` |
| **Scope** | `CLAUDE.md`, `docs/daily-routine.md`, `docs/issues/`, `docs/commit-local/README.md` |
| **Kind** | docs |

## What changed

The repository's own documentation no longer points at anything outside it.

- **`CLAUDE.md` says the deltas exist.** It is loaded into every session and
  previously did not mention `pipelines/local/`, `docs/LOCAL-DELTAS.md`,
  `docs/commit-local/` or the `model` kind at all — so a session could replace a
  file under `pipelines/` having been given no reason to check.
- **`docs/issues/` gains the keyword-overlap defect**: four tracked keyword pairs
  where one term contains another, so one occurrence scores twice. Investigated,
  measured, not yet fixed, with the four options and a leaning.
- **`docs/daily-routine.md` records this archive's scheduled routine** — that one
  exists, that it is paused, and the three things to settle before re-enabling
  it.
- **`docs/commit-local/README.md` says the directory is closed history**: new
  notes go in `docs/commit/`, and the remote those notes describe is not
  configured here, so a command quoted inside one is a record and not an
  instruction.

## Why it is built this way

Knowledge that lives only outside the repository is knowledge the next session
does not have. Each item above previously lived somewhere a clone cannot reach —
a staging folder that was excluded from git, or an agent's memory directory
keyed to a filesystem path. Both were about to be deleted or become wrong.

The routine's paused state is the sharpest case and is why deployment state sits
in a general document rather than nowhere. The trigger's prompt lives in the
account, not in any checkout. Nothing in the repository points at it unless
something here says so — and without that, the next session cannot tell a routine
that is *paused* from one that never existed. Re-enabling it blind would advance
a different archive than the one in front of you.

The keyword defect goes to `docs/issues/` rather than being fixed here because
the fix needs a decision, not an implementation: the honest options range from
editing the topic files to putting span bookkeeping into a scorer whose entire
value is that it can be read in one sitting. The issue argues that the problem is
real — measured at 0.50 against a correct 0.667, and **zero flipped acceptance
decisions** — so the next person can weigh it rather than rediscover it.

`docs/commit-local/` is annotated rather than rewritten. A pushed note is never
rewritten in this repository; the header says the directory is closed and the
notes stay exactly as they were.

## Trade-offs and rejected alternatives

`docs/daily-routine.md` now carries an account-specific trigger id, which is
deployment state in a general document. There was no better home: an issue is for
defects, a commit note is for changes, and inventing a fourth documentation kind
for one paragraph is worse than the mixture. It is marked `<!-- LOCAL -->` and
registered in `docs/LOCAL-DELTAS.md` as entry 4, so a future replacement of that
file is told what it is about to remove.

Five references to a no-longer-configured remote survive in
`docs/commit-local/`. They describe what was true when those commits were made
and are left alone deliberately; the README header is what stops a reader acting
on them.

## What a reviewer should check

- `grep -rn "/home/" --exclude-dir=.git .` returns nothing outside `.git`.
- Every relative markdown link resolves — including the ones into
  `docs/commit-local/` from `LOCAL-DELTAS.md`.
- The keyword issue reproduces: the script in it prints the four pairs against
  the live `config/topics/`.

## Downstream impact

None for behaviour. A project adopting the template should delete
`docs/commit-local/`, `docs/LOCAL-DELTAS.md` and the `<!-- LOCAL -->` block in
`docs/daily-routine.md` along with the archive directories — they describe this
archive, not the program.
