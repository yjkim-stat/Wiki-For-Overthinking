# SWE-bench Verified

<!-- auto:begin -->

A curated, human-verified subset of SWE-bench (real GitHub issue-resolution tasks) used to evaluate agentic coding performance under a fixed compute/cost budget. 'The Danger of Overthinking' uses it as its main evaluation set, showing that a lower measured overthinking score correlates with higher issue-resolution rates and lower cost; Consilience's verifier-free rollout-selection metric also evaluates on it.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [best-of-n selection](../methods/best-of-n-selection.md), [deepseek-v4-flash](../models/deepseek-v4-flash.md), [deepseek-v4-pro](../models/deepseek-v4-pro.md), [GAIA](gaia.md), [GPQA-Diamond](gpqa-diamond.md), [HMMT 2025](hmmt-2025.md), [LiveCodeBench-v6](livecodebench-v6.md), [Overthinking](../concepts/overthinking.md), [Pass@1](../concepts/pass-1.md), [pass@K](../concepts/pass-k.md), [reasoning effort](../concepts/reasoning-effort.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md)

## Appears in

- [CHILL-Harness: Counterfactual Harness Learning for Efficient Reasoning in Long-Horizon Agents](../../archive/papers/2026/arxiv-2607-25825/summary.md) — Treats an agent harness's orchestration decisions as causal interventions on the current workflow, learns which ones would improve it, and executes only those whose estimated advantage clears a margin -- so deliberation is spent where it changes the plan rather than at every step.
- [Consilience for Verifier-Free Test-Time Scaling](../../archive/papers/2026/arxiv-2608-09898/summary.md) — Introduces consilience, a verifier-free test-time-scaling selection metric that picks the sampled reasoning rollout whose confidence starts low (exploratory) and ends high (convergent), fixing a failure mode where naive confidence maximization favors confidently wrong answers on hard problems.
- [The Danger of Overthinking: Examining the Reasoning-Action Dilemma in Agentic Tasks](../../archive/papers/2025/local-9f60265e5ada34cb/summary.md) — Defines and measures 'overthinking' in Large Reasoning Models on real software-engineering agent tasks, showing that favoring internal reasoning over environment interaction correlates with lower SWE-bench issue-resolution rates and can be mitigated at lower cost.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
