# Minerva Math

<!-- auto:begin -->

A mathematics benchmark that five archived efficient-reasoning papers evaluate on (AutoThink, REO-RL, QuRL, Ada-R1, ThreadWeaver); none of them describes its contents, so what the archive records is the role it plays - the harder maths set where accuracy sits far below MATH-500 for the same model. ThreadWeaver's Qwen3-8B scores 43.7% on Minerva Math against 91.4% on MATH500, and its threading ends 0.2 points below the sequential GRPO baseline (43.7% vs 43.9%) while producing the largest token-latency speedup of its six benchmarks, 1.53x against a median of about 1.19x - an outlier its own record flags. REO-RL uses it as one of only four maths benchmarks (AMC23, AIME24, AIME25, Minerva Math), which that paper's record names as the limit of its evidence: nothing is established outside mathematics. The archive separately holds an entry 'Minerva', written from the papers that use the shorter spelling; the two are near-certainly the same benchmark and are deliberately left un-aliased rather than merged, since an alias filed wrongly cannot be undone.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 5

**Related**: [Accuracy-Efficiency Pareto Frontier](../concepts/accuracy-efficiency-pareto-frontier.md), [Accuracy-Efficiency Tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [Ada-R1](../methods/ada-r1.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [AIME](aime.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [DAPO](../methods/dapo.md), [DeepScaleR](deepscaler.md), [DeepSeek-R1-Distill-Qwen-1.5B](../methods/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../methods/deepseek-r1-distill-qwen-7b.md), [GPQA](gpqa.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [LiveCodeBench](livecodebench.md), [MATH](math.md), [MATH-500](math-500.md), [Minerva](minerva.md), [MMLU](mmlu.md), [Model Merging](../methods/model-merging.md), [OlympiadBench](olympiadbench.md), [Omni-MATH](omni-math.md), [overthinking](../concepts/overthinking.md), [Reinforcement Learning with Verifiable Rewards](../concepts/reinforcement-learning-with-verifiable-rewards.md), [reward hacking](../concepts/reward-hacking.md), [Reward Shaping](../concepts/reward-shaping.md), [RLVR](../concepts/rlvr.md), [Still](still.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md), [test-time compute](../concepts/test-time-compute.md), [test-time compute scaling](../concepts/test-time-compute-scaling.md), [Token Budget](../concepts/token-budget.md)

## Appears in

- [Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL](../../archive/papers/2025/title-0bc5d9b198744bed/summary.md) — AutoThink uses a three-stage RL curriculum with stage-wise reward shaping to teach R1-style distilled models to decide per problem whether to emit an explicit reasoning chain at all.
- [How Far Are We from Optimal Reasoning Efficiency?](../../archive/papers/2025/title-279ee92c27a8bb8d/summary.md) — Defines an empirical accuracy-vs-token-budget frontier for a fixed base reasoning model, measures how far existing efficiency methods fall short of it with a single metric (REG), and proposes REO-RL, an RL objective that targets a handful of token budgets to close most of that gap.
- [QuRL: Low-Precision Reinforcement Learning for Efficient Reasoning](../../archive/papers/2026/title-9b034ca49bd46f6f/summary.md) — QuRL runs the rollout phase of RL-with-verifiable-rewards training with an INT8 or FP8 quantized copy of the actor, adding an adaptive clipping range and an invariant weight-scaling trick to keep the low-precision policy from collapsing, for 20-80% faster rollout.
- [Ada-R1: Hybrid-CoT via Bi-Level Adaptive Reasoning Optimization](../../archive/papers/2025/title-a6dab00057eab5aa/summary.md) — Ada-R1 merges a long-CoT and a short-CoT model into one hybrid, then applies two levels of preference training so the model first picks a reasoning style per problem and then prefers the shorter correct trace within that style, cutting average reasoning length by about 51% on five maths datasets.
- [ThreadWeaver: Adaptive Threading for Efficient Parallel Reasoning in Language Models](../../archive/papers/2026/title-c65838fd39e8d183/summary.md) — Trains Qwen3-8B to split its chain of thought into concurrently decoded threads that spawn and join, so the critical path is shorter than a sequential trace of the same total length, using a trie-based rollout that runs on stock autoregressive inference engines.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
