<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Theoretical Guarantees for One-Shot Magnitude Pruning and Compute-Adaptive Early Exit

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/63550>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

A theoretical analysis of compute reduction in neural networks, deriving concentration results for one-shot magnitude pruning and generalization-error scaling for a 'conditional perceptron' that performs early exit at the neuron level.

## Problem

Pruning and conditional computation both reduce the amount of arithmetic a network performs, and both empirically preserve accuracy, but there is little theory saying why or at what rate accuracy degrades as compute is cut. The paper treats the two as a single 'partial versus full computation' question: pruning in the static regime (the same subset of weights is dropped for every input) and early exit in the adaptive regime (how much is computed depends on the input).

## Contributions

- A concentration theorem, with explicit rates, for one-shot magnitude pruning of a neuron in an asymptotic large-dimension regime.
- The conditional perceptron, a neuron-level early-exit construction that skips reading the remainder of its inputs when a sub-local field computed from a subset is strong enough.
- A bound showing the conditional perceptron's excess generalization error decays as a power of the compute gap, with an exponent that grows to infinity as partial/full computation alignment tends to one.
- An extension to deep networks characterising how pruning distortion accumulates with depth, and a compute-accuracy tradeoff for frozen-backbone early exit under a neural network Gaussian process model.
- Numerical simulations corroborating the predicted scaling laws.

## Method

Two regimes are analysed in an asymptotic limit of large input dimension and training-set size. For the static regime, a concentration theorem is proved for one-shot magnitude pruning of a single neuron, with explicit rates. For the adaptive regime, the paper defines the conditional perceptron: the neuron first forms a sub-local field from a subset of its inputs, and if that partial field is strong enough the remaining inputs are never read, saving computation. Its excess generalization error is shown to decay as a power of the compute gap between the partial and full computation, with the exponent growing without bound as the alignment between partial and full computations approaches one. The analysis is then extended to deep networks: pruning-induced distortion is characterised as it accumulates with depth, and a compute-accuracy tradeoff is derived for frozen-backbone early exit under a neural network Gaussian process (NNGP) model. Numerical simulations are used to check the predicted scaling laws.

## Results

The paper reports that numerical simulations corroborate the predicted scaling laws. The abstract and available material state no benchmark accuracies, no wall-clock or FLOP measurements on real models, and no language-model experiments.

## Limitations

The guarantees are asymptotic and rest on a single-neuron model, extended to deep networks only under an NNGP (infinite-width, frozen-backbone) idealisation, which is not the regime a trained finite-width transformer occupies. The early-exit result is about a neuron ignoring part of its input vector, not about a network halting after a variable number of layers on a real task, and the validation is simulation rather than measurement on a deployed model. Nothing in the paper addresses the token-level or step-level decisions that adaptive-compute work on language models is concerned with.

## Why it matters here

- **overthinking**: Tangential, and matched on the phrase 'early exit' alone. 'Early exit' here means a neuron declining to read the rest of its input vector, and the deep-network case means halting at an intermediate layer of a frozen backbone; both are architectural compute reduction per forward pass. The topic is about how many reasoning tokens or steps a model spends on a problem, which is a decision made across many forward passes and is not modelled here at all. There are no language models, no reasoning traces and no accuracy/length tradeoff over chain-of-thought in the paper. The only transferable idea is the abstract shape of the result — accuracy loss decaying as a power of the compute gap, with the exponent controlled by how well the partial computation is aligned with the full one — which is an analogy to, not evidence about, deciding when a reasoning model should stop. Treat this as a false positive for the topic.

## Entities

- **Concepts**: partial versus full computation, static versus adaptive compute reduction, compute gap, alignment between partial and full computation, excess generalization error, compute-accuracy tradeoff, depth-accumulated pruning distortion, scaling law
- **Methods**: one-shot magnitude pruning, conditional perceptron, frozen-backbone early exit, neural network Gaussian process (NNGP)
- **Datasets**: _none recorded_

Tags: `pruning`, `early exit`, `conditional computation`, `generalization bounds`, `nngp`, `scaling laws`, `theory`, `off-topic`

---

Record id: `title:eaf8c68124e5ee94`
