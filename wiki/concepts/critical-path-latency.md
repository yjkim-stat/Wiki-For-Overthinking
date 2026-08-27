# critical-path latency

<!-- auto:begin -->

The wall-clock cost of a reasoning trace measured as the length of its longest sequential (non-parallelizable) token path, rather than its total token count -- so a trace whose branches run concurrently can have a critical path much shorter than its total length. Both sources use this as the metric that parallel-reasoning training methods are optimized to reduce, distinct from raw token count.

- **Kind**: concept
- **Also called**: Critical Path Latency, longest-token-path latency
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Accuracy-Efficiency Pareto Frontier](accuracy-efficiency-pareto-frontier.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [DeepSeek-R1](../models/deepseek-r1.md), [Gemini-2.5-Pro](../models/gemini-2-5-pro.md), [GPT-5.5](../models/gpt-5-5.md), [GRPO](../methods/grpo.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [OlympiadBench](../datasets/olympiadbench.md), [Qwen3-30B-A3B](../models/qwen3-30b-a3b.md), [Reward Hacking](reward-hacking.md), [Test-Time Compute Scaling](test-time-compute-scaling.md)

## Appears in

- [Parason: Revealing Subtask and Trial Parallelism in LLM Reasoning](../../archive/papers/2026/arxiv-2608-24658/summary.md) — Parason distinguishes two forms of parallel reasoning -- AND-branch Subtask Parallelism and OR-branch Trial Parallelism -- shows Trial Parallelism dominates on hard reasoning traces, and trains models to convert sequential CoT into grammar-structured parallel trajectories that a real inference engine executes for ~1.7x wall-clock speedup with competitive accuracy.
- [ThreadWeaver: Adaptive Threading for Efficient Parallel Reasoning in Language Models](../../archive/papers/2026/title-c65838fd39e8d183/summary.md) — Trains Qwen3-8B to split its chain of thought into concurrently decoded threads that spawn and join, so the critical path is shorter than a sequential trace of the same total length, using a trie-based rollout that runs on stock autoregressive inference engines.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
