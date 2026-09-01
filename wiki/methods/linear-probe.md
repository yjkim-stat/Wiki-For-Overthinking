# linear probe

<!-- auto:begin -->

A linear classifier -- logistic regression in the sources here -- fitted to a model's hidden-state activations to predict a property of the generation that the text does not yet show. The two archived uses are a non-convergence study, where a probe on the 3,584-dimensional hidden state at token 150 predicts whether an AIME generation will terminate or loop to the ceiling and beats a behavioural baseline built from entropy statistics and repeated n-grams, and hallucination detection, where probing scores sit far above perplexity and verbalized-certainty detectors. Both sources are explicit about what it does not establish: a probe shows predictive information is present in the hidden state, not that the state causes the outcome, which would need activation patching.

- **Kind**: method
- **Also called**: activation probe, linear probing
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [activation steering](activation-steering.md), [Aha Moment](../concepts/aha-moment.md), [early stopping](../concepts/early-stopping.md), [Overthinking](../concepts/overthinking.md), [Reward Hacking](../concepts/reward-hacking.md), [sparse autoencoders (SAEs)](sparse-autoencoders-saes.md)

## Appears in

- [A Data-dependent Early Stopping Rule using Rademacher Complexity with L1-norm](../../archive/papers/2026/arxiv-2608-24210/summary.md) — Derives an analytic, data-dependent estimate of the optimal early-stopping time for gradient-flow training of linear (and, via linear probing, underparameterized neural) models, using Rademacher complexity with the L1-norm instead of assumptions on the data distribution.
- [Towards a Mechanistic Understanding of Large Reasoning Models: A Survey of Training, Inference, and Failures](../../archive/papers/2026/local-34cecfd6f28ba72b/summary.md) — A survey that organizes existing mechanistic-interpretability research on large reasoning models into three areas -- reasoning-oriented training dynamics, reasoning mechanisms, and unintended behaviors (hallucination, CoT unfaithfulness, overthinking, unsafety) -- and proposes directions for future mechanistic work.
- [On Reasoning Strength Planning in Large Reasoning Models](../../archive/papers/2025/title-11c0c9193baf1d69/summary.md) — Finds that large reasoning models pre-plan how much to reason via a directional vector in their activations, whose magnitude causally sets reasoning length.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
