# OpenMathReasoning

<!-- auto:begin -->

OpenMathReasoning is a math-reasoning dataset used to evaluate Parason (which distinguishes Subtask and Trial parallelism in LLM reasoning, showing Trial Parallelism dominates on hard reasoning traces) and ReasMark (a reasoning-model watermarking method for attributing knowledge distillation).

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC](amc.md), [Claude-Opus-4.5](../models/claude-opus-4-5.md), [critical-path latency](../concepts/critical-path-latency.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [Gemini-2.5-Pro](../models/gemini-2-5-pro.md), [Gemini-3-Pro](../models/gemini-3-pro.md), [GPT-5.5](../models/gpt-5-5.md), [GSM8K](gsm8k.md), [MATH](math.md), [MATH500](math500.md), [OpenCodeReasoning](opencodereasoning.md), [OpenR1-Math-220k](openr1-math-220k.md), [OpenThoughts-114k](openthoughts-114k.md), [Phi-4-mini-reasoning](../models/phi-4-mini-reasoning.md), [Qwen3-30B-A3B](../models/qwen3-30b-a3b.md)

## Appears in

- [Parason: Revealing Subtask and Trial Parallelism in LLM Reasoning](../../archive/papers/2026/arxiv-2608-24658/summary.md) — Parason distinguishes two forms of parallel reasoning -- AND-branch Subtask Parallelism and OR-branch Trial Parallelism -- shows Trial Parallelism dominates on hard reasoning traces, and trains models to convert sequential CoT into grammar-structured parallel trajectories that a real inference engine executes for ~1.7x wall-clock speedup with competitive accuracy.
- [ReasMark: A Robust Watermark for Attributing LLM Reasoning Under Knowledge Distillation Attacks](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2185/summary.md) — ReasMark protects proprietary reasoning models' intellectual property by training them to systematically produce longer chains-of-thought for prompts dominated by a secret 'long' high-frequency-token set and shorter chains for a 'short' token set (plus a matching entropy signature), so that a student model distilled from the protected model inherits this reasoning-length watermark and can be detected black-box via a one-sided t-test, surviving knowledge distillation, pruning, quantization and LoRA fine-tuning attacks where standard token-distribution watermarks fail.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
