# 0092 — A repository is a candidate, not a paper

| | |
| --- | --- |
| **Commit** | `feat(collect): search GitHub for candidates, and let a person cite them` |
| **Scope** | `pipelines/collect/github.py`, `pipelines/candidates.py`, `pipelines/common/paths.py`, `pipelines/run_daily.py`, `config/sources.yaml`, `tests/test_candidates.py` |
| **Kind** | feature |

## What changed

A daily GitHub sweep, and a third drop lane for what it finds.

```bash
python3 -m pipelines.candidates list
python3 -m pipelines.candidates show <id>
python3 -m pipelines.candidates promote <id> --quoted "the passage relied on"
python3 -m pipelines.candidates drop <id> --reason "a wrapper, not a method"
```

`run_daily` gains a `github` source. It queries once per topic from that
topic's own `keywords.any`, scores every hit with the archive's own scorer, and
files what clears a topic threshold into `candidates/pending/`.

## Why a repository cannot enter as a paper

`Concept.evidence` counts papers and talks the archive has *read*, and that
count is what promotes an entity to a note of its own. If a repository could
contribute to it, nothing afterwards could say what the wiki grew from, and
deleting the repository would not undo it. That rule is already written down;
this feature is the first thing that could have broken it, so the collector is
built so that it cannot: it returns candidates and writes no record at all.
`test_promotion_never_touches_an_entity` pins it.

## Why the collector may not write the reference either

A repository's destination is a `Reference`, whose two required fields are
`retrieved_at` and `quoted` — the date somebody looked, and the passage they
relied on. Those two are what make the record a citation instead of a rumour.

**Neither can be filled by a collector.** A scraped README blurb in `quoted` is
a passage nobody relied on, and a record that looks like a citation and is not
one is exactly what those fields exist to prevent. So `promote` requires
`--quoted` and exits non-zero without it. The friction is the feature, and it
is the same argument `inbox/` and `requests/` are built on: something arrives
that is not yet a record, and a person decides what it becomes.

`candidates/` therefore sits at the deployment root beside those two and never
under `data/`, which holds only what arrived as literature or was derived from
it.

## A decision is permanent; a repository is not

`drop` writes the candidate to `candidates/dropped/` with the reason, and a
dropped id is never offered again however many times GitHub returns it. That is
why `file_new` lives in `candidates.py` rather than in the collector: what is
new is a fact about the decisions, not about the search. The per-run cap works
the other way and is documented as such — what the cap drops is offered again
tomorrow, because a cap bounds a run and not a decision (note 0088).

## What the first real run showed, which is not what was expected

Four candidates cleared, and **all four are curated bibliographies rather than
implementations** — `Awesome-LLM-RLVR`, `awesome-mechanistic-interpretability`
and two like them. Sorting GitHub by stars over reasoning terms surfaces
reading lists, because that is what accumulates stars in this field.

That is worth stating rather than tuning away, for two reasons. An awesome-list
is somebody else's editorial decision over a whole field, which is precisely
what `config/sources.yaml`'s `curated:` block already exists to consume — so the
better destination for this yield may be that collector rather than a
`Reference`. And it means the lane has not yet been shown to do the job it was
built for, which is finding published implementations. Both are for the next
session; nothing here guesses at a fix.

## Costs and limits

- **Anonymous only.** No token, by choice: an unauthenticated collector cannot
  act on behalf of anybody. Search is 10 requests/minute, which one query per
  topic sits well inside.
- **READMEs are not fetched.** Name and description are enough to reject the
  bulk, and fetching a README per hit would spend the core rate limit on items
  most of which are about to be dropped. It also means the scorer sees less
  than it does for a paper.
- **`--dry-run` writes nothing**, which was wrong in the first version of this
  commit and is now pinned by `test_a_dry_run_of_the_daily_collector_files_nothing`.

## The neighbour upstream added while this was being written

`enrich/lookup.py` ([0061](0061-a-look-outside-that-has-to-cite-what-it-saw.md))
is the same record type approached from the opposite direction: a session asks
*is there published code for this paper*, and the answer must cite a reference.
This lane surfaces repositories nobody asked about. Neither subsumes the other,
and they should share a promotion path — a promoted candidate ought to be able
to answer a pending `artifact` lookup. That wiring is not done.

## What a reviewer should check

- `tests/test_layering.py` still passes: `collect/` and `enrich/` write to
  `data/`, `publish/` does not, and nothing in this lane writes an entity.
- The suite is 756 tests, up from 744.
- `candidates promote` without `--quoted` exits non-zero.
- A dropped candidate does not reappear after a second `run_daily --source github`.
