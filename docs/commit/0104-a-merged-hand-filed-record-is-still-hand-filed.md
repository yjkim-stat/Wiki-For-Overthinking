# 0104 — A merged hand-filed record is still hand-filed

| | |
| --- | --- |
| **Commit** | `fix(scripts): discard reads source as the set it is` |
| **Scope** | `scripts/discard.py`, `tests/test_model_kind.py` |
| **Kind** | fix |

## What changed

`discard.py --rescore` guarded hand-filed records with `paper.source ==
"local"`. `source` is not a single word: `merge_papers` builds it by joining the
two records' sources with `+`, so a PDF filed in `inbox/` and later also
collected from the ACL Anthology reads as `local+anthology`. The equality test
missed every one of those. Both guard sites now go through `_hand_filed`, which
tests membership in `source.split("+")` — the same idiom `merge_papers` uses to
build the string.

## Why it matters more than the size of the diff suggests

The rule it protects is one the archive states twice: a PDF somebody filed by
hand is kept whatever its keywords say, because filing it *is* the editorial
decision scoring exists to approximate. `--rescore` exists to propose records
that no topic accepts, and its own docstring promises it skips hand-filed ones
entirely.

The records that fell through the gap were the ones with the **most**
provenance, not the least — a document a reader filed *and* a collector later
found independently. On this archive one such record, a hand-filed survey since
merged with its Anthology entry, was being offered for discard on every
`--rescore`.

Nothing was lost: dry run is the default, and removal would still have required
`--apply`. The defect was in what the tool proposed, not in what it did.

## How it surfaced

`test_hand_filed_pdfs_are_never_selected_by_rescore` began failing. That test
runs the script against the real repository rather than a sandbox, which is
itself contrary to the rule that tests touch neither the network nor the real
`data/` — and it is why the failure appeared only once this deployment's archive
happened to contain a merged local record. The test is left as it is here,
because changing it is a separate decision from fixing the bug it caught; the
new test beside it is a unit test of the predicate and needs no archive at all.

## Trade-offs and rejected alternatives

**Rejected: `paper.source.startswith("local")`.** It reads as a smaller change
and is wrong in the other order — `merge_papers` puts the *stored* record's
source first, so an arXiv record that absorbs a hand-filed one is
`anthology+local`. The test covers both orders for that reason.

**Rejected: normalising `source` to a list on the record.** That is a schema
change, and the field is written by collectors that have never needed it. Adding
a field is safe here but renaming or retyping one drops data on load, and the
predicate costs nothing.

## What a reviewer should check

- `python3 scripts/discard.py --rescore` prints no `local:` row on an archive
  that holds merged hand-filed records; before the change this one printed one.
- `_hand_filed` is true for `local`, `local+anthology` and `anthology+local`,
  and false for `arxiv`, `anthology`, `""` and `None` —
  `test_a_merged_hand_filed_record_is_still_hand_filed`.
- The explicit route is unchanged: `--id local:... --apply` still removes a
  hand-filed record, and still prints the line saying that is what it is doing.

## Downstream impact

None to config or data. A deployment that has never merged a hand-filed record
with a collected one will see no change at all; one that has will find those
records no longer proposed for discard.
