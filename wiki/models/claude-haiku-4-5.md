# Claude Haiku 4.5

<!-- auto:begin -->

A small frontier model appearing across 3 sources as a reviewer, a participant and an extraction target. Its notable role is in benchmark construction, where it independently reviews each query for naturalness, informativeness, capability requirement and target consistency alongside another frontier model, with disagreements adjudicated by hand -- one of the archive's cases where a benchmark's definition of a property is what two models judged it to be. It also appears in multi-agent medical deliberation and as a target for reasoning-trace extraction.

- **Kind**: model
- **Also called**: Claude Haiku 4.5
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [annotation incompleteness](../concepts/annotation-incompleteness.md), [benchmark design](../concepts/benchmark-design.md), [best-of-n](../methods/best-of-n.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Claude Sonnet 4.5](claude-sonnet-4-5.md), [Claude Sonnet 4.6](claude-sonnet-4-6.md), [consensus](../concepts/consensus.md), [DeepSeek-R1](deepseek-r1.md), [dense retrieval](../methods/dense-retrieval.md), [difficulty conditioning](../concepts/difficulty-conditioning.md), [Gemini-3.1-Pro](gemini-3-1-pro.md), [Gemini-3.5-Flash](gemini-3-5-flash.md), [GPT-5](gpt-5.md), [gpt-5.6-luna](gpt-5-6-luna.md), [GPT-5.6-Sol](gpt-5-6-sol.md), [GPT-5.6 Terra](gpt-5-6-terra.md), [GPT-5-mini](gpt-5-mini.md), [GRPO](../methods/grpo.md), [hard negative mining](../methods/hard-negative-mining.md), [Humanity's Last Exam](../datasets/humanity-s-last-exam.md), [jury aggregation](../methods/jury-aggregation.md), [knowledge distillation](../methods/knowledge-distillation.md), [latent reasoning](../concepts/latent-reasoning.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [monitorability](../concepts/monitorability.md), [multi-agent pipeline](../concepts/multi-agent-pipeline.md), [o4-mini](o4-mini.md), [persistent semantic entity](../concepts/persistent-semantic-entity.md), [persona conditioning](../methods/persona-conditioning.md), [privileged information](../concepts/privileged-information.md), [prompt injection](../concepts/prompt-injection.md), [Qwen3-235B-A22B](qwen3-235b-a22b.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-4B](qwen3-4b.md), [reranking](../methods/reranking.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [reward shaping](../methods/reward-shaping.md), [self-consistency](../methods/self-consistency.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time scaling](../concepts/test-time-scaling.md)

## Appears in

- [SkillReason: Reasoning-Enhanced Agent Skill Retrieval for Implicit User Requests](../../archive/papers/2026/arxiv-2608-08640/summary.md) — Uses chain-of-thought about required capabilities as training-time supervision for a skill retriever -- distilled from a teacher in stage one and refined by retrieval-rewarded GRPO in stage two -- so that at inference the model encodes the bare query with no generation at all.
- [Stealing Reasoning Traces from Proprietary LLM APIs](../../archive/papers/2026/arxiv-2608-09867/summary.md) — Shows that the encrypted reasoning blocks major providers return to clients are interchangeable across sessions, users and models within a provider, and measures four consequences of that interchangeability -- distillation, third-party secret extraction, hazardous-content exposure and monitor-invisible prompt injection -- before responsible disclosure closed it.
- [Social Chain of Thought: A Multi-Agent Architecture Grounded in Medical Differential Diagnosis Methodology](../../archive/papers/2026/arxiv-2608-11420/summary.md) — Structures multi-agent medical differential diagnosis as rounds of persona-conditioned specialist deliberation, and shows the recall advantage is not reproduced by best-of-n sampling from the same model, concentrates entirely in the cases where monolithic inference fails, and reverses on the easiest quartile.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
