# expected calibration error

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [advantage estimation](../concepts/advantage-estimation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [answer stabilization](../concepts/answer-stabilization.md), [Bamboogle](../datasets/bamboogle.md), [Brumo](../datasets/brumo.md), [calibration](calibration.md), [DAPO](dapo.md), [DAPO-Math-17k](../datasets/dapo-math-17k.md), [GRPO](grpo.md), [HotpotQA](../datasets/hotpotqa.md), [MuSiQue](../datasets/musique.md), [Natural Questions](../datasets/natural-questions.md), [PopQA](../datasets/popqa.md), [PPO](ppo.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [reasoning boundary](../concepts/reasoning-boundary.md), [reward sparsity](../concepts/reward-sparsity.md), [Search-R1](search-r1.md), [TriviaQA](../datasets/triviaqa.md), [uncertainty quantification](../concepts/uncertainty-quantification.md)

## Appears in

- [Start Classifying: Categorical Critics for LLM Reinforcement Learning](../../archive/papers/2026/arxiv-2608-02181/summary.md) — Replaces PPO's scalar mean-squared-error critic head with a categorical predictor over a discretized value support trained by cross-entropy against Gaussian-smoothed targets, decodes it back to a scalar for an unchanged GAE update, and shows the resulting critic is better calibrated and produces near-symmetric advantages where the MSE critic penalizes failures two-to-three times harder than it rewards successes.
- [The Confidence Paradox: Unveiling the Latent Discriminative Power of Diffusion Large Language Models in Mathematical Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2142/summary.md) — Finds diffusion language models are badly miscalibrated on math reasoning yet rank correct from incorrect far better than autoregressive baselines, because their confidence tracks structural consistency rather than correctness.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
