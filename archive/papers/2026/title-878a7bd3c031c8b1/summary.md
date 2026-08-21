<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Conformal Prediction for Early Stopping in Mixed Integer Optimization

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/61715>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Trains a neural network to estimate a mixed-integer solver's true optimality gap from its internal state, then uses conformal prediction to calibrate a termination threshold that carries a distribution-free probabilistic guarantee on the quality of the solution returned.

## Problem

Mixed-integer optimization solvers typically find an optimal or near-optimal solution early in the branch-and-bound search and then spend most of the remaining runtime proving that it is optimal. For a practitioner who repeatedly solves similar instances drawn from the same distribution, that proof time is largely wasted, but stopping early is unsafe without knowing how far the incumbent is from optimal -- and the true gap is exactly what is unknown until the proof completes.

## Contributions

- Frames early solver termination as a learning problem: predict the true optimality gap from solver state on a distribution of related instances
- Applies conformal prediction to convert that learned estimate into a stopping threshold with a distribution-free probabilistic guarantee on solution quality
- Reports over 60% reduction in solve time on six Distributional MIPLIB families at 0.1%-optimality with 95% probability

## Method

A neural network is trained to predict the true optimality gap of the incumbent solution from features of the solver state, using a distribution of similar problem instances. Because a learned point estimate carries no guarantee, conformal prediction is applied on a calibration set of instances from the same distribution to turn the predictor into a stopping threshold with a rigorous coverage guarantee: for a new instance drawn from that distribution, terminating when the calibrated criterion fires yields a solution within the stated optimality tolerance with the stated probability. The guarantee is therefore distributional and marginal -- it holds over draws from the training distribution, not per instance.

## Results

On six problem families from the Distributional MIPLIB library, solve time is reduced by over 60% while guaranteeing 0.1%-optimal solutions with 95% probability for new instances drawn from the same distribution.

## Limitations

The guarantee is exchangeability-based and holds only for instances drawn from the same distribution as the calibration set; nothing is claimed for a shifted distribution, and the abstract does not report behaviour under shift. The coverage is marginal over instances rather than conditional, so the 5% of instances that fall outside the guarantee are not characterised -- how bad the worst returned solution is is not stated. Both the 0.1% tolerance and the 95% level are chosen settings, and no curve trading time saved against tolerance or confidence is reported in the abstract. The method requires a corpus of similar solved instances to train and calibrate on, so it does not apply to a one-off problem, and the cost of generating that corpus is not counted against the 60% saving. Only six families from one library are evaluated.

## Why it matters here

- **overthinking**: Not relevant to this topic. The match came from the keyword "early stopping", which here means terminating a branch-and-bound search in a mixed-integer programming solver, not stopping a reasoning model's chain of thought. There is no language model, no reasoning trace and no test-time compute scaling in the paper; the computation being cut short is optimality proof work in a classical solver, and the quality measure is an optimality gap on an integer program. The one idea with any portability is methodological rather than topical: a learned predictor of an unobservable quality signal is unsafe on its own, and conformal prediction over a distribution of similar instances converts it into a stopping rule with a stated coverage guarantee. If the group ever wanted a calibrated guarantee on the accuracy cost of truncating a reasoning trace, that construction is a template -- but this paper neither makes nor tests that connection, and the exchangeability assumption it relies on would have to be re-argued for reasoning traces. File as a false positive of the keyword filter.

## Entities

- **Concepts**: Conformal Prediction, Early Stopping, Distribution-Free Coverage Guarantees, Optimality Gap, Learning to Optimize
- **Methods**: [conformal prediction](../../../../wiki/methods/conformal-prediction.md), learned optimality-gap estimation from solver state, branch-and-bound early termination, mixed-integer programming
- **Datasets**: Distributional MIPLIB (six problem families)

Tags: `early stopping`, `conformal prediction`, `mixed integer optimization`, `branch and bound`, `optimality gap`, `learning to optimize`, `off-topic`, `icml-2026`

---

Record id: `title:878a7bd3c031c8b1`
