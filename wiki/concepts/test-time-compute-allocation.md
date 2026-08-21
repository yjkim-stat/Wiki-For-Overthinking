# test-time compute allocation

<!-- auto:begin -->

Test-time compute allocation means deciding, per query, how much inference-time compute or reasoning effort to spend. The RTL-optimization source (ARES) raises an LLM agent's per-call reasoning effort only after progress on a task stalls, reporting normalized dollar cost alongside a power-area-delay figure of merit; 'Strategic Scaling of Test-Time Compute' instead formulates the allocation across queries as a bandit-learning problem, so harder queries receive more compute and easier ones less.

- **Kind**: concept
- **Also called**: Test-Time Compute Allocation
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2025](../datasets/aime-2025.md), [Ares](../methods/ares.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH-500](../datasets/math-500.md)

## Appears in

- [ARES: Adaptive Reasoning-Effort Steering for PPA- and Cost-Aware RTL Optimization with LLM Agents](../../archive/papers/2026/arxiv-2607-27879/summary.md) — Ares is an LLM-agent RTL optimizer that raises the per-call reasoning effort only after progress stalls, and reports the normalized dollar cost of every call next to the power-area-delay figure of merit.
- [Strategic Scaling of Test-Time Compute: A Bandit Learning Approach](../../archive/papers/2026/title-de00054e3faab991/summary.md) — Formulates test-time compute allocation across queries as a bandit learning problem so that harder queries get more compute and easier ones get less.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
