# No-Wait (baseline)

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Also called**: NoWait (baseline)
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [ARC-Challenge](../datasets/arc-challenge.md), [DAST (baseline)](dast-baseline.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER (baseline)](deer-baseline.md), [Dynasor-CoT (baseline)](dynasor-cot-baseline.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [MATH500](../datasets/math500.md), [O1-Pruner (baseline)](o1-pruner-baseline.md), [Omni-MATH](../datasets/omni-math.md), [Overthinking](../concepts/overthinking.md), [Phi-4-Reasoning](phi-4-reasoning.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-4B-Thinking](../models/qwen3-4b-thinking.md), [Thinkless (baseline)](thinkless-baseline.md)

## Appears in

- [ThinkBrake: Efficient Reasoning via Log-Probability Margin Guided Decoding](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1095/summary.md) — ThinkBrake is a training-free decoding rule that injects </think> at sentence boundaries whenever the log-probability margin between the top continuation token and </think> narrows below a threshold, recovering most of an oracle stopping point's headroom (8% accuracy gain, 72% token reduction) with a theoretically grounded, model-agnostic criterion, and its generated trajectories can also train models via DPO for training-free-free efficient reasoning.
- [AdapThink: Adaptive Thinking Preferences for Reasoning Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-477/summary.md) — AdapThink measures reflection behavior with a BERT classifier (trained on DeepSeek-R1-Distill-Qwen-32B-annotated 256-token segments, 98.86% F1) to find incorrect reasoning has systematically more reflection segments than correct reasoning at every model scale, then trains a group-relative reasoning-process reward that only discourages reflection once group accuracy exceeds a threshold (below it, no length pressure at all) combined with dispersion-maximizing sample selection that explicitly diversifies reasoning patterns within each training group -- cutting length 33.15%/29.10% on 1.5B/7B models while improving accuracy +6.59/+6.12 over GRPO, adaptively producing *longer* answers on hard AIME problems under a 32K context despite training at a strict 2K token limit, transferring to code generation and out-of-distribution benchmarks, and showing near-zero reward-hacking (0.7% N-gram repetition vs. LCPO's 10.8%).

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
