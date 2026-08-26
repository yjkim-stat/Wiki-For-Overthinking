# Pass@1

<!-- auto:begin -->

The fraction of problems a model solves correctly on its first (single) sampled attempt, the baseline accuracy metric against which test-time-compute methods that spend more (Best-of-N, self-consistency, verification) are compared. Consilience's verifier-free rollout-selection metric and CLR's claim-level reliability assessment both report gains over a Pass@1 baseline.

- **Kind**: concept
- **Also called**: pass@1
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Best-of-N sampling](../methods/best-of-n-sampling.md), [best-of-n selection](../methods/best-of-n-selection.md), [CMIMC25](../datasets/cmimc25.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [HMMT 2025](../datasets/hmmt-2025.md), [HMMT25](../datasets/hmmt25.md), [LiveCodeBench-v6](../datasets/livecodebench-v6.md), [pass@K](pass-k.md), [SWE-bench Verified](../datasets/swe-bench-verified.md)

## Appears in

- [Consilience for Verifier-Free Test-Time Scaling](../../archive/papers/2026/arxiv-2608-09898/summary.md) — Introduces consilience, a verifier-free test-time-scaling selection metric that picks the sampled reasoning rollout whose confidence starts low (exploratory) and ends high (convergent), fixing a failure mode where naive confidence maximization favors confidently wrong answers on hard problems.
- [Claim-Level Reliability Assessment for Efficient Test-Time Reasoning](../../archive/papers/2026/arxiv-2608-11994/summary.md) — CLR reallocates part of the test-time compute budget from generating more solution samples to falsifying a small set of decision-critical claims extracted from each trace, improving accuracy over self-consistency while using fewer tokens on some models.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
