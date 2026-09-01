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

Proves that early-stopped gradient descent for overparameterized logistic regression achieves bounded excess logistic risk and polynomial sample complexity for minimal zero-one risk, while asymptotic (fully converged) GD has statistically inconsistent, unboundedly growing excess risk and requires exponential sample complexity for interpolating solutions, and derives quantitative bounds connecting early-stopped GD to explicit L2-regularized solutions.

## Problem

In high-dimensional (overparameterized) logistic regression, gradient descent run to convergence interpolates the training data and is known to behave poorly, but the precise statistical benefit of stopping GD early -- as an implicit regularization mechanism -- and its relationship to explicit L2 regularization were not fully characterized.

## Contributions

- a theoretical characterization of early-stopped GD's excess logistic risk (bounded) versus asymptotic GD's (unbounded, statistically inconsistent) in overparameterized logistic regression
- sample-complexity results showing early-stopped GD needs only polynomial samples for minimal zero-one risk versus exponential samples for interpolating methods
- quantitative bounds connecting early-stopped GD to explicit L2-regularized solutions, formalizing the implicit-explicit regularization relationship

## Method

Theoretically analyzes gradient descent for overparameterized logistic regression, deriving statistical guarantees for both early-stopped and asymptotic (converged) GD: excess logistic risk bounds, sample complexity requirements for achieving minimal zero-one (classification) risk, and quantitative bounds on the difference between early-stopped GD solutions and explicit L2-regularized solutions.

## Results

Excess logistic risk for early-stopped GD diminishes (remains bounded and controlled), while it grows without bound for GD continued to convergence, indicating early-stopped GD maintains proper statistical calibration whereas asymptotic GD is statistically inconsistent. Early-stopped GD requires only polynomial sample complexity to achieve minimal zero-one risk, whereas interpolating methods (including standard GD run to convergence) require exponential sample complexity. Quantitative bounds establish that early-stopped GD solutions are closely related to explicit L2-regularized solutions, illuminating the connection between implicit regularization (via early stopping) and explicit regularization (via an L2 penalty).

## Limitations

Not stated in the fetched abstract beyond the overparameterized logistic regression setting analyzed.

## Why it matters here

- **overthinking**: Not relevant beyond the shared keyword 'early stopping': this is a theoretical statistical-learning-theory result about implicit regularization via early stopping in overparameterized logistic regression training, unconnected to inference-time reasoning length or test-time compute for LLM reasoning.

## Entities

- **Concepts**: implicit regularization via early stopping, excess logistic risk, statistical consistency of gradient descent, polynomial vs. exponential sample complexity
- **Methods**: gradient descent (early-stopped and asymptotic), theoretical statistical learning analysis
- **Datasets**: _none recorded_

Tags: `early-stopping`, `implicit-regularization`, `logistic-regression`, `learning-theory`

---

Record id: `title:db0a2f307926937b`
