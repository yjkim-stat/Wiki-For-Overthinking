# Monte Carlo Tree Search

<!-- auto:begin -->

A search algorithm that builds a tree of candidate reasoning/solution steps, using simulated rollouts to decide which branches to explore further, applied at inference time to scale test-time compute. BG-MCTS reallocates exploration versus refinement as a fixed token budget depletes; 'Less Diverse, Less Safe' finds MCTS (like Best-of-N) becomes more likely to produce unsafe outputs when candidate diversity is reduced; UnMaskFork applies it to masked-diffusion-model unmasking decisions.

- **Kind**: method
- **Also called**: MCTS, tree search
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [Best-of-N](best-of-n.md), [Best-of-N sampling](best-of-n-sampling.md), [mathematical reasoning benchmarks](../concepts/mathematical-reasoning-benchmarks.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [Test-time scaling](../concepts/test-time-scaling.md), [Tree Search Decoding](../concepts/tree-search-decoding.md)

## Appears in

- [Aligning Tree-Search Policies with Fixed Token Budgets in Test-Time Scaling of LLMs](../../archive/papers/2026/title-20270e5fc6210ea6/summary.md) — Proposes a budget-aware Monte Carlo Tree Search policy (BG-MCTS) that reallocates exploration versus refinement as a fixed per-query token budget is consumed, for test-time scaling of LLMs.
- [Less Diverse, Less Safe: The Indirect But Pervasive Risk of Test-Time Scaling in Large Language Models](../../archive/papers/2026/title-abd61e399170fa2c/summary.md) — Shows that test-time-scaling methods such as Monte Carlo Tree Search and Best-of-N become substantially more likely to produce unsafe outputs when candidate diversity is curtailed, using a diagnostic protocol called RefDiv.
- [UnMaskFork: Test-Time Scaling for Masked Diffusion via Deterministic Action Branching](../../archive/papers/2026/title-d9e74e95d6430dc0/summary.md) — Uses Monte Carlo Tree Search over deterministic partial-unmasking actions to scale test-time compute for masked diffusion language models on coding and math tasks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
