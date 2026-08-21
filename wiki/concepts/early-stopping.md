# early stopping

<!-- auto:begin -->

The five archived sources use 'early stopping' in three unrelated senses, and the archive should not be read as holding one idea here. Two halt a large reasoning model at inference: CaTS stops drawing further samples for a query once its self-distilled confidence is high enough, and 'Statistical Early Stopping for Reasoning Models' applies sequential stopping rules to the arrival of uncertainty keywords inside a trace, halting on ill-posed or ambiguous queries, with a finite-sample bound on the probability of halting too early on a well-posed one. Two use the classical training sense of stopping an optimizer short of convergence: Instance-dependent Early Stopping drops a training example from backpropagation once the second-order difference of its loss stays near zero, and a theoretical paper shows that in well-specified high-dimensional logistic regression gradient descent stopped early is consistent with polynomially many samples while gradient descent run to convergence is not. The fifth is neither, calibrating a termination threshold for a mixed-integer solver by conformal prediction on a learned estimate of the optimality gap; and none of the five is about leaving a network's layer stack at an intermediate head, which is early exit.

- **Kind**: concept
- **Also called**: Early Stopping
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 5

**Related**: [adaptive test-time compute](adaptive-test-time-compute.md), [Best-of-N](../methods/best-of-n.md), [confidence-based early stopping](../methods/confidence-based-early-stopping.md), [confidence calibration](confidence-calibration.md), [conformal prediction](../methods/conformal-prediction.md), [early exit](../methods/early-exit.md), [GPQA](../datasets/gpqa.md), [GSM8K](../datasets/gsm8k.md), [HLE](../datasets/hle.md), [MathQA](../datasets/mathqa.md), [MMLU](../datasets/mmlu.md), [overthinking](overthinking.md), [self-consistency](../methods/self-consistency.md), [test-time compute](test-time-compute.md), [test-time scaling](test-time-scaling.md), [Uncertainty Quantification](uncertainty-quantification.md)

## Appears in

- [CaTS: Calibrated Test-Time Scaling for Efficient LLM Reasoning](../../archive/papers/2026/title-03232c54fde9b57f/summary.md) — Proposes CaTS, a calibrated test-time scaling framework that uses a self-distilled confidence signal to adaptively allocate sampling budget per query, including early stopping once the model is confident.
- [Statistical Early Stopping for Reasoning Models](../../archive/papers/2026/title-594984624acaa60d/summary.md) — Two statistical stopping rules monitor uncertainty-keyword arrivals inside a reasoning trace and halt generation on ill-posed or ambiguous queries, one with a finite-sample bound on the probability of halting too early on a well-posed query.
- [Instance-dependent Early Stopping](../../archive/papers/2025/title-5f72fe24f143bb5d/summary.md) — Moves early stopping from the whole training set down to the individual training example, dropping an instance from backpropagation once the second-order difference of its loss stays near zero.
- [Conformal Prediction for Early Stopping in Mixed Integer Optimization](../../archive/papers/2026/title-878a7bd3c031c8b1/summary.md) — Trains a neural network to estimate a mixed-integer solver's true optimality gap from its internal state, then uses conformal prediction to calibrate a termination threshold that carries a distribution-free probabilistic guarantee on the quality of the solution returned.
- [Benefits of Early Stopping in Gradient Descent for Overparameterized Logistic Regression](../../archive/papers/2025/title-db0a2f307926937b/summary.md) — A theoretical analysis showing that in well-specified high-dimensional logistic regression, gradient descent stopped early is statistically consistent and needs polynomially many samples, whereas gradient descent run to convergence is inconsistent and any interpolating estimator needs exponentially many.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
