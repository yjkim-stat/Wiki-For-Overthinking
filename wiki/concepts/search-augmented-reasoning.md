# search-augmented reasoning

<!-- auto:begin -->

Interleaving generation with calls to an external retriever, so the model decides what to query, when to query again, and when it has enough to answer. Both sources treat it as a sequential decision process trained with reinforcement learning rather than as prompting, and both attack the same weakness: an outcome reward cannot say which retrieval mattered. One measures each step's contribution directly, by how much it raised the likelihood of the correct answer and how necessary it looks in hindsight; the other re-scores the agent's own tokens under a teacher shown the instance's supporting evidence. They also share an evaluation shape — three single-hop and four multi-hop QA sets, split into in-domain and held-out — and a common secondary claim, that better credit produces fewer and less redundant searches rather than more.

- **Kind**: concept
- **Also called**: agentic search, search agent, search-augmented QA
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [advantage estimation](advantage-estimation.md), [Bamboogle](../datasets/bamboogle.md), [credit assignment](credit-assignment.md), [GiGPO](../methods/gigpo.md), [GRPO](../methods/grpo.md), [HotpotQA](../datasets/hotpotqa.md), [multi-hop reasoning](multi-hop-reasoning.md), [MuSiQue](../datasets/musique.md), [Natural Questions](../datasets/natural-questions.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [outcome reward](outcome-reward.md), [PopQA](../datasets/popqa.md), [PPO](../methods/ppo.md), [privileged information](privileged-information.md), [process reward](process-reward.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [reward sparsity](reward-sparsity.md), [Search-R1](../methods/search-r1.md), [TriviaQA](../datasets/triviaqa.md)

## Appears in

- [BiCAA: Bidirectional Credit Assignment for Search-Augmented Agent](../../archive/papers/2026/arxiv-2608-01321/summary.md) — Gives each retrieval step of a search agent a dense reward built from two ground-truth-conditioned signals — how much the step raised the model's likelihood of the correct answer, and how necessary the step looks in hindsight — and fuses them asymmetrically so that a step which helps locally but is redundant globally is discounted.
- [EviSD: Evidence-Conditioned Self-Distillation for Search-Augmented Agents](../../archive/papers/2026/arxiv-2608-01359/summary.md) — Re-scores a search agent's own sampled tokens under a teacher that has been shown the instance's supporting evidence, and uses the detached teacher-student gap to nudge the GRPO advantage up or down on search and answer tokens only, without adding a distillation loss or changing anything at inference.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
