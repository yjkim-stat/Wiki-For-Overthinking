# ALFWorld

<!-- auto:begin -->

A text-based interactive environment in which an agent completes household tasks through discrete actions over multiple turns, split into seen and unseen validation sets and decomposable into six task families. Across 3 sources it is the archive's default embodied benchmark for multi-turn credit assignment, and its value is that per-family and per-split results are available -- one source reports the full six-family matrix, making visible that individual families move by ten or more points between methods in directions the aggregate does not follow. It is also where the archive's largest single agent result sits: a diagnosis-guided recovery harness reaching 91.94 percent macro against a base 40.13 and 52.24 for the strongest prompt-adaptation baseline, with the matched-information rerun showing the gain belongs to a ranked recovery operator rather than to the action restriction or the diagnosis alone.

- **Kind**: dataset
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [advantage estimation](../concepts/advantage-estimation.md), [belief state](../concepts/belief-state.md), [component ablation](../methods/component-ablation.md), [compute allocation](../concepts/compute-allocation.md), [credit assignment](../concepts/credit-assignment.md), [DeepSeek-V4-Flash](../models/deepseek-v4-flash.md), [GRPO](../methods/grpo.md), [hindsight](../concepts/hindsight.md), [in-context learning](../concepts/in-context-learning.md), [long-horizon agency](../concepts/long-horizon-agency.md), [long-horizon reasoning](../concepts/long-horizon-reasoning.md), [multi-agent pipeline](../concepts/multi-agent-pipeline.md), [on-policy distillation](../methods/on-policy-distillation.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [outcome reward](../concepts/outcome-reward.md), [privileged information](../concepts/privileged-information.md), [process reward](../concepts/process-reward.md), [process supervision](../concepts/process-supervision.md), [Qwen2.5-3B](../models/qwen2-5-3b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3.5-27B](../models/qwen3-5-27b.md), [Qwen3.6-27B](../models/qwen3-6-27b.md), [Qwen3-8B](../models/qwen3-8b.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [RLVR](../methods/rlvr.md), [selective prediction](../concepts/selective-prediction.md), [selectivity control](../methods/selectivity-control.md), [self-correction](../concepts/self-correction.md), [teacher-student gap](../concepts/teacher-student-gap.md), [token-level distillation](../methods/token-level-distillation.md), [tool orchestration](../concepts/tool-orchestration.md), [WebShop](webshop.md)

## Appears in

- [AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning](../../archive/papers/2026/arxiv-2608-05987/summary.md) — Turns token-level teacher-student log-probability gaps into turn-level credit for agentic RL by recursively updating a Bayesian belief in log-odds space, identifying pivotal turns without a critic.
- [Trajectory-Relative Hindsight Distillation for Agentic Reinforcement Learning](../../archive/papers/2026/arxiv-2608-07371/summary.md) — Distributes hindsight supervision across the turns of an agent trajectory by comparing each turn's share of total revision magnitude against its share of eligible tokens, holding the average multiplier at one so the total supervision is fixed and only its allocation changes -- and isolates that allocation with a permutation control that keeps the multiplier values and scrambles which turn receives which.
- [Diagnosis Before Recovery: Turning Agent Failures into Selective Self-Correction](../../archive/papers/2026/arxiv-2608-11772/summary.md) — Profiles the dominant failure mode of an agent task family on development data, then freezes a policy that permits only the recovery interventions matched to that failure -- so a failure decides which repair is admissible and how much evidence to spend, rather than triggering more context indiscriminately.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
