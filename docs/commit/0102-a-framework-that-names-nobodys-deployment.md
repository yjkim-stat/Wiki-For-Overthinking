# 0102 — A framework that names nobody's deployment

| | |
| --- | --- |
| **Commit** | `docs: remove one deployment's identifiers from the shipped tree` |
| **Scope** | `docs/daily-routine.md`, `scripts/install-cron.sh`, `workflows/deployment/` |
| **Kind** | docs |

## What changed

Three kinds of one-deployment detail leave the tree.

**A live Routine's identity.** `docs/daily-routine.md` carried a trigger ID, the
Routine's name, its schedule in a particular timezone, both of its repositories
by name, and its paused/enabled state. That section is replaced by what a
reader of any deployment can use: the three shapes a scheduled run fails in.

**A local checkout name in the installer.** The crontab tag written by
`scripts/install-cron.sh` carried the name one person had given their own
clone. It is now `# ra-wm-schedule[...]`, which does not move when somebody
renames a checkout.

**Stale example paths.** `~/ra-wm` in the deployment workflow becomes
`~/research-framework`.

## Why it is built this way

**The routine section was not documentation, it was state.** Everything in it
was true of one archive on one day: paused since a date, tracking five topics,
committing to a repository named after somebody's subject. A reader of this
repository cannot act on any of it, and a reader who mistakes it for guidance
acts on somebody else's decisions. What survives the edit is the part that was
never local — that "no new commit" is ambiguous between a quiet day and a dead
run, that a pause does not backfill, that the sweep caps are tuned to a topic
count. Those are properties of the pipeline.

**A trigger ID is an account's, not a repository's.** It identifies a live
object in whoever's account created it. It cannot be useful to anyone else and
should not travel in a tree that gets cloned.

**The crontab tag is the installer's compatibility surface.** It is how the
script finds the line it wrote last time in order to replace it rather than
duplicate it, so it must be stable across everything that can change around it —
including the directory name. Deriving it from the checkout's name would mean a
renamed checkout silently loses the ability to update or remove its own entry.
No entry carrying the old tag exists anywhere yet: the installer shipped one
commit ago and this changes the literal before anybody has installed one.

## Trade-offs and rejected alternatives

- *Move the routine section to rather than rewriting it.*
  Rejected: that register exists for **code** deltas that a wholesale file
  replacement would silently revert. A paused trigger is not a code delta, and
  filing it there would dilute a register whose value is that everything in it
  is load-bearing.
- *Keep the section behind its `<!-- LOCAL -->` marker.* The marker tells a
  maintainer not to overwrite it during a template update. It does nothing about
  the reader who is looking for how to schedule a run and finds somebody else's
  trigger instead.
- *Keep the notes that describe the archive itself.* Two of them — what the
  archive held when it moved in, and what it held when it moved out — were
  removed rather than edited. They record where somebody's papers lived, which
  is the thing this commit exists to stop shipping, and there is no version of
  them that is about the program.

## What a reviewer should check

```bash
grep -rn "trig_[A-Za-z0-9]" --include=*.md --include=*.yaml --include=*.sh .
python3 -m unittest tests.test_install_cron
```

The first should return nothing. The second is 15 tests and passes unchanged —
the tag is asserted for its behaviour (replace rather than duplicate, one line
per root) and not for its spelling, which is why renaming it broke no test.

## Downstream impact

None. No crontab entry carrying the previous tag has been installed anywhere;
the installer was added one commit earlier. A deployment that had copied the
routine section for its own reference keeps its copy.
