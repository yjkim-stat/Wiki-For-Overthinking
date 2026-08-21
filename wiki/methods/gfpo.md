# GFPO

<!-- auto:begin -->

GFPO keeps GRPO's group-relative structure and changes only what reaches the gradient: it samples a larger group per question (G tested at 8, 16, 24), scores each response by a selection metric — shortest length, or token efficiency defined as reward divided by token count — and assigns zero advantage to everything outside the top-k, with k held at 8 or below so the number of responses producing gradient signal matches GRPO's. The retained fraction k/G is the length knob; on Phi-4-reasoning the shortest-response variant cuts GRPO's excess length by 23.7-36.5% across five benchmarks and the token-efficiency variant by 70.9-84.6%, with no statistically significant accuracy difference from GRPO, and Adaptive Difficulty GFPO sets k per question (4 easy, 6 medium, 8 hard, out of G=16) so hard problems keep more long solutions. The trade it names explicitly is training-time sampling converted into reduced test-time compute. IAPO cites it only as one of four baselines (with DAPO, GTPO and S-GRPO) that it reports beating on the Pass@k/Length@k ratio.

- **Kind**: method
- **Also called**: Group Filtered Policy Optimization
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [DAPO](dapo.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [GPQA](../datasets/gpqa.md), [Group-Relative Advantage](../concepts/group-relative-advantage.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH500](../datasets/math500.md), [Omni-MATH](../datasets/omni-math.md), [Overthinking](../concepts/overthinking.md), [Phi-4-reasoning](phi-4-reasoning.md), [Qwen2.5-Instruct](qwen2-5-instruct.md), [RLVR](rlvr.md), [S-GRPO](s-grpo.md)

## Appears in

- [IAPO: Information-Aware Policy Optimization for Token-Efficient Reasoning](../../archive/papers/2026/title-4bd9ad89663d1e26/summary.md) — IAPO shapes token-level RL advantages by each reasoning token's conditional mutual information with the final answer, so uninformative exploration is suppressed rather than length being penalized in aggregate, reporting up to 36% shorter reasoning at equal or better accuracy on math benchmarks.
- [Sample More to Think Less: Group Filtered Policy Optimization for Concise Reasoning](../../archive/papers/2026/title-d02c8db6721c4d3c/summary.md) — GFPO samples a larger group of rollouts per problem during RL training and updates only on the top-k by length or by reward-per-token, converting extra training-time compute into shorter responses at inference.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
