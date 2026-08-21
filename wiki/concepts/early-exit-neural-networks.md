# early-exit neural networks

<!-- auto:begin -->

In these three sources an early-exit neural network is a backbone with intermediate prediction heads, so that a forward pass can be terminated at a shallower depth for inputs that do not need the full stack. This is the forward-pass sense of early exit and has nothing to do with shortening a reasoning model's chain of thought. The sources differ entirely on what decides the exit: BEXA attaches exit branches to the actor of an off-policy actor-critic agent and picks the exit per state by solving a constrained linear program during training, then amortizes that solution for cheap runtime inference; the speech-separation paper pairs the architecture with a probabilistic model of the clean signal and its error variance so a target signal-to-noise ratio becomes the exit condition. 'Rethinking Calibration for Early-Exit Neural Networks' argues against the usual criterion, holding that confidence calibration is the wrong objective and replacing it with Early-Exit Failure Prediction, which also accounts for whether later layers could still fix the prediction.

- **Kind**: concept
- **Also called**: early exit neural networks
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [confidence calibration](confidence-calibration.md), [Confidence Thresholding](../methods/confidence-thresholding.md), [early exit](../methods/early-exit.md), [early-exit ensembles](../methods/early-exit-ensembles.md), [ImageNet-1K](../datasets/imagenet-1k.md), [Layer-wise early exit](../methods/layer-wise-early-exit.md)

## Appears in

- [Rethinking Calibration for Early-Exit Neural Networks](../../archive/papers/2026/title-14e8a3607202d3e2/summary.md) — Argues that confidence calibration is the wrong objective for early-exit image classifiers and replaces it with Early-Exit Failure Prediction, a criterion that also accounts for whether later layers could fix the prediction.
- [Mind the Budget: Accelerating Deep Reinforcement Learning using Constrained Early Exit Neural Networks](../../archive/papers/2026/title-1c8c5064463b1075/summary.md) — BEXA adds early-exit branches to the actor network of an off-policy actor-critic agent and picks the exit per state by solving a constrained linear program during training, then amortizes that solution for cheap runtime inference.
- [Knowing When to Quit: Probabilistic Early Exits for Speech Separation Networks](../../archive/papers/2026/title-8342bedc3c993484/summary.md) — An early-exit neural architecture for single-channel speech separation and enhancement, paired with a probabilistic model of the clean signal and its error variance that turns a target signal-to-noise ratio into an exit condition.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
