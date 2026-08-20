# Claude Haiku 4.5

<!-- auto:begin -->

The small model of the Claude 4.5 generation, appearing in this archive twice and in both cases as an instrument rather than a subject. In the skill-retrieval work it is one of two models that independently review each candidate benchmark query for naturalness, informativeness and consistency with its target, with disagreements adjudicated by hand. In the reasoning-trace extraction work it is one of the models whose encrypted reasoning blocks were shown interchangeable across sessions and models, and specifically the kind of less-safeguarded model that a more capable sibling's material can be routed through -- which is the structural point that paper makes, that safeguards on a capable model do not bind material processed by a weaker one in the same family. Neither source describes the model's training or capabilities.

- **Kind**: model
- **Also called**: Claude Haiku 4.5
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [annotation incompleteness](../concepts/annotation-incompleteness.md), [benchmark design](../concepts/benchmark-design.md), [best-of-n](../methods/best-of-n.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Claude Sonnet 4.5](claude-sonnet-4-5.md), [Claude Sonnet 4.6](claude-sonnet-4-6.md), [consensus](../concepts/consensus.md), [DeepSeek-R1](deepseek-r1.md), [dense retrieval](../methods/dense-retrieval.md), [Gemini-3.1-Pro](gemini-3-1-pro.md), [Gemini-3.5-Flash](gemini-3-5-flash.md), [GPT-5](gpt-5.md), [gpt-5.6-luna](gpt-5-6-luna.md), [GPT-5.6-Sol](gpt-5-6-sol.md), [GPT-5.6 Terra](gpt-5-6-terra.md), [GPT-5-mini](gpt-5-mini.md), [GRPO](../methods/grpo.md), [hard negative mining](../methods/hard-negative-mining.md), [Humanity's Last Exam](../datasets/humanity-s-last-exam.md), [jury aggregation](../methods/jury-aggregation.md), [knowledge distillation](../methods/knowledge-distillation.md), [latent reasoning](../concepts/latent-reasoning.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [monitorability](../concepts/monitorability.md), [multi-agent pipeline](../concepts/multi-agent-pipeline.md), [o4-mini](o4-mini.md), [persistent semantic entity](../concepts/persistent-semantic-entity.md), [persona conditioning](../methods/persona-conditioning.md), [privileged information](../concepts/privileged-information.md), [prompt injection](../concepts/prompt-injection.md), [Qwen3-235B-A22B](qwen3-235b-a22b.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-4B](qwen3-4b.md), [reranking](../methods/reranking.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [reward shaping](../concepts/reward-shaping.md), [self-consistency](../methods/self-consistency.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time scaling](../concepts/test-time-scaling.md)

## Appears in

- [SkillReason: Reasoning-Enhanced Agent Skill Retrieval for Implicit User Requests](../../archive/papers/2026/arxiv-2608-08640/summary.md) — Uses chain-of-thought about required capabilities as training-time supervision for a skill retriever -- distilled from a teacher in stage one and refined by retrieval-rewarded GRPO in stage two -- so that at inference the model encodes the bare query with no generation at all.
- [Stealing Reasoning Traces from Proprietary LLM APIs](../../archive/papers/2026/arxiv-2608-09867/summary.md) — Shows that the encrypted reasoning blocks major providers return to clients are interchangeable across sessions, users and models within a provider, and measures four consequences of that interchangeability -- distillation, third-party secret extraction, hazardous-content exposure and monitor-invisible prompt injection -- before responsible disclosure closed it.
- [Social Chain of Thought: A Multi-Agent Architecture Grounded in Medical Differential Diagnosis Methodology](../../archive/papers/2026/arxiv-2608-11420/summary.md) — Structures multi-agent medical differential diagnosis as rounds of persona-conditioned specialist deliberation, and shows the recall advantage is not reproduced by best-of-n sampling from the same model, concentrates entirely in the cases where monolithic inference fails, and reverses on the easiest quartile.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
