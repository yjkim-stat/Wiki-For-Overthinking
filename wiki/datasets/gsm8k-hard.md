# GSM8K-Hard

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [activation steering](../methods/activation-steering.md), [AQuA-RAT](aqua-rat.md), [beam search](../methods/beam-search.md), [best-of-n selection](../methods/best-of-n-selection.md), [COCONUT](../methods/coconut.md), [CODI](../methods/codi.md), [CoLaR](../methods/colar.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER (baseline)](../methods/deer-baseline.md), [GSM8K](gsm8k.md), [GSM8K-Test](gsm8k-test.md), [LiveCodeBench](livecodebench.md), [majority voting (baseline)](../methods/majority-voting-baseline.md), [MATH500](math500.md), [MultiArith](multiarith.md), [Overthinking](../concepts/overthinking.md), [QwQ-32B](../models/qwq-32b.md), [SEAL (baseline)](../methods/seal-baseline.md)

## Appears in

- [Parallel Test-Time Scaling for Latent Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2069/summary.md) — Extends parallel test-time scaling to latent reasoning models (which reason in continuous hidden-state vectors rather than tokens) by introducing two stochastic sampling strategies (Monte Carlo Dropout, Additive Gaussian Noise) to generate diverse latent trajectories and a Latent Reward Model trained with a step-wise contrastive objective to score and aggregate them, showing consistent scaling gains with best-of-N and beam search across three arithmetic benchmarks and backbones up to 4B parameters.
- [Activation Steering for Chain-of-Thought Compression](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1828/summary.md) — Shows via t-SNE that verbose and concise chains-of-thought occupy visibly separable regions of a reasoning model's intermediate activation space, then learns a single, KL-trust-region-constrained steering vector (Contrastive Energy-Based Steering, CES) from only 100 verbose-concise CoT pairs by ranking concise traces below verbose ones in length-normalized energy under the steered model -- Activation-Steered Compression (ASC) cuts CoT length up to 69.35% with no accuracy loss across four model scales and multiple benchmarks, achieves 2.7x end-to-end wall-clock speedup, generalizes cross-task with 0.92 cosine similarity between dataset-specific steering vectors, and mitigates a documented 'underthinking' failure mode (excessive backtracking/path-switching without commitment) in QwQ-32B specifically.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
