# weighted voting

<!-- auto:begin -->

Weighted voting selects a final answer from multiple sampled reasoning chains by weighting each vote instead of counting them equally, as in plain majority voting. The inference-scaling-laws source includes it as one point of comparison against greedy decoding, majority voting, best-of-n and tree search when measuring accuracy against FLOPs; ContextPRM instead trains a process reward model that scores chain-of-thought coherence, rather than domain knowledge, and uses that score to weight the votes, extending the approach to non-math domains.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [accuracy-efficiency tradeoff](accuracy-efficiency-tradeoff.md), [best-of-N](../methods/best-of-n.md), [Compute-optimal inference](compute-optimal-inference.md), [greedy decoding](../methods/greedy-decoding.md), [GSM8K](../datasets/gsm8k.md), [majority voting](../methods/majority-voting.md), [majority voting / self-consistency](../methods/majority-voting-self-consistency.md), [MATH500](../datasets/math500.md), [MBPP](../datasets/mbpp.md), [process reward model](../methods/process-reward-model.md), [Test-Time Compute Scaling](test-time-compute-scaling.md), [Tree Search Decoding](tree-search-decoding.md)

## Appears in

- [Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving](../../archive/papers/2025/title-0d818df77a2dc810/summary.md) — An empirical study of compute-optimal inference that measures accuracy against FLOPs for greedy decoding, sampling with majority and weighted voting, best-of-n and tree search across model sizes, and introduces REBASE, a reward-guided tree search.
- [ContextPRM: Leveraging Contextual Coherence for multi-domain Test-Time Scaling](../../archive/papers/2026/title-da31eb8bef16ddcc/summary.md) — Trains a process reward model that scores chain-of-thought coherence instead of domain knowledge, and uses it to weight votes among sampled reasoning chains for test-time scaling across math and non-math domains.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
