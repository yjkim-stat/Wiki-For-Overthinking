# MuSiQue

<!-- auto:begin -->

A multi-hop question-answering set constructed by composing single-hop questions, used by both sources as held-out evaluation and in both the hardest of their seven benchmarks by absolute score. One reaches 28.6 F1 on it against 8.5 for chain-of-thought prompting and 10.0 with retrieval added, and finds it among the sets most damaged when step-level reward is removed (28.6 down to 24.2). The other reports 21.6 EM while a competing method reaches 23.6, making it one of the benchmarks where its macro-average lead does not hold. Its role here is as the floor: where the other multi-hop sets run in the fifties and seventies, methods on this one sit in the twenties.

- **Kind**: dataset
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [2WikiMultiHopQA](2wikimultihopqa.md), [advantage estimation](../concepts/advantage-estimation.md), [Bamboogle](bamboogle.md), [credit assignment](../concepts/credit-assignment.md), [GiGPO](../methods/gigpo.md), [GRPO](../methods/grpo.md), [HotpotQA](hotpotqa.md), [multi-hop reasoning](../concepts/multi-hop-reasoning.md), [Natural Questions](natural-questions.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [outcome reward](../concepts/outcome-reward.md), [PopQA](popqa.md), [PPO](../methods/ppo.md), [privileged information](../concepts/privileged-information.md), [process reward](../concepts/process-reward.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [search-augmented reasoning](../concepts/search-augmented-reasoning.md), [Search-R1](../methods/search-r1.md), [TriviaQA](triviaqa.md)

## Appears in

- [BiCAA: Bidirectional Credit Assignment for Search-Augmented Agent](../../archive/papers/2026/arxiv-2608-01321/summary.md) — Gives each retrieval step of a search agent a dense reward built from two ground-truth-conditioned signals — how much the step raised the model's likelihood of the correct answer, and how necessary the step looks in hindsight — and fuses them asymmetrically so that a step which helps locally but is redundant globally is discounted.
- [EviSD: Evidence-Conditioned Self-Distillation for Search-Augmented Agents](../../archive/papers/2026/arxiv-2608-01359/summary.md) — Re-scores a search agent's own sampled tokens under a teacher that has been shown the instance's supporting evidence, and uses the detached teacher-student gap to nudge the GRPO advantage up or down on search and answer tokens only, without adding a distillation loss or changing anything at inference.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
