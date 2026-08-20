# cross-lingual transfer

<!-- auto:begin -->

Whether a capability trained in one language appears in another. Both sources train in one language and evaluate in others, and both find the transfer real but unevenly distributed. The distillation source concentrates its privileged supervision on tokens where the teacher's distribution shifts most when an English reference is added or removed, on the argument that the objective otherwise spreads supervision over tokens irrelevant to transfer. The tool-use source trains on Spanish and evaluates on three unseen European languages, where supervised fine-tuning and reinforcement learning reach near-identical averages (57.88 against 57.72) while distributing the gain differently across the three -- and where the supervised model's task gain is paid for by an 8.6-point regression in English mathematics that the reinforcement-learning model does not incur. That last point is the one worth carrying: transfer measured only in the target languages misses that the training may have damaged the source language, and an average over languages hides a loss concentrated in one.

- **Kind**: concept
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [advantage estimation](advantage-estimation.md), [catastrophic forgetting](catastrophic-forgetting.md), [credit assignment](credit-assignment.md), [GRPO](../methods/grpo.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [PPO](../methods/ppo.md), [privileged information](privileged-information.md), [process reward](process-reward.md), [process supervision](process-supervision.md), [Qwen2.5-14B-Instruct](../models/qwen2-5-14b-instruct.md), [Qwen2.5-32B-Instruct](../models/qwen2-5-32b-instruct.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [token-level distillation](../methods/token-level-distillation.md), [token selection](token-selection.md), [tool learning](tool-learning.md)

## Appears in

- [RP-OPSD: Reasoning-Pivot-Guided On-Policy Self-Distillation for Multilingual Reasoning Transfer](../../archive/papers/2026/arxiv-2608-06347/summary.md) — Concentrates privileged self-distillation on reasoning pivots identified by the teacher's distributional shift when an English reference solution is added or removed, for multilingual reasoning transfer.
- [When the API Speaks the Wrong Language: Revisiting Post-Training for Multilingual Tool Use](../../archive/papers/2026/arxiv-2608-11715/summary.md) — Names and measures a multilingual tool-calling failure in which the model picks the right API but writes argument values in the wrong language, then compares supervised fine-tuning against PPO and GRPO under matched budgets and finds that a well-selected supervised checkpoint matches or beats reinforcement learning on the task while costing more elsewhere.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
