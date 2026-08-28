# GPQA-D

<!-- auto:begin -->

GPQA-D (GPQA-Diamond) is a graduate-level QA benchmark used in this archive to evaluate GRIP's reward-guided parameter interpolation for efficient reasoning and to validate the two-stage 'Reasoning Dynamics' structure (Pre-RCP Active Reasoning / Post-RCP Converged Reasoning) whose Reasoning Completion Point detector cuts tokens up to 44% while preserving or improving accuracy-per-token.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [DeepScaleR-preview (training)](deepscaler-preview-training.md), [GSM8K](gsm8k.md), [LiveCodeBench](livecodebench.md), [MATH500](math500.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-30B-A3B](../models/qwen3-30b-a3b.md), [Qwen3-4B-Instruct-2507](../models/qwen3-4b-instruct-2507.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [Qwen3-8B](../models/qwen3-8b.md)

## Appears in

- [GRIP: Granular Reward-Guided Parameter Interpolation for Efficient Reasoning](../../archive/papers/2026/arxiv-2608-25583/summary.md) — GRIP fuses a reasoning model and an instruction (non-thinking) model of identical architecture by learning a separate sigmoid-controlled interpolation ratio per module (attention, FFN, embedding/LM-head), trained with an RL reward that favors correct and concise responses while keeping both source models frozen, cutting Qwen3-4B-Thinking's average generation length 27.0% while slightly improving average accuracy.
- [The Evolution of Thought: Tracking LLM Overthinking via Reasoning Dynamics Analysis](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1239/summary.md) — Identifies a two-stage 'Reasoning Dynamics' structure in LRM chains-of-thought -- a Pre-RCP Active Reasoning stage where thinking length and content length compensate for each other, followed by a Post-RCP Converged Reasoning stage where the semantic trajectory has stabilized and further thinking is redundant -- defines the boundary as the instance-specific Reasoning Completion Point (RCP), and builds RCPD, an online detector (monitoring the rank of the </think> token) that truncates post-RCP overthinking, cutting tokens up to 44% while preserving or improving accuracy-per-token across four models and three benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
