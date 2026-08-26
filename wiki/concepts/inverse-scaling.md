# Inverse Scaling

<!-- auto:begin -->

A finding, or a task designed to produce one, where a model performs worse as it is given more of some resource -- more parameters, or more test-time reasoning -- rather than better. The archive holds two distinct sources under this name: 'Inverse Scaling in Test-Time Compute' constructs tasks where letting large reasoning models think longer degrades accuracy or safety-relevant behavior; the original 'Inverse Scaling: When Bigger Isn't Better' (Inverse Scaling Prize) instead reports 11 tasks where accuracy declines with model parameter count, an unrelated axis of scaling.

- **Kind**: concept
- **Also called**: inverse scaling
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [Overthinking](overthinking.md), [routing collapse](routing-collapse.md), [scaling laws](scaling-laws.md), [Test-Time Compute Scaling](test-time-compute-scaling.md)

## Appears in

- [More Experts, Worse Dynamics: Inverse Scaling and Spectral Bias in Mixture-of-Experts State-Space Models](../../archive/papers/2026/arxiv-2608-21840/summary.md) — A controlled synthetic study finding that mixing stable spectral state-space operators through a learned router fails to beat a single-expert baseline on regime-switching time series, with more experts making it worse, routing collapsing to one expert, and apparent MSE gains on chaotic data coming from variance suppression that destroys the attractor.
- [Inverse Scaling in Test-Time Compute](../../archive/papers/2025/local-018eb3ee241c1a69/summary.md) — Constructs evaluation tasks across four categories (distractor counting, spurious-feature regression, constraint-tracking deduction, and AI-risk model-written evaluations) where letting large reasoning models reason longer at test time makes their accuracy or alignment worse, not better.
- [Inverse Scaling: When Bigger Isn't Better](../../archive/papers/2025/title-cb7f41c5af287a91/summary.md) — Reports 11 tasks, found via the Inverse Scaling Prize contest, on which language model accuracy declines as model parameter count and training compute increase, and analyzes why.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
