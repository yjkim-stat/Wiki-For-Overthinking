# 0097 — A field the prompt never mentions

| | |
| --- | --- |
| **Commit** | `fix(llm): name the models field in the prompt a reader follows` |
| **Scope** | `pipelines/common/llm.py`, `pipelines/render.py`, `tests/test_models_are_answered.py`, `tests/test_render.py`, `docs/issues/`, `docs/solved/` |
| **Kind** | fix |

LOCAL: `models` — see `docs/LOCAL-DELTAS.md`.

## What changed

`models` was in the output schema, type-checked when present, and **never named
in the instructions** — which is the text a reader actually follows. Nine
consecutive readings went out empty before anybody noticed, and it was the
second time this field had gone missing quietly.

Both paper prompts now name it, and `render`'s `stale` block counts the readings
that answered nothing.

## Why it is built this way

**The cause is the prompt, so the fix is in the prompt.** A schema entry is a
contract; the instructions are what somebody reads. When they disagree, the
instructions win in practice every time.

**The field stays optional, and the prompt says why.** A paper that evaluates no
checkpoint answers `[]`, and requiring a non-empty list would force a guess
where the honest answer is silence — the same reasoning that keeps `results`
optional. What the prompt now adds is the part that made the defect invisible:
leaving it out and answering "none" produce **identical records**, and nothing
afterwards can tell the two apart.

**Counted in the `stale` block, not warned in a log.** The issue leaned towards a
warning in `_apply_paper` and then argued against its own leaning: a warning in a
render log nobody reads is barely better than nothing. The `stale` block is the
one place this archive already looks for rot. A count that stays flat while
readings accumulate says the prompt is being followed; one that tracks them says
it is not.

**The contract was not changed, and that was the harder call.** The issue asks
the group to decide whether an omitted `models` is a defect before the code
asserts one. Requiring the *key* while accepting `[]` — the shape `read_from`
uses in [note 0044](0044-a-reading-says-what-it-was-based-on.md) — was
implemented and backed out. It works, and it takes down **59 tests across eight
files**, every one a fixture that did not bother. That number is the measurement
this issue is really about, and it is more useful recorded than spent.

## Trade-offs and rejected alternatives

**A reader can still omit it**, and the count is how anybody finds out. That is
the deliberate consequence of leaving the contract to the group.

**The count is over all readings, not new ones.** An archive with a history of
omissions starts at a high number that does not fall until those readings are
revisited. It is a level, not a rate, and the note says so.

**`models` is a local delta**, so this hardens something the shipped template
does not have. Both changes are marked `LOCAL`, which is what makes them
survivable across an update.

## What a reviewer should check

- Two mutations: drop the rule from the paper prompt (three tests), stop
  counting (two).
- **`test_a_hand_filed_pdf_is_told_too`.** The first attempt fixed
  `paper_instructions` only; a hand-filed PDF goes through
  `local_pdf_instructions`, produces a paper reading against the same schema,
  and was still never told. The test caught it, reading the diff had not.
- `tests/test_render.py::test_render_reports_every_count` pins the exact
  vocabulary of the `stale` block, so a fifth key has to be added on purpose. It
  failed on this change, which is the test working — the second time this
  session.

## Downstream impact

Paper tasks filed or refreshed after this carry the rule in their instructions.
`render`'s `stale` block gains `readings_without_models`; anything comparing that
dict by exact equality needs updating. No record is rewritten and no reading is
rejected.
