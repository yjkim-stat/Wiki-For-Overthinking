# Qwen3-1.7B-Base

<!-- auto:begin -->

A small base checkpoint, used by both sources as the lower end of a two-scale comparison and, in both, the scale at which method differences nearly vanish. One reports that most alternative reinforcement-learning objectives yield marginal or no gains over GRPO here and attributes it to limited reasoning capacity leaving little room for objective design — its own margin is 0.8 points against 2.6 at 4B. The other uses it among the base models where suppressing epistemic verbalization cuts AIME24 pass@1 from 16.7 to 3.3. Its function in the archive is as evidence about where a result comes from: a method that only separates at the larger scale is telling you something about capacity rather than about the method.

- **Kind**: model
- **Also called**: Qwen3-1.7B, Qwen3-1.7b-Base
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [aha moment](../concepts/aha-moment.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AMC23](../datasets/amc23.md), [DeepSeek-R1-Distill-Qwen-32B](deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [epistemic verbalization](../concepts/epistemic-verbalization.md), [exploration](../concepts/exploration.md), [GRPO](../methods/grpo.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH](../datasets/math.md), [MATH-500](../datasets/math-500.md), [MATH500](../datasets/math500.md), [PPO](../methods/ppo.md), [Qwen2.5-32B-Instruct](qwen2-5-32b-instruct.md), [Qwen2.5-7B](qwen2-5-7b.md), [Qwen2.5-Math-7B](qwen2-5-math-7b.md), [Qwen3-14B](qwen3-14b.md), [Qwen3-4B-Base](qwen3-4b-base.md), [Qwen3-8B](qwen3-8b.md), [reasoning boundary](../concepts/reasoning-boundary.md), [REINFORCE](../methods/reinforce.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md)

## Appears in

- [Beyond the Mean: Multi-Moment Policy Optimization for LLM Reasoning](../../archive/papers/2026/arxiv-2608-02149/summary.md) — Treats a policy's per-problem failure probability as a random variable over the problem distribution and shows that REINFORCE, pass@K training and MaxRL each optimize a single moment of it, then proposes minimizing the first T moments jointly — which is exactly minimizing the expected truncated number of rollouts needed to reach a first success.
- [Understanding Reasoning in LLMs through Strategic Information Allocation under Uncertainty](../../archive/papers/2026/local-99019f66bdc27581/summary.md) — Separates reasoning into procedural advancement and 'epistemic verbalization' — the token-level externalization of uncertainty — and shows that emitting doubt is what lets a model recover from silent divergence, that injecting a bare doubt cue recovers failed trajectories, and that 800 SFT examples suffice to install or destroy the habit.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
