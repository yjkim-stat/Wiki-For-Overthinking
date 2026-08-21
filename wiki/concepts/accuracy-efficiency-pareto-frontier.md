# Accuracy-Efficiency Pareto Frontier

<!-- auto:begin -->

In the archived sources this names the set of non-dominated operating points when task accuracy is plotted against an efficiency cost, and it is used as an evaluative frame rather than as a quantity anyone computes. The multimodal edge-inference survey invokes it to argue that visual token compression, MoE routing, quantization and KV-cache policy cannot each be pushed to their own frontier independently, because their errors form a failure-propagation chain; ThreadWeaver invokes it for a different cost axis, latency, splitting a Qwen3-8B chain of thought into concurrently decoded threads so the critical path is shorter than a sequential trace of the same total token count. Neither source states a formula or a threshold, and the two do not agree on what 'efficiency' is measured in. Note: the archive tracks this idea under several near-duplicate entries that were never merged -- 'Accuracy-Efficiency Tradeoff', 'Accuracy-Length Tradeoff', 'Accuracy-token Pareto frontier', 'accuracy-efficiency tradeoff curve', 'accuracy-cost Pareto frontier' and 'accuracy-efficiency tradeoff of reasoning length' -- and they describe substantially the same thing.

- **Kind**: concept
- **Also called**: accuracy-cost Pareto frontier, accuracy-efficiency Pareto front
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [accuracy-efficiency tradeoff](accuracy-efficiency-tradeoff.md), [accuracy-efficiency tradeoff of reasoning length](accuracy-efficiency-tradeoff-of-reasoning-length.md), [Accuracy-Length Tradeoff](accuracy-length-tradeoff.md), [Accuracy-token Pareto frontier](accuracy-token-pareto-frontier.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [GRPO](../methods/grpo.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [OlympiadBench](../datasets/olympiadbench.md), [Reward Hacking](reward-hacking.md), [Test-Time Compute Scaling](test-time-compute-scaling.md)

## Appears in

- [ThreadWeaver: Adaptive Threading for Efficient Parallel Reasoning in Language Models](../../archive/papers/2026/title-c65838fd39e8d183/summary.md) — Trains Qwen3-8B to split its chain of thought into concurrently decoded threads that spawn and join, so the critical path is shorter than a sequential trace of the same total length, using a trie-based rollout that runs on stock autoregressive inference engines.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
