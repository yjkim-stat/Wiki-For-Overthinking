# GPQA-D

<!-- auto:begin -->

GPQA-D (GPQA-Diamond) is a graduate-level QA benchmark used in this archive to evaluate GRIP's reward-guided parameter interpolation for efficient reasoning and to validate the two-stage 'Reasoning Dynamics' structure (Pre-RCP Active Reasoning / Post-RCP Converged Reasoning) whose Reasoning Completion Point detector cuts tokens up to 44% while preserving or improving accuracy-per-token.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [AIME 2025](aime-2025.md), [DeepScaleR-preview (training)](deepscaler-preview-training.md), [GSM8K](gsm8k.md), [LiveCodeBench](livecodebench.md), [MATH500](math500.md), [Qwen3-4B-Instruct-2507](../models/qwen3-4b-instruct-2507.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md)

## Appears in

- [GRIP: Granular Reward-Guided Parameter Interpolation for Efficient Reasoning](../../archive/papers/2026/arxiv-2608-25583/summary.md) — GRIP fuses a reasoning model and an instruction (non-thinking) model of identical architecture by learning a separate sigmoid-controlled interpolation ratio per module (attention, FFN, embedding/LM-head), trained with an RL reward that favors correct and concise responses while keeping both source models frozen, cutting Qwen3-4B-Thinking's average generation length 27.0% while slightly improving average accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
