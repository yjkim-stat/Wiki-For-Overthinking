# Risk Control

<!-- auto:begin -->

Risk control names giving an efficiency method a statistical guarantee on how much accuracy it can give up, rather than tuning a threshold by hand. The 'Anytime Safe PAC' source certifies, via a betting supermartingale over accumulated evidence, that switching between a thinking and non-thinking model keeps the accuracy loss under a user-set tolerance at any stopping time; UAT instead adapts an early-exit confidence threshold online with a multi-armed bandit, reporting 1.70-2.10x speedup at under 2% performance drop, without a formal guarantee of the first kind.

- **Kind**: concept
- **Also called**: Risk control
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [BIG-Bench Hard](../datasets/big-bench-hard.md), [Chain-of-Draft](../methods/chain-of-draft.md), [Confidence Thresholding](../methods/confidence-thresholding.md), [Distribution Shift](distribution-shift.md), [early exit](../methods/early-exit.md), [MATH](../datasets/math.md), [MMLU-PRO](../datasets/mmlu-pro.md), [SST-2](../datasets/sst-2.md), [T5-Large](../methods/t5-large.md), [test-time compute scaling](test-time-compute-scaling.md)

## Appears in

- [Anytime Safe PAC Efficient Reasoning](../../archive/papers/2026/title-b525ac9b26640523/summary.md) — Routes queries between a thinking and a non-thinking model with a threshold that is adjusted online by a betting supermartingale, so the accumulated statistical evidence certifies at any stopping time that the accuracy given up stays under a user-specified tolerance.
- [Beyond Greedy Exits: Improved Early Exit Decisions for Risk Control and Reliability](../../archive/papers/2025/title-c65d4659ec08b51c/summary.md) — UAT replaces the static confidence threshold in early-exit deep networks with a multi-armed bandit that adapts the threshold online and unsupervised, reporting 1.70-2.10x speedup at under 2% performance drop.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
