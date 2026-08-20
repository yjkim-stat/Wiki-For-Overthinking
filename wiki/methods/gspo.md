# GSPO

<!-- auto:begin -->

A group-relative variant that computes the importance ratio at the sequence level rather than the token level, intended to reduce variance. Across 3 sources it is a comparator rather than a subject. Two results place it: on subjective judgement tasks it produces the same backbone-dependent split as the other two algorithms tested, with one model improving on every task and another falling below its own reasoning baseline on three of four; and in a forecasting study standard group-relative training given a bounded reward mapping beats it and three other optimisation-level variants each given the naive unbounded reward, which that source reads as showing reward-level and optimisation-level fixes are not interchangeable.

- **Kind**: method
- **Also called**: Group Sequence Policy Optimization
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [advantage function](../concepts/advantage-function.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [clip-higher](clip-higher.md), [credit assignment](../concepts/credit-assignment.md), [DAPO](dapo.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DeepSeek-V3.2](../models/deepseek-v3-2.md), [Dr. GRPO](dr-grpo.md), [entropy collapse](../concepts/entropy-collapse.md), [entropy regularization](entropy-regularization.md), [ETTh1](../datasets/etth1.md), [ETTh2](../datasets/etth2.md), [ETTm1](../datasets/ettm1.md), [ETTm2](../datasets/ettm2.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [GPT-5.5](../models/gpt-5-5.md), [GRPO](grpo.md), [length control](../concepts/length-control.md), [length penalty](length-penalty.md), [LLM-as-a-judge](llm-as-a-judge.md), [majority voting](majority-voting.md), [out-of-distribution generalization](../concepts/out-of-distribution-generalization.md), [outcome reward](../concepts/outcome-reward.md), [pass@k](../concepts/pass-k.md), [persona conditioning](persona-conditioning.md), [policy entropy](../concepts/policy-entropy.md), [policy gradient masking](policy-gradient-masking.md), [post-hoc rationalization](../concepts/post-hoc-rationalization.md), [PPO](ppo.md), [prompt sensitivity](../concepts/prompt-sensitivity.md), [Qwen2.5-14B-Instruct](../models/qwen2-5-14b-instruct.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [reasoning collapse](../concepts/reasoning-collapse.md), [retrieval-augmented generation](retrieval-augmented-generation.md), [reward hacking](../concepts/reward-hacking.md), [reward shaping](reward-shaping.md), [RLVR](rlvr.md), [self-consistency](self-consistency.md), [supervised fine-tuning](supervised-fine-tuning.md), [test-time scaling](../concepts/test-time-scaling.md), [TimesFM](../models/timesfm.md), [token-level entropy](../concepts/token-level-entropy.md), [Traffic](../datasets/traffic.md), [training dynamics](../concepts/training-dynamics.md), [Weather](../datasets/weather.md), [zero-advantage group](../concepts/zero-advantage-group.md)

## Appears in

- [LLM Reasoning for Subjective Tasks: Failure Modes, Mitigation, and Dynamic Reasoning Routing](../../archive/papers/2026/arxiv-2608-08889/summary.md) — Shows on four internal Netflix verification tasks that explicit reasoning usually degrades subjective judgement, that applying RLVR to fix it makes the policy abandon deliberation for short heuristic guessing, and that a length bonus gated on answer correctness is what stops the collapse.
- [REATS: LLM Reasoning-based Ensemble Learning for Adaptive Time Series Forecasting](../../archive/papers/2026/arxiv-2608-10149/summary.md) — Fine-tunes a 1.7B model to read structured summaries of a time series and allocate ensemble weights across candidate forecasters, trained by SFT on rule-generated chains of thought and then by GRPO with a bounded reciprocal reward that keeps a continuous error gap from collapsing the group advantage.
- [On the Entropy Dynamics in Reinforcement Fine-Tuning of Large Language Models](../../archive/papers/2026/local-837612b527cb427c/summary.md) — Reduces the question of whether an update raises or lowers entropy to the sign of one scalar per token, shows that under GRPO what matters is that scalar's deviation from a policy-weighted baseline rather than its own value, and proves the deviation averages to zero over a batch.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
