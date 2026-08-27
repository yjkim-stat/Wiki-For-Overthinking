# HMMT25

<!-- auto:begin -->

A sitting of the Harvard-MIT Mathematics Tournament used in this archive as a hard competition-maths benchmark alongside AIME, on the order of 30 problems. It appears mainly in parallel-reasoning and test-time-scaling evaluations, where sources use it as the case that breaks an aggregate: it is named as the one regression in a method that gains elsewhere, and as the ablation set where removing a component costs the most. At that size a few items move the score by several points, so per-benchmark differences here are not separable from noise without repeated runs.

- **Kind**: dataset
- **Also called**: HMMT Nov 2025, HMMT'25, HMMT-25
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [accuracy-efficiency tradeoff of reasoning length](../concepts/accuracy-efficiency-tradeoff-of-reasoning-length.md), [AdaptThink](../methods/adaptthink.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [AUC_OAA](../concepts/auc-oaa.md), [CMIMC25](cmimc25.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [difficulty-based routing between reasoning modes](../concepts/difficulty-based-routing-between-reasoning-modes.md), [F1^otb combined metric](../concepts/f1-otb-combined-metric.md), [GPQA](gpqa.md), [hybrid thinking/non-thinking models](../concepts/hybrid-thinking-non-thinking-models.md), [L1 length-controlled reinforcement learning](../methods/l1-length-controlled-reinforcement-learning.md), [MMLU-Pro](mmlu-pro.md), [Model Merging](../methods/model-merging.md), [Overthinking](../concepts/overthinking.md), [Overthinking-Adjusted Accuracy (OAA)](../concepts/overthinking-adjusted-accuracy-oaa.md), [OverthinkingBench](overthinkingbench.md), [Pass@1](../concepts/pass-1.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [thinking-token budget](../concepts/thinking-token-budget.md), [trained difficulty-based router / oracle router](../concepts/trained-difficulty-based-router-oracle-router.md), [underthinking](../concepts/underthinking.md), [UnderthinkingBench](underthinkingbench.md), [VeriThinker](../methods/verithinker.md)

## Appears in

- [Claim-Level Reliability Assessment for Efficient Test-Time Reasoning](../../archive/papers/2026/arxiv-2608-11994/summary.md) — CLR reallocates part of the test-time compute budget from generating more solution samples to falsifying a small set of decision-critical claims extracted from each trace, improving accuracy over self-consistency while using fewer tokens on some models.
- [LEASH: Adaptive Length Penalty and Reward Shaping for Efficient Large Reasoning Model](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-129/summary.md) — LEASH formulates reasoning-length control as a constrained RL optimization (maximize task reward subject to an expected-length constraint) solved via a Lagrangian primal-dual method with a one-sided length penalty, letting the penalty coefficient lambda self-tighten or self-relax based on real-time constraint violation rather than requiring manual tuning, and reduces average reasoning length by up to 62.7% (1.5B model) or 26.2% (4B model) while maintaining or improving accuracy on in-domain math and out-of-domain (GPQA, MMLU-Pro) benchmarks, outperforming fixed-penalty and prior length-control baselines.
- [OptimalThinkingBench: Evaluating Over and Underthinking in LLMs](../../archive/papers/2025/local-49199e3b0f694ee1/summary.md) — Introduces OptimalThinkingBench, a unified benchmark pairing OverthinkingBench (simple queries) and UnderthinkingBench (hard reasoning/math) with a shared F1 metric, showing that none of 33 evaluated LLMs balances accuracy and thinking-token efficiency.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
