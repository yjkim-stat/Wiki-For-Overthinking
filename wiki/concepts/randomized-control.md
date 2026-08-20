# randomized control

<!-- auto:begin -->

An arm of an experiment in which the targeted criterion is replaced by random selection at matched cost, so the benefit attributable to the criterion can be separated from the benefit of the mechanical change it accompanies. Both sources run one and both report a result that qualifies their own claim. In one, partitioning verified-correct completions at random and applying the same rarity-based credit redistribution recovers 1.45 of a 3.55-point gain — half the benefit survives destroying the partition's meaning, with the semantic partition adding 2.10 on top. In the other, matched-norm random vectors orthogonal to the steering direction produce substantially smaller and inconsistently signed movement, which is what licenses reading the steering effect as directional rather than as a generic perturbation. The two uses differ in outcome and agree in discipline: without this arm, neither claim would be separable from its own side effects.

- **Kind**: concept
- **Also called**: matched-norm control, random control
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [activation steering](../methods/activation-steering.md), [advantage estimation](advantage-estimation.md), [AIME](../datasets/aime.md), [causal intervention](../methods/causal-intervention.md), [construct validity](construct-validity.md), [contrastive activation addition](../methods/contrastive-activation-addition.md), [credit assignment](credit-assignment.md), [detection versus control](detection-versus-control.md), [difference-of-means probe](../methods/difference-of-means-probe.md), [entropy collapse](entropy-collapse.md), [exploration](exploration.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [Humanity's Last Exam](../datasets/humanity-s-last-exam.md), [linear probe](../methods/linear-probe.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [logistic regression](../methods/logistic-regression.md), [LoRA](../methods/lora.md), [matched-budget comparison](../methods/matched-budget-comparison.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [out-of-distribution generalization](out-of-distribution-generalization.md), [pass@k](pass-k.md), [Qwen2.5-32B-Instruct](../models/qwen2-5-32b-instruct.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen3-32B](../models/qwen3-32b.md), [reasoning boundary](reasoning-boundary.md), [RLVR](../methods/rlvr.md), [steering vector](../methods/steering-vector.md), [trajectory diversity](trajectory-diversity.md)

## What we have settled

- **Established** — In RLVR credit-assignment work, a randomized control routinely captures much of the benefit attributed to the targeted criterion — so a criterion is not credited until it has been raced against random selection at matched cost.
  - Three independent instances, on three different intervention types. Partitioning verified-correct completions at random and applying the same rarity-based credit redistribution recovers 1.45 of a 3.55-point gain, with the cue-derived semantic partition adding 2.10 on top — half the benefit survives destroying the partition's meaning. Zeroing the gradients of a randomly chosen subset of positive-advantage tokens performs comparably to selecting those tokens by covariance, suggesting what does the work is the reduction in effective gradient rather than the criterion that picks them. And a reward-free random walk in an intermediate latent space reaches 60.6% against 60.3% for a reward-guided method operating at the output, so the choice of space dominated the choice of direction. In none of the three does the randomized arm match fully, so the targeted criteria are doing something; what the pattern establishes is that the untested attribution is routinely wrong about how much.

## Appears in

- [When Correct Solutions Repeat: Rarity-Aware Credit Redistribution for GRPO](../../archive/papers/2026/arxiv-2608-03467/summary.md) — Shows that GRPO's per-completion uniformity is frequency-skewed once credit is aggregated by solution structure — a recurring correct form accumulates positive coefficient mass proportional to how often it is sampled — and rebalances it by a rarity exponent over a partition built from deterministic cue signatures rather than a judge model.
- [Intertemporal Preference Steering in Qwen3 via Contrastive Activation Addition](../../archive/papers/2026/arxiv-2608-03892/summary.md) — Trains a difference-of-means direction on short- versus long-horizon answer continuations and steers along it, shifting binary temporal choices, moving the monetary indifference threshold on an untrained task by a factor of 56 at a ten-year delay, and changing a planning benchmark — with matched-norm random controls and an unusually candid account of what the direction may actually encode.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
