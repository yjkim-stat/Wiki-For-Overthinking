# Harness — knowledge and wiki

What checks each step, and what nothing checks.

## Checked at the moment you do it

| Step | Guard | What it refuses |
| --- | --- | --- |
| `queue complete` | Result validator | A missing or mistyped required field; a `relevance` key naming a topic the paper does not have; a generic entity string where one specific name belongs |
| `queue reopen` | Task lifecycle | A task `render` has already consumed. Deliberate: re-deriving a record against a conclusion you have been told tends to satisfy the conclusion rather than the evidence |
| `findings add` | Finding validator | A topic slug that does not exist; a paper that was never collected. A record of what the group settled is only worth having if it cannot be quietly wrong about what it attaches to |
| Any write to `data/` | `tests/test_layering.py` | A renderer that writes to the source of truth. Behavioural — `data/` is snapshotted by content, each renderer runs, the snapshot must be unchanged |

**Work with the validators, never around them.** A rejection names what is
wrong. Hand-editing `data/` is what they exist to prevent — an alias filed that
way does not merely mislabel, it silently merges two entities.

## Checked by the suite

```bash
python3 -m unittest discover -s tests -t .
```

| File | Tests | Guards |
| --- | --- | --- |
| `test_queue.py` | 40 | Filing, validation, completion, reopen, the pending cap |
| `test_render.py` | 34 | Records in, artifacts out; promotion; the preserved manual section |
| `test_findings.py` | 20 | Validation, superseding, where findings surface |
| `test_score.py` | 20 | Keyword rules, including regular plurals |
| `test_dedupe.py` | 15 | Identity and merging: arXiv id, then DOI, then title fingerprint |
| `test_layering.py` | 8 | Rendering never writes to `data/`; a render is not an edit |

Two of those are worth knowing individually:

- **`test_a_full_render_over_an_unchanged_archive_changes_no_record`** deletes
  every generated tree, sleeps past a second boundary and re-renders. It sleeps
  because the bug it guards against was a timestamp: `harvest` used to restamp
  every entity every pass, so an untouched archive still produced a diff across
  every concept file.
- **`test_manual_section_survives_a_rerender`** is the promise `<!-- auto:end -->`
  makes. Everything after that marker is preserved forever.

## Reported, never acted on

`render`'s result carries `stale`. Read it:

```
definition for 'X' was written against 3 source(s); there are now 9
```

Nothing is rewritten automatically, because re-deriving a definition means
reading its sources and a counter must not discard written work on arithmetic
alone. Your own prose after `<!-- auto:end -->` can opt into the same check by
ending with `<!-- analysis-sources: 9 -->`; update the number when you revise
the section, and leave the marker out of prose that does not depend on the
evidence count.

## What nothing checks

Named here on purpose — an unchecked step you know about is safer than one you
assume is covered.

- **Whether a summary is true.** The validator checks shape, not fidelity. A
  confident, plausible, invented `results` field passes everything and corrupts
  the lecture notes, the wiki and every report built on top of it. This is why
  the rule is *leave it empty*.
- **Whether the right paper was collected.** Scoring is a keyword rule. A topic
  that returns nothing for several days running is a scoring bug at least as
  often as it is a quiet week — check `data/index/rejected.jsonl`.
- **Whether an entity name is the published spelling.** `Isaac Lab` and
  `IsaacLab` are two entities and nothing will say so. Only reading the notes
  finds it.
- **Whether a definition still matches its evidence.** `stale` counts sources;
  it cannot read.
