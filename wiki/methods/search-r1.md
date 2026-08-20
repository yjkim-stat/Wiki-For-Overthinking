# Search-R1

<!-- auto:begin -->

A reinforcement-learning-trained search agent that interleaves retrieval with reasoning, used across 3 sources as the standard baseline for the archive's search-agent credit-assignment work. Its role is comparative: methods adding turn-level or evidence-conditioned signal report margins of 1.3 to 3.9 average exact-match points over it, and the archive's standing caution about those margins applies -- single evaluation runs, no seeds, and macro averages that hide per-benchmark losses.

- **Kind**: method
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [advantage estimation](../concepts/advantage-estimation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [Bamboogle](../datasets/bamboogle.md), [Brumo](../datasets/brumo.md), [credit assignment](../concepts/credit-assignment.md), [DAPO](dapo.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [dense retrieval](dense-retrieval.md), [E5-base-v2](../models/e5-base-v2.md), [expected calibration error](expected-calibration-error.md), [GiGPO](gigpo.md), [GPT-5.5](../models/gpt-5-5.md), [GRPO](grpo.md), [HMMT](../datasets/hmmt.md), [HotpotQA](../datasets/hotpotqa.md), [multi-hop reasoning](../concepts/multi-hop-reasoning.md), [MuSiQue](../datasets/musique.md), [Natural Questions](../datasets/natural-questions.md), [on-policy self-distillation](on-policy-self-distillation.md), [outcome reward](../concepts/outcome-reward.md), [PopQA](../datasets/popqa.md), [PPO](ppo.md), [privileged information](../concepts/privileged-information.md), [process reward](../concepts/process-reward.md), [Qwen2.5-3B-Instruct](../models/qwen2-5-3b-instruct.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [Qwen3-8B](../models/qwen3-8b.md), [reasoning boundary](../concepts/reasoning-boundary.md), [retrieval-augmented generation](retrieval-augmented-generation.md), [reward sparsity](../concepts/reward-sparsity.md), [search-augmented reasoning](../concepts/search-augmented-reasoning.md), [teacher-student gap](../concepts/teacher-student-gap.md), [TriviaQA](../datasets/triviaqa.md)

## Appears in

- [BiCAA: Bidirectional Credit Assignment for Search-Augmented Agent](../../archive/papers/2026/arxiv-2608-01321/summary.md) — Gives each retrieval step of a search agent a dense reward built from two ground-truth-conditioned signals — how much the step raised the model's likelihood of the correct answer, and how necessary the step looks in hindsight — and fuses them asymmetrically so that a step which helps locally but is redundant globally is discounted.
- [EviSD: Evidence-Conditioned Self-Distillation for Search-Augmented Agents](../../archive/papers/2026/arxiv-2608-01359/summary.md) — Re-scores a search agent's own sampled tokens under a teacher that has been shown the instance's supporting evidence, and uses the detached teacher-student gap to nudge the GRPO advantage up or down on search and answer tokens only, without adding a distillation loss or changing anything at inference.
- [Start Classifying: Categorical Critics for LLM Reinforcement Learning](../../archive/papers/2026/arxiv-2608-02181/summary.md) — Replaces PPO's scalar mean-squared-error critic head with a categorical predictor over a discretized value support trained by cross-entropy against Gaussian-smoothed targets, decodes it back to a scalar for an unchanged GAE update, and shows the resulting critic is better calibrated and produces near-symmetric advantages where the MSE critic penalizes failures two-to-three times harder than it rewards successes.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
