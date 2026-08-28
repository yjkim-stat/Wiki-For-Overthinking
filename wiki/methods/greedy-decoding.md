# greedy decoding

<!-- auto:begin -->

Greedy decoding is used in these sources as a deterministic baseline decoding strategy against which compute-scaling methods are measured: an inference-scaling-laws study measures accuracy-vs-FLOPs for greedy decoding alongside majority/weighted-vote sampling, best-of-n, and tree search (introducing REBASE, a reward-guided tree search, as an alternative), and TRACE's overthinking-structure study also uses greedy decoding as its generation setting when benchmarking thinking vs. non-thinking mode across 14 models.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [ASDiv](../datasets/asdiv.md), [best-of-N](best-of-n.md), [Compute-optimal inference](../concepts/compute-optimal-inference.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [GSM8K](../datasets/gsm8k.md), [majority voting](majority-voting.md), [majority voting / self-consistency](majority-voting-self-consistency.md), [MATH500](../datasets/math500.md), [MBPP](../datasets/mbpp.md), [Overthinking](../concepts/overthinking.md), [process reward model](process-reward-model.md), [Qwen3-235B-A22B](../models/qwen3-235b-a22b.md), [Qwen3-30B-A3B](../models/qwen3-30b-a3b.md), [Qwen3-32B](../models/qwen3-32b.md), [SimpleQA](../datasets/simpleqa.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [Tree Search Decoding](../concepts/tree-search-decoding.md), [weighted voting](../concepts/weighted-voting.md)

## Appears in

- [Do LLMs Really Need 10+ Thoughts for “Find the Time 1000 Days Later”? Towards Structural Understanding of LLM Overthinking](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-773/summary.md) — TRACE decomposes reasoning traces into sub-thoughts and labeled progression graphs across 14 thinking models and 6 domains, finding thinking helps only within a narrow middle ground (5-20x more compute wasted on simple tasks with no gain, and no benefit at all once model scale exceeds ~4-8B or task difficulty exceeds representational capacity), identifies two overthinking-driving thought-progression patterns (Explorer, Late Landing), and redefines overthinking structurally as continuation past the point where marginal return per sub-thought drops below a threshold.
- [Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving](../../archive/papers/2025/title-0d818df77a2dc810/summary.md) — An empirical study of compute-optimal inference that measures accuracy against FLOPs for greedy decoding, sampling with majority and weighted voting, best-of-n and tree search across model sizes, and introduces REBASE, a reward-guided tree search.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
