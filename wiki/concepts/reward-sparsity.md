# reward sparsity

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [advantage estimation](advantage-estimation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [Bamboogle](../datasets/bamboogle.md), [credit assignment](credit-assignment.md), [DAPO-Math-17k](../datasets/dapo-math-17k.md), [data efficiency](data-efficiency.md), [exploration](exploration.md), [GiGPO](../methods/gigpo.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [HotpotQA](../datasets/hotpotqa.md), [MATH-500](../datasets/math-500.md), [multi-hop reasoning](multi-hop-reasoning.md), [MuSiQue](../datasets/musique.md), [Natural Questions](../datasets/natural-questions.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [outcome reward](outcome-reward.md), [policy entropy](policy-entropy.md), [PopQA](../datasets/popqa.md), [post-hoc rationalization](post-hoc-rationalization.md), [PPO](../methods/ppo.md), [privileged information](privileged-information.md), [process reward](process-reward.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [search-augmented reasoning](search-augmented-reasoning.md), [Search-R1](../methods/search-r1.md), [TriviaQA](../datasets/triviaqa.md)

## Appears in

- [BiCAA: Bidirectional Credit Assignment for Search-Augmented Agent](../../archive/papers/2026/arxiv-2608-01321/summary.md) — Gives each retrieval step of a search agent a dense reward built from two ground-truth-conditioned signals — how much the step raised the model's likelihood of the correct answer, and how necessary the step looks in hindsight — and fuses them asymmetrically so that a step which helps locally but is redundant globally is discounted.
- [Self-Improving Large Language Models via Progressive Experience Evolution](../../archive/papers/2026/arxiv-2608-02139/summary.md) — Inserts a stage before RL in which the model extracts textual lessons from its own successful and failed rollouts, filters them by measured marginal utility on a held-out probe set, and distills the surviving pool into its own weights — so that GRPO starts from a policy that fails all-eight-samples less often.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
