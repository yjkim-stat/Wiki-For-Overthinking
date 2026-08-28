# CODI

<!-- auto:begin -->

A latent chain-of-thought reasoner that carries intermediate computation as continuous vectors rather than emitted tokens, grouped with COCONUT throughout the archive as the pair of existing latent reasoners that prescribe a fixed number of latent steps at training and inference - which is SLPO's stated reason that nothing about their compute horizon is optimizable, the vocabulary distribution being bypassed so no per-step action likelihood exists for credit assignment. None of the three sources describes how it is trained; all three use it as a baseline. Penelope measures it at 51.17+/-0.31 EM on Deep ListOps, below its own 52.25+/-0.72 and Coconut's 52.79; ImgCoT reports 4.3 on MATH at 1.5B; SLPO on top of CODI moves GSM8K only marginally, 55.22 to 55.27 on Llama-1B and 42.30 to 42.76 on GPT-2, while cutting reasoning steps sharply against explicit CoT-SFT.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [beam search](beam-search.md), [best-of-n selection](best-of-n-selection.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [COCONUT](coconut.md), [CoLaR](colar.md), [GRPO](grpo.md), [GSM-Hard](../datasets/gsm-hard.md), [GSM8K](../datasets/gsm8k.md), [GSM8K-Test](../datasets/gsm8k-test.md), [Latent reasoning](../concepts/latent-reasoning.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [LoRA](lora.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MultiArith](../datasets/multiarith.md), [Recurrent Depth](../concepts/recurrent-depth.md), [RLOO](rloo.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [Test-Time Scaling](../concepts/test-time-scaling.md), [Thinking Budget](../concepts/thinking-budget.md)

## Appears in

- [SLPO: Scaling Latent Reasoning via a Surrogate Policy](../../archive/papers/2026/arxiv-2607-19691/summary.md) — SLPO adds outcome-reward RL to autoregressive latent (continuous-vector) reasoners by scoring latent transitions with a Gaussian surrogate density built from MC-dropout forwards, and by training a stopping head that turns a fixed latent thinking budget into a learned per-instance horizon.
- [Penelope: Localized Latent Recurrence for Efficient Structured Reasoning](../../archive/papers/2026/arxiv-2607-25915/summary.md) — Penelope confines latent reasoning recurrence to a five-layer slice of a decoder-only Transformer, refining a fixed-size boundary memory K times instead of re-running the whole decoder or emitting a chain-of-thought trace.
- [Parallel Test-Time Scaling for Latent Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2069/summary.md) — Extends parallel test-time scaling to latent reasoning models (which reason in continuous hidden-state vectors rather than tokens) by introducing two stochastic sampling strategies (Monte Carlo Dropout, Additive Gaussian Noise) to generate diverse latent trajectories and a Latent Reward Model trained with a step-wise contrastive objective to score and aggregate them, showing consistent scaling gains with best-of-N and beam search across three arithmetic benchmarks and backbones up to 4B parameters.
- [ImgCoT: Compressing Long Chain of Thought into Compact Visual Tokens for Efficient Reasoning of Large Language Model](../../archive/papers/2026/title-154a4b443b05189a/summary.md) — ImgCoT compresses a long chain of thought into a small set of latent tokens by training the autoencoder to reconstruct an image of the rendered CoT rather than its text.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
