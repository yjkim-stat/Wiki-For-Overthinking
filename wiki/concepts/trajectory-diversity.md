# trajectory diversity

<!-- auto:begin -->

How many genuinely different solution paths a policy will produce, as against how many samples it draws. Both sources argue reinforcement learning erodes it and locate the erosion in credit rather than in entropy. One measures a policy's preference between two specific verifier-equivalent continuations at a shared branch point and finds RLVR policies more decided than distilled ones on 95.5-100% of branches, with the collapse significantly stronger for semantically distinct continuations than for syntactic variants of the same statement. The other identifies the mechanism in the objective: with binary rewards every verified-correct completion receives the same positive advantage, so a recurring solution form accumulates positive coefficient mass proportional to how often it is sampled, and the fitted slope of cluster credit against cluster size is 1.00. Both then show the cost is real at high sampling budgets, where retaining alternative correct modes is what solves hard problems.

- **Kind**: concept
- **Also called**: diversity collapse, solution diversity
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [advantage estimation](advantage-estimation.md), [AIME](../datasets/aime.md), [backtracking](backtracking.md), [credit assignment](credit-assignment.md), [DAPO](../methods/dapo.md), [DAPO-Math-17k](../datasets/dapo-math-17k.md), [entropy collapse](entropy-collapse.md), [exploration](exploration.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [long chain-of-thought distillation](../methods/long-chain-of-thought-distillation.md), [LoRA](../methods/lora.md), [MATH](../datasets/math.md), [MATH-500](../datasets/math-500.md), [pass@k](../methods/pass-k.md), [policy entropy](policy-entropy.md), [Qwen2.5-32B-Instruct](../models/qwen2-5-32b-instruct.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen3-8B-Base](../models/qwen3-8b-base.md), [reasoning boundary](reasoning-boundary.md), [RLVR](../methods/rlvr.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md)

## Appears in

- [BODHI: Do LLMs Branch Out and Discover Heterogeneous Inferences?](../../archive/papers/2026/arxiv-2608-02867/summary.md) — Builds prefix trees of semantically equivalent reasoning statements and measures how RLVR changes a model's preference between branches, finding the entropy collapse is not stylistic — the collapse is stronger for semantically distinct continuations than for syntactic variants of the same statement.
- [When Correct Solutions Repeat: Rarity-Aware Credit Redistribution for GRPO](../../archive/papers/2026/arxiv-2608-03467/summary.md) — Shows that GRPO's per-completion uniformity is frequency-skewed once credit is aggregated by solution structure — a recurring correct form accumulates positive coefficient mass proportional to how often it is sampled — and rebalances it by a rarity exponent over a partition built from deterministic cue signatures rather than a judge model.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
