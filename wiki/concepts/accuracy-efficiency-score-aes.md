# Accuracy-Efficiency Score (AES)

<!-- auto:begin -->

The two archived papers tagged to this entity -- BLADE, which trains a hidden-state probe to exit generation once a reasoning prefix already supports the correct answer, and DRPO, which fixes the accuracy loss GRPO suffers under a length penalty by normalising correct rollouts only against other correct rollouts -- both aim at reporting accuracy and token cost together, but neither note states what the Accuracy-Efficiency Score is, how it is computed, or what range it takes. On the evidence in the archive this is a single-number summary metric combining task accuracy with generation cost, and nothing more specific can honestly be said until one of the source papers is read for its formula.

- **Kind**: concept
- **Also called**: AES, Accuracy Efficiency Score (AES)
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Accuracy-Efficiency Tradeoff](accuracy-efficiency-tradeoff.md), [AIME](../datasets/aime.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Dynamic Early Exit](../methods/dynamic-early-exit.md), [Efficient Reasoning](efficient-reasoning.md), [group relative advantage](group-relative-advantage.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [Hidden-State Probing](hidden-state-probing.md), [Length reward](length-reward.md), [MATH-500](../datasets/math-500.md), [OlympiadBench](../datasets/olympiadbench.md), [overthinking](overthinking.md), [Overthinking-Adjusted Accuracy (OAA)](overthinking-adjusted-accuracy-oaa.md), [RLOO](../methods/rloo.md)

## Appears in

- [BLADE: Boundary-Expanded and Layer-Adaptive Dynamic Exit for Efficient LLM Reasoning](../../archive/papers/2026/arxiv-2607-28966/summary.md) — BLADE trains a lightweight hidden-state probe to decide, at sentence and self-doubt boundaries, whether a reasoning prefix already supports the correct answer, and stops generation when it does.
- [DRPO: Efficient Reasoning via Decoupled Reward Policy Optimization](../../archive/papers/2026/title-68327bf6b9e4e869/summary.md) — Diagnoses why adding a length penalty to GRPO degrades accuracy — the group-relative advantage can turn correct-but-long rollouts negative — and fixes it by normalising the reward of correct rollouts only against other correct rollouts.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
