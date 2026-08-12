# Natural Questions

<!-- auto:begin -->

A question-answering set drawn from real search queries, answerable from a single passage, used by both sources as in-domain data and — more load-bearing than that — as the control their multi-hop claims are read against. Removing the forward-looking step reward in one costs 0.9 F1 here against 5.9 on HotpotQA, and that contrast is what localizes the benefit of dense per-step supervision to trajectories with several decisions rather than to search agents generally. The other reports it among the sets where its method is not best (48.9 EM against 49.5 for a rollout-conditioned baseline) while still leading the seven-benchmark average.

- **Kind**: dataset
- **Also called**: NQ
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [2WikiMultiHopQA](2wikimultihopqa.md), [advantage estimation](../concepts/advantage-estimation.md), [Bamboogle](bamboogle.md), [credit assignment](../concepts/credit-assignment.md), [GiGPO](../methods/gigpo.md), [GRPO](../methods/grpo.md), [HotpotQA](hotpotqa.md), [multi-hop reasoning](../concepts/multi-hop-reasoning.md), [MuSiQue](musique.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [outcome reward](../concepts/outcome-reward.md), [PopQA](popqa.md), [PPO](../methods/ppo.md), [privileged information](../concepts/privileged-information.md), [process reward](../concepts/process-reward.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [search-augmented reasoning](../concepts/search-augmented-reasoning.md), [Search-R1](../methods/search-r1.md), [TriviaQA](triviaqa.md)

## Appears in

- [BiCAA: Bidirectional Credit Assignment for Search-Augmented Agent](../../archive/papers/2026/arxiv-2608-01321/summary.md) — Gives each retrieval step of a search agent a dense reward built from two ground-truth-conditioned signals — how much the step raised the model's likelihood of the correct answer, and how necessary the step looks in hindsight — and fuses them asymmetrically so that a step which helps locally but is redundant globally is discounted.
- [EviSD: Evidence-Conditioned Self-Distillation for Search-Augmented Agents](../../archive/papers/2026/arxiv-2608-01359/summary.md) — Re-scores a search agent's own sampled tokens under a teacher that has been shown the instance's supporting evidence, and uses the detached teacher-student gap to nudge the GRPO advantage up or down on search and answer tokens only, without adding a distillation loss or changing anything at inference.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
