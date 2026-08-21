# Reward Shaping

<!-- auto:begin -->

Reward shaping here means adding structure to an RL reward beyond a single terminal correctness signal, to steer a specific behaviour during training. AutoThink uses a three-stage curriculum with stage-wise reward shaping so an R1-style model learns to decide, per problem, whether to reason explicitly at all; the second source shapes its reward across an SFT-then-GRPO pipeline so the choice between explicit reasoning and a direct answer tracks actual task difficulty rather than how verbosely the question is phrased.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [accuracy-efficiency tradeoff](accuracy-efficiency-tradeoff.md), [adaptive reasoning](adaptive-reasoning.md), [AIME 2024](../datasets/aime-2024.md), [AMC23](../datasets/amc23.md), [GPQA](../datasets/gpqa.md), [GRPO](../methods/grpo.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH](../datasets/math.md), [Minerva](../datasets/minerva.md), [MMLU](../datasets/mmlu.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](overthinking.md), [Test-Time Compute](test-time-compute.md)

## Appears in

- [Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL](../../archive/papers/2025/title-0bc5d9b198744bed/summary.md) — AutoThink uses a three-stage RL curriculum with stage-wise reward shaping to teach R1-style distilled models to decide per problem whether to emit an explicit reasoning chain at all.
- [When Simple Problems Wear Complex Costumes: Improving Efficiency in LRM's Adaptive Reasoning](../../archive/papers/2026/title-75760913d4d6cfa4/summary.md) — Trains an adaptive reasoning model in two stages -- SFT on simple problems presented in both concise and verbose phrasings, then GRPO with a custom reward -- so that its choice between explicit reasoning and a direct answer tracks actual task difficulty rather than how wordy the question is.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
