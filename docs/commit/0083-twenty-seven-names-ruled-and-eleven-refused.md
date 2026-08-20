# 0083 — Twenty-seven names ruled, and eleven refused

| | |
| --- | --- |
| **Commit** | `feat(config): rule on twenty-seven more concept aliases` |
| **Scope** | `config/concept-aliases.yaml`, `docs/issues/concept-alias-candidates.md` |
| **Kind** | feat |

## What changed

The alias map goes from 15 redirects to 40, folding 40 records into 24. Concept
entities 1952 → 1927, wiki notes 361 → 359.

The additions are in three groups, and the grouping is the ruling:

- **Acronym and expansion** — `PCA`, `process reward model`, `indirect object
  identification`.
- **One name for one thing** — 15 entries. Not spelling, but not a judgement
  either: in every source here the two strings pick out the same object and a
  reader looking up one is answered by the other's note. `data contamination` /
  `benchmark contamination`, `reasoning trace` / `chain of thought`,
  `rationalization` / `post-hoc rationalization`, and so on.
- **Checkpoints and systems named two ways** — `Dynasor-CoT` → `Dynasor`,
  `DEER-PRo` → `DEER`, `Qwen3-235B` → `Qwen3-235B-A22B`.

## The refusals are the substance

Three near-misses are declared inline in the config, because the next person
reading the file will consider them and should not have to re-derive why not:

- `steering` merges into `activation steering`; **`steering vector` does not**.
  The archive holds results about the vector itself, including that its
  detection quality licenses no claim about its intervention effect.
- `reasoning trace` merges into `chain of thought`; **`reasoning trajectory`
  does not**. The probing work here treats the trajectory as an object with
  geometry; the trace is the text.
- `linear probing` merges into `linear probe`; **`probing` does not**. The
  family includes non-linear readouts.

And the largest ruling is a refusal. **The eleven base/instruct checkpoint pairs
stay separate.** `Qwen2.5-14B` and `Qwen2.5-14B-Instruct` are different weights,
half this archive's results turn on which was used, and a summary writing the
bare name is reporting what its paper wrote. Merging would assert a fact about
the experiment that no source states. The fragmentation is real — `qwen3-4b-base`
at 5 sources against `qwen3-4b` at 3 — and it is the lesser cost. Ruling them
one way and saying so once is what stops a reader having to guess which spelling
a result was filed under.

## One row that settles the design question

`Llama-3.3-70B-Instruct` is declared, by a reader, as an alias of
`llama-3-1-70b`. Those are different releases.

Nothing checks that. The field is harvested from prose and records whatever was
written as an identity claim, which is the entire argument for the map being
authored, small and reviewed rather than derived from what is already in the
records.

## What it costs

Four definitions. Two were cleared because both halves had been separately
written — `linear probe` at 14 + 4 sources, `activation steering` at 9 + 2 —
and two entities lost the only definition they had, because it sat on the
retired side: `PCA` and `indirect object identification`. All four re-queue and
are re-derived against the union.

Seventy-two candidates remain unruled. The issue file sorts them and names the
cheap defence nobody has built: a render-time warning when two slugs differ only
by punctuation, so the next fragmentation is visible on the day it happens
rather than at 39 sources.
