# 0064 — A merge with a person in it

| | |
| --- | --- |
| **Commit** | `feat(enrich): fold one paper record into another, survivor named by you` |
| **Scope** | `pipelines/enrich/dedupe.py`, `pipelines/common/store.py`, `pipelines/requests.py`, `tests/test_merge_records.py`, `requests/README.md`, `CLAUDE.md` |
| **Kind** | feature |

## What changed

[Note 0059](0059-an-identifier-learned-late-is-still-registered.md) reports two
records claiming one identifier and stops, because choosing between them is a
merge. This is the other side of that stop line.

```bash
python3 -m pipelines.enrich.dedupe conflicts
python3 -m pipelines.enrich.dedupe merge <survivor> <absorbed> --dry-run
```

`requests.py` also gains a `merge` kind, because there was no way for anybody
but the archive's owner to formally ask for one.

## Why it is built this way

**The survivor is an argument, so the machine still chooses nothing.** The stop
line 0059 drew is not softened here; it is given a door with a person in it.

**Why no rule could choose.** Measured on the archive that prompted this: a paper
filed by hand *and* collected from arXiv ended up with the **reading on one
record and the document on the other**. The arXiv record held the PDF and had no
summary, sitting unread in the queue; the hand-filed record had been read and had
no document. Preferring the richer record, the older, or the one with more topics
each discards something real. That asymmetry is now the fixture
`tests/test_merge_records.py` is built on.

**`data/concepts/` is not touched, and that is not an omission.** Evidence is
derived — `harvest` rebuilds it from the summaries on every render — so moving
the reading *is* how the entities get repointed. A test asserts the merge leaves
those records alone and that the next render repoints them, which is the
derived/authored split doing its job. The analysis that prompted this listed
concept records as something a merge must edit; that would have written derived
data by hand and been undone by the next pass. `archive/` is untouched for the
same reason: `rebuild_archive` clears and regenerates it, so a ghost page goes on
its own.

**Two readings are reported, never reconciled.** If both records carry a
summary, the survivor keeps its own and the command says so on stderr. Which
reading is better is a judgement about their content, and this command has a
person for *identity* only. Silently preferring either would be the quiet merge
the whole design refuses.

**`topics` are unioned here although `merge_papers` leaves them alone.** That is
deliberate on both sides. At collection time the two records were scored
separately and the stored one's answer stands; here a person has said they are
one paper, so both taggings describe it. It is not hypothetical — in the pair
that prompted this, the wider tagging was only on the record about to be
absorbed, and the first version of this command dropped it. A test caught that.

**`SeenStore.repoint` is the one place repointing is allowed**, and it exists
only for this path. `reconcile_identifiers` refuses to call anything like it.

## Trade-offs and rejected alternatives

**It is not atomic.** Seven writes across records, summaries, findings, the queue
and SQLite, with no transaction spanning them. A crash halfway leaves a
recoverable mess rather than a corrupt one — the survivor may hold the reading
while the absorbed record still exists — and `--dry-run` plus a clean git tree
are the mitigation. A real transaction would mean a staging copy of `data/`,
which is a larger machine than this problem.

**The absorbed record is deleted, not tombstoned.** Nothing records that it ever
existed except git history, which does hold it. A tombstone would need its own
record type and a rule for when the archive stops mentioning it.

**`merge_papers` still does not merge `topics` on the collection path.** That may
or may not be right there — a paper scored against one topic by arXiv and another
by a curated list arguably belongs to both — and changing it would alter what
collection produces. Named here rather than fixed in a commit about something
else.

**Nothing re-checks `analysis-sources` markers.** A note whose evidence count
drops by one may now carry a marker that is too high, which `render`'s `stale`
block will not report because it only looks for counts that are too *low*. Real,
small, and out of scope.

## What a reviewer should check

Five mutations, each taking down its own tests: overwrite the survivor's reading,
drop the absorbed record's topics, skip the `seen.sqlite` repoint, let `--dry-run`
write, and skip repointing findings.

- `test_concept_records_are_not_edited_by_the_merge` asserts both halves — the
  merge leaves them, and the next render fixes them.
- `test_the_entity_stops_counting_the_paper_twice` is the damage the command
  exists to undo, asserted end to end.
- `test_two_readings_are_not_silently_reconciled`.

## Downstream impact

New subcommand; nothing runs it automatically and nothing changes until somebody
does. `Finding.papers` entries naming an absorbed record are rewritten, which is
the only authored record this touches.

Run `--dry-run` first and read the plan. Commit before merging, so the git tree
is the transaction this command does not have.
