# Ninety-nine names, twenty-seven ruled

**Status:** the code half is done — see [Resolution](#resolution) at the foot of
this file and [note 0099](../commit/0099-a-spelling-said-on-the-day-it-splits.md).
The 72 rulings remain the group's.

`config/concept-aliases.yaml` holds **40 redirects** and has folded 40 records
into 24. `python3 scripts/merge_concept_aliases.py --candidates` lists the
**72 remaining** — names some reader declared as an alias in a summary that are
separate records here.

They are not a backlog to work through. Most of them should stay separate, and
the interesting part is why the same list holds both kinds.

## The list conflates three relations

A reader filling `aliases` is answering "what else is this called", and in
practice they answer three different questions with it.

**Another spelling.** `IF-Eval` / `IFEval`, `AMC-23` / `AMC23`. Mechanical.

**One name for one thing.** Not spelling, but not a judgement either: in every
source here the two strings pick out the same object, and a reader looking up
one is answered by the other's note. `data contamination` / `benchmark
contamination`, `rationalization` / `post-hoc rationalization`, `reasoning
trace` / `chain of thought`, `learning dynamics` / `training dynamics`.

**A neighbour, a parent or a child.** This is the majority of what is left, and
the reason the field cannot be merged on automatically:

| Declared as an alias of | Actually |
| --- | --- |
| `MATH` under `math500` | MATH is 12,500 problems; MATH500 is 500 drawn from it |
| `GPQA` under `gpqa-diamond` | Diamond is the hard subset |
| `causal tracing` under `activation-patching` | [[activation-patching]]'s own note argues they measure different quantities — patching a contrast, ablation an absolute level |
| `entropy bonus` under `entropy-regularization` | the bonus is one instrument; the family includes clip-higher, Clip-Cov, KL-Cov |
| `steering vector` under `activation-steering` | the archive holds results about the vector itself, including that its detection quality says nothing about its intervention effect |
| `probing` under `linear-probing` | the family includes non-linear readouts |
| `majority voting` under `self-consistency` | the aggregation rule against the method that popularised it |
| `certaindex` under `dynasor` | the measure against the serving system built on it |
| `entropy dynamics` under `entropy-trajectory` | the first names the training-time phenomenon, the second a single generation's per-step sequence — two literatures |

Merging any of these would not mislabel a record. It would make the archive
unable to state a distinction it currently states — and silently, since the
merged record reads as complete.

**A term the group has not settled.** `latent reasoning` / `implicit
reasoning`, `detection versus control` / `representation versus readout`,
`test-time scaling` / `test-time compute`, `process reward` / `process
supervision`. Real synonyms in some papers and distinctions in others. The
group's call, not a spelling question.

## The `aliases` field is not evidence

One entry in the list is simply wrong: `Llama-3.3-70B-Instruct` is declared an
alias of `llama-3-1-70b`. Those are different releases. Whatever a reader meant,
the field records it as an identity claim, and nothing checks it.

That single row is the argument for the whole design. The map is authored and
small; the field is harvested and large; only one of them can be trusted to
merge on.

## What was ruled, and what it cost

Twenty-seven entries added in this pass, in three groups (`config/concept-aliases.yaml`
carries the reasoning inline):

- **Acronym and expansion** — `PCA`, `process reward model`, `indirect object
  identification`.
- **One name for one thing** — 15 entries, from `benchmark contamination` to
  `Inference Time Intervention`.
- **Checkpoints and systems named two ways** — `Dynasor-CoT` → `Dynasor`,
  `DEER-PRo` → `DEER`, `Qwen3-235B` → `Qwen3-235B-A22B`, and two more.

Two definitions were cleared for re-derivation because both halves had been
separately written: `linear probe` (14 + 4 sources) and `activation steering`
(9 + 2). Two more entities lost the only definition they had, because it sat on
the retired side — `PCA` and `indirect object identification` — and re-queue
from scratch.

## What deliberately stays separate

**The eleven base/instruct checkpoint pairs are not merged**, and this is the
ruling rather than a deferral. `Qwen2.5-14B` and `Qwen2.5-14B-Instruct` are
different weights, half this archive's results turn on which was used, and a
summary writing the bare name is reporting what its paper wrote. Merging would
assert a fact about the experiment that no source states. The fragmentation is
real — `qwen3-4b-base` at 5 sources against `qwen3-4b` at 3 — and it is the
lesser cost.

The same reasoning holds for `Mistral-7B` / `Mistral-7B-v0.3` and for the
`gpt-oss` family record, which legitimately holds what belongs to neither size.

## What would make this stop happening

Nothing here prevents the next fragmentation; it only cleans up after one.

- **Report near-collisions at render.** A warning when two slugs differ only by
  punctuation. Cheap, and it makes the fragmentation visible on the day it
  happens rather than at 39 sources. **The one worth doing.**
- **Show the reader the existing entities.** A definition task could list the
  entity names already in the archive. Attacks the cause, but the list is 1,927
  names long and would have to be filtered to plausible neighbours, which is its
  own problem.
- **Normalize harder in `slugify`.** Would have caught 9 of the first 15
  automatically. It also renames every slug in the archive and merges pairs
  nobody ruled on, which is this issue's failure mode applied to every name at
  once.

## Status

Open, and smaller. 40 ruled, 72 left, of which the base/instruct group is ruled
*not* to merge and the rest wait on the group.

---

## Resolution

**The one action this document called "the one worth doing" is done.** `render`
reports entity slugs that differ only in punctuation, on the day the second
spelling appears rather than at 39 sources against 5. Commit
`feat(render): report an entity that has split on a spelling`, note
[0099](../commit/0099-a-spelling-said-on-the-day-it-splits.md).

**The other two options were not taken, for this document's own reasons.**
Showing the reader the existing entities would need 1,927 names filtered to
plausible neighbours, which is its own problem. Normalising harder in `slugify`
would rename every slug in the archive and merge pairs nobody ruled on — this
issue's failure mode applied to every name at once.

**Only the narrowest rule fires at render.** `pipelines.duplicates`
([0072](../commit/0072-two-names-for-one-entity.md)) knows four — variant,
plural, suffix, edit distance — and stays a command somebody runs. The render
reports variants alone, because it fires every pass and a rule with false
positives becomes noise, and because the other three are exactly the judgements
this document is about: `MATH` under `MATH500` is a subset, and merging it would
make the archive unable to state a distinction it currently states.

**Nothing is merged, and the report says where the ruling goes.** The warning
names `config/concept-aliases.yaml`, which is the authored map — this document's
own argument for why the harvested `aliases` field cannot be merged on, given it
holds at least one claim that is simply false.

### What remains, and is not code

The 72 candidates. The three relations this document separates — a spelling, one
name for one thing, and a neighbour or parent or child — cannot be told apart by
any rule, which is the finding. The eleven base/instruct pairs stay separate as a
ruling rather than a deferral. Nothing here changes that, and nothing should.
