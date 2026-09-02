# Qwen3-0.6B

<!-- auto:begin -->

Qwen3-0.6B is a small model referenced as a scale point in a study training a ~1B-parameter multimodal model to predict, before any API call, which of seven performance bins a frontier LLM will land in for a given input, and in Thermometer of Thoughts (attention-temperature modulation as a difficulty-adaptive exploration control).

- **Kind**: model
- **Also called**: Qwen-3-0.6B
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [Claude-3.7-Sonnet](claude-3-7-sonnet.md), [Compute-optimal inference](../concepts/compute-optimal-inference.md), [Direct Preference Optimization (DPO)](../methods/direct-preference-optimization-dpo.md), [Gemini 2.5 Flash](gemini-2-5-flash.md), [Gemini 3 Flash Preview](gemini-3-flash-preview.md), [GPQA](../datasets/gpqa.md), [GSM8K](../datasets/gsm8k.md), [HMMT](../datasets/hmmt.md), [HumanEval](../datasets/humaneval.md), [LogiQA](../datasets/logiqa.md), [MATH500](../datasets/math500.md), [MedQA](../datasets/medqa.md), [Qwen3-1.7B](qwen3-1-7b.md), [Qwen3-14B](qwen3-14b.md), [Qwen3-4B](qwen3-4b.md), [Qwen3-8B](qwen3-8b.md)

## Appears in

- [Can a Lightweight Multimodal Model Estimate LLM Reasoning Performance? A Study for Compute-Optimal Document Inference](../../archive/papers/2026/arxiv-2608-18591/summary.md) — Trains a ~1B-parameter multimodal model to predict, before any API call, which of seven performance bins a frontier LLM will land in for a given (document, prompt, model, reasoning budget) tuple, and uses those predictions to pick a per-sample reasoning budget for document tasks.
- [Thermometer of Thoughts: Enhancing LLM’s Exploration via Attention Temperature Modulation](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-200/summary.md) — Introduces attention-temperature modulation (softening/sharpening the attention softmax at inference, distinct from decoding-temperature sampling) as a difficulty-adaptive exploration control -- higher attention temperature broadens exploration and helps hard problems, lower temperature curbs overthinking and helps easy ones -- and pairs it with a difficulty-induced weighted-voting aggregation scheme (Thermometer of Thoughts), improving Pass@10 by 6.78-14.20% and aggregation accuracy by 9.74% across seven reasoning benchmarks.
- [Correct Reasoning Paths Visit Shared Decision Pivots](../../archive/papers/2026/local-f8a4b161736737f2/summary.md) — Proposes that correct chain-of-thought paths for a given question converge on a small shared set of verifiable 'decision pivots', and builds a self-training pipeline that intersects multiple sampled correct paths into a compact pivot-focused reasoning trace used as the preferred completion for DPO, improving accuracy on LogiQA, MedQA and MATH500 over prior self-training baselines while also shortening generated reasoning as a side effect.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
