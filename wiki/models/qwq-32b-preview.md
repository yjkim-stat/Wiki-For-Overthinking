# QwQ-32B-Preview

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Best-of-N reranking](../methods/best-of-n-reranking.md), [DeepSeek-R1-Distill-Qwen-14B](deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [LiveCodeBench](../datasets/livecodebench.md), [LLaMA-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [OlympiadBench](../datasets/olympiadbench.md), [QwQ-32B](qwq-32b.md)

## Appears in

- [Reasoning Fails Where Step Flow Breaks](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1212/summary.md) — Step-Saliency pools token-level attention-gradient saliency into step-to-step maps across a reasoning trace's question/thinking/summary structure, revealing two depth-wise information-flow failures in incorrect outputs -- Shallow Lock-in (shallow layers over-focus on the current step, ignoring earlier context) and Deep Decay (deep layers lose connection to the thinking segment, with the summary attending mainly to itself) -- and fixes both with StepFlow, a training-free single-pass decoding intervention that improves accuracy by up to 11.8 points across six LRM backbones and six benchmarks.
- [Scaling Evaluation-Time Compute with Reasoning Models as Evaluators](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2102/summary.md) — Shows evaluation itself scales like generation: off-the-shelf reasoning models, simply prompted to generate a chain-of-thought judgment (no evaluator-specific training), improve monotonically with more reasoning tokens and, when made to individually assess every reasoning step rather than a single-pass judgment, a 32B reasoning evaluator beats a specialized 72B PRM by 4.5 F1 points on ProcessBench; folding this into Best-of-N reranking, spending the fixed test-time budget on evaluation-time reasoning (Best-of-8 with a reasoning evaluator) beats spending it on more candidate samples (Best-of-64 with a direct evaluator) by 4.30-6.63 points, and reasoning evaluators are shown to resist reward-model over-optimization that both direct evaluator types suffer from.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
