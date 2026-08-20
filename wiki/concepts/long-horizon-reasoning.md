# long-horizon reasoning

<!-- auto:begin -->

Reasoning over many dependent steps where an early decision determines much later outcomes, which both sources treat as the regime where standard methods break down. One shows trajectory-level advantage estimates fail to credit the few pivotal decisions that determine multi-turn agentic outcomes, and recovers turn-level credit by recursively updating a belief in log-odds space. The other supplies an absolute measurement, using chess to require strategic reasoning, rule adherence and state tracking at once, and finding no model beats a human-amateur-level engine while some lose to random play. The shared point is that competence on single steps does not compose over a long horizon.

- **Kind**: concept
- **Also called**: long-horizon planning, multi-step horizon
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [ALFWorld](../datasets/alfworld.md), [belief state](belief-state.md), [construct validity](construct-validity.md), [credit assignment](credit-assignment.md), [GRPO](../methods/grpo.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [pattern recognition versus reasoning](pattern-recognition-versus-reasoning.md), [privileged information](privileged-information.md), [process supervision](process-supervision.md), [Qwen2.5-3B](../models/qwen2-5-3b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen3-8B](../models/qwen3-8b.md), [RLVR](../methods/rlvr.md), [state tracking](state-tracking.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [token-level distillation](../methods/token-level-distillation.md), [WebShop](../datasets/webshop.md)

## Appears in

- [AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning](../../archive/papers/2026/arxiv-2608-05987/summary.md) — Turns token-level teacher-student log-probability gaps into turn-level credit for agentic RL by recursively updating a Bayesian belief in log-odds space, identifying pivotal turns without a critic.
- [ChessArena: A Chess Testbed for Evaluating Strategic Reasoning Capabilities of Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-360/summary.md) — A competitive chess testbed where 13 models play each other, and no model beats a human-amateur-level engine while some lose to random play.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
