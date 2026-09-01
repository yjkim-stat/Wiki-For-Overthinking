# DAST (baseline)

<!-- auto:begin -->

DAST is a difficulty-aware baseline for efficient/compressed reasoning, cited as a comparison point by PACE (which identifies over-compression failure modes of uniform length-penalty RL that difficulty-aware methods like DAST aim to avoid) and by AdapThink (which measures reflection behavior with a BERT classifier finding incorrect reasoning has systematically more reflection than DAST-style baselines address).

- **Kind**: method
- **Also called**: DAST
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AdaptThink (baseline)](adaptthink-baseline.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER (baseline)](deer-baseline.md), [Dynasor-CoT (baseline)](dynasor-cot-baseline.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [IFEval](../datasets/ifeval.md), [LiveCodeBench-v6](../datasets/livecodebench-v6.md), [MATH500](../datasets/math500.md), [O1-Pruner (baseline)](o1-pruner-baseline.md), [Overthinking](../concepts/overthinking.md), [Reasoning Collapse](../concepts/reasoning-collapse.md)

## Appears in

- [PACE: Prefix-Protected and Difficulty-Aware Compression for Efficient Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1545/summary.md) — PACE identifies two distinct failure modes of uniform length-penalty RL for efficient reasoning -- sequence-level over-compression of critical early deduction steps, and group-level indiscriminate compression that ignores query difficulty -- and fixes both with a frozen-policy prefix-rollout anchor (decaying over training) plus a pass-rate-derived, difficulty-scaled length penalty, becoming the only compared method to cut token usage over 45% while simultaneously improving accuracy, and generalizing to code, science and instruction-following domains.
- [AdapThink: Adaptive Thinking Preferences for Reasoning Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-477/summary.md) — AdapThink measures reflection behavior with a BERT classifier (trained on DeepSeek-R1-Distill-Qwen-32B-annotated 256-token segments, 98.86% F1) to find incorrect reasoning has systematically more reflection segments than correct reasoning at every model scale, then trains a group-relative reasoning-process reward that only discourages reflection once group accuracy exceeds a threshold (below it, no length pressure at all) combined with dispersion-maximizing sample selection that explicitly diversifies reasoning patterns within each training group -- cutting length 33.15%/29.10% on 1.5B/7B models while improving accuracy +6.59/+6.12 over GRPO, adaptively producing *longer* answers on hard AIME problems under a 32K context despite training at a strict 2K token limit, transferring to code generation and out-of-distribution benchmarks, and showing near-zero reward-hacking (0.7% N-gram repetition vs. LCPO's 10.8%).

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
