# 0090 — A marker can be wrong in two directions

| | |
| --- | --- |
| **Commit** | `fix(render): an over-declared analysis marker is stale too` |
| **Scope** | `pipelines/render.py`, `tests/test_render.py` |
| **Kind** | fix |

## What changed

`stale_analysis` reported a note whose `<!-- analysis-sources: N -->` marker had
been *outgrown* — `now > written_for`. It now reports any disagreement, and each
row carries a `direction` of `outgrown` or `over-declared`.

## Why the other direction is not harmless

The marker's whole job is to state how much evidence a piece of prose rests on.
A marker naming more sources than the entity has means one of two things, and
both are the condition this check exists to surface:

- **The count is wrong.** The one number that says what the analysis depends on
  is itself unreliable, and every future check against it inherits the error.
- **Evidence really left.** A paper was discarded, retopiced, or folded into
  another entity by the alias map — and the prose now describes sources the
  archive no longer holds. That is worse than describing too few, because a
  reader cannot go and find what it is talking about.

The old check could not see either. Worse, it *would* see them eventually: an
over-declared marker goes quiet until the evidence catches up and passes it,
at which point the note reads as freshly stale for an unrelated reason.

## It found one on the first run

`wiki/concepts/policy-entropy.md` declared 9 against 8. The cause is the third
possibility and the most likely one in practice: the section draws on RaML,
which is evidence for other entities and not for this one, and the count
included it. The prose already named RaML explicitly, so nothing was
misattributed — but the marker was counting a different set from the one the
check reads.

The note is corrected to 8, with a line saying where the ninth source came from.
That is the general answer when this fires: state the outside source in the
prose and count only the entity's own.

## What it costs

One more class of warning on every render, and markers now have to be exact
rather than merely not-too-low. That is the intended cost — an inexact marker
was previously indistinguishable from a correct one in one direction, which
made the field's precision unenforceable.

Nothing is rewritten, as before. `report_staleness` reports and never edits, for
the reason in its own docstring.

## What a reviewer should check

- `stale.analysis` in a render result now counts both directions; on this
  archive it is 0 after the correction above.
- The equal case is still silent — `test_analysis_still_matching_is_not_reported`.
- A note with no marker is still never checked. Opt-in was the point and has not
  changed.
