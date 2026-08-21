# early-exit ensembles

<!-- auto:begin -->

In both sources an early-exit ensemble is a network whose intermediate exit heads are treated as ensemble members rather than as alternative stopping points, on very small on-device models; this is the forward-pass sense of early exit, unrelated to shortening a reasoning trace. QUTE uses early-exit-assisted ensembles to quantify predictive uncertainty in KB-sized TinyML classifiers within a single forward pass, so a deployed model can be monitored without labels. TinyTTA makes test-time adaptation to distribution shift feasible on microcontrollers by adapting only the early-exit heads of a self-ensemble instead of backpropagating through the whole network, and ships an MCU runtime that executes it. What the two share is the ensemble use of the heads; neither source, as held here, gives an exit criterion for terminating the pass.

- **Kind**: method
- **Also called**: early-exit-assisted ensembles
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Distribution Shift](../concepts/distribution-shift.md), [Early Exit](early-exit.md), [early-exit neural networks](../concepts/early-exit-neural-networks.md), [knowledge distillation](knowledge-distillation.md), [test-time adaptation](../concepts/test-time-adaptation.md), [Uncertainty Quantification](../concepts/uncertainty-quantification.md)

## Appears in

- [QUTE: Quantifying Uncertainty in TinyML models with Early-exit-assisted ensembles for model-monitoring](../../archive/papers/2025/title-53c7cfefc569f403/summary.md) — QUTE is an early-exit-assisted ensemble architecture that quantifies predictive uncertainty in KB-sized TinyML classifiers within a single forward pass, for on-device monitoring without labels.
- [TinyTTA: Efficient Test-time Adaptation via Early-exit Ensembles on Edge Devices](../../archive/papers/2024/title-bf8bc6d3bbf1c242/summary.md) — Makes test-time adaptation to distribution shift feasible on microcontrollers by adapting only early-exit heads in a self-ensemble instead of backpropagating through the whole network, and ships an MCU runtime that executes it.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
