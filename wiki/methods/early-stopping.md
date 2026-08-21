# early stopping

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Also called**: Early Stopping
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 5

**Related**: [adaptive test-time compute](../concepts/adaptive-test-time-compute.md), [Best-of-N](best-of-n.md), [confidence-based early stopping](confidence-based-early-stopping.md), [confidence calibration](../concepts/confidence-calibration.md), [conformal prediction](conformal-prediction.md), [GPQA](../datasets/gpqa.md), [GSM8K](../datasets/gsm8k.md), [HLE](../datasets/hle.md), [MathQA](../datasets/mathqa.md), [MMLU](../datasets/mmlu.md), [overthinking](../concepts/overthinking.md), [self-consistency](self-consistency.md), [test-time compute](../concepts/test-time-compute.md), [Uncertainty Quantification](../concepts/uncertainty-quantification.md)

## Appears in

- [CaTS: Calibrated Test-Time Scaling for Efficient LLM Reasoning](../../archive/papers/2026/title-03232c54fde9b57f/summary.md) — Proposes CaTS, a calibrated test-time scaling framework that uses a self-distilled confidence signal to adaptively allocate sampling budget per query, including early stopping once the model is confident.
- [Statistical Early Stopping for Reasoning Models](../../archive/papers/2026/title-594984624acaa60d/summary.md) — Two statistical stopping rules monitor uncertainty-keyword arrivals inside a reasoning trace and halt generation on ill-posed or ambiguous queries, one with a finite-sample bound on the probability of halting too early on a well-posed query.
- [Instance-dependent Early Stopping](../../archive/papers/2025/title-5f72fe24f143bb5d/summary.md) — Moves early stopping from the whole training set down to the individual training example, dropping an instance from backpropagation once the second-order difference of its loss stays near zero.
- [Conformal Prediction for Early Stopping in Mixed Integer Optimization](../../archive/papers/2026/title-878a7bd3c031c8b1/summary.md) — Trains a neural network to estimate a mixed-integer solver's true optimality gap from its internal state, then uses conformal prediction to calibrate a termination threshold that carries a distribution-free probabilistic guarantee on the quality of the solution returned.
- [Benefits of Early Stopping in Gradient Descent for Overparameterized Logistic Regression](../../archive/papers/2025/title-db0a2f307926937b/summary.md) — A theoretical analysis showing that in well-specified high-dimensional logistic regression, gradient descent stopped early is statistically consistent and needs polynomially many samples, whereas gradient descent run to convergence is inconsistent and any interpolating estimator needs exponentially many.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
