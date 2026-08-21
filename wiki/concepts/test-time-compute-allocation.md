# test-time compute allocation

<!-- auto:begin -->

Test-time compute allocation means deciding, per query, how much inference-time compute or reasoning effort to spend. The RTL-optimization source (ARES) raises an LLM agent's per-call reasoning effort only after progress on a task stalls, reporting normalized dollar cost alongside a power-area-delay figure of merit; 'Strategic Scaling of Test-Time Compute' instead formulates the allocation across queries as a bandit-learning problem, so harder queries receive more compute and easier ones less.

- **Kind**: concept
- **Also called**: Test-Time Compute Allocation, test-time compute allocation
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [AIME 2025](../datasets/aime-2025.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH500](../datasets/math500.md)

## Appears in

- [Strategic Scaling of Test-Time Compute: A Bandit Learning Approach](../../archive/papers/2026/title-de00054e3faab991/summary.md) — Formulates test-time compute allocation across queries as a bandit learning problem so that harder queries get more compute and easier ones get less.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
