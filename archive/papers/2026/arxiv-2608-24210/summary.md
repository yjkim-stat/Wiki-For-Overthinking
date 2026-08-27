<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# A Data-dependent Early Stopping Rule using Rademacher Complexity with L1-norm

- **Authors**: Duy Hoang, Bastien Berret, Olivier Bruneau, Laurent Fribourg
- **Venue**: cs.LG
- **Published**: 2026-08-25
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.24210>
- **PDF**: <https://arxiv.org/pdf/2608.24210v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Derives an analytic, data-dependent estimate of the optimal early-stopping time for gradient-flow training of linear (and, via linear probing, underparameterized neural) models, using Rademacher complexity with the L1-norm instead of assumptions on the data distribution.

## Problem

Existing analytic estimates of when to stop gradient descent to balance training fit against generalization typically rely on random matrix theory and assumptions about the data distribution (e.g. Gaussian, Marchenko-Pastur eigenvalue spectrum) or require a held-out validation set and numerical search; the paper seeks a distribution-free analytic stopping time.

## Contributions

- an analytic, training-free estimate t+ of the optimal early-stopping time for linear models under gradient flow, derived from Rademacher complexity with the L1-norm and requiring no assumption on the data distribution
- a closed-form expression for the generalization-bound's value at infinite training time, letting one check analytically whether early stopping is actually beneficial versus benign overfitting
- an empirical demonstration, via linear probing, that the linear-model estimate transfers to nonlinear MNIST classifiers and closely matches numerically tuned stopping times

## Method

Bounds the population loss by an empirical-loss term plus a Rademacher-complexity generalization term, using the L1-norm (rather than the standard L2-norm) so the bound's dependence on a model-output bound M drops out. For gradient flow on a linear regression model, derives a closed form for the time derivative of this bound and identifies the earliest time t+ at which the bound is guaranteed to stop decreasing, via a decomposition of the data covariance matrix's eigenvalues into a small 'informative' set and a 'nuisance' bulk (interpretable as a signal-to-noise ratio). Also derives a closed form for the bound's value as training time goes to infinity, to check whether stopping early actually helps or whether benign overfitting means training longer would be better. Applies the linear-model theory to nonlinear MLPs via linear probing (freezing all layers but the last).

## Results

On a synthetic Gaussian binary-classification task (m=256, n=512), the analytic estimate t+ exactly matches the true first stationary point t* (=27 iterations) and is closer to the numerically-tuned stopping time on a held-out set than the same bound computed with the L2-norm. On MNIST digit classification via linear probing (classes 3-vs-5, 4 hidden layers of width 10, n=10,000), t+ = t* = 342-357 depending on the exact criterion, versus a numerically tuned t_test = 356, and the test loss at t+ (0.1166) matches the test loss at t_test almost exactly; the crude closed-form approximation t+_approx is off by only ~40-150 iterations out of ~350. A second MNIST pair (0-vs-1) shows the same pattern (t+ = t* = 415 vs. t_test = 418, test loss 0.0582 in both cases). Across Gaussian, uniform and Pareto synthetic input distributions, the estimate is closer to the true stopping time when the samples-to-parameters ratio n/m is larger; for one small-ratio case (m=256, n=512, Pareto) the method fails outright (t+ = t* = 0).

## Limitations

The method requires the underparameterized regime (m <= n); for m > n (overparameterization) the paper states t* is close to 0 and the method fails outright, and epoch-wise double descent (where a later, lower loss minimum exists) is explicitly noted as a regime the method does not address, since it estimates only the first local minimum. It is derived for linear regression with gradient flow (continuous-time idealization of gradient descent) with a to zero initialized, and its use on nonlinear networks depends on the linear-probing approximation being adequate. No comparison against other analytic (random-matrix-theory-based) stopping-time estimators is run on the same examples.

## Why it matters here

- **overthinking**: Not actually about overthinking: this is training-time early stopping for generalization in linear/underparameterized-network regression (when to halt gradient descent to avoid overfitting), matched to the topic only by the shared term 'early stopping.' It has no connection to LLM reasoning length, test-time compute, or the accuracy/efficiency tradeoff of inference-time reasoning that the topic tracks.

## Entities

- **Concepts**: Rademacher complexity, [early stopping](../../../../wiki/concepts/early-stopping.md), bias-variance tradeoff, generalization gap, linear probing, epoch-wise double descent
- **Methods**: gradient flow, Rademacher complexity bound (L1-norm), [linear probing](../../../../wiki/methods/linear-probe.md)
- **Datasets**: MNIST (classes 3 vs 5, and 0 vs 1), synthetic Gaussian/uniform/Pareto-distributed data

Tags: `generalization`, `early-stopping`, `rademacher-complexity`, `linear-regression`, `double-descent`

## Abstract

Training neural networks requires balancing the trade-off between fitting the training data and achieving robust performance on unseen inputs. This ability, commonly referred to as generalizability, is determined by the gap between the empirical risk on the training set (``empirical loss'') and the expected risk over the data distribution (``generalization error''). Existing approaches typically estimate the generalization error numerically, requiring gradient descent training and an ``early stopping'' strategy. In this work, we introduce an analytic framework that estimates the optimal time of early stopping without the need for training. Several works in the literature also give such analytical estimations, but they are generally based on random matrix theory and often make assumptions on the distribution of the data or the eigenvalue distribution of the covariance matrix. In contrast, our work is based on Rademacher complexity (RC) without needing such probabilistic assumptions. For both theoretical and numerical reasons, it is more relevant to express RC with the L1- norm rather than with the L2-norm. We focus on the case of linear models and the problem of linear regression. Thanks to the ``linear probing'' method, our results can, however, be successfully applied to nonlinear neural networks, as illustrated in the classification MNIST example.

---

Record id: `arxiv:2608.24210`
