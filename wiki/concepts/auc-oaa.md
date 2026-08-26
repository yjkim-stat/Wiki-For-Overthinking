# AUC_OAA

<!-- auto:begin -->

A metric from OptimalThinkingBench for scoring overthinking: Overthinking-Adjusted Accuracy (OAA_t) counts a response correct only if it also stays under a thinking-token threshold t, and AUC_OAA is the area under the OAA_t curve as t sweeps up to 1000 tokens. A model that reaches the right answer but keeps generating unnecessary tokens scores lower on AUC_OAA than one that stops promptly, even at equal raw accuracy.

- **Kind**: concept
- **Also called**: OAA, Overthinking-Adjusted Accuracy
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [accuracy-efficiency tradeoff of reasoning length](accuracy-efficiency-tradeoff-of-reasoning-length.md), [AdaptThink](../methods/adaptthink.md), [AIME 2025](../datasets/aime-2025.md), [difficulty-based routing between reasoning modes](difficulty-based-routing-between-reasoning-modes.md), [F1^otb combined metric](f1-otb-combined-metric.md), [HMMT25](../datasets/hmmt25.md), [hybrid thinking/non-thinking models](hybrid-thinking-non-thinking-models.md), [L1 length-controlled reinforcement learning](../methods/l1-length-controlled-reinforcement-learning.md), [Model Merging](../methods/model-merging.md), [Overthinking](overthinking.md), [Overthinking-Adjusted Accuracy (OAA)](overthinking-adjusted-accuracy-oaa.md), [OverthinkingBench](../datasets/overthinkingbench.md), [Test-Time Compute Scaling](test-time-compute-scaling.md), [thinking-token budget](thinking-token-budget.md), [trained difficulty-based router / oracle router](trained-difficulty-based-router-oracle-router.md), [underthinking](underthinking.md), [UnderthinkingBench](../datasets/underthinkingbench.md), [VeriThinker](../methods/verithinker.md)

## What we have settled

- **Established** — An overthinking metric evaluated on a non-thinking model measures nothing but its accuracy, so any cross-benchmark agreement established on such models is vacuous and cannot support a claim that two metrics measure the same thing.
  - Both of the archive's composite overthinking metrics degenerate on models that emit no reasoning, and the degeneration is provable from the published tables rather than inferred. On the OptimalThinkingBench side, AUC_OAA integrates OAA_t = mean of Correctness_i * I(ThinkTokens_i < t) over t in [0, 1000]; a non-thinking model has ThinkTokens = 0, the indicator is 1 for every t, and AUC_OAA becomes OverthinkingBench accuracy identically. Table 6 shows the two columns coinciding for every non-thinking entry -- Llama-4-Scout 95.0/95.0, Llama-4-Maverick 95.7/95.7, Qwen2.5-7B 93.6/93.6, GPT-4o 95.3/95.3. On the LLMThinkBench side the collapse is empirical rather than algebraic: E_t = 1 - (T_bar - T_min)/(T_max - T_min) is normalised over the whole evaluated set, whose extremes are T_min = 89.4 and T_max = 6780.7 tokens, both set by models outside the non-reasoning group; the seven non-thinking models this archive could match across both benchmarks emit 286.9 to 411.7 tokens, so their E_t spans only 0.9518 to 0.9705 -- a spread of 0.019 against an accuracy spread of 0.410, about 4.5% -- and the harmonic mean O = 2*A*E_t/(A + E_t) is a monotone function of accuracy over that range. Recomputing O from the published token counts and accuracies reproduces every reported Overthinking Score to within 0.003. The measurable consequence: across those seven models Spearman(Overthinking Score, LLMThinkBench accuracy) = +0.991, while Spearman(F1^otb, Overthinking Score) = +0.937. The second number would ordinarily read as two independent metrics converging; the first shows both are reporting the accuracy ranking. The consequence for this archive is a precondition on any metric-comparison claim: state which models carry reasoning, and treat a validation set without thinking models as no validation at all.

## Appears in

- [OptimalThinkingBench: Evaluating Over and Underthinking in LLMs](../../archive/papers/2025/local-49199e3b0f694ee1/summary.md) — Introduces OptimalThinkingBench, a unified benchmark pairing OverthinkingBench (simple queries) and UnderthinkingBench (hard reasoning/math) with a shared F1 metric, showing that none of 33 evaluated LLMs balances accuracy and thinking-token efficiency.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
