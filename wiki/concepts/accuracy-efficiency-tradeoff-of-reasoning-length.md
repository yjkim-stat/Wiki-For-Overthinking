# accuracy-efficiency tradeoff of reasoning length

<!-- auto:begin -->

The core tension the archive's sources study: a reasoning model's accuracy as a function of how many tokens it spends thinking is not monotonic — spending more improves accuracy up to a point and then wastes compute or actively hurts it (overthinking), while spending too few tokens leaves genuinely hard problems unsolved (underthinking). OptimalThinkingBench frames this as a single benchmark (OverthinkingBench + UnderthinkingBench) precisely because no evaluated model balances both sides of the tradeoff at once.

- **Kind**: concept
- **Also called**: overthinking/underthinking tradeoff
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [AdaptThink](../methods/adaptthink.md), [AIME 2025](../datasets/aime-2025.md), [AUC_OAA](auc-oaa.md), [difficulty-based routing between reasoning modes](difficulty-based-routing-between-reasoning-modes.md), [F1^otb combined metric](f1-otb-combined-metric.md), [HMMT25](../datasets/hmmt25.md), [hybrid thinking/non-thinking models](hybrid-thinking-non-thinking-models.md), [L1 length-controlled reinforcement learning](../methods/l1-length-controlled-reinforcement-learning.md), [Model Merging](../methods/model-merging.md), [Overthinking](overthinking.md), [Overthinking-Adjusted Accuracy (OAA)](overthinking-adjusted-accuracy-oaa.md), [OverthinkingBench](../datasets/overthinkingbench.md), [Test-Time Compute Scaling](test-time-compute-scaling.md), [thinking-token budget](thinking-token-budget.md), [trained difficulty-based router / oracle router](trained-difficulty-based-router-oracle-router.md), [underthinking](underthinking.md), [UnderthinkingBench](../datasets/underthinkingbench.md), [VeriThinker](../methods/verithinker.md)

## Appears in

- [OptimalThinkingBench: Evaluating Over and Underthinking in LLMs](../../archive/papers/2025/local-49199e3b0f694ee1/summary.md) — Introduces OptimalThinkingBench, a unified benchmark pairing OverthinkingBench (simple queries) and UnderthinkingBench (hard reasoning/math) with a shared F1 metric, showing that none of 33 evaluated LLMs balances accuracy and thinking-token efficiency.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
