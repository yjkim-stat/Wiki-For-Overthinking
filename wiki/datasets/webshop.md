# WebShop

<!-- auto:begin -->

A simulated web-shopping environment in which an agent searches, browses and selects a product matching a natural-language instruction, scored on how well the purchase matches the specification. Both sources use it as one of the multi-turn environments for agentic reinforcement learning, paired with ALFWorld and a search-based question-answering task, because its episodes are long enough that turn-level credit assignment is a real question. Neither describes its construction. What the archive should carry from these two is that it behaves differently from ALFWorld under the same method -- gains do not transfer between them, and the recursive self-distillation work reaches 89.1 percent on ALFWorld while reporting a far narrower margin here -- so a method demonstrated on one of the two has not been demonstrated on multi-turn agency in general.

- **Kind**: dataset
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [ALFWorld](alfworld.md), [belief state](../concepts/belief-state.md), [component ablation](../methods/component-ablation.md), [credit assignment](../concepts/credit-assignment.md), [GRPO](../methods/grpo.md), [hindsight](../concepts/hindsight.md), [long-horizon reasoning](../concepts/long-horizon-reasoning.md), [multi-agent pipeline](../concepts/multi-agent-pipeline.md), [on-policy distillation](../methods/on-policy-distillation.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [outcome reward](../concepts/outcome-reward.md), [privileged information](../concepts/privileged-information.md), [process reward](../concepts/process-reward.md), [process supervision](../concepts/process-supervision.md), [Qwen2.5-3B](../models/qwen2-5-3b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [RLVR](../methods/rlvr.md), [selectivity control](../methods/selectivity-control.md), [teacher-student gap](../concepts/teacher-student-gap.md), [token-level distillation](../methods/token-level-distillation.md)

## Appears in

- [AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning](../../archive/papers/2026/arxiv-2608-05987/summary.md) — Turns token-level teacher-student log-probability gaps into turn-level credit for agentic RL by recursively updating a Bayesian belief in log-odds space, identifying pivotal turns without a critic.
- [Trajectory-Relative Hindsight Distillation for Agentic Reinforcement Learning](../../archive/papers/2026/arxiv-2608-07371/summary.md) — Distributes hindsight supervision across the turns of an agent trajectory by comparing each turn's share of total revision magnitude against its share of eligible tokens, holding the average multiplier at one so the total supervision is fixed and only its allocation changes -- and isolates that allocation with a permutation control that keeps the multiplier values and scrambles which turn receives which.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
