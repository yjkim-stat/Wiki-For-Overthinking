# belief state

<!-- auto:begin -->

A running internal summary of what has been established so far, used by both sources as the object that long-horizon reasoning must maintain. They apply it at different levels. One makes it a pretraining target, adding a higher-level abstract latent so that latent-space rollouts accumulate less error and belief-state representations stay coherent over longer horizons. The other makes it explicit and Bayesian, aggregating token-level teacher-student log-probability gaps into turn-level evidence and updating a belief in log-odds space, where the marginal revision between consecutive states identifies which turn mattered. The shared claim is that a scalar per step is not enough and the history has to be carried.

- **Kind**: concept
- **Also called**: belief, state representation
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [compounding error](compounding-error.md), [credit assignment](credit-assignment.md), [GRPO](../methods/grpo.md), [implicit reasoning](implicit-reasoning.md), [latent reasoning](latent-reasoning.md), [long-horizon reasoning](long-horizon-reasoning.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [privileged information](privileged-information.md), [process supervision](process-supervision.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [RLVR](../methods/rlvr.md), [speculative decoding](../methods/speculative-decoding.md), [teacher forcing](../methods/teacher-forcing.md), [token-level distillation](../methods/token-level-distillation.md)

## Appears in

- [Hierarchical Latent Prediction for Language Models](../../archive/papers/2026/arxiv-2608-05806/summary.md) — Adds a higher-level abstract latent as an auxiliary pretraining target to reduce compounding error in latent-space rollouts, aiming at longer-horizon coherence than multi-token or next-latent prediction.
- [AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning](../../archive/papers/2026/arxiv-2608-05987/summary.md) — Turns token-level teacher-student log-probability gaps into turn-level credit for agentic RL by recursively updating a Bayesian belief in log-odds space, identifying pivotal turns without a critic.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
