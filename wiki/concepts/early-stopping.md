# early stopping

<!-- auto:begin -->

The five archived sources use 'early stopping' in three unrelated senses, and the archive should not be read as holding one idea here. Two halt a large reasoning model at inference: CaTS stops drawing further samples for a query once its self-distilled confidence is high enough, and 'Statistical Early Stopping for Reasoning Models' applies sequential stopping rules to the arrival of uncertainty keywords inside a trace, halting on ill-posed or ambiguous queries, with a finite-sample bound on the probability of halting too early on a well-posed one. Two use the classical training sense of stopping an optimizer short of convergence: Instance-dependent Early Stopping drops a training example from backpropagation once the second-order difference of its loss stays near zero, and a theoretical paper shows that in well-specified high-dimensional logistic regression gradient descent stopped early is consistent with polynomially many samples while gradient descent run to convergence is not. The fifth is neither, calibrating a termination threshold for a mixed-integer solver by conformal prediction on a learned estimate of the optimality gap; and none of the five is about leaving a network's layer stack at an intermediate head, which is early exit.

- **Kind**: concept
- **Also called**: Early Stopping
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [adaptive test-time compute](adaptive-test-time-compute.md), [Best-of-N](../methods/best-of-n.md), [Confidence-based early stopping](../methods/confidence-based-early-stopping.md), [Confidence Calibration](confidence-calibration.md), [Conformal Prediction](../methods/conformal-prediction.md), [Early Exit](../methods/early-exit.md), [GPQA](../datasets/gpqa.md), [GSM8K](../datasets/gsm8k.md), [HLE](../datasets/hle.md), [MathQA](../datasets/mathqa.md), [MMLU](../datasets/mmlu.md), [Overthinking](overthinking.md), [Self-Consistency](../methods/self-consistency.md), [Test-Time Compute](test-time-compute.md), [Test-Time Scaling](test-time-scaling.md), [Uncertainty Quantification](uncertainty-quantification.md)

## Appears in

- [CaTS: Calibrated Test-Time Scaling for Efficient LLM Reasoning](../../archive/papers/2026/title-03232c54fde9b57f/summary.md) — Proposes CaTS, a calibrated test-time scaling framework that uses a self-distilled confidence signal to adaptively allocate sampling budget per query, including early stopping once the model is confident.
- [Statistical Early Stopping for Reasoning Models](../../archive/papers/2026/title-594984624acaa60d/summary.md) — Two statistical stopping rules monitor uncertainty-keyword arrivals inside a reasoning trace and halt generation on ill-posed or ambiguous queries, one with a finite-sample bound on the probability of halting too early on a well-posed query.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
