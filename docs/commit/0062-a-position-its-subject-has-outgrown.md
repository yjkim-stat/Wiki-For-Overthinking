# 0062 — A position its subject has outgrown

| | |
| --- | --- |
| **Commit** | `feat(render): report findings their subject has outgrown` |
| **Scope** | `pipelines/common/schema.py`, `pipelines/enrich/findings.py`, `pipelines/render.py`, `tests/test_stale_findings.py`, `tests/test_render.py`, `CLAUDE.md` |
| **Kind** | feature |

## What changed

`Finding.established_against` records how much evidence existed on a finding's
subject when it was recorded — the distinct sources behind the entities it
names. `render`'s `stale` block gains a `findings` count and names the worst.

Requirement R6.

## Why it is built this way

**A finding is the most expensive thing here to have quietly outgrown.**
`publish/wiki.py` puts it at the top of every note it bears on, above the
sources, in the place reserved for what outranks them — and that is right. It
also means a judgement reached across three papers goes on reading exactly as it
did once there are thirty, in the position a reader trusts most.

**A union, not a sum.** Two entities that share a paper were established by one
reading. Summing would make a finding look better supported the more entities it
happened to mention, which is the opposite of the truth.

**Reported and never re-queued, and this is the difference from a definition.**
Note 0058 asks for a stale definition again, because a definition is *derived
from its sources* — a task can hand it back with "what has changed". A finding
is a position somebody took. A queue task inviting a reader to revise the
group's mind would produce something that is not a finding at all: the record's
whole value is that its author is the group. Only the group revisits it, with
`findings add --supersedes`, and the old statement stays.

**0 means unknown, not none.** A finding recorded before this field reports
nothing, because a finding is not settled against nothing and treating the two
alike would report every pre-existing finding as stale on the first render after
the upgrade.

**Recording the same statement again moves the count.** Findings are
content-addressed on the statement, so re-recording is how a position is
reaffirmed against what the archive now holds — and keeping the original count
would report the revision as stale the moment it was made.

**A retired finding is not reported.** It has already been superseded; reporting
it would ask for the same decision twice.

## Trade-offs and rejected alternatives

**A finding naming no entity cannot be measured at all**, and reports nothing.
The subject of a finding is what it bears on, and the wiki's entities are the
only handle on that the archive has. A finding about a topic rather than an
entity is invisible to this, which is a real gap and a smaller one than
inventing a subject for it.

**Considered: comparing against `Finding.papers`.** That list is what the
finding cited, and it does not grow, so nothing would ever be reported. The
question is not "has the citation list changed" but "has the archive learned
more about this since".

**The count grows when an entity gains sources, even if none of them bear on the
question.** A coarse signal, deliberately: it is a prompt to look, not a verdict,
and the same coarseness has been acceptable for definitions since note 0021.

**It will report the same findings on every render until somebody acts**, which
is the standing-condition problem this archive keeps meeting. Left that way here
for the same reason as duplicate records: a position that has outgrown its
evidence is a defect in the archive's confidence, and it should not become quiet.

## What a reviewer should check

Four mutations, each taking down its own tests: count per entity instead of as a
union, treat `0` as "settled against nothing", report retired findings, and skip
recording the count at all.

- `test_two_entities_sharing_a_paper_count_it_once` is the union rule.
- `test_re_recording_the_same_statement_moves_the_count` — otherwise reaffirming
  a position reports it as stale immediately.
- `test_nothing_queues_a_finding_for_revision`, which is the line between this
  and note 0058.
- `tests/test_render.py::test_render_reports_every_count` pins the exact
  vocabulary of the `stale` block, so a fourth kind has to be added on purpose.
  It failed on this change, which is the test working.

## Downstream impact

`Finding` gains a field defaulting to `0`; existing records load and report
nothing until they are next recorded. `render`'s `stale` block gains a third
key — anything reading that dict by exact equality will need updating, which is
how this change was noticed in the suite.
