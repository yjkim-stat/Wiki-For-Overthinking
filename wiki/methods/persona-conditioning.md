# persona conditioning

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [best-of-n](best-of-n.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [Claude Haiku 4.5](../models/claude-haiku-4-5.md), [Claude Sonnet 4.6](../models/claude-sonnet-4-6.md), [consensus](../concepts/consensus.md), [credit assignment](../concepts/credit-assignment.md), [GRPO](grpo.md), [GSPO](gspo.md), [jury aggregation](jury-aggregation.md), [length control](length-control.md), [length penalty](length-penalty.md), [LLM-as-a-judge](llm-as-a-judge.md), [majority voting](majority-voting.md), [multi-agent pipeline](multi-agent-pipeline.md), [outcome reward](../concepts/outcome-reward.md), [prompt sensitivity](../concepts/prompt-sensitivity.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [reasoning collapse](../concepts/reasoning-collapse.md), [reward hacking](../concepts/reward-hacking.md), [reward shaping](../concepts/reward-shaping.md), [RLVR](rlvr.md), [self-consistency](self-consistency.md), [test-time scaling](../concepts/test-time-scaling.md)

## Appears in

- [LLM Reasoning for Subjective Tasks: Failure Modes, Mitigation, and Dynamic Reasoning Routing](../../archive/papers/2026/arxiv-2608-08889/summary.md) — Shows on four internal Netflix verification tasks that explicit reasoning usually degrades subjective judgement, that applying RLVR to fix it makes the policy abandon deliberation for short heuristic guessing, and that a length bonus gated on answer correctness is what stops the collapse.
- [Social Chain of Thought: A Multi-Agent Architecture Grounded in Medical Differential Diagnosis Methodology](../../archive/papers/2026/arxiv-2608-11420/summary.md) — Structures multi-agent medical differential diagnosis as rounds of persona-conditioned specialist deliberation, and shows the recall advantage is not reproduced by best-of-n sampling from the same model, concentrates entirely in the cases where monolithic inference fails, and reverses on the easiest quartile.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
