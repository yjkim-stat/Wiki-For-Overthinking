# T5-Large

<!-- auto:begin -->

Neither source describes T5-Large directly; it is used as a backbone model for early-exit inference experiments. RAEE retrieves the exit behaviour of similar training examples from a pre-built database instead of training internal per-layer classifiers; UAT replaces a static confidence threshold with an online multi-armed bandit, reporting 1.70-2.10x speedup at under 2% performance drop.

- **Kind**: method
- **Also called**: T5-large
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Confidence Thresholding](confidence-thresholding.md), [Early Exit](early-exit.md), [Llama-3-8B](../models/llama-3-8b.md), [Risk Control](../concepts/risk-control.md), [SST-2](../datasets/sst-2.md)

## Appears in

- [RAEE: A Robust Retrieval-Augmented Early Exit Framework for Efficient Inference](../../archive/papers/2026/title-5e9b243e4d404cc8/summary.md) — RAEE decides which transformer layer to exit at by retrieving the exit behaviour of similar training examples from a pre-built database, instead of training internal classifiers or using heuristics.
- [Beyond Greedy Exits: Improved Early Exit Decisions for Risk Control and Reliability](../../archive/papers/2025/title-c65d4659ec08b51c/summary.md) — UAT replaces the static confidence threshold in early-exit deep networks with a multi-armed bandit that adapts the threshold online and unsupervised, reporting 1.70-2.10x speedup at under 2% performance drop.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
