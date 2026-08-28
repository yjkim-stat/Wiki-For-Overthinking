# Thinking Budget

<!-- auto:begin -->

Thinking budget denotes a cap, fixed or learned, on how much reasoning a model performs before answering. SLPO turns a fixed latent thinking budget into a learned per-instance horizon via a trained stopping head; the machine-translation-evaluator source instead finds reasoning models overthink simple translation-quality judgments and calibrates their thinking via synthetic human-like trajectories, cutting the thinking budget roughly 35x while improving correlation with human judgments.

- **Kind**: concept
- **Also called**: Thinking Budget, thinking budget
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [COCONUT](../methods/coconut.md), [CODI](../methods/codi.md), [CoLaR](../methods/colar.md), [GRPO](../methods/grpo.md), [GSM-Hard](../datasets/gsm-hard.md), [GSM8K-Test](../datasets/gsm8k-test.md), [Latent reasoning](latent-reasoning.md), [MATH500](../datasets/math500.md), [MultiArith](../datasets/multiarith.md), [RLOO](../methods/rloo.md), [Test-Time Scaling](test-time-scaling.md)

## Appears in

- [SLPO: Scaling Latent Reasoning via a Surrogate Policy](../../archive/papers/2026/arxiv-2607-19691/summary.md) — SLPO adds outcome-reward RL to autoregressive latent (continuous-vector) reasoners by scoring latent transitions with a Gaussian surrogate density built from MC-dropout forwards, and by training a stopping head that turns a fixed latent thinking budget into a learned per-instance horizon.
- [Are Large Reasoning Models Good Translation Evaluators? Analysis and Performance Boost](../../archive/papers/2025/title-cca25579537de930/summary.md) — Analyzes large reasoning models as machine-translation evaluators, finds they overthink simple instances, and calibrates their thinking via synthetic human-like trajectories to cut thinking budget ~35x while improving correlation with human judgments.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
