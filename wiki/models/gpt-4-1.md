# GPT-4.1

<!-- auto:begin -->

GPT-4.1 is used as an evaluated/backbone model in LEGIT (a Korean legal-judgment-prediction benchmark using hierarchical legal issue trees as rubrics) and in Budget-Aware Anytime Reasoning with LLM-Synthesized Preference Data, where it is one of the general-purpose models tested with the Anytime Index and Preference Data Prompting (PDP).

- **Kind**: model
- **Also called**: GPT-4.1
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [Chain-of-Thought (CoT)](../methods/chain-of-thought-cot.md), [Gemini-2.0-Flash](gemini-2-0-flash.md), [Gemini 2.5 Flash](gemini-2-5-flash.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-4.1-mini](gpt-4-1-mini.md), [GPT-4o](gpt-4o.md), [GPT-5](gpt-5.md), [gpt-oss-120b](gpt-oss-120b.md), [GPT-OSS-20B](gpt-oss-20b.md), [Grok-3](grok-3.md), [Llama 3.3 70B](llama-3-3-70b.md), [o1](o1.md), [o3](o3.md)

## Appears in

- [Evaluating Legal Reasoning Traces with Legal Issue Tree Rubrics](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-150/summary.md) — LEGIT is a 24K-instance Korean legal-judgment-prediction benchmark that converts real court judgments into hierarchical legal issue trees, using them as fine-grained rubrics (issue coverage and issue correctness, alongside final-order correctness) to evaluate LLM reasoning traces with human-lawyer-level reliability, and shows retrieval-augmented generation and RL-with-rubrics have complementary effects on legal reasoning quality.
- [Budget-Aware Anytime Reasoning with LLM-Synthesized Preference Data](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-417/summary.md) — Introduces the Anytime Index, an AUC-style metric quantifying how solution quality improves as reasoning-token budget increases, and Preference Data Prompting (PDP), an inference-time self-improvement method using self-generated contrastive reasoning pairs at fixed token budgets, giving consistent gains across seven LLM families on trip planning, math, and scientific QA.
- [Understanding LLM Reasoning for Abstractive Summarization](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-859/summary.md) — The first large-scale, systematic evaluation of 8 reasoning prompting strategies (across augmentation, organization, reflection paradigms) and 3 Large Reasoning Models on abstractive summarization across 8 datasets finds reasoning is not a panacea for this task -- there is a statistically significant quality-faithfulness trade-off, and increasing an LRM's internal reasoning budget does not reliably improve, and can actively reduce, factual consistency.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
