<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Benefits of Early Stopping in Gradient Descent for Overparameterized Logistic Regression

- **Authors**: _unknown_
- **Venue**: ICML 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2025/poster/44193>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

A theoretical analysis showing that in well-specified high-dimensional logistic regression, gradient descent stopped early is statistically consistent and needs polynomially many samples, whereas gradient descent run to convergence is inconsistent and any interpolating estimator needs exponentially many.

## Problem

In overparameterized logistic regression the iterates of gradient descent diverge in norm while converging in direction to the maximum l2-margin solution, the implicit bias of GD. What remained open was whether stopping GD early confers a statistical benefit beyond that directional bias, and how such an implicit regularization relates quantitatively to explicit l2 regularization.

## Contributions

- Proof that excess logistic risk vanishes for early-stopped GD but diverges for GD iterates at convergence, so early-stopped GD is calibrated and asymptotic GD is statistically inconsistent
- A polynomial-versus-exponential sample-complexity separation for small excess zero-one risk between early-stopped GD and any interpolating estimator
- Nonasymptotic bounds on the norm and angular difference between early-stopped GD and the l2-regularized empirical risk minimizer, connecting implicit and explicit regularization

## Method

The paper analyses gradient descent on well-specified high-dimensional logistic regression and compares the early-stopped iterate against the asymptotic (interpolating) solution along three axes. First it bounds the excess logistic risk of the early-stopped iterate and shows it vanishes, while the same quantity diverges to infinity along the GD trajectory at convergence, which is the sense in which early-stopped GD is calibrated and asymptotic GD is statistically inconsistent. Second it derives sample-complexity separations for small excess zero-one risk: an upper bound showing polynomially many samples suffice for early-stopped GD, against a lower bound showing exponentially many are necessary for any interpolating estimator, the asymptotic GD solution included. Third it gives nonasymptotic bounds on the norm difference and the angular difference between the early-stopped GD iterate and the l2-regularized empirical risk minimizer, tying the implicit regularization of early stopping to an explicit penalty.

## Results

The results are theorems rather than benchmark numbers. The stated separations are: excess logistic risk vanishing for early-stopped GD versus diverging to infinity for GD at convergence; polynomially many samples sufficient for early-stopped GD to reach small excess zero-one risk versus exponentially many necessary for any interpolating estimator; and nonasymptotic norm and angle bounds between the early-stopped iterate and the l2-regularized ERM.

## Limitations

The setting is deliberately narrow: well-specified high-dimensional logistic regression with gradient descent, so the guarantees do not carry to misspecified models, other losses, or nonlinear predictors without new argument. The supplied material states no empirical validation, and the analysis characterises the existence of a good stopping time rather than giving a procedure that finds it from data.

## Why it matters here

- **overthinking**: Tangential: this matched only on the phrase 'early stopping'. The term here means halting an optimizer's iterations during training of a linear classifier, a statistical regularization question about excess risk and sample complexity; it has nothing to do with a language model deciding when to stop generating a chain of thought at inference. There is no reasoning model, no test-time compute, and no accuracy/length tradeoff in the paper. The shared word is the only connection, and treating the result as evidence about reasoning length would be a category error.

## Entities

- **Concepts**: implicit bias of gradient descent, early stopping as implicit regularization, overparameterization, benign overfitting / interpolating estimators, excess risk and calibration, sample complexity separation
- **Methods**: gradient descent, early stopping, l2-regularized empirical risk minimization, max-margin / implicit bias analysis
- **Datasets**: _none recorded_

Tags: `learning-theory`, `early-stopping`, `logistic-regression`, `implicit-regularization`, `overparameterization`, `sample-complexity`

---

Record id: `title:db0a2f307926937b`
