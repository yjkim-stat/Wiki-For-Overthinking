# weighted voting

<!-- auto:begin -->

Weighted voting selects a final answer from multiple sampled reasoning chains by weighting each vote instead of counting them equally, as in plain majority voting. The inference-scaling-laws source includes it as one point of comparison against greedy decoding, majority voting, best-of-n and tree search when measuring accuracy against FLOPs; ContextPRM instead trains a process reward model that scores chain-of-thought coherence, rather than domain knowledge, and uses that score to weight the votes, extending the approach to non-math domains.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Accuracy-Efficiency Tradeoff](accuracy-efficiency-tradeoff.md), [Best-of-N](../methods/best-of-n.md), [Compute-optimal inference](compute-optimal-inference.md), [GSM8K](../datasets/gsm8k.md), [majority voting](../methods/majority-voting.md), [MATH-500](../datasets/math-500.md), [MBPP](../datasets/mbpp.md), [process reward model](process-reward-model.md), [test-time compute scaling](test-time-compute-scaling.md), [tree-search decoding](tree-search-decoding.md)

## Appears in

- [Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving](../../archive/papers/2025/title-0d818df77a2dc810/summary.md) — An empirical study of compute-optimal inference that measures accuracy against FLOPs for greedy decoding, sampling with majority and weighted voting, best-of-n and tree search across model sizes, and introduces REBASE, a reward-guided tree search.
- [ContextPRM: Leveraging Contextual Coherence for multi-domain Test-Time Scaling](../../archive/papers/2026/title-da31eb8bef16ddcc/summary.md) — Trains a process reward model that scores chain-of-thought coherence instead of domain knowledge, and uses it to weight votes among sampled reasoning chains for test-time scaling across math and non-math domains.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
