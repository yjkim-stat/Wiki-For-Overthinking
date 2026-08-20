# token-level distillation

<!-- auto:begin -->

Supervising a student on the teacher's full distribution at each token rather than on a sequence-level outcome, which both sources use as the density source that turns sparse rewards into per-token signal. They then disagree about what to do with that density. One aggregates the token-level teacher-student log-probability gaps upward into turn-level evidence, on the view that the useful unit in agentic tasks is the turn. The other keeps the token unit but reweights it, concentrating supervision on tokens whose distribution shifts when a reference solution is supplied. Both derive the signal from distributions the training loop already computes, so neither needs an extra forward pass.

- **Kind**: method
- **Also called**: distributional distillation, token-level supervision
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [ALFWorld](../datasets/alfworld.md), [belief state](../concepts/belief-state.md), [credit assignment](../concepts/credit-assignment.md), [cross-lingual transfer](../concepts/cross-lingual-transfer.md), [GRPO](grpo.md), [long-horizon reasoning](../concepts/long-horizon-reasoning.md), [on-policy self-distillation](on-policy-self-distillation.md), [privileged information](../concepts/privileged-information.md), [process supervision](../concepts/process-supervision.md), [Qwen2.5-3B](../models/qwen2-5-3b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [RLVR](rlvr.md), [token selection](token-selection.md), [WebShop](../datasets/webshop.md)

## Appears in

- [AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning](../../archive/papers/2026/arxiv-2608-05987/summary.md) — Turns token-level teacher-student log-probability gaps into turn-level credit for agentic RL by recursively updating a Bayesian belief in log-odds space, identifying pivotal turns without a critic.
- [RP-OPSD: Reasoning-Pivot-Guided On-Policy Self-Distillation for Multilingual Reasoning Transfer](../../archive/papers/2026/arxiv-2608-06347/summary.md) — Concentrates privileged self-distillation on reasoning pivots identified by the teacher's distributional shift when an English reference solution is added or removed, for multilingual reasoning transfer.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
