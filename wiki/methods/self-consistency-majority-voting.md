# self-consistency (majority voting)

<!-- auto:begin -->

Self-consistency (majority voting) is sampling multiple independent reasoning attempts and taking the majority/plurality answer as the final one. In this archive it appears as the baseline SoftCoT's soft-thought-token method is meant to improve upon or complement, and as one of two signals (alongside PRM scores) that a separate paper derives an optimal weighted combination of for selecting responses at test time, cutting the compute needed for comparable accuracy versus using either signal alone.

- **Kind**: method
- **Also called**: self-consistency / majority voting
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [GSM8K](../datasets/gsm8k.md), [LLaMA-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [StrategyQA](../datasets/strategyqa.md), [Test-Time Scaling](../concepts/test-time-scaling.md)

## Appears in

- [SoftCoT: Soft Chain-of-Thought for Efficient Reasoning with LLMs](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-1137/summary.md) — SoftCoT keeps the backbone LLM frozen and instead uses a small auxiliary assistant model plus a trainable projection module to generate instance-specific continuous 'soft thought' tokens that prime the LLM's chain-of-thought, avoiding the catastrophic forgetting that full-model fine-tuning for continuous-space reasoning (e.g. Coconut) causes on modern instruction-tuned LLMs, and improving accuracy on five reasoning benchmarks with only ~6 soft tokens versus 24 hard tokens needed by a discrete-token assistant baseline.
- [Optimal Aggregation of LLM and PRM Signals for Efficient Test-Time Scaling](../../archive/papers/2026/title-68800e46710617dd/summary.md) — Derives and calibrates an optimal weighted combination of LLM self-consistency and PRM signals for selecting responses at test time, cutting compute needed for comparable accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
