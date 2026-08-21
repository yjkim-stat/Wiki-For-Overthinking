# CODI

<!-- auto:begin -->

A latent chain-of-thought reasoner that carries intermediate computation as continuous vectors rather than emitted tokens, grouped with COCONUT throughout the archive as the pair of existing latent reasoners that prescribe a fixed number of latent steps at training and inference - which is SLPO's stated reason that nothing about their compute horizon is optimizable, the vocabulary distribution being bypassed so no per-step action likelihood exists for credit assignment. None of the three sources describes how it is trained; all three use it as a baseline. Penelope measures it at 51.17+/-0.31 EM on Deep ListOps, below its own 52.25+/-0.72 and Coconut's 52.79; ImgCoT reports 4.3 on MATH at 1.5B; SLPO on top of CODI moves GSM8K only marginally, 55.22 to 55.27 on Llama-1B and 42.30 to 42.76 on GPT-2, while cutting reasoning steps sharply against explicit CoT-SFT.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [Accuracy-Efficiency Tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [chain-of-thought compression](../concepts/chain-of-thought-compression.md), [COCONUT](coconut.md), [CoLaR](colar.md), [GRPO](grpo.md), [GSM-Hard](../datasets/gsm-hard.md), [GSM8K](../datasets/gsm8k.md), [latent reasoning](latent-reasoning.md), [MATH](../datasets/math.md), [MATH-500](../datasets/math-500.md), [recurrent depth](../concepts/recurrent-depth.md), [RLOO](rloo.md), [test-time compute scaling](../concepts/test-time-compute-scaling.md), [test-time scaling](../concepts/test-time-scaling.md), [thinking budget](../concepts/thinking-budget.md)

## Appears in

- [SLPO: Scaling Latent Reasoning via a Surrogate Policy](../../archive/papers/2026/arxiv-2607-19691/summary.md) — SLPO adds outcome-reward RL to autoregressive latent (continuous-vector) reasoners by scoring latent transitions with a Gaussian surrogate density built from MC-dropout forwards, and by training a stopping head that turns a fixed latent thinking budget into a learned per-instance horizon.
- [Penelope: Localized Latent Recurrence for Efficient Structured Reasoning](../../archive/papers/2026/arxiv-2607-25915/summary.md) — Penelope confines latent reasoning recurrence to a five-layer slice of a decoder-only Transformer, refining a fixed-size boundary memory K times instead of re-running the whole decoder or emitting a chain-of-thought trace.
- [ImgCoT: Compressing Long Chain of Thought into Compact Visual Tokens for Efficient Reasoning of Large Language Model](../../archive/papers/2026/title-154a4b443b05189a/summary.md) — ImgCoT compresses a long chain of thought into a small set of latent tokens by training the autoencoder to reconstruct an image of the rendered CoT rather than its text.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
