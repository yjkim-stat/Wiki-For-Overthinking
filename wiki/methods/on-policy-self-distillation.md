# on-policy self-distillation

<!-- auto:begin -->

Querying a privileged teacher at prefixes the student actually visits, so that sparse outcome rewards are replaced by dense token-level distributional supervision on the student's own rollouts. Three sources form a family that agrees on the mechanism and differs on how to weight it. One aggregates token-level teacher-student log-probability gaps into turn-level evidence via a recursive Bayesian belief update, identifying pivotal turns by marginal belief revision. One gates backward multi-step aggregation on how each local divergence compares to the sequence mean, arguing that equal magnitudes following different histories should not be weighted equally. One concentrates distillation on reasoning pivots located by the teacher's distributional shift when an English reference solution is added or removed. Three variants appearing together is evidence the approach is consolidating into a named subfield.

- **Kind**: method
- **Also called**: OPSD, on-policy distillation, privileged self-distillation
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 4

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [advantage estimation](../concepts/advantage-estimation.md), [Bamboogle](../datasets/bamboogle.md), [belief state](../concepts/belief-state.md), [credit assignment](../concepts/credit-assignment.md), [GiGPO](gigpo.md), [GRPO](grpo.md), [HotpotQA](../datasets/hotpotqa.md), [long-horizon reasoning](../concepts/long-horizon-reasoning.md), [multi-hop reasoning](../concepts/multi-hop-reasoning.md), [MuSiQue](../datasets/musique.md), [Natural Questions](../datasets/natural-questions.md), [outcome reward](../concepts/outcome-reward.md), [PopQA](../datasets/popqa.md), [privileged information](../concepts/privileged-information.md), [process supervision](../concepts/process-supervision.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [RLVR](rlvr.md), [search-augmented reasoning](../concepts/search-augmented-reasoning.md), [Search-R1](search-r1.md), [token-level distillation](token-level-distillation.md), [token selection](../concepts/token-selection.md), [TriviaQA](../datasets/triviaqa.md)

## Appears in

- [EviSD: Evidence-Conditioned Self-Distillation for Search-Augmented Agents](../../archive/papers/2026/arxiv-2608-01359/summary.md) — Re-scores a search agent's own sampled tokens under a teacher that has been shown the instance's supporting evidence, and uses the detached teacher-student gap to nudge the GRPO advantage up or down on search and answer tokens only, without adding a distillation loss or changing anything at inference.
- [AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning](../../archive/papers/2026/arxiv-2608-05987/summary.md) — Turns token-level teacher-student log-probability gaps into turn-level credit for agentic RL by recursively updating a Bayesian belief in log-odds space, identifying pivotal turns without a critic.
- [DASH: Divergence-Adaptive Supervision Horizons for On-Policy Self-Distillation of Reasoning Models](../../archive/papers/2026/arxiv-2608-06243/summary.md) — Weights on-policy self-distillation supervision by how each local teacher-student divergence compares to the sequence mean, gating backward multi-step aggregation on that comparison.
- [RP-OPSD: Reasoning-Pivot-Guided On-Policy Self-Distillation for Multilingual Reasoning Transfer](../../archive/papers/2026/arxiv-2608-06347/summary.md) — Concentrates privileged self-distillation on reasoning pivots identified by the teacher's distributional shift when an English reference solution is added or removed, for multilingual reasoning transfer.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
