# 2WikiMultiHopQA

<!-- auto:begin -->

A multi-hop question-answering set built so that answering requires composing facts across two Wikipedia articles, used in both sources as an in-domain companion to HotpotQA for search agents. It carries the largest relative movement of any benchmark in one of them — 51.9 F1 against 24.4 for retrieval-augmented prompting, a gap of 27.5 points, falling to 46.2 when the forward step reward is removed. In the other it is close between methods at the 7B scale (48.6 against 48.9 for the best baseline) and won outright at 3B, so the sources agree it responds strongly to step-level credit and disagree on which form of it wins.

- **Kind**: dataset
- **Also called**: 2Wiki, 2WikiMQA
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [Bamboogle](bamboogle.md), [Brumo](brumo.md), [credit assignment](../concepts/credit-assignment.md), [DAPO](../methods/dapo.md), [DAPO-Math-17k](dapo-math-17k.md), [E5-base-v2](../models/e5-base-v2.md), [expected calibration error](../concepts/expected-calibration-error.md), [GiGPO](../methods/gigpo.md), [GPT-5.5](../models/gpt-5-5.md), [GRPO](../methods/grpo.md), [HMMT](hmmt.md), [HotpotQA](hotpotqa.md), [multi-hop reasoning](../concepts/multi-hop-reasoning.md), [MuSiQue](musique.md), [Natural Questions](natural-questions.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [outcome reward](../concepts/outcome-reward.md), [PopQA](popqa.md), [PPO](../methods/ppo.md), [privileged information](../concepts/privileged-information.md), [process reward](../concepts/process-reward.md), [Qwen2.5-3B-Instruct](../models/qwen2-5-3b-instruct.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [Qwen3-8B](../models/qwen3-8b.md), [reasoning boundary](../concepts/reasoning-boundary.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [reward sparsity](../concepts/reward-sparsity.md), [search-augmented reasoning](../concepts/search-augmented-reasoning.md), [Search-R1](../methods/search-r1.md), [TriviaQA](triviaqa.md)

## Appears in

- [BiCAA: Bidirectional Credit Assignment for Search-Augmented Agent](../../archive/papers/2026/arxiv-2608-01321/summary.md) — Gives each retrieval step of a search agent a dense reward built from two ground-truth-conditioned signals — how much the step raised the model's likelihood of the correct answer, and how necessary the step looks in hindsight — and fuses them asymmetrically so that a step which helps locally but is redundant globally is discounted.
- [EviSD: Evidence-Conditioned Self-Distillation for Search-Augmented Agents](../../archive/papers/2026/arxiv-2608-01359/summary.md) — Re-scores a search agent's own sampled tokens under a teacher that has been shown the instance's supporting evidence, and uses the detached teacher-student gap to nudge the GRPO advantage up or down on search and answer tokens only, without adding a distillation loss or changing anything at inference.
- [Start Classifying: Categorical Critics for LLM Reinforcement Learning](../../archive/papers/2026/arxiv-2608-02181/summary.md) — Replaces PPO's scalar mean-squared-error critic head with a categorical predictor over a discretized value support trained by cross-entropy against Gaussian-smoothed targets, decodes it back to a scalar for an unchanged GAE update, and shows the resulting critic is better calibrated and produces near-symmetric advantages where the MSE critic penalizes failures two-to-three times harder than it rewards successes.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
