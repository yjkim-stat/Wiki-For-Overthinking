# GSM8K-Test

<!-- auto:begin -->

GSM8K (test) is referenced in these sources as one of the arithmetic/math reasoning benchmarks used to evaluate latent (continuous-vector) reasoning methods: SLPO and the parallel-test-time-scaling-for-latent-reasoning paper both use it (among other arithmetic benchmarks) to show scaling gains for their respective latent-reasoning approaches, without further detail on the test set itself.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2025](aime-2025.md), [AMC23](amc23.md), [beam search](../methods/beam-search.md), [best-of-n selection](../methods/best-of-n-selection.md), [COCONUT](../methods/coconut.md), [CODI](../methods/codi.md), [CoLaR](../methods/colar.md), [GRPO](../methods/grpo.md), [GSM-Hard](gsm-hard.md), [GSM8K-Hard](gsm8k-hard.md), [Latent reasoning](../concepts/latent-reasoning.md), [majority voting (baseline)](../methods/majority-voting-baseline.md), [MATH500](math500.md), [MultiArith](multiarith.md), [RLOO](../methods/rloo.md), [Test-Time Scaling](../concepts/test-time-scaling.md), [Thinking Budget](../concepts/thinking-budget.md)

## Appears in

- [SLPO: Scaling Latent Reasoning via a Surrogate Policy](../../archive/papers/2026/arxiv-2607-19691/summary.md) — SLPO adds outcome-reward RL to autoregressive latent (continuous-vector) reasoners by scoring latent transitions with a Gaussian surrogate density built from MC-dropout forwards, and by training a stopping head that turns a fixed latent thinking budget into a learned per-instance horizon.
- [Parallel Test-Time Scaling for Latent Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2069/summary.md) — Extends parallel test-time scaling to latent reasoning models (which reason in continuous hidden-state vectors rather than tokens) by introducing two stochastic sampling strategies (Monte Carlo Dropout, Additive Gaussian Noise) to generate diverse latent trajectories and a Latent Reward Model trained with a step-wise contrastive objective to score and aggregate them, showing consistent scaling gains with best-of-N and beam search across three arithmetic benchmarks and backbones up to 4B parameters.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
