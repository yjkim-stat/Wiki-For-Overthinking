# Gemini 3 Flash Preview

<!-- auto:begin -->

Gemini 3 Flash Preview is a closed-weight model used in this archive as the prediction target for a lightweight (~1B-parameter) performance-bin classifier that estimates reasoning outcomes before an API call, and as the frontier-accuracy reference that Thinking with Reasoning Skills (TRS) and, separately, Prompt-Level Distillation aim to match or approach via cheaper inference-time methods.

- **Kind**: model
- **Also called**: Gemini-3-Flash-Preview
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Compute-optimal inference](../concepts/compute-optimal-inference.md), [Gemini 2.5 Flash](gemini-2-5-flash.md), [GPT-4o-mini](gpt-4o-mini.md), [gpt-oss-120b](gpt-oss-120b.md), [GPT-OSS-20B](gpt-oss-20b.md), [Qwen3-0.6B](qwen3-0-6b.md)

## Appears in

- [Can a Lightweight Multimodal Model Estimate LLM Reasoning Performance? A Study for Compute-Optimal Document Inference](../../archive/papers/2026/arxiv-2608-18591/summary.md) — Trains a ~1B-parameter multimodal model to predict, before any API call, which of seven performance bins a frontier LLM will land in for a given (document, prompt, model, reasoning budget) tuple, and uses those predictions to pick a per-sample reasoning budget for document tasks.
- [Thinking with Reasoning Skills: Fewer Tokens, More Accuracy](../../archive/papers/2026/doi-10-18653-v1-2026-acl-industry-154/summary.md) — Thinking with Reasoning Skills (TRS) is a training-free, black-box-compatible framework that offline-distills long deliberation trajectories (successes and failures) into compact, retrievable 'skill cards' (Trigger/Do/Avoid/Check/Risk), retrieves and injects the most relevant cards into a new query's prompt at inference time instead of forcing the model to re-derive solution logic from scratch, and empirically reduces reasoning tokens while matching or improving accuracy versus standard CoT across multiple LLMs on math and coding benchmarks -- with gains growing on harder problems, unlike budget-forcing baselines (TALE, Chain-of-Draft) which collapse below baseline accuracy as difficulty increases.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
