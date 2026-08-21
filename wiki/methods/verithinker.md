# VeriThinker

<!-- auto:begin -->

An auxiliary-verification-training method for reducing overthinking, listed in the 'Don't Overthink It' survey's taxonomy and tested as one of five mitigation strategies in OptimalThinkingBench (appearing there twice in the archive's evidence, from the same paper's discussion of training-time and test-time mitigations). Like the other length-reduction methods tested (L1, AdaptThink, Model Merging), it cuts OverthinkingBench token usage but, in most tested configurations, degrades UnderthinkingBench accuracy by up to 13%.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [A*-Thought](a-thought.md), [accuracy-efficiency tradeoff of reasoning length](../concepts/accuracy-efficiency-tradeoff-of-reasoning-length.md), [Ada-R1](ada-r1.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [AdaptThink](adaptthink.md), [AIME 2025](../datasets/aime-2025.md), [AUC_OAA](../concepts/auc-oaa.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [DEER](deer.md), [difficulty-based routing between reasoning modes](../concepts/difficulty-based-routing-between-reasoning-modes.md), [DRP](drp.md), [Early Exit](early-exit.md), [F1^otb combined metric](../concepts/f1-otb-combined-metric.md), [HMMT25](../datasets/hmmt25.md), [hybrid thinking/non-thinking models](../concepts/hybrid-thinking-non-thinking-models.md), [L1 length-controlled reinforcement learning](l1-length-controlled-reinforcement-learning.md), [Laser](laser.md), [LC-R1](lc-r1.md), [Manifold Steering](manifold-steering.md), [Model Merging](model-merging.md), [NOWAIT](nowait.md), [Overthinking](../concepts/overthinking.md), [Overthinking-Adjusted Accuracy (OAA)](../concepts/overthinking-adjusted-accuracy-oaa.md), [OverthinkingBench](../datasets/overthinkingbench.md), [PLAN-AND-BUDGET](plan-and-budget.md), [S-GRPO](s-grpo.md), [SEAL](seal.md), [SelfBudgeter](selfbudgeter.md), [SPIRIT](spirit.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [thinking-token budget](../concepts/thinking-token-budget.md), [Thinkless](thinkless.md), [TokenSkip](tokenskip.md), [trained difficulty-based router / oracle router](../concepts/trained-difficulty-based-router-oracle-router.md), [underthinking](../concepts/underthinking.md), [UnderthinkingBench](../datasets/underthinkingbench.md)

## What we have settled

- **Established** — VeriThinker has an official public code release at github.com/czg1225/VeriThinker, published alongside its NeurIPS 2025 paper.
  - Checked the repository directly; it is the paper authors' own implementation of the auxiliary-verification-training method for reducing overthinking.

## Appears in

- [OptimalThinkingBench: Evaluating Over and Underthinking in LLMs](../../archive/papers/2025/local-49199e3b0f694ee1/summary.md) — Introduces OptimalThinkingBench, a unified benchmark pairing OverthinkingBench (simple queries) and UnderthinkingBench (hard reasoning/math) with a shared F1 metric, showing that none of 33 evaluated LLMs balances accuracy and thinking-token efficiency.
- [Don't Overthink It: A Survey of Efficient R1-style Large Reasoning Models](../../archive/papers/2025/local-6c80b6fd388d671e/summary.md) — A survey that organizes methods for making R1-style large reasoning models reason efficiently (i.e., avoid overthinking) into two axes: single-model optimization and multi-model collaboration.

## Checked against

- [https://github.com/czg1225/VeriThinker](https://github.com/czg1225/VeriThinker) — github.com · code · retrieved 2026-08-21
  - _We introduce VeriThinker, a novel approach for CoT compression. Unlike conventional methods that fine-tune LRMs directly on the original reasoning task using synthetic concise CoT data, we innovatively fine-tune the model solely through an auxiliary verification task._

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
