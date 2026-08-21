# CoLaR

<!-- auto:begin -->

A latent chain-of-thought method that the archive's two sources cite only as prior work, and each for a different reason. SLPO classes it with LEPO and Latent-GRPO as a latent-policy method that routes credit back through the vocabulary or through architecture-specific latent heads, which is why SLPO says those methods do not apply to a reasoner propagating plain hidden states - the contrast that motivates its own Gaussian surrogate density over latent transitions. ImgCoT lists it as the strongest of the earlier latent-CoT baselines it reports, at 19.1 on MATH and 27.4 on GSM8K with a 3B model, ahead of Coconut and CODI but still well below full text chain-of-thought. Neither source states how CoLaR is trained or what its latent step schedule is.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [COCONUT](coconut.md), [CODI](codi.md), [GRPO](grpo.md), [GSM-Hard](../datasets/gsm-hard.md), [GSM8K](../datasets/gsm8k.md), [Latent reasoning](../concepts/latent-reasoning.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [RLOO](rloo.md), [Test-time scaling](../concepts/test-time-scaling.md), [Thinking Budget](../concepts/thinking-budget.md)

## Appears in

- [SLPO: Scaling Latent Reasoning via a Surrogate Policy](../../archive/papers/2026/arxiv-2607-19691/summary.md) — SLPO adds outcome-reward RL to autoregressive latent (continuous-vector) reasoners by scoring latent transitions with a Gaussian surrogate density built from MC-dropout forwards, and by training a stopping head that turns a fixed latent thinking budget into a learned per-instance horizon.
- [ImgCoT: Compressing Long Chain of Thought into Compact Visual Tokens for Efficient Reasoning of Large Language Model](../../archive/papers/2026/title-154a4b443b05189a/summary.md) — ImgCoT compresses a long chain of thought into a small set of latent tokens by training the autoencoder to reconstruct an image of the rendered CoT rather than its text.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
