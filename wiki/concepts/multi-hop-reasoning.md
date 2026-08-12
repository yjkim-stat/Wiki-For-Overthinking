# multi-hop reasoning

<!-- auto:begin -->

Answering a question that requires combining facts no single retrieved document contains, and in both sources the regime that separates step-level credit assignment from outcome-only training. The evidence for that is an ablation rather than a definition: removing a forward-looking per-step reward costs 5.9 F1 on HotpotQA, 5.7 on 2WikiMultiHopQA and 4.4 on MuSiQue while costing 0.9 on single-hop Natural Questions, so dense step supervision earns its keep exactly where a trajectory holds several decisions that jointly determine the answer. Both sources also split their evaluation tables into single-hop and multi-hop averages and report them separately, treating the distinction as the axis along which a search policy either generalizes or does not.

- **Kind**: concept
- **Also called**: multi-hop QA
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [advantage estimation](advantage-estimation.md), [Bamboogle](../datasets/bamboogle.md), [credit assignment](credit-assignment.md), [GiGPO](../methods/gigpo.md), [GRPO](../methods/grpo.md), [HotpotQA](../datasets/hotpotqa.md), [MuSiQue](../datasets/musique.md), [Natural Questions](../datasets/natural-questions.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [outcome reward](outcome-reward.md), [PopQA](../datasets/popqa.md), [PPO](../methods/ppo.md), [privileged information](privileged-information.md), [process reward](process-reward.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [reward sparsity](reward-sparsity.md), [search-augmented reasoning](search-augmented-reasoning.md), [Search-R1](../methods/search-r1.md), [TriviaQA](../datasets/triviaqa.md)

## Appears in

- [BiCAA: Bidirectional Credit Assignment for Search-Augmented Agent](../../archive/papers/2026/arxiv-2608-01321/summary.md) — Gives each retrieval step of a search agent a dense reward built from two ground-truth-conditioned signals — how much the step raised the model's likelihood of the correct answer, and how necessary the step looks in hindsight — and fuses them asymmetrically so that a step which helps locally but is redundant globally is discounted.
- [EviSD: Evidence-Conditioned Self-Distillation for Search-Augmented Agents](../../archive/papers/2026/arxiv-2608-01359/summary.md) — Re-scores a search agent's own sampled tokens under a teacher that has been shown the instance's supporting evidence, and uses the detached teacher-student gap to nudge the GRPO advantage up or down on search and answer tokens only, without adding a distillation loss or changing anything at inference.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
