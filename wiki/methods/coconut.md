# COCONUT

<!-- auto:begin -->

The latent reasoner the archive's sources use as the reference point for continuous-space reasoning: intermediate computation is carried as continuous hidden vectors fed back into the model instead of being emitted as chain-of-thought tokens. All three sources cite it as a baseline rather than defining it, and each names the same limitation from a different side - SLPO notes that bypassing the vocabulary distribution leaves no per-step action likelihood for credit assignment and that COCONUT prescribes a fixed number of latent steps at training and inference, so the compute horizon is not optimizable (its ungated runs use T_max=6 against SLPO's 12). Penelope reports it at 52.79+/-0.36 EM on Deep ListOps with K=8 but at 188.15+/-1.02 ms latency, against Penelope's 99.82 ms, because the recurrence re-runs the whole decoder; ImgCoT reports it far weaker on mathematics, 3.5 on MATH and 3.7 on GSM8K at 0.5B. Adding SLPO on top lifts Pass@8 on MultiArith with a Llama-3.2-1B COCONUT from 45.00 to 57.07, though absolute accuracy stays low (25.01 average).

- **Kind**: method
- **Also called**: Coconut
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [CODI](codi.md), [CoLaR](colar.md), [GRPO](grpo.md), [GSM-Hard](../datasets/gsm-hard.md), [GSM8K](../datasets/gsm8k.md), [Latent reasoning](../concepts/latent-reasoning.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [Recurrent Depth](../concepts/recurrent-depth.md), [RLOO](rloo.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [Test-Time Scaling](../concepts/test-time-scaling.md), [Thinking Budget](../concepts/thinking-budget.md)

## Appears in

- [SLPO: Scaling Latent Reasoning via a Surrogate Policy](../../archive/papers/2026/arxiv-2607-19691/summary.md) — SLPO adds outcome-reward RL to autoregressive latent (continuous-vector) reasoners by scoring latent transitions with a Gaussian surrogate density built from MC-dropout forwards, and by training a stopping head that turns a fixed latent thinking budget into a learned per-instance horizon.
- [Penelope: Localized Latent Recurrence for Efficient Structured Reasoning](../../archive/papers/2026/arxiv-2607-25915/summary.md) — Penelope confines latent reasoning recurrence to a five-layer slice of a decoder-only Transformer, refining a fixed-size boundary memory K times instead of re-running the whole decoder or emitting a chain-of-thought trace.
- [ImgCoT: Compressing Long Chain of Thought into Compact Visual Tokens for Efficient Reasoning of Large Language Model](../../archive/papers/2026/title-154a4b443b05189a/summary.md) — ImgCoT compresses a long chain of thought into a small set of latent tokens by training the autoencoder to reconstruct an image of the rendered CoT rather than its text.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
