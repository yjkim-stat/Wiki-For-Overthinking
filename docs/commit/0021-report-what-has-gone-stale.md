# 0021 — Report what has gone stale

| | |
| --- | --- |
| **Commit** | `feat(render): report definitions and analysis outgrown by their evidence` |
| **Scope** | `pipelines/render.py`, `CLAUDE.md`, `tests/test_render.py` |
| **Kind** | feature |

## What changed

`render` gains a `stale` block in its result: how many definitions were written
against fewer sources than the entity now has, and how many hand-written
sections declared a source count they have since outgrown. Both are logged as
warnings. Neither is rewritten.

A hand-written section opts into the second check by ending with
`<!-- analysis-sources: 40 -->`.

## Why it is built this way

Every counter in this system measured whether something was *unwritten*. None
measured whether it was *out of date*. `queue_missing_definitions` files a task
only for an entity with no definition, so a definition was written once and
never revisited, however far its evidence outgrew it.

The result is not a thin note. It is a wrong one: a definition saying "in all
three sources" while standing at nine, or a claim a later source flatly
contradicts. It reads as complete and confident. In a field archive **38 of 121
definitions** were in this state after a single day of collection. For an
unattended scheduled archive this degrades monotonically and silently, which is
why the operating consequence is now stated in `CLAUDE.md`:

> An empty queue means nothing is unwritten. It does not mean nothing is out of
> date.

**Reporting, never rewriting.** This is the load-bearing constraint. Re-deriving
a definition means reading its sources; clearing the field on arithmetic alone
would discard written work because a number moved. The operator clears
`definition` in `data/concepts/<slug>.json` and re-renders to re-queue — a
deliberate act, on a definition they have looked at.

**The recorded count, not a phrase match.** Each concept task already stores
`payload.source_count`, so staleness is arithmetic against what the writer
actually saw. Grepping for "three sources" would only catch definitions that
count out loud, and miss the more dangerous kind — one that enumerates its
sources by name reads as exhaustive while describing four of ten.

**Prose has no declared dependency, so it declares one.** The section under
`auto:end` is where the archive's actual reasoning lives, and its staleness is
*structurally* undetectable: a definition has a countable evidence base and a
recorded count; prose has neither. The marker is the smallest thing that makes
the check possible at all. It is opt-in because some analysis genuinely does not
depend on how many sources exist.

That half is weaker and should be reviewed as such — it relies on authors
maintaining a number by hand, and an unmaintained marker reports a false
positive or, worse, stays quiet. It is still better than the alternative, which
is that the most valuable artifact in the repository is the only one with no
integrity check at all.

## Trade-offs and rejected alternatives

**Rejected: clear stale definitions automatically and let the queue re-ask.**
Symmetrical with how the wiki extends itself, and wrong. It deletes a human
judgement because a counter incremented, and the re-derivation would be done
without anyone deciding it was warranted.

**Rejected: infer prose staleness from file mtime versus evidence.** No marker
to maintain, and it fires on every whitespace edit while missing a section
rewritten before the evidence grew.

**Cost: a first run on an existing archive reports a large backlog.** That is a
backlog to work through, not an error. Nothing is blocked by it.

**Cost: the analysis marker can lie.** An author who revises the prose without
updating the number gets silence. The check is a floor, not a guarantee.

## What a reviewer should check

The safety property first, because everything else is cosmetic next to it:

```bash
python3 -m unittest tests.test_render -v -k Staleness
```

`test_reporting_never_rewrites_the_definition` and
`test_reporting_never_rewrites_the_analysis` assert the text is byte-identical
after the report runs. If either can be made to fail, this tool has become
capable of destroying work.

Then check `test_an_entity_with_no_definition_is_never_reported` — an unwritten
definition is the queue's job, not this one, and reporting it here would double
every backlog count.

## Downstream impact

Purely additive; `render`'s result dict gains a `stale` key with two counts. A
deployment pulling this should expect a non-zero count on the first run and
should treat it as a backlog rather than a failure.

To use the analysis check, add `<!-- analysis-sources: N -->` to the end of a
hand-written section. Sections without it are unaffected, which is every
existing one.
