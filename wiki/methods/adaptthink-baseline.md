# AdaptThink (baseline)

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [compression ratio](../concepts/compression-ratio.md), [DAPO (baseline)](dapo-baseline.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER (baseline)](deer-baseline.md), [DPO (baseline)](dpo-baseline.md), [Dynasor-CoT (baseline)](dynasor-cot-baseline.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [IFEval](../datasets/ifeval.md), [LC-R1 (baseline)](lc-r1-baseline.md), [LiveCodeBench](../datasets/livecodebench.md), [LiveCodeBench-v6](../datasets/livecodebench-v6.md), [MATH500](../datasets/math500.md), [O1-Pruner (baseline)](o1-pruner-baseline.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-8B](../models/qwen3-8b.md), [Reasoning Collapse](../concepts/reasoning-collapse.md), [SFT (baseline)](sft-baseline.md), [Thinkless (baseline)](thinkless-baseline.md)

## Appears in

- [Efficiently Learning To Reason or Not to Reason: Root-token Policy Optimization for Adaptive Thinking](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-816/summary.md) — Root-token Policy Optimization (RPO) reframes adaptive thinking/non-thinking gating as a branching decision at a single root token (the newline choice right after <think>) and trains only that one token's probability with group-relative RL, cutting GRPO training compute to ~2% of a comparable adaptive-reasoning method while improving the accuracy-vs-thinking-rate tradeoff across model families.
- [Exploration-Exploitation Reshaping towards Efficient Reasoning for Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1520/summary.md) — SIGMA reframes token-efficient RL as a classical exploration-exploitation problem: a self-imitation exploitation module prioritizes training on prompts/rollouts with high compression potential via a dynamic priority table and a compression-ratio-weighted self-imitation loss, while a self-guidance exploration module directs otherwise-undirected long-response exploration via prompt-based token-budget regeneration or random truncation -- improving average accuracy by 7.9%/2.9% while cutting average reasoning length 43.4%/40.3% on 1.5B/7B DeepSeek-R1-Distill models across six benchmarks, beating eight RL-based efficient-reasoning baselines.
- [PACE: Prefix-Protected and Difficulty-Aware Compression for Efficient Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1545/summary.md) — PACE identifies two distinct failure modes of uniform length-penalty RL for efficient reasoning -- sequence-level over-compression of critical early deduction steps, and group-level indiscriminate compression that ignores query difficulty -- and fixes both with a frozen-policy prefix-rollout anchor (decaying over training) plus a pass-rate-derived, difficulty-scaled length penalty, becoming the only compared method to cut token usage over 45% while simultaneously improving accuracy, and generalizing to code, science and instruction-following domains.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
