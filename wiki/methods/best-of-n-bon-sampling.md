# Best-of-N (BoN) sampling

<!-- auto:begin -->

A test-time-compute strategy that samples N candidate solutions independently and selects one by a verifier or reward model, trading inference compute for accuracy. Under this spelling: ST-BoN truncates unpromising candidates early using internal-state sampling consistency to cut Best-of-N's cost, and Sequential Reward Filtering proves standard best-of-n is suboptimal under a mixture-of-reference-policy model, proposing a sequential alternative with better guarantees. Note: same method as the archive's separately-tracked 'best-of-N sampling' / 'Best-of-N' entries -- never merged.

- **Kind**: method
- **Also called**: Best-of-N, BoN, best-of-N sampling, best-of-n (BoN) sampling
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [best-of-N sampling](best-of-n-sampling.md), [rejection sampling](rejection-sampling.md), [test-time compute](../concepts/test-time-compute.md), [test-time scaling](../concepts/test-time-scaling.md)

## Appears in

- [Sampling-Efficient Test-Time Scaling: Self-Estimating the Best-of-N Sampling in Early Decoding](../../archive/papers/2025/title-9dcfd1b98bd7008e/summary.md) — ST-BoN cuts the cost of Best-of-N test-time scaling by using early sampling consistency in internal states to truncate unpromising candidates before they finish generating, without a reward model.
- [On the Limits of Test-Time Compute: Sequential Reward Filtering for Better Inference](../../archive/papers/2026/title-cd5c62ac6be53cbc/summary.md) — Proves standard best-of-n sampling is suboptimal for test-time compute under a mixture-of-reference-policy model and proposes reward-filtered sequential inference as a stronger alternative.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
