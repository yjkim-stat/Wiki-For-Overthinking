# hallucination

<!-- auto:begin -->

Producing content unsupported by the input or by fact, which the sources locate at three different points in a reasoning system. One treats it as an output failure to be refused: models emit bounding boxes for objects that are not present because training lacked negative samples. Another finds it inside the reasoning process itself, cataloguing hallucination and incompleteness among 10 error types in mathematical proofs where intermediate steps carry no correctness guarantee. A third motivates delegating deduction to a symbolic solver because purely model-based logical reasoning hallucinates. The archive also holds a step-level detector reading it from attention routing, and a 4B guardrail model that classifies claims as grounded or hallucinated.

- **Kind**: concept
- **Also called**: confabulation, reasoning hallucination, unsupported generation
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 5

**Related**: [abstention](abstention.md), [activation patching](../methods/activation-patching.md), [advantage estimation](advantage-estimation.md), [calibration](../methods/calibration.md), [construct validity](construct-validity.md), [detection versus control](detection-versus-control.md), [GPT-4o](../models/gpt-4o.md), [GRPO](../methods/grpo.md), [linear probe](../methods/linear-probe.md), [linear separability](linear-separability.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [predictive entropy](predictive-entropy.md), [process evaluation](../methods/process-evaluation.md), [Qwen3-4B](../models/qwen3-4b.md), [ReAct](../methods/react.md), [reasoning distillation](../methods/reasoning-distillation.md), [reinforcement learning post-training](../methods/reinforcement-learning-post-training.md), [residual stream](residual-stream.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [reward shaping](reward-shaping.md), [self-correction](self-correction.md), [self-training](self-training.md), [semantic entropy](../methods/semantic-entropy.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [synthetic data generation](../methods/synthetic-data-generation.md), [uncertainty quantification](uncertainty-quantification.md), [verification](verification.md)

## Appears in

- [Teaching MLLMs to Say No: Generalized Referring Expression Comprehension via Refusal Calibrated GRPO](../../archive/papers/2026/arxiv-2608-04698/summary.md) — A GRPO variant that teaches multimodal models to refuse when a referred object is absent, without losing localization accuracy on cases where it is present.
- [Actionable Hallucination Detection: Translating Latent Uncertainty into Agentic Critique](../../archive/papers/2026/arxiv-2608-10430/summary.md) — Detects the class of hallucination where a model confidently fabricates a parameter the user never gave, by running a LoRA adapter alongside the frozen model that restructures the residual stream and then names the offending parameter in words the agent can act on.
- [Mathematical Proof as a Litmus Test: Revealing Failure Modes of Advanced Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-582/summary.md) — Uses 200 mathematical proof problems as a diagnostic, finding some reasoning models solve under 20% and cataloguing 10 fine-grained error types that numerical benchmarks hide.
- [MAC-Reasoner: A Multi-Agent Collaborative Framework for Enhancing Logical Reasoning in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-233/summary.md) — Keeps the LLM as the reasoner while a symbolic solver supplies a Logic-Augmented Context, so conflicts flagged by execution direct attention to violated constraints instead of replacing deduction.
- [HalluGuard: Evidence-Grounded Small Reasoning Models to Mitigate Hallucinations in Retrieval-Augmented Generation](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-835/summary.md) — A 4B small reasoning model that classifies document-claim pairs as grounded or hallucinated for RAG pipelines and produces evidence-grounded justifications.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
