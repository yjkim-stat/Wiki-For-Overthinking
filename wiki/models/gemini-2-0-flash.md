# Gemini-2.0-Flash

<!-- auto:begin -->

Gemini 2.0 Flash is used in these sources as an evaluated or judging model in reasoning-trace-quality benchmarks: LEGIT uses it (among other LLMs) in a Korean legal-reasoning-trace evaluation with hierarchical issue-tree rubrics, and ReTraceQA uses it in evaluating small-language-model reasoning traces on commonsense QA, without further characterization of the model itself.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [CommonsenseQA](../datasets/commonsenseqa.md), [DeepSeek-R1](deepseek-r1.md), [Gemini 2.5 Flash](gemini-2-5-flash.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [GPT-4o](gpt-4o.md), [GPT-4o-mini](gpt-4o-mini.md), [LLaMA-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [Llama-3.3-70B-Instruct](llama-3-3-70b-instruct.md), [o1-mini](o1-mini.md), [OpenBookQA](../datasets/openbookqa.md), [Qwen2.5-72B-Instruct](qwen2-5-72b-instruct.md), [StrategyQA](../datasets/strategyqa.md)

## Appears in

- [Evaluating Legal Reasoning Traces with Legal Issue Tree Rubrics](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-150/summary.md) — LEGIT is a 24K-instance Korean legal-judgment-prediction benchmark that converts real court judgments into hierarchical legal issue trees, using them as fine-grained rubrics (issue coverage and issue correctness, alongside final-order correctness) to evaluate LLM reasoning traces with human-lawyer-level reliability, and shows retrieval-augmented generation and RL-with-rubrics have complementary effects on legal reasoning quality.
- [ReTraceQA: Evaluating Reasoning Traces of Small Language Models in Commonsense Question Answering](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1798/summary.md) — ReTraceQA is a 2,421-instance expert-annotated benchmark showing that small language models (SLMs) reach the correct final answer via a flawed reasoning trace 14-24% of the time on commonsense QA, and that LLM-as-judge and PRM evaluators reliably detect overall trace correctness but struggle to localize the specific erroneous step, inflating answer-only accuracy scores by up to 25%.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
