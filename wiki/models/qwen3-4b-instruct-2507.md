# Qwen3-4B-Instruct-2507

<!-- auto:begin -->

An open-weight instruction-tuned model used across sources as a cross-model transfer test subject for decoding-time code-verification methods (DTV), and as one of the two identical-architecture models (paired with Qwen3-4B-Thinking-2507) that GRIP's module-wise, RL-learned interpolation fuses to reduce reasoning-model overthinking while preserving or improving accuracy.

- **Kind**: model
- **Also called**: Qwen3-4B-Instruct
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2025](../datasets/aime-2025.md), [best-of-N](../methods/best-of-n.md), [DeepScaleR-preview (training)](../datasets/deepscaler-preview-training.md), [Gemma-4-E4B](gemma-4-e4b.md), [GPQA-D](../datasets/gpqa-d.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH500](../datasets/math500.md), [Qwen3-4B-Thinking-2507](qwen3-4b-thinking-2507.md), [self-refine](../methods/self-refine.md)

## Appears in

- [Verifier-Guided Code Translation via Meta-Step Decoding](../../archive/papers/2026/arxiv-2605-17626/summary.md) — Decoding Time Verification (DTV) interleaves code generation with deterministic verifier calls (compiler, type checker) at structural boundaries, using structure-aware rollback and diagnostic feedback instead of post-hoc filtering, to translate code more accurately and more token-efficiently than resampling-based test-time scaling.
- [GRIP: Granular Reward-Guided Parameter Interpolation for Efficient Reasoning](../../archive/papers/2026/arxiv-2608-25583/summary.md) — GRIP fuses a reasoning model and an instruction (non-thinking) model of identical architecture by learning a separate sigmoid-controlled interpolation ratio per module (attention, FFN, embedding/LM-head), trained with an RL reward that favors correct and concise responses while keeping both source models frozen, cutting Qwen3-4B-Thinking's average generation length 27.0% while slightly improving average accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
