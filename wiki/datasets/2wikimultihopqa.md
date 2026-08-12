# 2WikiMultiHopQA

<!-- auto:begin -->

A multi-hop question-answering set built so that answering requires composing facts across two Wikipedia articles, used in both sources as an in-domain companion to HotpotQA for search agents. It carries the largest relative movement of any benchmark in one of them — 51.9 F1 against 24.4 for retrieval-augmented prompting, a gap of 27.5 points, falling to 46.2 when the forward step reward is removed. In the other it is close between methods at the 7B scale (48.6 against 48.9 for the best baseline) and won outright at 3B, so the sources agree it responds strongly to step-level credit and disagree on which form of it wins.

- **Kind**: dataset
- **Also called**: 2Wiki, 2WikiMQA
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [Bamboogle](bamboogle.md), [credit assignment](../concepts/credit-assignment.md), [GiGPO](../methods/gigpo.md), [GRPO](../methods/grpo.md), [HotpotQA](hotpotqa.md), [multi-hop reasoning](../concepts/multi-hop-reasoning.md), [MuSiQue](musique.md), [Natural Questions](natural-questions.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [outcome reward](../concepts/outcome-reward.md), [PopQA](popqa.md), [PPO](../methods/ppo.md), [privileged information](../concepts/privileged-information.md), [process reward](../concepts/process-reward.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [search-augmented reasoning](../concepts/search-augmented-reasoning.md), [Search-R1](../methods/search-r1.md), [TriviaQA](triviaqa.md)

## Appears in

- [BiCAA: Bidirectional Credit Assignment for Search-Augmented Agent](../../archive/papers/2026/arxiv-2608-01321/summary.md) — Gives each retrieval step of a search agent a dense reward built from two ground-truth-conditioned signals — how much the step raised the model's likelihood of the correct answer, and how necessary the step looks in hindsight — and fuses them asymmetrically so that a step which helps locally but is redundant globally is discounted.
- [EviSD: Evidence-Conditioned Self-Distillation for Search-Augmented Agents](../../archive/papers/2026/arxiv-2608-01359/summary.md) — Re-scores a search agent's own sampled tokens under a teacher that has been shown the instance's supporting evidence, and uses the detached teacher-student gap to nudge the GRPO advantage up or down on search and answer tokens only, without adding a distillation loss or changing anything at inference.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
