<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# MIND over Body: Adaptive Thinking using Dynamic Computation

- **Authors**: _unknown_
- **Venue**: ICLR 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2025/poster/30390>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Adds a self-introspection module to CNN and transformer networks that decides, per input, how many parameters to reuse and how long to iterate, so computation scales with input complexity rather than input size.

## Problem

Standard networks spend the same computation on every input of a given size regardless of how hard that input is, and improving accuracy usually means adding parameters. The paper frames this as inefficient use of capacity and asks whether a network can instead decide at inference time how much of itself to run.

## Contributions

- A self-introspection mechanism that lets a network choose, from its own internal representation, how many parameters to use for a given input
- Adaptive computation time driven by input complexity rather than input size
- Parameter reuse across tasks in place of parameter growth
- Reported accuracy figures on ImageNet and SQuAD v1.1/v2.0 claimed to match or exceed much larger fixed-computation baselines

## Method

The network is given self-introspection: a component that reads the internal representation of the current input and decides how many parameters to use and how long to compute. Reported by a third-party summary of the paper's talk (not by the abstract) as fixed-point iteration applied at each layer until the layer's activations converge, with a separate introspection model trained under an auxiliary loss to predict when the fixed-point iteration can be skipped entirely; the same construction is applied to a CNN, where the iteration masks features, and to a transformer, where it is run to attention-activation convergence. Parameters are reused across tasks rather than added. The primary abstract states the mechanism only at the level of 'adjust the number of used parameters based on the internal representation of the task and adapt the computation time based on the task complexity'; the layer-level detail above could not be confirmed against the paper itself, which was not reachable.

## Results

Reported in the abstract: 96.62% accuracy on ImageNet with a three-layer network, stated as surpassing ResNet-50 and EfficientNet; 95.8% / 88.7% F1 on SQuAD v1.1 / v2.0 with a transformer architecture, at what the abstract calls negligible parameter cost. No per-input compute savings, latency or FLOP numbers appear in the material available. No breakdown by input difficulty is given, so the central claim -- that compute tracks complexity -- is not quantified in what could be read.

## Limitations

The paper's full text was not reachable (OpenReview blocked automated access), so this record rests on the abstract and one third-party talk summary; no limitations section could be read. Two things a reader should notice. First, 96.62% top-1 on ImageNet from a three-layer network is far above published top-1 for much larger models, and the abstract gives no evaluation protocol, so the figure cannot be checked from the material available and should not be relied on without the paper. Second, the abstract reports only accuracy, never the compute actually saved, so the efficiency claim that motivates the method is not evidenced by the numbers quoted.

## Why it matters here

- **overthinking**: Shares the principle the topic is about -- spend compute in proportion to how hard the instance is, decided by the model from its own internal state -- but not the setting. The axis being adapted is network depth and parameter reuse for a single forward pass on ImageNet and SQuAD, not the number of reasoning tokens a large reasoning model emits, and there is no chain of thought, no stopping criterion over a trace, and no accuracy/length curve. It is best read as prior art on the adaptive-computation side of test-time compute rather than as evidence about reasoning length: the matched keyword 'adaptive thinking' points at a 2025 dynamic-computation paper for vision and QA. Tangential, but conceptually adjacent, and the caveat above about its unverifiable ImageNet number applies to any use of it.

## Entities

- **Concepts**: adaptive computation time, input-conditional computation, parameter reuse, self-introspection, fixed-point iteration
- **Methods**: MIND, self-introspection module, [fixed-point iteration](../../../../wiki/methods/fixed-point-iteration.md), adaptive computation time
- **Datasets**: ImageNet, SQuAD v1.1, SQuAD v2.0

Tags: `adaptive-computation`, `dynamic-computation`, `parameter-efficiency`, `vision`, `question-answering`, `tangential`

---

Record id: `title:3d49618364a0cc92`
