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

Using compressed sensing theory, proves that a sparse autoencoder (SAE) encoder is inherently insufficient for accurate sparse inference even in solvable cases, and shows decoupling encoding from decoding to use more expressive inference techniques yields substantial interpretability gains with minimal extra compute, including on large language models.

## Problem

Sparse autoencoders are widely used to extract interpretable features from neural network activations, but the standard SAE encoder architecture's fundamental adequacy for accurate sparse inference has not been theoretically established.

## Contributions

- a compressed-sensing-theoretic proof that standard SAE encoders are inherently insufficient for accurate sparse inference even in solvable cases
- a decoupled encoding/decoding framework testing more expressive inference techniques against standard SAE encoders
- empirical demonstration that more expressive encoders yield substantial sparse-code-inference and interpretability gains at minimal extra compute, including on LLMs

## Method

Applies compressed sensing theory to prove that a standard SAE encoder is inherently insufficient for accurate sparse inference even in cases where the underlying sparse code is theoretically recoverable (solvable), then decouples the encoding and decoding mechanisms to test whether more expressive/advanced inference techniques (beyond the standard encoder) can surpass standard SAE encoders at inferring sparse codes.

## Results

More expressive encoders/inference techniques achieve substantial gains in correctly inferring sparse codes with only minimal additional compute, and this benefit extends to large language models, where more expressive encoders are shown to achieve greater interpretability than standard SAE encoders.

## Limitations

Not stated in the fetched abstract beyond the compressed-sensing theoretical framework and the described encoder/decoder decoupling methodology.

## Why it matters here

- **overthinking**: Not relevant beyond the shared keyword 'compute-optimal': this is a theoretical and empirical study of sparse autoencoder interpretability limitations, unconnected to LLM reasoning-trace length or test-time compute for reasoning.

## Entities

- **Concepts**: sparse autoencoder (SAE) encoder insufficiency, compressed sensing theory applied to interpretability, amortization gap in sparse inference
- **Methods**: sparse autoencoders (SAEs), compressed sensing theory, decoupled encoder/decoder inference
- **Datasets**: _none recorded_

Tags: `interpretability`, `sparse-autoencoders`, `compute-optimal-inference`, `compressed-sensing`

---

Record id: `title:67cc50b85e8eb705`
