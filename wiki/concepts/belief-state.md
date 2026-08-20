# belief state

<!-- auto:begin -->

A maintained estimate of an unobserved variable, updated as evidence arrives, appearing across 3 sources in three different mechanisms. In agentic credit assignment it is a Bayesian belief over which turn was pivotal, updated recursively in log-odds space from token-level teacher-student gaps, which identifies pivotal turns without a critic. In planning it is a filter over per-device latent parameters, reduced from about 0.31 to 0.044 uncertainty across a test with most of the information gained in the first 30 epochs. And in language modelling it is a hierarchical latent predicted several steps ahead. The common shape worth recording is that a belief state converts a sparse terminal observation into a dense per-step quantity without requiring a learned value function -- which is the same job a critic does, done by inference rather than by regression.

- **Kind**: concept
- **Also called**: belief, state representation
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [ALFWorld](../datasets/alfworld.md), [compounding error](compounding-error.md), [compute allocation](compute-allocation.md), [credit assignment](credit-assignment.md), [GRPO](../methods/grpo.md), [implicit reasoning](implicit-reasoning.md), [latent reasoning](latent-reasoning.md), [long-horizon reasoning](long-horizon-reasoning.md), [Monte Carlo tree search](../methods/monte-carlo-tree-search.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [privileged information](privileged-information.md), [process supervision](process-supervision.md), [Qwen2.5-3B](../models/qwen2-5-3b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [reward shaping](../methods/reward-shaping.md), [RLVR](../methods/rlvr.md), [speculative decoding](../methods/speculative-decoding.md), [teacher forcing](../methods/teacher-forcing.md), [token-level distillation](../methods/token-level-distillation.md), [WebShop](../datasets/webshop.md)

## Appears in

- [Hierarchical Latent Prediction for Language Models](../../archive/papers/2026/arxiv-2608-05806/summary.md) — Adds a higher-level abstract latent as an auxiliary pretraining target to reduce compounding error in latent-space rollouts, aiming at longer-horizon coherence than multi-token or next-latent prediction.
- [AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning](../../archive/papers/2026/arxiv-2608-05987/summary.md) — Turns token-level teacher-student log-probability gaps into turn-level credit for agentic RL by recursively updating a Bayesian belief in log-odds space, identifying pivotal turns without a critic.
- [Adaptive Sequential Test Planning for Multi-Mechanism Reliability Qualification via Bayesian Monte Carlo Tree Search](../../archive/papers/2026/arxiv-2608-09622/summary.md) — Plans semiconductor reliability stress tests as a partially observable sequential decision problem, using Monte Carlo tree search over a seed-action simulator with an extended Kalman filter tracking per-device latent degradation parameters, so each device's test adapts to its own measured behaviour rather than to a population model.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
