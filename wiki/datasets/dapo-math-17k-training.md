# DAPO-Math-17k (training)

<!-- auto:begin -->

DAPO-Math-17K is used in these sources as an RL training corpus for reasoning-efficiency methods: Step-GRPO selects its training data from it across three model scales, and the entropy-in-RLVR study trains Qwen2.5-Math-7B on it via GRPO to study clipping-threshold, off-policy-update, and data-diversity effects on entropy collapse.

- **Kind**: dataset
- **Also called**: DAPO-Math-17K (training)
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [entropy collapse](../concepts/entropy-collapse.md), [GPQA-Diamond](gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [IFEval](ifeval.md), [LiveCodeBench](livecodebench.md), [MATH500](math500.md), [Minerva](minerva.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-8B](../models/qwen3-8b.md)

## Appears in

- [Step-GRPO: Internalizing Dynamic Early Exit for Efficient Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-990/summary.md) — Step-GRPO internalizes dynamic early-exit into a reasoning model's own weights via a Dynamic Truncated Rollout exposing the model to short-yet-correct trajectories during RL training and a Step-Aware Relative Reward that penalizes redundant semantic steps relative to the group's own correct-completion baseline, cutting Qwen3-8B token usage 32.0% with no accuracy loss and zero inference-time overhead.
- [Revisiting Entropy in Reinforcement Learning for Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1266/summary.md) — A systematic study of entropy collapse in GRPO-based RLVR training finds performance can improve without entropy loss (so entropy collapse is not merely a side effect of legitimate learning), identifies clipping thresholds, off-policy update count, and training-data diversity as governing factors, proves theoretically and confirms empirically that positive-advantage tokens are the primary driver of entropy collapse, and proposes Positive-Advantage Reweighting -- dynamically down-weighting positive-advantage-token loss -- to regulate entropy while maintaining performance, though training exclusively on non-positive-advantage tokens actually hurts benchmark scores despite reducing collapse.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
