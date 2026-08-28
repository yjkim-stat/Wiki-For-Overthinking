# Thinkless (baseline)

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Also called**: ThinkLess (baseline)
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [ARC-Challenge](../datasets/arc-challenge.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH500](../datasets/math500.md), [Omni-MATH](../datasets/omni-math.md), [Overthinking](../concepts/overthinking.md), [Phi-4-Reasoning](phi-4-reasoning.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-8B](../models/qwen3-8b.md)

## Appears in

- [Efficiently Learning To Reason or Not to Reason: Root-token Policy Optimization for Adaptive Thinking](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-816/summary.md) — Root-token Policy Optimization (RPO) reframes adaptive thinking/non-thinking gating as a branching decision at a single root token (the newline choice right after <think>) and trains only that one token's probability with group-relative RL, cutting GRPO training compute to ~2% of a comparable adaptive-reasoning method while improving the accuracy-vs-thinking-rate tradeoff across model families.
- [ThinkBrake: Efficient Reasoning via Log-Probability Margin Guided Decoding](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1095/summary.md) — ThinkBrake is a training-free decoding rule that injects </think> at sentence boundaries whenever the log-probability margin between the top continuation token and </think> narrows below a threshold, recovering most of an oracle stopping point's headroom (8% accuracy gain, 72% token reduction) with a theoretically grounded, model-agnostic criterion, and its generated trajectories can also train models via DPO for training-free-free efficient reasoning.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
