# 0067 — A note says when its own prose is behind

| | |
| --- | --- |
| **Commit** | `feat(publish): a note carries the notice that its analysis is outgrown` |
| **Scope** | `pipelines/publish/wiki.py`, `tests/test_outgrown_analysis.py`, `CLAUDE.md` |
| **Kind** | feature |

## What changed

Analysis under `<!-- auto:end -->` can declare what it was written against, and
[note 0021](0021-report-what-has-gone-stale.md) made `render` report when the
evidence passed that. The note itself said nothing.

It now carries a line at the foot of its generated block, immediately above the
prose in question:

> **The analysis below was written against 4 source(s); there are now 9.** It
> may still be right — nothing here has read it. Revise it, or update its
> `analysis-sources` marker to say it was checked.

## Why it is built this way

**The person who needs this is reading the note, not the log.** A run reports
staleness to whoever ran it; a wiki note is read weeks later by somebody who was
not there. Everywhere else this archive puts a caveat where the reader is —
`## What we have settled` sits above the sources, a reference's quotation goes
into the note rather than staying in the record — and this was the one measure
that stayed in a log line.

**Nothing touches the prose, and nothing can.** Everything after `auto:end` is
preserved for ever and only its author revises it. The notice goes *inside* the
generated block, which is the one part of the file this code may write, and a
test splits the note on the marker to assert the notice is on one side and the
prose untouched on the other.

**It cannot be a task, unlike a stale definition.** A definition is derived from
its sources, so [note 0058](0058-a-stale-definition-is-asked-for-again.md) can
hand it back and ask what changed; the answer goes through a validator into a
record. Prose in a note's manual tail is not a record and `apply` has nowhere to
put an answer — writing one would break the promise that makes the tail worth
having. So the only honest action is to tell the reader.

**Updating the marker clears it**, and that is a real answer. "Checked, still
right" is information: it records that somebody looked, which is exactly what a
count alone cannot say.

**It is idempotent by construction.** The notice is derived from the tail on
every render and written into a block that is rebuilt from scratch, so it cannot
accumulate — asserted over three consecutive renders.

## Trade-offs and rejected alternatives

**It cannot say which sources are new.** The marker records a count, not a set,
so "five arrived since" is knowable and "which five" is not. Recording the set
would mean a bigger marker for an author to maintain, and the whole reason this
mechanism is opt-in is that it costs an author something.

**Both directions are shown, because the report shows both.** A marker higher
than the note's current count means the prose was written against more than the
note now holds — after a merge, or a re-read that dropped a mention — and
[note 0090](0090-a-marker-can-be-wrong-in-two-directions.md) made
`stale_analysis` report that as well as growth. The notice would have covered
one direction and the run the other; that mismatch was found while rebasing this
onto it, which is the whole argument for fetching before the first edit.

**Every note with a marker is now examined on every render**, which is one regex
over the preserved tail per note. The tail was already being read to preserve it.

**Considered: an inline marker beside the prose.** It would put the caveat closer
still, and it would mean writing into the tail — the one thing that is promised
never to happen.

## What a reviewer should check

Three mutations: emit the notice for prose that is not behind, write it into the
tail instead of the block, and emit it for prose with no marker at all.

- **The third one needed the test tightening.** It asserted the absence of a
  particular phrase, so a notice worded differently passed. It now asserts the
  generated block contains no blockquote at all — the notice is the only thing
  that block ever emits as one.
- `test_the_prose_itself_is_untouched`, which is the promise the whole preserved
  tail rests on.
- `test_the_notice_does_not_accumulate`.

## Downstream impact

Notes whose analysis declares a source count below their current evidence gain a
line inside the generated block on the next render. No prose is altered, and a
deployment with no `analysis-sources` markers sees no change at all.
