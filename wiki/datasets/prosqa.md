# ProsQA

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [COCONUT](../methods/coconut.md), [CODI](../methods/codi.md), [CoLaR](../methods/colar.md), [GSM8K](gsm8k.md), [MATH](math.md), [StrategyQA](strategyqa.md)

## Appears in

- [SpiralThinker: Latent Reasoning through an Iterative Process with Text–Latent Interleaving](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1605/summary.md) — SpiralThinker interleaves explicit textual reasoning steps with implicit latent-token steps (rather than picking one mode exclusively, which the paper frames as risking overthinking in verbose textual frameworks or underthinking in purely latent ones), iteratively refining the latent representations across K passes with no new tokens generated, and stabilizes this via a progressive alignment objective that pulls each iteration's latent hidden state toward its corresponding explicit-reasoning-step hidden state (weighted to emphasize later, more consolidated iterations) -- beating five latent-reasoning baselines on GSM8K-Aug/ProsQA/StrategyQA, with ablations showing iteration alone can degrade performance and only iteration-plus-alignment together deliver the gains.
- [ImgCoT: Compressing Long Chain of Thought into Compact Visual Tokens for Efficient Reasoning of Large Language Model](../../archive/papers/2026/title-154a4b443b05189a/summary.md) — ImgCoT compresses a long chain of thought into a small set of latent tokens by training the autoencoder to reconstruct an image of the rendered CoT rather than its text.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
