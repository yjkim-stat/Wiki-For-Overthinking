# synthetic data generation

<!-- auto:begin -->

Producing training data with a model instead of collecting or annotating it, used by all three sources to obtain supervision that does not otherwise exist. One generates therapy dialogues with a structured CoT strategy plus a resistance orchestrator, specifically to avoid the uniformly compliant patients that make naive synthesis unrealistic. One generates instruction-following data for reasoning traces, raising one model's compliance score from 0.11 to 0.27. One derives a domain-agnostic dataset from a web corpus and synthesizes paired grounded and hallucinated claims, which is what makes its guardrail domain-agnostic. All three synthesize the negative or difficult case specifically, since that is the part real data lacks.

- **Kind**: method
- **Also called**: data synthesis, synthetic corpora
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [activation steering](activation-steering.md), [alignment](../concepts/alignment.md), [chain of thought](chain-of-thought.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [compositional generalization](../concepts/compositional-generalization.md), [controllability](../concepts/controllability.md), [curriculum learning](../concepts/curriculum-learning.md), [DeepSeek-R1](../models/deepseek-r1.md), [Gemma-3-4B](../models/gemma-3-4b.md), [GPT-4o](../models/gpt-4o.md), [GPT-OSS](../models/gpt-oss.md), [gpt-oss-20b](../models/gpt-oss-20b.md), [hallucination](../concepts/hallucination.md), [instruction following](../concepts/instruction-following.md), [LLM-as-a-judge](llm-as-a-judge.md), [MathVista](../datasets/mathvista.md), [monitorability](../concepts/monitorability.md), [multi-turn reasoning](multi-turn-reasoning.md), [multimodal reasoning](../concepts/multimodal-reasoning.md), [process supervision](../concepts/process-supervision.md), [Qwen2.5-VL-3B](../models/qwen2-5-vl-3b.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [reasoning distillation](reasoning-distillation.md), [reinforcement learning](reinforcement-learning.md), [retrieval-augmented generation](retrieval-augmented-generation.md), [reward hacking](../concepts/reward-hacking.md), [supervised fine-tuning](supervised-fine-tuning.md), [sycophancy](../concepts/sycophancy.md), [verification](../concepts/verification.md), [visual grounding](../concepts/visual-grounding.md)

## Appears in

- [CURV: Enhancing Chart Understanding Through Curriculum Visual Grounded Reasoning](../../archive/papers/2026/arxiv-2608-02833/summary.md) — Reformulates chart question answering as a chain in which every reasoning step carries a predicted image region, trains that pairing through a curriculum graded by nesting depth, and finds explicit intermediate grounding worth 8.78 points over letting the model attend implicitly.
- [ODRA: Synthesizing Cognitive Behavioral Therapy Sessions with Structured Chain-Of-Thought and Dynamic Patient Resistance](../../archive/papers/2026/arxiv-2608-04524/summary.md) — Synthesizes Cognitive Behavioral Therapy dialogues using a CoT strategy grounded in CBT guidelines plus a resistance orchestrator that steers simulated patients away from sycophantic compliance.
- [ReasonIF: Large Reasoning Models Fail to Follow Instructions During Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1456/summary.md) — Benchmarks whether reasoning models follow instructions inside their reasoning traces, finding under 25% compliance at best and worse as difficulty rises.
- [HalluGuard: Evidence-Grounded Small Reasoning Models to Mitigate Hallucinations in Retrieval-Augmented Generation](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-835/summary.md) — A 4B small reasoning model that classifies document-claim pairs as grounded or hallucinated for RAG pipelines and produces evidence-grounded justifications.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
