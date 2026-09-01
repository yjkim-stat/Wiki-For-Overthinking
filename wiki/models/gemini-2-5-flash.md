# Gemini 2.5 Flash

<!-- auto:begin -->

Gemini 2.5 Flash is cited in this archive as the prediction target for a lightweight (~1B-parameter) multimodal model that estimates LLM reasoning performance bins before an API call to guide compute-optimal reasoning-budget selection, and appears in the construction pipeline of LEGIT, a legal-reasoning-trace benchmark, as one of the LLMs used to extract facts and issue structure from court judgments.

- **Kind**: model
- **Also called**: Gemini-2.5-Flash
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 5

**Related**: [AdvBench](../datasets/advbench.md), [Chain-of-Thought (CoT)](../methods/chain-of-thought-cot.md), [Claude-3.7-Sonnet](claude-3-7-sonnet.md), [Compute-optimal inference](../concepts/compute-optimal-inference.md), [DeepSeek-R1](deepseek-r1.md), [Gemini-2.0-Flash](gemini-2-0-flash.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [Gemini 3 Flash Preview](gemini-3-flash-preview.md), [GPT-4.1](gpt-4-1.md), [GPT-4.1-mini](gpt-4-1-mini.md), [GPT-5](gpt-5.md), [gpt-o3](gpt-o3.md), [HarmBench](../datasets/harmbench.md), [Llama 3.3 70B](llama-3-3-70b.md), [Nemotron-32B](nemotron-32b.md), [o1](o1.md), [o3](o3.md), [Qwen3-0.6B](qwen3-0-6b.md), [Qwen3-8B](qwen3-8b.md), [StrongReject](../datasets/strongreject.md)

## Appears in

- [Can a Lightweight Multimodal Model Estimate LLM Reasoning Performance? A Study for Compute-Optimal Document Inference](../../archive/papers/2026/arxiv-2608-18591/summary.md) — Trains a ~1B-parameter multimodal model to predict, before any API call, which of seven performance bins a frontier LLM will land in for a given (document, prompt, model, reasoning budget) tuple, and uses those predictions to pick a per-sample reasoning budget for document tasks.
- [Evaluating Legal Reasoning Traces with Legal Issue Tree Rubrics](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-150/summary.md) — LEGIT is a 24K-instance Korean legal-judgment-prediction benchmark that converts real court judgments into hierarchical legal issue trees, using them as fine-grained rubrics (issue coverage and issue correctness, alongside final-order correctness) to evaluate LLM reasoning traces with human-lawyer-level reliability, and shows retrieval-augmented generation and RL-with-rubrics have complementary effects on legal reasoning quality.
- [AutoRAN: Automated Hijacking of Safety Reasoning in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1988/summary.md) — AutoRAN is the first automated framework for hijacking a large reasoning model's internal safety deliberation, using a weaker, less-aligned auxiliary model to simulate the target's execution reasoning and iteratively refine attack prompts from leaked refusal reasoning, achieving near-100% attack success against gpt-o3/o4-mini and Gemini-2.5-Flash within a few turns.
- [Beyond Memorization: Extending Reasoning Depth with Recurrence, Memory and Test-Time Compute Scaling](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2103/summary.md) — Using a controlled 1D-cellular-automata benchmark with disjoint train/test rule sets (precluding memorization), this paper shows models can genuinely infer unseen local rules but fixed-depth architectures collapse sharply beyond one-step-ahead prediction, that most frontier LLMs (except Gemini-2.5-Pro) fail even the simplest natural-language proxy of this task, and that depth -- not width -- is what drives multi-step accuracy, with chain-of-thought-style token-level supervision reaching near-perfect accuracy up to 4 look-ahead steps while RL (GRPO) without intermediate supervision reaches only 3 steps and architectural depth-extension tricks (ACT, recurrent memory) each add only about one effective step.
- [Understanding LLM Reasoning for Abstractive Summarization](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-859/summary.md) — The first large-scale, systematic evaluation of 8 reasoning prompting strategies (across augmentation, organization, reflection paradigms) and 3 Large Reasoning Models on abstractive summarization across 8 datasets finds reasoning is not a panacea for this task -- there is a statistically significant quality-faithfulness trade-off, and increasing an LRM's internal reasoning budget does not reliably improve, and can actively reduce, factual consistency.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
