# Tree Search Decoding

<!-- auto:begin -->

Tree-search decoding explores a branching space of partial reasoning continuations rather than sampling independent complete rollouts. The inference-scaling-laws source measures accuracy against FLOPs for greedy decoding, majority/weighted-vote sampling, best-of-n and tree search, and introduces REBASE, a reward-guided tree search; the second source proposes BG-MCTS, a budget-aware Monte Carlo Tree Search policy that reallocates exploration versus refinement as a fixed per-query token budget is consumed.

- **Kind**: concept
- **Also called**: Tree Search Decoding, tree-search decoding
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [accuracy-efficiency tradeoff](accuracy-efficiency-tradeoff.md), [Best-of-N](../methods/best-of-n.md), [Compute-optimal inference](compute-optimal-inference.md), [GSM8K](../datasets/gsm8k.md), [Majority Voting](../methods/majority-voting.md), [MATH500](../datasets/math500.md), [mathematical reasoning benchmarks](mathematical-reasoning-benchmarks.md), [MBPP](../datasets/mbpp.md), [Monte Carlo Tree Search](../methods/monte-carlo-tree-search.md), [process reward model](../methods/process-reward-model.md), [Test-Time Compute Scaling](test-time-compute-scaling.md), [Test-Time Scaling](test-time-scaling.md), [weighted voting](weighted-voting.md)

## Appears in

- [Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving](../../archive/papers/2025/title-0d818df77a2dc810/summary.md) — An empirical study of compute-optimal inference that measures accuracy against FLOPs for greedy decoding, sampling with majority and weighted voting, best-of-n and tree search across model sizes, and introduces REBASE, a reward-guided tree search.
- [Aligning Tree-Search Policies with Fixed Token Budgets in Test-Time Scaling of LLMs](../../archive/papers/2026/title-20270e5fc6210ea6/summary.md) — Proposes a budget-aware Monte Carlo Tree Search policy (BG-MCTS) that reallocates exploration versus refinement as a fixed per-query token budget is consumed, for test-time scaling of LLMs.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
