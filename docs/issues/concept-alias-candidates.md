# Ninety-nine names waiting for a ruling

`config/concept-aliases.yaml` now holds 15 redirects and folded 15 records into
9. `python3 scripts/merge_concept_aliases.py --candidates` lists **99 more** —
names some reader declared as an alias in a summary that are separate records
here, each with its own share of the evidence and its own definition.

They are not a backlog to work through. Most of them should stay separate, and
the interesting part is *why the same list holds both kinds*.

## The list conflates three relations

A reader filling `aliases` is answering "what else is this called", and in
practice they answer three different questions with it.

**Another spelling.** `IF-Eval` / `IFEval`, `AMC-23` / `AMC23`. Mechanical, and
the 15 already ruled on were all of this kind.

**A neighbour, a parent or a child.** This is the majority and the reason the
field cannot be merged on automatically:

| Declared as an alias of | Actually |
| --- | --- |
| `MATH` under `math500` | MATH is 12,500 problems; MATH500 is 500 drawn from it |
| `GPQA` under `gpqa-diamond` | Diamond is the hard subset |
| `causal tracing` under `activation-patching` | [[activation-patching]]'s own note argues they measure different quantities — patching a contrast, ablation an absolute level |
| `entropy bonus` under `entropy-regularization` | the bonus is one instrument; the family includes clip-higher, Clip-Cov, KL-Cov |
| `Qwen3-4B-Base` under `qwen3-4b` | base and instruct are different checkpoints, and half this archive's results turn on which one was used |
| `majority voting` under `self-consistency` | the aggregation rule against the method that popularised it |
| `process reward` under `process-supervision` | the signal against the training regime |

Merging any of these would not mislabel a record. It would make the archive
unable to state a distinction it currently states — and, worse, would do it
silently, since the merged record reads as complete.

**A term the group has not settled.** `latent reasoning` / `implicit reasoning`,
`detection versus control` / `representation versus readout`, `test-time
scaling` / `test-time compute`. These are real synonyms in some papers and
distinctions in others. They are the group's editorial call, not a spelling
question, and they belong in a conversation rather than in a config file.

## What is worth ruling on next

Ordered by evidence at stake. Each is a judgement somebody has to make; none is
mechanical.

| Pair | Sources | The question |
| --- | --- | --- |
| `test-time-scaling` / `test-time-compute` | 15 + 20 | One is the resource, the other what you do with it — or are they used interchangeably here? |
| `llama-3-1-8b-instruct` / `llama-3-1-8b` | 12 + 6 | Checkpoint identity. The same question as every `-Base` / `-Instruct` pair below, and there are eleven of them |
| `latent-reasoning` / `implicit-reasoning` | 10 + 6 | Two literatures or one |
| `linear-probing` / `linear-probe` | 4 + 14 | The method against the artefact; probably one entity |
| `circuit-analysis` / `circuit-discovery` / `mechanistic-interpretability` | 7 + 3 + 6 | A three-way, and the middle one is arguably a step of the first |
| `gpt-oss-20b` / `gpt-oss-120b` / `gpt-oss` | 5 + 4 + 2 | The family record is the artefact here: it holds what belongs to neither size |

The checkpoint pairs are the largest single group — `qwen3-4b-base`,
`qwen3-1-7b`, `qwen2-5-14b`, `qwen2-5-1-5b`, `qwen2-5-vl-7b`, `mistral-7b`,
`llama-3-2-3b` and more. **The recommendation is to rule them all one way and
say so once**, because the failure of ruling case by case is that a reader
cannot predict which spelling a result was filed under.

## What would make this stop happening

Nothing here prevents the next fragmentation; it only cleans up after one. Three
options, none taken:

- **Show the reader the existing entities.** A definition task could list the
  entity names already in the archive, so a summary writes `AIME 2024` because
  that is what is there. Cheapest of the three and it attacks the cause, but it
  makes every task payload larger and the list is 1,952 names long — it would
  have to be filtered to plausible neighbours, which is its own problem.
- **Normalize harder in `slugify`.** Dropping every non-alphanumeric would have
  caught 9 of the 15 automatically. It also renames every slug in the archive
  and merges pairs nobody ruled on, which is the failure this whole issue is
  about, in one step and for every name at once.
- **Report near-collisions at render.** A warning when two slugs differ only by
  punctuation. Cheap, and it makes the fragmentation visible on the day it
  happens rather than at 39 sources. This is the one worth doing.

## Status

Open. The 15 mechanical redirects are applied and committed; nothing above is.
