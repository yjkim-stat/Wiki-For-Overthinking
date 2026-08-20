# hard negative mining

<!-- auto:begin -->

Constructing training examples that are wrong in ways close to right, so a model must learn the distinction rather than a coarse separation. Both sources build them deliberately rather than sampling them. The multimodal process-reward work has a strong model perturb correct trajectories at a single step, producing localised negatives that differ from a valid derivation in one place, and its ablation attributes 1.4 average points to that supervision -- distinguishing the contribution of localised hard negatives from that of recycled rollouts, which are worth a separate 0.9. The skill-retrieval work mines confusable candidates from the corpus by document overlap and dense retrieval, then uses a strong model to keep only queries whose annotated target remains clearly distinguishable from them, so the negatives are hard by construction and the benchmark stays answerable. The shared point is that a negative's usefulness is a property of its distance from the positive, and both sources engineer that distance rather than trusting random sampling to supply it.

- **Kind**: method
- **Also called**: hard negatives
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [annotation incompleteness](../concepts/annotation-incompleteness.md), [benchmark design](../concepts/benchmark-design.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [Claude Haiku 4.5](../models/claude-haiku-4-5.md), [component ablation](component-ablation.md), [credit assignment](../concepts/credit-assignment.md), [DeepSeek-R1](../models/deepseek-r1.md), [dense retrieval](dense-retrieval.md), [gpt-5.6-luna](../models/gpt-5-6-luna.md), [GRPO](grpo.md), [knowledge distillation](knowledge-distillation.md), [latent reasoning](../concepts/latent-reasoning.md), [LLM-as-a-judge](llm-as-a-judge.md), [MathVista](../datasets/mathvista.md), [MMMU](../datasets/mmmu.md), [MMMU-Pro](../datasets/mmmu-pro.md), [outcome reward](../concepts/outcome-reward.md), [privileged information](../concepts/privileged-information.md), [process reward](../concepts/process-reward.md), [process reward model](process-reward-model.md), [Qwen3-235B-A22B](../models/qwen3-235b-a22b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-VL-2B](../models/qwen3-vl-2b.md), [Qwen3-VL-8B](../models/qwen3-vl-8b.md), [reranking](reranking.md), [retrieval-augmented generation](retrieval-augmented-generation.md), [reward shaping](reward-shaping.md), [RLVR](rlvr.md), [self-correction](../concepts/self-correction.md), [supervised fine-tuning](supervised-fine-tuning.md)

## Appears in

- [StructReward: Efficient Structured Process Rewards for Self-Correcting Multimodal Reasoning](../../archive/papers/2026/arxiv-2608-08326/summary.md) — Builds a dense process reward without a learned verifier or an online judge, by aligning generated reasoning steps to the process-labelled reference steps that existing datasets already contain using numerical, symbolic and lexical matching rules, gated so a partial reference match cannot override a wrong final answer.
- [SkillReason: Reasoning-Enhanced Agent Skill Retrieval for Implicit User Requests](../../archive/papers/2026/arxiv-2608-08640/summary.md) — Uses chain-of-thought about required capabilities as training-time supervision for a skill retriever -- distilled from a teacher in stage one and refined by retrieval-rewarded GRPO in stage two -- so that at inference the model encodes the bare query with no generation at all.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
