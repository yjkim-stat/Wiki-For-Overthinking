# expected calibration error

<!-- auto:begin -->

The average gap between a model's stated confidence and its observed accuracy, binned over the confidence range — how wrong the numbers are, as against how well they order. Both sources use it precisely because it measures only that. One reports a critic's improvement from 0.2612 to 0.2131 alongside Brier and maximum calibration error, and connects it to a downstream consequence rather than treating it as an end: a critic that overestimates success probability turns a symmetric binary reward into an asymmetric advantage. The other separates the two properties outright, finding a diffusion language model at 31.2% on this measure — badly miscalibrated — while ranking correct from incorrect at 0.826 AUROC against 0.611 for autoregressive baselines, and shows post-hoc calibration cutting the error by over 60% while leaving the ranking intact. Read together the sources say the same thing from opposite directions: this quantity is not a proxy for whether a confidence signal is useful, and which one you need depends on whether something downstream consumes the value or only the order.

- **Kind**: concept
- **Also called**: ECE, calibration error
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [advantage estimation](advantage-estimation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [answer stabilization](answer-stabilization.md), [Bamboogle](../datasets/bamboogle.md), [Brumo](../datasets/brumo.md), [calibration](../methods/calibration.md), [DAPO](../methods/dapo.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [GRPO](../methods/grpo.md), [HMMT](../datasets/hmmt.md), [HotpotQA](../datasets/hotpotqa.md), [MuSiQue](../datasets/musique.md), [Natural Questions](../datasets/natural-questions.md), [PopQA](../datasets/popqa.md), [PPO](../methods/ppo.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [reasoning boundary](reasoning-boundary.md), [reward sparsity](reward-sparsity.md), [Search-R1](../methods/search-r1.md), [TriviaQA](../datasets/triviaqa.md), [uncertainty quantification](uncertainty-quantification.md)

## Appears in

- [Start Classifying: Categorical Critics for LLM Reinforcement Learning](../../archive/papers/2026/arxiv-2608-02181/summary.md) — Replaces PPO's scalar mean-squared-error critic head with a categorical predictor over a discretized value support trained by cross-entropy against Gaussian-smoothed targets, decodes it back to a scalar for an unchanged GAE update, and shows the resulting critic is better calibrated and produces near-symmetric advantages where the MSE critic penalizes failures two-to-three times harder than it rewards successes.
- [The Confidence Paradox: Unveiling the Latent Discriminative Power of Diffusion Large Language Models in Mathematical Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2142/summary.md) — Finds diffusion language models are badly miscalibrated on math reasoning yet rank correct from incorrect far better than autoregressive baselines, because their confidence tracks structural consistency rather than correctness.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
