# beam search

<!-- auto:begin -->

Beam search is cited as one of several test-time search strategies whose behavior on reasoning models these sources study or extend. It is one of the granularity choices studied in optimal-verification-granularity work, and one of the scaling strategies (alongside best-of-N) shown to transfer, with consistent gains, to latent (continuous-vector) reasoning models.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Best-of-N sampling](best-of-n-sampling.md), [best-of-n selection](best-of-n-selection.md), [COCONUT](coconut.md), [CODI](codi.md), [CoLaR](colar.md), [GSM8K-Test](../datasets/gsm8k-test.md), [majority voting (baseline)](majority-voting-baseline.md), [MATH500](../datasets/math500.md), [MultiArith](../datasets/multiarith.md)

## Appears in

- [Parallel Test-Time Scaling for Latent Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2069/summary.md) — Extends parallel test-time scaling to latent reasoning models (which reason in continuous hidden-state vectors rather than tokens) by introducing two stochastic sampling strategies (Monte Carlo Dropout, Additive Gaussian Noise) to generate diverse latent trajectories and a Latent Reward Model trained with a step-wise contrastive objective to score and aggregate them, showing consistent scaling gains with best-of-N and beam search across three arithmetic benchmarks and backbones up to 4B parameters.
- [Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling](../../archive/papers/2025/title-7409f584637723da/summary.md) — Studies how often a verifier should be called during LLM generation, proposing a search algorithm that tunes verification granularity to trade off accuracy and compute in test-time scaling.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
