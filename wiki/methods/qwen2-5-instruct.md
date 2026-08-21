# Qwen2.5-Instruct

<!-- auto:begin -->

Qwen2.5-Instruct is an instruction-tuned language model family that archived papers train and compare against, not a concept, method or dataset; the wiki has no kind for a model, so it is filed under the least wrong of the three available. IAPO trains it at 0.5B, 1.5B and 7B on GSM8K, MATH-500 and DAPO-Math-17k, its one concrete instance being Qwen2.5-7B-Instruct on GSM8K reaching 100% Pass@32 at 111.83 tokens against 177.62 for the S-GRPO baseline, roughly 37% fewer. ShorterBetter names it only as a comparison point alongside DeepSeek-R1-Distill-Qwen, Training Efficient and O1-Pruner; its own training is on the distilled models, not on this one. The name is used loosely for the whole size range rather than a single checkpoint, and the archive describes neither its architecture nor its instruction tuning.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME](../datasets/aime.md), [AMC](../datasets/amc.md), [chain-of-thought compression](../concepts/chain-of-thought-compression.md), [DAPO](dapo.md), [DAPO-Math-17k](../datasets/dapo-math-17k.md), [DeepSeek-R1-Distill-Qwen-1.5B](deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [GFPO](gfpo.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [HumanEval](../datasets/humaneval.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH](../datasets/math.md), [MATH-500](../datasets/math-500.md), [MathQA](../datasets/mathqa.md), [MBPP](../datasets/mbpp.md), [MMLU](../datasets/mmlu.md), [O1-Pruner](o1-pruner.md), [Omni-MATH](../datasets/omni-math.md), [overthinking](../concepts/overthinking.md), [Qwen3-8B](qwen3-8b.md), [Redundant Self-Verification](../concepts/redundant-self-verification.md), [Reinforcement Learning with Verifiable Rewards](../concepts/reinforcement-learning-with-verifiable-rewards.md), [S-GRPO](s-grpo.md), [Still](../datasets/still.md)

## Appears in

- [IAPO: Information-Aware Policy Optimization for Token-Efficient Reasoning](../../archive/papers/2026/title-4bd9ad89663d1e26/summary.md) — IAPO shapes token-level RL advantages by each reasoning token's conditional mutual information with the final answer, so uninformative exploration is suppressed rather than length being penalized in aggregate, reporting up to 36% shorter reasoning at equal or better accuracy on math benchmarks.
- [ShorterBetter: Guiding Reasoning Models to Find Optimal Inference Length for Efficient Reasoning](../../archive/papers/2025/title-d40396527f776f1d/summary.md) — ShorterBetter takes the length of the shortest correct response in a sampled group as a per-problem target and rewards the model for matching it, cutting output length by 50%-80% on DeepSeek-Distill-Qwen-1.5B/7B.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
