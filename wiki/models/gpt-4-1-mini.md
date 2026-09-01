# GPT-4.1-mini

<!-- auto:begin -->

GPT-4.1 Mini is used in these sources as one of the LLMs evaluated for test-time-compute allocation: the evolving-in-context-demonstration adaptive-allocation study evaluates it among four model configurations on math/coding/reasoning benchmarks, and LEGIT's cited note does not name GPT-4.1 Mini specifically (it is a Korean legal-reasoning-trace benchmark).

- **Kind**: model
- **Also called**: GPT-4.1 Mini
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [adaptive test-time compute allocation](../methods/adaptive-test-time-compute-allocation.md), [Gemini-2.0-Flash](gemini-2-0-flash.md), [Gemini 2.5 Flash](gemini-2-5-flash.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-4.1](gpt-4-1.md), [GPT-5-Nano](gpt-5-nano.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH500](../datasets/math500.md), [minervamath](../datasets/minervamath.md), [o3](o3.md)

## Appears in

- [Evaluating Legal Reasoning Traces with Legal Issue Tree Rubrics](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-150/summary.md) — LEGIT is a 24K-instance Korean legal-judgment-prediction benchmark that converts real court judgments into hierarchical legal issue trees, using them as fine-grained rubrics (issue coverage and issue correctness, alongside final-order correctness) to evaluate LLM reasoning traces with human-lawyer-level reliability, and shows retrieval-augmented generation and RL-with-rubrics have complementary effects on legal reasoning quality.
- [Adaptive Test-Time Compute Allocation with Evolving In-Context Demonstrations](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1754/summary.md) — A test-time-compute-allocation framework unifies where to spend compute (which unresolved queries get more sampling) with how generation is performed there (conditioning new samples on in-context demonstrations retrieved, via semantic similarity, from other queries already solved during the same inference run) -- consistently beating uniform Best-of-N and a difficulty-adaptive elimination baseline in coverage-per-token across four model families and multiple math/coding/reasoning benchmarks, with gains concentrated early in test-time scaling.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
