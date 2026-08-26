# deepseek-v4-pro

<!-- auto:begin -->

DeepSeek's largest V4 reasoning model, used in this archive as a frontier reference rather than as a subject. Two roles: it is one of three reference models whose average unbudgeted output length defines the difficulty stratification of a shared-budget benchmark, where it is also the best-allocating open model tested; and it is the backbone for the software-repair and terminal-interaction halves of an agentic harness study, whose GAIA half runs on the smaller deepseek-v4-flash instead. That split is worth remembering when reading either paper: a cross-benchmark pattern in the harness study is confounded with the change of backbone.

- **Kind**: model
- **Also called**: DeepSeek V4 Pro, DeepSeek-V4-Pro, deepseek-v4-pro
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Claude-Opus-4.8](claude-opus-4-8.md), [deepseek-v4-flash](deepseek-v4-flash.md), [GAIA](../datasets/gaia.md), [GLM-5.2](glm-5-2.md), [GPT-5.5](gpt-5-5.md), [Omni-MATH](../datasets/omni-math.md), [Resource-Rational Reasoning](../concepts/resource-rational-reasoning.md), [SWE-bench Verified](../datasets/swe-bench-verified.md)

## Appears in

- [CHILL-Harness: Counterfactual Harness Learning for Efficient Reasoning in Long-Horizon Agents](../../archive/papers/2026/arxiv-2607-25825/summary.md) — Treats an agent harness's orchestration decisions as causal interventions on the current workflow, learns which ones would improve it, and executes only those whose estimated advantage clears a margin -- so deliberation is spent where it changes the plan rather than at every step.
- [$R^3$-Bench: LLMs Struggle with Resource-Rational Reasoning under Shared Budgets](../../archive/papers/unknown/arxiv-2608-16033/summary.md) — A benchmark that puts six problems of mixed difficulty under one shared computation budget and measures the gap between what a model solves problem-by-problem and what it solves when it must decide how to divide the budget.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
