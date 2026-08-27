<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Adaptive Regularization for Random Features: A Neighboring Early-Stopping Rule with Oracle-Rate Guarantees

- **Authors**: Caixing Wang, Zhibo Chen, Yue Wang
- **Venue**: stat.ML
- **Published**: 2026-08-26
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.25513>
- **PDF**: <https://arxiv.org/pdf/2608.25513v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Proposes NESR-KRR-RF, a neighboring early-stopping rule that adaptively selects the regularization parameter for kernel ridge regression with random features by comparing only adjacent estimators on a uniform grid, proving it attains the oracle polynomial learning rate up to log factors at lower computational cost than classical Lepskii-type all-pairs comparison.

## Problem

Kernel ridge regression with random features (KRR-RF) needs its regularization parameter tuned to unknown smoothness and capacity parameters of the target function to reach the optimal (oracle) learning rate, and standard tuning via cross-validation or grid search is computationally expensive, sensitive to grid choice, and lacks sharp finite-sample guarantees in the random-feature setting.

## Contributions

- a high-probability comparison bound between two KRR-RF estimators at different regularization levels, computable directly in the random-feature representation without forming the exact kernel Gram matrix
- NESR, a neighboring (uniformly-subdivided-grid) early-stopping rule for adaptive regularization selection in KRR-RF, reducing all-pairs comparisons to linear-in-grid-size neighboring comparisons
- a proof that NESR attains the oracle polynomial learning rate up to log factors without prior knowledge of source/capacity exponents, plus simulation and real-data evidence that it matches or beats cross-validation and classical Lepskii-type selection at lower cost

## Method

Establishes a high-probability comparison bound between two KRR-RF estimators fit at different (neighboring) regularization levels, computable directly from empirical prediction differences and coefficient norms via the random-feature representation (no exact kernel Gram matrix needed). Builds a neighboring early-stopping rule (NESR) on a uniformly subdivided grid of inverse regularization values, scanning from a data-dependent starting index and stopping at the first neighboring pair whose discrepancy exceeds a threshold derived from the empirical random-feature effective dimension -- reducing the number of discrepancy comparisons versus classical all-pairs Lepskii-type or geometric-grid procedures.

## Results

Proves (Theorem 2) that under standard source/capacity conditions and a sufficient random-feature budget, the KRR-RF estimator selected by NESR attains the oracle polynomial excess-risk rate up to logarithmic factors, without prior knowledge of the source smoothness or capacity exponents, covering both well-specified and part of the misspecified regime. Computational-complexity analysis shows NESR's neighboring comparisons cost O(K|D|M^2 + KM^3) versus O(K^2|D|M^2 + K|D|M^2) for a direct random-feature implementation of the classical (all-pairs) Lepskii rule -- linear rather than quadratic in the grid size K. In simulations across four (smoothness, capacity) configurations on periodic-spline-kernel regression, NESR's RMSE is comparable to or better than 5-fold cross-validation and the classical Lepskii rule (closest to the oracle in 2 of 4 settings, e.g. (r,gamma)=(0.5,0.45)), while using markedly fewer regularization-path fits/comparisons than cross-validation or all-pairs Lepskii, and a separate motivating experiment shows 5-fold CV (80 ridge solves) both costs 5x more than an oracle-path benchmark (16 solves) and gives a worse average test RMSE (0.694 +/- 0.013 vs. 0.677 +/- 0.005).

## Limitations

The number of random features M is treated as a prespecified computational budget rather than adaptively selected -- adaptive selection of M is explicitly stated as not considered in this work. Theorem 2's feature-budget lower bound depends on the unknown exponents r, alpha, gamma (a uniform sufficient bound is given in Corollary 1, but it is conservative). Theoretical guarantees require 2r+gamma>1; one of the four simulated settings ((r,gamma)=(0.4,0.1), violating this) is included only as an empirical check outside the proven regime. All empirical validation is on synthetic periodic-spline-kernel data and one real-data experiment; no application to deep-learning or LLM settings is attempted or claimed.

## Why it matters here

- **overthinking**: Not relevant beyond the shared keyword 'early-stopping rule': this is a statistical-learning-theory result on selecting the regularization parameter of kernel ridge regression with random features, unconnected to LLM reasoning length, test-time compute, or the accuracy/efficiency tradeoff the topic tracks.

## Entities

- **Concepts**: neighboring early-stopping rule (Lepskii-principle variant), empirical random-feature effective dimension, kernel ridge regression with random features (KRR-RF)
- **Methods**: kernel ridge regression with random features (KRR-RF), Lepskii (balancing) principle, neighboring early-stopping rule (NESR), cross-validation (baseline)
- **Datasets**: synthetic periodic-spline-kernel regression data

Tags: `kernel-methods`, `statistical-learning-theory`, `early-stopping`, `regularization`, `random-features`

## Abstract

Random feature methods provide a scalable approximation to kernel ridge regression (KRR), but the regularization parameter that yields the oracle learning rate depends on unknown smoothness and capacity parameters. In this work, we propose a neighboring early-stopping rule for adaptive regularization in KRR with random features (KRR-RF). The method uses a grid that is uniform in inverse regularization and compares only adjacent estimators, reducing the number of discrepancy comparisons relative to standard all-pairs Lepskii-type procedures. Both the neighboring discrepancy and its empirical complexity term can be computed directly in the random feature space, without constructing the exact kernel Gram matrix. We establish a high-probability comparison bound for neighboring KRR-RF estimators and show that, under standard source and capacity conditions together with suitable grid and random feature budget conditions, the selected estimator attains the oracle polynomial learning rate up to logarithmic factors. The result allows the regularization parameter to be selected without prior knowledge of the source and capacity exponents and covers both well-specified and partially misspecified regimes. Our analysis is based on an empirical random feature effective dimension that connects the observable stopping threshold with the population complexity of the random feature model. Simulation and real-data experiments illustrate the prediction performance and computational behavior of the proposed method in comparison with standard tuning procedures.

---

Record id: `arxiv:2608.25513`
