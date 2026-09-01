# Qwen3-0.6B

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [Compute-optimal inference](../concepts/compute-optimal-inference.md), [Gemini 2.5 Flash](gemini-2-5-flash.md), [Gemini 3 Flash Preview](gemini-3-flash-preview.md), [GPQA](../datasets/gpqa.md), [GSM8K](../datasets/gsm8k.md), [HMMT](../datasets/hmmt.md), [HumanEval](../datasets/humaneval.md), [MATH500](../datasets/math500.md), [Qwen3-1.7B](qwen3-1-7b.md)

## Appears in

- [Can a Lightweight Multimodal Model Estimate LLM Reasoning Performance? A Study for Compute-Optimal Document Inference](../../archive/papers/2026/arxiv-2608-18591/summary.md) — Trains a ~1B-parameter multimodal model to predict, before any API call, which of seven performance bins a frontier LLM will land in for a given (document, prompt, model, reasoning budget) tuple, and uses those predictions to pick a per-sample reasoning budget for document tasks.
- [Thermometer of Thoughts: Enhancing LLM’s Exploration via Attention Temperature Modulation](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-200/summary.md) — Introduces attention-temperature modulation (softening/sharpening the attention softmax at inference, distinct from decoding-temperature sampling) as a difficulty-adaptive exploration control -- higher attention temperature broadens exploration and helps hard problems, lower temperature curbs overthinking and helps easy ones -- and pairs it with a difficulty-induced weighted-voting aggregation scheme (Thermometer of Thoughts), improving Pass@10 by 6.78-14.20% and aggregation accuracy by 9.74% across seven reasoning benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
