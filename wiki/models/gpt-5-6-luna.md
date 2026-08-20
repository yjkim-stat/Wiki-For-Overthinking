# gpt-5.6-luna

<!-- auto:begin -->

A GPT-5.6 variant that appears in this archive twice, in both cases as an instrument rather than as a subject. In the SkillReason work it is one of two judges performing an independent 300-sample quality audit of a benchmark, passing 97.7 percent of samples against the other judge's 99.3 percent, with 98.3 percent inter-judge agreement -- and the archive's reading of that paper flags the wider pattern that the benchmark is model-mediated at nearly every step, of which this audit is part. It is separately one of the models whose branch preferences are measured in the BODHI study of how RLVR reshapes a model's choice between semantically distinct reasoning continuations. Nothing in either source describes the model itself.

- **Kind**: model
- **Also called**: GPT-5.6-Luna, GPT-5.6-luna
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [AIME](../datasets/aime.md), [annotation incompleteness](../concepts/annotation-incompleteness.md), [backtracking](../concepts/backtracking.md), [benchmark design](../concepts/benchmark-design.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Claude Haiku 4.5](claude-haiku-4-5.md), [Claude Sonnet 4.5](claude-sonnet-4-5.md), [Claude Sonnet 4.6](claude-sonnet-4-6.md), [DAPO](../methods/dapo.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DAPO-Qwen-32B](dapo-qwen-32b.md), [DeepSeek-R1](deepseek-r1.md), [dense retrieval](../methods/dense-retrieval.md), [entropy collapse](../concepts/entropy-collapse.md), [exploration](../concepts/exploration.md), [Gemini-3.1-Pro](gemini-3-1-pro.md), [Gemini-3.5-Flash](gemini-3-5-flash.md), [GPT-5](gpt-5.md), [GPT-5.6-Sol](gpt-5-6-sol.md), [GPT-5.6 Terra](gpt-5-6-terra.md), [GPT-5-mini](gpt-5-mini.md), [gpt-oss-120b](gpt-oss-120b.md), [GRPO](../methods/grpo.md), [Humanity's Last Exam](../datasets/humanity-s-last-exam.md), [knowledge distillation](../methods/knowledge-distillation.md), [latent reasoning](../concepts/latent-reasoning.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [long chain-of-thought distillation](../methods/long-chain-of-thought-distillation.md), [monitorability](../concepts/monitorability.md), [o4-mini](o4-mini.md), [pass@k](../concepts/pass-k.md), [persistent semantic entity](../concepts/persistent-semantic-entity.md), [policy entropy](../concepts/policy-entropy.md), [privileged information](../concepts/privileged-information.md), [prompt injection](../concepts/prompt-injection.md), [Qwen3-235B-A22B](qwen3-235b-a22b.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-4B](qwen3-4b.md), [Qwen3-8B-Base](qwen3-8b-base.md), [reasoning boundary](../concepts/reasoning-boundary.md), [reranking](../methods/reranking.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [reward shaping](../concepts/reward-shaping.md), [RLVR](../methods/rlvr.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [trajectory diversity](../concepts/trajectory-diversity.md)

## Appears in

- [BODHI: Do LLMs Branch Out and Discover Heterogeneous Inferences?](../../archive/papers/2026/arxiv-2608-02867/summary.md) — Builds prefix trees of semantically equivalent reasoning statements and measures how RLVR changes a model's preference between branches, finding the entropy collapse is not stylistic — the collapse is stronger for semantically distinct continuations than for syntactic variants of the same statement.
- [SkillReason: Reasoning-Enhanced Agent Skill Retrieval for Implicit User Requests](../../archive/papers/2026/arxiv-2608-08640/summary.md) — Uses chain-of-thought about required capabilities as training-time supervision for a skill retriever -- distilled from a teacher in stage one and refined by retrieval-rewarded GRPO in stage two -- so that at inference the model encodes the bare query with no generation at all.
- [Stealing Reasoning Traces from Proprietary LLM APIs](../../archive/papers/2026/arxiv-2608-09867/summary.md) — Shows that the encrypted reasoning blocks major providers return to clients are interchangeable across sessions, users and models within a provider, and measures four consequences of that interchangeability -- distillation, third-party secret extraction, hazardous-content exposure and monitor-invisible prompt injection -- before responsible disclosure closed it.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
