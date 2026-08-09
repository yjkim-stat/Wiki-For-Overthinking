# 0030 — What the group settled

| | |
| --- | --- |
| **Commit** | `feat(enrich): record what a conversation settles, and draw it into the wiki` |
| **Scope** | `pipelines/enrich/findings.py`, `pipelines/common/schema.py`, `pipelines/common/store.py`, `pipelines/common/paths.py`, `pipelines/publish/wiki.py`, `pipelines/publish/graph_page.py`, `templates/wiki/graph.html`, `CLAUDE.md`, `README.md`, `tests/test_findings.py` |
| **Kind** | feature |

## What changed

A new record type and a CLI for it. A **finding** is something the group
settled — a `decision` it took, or a `fact` it established across several
sources. Findings live in `data/findings/`, are recorded through
`pipelines.enrich.findings`, and surface in three places: the concept notes they
name, a new `wiki/findings.md`, and as a mark on `wiki/graph.html`.

## Why it is built this way

**There was nowhere to put this, and the gap was structural.** Every record here
arrives from a collector, and `CLAUDE.md` forbids writing one by hand. But a
group's knowledge is not only in its sources: "we stopped tracking that", "those
two names are the same thing", "the headline result does not survive our
setting" are real and were homeless. A paper record cannot hold them, and a
concept's definition is written *from its sources*, not from the group's
position on them. So this is a separate record type, stored apart from the
literature — which is also how it stays consistent with the rule against
inventing sources. **A finding is not a source. It is the group's own voice, and
it is filed where nobody can mistake it for evidence.**

**It goes through a validator, for the same reason the queue does.** The
alternative to a CLI is editing `data/` by hand, and a finding filed that way
can name a topic that does not exist or a paper nobody collected, with nothing
to notice. Being able to say "the group established X" is worth something only
if the record cannot be quietly wrong about what X attaches to.

The two link checks are deliberately asymmetric. **Topics are rejected when
unknown** — they are a closed set defined in config, so a bad slug is a typo.
**Concepts are accepted when unknown**, because the wiki harvests those from
summaries and a finding may legitimately name an entity before any paper has
been read on it. **Papers are rejected when uncollected**, with a message saying
to collect it rather than cite a record that is not there.

**Superseding, not editing.** A group's decisions change, and a log that only
appends becomes a pile in which the current answer cannot be found. A new
finding may retire an older one; the old statement stays on disk and at the
bottom of `wiki/findings.md`, marked. Why the group used to think otherwise is
most of what a newcomer needs in order to trust what it thinks now — and the
same reasoning is already why `reopen` refuses an applied task and why a stale
definition is reported rather than deleted.

**Content-addressed on the statement.** Recording the same sentence twice
updates its links instead of creating a second finding that would double-count
in every view.

**Nothing about this is automatic, and it cannot be.** The pipeline never calls
a model and has no transcript; only the session in the conversation knows what
was settled. That is a limitation of the architecture and also the right
behaviour — a fact worth keeping is worth someone choosing to keep.

**The map flags settled entities with a dot, not a colour.** The palette in
[0029](0029-the-wiki-drawn.md) validates three categorical hues and no more, so
"the group has taken a position here" is a second channel on an existing mark.
Adding a fourth hue would have invalidated the work that palette rests on.

**Concept notes put what was settled *above* the source list**, because a reader
arriving at the note should meet the group's position before the evidence for
it. Retired findings are dropped from the note and kept on the page: the note
shows where things stand, the page keeps the history.

## Trade-offs and rejected alternatives

**Rejected: extend the queue with a "finding" task kind.** The queue is for
work owed — unread items. A finding is an answer nobody asked for, arriving at
an unpredictable moment. Modelling it as a task would mean inventing a task to
complete immediately.

**Rejected: a free-text log file.** Simplest, and it cannot be linked, counted,
validated, or drawn. "One big picture" requires the pieces to be addressable.

**Rejected: capturing findings automatically from the conversation.** Not
possible here — see above.

**Cost: it depends entirely on someone bothering.** An unused CLI records
nothing, and there is no way for the system to know a conversation settled
something and went unrecorded. `CLAUDE.md` now asks for it in the routine,
which is the only lever available.

**Cost: a wrong finding is more damaging than a wrong summary.** A summary is
one paper's reading; a finding claims the group's position. The validator checks
what it attaches to, not whether it is true.

## What a reviewer should check

That the validator's asymmetry is intentional and holds:

```bash
python3 -m unittest tests.test_findings -v
```

`test_an_unknown_topic_is_rejected`, `test_a_paper_not_in_the_archive_is_rejected`
and `test_a_concept_the_wiki_has_not_seen_is_allowed` are the three sides of it.
`test_a_retired_finding_leaves_the_note_but_stays_on_the_page` is the supersede
contract in one test.

Then check that the map still validates: `class="settled"` must be a second
channel on an existing mark, never a new fill colour. Re-run the palette check
from 0029 if the three hues are touched.

## Downstream impact

Additive. `data/findings/` is new and committed — it is small, it is the group's
own writing, and losing it on a fresh clone would lose the only record here that
cannot be re-derived from anything.

`wiki/findings.md` is a new generated file. `render`'s `wiki` block gains a
`settled` count. Nothing existing changes shape.
