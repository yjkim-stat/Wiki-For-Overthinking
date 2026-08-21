# T5-Large

<!-- auto:begin -->

Neither source describes T5-Large directly; it is used as a backbone model for early-exit inference experiments. RAEE retrieves the exit behaviour of similar training examples from a pre-built database instead of training internal per-layer classifiers; UAT replaces a static confidence threshold with an online multi-armed bandit, reporting 1.70-2.10x speedup at under 2% performance drop.

- **Kind**: method
- **Also called**: T5-large
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [Early Exit](early-exit.md), [Llama-3-8B](../models/llama-3-8b.md), [SST-2](../datasets/sst-2.md)

## Appears in

- [RAEE: A Robust Retrieval-Augmented Early Exit Framework for Efficient Inference](../../archive/papers/2026/title-5e9b243e4d404cc8/summary.md) — RAEE decides which transformer layer to exit at by retrieving the exit behaviour of similar training examples from a pre-built database, instead of training internal classifiers or using heuristics.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
