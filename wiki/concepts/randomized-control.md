# randomized control

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [activation steering](../methods/activation-steering.md), [advantage estimation](advantage-estimation.md), [AIME](../datasets/aime.md), [causal intervention](causal-intervention.md), [construct validity](construct-validity.md), [contrastive activation addition](../methods/contrastive-activation-addition.md), [credit assignment](credit-assignment.md), [detection versus control](detection-versus-control.md), [difference-of-means probe](../methods/difference-of-means-probe.md), [entropy collapse](entropy-collapse.md), [exploration](exploration.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [linear probe](../methods/linear-probe.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [logistic regression](../methods/logistic-regression.md), [LoRA](../methods/lora.md), [MATH](../datasets/math.md), [MATH-500](../datasets/math-500.md), [out-of-distribution generalization](out-of-distribution-generalization.md), [pass@k](../methods/pass-k.md), [Qwen2.5-32B-Instruct](../models/qwen2-5-32b-instruct.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen3-32B](../models/qwen3-32b.md), [reasoning boundary](reasoning-boundary.md), [RLVR](../methods/rlvr.md), [steering vector](../methods/steering-vector.md), [trajectory diversity](trajectory-diversity.md)

## What we have settled

- **Established** — In RLVR credit-assignment work, a randomized control routinely captures much of the benefit attributed to the targeted criterion — so a criterion is not credited until it has been raced against random selection at matched cost.
  - Three independent instances, on three different intervention types. Partitioning verified-correct completions at random and applying the same rarity-based credit redistribution recovers 1.45 of a 3.55-point gain, with the cue-derived semantic partition adding 2.10 on top — half the benefit survives destroying the partition's meaning. Zeroing the gradients of a randomly chosen subset of positive-advantage tokens performs comparably to selecting those tokens by covariance, suggesting what does the work is the reduction in effective gradient rather than the criterion that picks them. And a reward-free random walk in an intermediate latent space reaches 60.6% against 60.3% for a reward-guided method operating at the output, so the choice of space dominated the choice of direction. In none of the three does the randomized arm match fully, so the targeted criteria are doing something; what the pattern establishes is that the untested attribution is routinely wrong about how much.

## Appears in

- [When Correct Solutions Repeat: Rarity-Aware Credit Redistribution for GRPO](../../archive/papers/2026/arxiv-2608-03467/summary.md) — Shows that GRPO's per-completion uniformity is frequency-skewed once credit is aggregated by solution structure — a recurring correct form accumulates positive coefficient mass proportional to how often it is sampled — and rebalances it by a rarity exponent over a partition built from deterministic cue signatures rather than a judge model.
- [Intertemporal Preference Steering in Qwen3 via Contrastive Activation Addition](../../archive/papers/2026/arxiv-2608-03892/summary.md) — Trains a difference-of-means direction on short- versus long-horizon answer continuations and steers along it, shifting binary temporal choices, moving the monetary indifference threshold on an untrained task by a factor of 56 at a ten-year delay, and changing a planning benchmark — with matched-norm random controls and an unusually candid account of what the direction may actually encode.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
