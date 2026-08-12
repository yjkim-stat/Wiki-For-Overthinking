# privileged information

<!-- auto:begin -->

Information available to a teacher during training that the student will not have at inference, used by all three sources as the source of dense supervision that outcome rewards cannot provide. In two cases the privilege is the teacher's own distribution over the student's visited prefixes; in the third it is an English reference solution, where the shift between teacher views with and without it locates the tokens the reference decides. The common structure is that privilege makes an otherwise unavailable signal computable without labels, and the common cost is that a teacher must exist — none of the three methods applies where one does not.

- **Kind**: concept
- **Also called**: privileged teacher, teacher-side information
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [belief state](belief-state.md), [credit assignment](credit-assignment.md), [GRPO](../methods/grpo.md), [long-horizon reasoning](long-horizon-reasoning.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [process supervision](process-supervision.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [RLVR](../methods/rlvr.md), [token-level distillation](../methods/token-level-distillation.md), [token selection](token-selection.md)

## Appears in

- [AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning](../../archive/papers/2026/arxiv-2608-05987/summary.md) — Turns token-level teacher-student log-probability gaps into turn-level credit for agentic RL by recursively updating a Bayesian belief in log-odds space, identifying pivotal turns without a critic.
- [DASH: Divergence-Adaptive Supervision Horizons for On-Policy Self-Distillation of Reasoning Models](../../archive/papers/2026/arxiv-2608-06243/summary.md) — Weights on-policy self-distillation supervision by how each local teacher-student divergence compares to the sequence mean, gating backward multi-step aggregation on that comparison.
- [RP-OPSD: Reasoning-Pivot-Guided On-Policy Self-Distillation for Multilingual Reasoning Transfer](../../archive/papers/2026/arxiv-2608-06347/summary.md) — Concentrates privileged self-distillation on reasoning pivots identified by the teacher's distributional shift when an English reference solution is added or removed, for multilingual reasoning transfer.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
