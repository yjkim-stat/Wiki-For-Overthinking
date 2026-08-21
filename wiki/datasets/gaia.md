# GAIA

<!-- auto:begin -->

A benchmark of multi-step, tool-using agent tasks used in the archive to evaluate deep-search / web-research LLM agents: the asymmetric-verification deep-search paper and WebThinker's autonomous web-search-and-report-drafting loop both evaluate on it. Note: unrelated to the archive's separately-collected paper literally titled 'GAIA: A Data Flywheel System for Training GUI Test-Time Scaling Critic Models', which names its own, different GUI-agent critic system 'GAIA' -- a name collision between two distinct things both called GAIA.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [Budget Forcing](../methods/budget-forcing.md), [deepseek-v4-flash](../models/deepseek-v4-flash.md), [deepseek-v4-pro](../models/deepseek-v4-pro.md), [GPQA](gpqa.md), [HLE](hle.md), [SWE-bench Verified](swe-bench-verified.md)

## Appears in

- [CHILL-Harness: Counterfactual Harness Learning for Efficient Reasoning in Long-Horizon Agents](../../archive/papers/2026/arxiv-2607-25825/summary.md) — Treats an agent harness's orchestration decisions as causal interventions on the current workflow, learns which ones would improve it, and executes only those whose estimated advantage clears a margin -- so deliberation is spent where it changes the plan rather than at every step.
- [Pushing Test-Time Scaling Limits of Deep Search with Asymmetric Verification](../../archive/papers/2026/title-711c479b500244c5/summary.md) — Studies sequential and parallel test-time compute scaling for deep-search LLM agents and shows that allocating modest compute to a cheap verifier outperforms pushing sequential generation length further.
- [WebThinker: Empowering Large Reasoning Models with Deep Research Capability](../../archive/papers/2025/title-93df459afa09bdd6/summary.md) — WebThinker gives large reasoning models an autonomous web-search-and-report-drafting loop, trained via iterative online DPO, for knowledge-intensive deep research tasks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
