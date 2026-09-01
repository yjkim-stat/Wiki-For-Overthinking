# Reward Hacking

<!-- auto:begin -->

None of the three sources define reward hacking's mechanism directly; it appears only as a named risk category. The survey on mechanistic understanding of large reasoning models groups it with hallucination, CoT unfaithfulness and overthinking as one of the 'unintended behaviors' that RL training on reasoning models can produce. TwT's n-gram repetition penalty on its translation reward and ThreadWeaver's reward design for parallel reasoning threads are each built to prevent a shortcut that would satisfy the stated reward without the intended reasoning behaviour, which is the same underlying failure mode the term names.

- **Kind**: concept
- **Also called**: Reward Hacking, reward hacking
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [Accuracy-Efficiency Pareto Frontier](accuracy-efficiency-pareto-frontier.md), [Aha Moment](aha-moment.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [critical-path latency](critical-path-latency.md), [GRPO](../methods/grpo.md), [linear probe](../methods/linear-probe.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](overthinking.md), [Reasoning Collapse](reasoning-collapse.md), [Resource-Rational Reasoning](resource-rational-reasoning.md), [sparse autoencoders (SAEs)](../methods/sparse-autoencoders-saes.md), [Test-Time Compute Scaling](test-time-compute-scaling.md)

## Appears in

- [Translation with Thought: Difficulty-Adaptive Reasoning via Reinforcement Learning for Multi-Domain Machine Translation](../../archive/papers/2026/arxiv-2607-29287/summary.md) — TwT trains a translation model to spend reasoning tokens in proportion to input difficulty, by cold-starting on 7K difficulty-rewritten CoT traces and then running GRPO with a BLEU+COMET quality reward and an n-gram repetition penalty.
- [Towards a Mechanistic Understanding of Large Reasoning Models: A Survey of Training, Inference, and Failures](../../archive/papers/2026/local-34cecfd6f28ba72b/summary.md) — A survey that organizes existing mechanistic-interpretability research on large reasoning models into three areas -- reasoning-oriented training dynamics, reasoning mechanisms, and unintended behaviors (hallucination, CoT unfaithfulness, overthinking, unsafety) -- and proposes directions for future mechanistic work.
- [ThreadWeaver: Adaptive Threading for Efficient Parallel Reasoning in Language Models](../../archive/papers/2026/title-c65838fd39e8d183/summary.md) — Trains Qwen3-8B to split its chain of thought into concurrently decoded threads that spawn and join, so the critical path is shorter than a sequential trace of the same total length, using a trie-based rollout that runs on stock autoregressive inference engines.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
