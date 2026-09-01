# Accuracy-Efficiency Score (AES)

<!-- auto:begin -->

The two archived papers tagged to this entity -- BLADE, which trains a hidden-state probe to exit generation once a reasoning prefix already supports the correct answer, and DRPO, which fixes the accuracy loss GRPO suffers under a length penalty by normalising correct rollouts only against other correct rollouts -- both aim at reporting accuracy and token cost together, but neither note states what the Accuracy-Efficiency Score is, how it is computed, or what range it takes. On the evidence in the archive this is a single-number summary metric combining task accuracy with generation cost, and nothing more specific can honestly be said until one of the source papers is read for its formula.

- **Kind**: concept
- **Also called**: AES, Accuracy Efficiency Score (AES)
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [accuracy-efficiency tradeoff](accuracy-efficiency-tradeoff.md), [AIME](../datasets/aime.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DPO (baseline)](../methods/dpo-baseline.md), [Dynamic Early Exit](../methods/dynamic-early-exit.md), [Efficient Reasoning](efficient-reasoning.md), [Group-Relative Advantage](group-relative-advantage.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [Hidden-State Probing](hidden-state-probing.md), [Length reward](length-reward.md), [MATH500](../datasets/math500.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](overthinking.md), [Overthinking-Adjusted Accuracy (OAA)](overthinking-adjusted-accuracy-oaa.md), [QwQ-32B-Preview](../models/qwq-32b-preview.md), [RLOO](../methods/rloo.md), [SFT (baseline)](../methods/sft-baseline.md)

## Appears in

- [BLADE: Boundary-Expanded and Layer-Adaptive Dynamic Exit for Efficient LLM Reasoning](../../archive/papers/2026/arxiv-2607-28966/summary.md) — BLADE trains a lightweight hidden-state probe to decide, at sentence and self-doubt boundaries, whether a reasoning prefix already supports the correct answer, and stops generation when it does.
- [O1-Pruner: Length-Harmonizing Fine-Tuning for O1-Like Reasoning Pruning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-697/summary.md) — O1-Pruner identifies 'length disharmony' -- shorter responses often achieve equal or higher accuracy than longer ones, at both the instance and distribution level -- and fine-tunes long-thought models with a PPO-style Length-Harmonizing Reward that rewards brevity relative to a reference model's own pre-sampled length/accuracy baseline, subject to an accuracy non-degradation constraint, cutting solution length by 34.7-40.5% while improving accuracy.
- [DRPO: Efficient Reasoning via Decoupled Reward Policy Optimization](../../archive/papers/2026/title-68327bf6b9e4e869/summary.md) — Diagnoses why adding a length penalty to GRPO degrades accuracy — the group-relative advantage can turn correct-but-long rollouts negative — and fixes it by normalising the reward of correct rollouts only against other correct rollouts.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
