# reranking

<!-- auto:begin -->

Reordering a shortlist of candidates with a second, more expensive model after a cheap retriever or generator has produced it. The skill-retrieval work measures both what it buys and what it costs: pairing a reranker over the top-20 candidates lifts Recall@1 from 45.16 to 57.90 in one configuration, larger than any gain from generating a rationale at query time, while adding 1.9 to 4.8 seconds per query against a 32-millisecond retriever. That paper's practical conclusion is the comparison rather than either number -- if extra online compute is available, spending it on reranking beats spending it on inference-time chain of thought, which yielded no consistent gain at one to two orders of magnitude in added latency. The evaluation-compute source supports the same direction from a different angle, finding evaluator accuracy improves monotonically with the reasoning tokens an evaluator is allowed to spend. Neither source treats reranking as a research object; between them they establish it as the archive's best-supported answer to where an inference budget should go when the first-stage output is a ranked list.

- **Kind**: method
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [annotation incompleteness](../concepts/annotation-incompleteness.md), [benchmark design](../concepts/benchmark-design.md), [best-of-n](best-of-n.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [Claude Haiku 4.5](../models/claude-haiku-4-5.md), [compute allocation](../concepts/compute-allocation.md), [DeepSeek-R1](../models/deepseek-r1.md), [dense retrieval](dense-retrieval.md), [gpt-5.6-luna](../models/gpt-5-6-luna.md), [GRPO](grpo.md), [judge reliability](../concepts/judge-reliability.md), [knowledge distillation](knowledge-distillation.md), [latent reasoning](../concepts/latent-reasoning.md), [LLM-as-a-judge](llm-as-a-judge.md), [meta-evaluation](../concepts/meta-evaluation.md), [privileged information](../concepts/privileged-information.md), [process evaluation](process-evaluation.md), [Qwen3-235B-A22B](../models/qwen3-235b-a22b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B](../models/qwen3-4b.md), [retrieval-augmented generation](retrieval-augmented-generation.md), [reward shaping](../concepts/reward-shaping.md), [supervised fine-tuning](supervised-fine-tuning.md), [test-time compute](../concepts/test-time-compute.md), [test-time scaling](../concepts/test-time-scaling.md), [verification](../concepts/verification.md)

## Appears in

- [SkillReason: Reasoning-Enhanced Agent Skill Retrieval for Implicit User Requests](../../archive/papers/2026/arxiv-2608-08640/summary.md) — Uses chain-of-thought about required capabilities as training-time supervision for a skill retriever -- distilled from a teacher in stage one and refined by retrieval-rewarded GRPO in stage two -- so that at inference the model encodes the bare query with no generation at all.
- [Scaling Evaluation-Time Compute with Reasoning Models as Evaluators](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2102/summary.md) — Shows evaluator accuracy improves monotonically with reasoning tokens spent, and that buying compute at evaluation time can substitute for buying it at generation time.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
