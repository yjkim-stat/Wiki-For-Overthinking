# hallucination

<!-- auto:begin -->

Producing content unsupported by the input or by fact, which the sources locate at three different points in a reasoning system. One treats it as an output failure to be refused: models emit bounding boxes for objects that are not present because training lacked negative samples. Another finds it inside the reasoning process itself, cataloguing hallucination and incompleteness among 10 error types in mathematical proofs where intermediate steps carry no correctness guarantee. A third motivates delegating deduction to a symbolic solver because purely model-based logical reasoning hallucinates. The archive also holds a step-level detector reading it from attention routing, and a 4B guardrail model that classifies claims as grounded or hallucinated.

- **Kind**: concept
- **Also called**: confabulation, reasoning hallucination, unsupported generation
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 4

**Related**: [abstention](abstention.md), [advantage estimation](advantage-estimation.md), [construct validity](construct-validity.md), [GPT-4o](../models/gpt-4o.md), [GRPO](../methods/grpo.md), [process evaluation](../methods/process-evaluation.md), [reasoning distillation](../methods/reasoning-distillation.md), [reinforcement learning post-training](../methods/reinforcement-learning-post-training.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [reward shaping](reward-shaping.md), [self-correction](self-correction.md), [self-training](self-training.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [synthetic data generation](../methods/synthetic-data-generation.md), [verification](verification.md)

## Appears in

- [Teaching MLLMs to Say No: Generalized Referring Expression Comprehension via Refusal Calibrated GRPO](../../archive/papers/2026/arxiv-2608-04698/summary.md) — A GRPO variant that teaches multimodal models to refuse when a referred object is absent, without losing localization accuracy on cases where it is present.
- [Mathematical Proof as a Litmus Test: Revealing Failure Modes of Advanced Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-582/summary.md) — Uses 200 mathematical proof problems as a diagnostic, finding some reasoning models solve under 20% and cataloguing 10 fine-grained error types that numerical benchmarks hide.
- [MAC-Reasoner: A Multi-Agent Collaborative Framework for Enhancing Logical Reasoning in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-233/summary.md) — Keeps the LLM as the reasoner while a symbolic solver supplies a Logic-Augmented Context, so conflicts flagged by execution direct attention to violated constraints instead of replacing deduction.
- [HalluGuard: Evidence-Grounded Small Reasoning Models to Mitigate Hallucinations in Retrieval-Augmented Generation](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-835/summary.md) — A 4B small reasoning model that classifies document-claim pairs as grounded or hallucinated for RAG pipelines and produces evidence-grounded justifications.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
