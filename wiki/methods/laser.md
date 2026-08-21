# Laser

<!-- auto:begin -->

In this archive LASER is a named efficient-reasoning method that appears only as a comparison point, never as a subject: no archived source describes how it works beyond its category. The survey of efficient R1-style reasoning models files it under single-model Adaptive Reasoning as one of the length-reward-shaped methods, alongside HAPO, ALP and SelfBudgeter. ARLCP uses it as one of seven efficient-reasoning baselines on distilled DeepSeek-R1-Qwen models, where it is the strongest baseline on GSM8K at 1.5B (82.26% against ARLCP's 87.34%) and the one method that beats ARLCP outright on AMC2023 at 1.5B (75.94% against 73.28%). Treat the entry as a pointer to the length-reward family rather than as a description of the method.

- **Kind**: method
- **Also called**: LASER, Laser
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [A*-Thought](a-thought.md), [Accuracy-Length Tradeoff](../concepts/accuracy-length-tradeoff.md), [Ada-R1](ada-r1.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [AdaptThink](adaptthink.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [DEER](deer.md), [DPO_Shortest](dpo-shortest.md), [DRP](drp.md), [Early Exit](early-exit.md), [Efficient Reasoning](../concepts/efficient-reasoning.md), [GPQA](../datasets/gpqa.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [LC-R1](lc-r1.md), [Length Penalty](../concepts/length-penalty.md), [Length reward](../concepts/length-reward.md), [Manifold Steering](manifold-steering.md), [MATH500](../datasets/math500.md), [NoThinking](nothinking.md), [NOWAIT](nowait.md), [O1-Pruner](o1-pruner.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [PLAN-AND-BUDGET](plan-and-budget.md), [S-GRPO](s-grpo.md), [SEAL](seal.md), [SelfBudgeter](selfbudgeter.md), [SFT_Shortest](sft-shortest.md), [SPIRIT](spirit.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [Thinkless](thinkless.md), [ThinkPrune](thinkprune.md), [TokenSkip](tokenskip.md), [VeriThinker](verithinker.md), [veRL](verl.md)

## Appears in

- [QLPO: Quadrant-weighted Sampling for Length-aware Policy Optimization](../../archive/papers/2026/arxiv-2607-21793/summary.md) — QLPO is a GRPO variant that leaves the reward, advantage estimator and update untouched and instead over-generates K=16 rollouts per prompt and resamples the M=8 training group to favour short-correct and long-incorrect trajectories, which shortens outputs by 30-70% relative to GRPO at roughly unchanged accuracy.
- [Don't Overthink It: A Survey of Efficient R1-style Large Reasoning Models](../../archive/papers/2025/local-6c80b6fd388d671e/summary.md) — A survey that organizes methods for making R1-style large reasoning models reason efficiently (i.e., avoid overthinking) into two axes: single-model optimization and multi-model collaboration.
- [Stop Unnecessary Reflection: Training LRMs for Efficient Reasoning with Adaptive Reflection and Length Coordinated Penalty](../../archive/papers/2026/title-833de99e9b3ea69d/summary.md) — ARLCP is a reinforcement-learning fine-tuning recipe that adds two coupled reward penalties -- one on reflective steps, one on response length scaled by estimated problem complexity -- to shorten chains of thought in distilled reasoning models without losing accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
