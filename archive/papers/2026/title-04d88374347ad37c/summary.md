<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Base Models Know How to Reason, Thinking Models Learn When

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/66610>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

By decomposing the base-to-thinking model difference into reasoning mechanisms (steering vectors that induce a behaviour) and reasoning heuristics (a classifier deciding when the behaviour fires), the paper finds that hybrid models recover about 76% of the RL base-to-thinking gap but only about 11% of the SFT-distillation gap, indicating RL mainly teaches when to invoke reasoning behaviours the base model already has.

## Problem

Thinking models outperform their base models, but what training actually installs is unclear: whether RL and distillation add new reasoning capabilities, or merely change when existing ones are deployed. The question is open because the usual comparisons are behavioural — they show the thinking model scores higher — without isolating which part of the difference is a new mechanism and which is new control over an old one. Answering it matters for how one builds reasoning models efficiently, and for whether the extra tokens a thinking model spends buy new ability or better timing.

## Contributions

- An unsupervised method that discovers a model's reasoning behaviours by training small Sparse Autoencoders on sentence-level activations of reasoning traces, producing interpretable reasoning taxonomies.
- Constructive model diffing: reconstructing the base-to-fine-tuned difference from interpretable components and scoring the reconstruction by how much of the performance gap it recovers.
- The decomposition of that difference into reasoning mechanisms (category vectors inducing a behaviour) and reasoning heuristics (a classifier deciding when a mechanism fires).
- Evidence across nine base/thinking pairs that hybrids recover about 76% of the RL gap versus about 11% of the SFT gap, and that category vectors converge to lower loss for RL-derived taxonomies.

## Method

Two stages. First, an unsupervised discovery of a model's reasoning behaviours: small Sparse Autoencoders are trained on sentence-level activations taken from reasoning traces, and the resulting features are grouped into an interpretable taxonomy of reasoning behaviours (the traces come from 12,102 MMLU-Pro prompts, yielding 430,122 reasoning-trace sentences). Second, 'constructive model diffing': rather than describing the base-to-fine-tuned difference, the paper tries to rebuild it from interpretable parts and measures how much of the performance gap the rebuild recovers. The difference is split into two components. A reasoning mechanism is a category vector — a steering direction that, added to the base model's activations, induces a given reasoning behaviour in the base model. A reasoning heuristic is a classifier that decides when a mechanism should fire. Combining base model plus category vectors plus firing classifier produces a hybrid model, and the fraction of the base-to-thinking performance gap that hybrid closes is the measurement. Steering strength is set per position by a trained MLP predicting the coefficient.

## Results

Nine base/thinking pairs: four RL-trained (Open-Reasoner-Zero at 0.5B, 1.5B, 7B, 32B), four SFT-distilled (DeepSeek-R1-Distill Llama-8B, Qwen-1.5B, Qwen-14B, Qwen-32B), and one mixed (QwQ-32B, SFT then RL). Two independent findings agree. First, category vectors optimised in the base model converge to far lower loss when the taxonomy is derived from purely RL-trained models than from distilled ones. Second, hybrid models recover roughly 76% of the RL base-to-thinking gap, averaged over GSM8K, MATH500 and the held-out Hendrycks-MATH set, against only about 11% of the SFT gap. The SFT figure is not uniform: recovery is essentially zero for the smallest distilled pairs and reaches only about 15-20% for the 14B and 32B distilled models, so the headline 11% averages over a range in which the small models contribute nothing at all. Note also that even the RL result leaves about a quarter of the gap unexplained by the mechanism-plus-heuristic decomposition.

## Limitations

Stated: the taxonomy is derived from MMLU-Pro traces and is biased toward mathematical reasoning, which makes evaluation on non-math benchmarks difficult; choosing steering magnitudes is a known open problem, only partly addressed by the per-position coefficient MLP; and the low recovery for SFT-distilled models is genuinely ambiguous — it could mean distillation really installs new mechanisms, or it could mean the category-vector optimisation is failing for those models, and the paper cannot separate the two. That last caveat undercuts the sharper reading of the headline: the asymmetry between 76% and 11% is a robust observation, but the interpretation 'SFT installs new mechanisms' is one of two live explanations, not a demonstrated fact. Beyond what is stated: all evaluation is on mathematical benchmarks, the mixed QwQ-32B pair is a single data point and cannot separate the contributions of its SFT and RL stages, and 'recovery of the performance gap' measures accuracy restored, not that the hybrid reasons by the same route as the thinking model.

## Why it matters here

- **overthinking**: Directly on topic, and it addresses the topic's central question at the mechanism level rather than the behavioural one. The topic is about when a reasoning model should think more or less; this paper's claim is that when is precisely what RL training adds. If reasoning mechanisms — backtracking, verification, case-splitting and the rest of the discovered taxonomy — already exist in the base model, and what RL supplies is a heuristic classifier deciding at each point whether a mechanism should fire, then overthinking is naturally read as that heuristic firing too often or in the wrong places, rather than as the model lacking any ability to stop. That reframes length-control methods: they are adjusting a learned firing policy over pre-existing behaviours, which suggests intervention on the heuristic (or directly on the steering coefficients, which the paper predicts per position) as an alternative to length penalties or truncation. The 76%-versus-11% split also bears on which reasoning models the group should expect length-control work to transfer between: an RL-trained thinking model and an SFT-distilled one differ in kind under this analysis, so a method tuned on one family has no assumed claim on the other — a distinction worth carrying into how the archive reads efficient-reasoning results generally. Two cautions on how far to push this. The paper measures accuracy recovery on GSM8K, MATH500 and Hendrycks-MATH; it does not measure trace length, token cost, or the accuracy/length tradeoff at all, so it offers no direct evidence about how much a model thinks. And the authors say themselves that the low SFT recovery may be an artefact of their optimisation rather than a fact about distillation, so the mechanisms/heuristics story is best treated as a well-supported hypothesis for the RL case and an open question for the distilled one.

## Entities

- **Concepts**: reasoning mechanisms versus reasoning heuristics, knowing how to reason versus knowing when, RL as orchestration of pre-existing capability, SFT-distillation as mechanism installation, unsupervised reasoning-behaviour taxonomy, activation steering, performance-gap recovery as an interpretability metric
- **Methods**: constructive model diffing, Sparse Autoencoders on sentence-level activations, category (steering) vectors as reasoning mechanisms, firing classifier as reasoning heuristic, hybrid base+mechanism+heuristic models, per-position steering-coefficient MLP
- **Datasets**: MMLU-Pro (12,102 prompts, 430,122 reasoning-trace sentences, for taxonomy discovery), [GSM8K](../../../../wiki/datasets/gsm8k.md), MATH500, Hendrycks MATH (held-out 1,000-question subset)

Tags: `reasoning-models`, `interpretability`, `sparse-autoencoders`, `model-diffing`, `activation-steering`, `rl-vs-distillation`, `when-to-reason`, `efficient-reasoning`

---

Record id: `title:04d88374347ad37c`
