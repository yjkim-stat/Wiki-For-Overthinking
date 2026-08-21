# LiveCodeBench

<!-- auto:begin -->

A code-generation benchmark used in the archive alongside math benchmarks to evaluate test-time-compute methods across domains: the bandit-learning compute-allocation paper and Kinetics' reworked test-time scaling law both report results on it.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 8

**Related**: [Accuracy-Efficiency Tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [Accuracy-Length Tradeoff](../concepts/accuracy-length-tradeoff.md), [activation steering](../methods/activation-steering.md), [AIME](aime.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC](amc.md), [AMC23](amc23.md), [chain-of-thought compression](../concepts/chain-of-thought-compression.md), [chain-of-thought prompting](../concepts/chain-of-thought-prompting.md), [DeepSeek-R1-Distill-Qwen-1.5B](../methods/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../methods/deepseek-r1-distill-qwen-7b.md), [DEER](../methods/deer.md), [Dynamic Early Exit](../methods/dynamic-early-exit.md), [GFPO](../methods/gfpo.md), [GPQA](gpqa.md), [GPQA-Diamond](gpqa-diamond.md), [group relative advantage](../concepts/group-relative-advantage.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [HumanEval](humaneval.md), [KV cache compression](../methods/kv-cache-compression.md), [KV-cache eviction](../methods/kv-cache-eviction.md), [Manifold Steering](../methods/manifold-steering.md), [MATH](math.md), [MATH-500](math-500.md), [MathQA](mathqa.md), [MBPP](mbpp.md), [Minerva Math](minerva-math.md), [MMLU](mmlu.md), [NoThinking](../methods/nothinking.md), [NOWAIT](../methods/nowait.md), [O1-Pruner](../methods/o1-pruner.md), [OlympiadBench](olympiadbench.md), [Omni-MATH](omni-math.md), [overthinking](../concepts/overthinking.md), [Phi-4-reasoning](../methods/phi-4-reasoning.md), [Qwen2.5-Instruct](../methods/qwen2-5-instruct.md), [R-KV](../methods/r-kv.md), [Redundant Self-Verification](../concepts/redundant-self-verification.md), [Reinforcement Learning with Verifiable Rewards](../methods/reinforcement-learning-with-verifiable-rewards.md), [Reward Shaping](../concepts/reward-shaping.md), [SEAL](../methods/seal.md), [Still](still.md), [StrategyQA](strategyqa.md), [test-time compute](../concepts/test-time-compute.md), [test-time compute allocation](../concepts/test-time-compute-allocation.md), [test-time compute scaling](../concepts/test-time-compute-scaling.md), [test-time scaling](../concepts/test-time-scaling.md), [TrimR](../methods/trimr.md), [underthinking](../concepts/underthinking.md)

## Appears in

- [Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL](../../archive/papers/2025/title-0bc5d9b198744bed/summary.md) — AutoThink uses a three-stage RL curriculum with stage-wise reward shaping to teach R1-style distilled models to decide per problem whether to emit an explicit reasoning chain at all.
- [ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models](../../archive/papers/2026/title-3a1fb8083fa0ff85/summary.md) — A KV-cache compression framework that labels segments of a reasoning trace by thought type and applies per-type quantization and progressive eviction, keeping accuracy near full-cache at under 5% of the cache.
- [Efficient Reasoning with Balanced Thinking](../../archive/papers/2026/title-7a3e08192f168bcb/summary.md) — ReBalance is a training-free inference-time steering method that reads a reasoning model's token confidence to detect overthinking or underthinking and applies a hidden-state steering vector to shorten or extend the chain of thought accordingly.
- [Sample More to Think Less: Group Filtered Policy Optimization for Concise Reasoning](../../archive/papers/2026/title-d02c8db6721c4d3c/summary.md) — GFPO samples a larger group of rollouts per problem during RL training and updates only on the top-k by length or by reward-per-token, converting extra training-time compute into shorter responses at inference.
- [ShorterBetter: Guiding Reasoning Models to Find Optimal Inference Length for Efficient Reasoning](../../archive/papers/2025/title-d40396527f776f1d/summary.md) — ShorterBetter takes the length of the shortest correct response in a sampled group as a per-problem target and rewards the model for matching it, cutting output length by 50%-80% on DeepSeek-Distill-Qwen-1.5B/7B.
- [Strategic Scaling of Test-Time Compute: A Bandit Learning Approach](../../archive/papers/2026/title-de00054e3faab991/summary.md) — Formulates test-time compute allocation across queries as a bandit learning problem so that harder queries get more compute and easier ones get less.
- [Dynamic Early Exit in Reasoning Models](../../archive/papers/2026/title-f508a5b012a33fd1/summary.md) — DEER is a training-free decoding method that watches for the points where a reasoning model switches thought chains, prompts it for a trial answer there, and terminates the chain of thought when the trial answer's token confidence exceeds a threshold.
- [Kinetics: Rethinking Test-Time Scaling Law](../../archive/papers/2025/title-fe7ecea333b91370/summary.md) — Reworks test-time scaling laws to account for memory-access cost alongside compute, finding a 14B-parameter threshold below which test-time compute is less effective, and shows sparse attention substantially improves accuracy under a fixed test-time budget.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
