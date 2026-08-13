# privileged information

<!-- auto:begin -->

Information available to a teacher during training that the student will not have at inference, used by all three sources as the source of dense supervision that outcome rewards cannot provide. In two cases the privilege is the teacher's own distribution over the student's visited prefixes; in the third it is an English reference solution, where the shift between teacher views with and without it locates the tokens the reference decides. The common structure is that privilege makes an otherwise unavailable signal computable without labels, and the common cost is that a teacher must exist — none of the three methods applies where one does not.

- **Kind**: concept
- **Also called**: privileged teacher, teacher-side information
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 5

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [advantage estimation](advantage-estimation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [Bamboogle](../datasets/bamboogle.md), [belief state](belief-state.md), [credit assignment](credit-assignment.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [data efficiency](data-efficiency.md), [E5-base-v2](../models/e5-base-v2.md), [exploration](exploration.md), [GiGPO](../methods/gigpo.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [HotpotQA](../datasets/hotpotqa.md), [knowledge distillation](../methods/knowledge-distillation.md), [long-horizon reasoning](long-horizon-reasoning.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [multi-hop reasoning](multi-hop-reasoning.md), [MuSiQue](../datasets/musique.md), [Natural Questions](../datasets/natural-questions.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [outcome reward](outcome-reward.md), [policy entropy](policy-entropy.md), [PopQA](../datasets/popqa.md), [post-hoc rationalization](post-hoc-rationalization.md), [process supervision](process-supervision.md), [Qwen2.5-3B-Instruct](../models/qwen2-5-3b-instruct.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-1.7B-Base](../models/qwen3-1-7b-base.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [Qwen3-8B-Base](../models/qwen3-8b-base.md), [reward sparsity](reward-sparsity.md), [RLVR](../methods/rlvr.md), [search-augmented reasoning](search-augmented-reasoning.md), [Search-R1](../methods/search-r1.md), [token-level distillation](../methods/token-level-distillation.md), [token selection](token-selection.md), [TriviaQA](../datasets/triviaqa.md)

## Appears in

- [EviSD: Evidence-Conditioned Self-Distillation for Search-Augmented Agents](../../archive/papers/2026/arxiv-2608-01359/summary.md) — Re-scores a search agent's own sampled tokens under a teacher that has been shown the instance's supporting evidence, and uses the detached teacher-student gap to nudge the GRPO advantage up or down on search and answer tokens only, without adding a distillation loss or changing anything at inference.
- [Self-Improving Large Language Models via Progressive Experience Evolution](../../archive/papers/2026/arxiv-2608-02139/summary.md) — Inserts a stage before RL in which the model extracts textual lessons from its own successful and failed rollouts, filters them by measured marginal utility on a held-out probe set, and distills the surviving pool into its own weights — so that GRPO starts from a policy that fails all-eight-samples less often.
- [AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning](../../archive/papers/2026/arxiv-2608-05987/summary.md) — Turns token-level teacher-student log-probability gaps into turn-level credit for agentic RL by recursively updating a Bayesian belief in log-odds space, identifying pivotal turns without a critic.
- [DASH: Divergence-Adaptive Supervision Horizons for On-Policy Self-Distillation of Reasoning Models](../../archive/papers/2026/arxiv-2608-06243/summary.md) — Weights on-policy self-distillation supervision by how each local teacher-student divergence compares to the sequence mean, gating backward multi-step aggregation on that comparison.
- [RP-OPSD: Reasoning-Pivot-Guided On-Policy Self-Distillation for Multilingual Reasoning Transfer](../../archive/papers/2026/arxiv-2608-06347/summary.md) — Concentrates privileged self-distillation on reasoning pivots identified by the teacher's distributional shift when an English reference solution is added or removed, for multilingual reasoning transfer.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
