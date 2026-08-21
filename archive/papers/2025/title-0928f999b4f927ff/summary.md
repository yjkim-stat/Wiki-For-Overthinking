<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Compute-Optimal LLMs Provably Generalize Better with Scale

- **Authors**: _unknown_
- **Venue**: ICLR 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2025/poster/29945>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Derives generalization bounds on the LLM pretraining objective in the Chinchilla compute-optimal regime, decomposing the bound into parameters per token, loss variance and quantization error, and showing that the latter two shrink with scale so that larger compute-optimal models have provably smaller generalization gaps.

## Problem

Larger language models generalize better, and the standard generalization theory does not explain why — most bounds get worse as parameter count grows, which is the opposite of what is observed. The question is open partly because existing bounds ignore the variance of the loss and are therefore loose for a low-variance objective like next-token prediction, and partly because nothing in the usual analysis takes account of the specific way real models are scaled, in which parameters and data grow together along a compute-optimal frontier rather than parameters growing alone.

## Contributions

- A fully empirical Freedman-type martingale concentration inequality that tightens generalization bounds by accounting for loss variance.
- Generalization bounds on the LLM pretraining objective in the compute-optimal regime, decomposed into parameters per token, loss variance and quantization error.
- The argument that on the compute-optimal frontier parameters per data point stay constant while loss variance and quantization error decrease, implying smaller generalization gaps at larger scale.
- An information-theoretic account of why larger models are more quantizable, via prequential coding showing information integration growing more slowly than capacity.
- A scaling law for the generalization gap, fitted on Pythia checkpoints from 70M to 12B on the Pile.

## Method

The analysis is a compression-style generalization bound applied to the pretraining objective, evaluated along the Chinchilla compute-optimal frontier where the parameter-to-token ratio N/D is held near 1/20. The technical instrument is a fully empirical Freedman-type martingale concentration inequality, which tightens standard bounds by using the observed variance of the loss rather than only its range — this matters because next-token loss has small variance relative to its range. The resulting bound decomposes into three interpretable terms: the number of parameters per token, the loss variance, and the quantization error incurred by representing the model at a fixed bitrate. The scaling argument then follows from how each term behaves as compute grows. Parameters per data point stay constant by construction on the compute-optimal frontier, so that term does not degrade; loss variance decreases with scale; quantization error decreases with scale. Two terms falling and one flat gives a bound that strengthens with scale. The paper additionally argues from information theory why larger models are more quantizable, using prequential coding to show that the rate at which a model integrates new information grows more slowly than its capacity along the compute-optimal frontier, so proportionally more of the capacity is redundant and compressible.

## Results

Bounds are computed empirically on Pythia models from 70M to 12B trained on the Pile, at checkpoints selected along the compute-optimal frontier with N/D approximately 1/20. The loss-variation term decreases roughly as 0.27 + 8337*N^-0.54, approximately proportional to 1/sqrt(N). The dominant complexity contribution is C*log V, with C = (N/D)*b*log 2 approximately 1/9 for vocabulary V = 50,000 at b = 3 bits. For a representative configuration the bound gives a token-wise gap of about 11/9 + 1/30 + 1.4/3 + 1/10, roughly 1.8 nats per token, against an empirical risk of about 2 nats per token — so the bound is of the same order as the quantity it bounds and is non-vacuous but not tight. Prequential coding gives information content scaling as 6e5 * N^(0.5 +/- 0.1), proportional to sqrt(D), the sublinear growth that underwrites the quantizability argument. The overall output is a scaling law for the generalization gap that predicts the bound strengthening with scale.

## Limitations

Stated: the sqrt(2C) smoothing term is described by the authors as pessimistic and likely improvable; the bounds constrain only the token-wise generalization gap, not full-sequence performance; the framework does not explain why the Hessian spectrum decays as observed, which the argument relies on; and the largest models at 12B failed quantization, leaving the empirical dataset incomplete at exactly the scale the trend most needs to be checked. That last point is worth weighting — the claim is about what happens as models get larger, and the largest point is missing. Beyond what is stated: the bound at roughly 1.8 nats per token against an empirical risk of about 2 nats per token is close to vacuous in practical terms even though formally non-vacuous. Everything is measured on one model family and one corpus, so the fitted exponents are a Pythia/Pile result rather than an established constant. And the whole analysis is about the pretraining objective — held-out next-token loss — which is not the downstream capability that motivates the opening question about why larger models are better.

## Why it matters here

- **overthinking**: A keyword false positive. The match was on 'compute-optimal', which in this paper carries its Chinchilla meaning — how to divide a fixed pretraining budget between parameters and training tokens — and has nothing to do with test-time compute. The topic concerns how much a model thinks while answering a question: reasoning length, when to stop, the accuracy/efficiency tradeoff at inference. This paper is about statistical generalization of the pretraining objective, measured as held-out next-token loss in nats. There is no reasoning model, no chain of thought, no inference-time budget, no notion of a response being longer than it needs to be. The compute being optimised is spent before the model ever answers anything, and the paper's scaling variables N and D are parameters and training tokens, not thinking tokens. The two senses of 'compute-optimal' are genuinely distinct vocabulary that collide on the same phrase, and this is the pretraining one. There is no substantive connection to record; the paper is legitimate work in a different area. Worth noting for the group's keyword list that 'compute-optimal' unqualified will keep matching pretraining scaling-law papers, of which there are many, and that narrowing it to something like 'test-time compute' or 'inference compute' would separate the two senses.

## Entities

- **Concepts**: compute-optimal (Chinchilla) frontier, generalization gap and its scaling law, parameters per token, loss variance as a bound-tightening quantity, quantization error / model compressibility, information integration rate versus model capacity
- **Methods**: empirical Freedman-type martingale concentration inequality, compression-based generalization bounds, post-training quantization at fixed bitrate, prequential coding, Chinchilla compute-optimal scaling
- **Datasets**: The Pile, Pythia model suite checkpoints (70M to 12B parameters)

Tags: `scaling-laws`, `generalization-bounds`, `chinchilla`, `pretraining`, `quantization`, `learning-theory`, `pythia`, `not-test-time-compute`

---

Record id: `title:0928f999b4f927ff`
