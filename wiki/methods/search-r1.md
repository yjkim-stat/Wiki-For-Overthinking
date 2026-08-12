# Search-R1

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [advantage estimation](../concepts/advantage-estimation.md), [Bamboogle](../datasets/bamboogle.md), [credit assignment](../concepts/credit-assignment.md), [GiGPO](gigpo.md), [GRPO](grpo.md), [HotpotQA](../datasets/hotpotqa.md), [multi-hop reasoning](../concepts/multi-hop-reasoning.md), [MuSiQue](../datasets/musique.md), [Natural Questions](../datasets/natural-questions.md), [on-policy self-distillation](on-policy-self-distillation.md), [outcome reward](../concepts/outcome-reward.md), [PopQA](../datasets/popqa.md), [PPO](ppo.md), [privileged information](../concepts/privileged-information.md), [process reward](../concepts/process-reward.md), [retrieval-augmented generation](retrieval-augmented-generation.md), [reward sparsity](../concepts/reward-sparsity.md), [search-augmented reasoning](../concepts/search-augmented-reasoning.md), [TriviaQA](../datasets/triviaqa.md)

## Appears in

- [BiCAA: Bidirectional Credit Assignment for Search-Augmented Agent](../../archive/papers/2026/arxiv-2608-01321/summary.md) — Gives each retrieval step of a search agent a dense reward built from two ground-truth-conditioned signals — how much the step raised the model's likelihood of the correct answer, and how necessary the step looks in hindsight — and fuses them asymmetrically so that a step which helps locally but is redundant globally is discounted.
- [EviSD: Evidence-Conditioned Self-Distillation for Search-Augmented Agents](../../archive/papers/2026/arxiv-2608-01359/summary.md) — Re-scores a search agent's own sampled tokens under a teacher that has been shown the instance's supporting evidence, and uses the detached teacher-student gap to nudge the GRPO advantage up or down on search and answer tokens only, without adding a distillation loss or changing anything at inference.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
