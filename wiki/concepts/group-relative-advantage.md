# group relative advantage

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Also called**: Group-Relative Advantage, Group-relative advantage
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [Accuracy-Efficiency Score (AES)](accuracy-efficiency-score-aes.md), [Accuracy-Efficiency Tradeoff](accuracy-efficiency-tradeoff.md), [AIME](../datasets/aime.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [Efficient Reasoning](efficient-reasoning.md), [GFPO](../methods/gfpo.md), [GPQA](../datasets/gpqa.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [Length reward](length-reward.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH-500](../datasets/math-500.md), [OlympiadBench](../datasets/olympiadbench.md), [Omni-MATH](../datasets/omni-math.md), [overthinking](overthinking.md), [Phi-4-reasoning](../methods/phi-4-reasoning.md), [Reinforcement Learning with Verifiable Rewards](../methods/reinforcement-learning-with-verifiable-rewards.md), [RLOO](../methods/rloo.md)

## Appears in

- [DRPO: Efficient Reasoning via Decoupled Reward Policy Optimization](../../archive/papers/2026/title-68327bf6b9e4e869/summary.md) — Diagnoses why adding a length penalty to GRPO degrades accuracy — the group-relative advantage can turn correct-but-long rollouts negative — and fixes it by normalising the reward of correct rollouts only against other correct rollouts.
- [Sample More to Think Less: Group Filtered Policy Optimization for Concise Reasoning](../../archive/papers/2026/title-d02c8db6721c4d3c/summary.md) — GFPO samples a larger group of rollouts per problem during RL training and updates only on the top-k by length or by reward-per-token, converting extra training-time compute into shorter responses at inference.
- [DisCO: Reinforcing Large Reasoning Models with Discriminative Constrained Optimization](../../archive/papers/2025/title-ec9090a2d1f7fb05/summary.md) — Proposes DisCO, a discriminative constrained-optimization alternative to GRPO for RL-training of large reasoning models, that removes question-level difficulty bias and entropy instability, giving average gains of 7% over GRPO and 6% over DAPO on math reasoning benchmarks with a 1.5B model.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
