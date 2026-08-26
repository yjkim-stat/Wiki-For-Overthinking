<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# More Experts, Worse Dynamics: Inverse Scaling and Spectral Bias in Mixture-of-Experts State-Space Models

- **Authors**: Chandresh Pandey
- **Venue**: cs.LG
- **Published**: 2026-08-22
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.21840>
- **PDF**: <https://arxiv.org/pdf/2608.21840v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

A controlled synthetic study finding that mixing stable spectral state-space operators through a learned router fails to beat a single-expert baseline on regime-switching time series, with more experts making it worse, routing collapsing to one expert, and apparent MSE gains on chaotic data coming from variance suppression that destroys the attractor.

## Problem

Mixture-of-Experts is commonly motivated for regime-switching dynamics on the assumption that heterogeneous behaviour decomposes into a few simpler local dynamics, and this has been extended to spectral state-space models where mixing stable operators is assumed to add expressivity while keeping stability. The assumption had not been isolated from representational difficulty and tested directly.

## Contributions

- A controlled synthetic testbed isolating dynamical rather than representational difficulty for regime-switching sequence models.
- Evidence of inverse scaling in operator-level MoE state-space models: NMSE and seed variance both rise from K = 1 to K = 4 and K = 8.
- Evidence that soft routing at the operator level collapses to a dominant expert even with explicit regime boundaries and supervised warmup.
- A demonstration that lower MSE on chaotic dynamics can come from variance suppression -- a 61% MSE reduction accompanied by attractor collapse -- arguing for geometry-aware evaluation alongside pointwise error.

## Method

The model, Gated Multi-Stability (GMS), gives each expert a linear state-space model parameterised in the spectral domain with transition eigenvalues constrained strictly inside the unit circle; at each timestep a router produces soft weights from the current input and the effective transition operator is their convex combination. The test sequence has three sequential regimes: chaotic Mackey-Glass with delay tau = 17, a stable oscillatory regime, and a noise-dominated autoregressive regime. Next-step prediction is scored by normalized MSE globally and per regime, over five seeds. Ablations cover capacity scaling in the number of experts K, oracle routing, frozen experts, and output-level (rather than operator-level) MoE baselines. Beyond NMSE, delay-coordinate phase-space reconstruction (x(t), x(t - tau)) compares predicted against true attractor geometry.

## Results

NMSE does not improve with capacity: a modest gain sometimes appears at K = 2, but K = 4 and K = 8 both have higher mean NMSE and substantially higher across-seed variance than the single-expert baseline, which is itself low-variance. K = 4, the primary setting, is worse on average than the baseline despite greater representational capacity. Routing collapses -- the router sends the majority of timesteps to one expert across chaotic, oscillatory and noise segments alike, and this persists after the supervised warmup signal is annealed to zero, with only transient deviations at regime boundaries. The per-regime profile shows why the global number moves little: GMS reduces chaotic-regime error relative to baseline but is worse on the oscillatory regime and unchanged on noise, so the regressions offset the gain. The phase-space result is the paper's central one: on the chaotic regime GMS achieves a 61% MSE reduction while its delay-embedded trajectory contracts toward a smooth low-variance manifold, losing the folded Mackey-Glass geometry that the single-expert baseline partially preserves -- the error gain comes from temporal smoothing, not from modelling the dynamics. Oracle routing and frozen-expert ablations are reported to leave this intact.

## Limitations

Stated: the conclusion is scoped to the studied convex spectral-operator parameterisation and training protocol. Noticed by the reader: (a) the setting is a single synthetic three-regime sequence, so the negative result is about this construction rather than about operator mixing in general, and no real time series is tested; (b) K is explored only at 1, 2, 4, 8 with five seeds, and the K = 2 result is described as inconsistent ('sometimes observed'), so the inverse-scaling claim rests on K = 4 and K = 8; (c) the oracle-routing and frozen-expert ablations that carry the strongest form of the claim -- that even perfect regime supervision does not help -- are in an appendix and summarised in one sentence in the main text; (d) the text states that under K = 4 routing collapse 'only 1/3 experts' are active, which does not match K = 4 and is left unexplained; (e) the 61% MSE reduction is quoted against the baseline for the chaotic regime only, and no quantitative geometry measure accompanies the phase-space figure -- the attractor comparison is visual, so the paper's headline methodological claim is supported by a plot rather than by a statistic; (f) single author, no released code referenced in the text read.

## Why it matters here

- **overthinking**: Does not bear on the topic. This is sequence modelling of synthetic dynamical systems with no language model, no reasoning trace and no test-time compute; it entered the archive on the keyword 'inverse scaling', which here means degradation as the number of MoE experts grows -- a training-capacity axis, not the inference-length axis the topic is about. The archive should treat it as a scoring false positive. One methodological point transfers by analogy only, and should be cited as an analogy if at all: a 61% MSE reduction is shown to come from variance suppression that destroys the structure the metric was standing in for. That is the same failure shape as the pseudo-conciseness the archive records for length metrics -- a proxy improving while the property it proxies degrades -- and it is a second independent argument for checking an efficiency metric against a structural measurement rather than trusting it alone. Nothing in the paper's evidence is about reasoning.

## Entities

- **Concepts**: [Inverse Scaling](../../../../wiki/concepts/inverse-scaling.md), Mixture-of-Experts, [Routing Collapse](../../../../wiki/concepts/routing-collapse.md), Expert Specialization, Spectral State-Space Models, Operator Interpolation, Phase-Space Reconstruction, Metric-Fidelity Mismatch
- **Methods**: Gated Multi-Stability (GMS), Spectral state-space model, Soft routing, Oracle routing ablation, Frozen-expert ablation, Delay-coordinate embedding
- **Datasets**: Synthetic three-regime sequence: Mackey-Glass chaotic (tau = 17), stable oscillatory, noise-dominated autoregressive

Tags: `inverse scaling`, `mixture-of-experts`, `state-space models`, `routing collapse`, `chaotic dynamics`, `evaluation metrics`, `off-topic`

## Abstract

Mixture-of-Experts (MoE) architectures are commonly motivated as a way to increase expressivity by decomposing complex systems into simpler local dynamics. This intuition has recently been extended to spectral state-space models, where mixing stable operators is assumed to enable adaptation to heterogeneous or regime-switching time series. We critically evaluate this assumption in a controlled synthetic setting designed to isolate dynamical rather than representational challenges. We study a next-step prediction task on sequences composed of three regimes: chaotic dynamics generated by the Mackey-Glass system, a stable oscillatory regime, and a noise-dominated autoregressive regime. Across extensive ablations including capacity scaling, oracle routing, frozen-expert variants, and comparisons to output-level MoE baselines, operator-level mixture models consistently fail to outperform a single-expert baseline. Increasing the number of experts leads to inverse scaling, routing collapses or fails to induce meaningful specialization, and even perfect regime supervision does not prevent degradation in global performance. Furthermore, we show that apparent improvements in mean squared error on chaotic trajectories can be misleading. Phase-space analysis reveals that lower error often arises from temporal smoothing that destroys the geometry of the underlying attractor rather than from faithful modeling of the dynamics. These results identify a likely limitation of operator interpolation under the studied parameterization and training protocol, and underscore the need for geometry-aware evaluation when assessing regime-switching dynamical systems.

---

Record id: `arxiv:2608.21840`
