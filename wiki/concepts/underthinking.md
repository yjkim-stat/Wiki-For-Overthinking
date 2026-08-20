# underthinking

<!-- auto:begin -->

The complement failure mode to overthinking: a model reasons too little on a problem that genuinely requires deliberate, multi-step reasoning. The archive's 6 sources give it several concrete mechanisms: taking the first plausible answer without exploring alternatives or verifying it (OptimalThinkingBench), failing to extend a chain of thought far enough on hard questions while overthinking easy ones (Between Underthinking and Overthinking), and frequent premature switching between partial reasoning 'thoughts' before any is followed to completion, which prevents deep exploration of a promising line of reasoning ('Thoughts Are All Over the Place', which introduces a decoding-time penalty, TIP, to discourage the switching). TrimR and Plan-and-Budget both note it as the failure mode their overthinking-trimming methods must avoid falling into.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 6

**Related**: [accuracy-efficiency tradeoff of reasoning length](accuracy-efficiency-tradeoff-of-reasoning-length.md), [AdaptThink](../methods/adaptthink.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AUC_OAA](auc-oaa.md), [difficulty-based routing between reasoning modes](difficulty-based-routing-between-reasoning-modes.md), [F1^otb combined metric](f1-otb-combined-metric.md), [GPQA](../datasets/gpqa.md), [GSM8K](../datasets/gsm8k.md), [HMMT 2025](../datasets/hmmt-2025.md), [hybrid thinking/non-thinking models](hybrid-thinking-non-thinking-models.md), [L1 length-controlled reinforcement learning](../methods/l1-length-controlled-reinforcement-learning.md), [MATH](../datasets/math.md), [MATH-500](../datasets/math-500.md), [Model Merging](../methods/model-merging.md), [overthinking](overthinking.md), [Overthinking-Adjusted Accuracy (OAA)](overthinking-adjusted-accuracy-oaa.md), [OverthinkingBench](../datasets/overthinkingbench.md), [PLAN-AND-BUDGET](../methods/plan-and-budget.md), [SuperGPQA](../datasets/supergpqa.md), [test-time compute scaling](test-time-compute-scaling.md), [test-time scaling](test-time-scaling.md), [thinking-token budget](thinking-token-budget.md), [trained difficulty-based router / oracle router](trained-difficulty-based-router-oracle-router.md), [UnderthinkingBench](../datasets/underthinkingbench.md), [VeriThinker](../methods/verithinker.md)

## Appears in

- [OptimalThinkingBench: Evaluating Over and Underthinking in LLMs](../../archive/papers/2025/local-49199e3b0f694ee1/summary.md) — Introduces OptimalThinkingBench, a unified benchmark pairing OverthinkingBench (simple queries) and UnderthinkingBench (hard reasoning/math) with a shared F1 metric, showing that none of 33 evaluated LLMs balances accuracy and thinking-token efficiency.
- [Between Underthinking and Overthinking: An Empirical Study of Reasoning Length and correctness in LLMs](../../archive/papers/2025/local-6afb006d68240134/summary.md) — An empirical study showing reasoning LLMs overthink easy questions and underthink hard ones, and that preferring shorter outputs via SimPO can cut generation length 30-60% with little accuracy loss.
- [Thoughts Are All Over the Place: On the Underthinking of Long Reasoning Models](../../archive/papers/2025/title-2e5e00164f8a905d/summary.md) — Identifies 'underthinking' in long reasoning models, where frequent switching between reasoning thoughts prevents sufficient exploration and hurts accuracy, and proposes a decoding-time penalty to fix it.
- [OptimalThinkingBench: Evaluating Over and Underthinking in LLMs](../../archive/papers/2026/title-441c8494292f11c7/summary.md) — Introduces OptimalThinkingBench, a unified benchmark pairing OverthinkingBench (simple queries) and UnderthinkingBench (hard reasoning/math) with a shared F1 metric, showing that none of 33 evaluated LLMs balances accuracy and thinking-token efficiency.
- [TrimR: Verifier-based Training-Free Thinking Trimming for Efficient Test-Time Scaling](../../archive/papers/2026/title-b987d2649d32f1f3/summary.md) — TrimR is a training-free, verifier-based system that trims redundant chain-of-thought reasoning in deployed large reasoning models to speed up test-time scaling with little accuracy loss.
- [Plan and Budget: Effective and Efficient Test-Time Scaling on Reasoning Large Language Models](../../archive/papers/2026/title-f0073c841a41fca9/summary.md) — Plan-and-Budget decomposes queries into sub-questions and allocates test-time token budgets by estimated complexity, using a theoretical model of reasoning as sequential sub-questions to reduce both overthinking and underthinking.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
