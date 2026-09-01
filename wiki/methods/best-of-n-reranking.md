# Best-of-N reranking

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Also called**: best-of-n reranking
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AMC23](../datasets/amc23.md), [GPQA](../datasets/gpqa.md), [LLaMA-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [OlympiadBench](../datasets/olympiadbench.md), [process reward model](process-reward-model.md), [QwQ-32B](../models/qwq-32b.md), [QwQ-32B-Preview](../models/qwq-32b-preview.md), [Test-Time Scaling](../concepts/test-time-scaling.md)

## Appears in

- [Scaling Evaluation-Time Compute with Reasoning Models as Evaluators](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2102/summary.md) — Shows evaluation itself scales like generation: off-the-shelf reasoning models, simply prompted to generate a chain-of-thought judgment (no evaluator-specific training), improve monotonically with more reasoning tokens and, when made to individually assess every reasoning step rather than a single-pass judgment, a 32B reasoning evaluator beats a specialized 72B PRM by 4.5 F1 points on ProcessBench; folding this into Best-of-N reranking, spending the fixed test-time budget on evaluation-time reasoning (Best-of-8 with a reasoning evaluator) beats spending it on more candidate samples (Best-of-64 with a direct evaluator) by 4.30-6.63 points, and reasoning evaluators are shown to resist reward-model over-optimization that both direct evaluator types suffer from.
- [Evaluating Judges as Evaluators: The JETTS Benchmark of LLM-as-Judges as Test-Time Scaling Evaluators](../../archive/papers/2025/title-ab80eef8a7c42e7c/summary.md) — JETTS is a benchmark evaluating how well LLM-as-judge models perform as evaluators guiding test-time-scaling methods -- response reranking, step-level beam search, and critique-based refinement -- across math, code and instruction-following.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
