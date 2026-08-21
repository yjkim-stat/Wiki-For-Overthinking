# Distribution Shift

<!-- auto:begin -->

Neither source defines distribution shift; both take it as the reason a decision rule fixed before deployment stops being valid after it, and each handles it online. In Anytime Safe PAC Efficient Reasoning the shift is in the query stream reaching a thinking/non-thinking router: a threshold calibrated offline on a held-out set is not safe on a later, non-stationary stream, and the paper replaces offline calibration with a betting supermartingale that recertifies the threshold at every time step under partial feedback. In TinyTTA it is shift in the input distribution of a deployed network on a microcontroller, corrected by test-time adaptation of early-exit heads only rather than full backpropagation, reported at up to 57.6% accuracy improvement and up to six times lower memory, and running within the 512 KB of an STM32H747. What the two share is the assumption that the shift is never directly observed at run time -- no labels on device, no counterfactual loss for an unrouted query -- so it has to be tracked through a proxy signal as the stream arrives.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [BBH](../datasets/bbh.md), [Chain-of-Draft](../methods/chain-of-draft.md), [MATH](../datasets/math.md), [MMLU-Pro](../datasets/mmlu-pro.md), [Risk Control](risk-control.md), [Test-Time Compute Scaling](test-time-compute-scaling.md), [Uncertainty Quantification](uncertainty-quantification.md)

## Appears in

- [Anytime Safe PAC Efficient Reasoning](../../archive/papers/2026/title-b525ac9b26640523/summary.md) — Routes queries between a thinking and a non-thinking model with a threshold that is adjusted online by a betting supermartingale, so the accumulated statistical evidence certifies at any stopping time that the accuracy given up stays under a user-specified tolerance.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
