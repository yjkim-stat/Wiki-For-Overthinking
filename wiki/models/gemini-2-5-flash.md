# Gemini 2.5 Flash

<!-- auto:begin -->

Gemini 2.5 Flash is cited in this archive as the prediction target for a lightweight (~1B-parameter) multimodal model that estimates LLM reasoning performance bins before an API call to guide compute-optimal reasoning-budget selection, and appears in the construction pipeline of LEGIT, a legal-reasoning-trace benchmark, as one of the LLMs used to extract facts and issue structure from court judgments.

- **Kind**: model
- **Also called**: Gemini-2.5-Flash
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AdvBench](../datasets/advbench.md), [Claude-3.7-Sonnet](claude-3-7-sonnet.md), [Compute-optimal inference](../concepts/compute-optimal-inference.md), [DeepSeek-R1](deepseek-r1.md), [Gemini-2.0-Flash](gemini-2-0-flash.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [Gemini 3 Flash Preview](gemini-3-flash-preview.md), [GPT-4.1-mini](gpt-4-1-mini.md), [gpt-o3](gpt-o3.md), [HarmBench](../datasets/harmbench.md), [Qwen3-0.6B](qwen3-0-6b.md), [Qwen3-8B](qwen3-8b.md), [StrongReject](../datasets/strongreject.md)

## Appears in

- [Can a Lightweight Multimodal Model Estimate LLM Reasoning Performance? A Study for Compute-Optimal Document Inference](../../archive/papers/2026/arxiv-2608-18591/summary.md) — Trains a ~1B-parameter multimodal model to predict, before any API call, which of seven performance bins a frontier LLM will land in for a given (document, prompt, model, reasoning budget) tuple, and uses those predictions to pick a per-sample reasoning budget for document tasks.
- [Evaluating Legal Reasoning Traces with Legal Issue Tree Rubrics](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-150/summary.md) — LEGIT is a 24K-instance Korean legal-judgment-prediction benchmark that converts real court judgments into hierarchical legal issue trees, using them as fine-grained rubrics (issue coverage and issue correctness, alongside final-order correctness) to evaluate LLM reasoning traces with human-lawyer-level reliability, and shows retrieval-augmented generation and RL-with-rubrics have complementary effects on legal reasoning quality.
- [AutoRAN: Automated Hijacking of Safety Reasoning in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1988/summary.md) — AutoRAN is the first automated framework for hijacking a large reasoning model's internal safety deliberation, using a weaker, less-aligned auxiliary model to simulate the target's execution reasoning and iteratively refine attack prompts from leaked refusal reasoning, achieving near-100% attack success against gpt-o3/o4-mini and Gemini-2.5-Flash within a few turns.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
