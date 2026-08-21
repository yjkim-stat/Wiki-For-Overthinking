<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Compute Optimal Inference and Provable Amortisation Gap in Sparse Autoencoders

- **Authors**: _unknown_
- **Venue**: ICML 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2025/poster/46270>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Proves via compressed sensing that a sparse autoencoder's linear-nonlinear encoder cannot perform accurate sparse inference even in solvable cases, and shows empirically that replacing the encoder with a stronger sparse-inference procedure recovers codes better at small extra compute.

## Problem

Sparse autoencoders are used to extract interpretable features from neural network representations, but the encoder is a single linear map plus a nonlinearity, i.e. an amortised approximation to a sparse-coding optimisation problem. Whether that amortisation costs accuracy, and how much, was not established.

## Contributions

- A proof, using compressed sensing theory, that an SAE encoder is inherently insufficient for accurate sparse inference even in solvable cases
- Decoupling encoding from decoding to compare sparse-inference procedures against the SAE encoder at matched dictionaries
- Empirical identification of conditions where more sophisticated sparse inference beats the SAE encoder with minimal extra compute
- Extension of the comparison to SAEs on large language model activations, where more expressive encoders are reported to yield greater interpretability

## Method

The authors treat the SAE encoder as an amortised solver for sparse recovery and analyse it with compressed sensing theory, proving there is a gap between what a linear-nonlinear encoder can recover and the true sparse code, even on instances where recovery is provably possible. They then decouple encoding from decoding: keeping the learned dictionary (decoder), they substitute more expressive sparse inference procedures at inference time and measure recovery of the sparse codes as a function of inference compute, sweeping to find where the extra compute pays. They repeat the comparison on SAEs fitted to large language model activations, scoring the resulting features for interpretability.

## Results

The abstract reports substantial gains in correct inference of sparse codes for minimal increases in compute, and that the finding generalises to SAEs applied to large language models, where more expressive encoders achieve greater interpretability. No specific numbers, dictionaries, models or interpretability scores are stated in the material available here.

## Limitations

None stated in the available material. A reader should notice that the empirical claim is about recovering sparse codes against a known dictionary, which is not the same as the downstream use of SAEs; that 'greater interpretability' is asserted without the metric being named in the abstract; and that the theoretical insufficiency result concerns the encoder architecture, so it constrains what a trained SAE encoder can do but says nothing about how large the gap is for any particular trained SAE.

## Why it matters here

- **overthinking**: Tangential: matched only on 'compute optimal', which here refers to how much compute to spend solving a sparse-recovery problem at the encoder, not to test-time compute for reasoning. The paper is about sparse autoencoders and mechanistic interpretability; there is no reasoning chain, no reasoning length and no stopping decision. The nearest conceptual echo is that spending more inference compute buys accuracy up to a point, which is the shape of a test-time scaling curve, but it is measured over sparse-code recovery rather than over a model's reasoning. A keyword false positive for this topic.

## Entities

- **Concepts**: Amortisation Gap, Sparse Coding, Compute-Accuracy Tradeoff in Inference, [Mechanistic Interpretability](../../../../wiki/concepts/mechanistic-interpretability.md), Sparse Autoencoder
- **Methods**: sparse autoencoders, compressed sensing, sparse inference, amortised inference, decoupled encoder/decoder inference
- **Datasets**: _none recorded_

Tags: `sparse-autoencoders`, `interpretability`, `compressed-sensing`, `amortised-inference`, `sparse-coding`

---

Record id: `title:67cc50b85e8eb705`
