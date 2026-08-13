# reward sparsity

<!-- auto:begin -->

Having too few informative reward signals for the policy gradient to say much, and in both sources the named cause of a specific failure rather than a general complaint. One locates it along a trajectory: a multi-step search agent receives one scalar for ten retrievals, so the query that found the decisive document and the one that repeated an earlier query inherit the same credit, and it reports that removing the terminal reward while keeping dense per-step signals is nonetheless its largest single loss. The other locates it across a group: when all eight sampled responses to a problem are wrong they share a reward, the group-relative advantage is zero, and the update carries no gradient at all — which it addresses by distilling extracted experience into the policy first, cutting the all-incorrect rate by 4.95 points before reinforcement learning begins. The two readings are complementary: sparsity is about how much of the reward varies, and it can fail to vary either within a trajectory or within a group.

- **Kind**: concept
- **Also called**: sparse reward, sparse supervision
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [advantage estimation](advantage-estimation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [Bamboogle](../datasets/bamboogle.md), [Brumo](../datasets/brumo.md), [credit assignment](credit-assignment.md), [DAPO](../methods/dapo.md), [DAPO-Math-17k](../datasets/dapo-math-17k.md), [data efficiency](data-efficiency.md), [expected calibration error](expected-calibration-error.md), [exploration](exploration.md), [GiGPO](../methods/gigpo.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [HotpotQA](../datasets/hotpotqa.md), [MATH-500](../datasets/math-500.md), [multi-hop reasoning](multi-hop-reasoning.md), [MuSiQue](../datasets/musique.md), [Natural Questions](../datasets/natural-questions.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [outcome reward](outcome-reward.md), [policy entropy](policy-entropy.md), [PopQA](../datasets/popqa.md), [post-hoc rationalization](post-hoc-rationalization.md), [PPO](../methods/ppo.md), [privileged information](privileged-information.md), [process reward](process-reward.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [reasoning boundary](reasoning-boundary.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [search-augmented reasoning](search-augmented-reasoning.md), [Search-R1](../methods/search-r1.md), [TriviaQA](../datasets/triviaqa.md)

## Appears in

- [BiCAA: Bidirectional Credit Assignment for Search-Augmented Agent](../../archive/papers/2026/arxiv-2608-01321/summary.md) — Gives each retrieval step of a search agent a dense reward built from two ground-truth-conditioned signals — how much the step raised the model's likelihood of the correct answer, and how necessary the step looks in hindsight — and fuses them asymmetrically so that a step which helps locally but is redundant globally is discounted.
- [Self-Improving Large Language Models via Progressive Experience Evolution](../../archive/papers/2026/arxiv-2608-02139/summary.md) — Inserts a stage before RL in which the model extracts textual lessons from its own successful and failed rollouts, filters them by measured marginal utility on a held-out probe set, and distills the surviving pool into its own weights — so that GRPO starts from a policy that fails all-eight-samples less often.
- [Start Classifying: Categorical Critics for LLM Reinforcement Learning](../../archive/papers/2026/arxiv-2608-02181/summary.md) — Replaces PPO's scalar mean-squared-error critic head with a categorical predictor over a discretized value support trained by cross-entropy against Gaussian-smoothed targets, decodes it back to a scalar for an unchanged GAE update, and shows the resulting critic is better calibrated and produces near-symmetric advantages where the MSE critic penalizes failures two-to-three times harder than it rewards successes.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
