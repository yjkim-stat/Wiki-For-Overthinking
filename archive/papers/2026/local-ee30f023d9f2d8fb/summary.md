<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Transformers Provably Learn to Internalize Chain-of-Thought

- **Authors**: Yixiao Huang, Hanlin Zhu, Zixuan Wang, Jiantao Jiao, Stuart Russell, Somayeh Sojoudi, Song Mei
- **Venue**: preprint
- **Published**: 2026-01-01
- **Source**: local
- **Topics**: reasoning-training, test-time-scaling
- **Relevance score**: reasoning-training 0.50, test-time-scaling 0.50

## In one line

Proves that reasoning can be moved from emitted tokens into hidden states without losing sample efficiency, using a curriculum that deletes thinking tokens in geometric chunks and so needs only logarithmically many training stages.

## Problem

Explicit CoT buys sample efficiency — parity goes from exponential to polynomial in input length — at the cost of generating reasoning tokens at inference, which is expensive. Implicit CoT removes intermediate steps progressively during fine-tuning so the reasoning is carried in hidden states instead, and it works empirically without any theory saying when or how internalization succeeds. Its standard curriculum also removes steps one at a time, so training scales linearly with chain length.

## Contributions

- The first theoretical analysis of implicit chain of thought, establishing that explicit CoT's sample efficiency survives internalization into hidden states
- The Log-ICoT curriculum, deleting thinking tokens in geometric chunks aligned to the parity tree's recursive levels
- A proof that an L-layer transformer under Log-ICoT learns k-parity with poly(n) samples and L = log2 k stages
- A reduction in training stages from linear in chain length to logarithmic
- An extension of prior one-layer parity guarantees to multi-layer architectures
- Experimental visualization of reasoning being absorbed into progressively deeper layers

## Method

k-parity is the testbed because the separation is sharp and known: without intermediate supervision the task is provably hard for finite-precision gradient methods, while with explicit CoT even a one-layer transformer learns it efficiently — so it isolates how CoT makes an expressible solution reachable. The parity target has a recursive tree structure of depth log2 k, and the Log-ICoT curriculum is built to match it: rather than deleting one thinking token per stage, it deletes them in geometric chunks aligned to the tree's levels, so each stage absorbs a whole level of the computation into the weights.

## Results

An L-layer transformer trained under Log-ICoT learns k-parity with poly(n) samples and L = log2 k training stages, matching the sample efficiency of explicit CoT while removing its inference overhead. This reduces the number of training stages from linear in k, as under standard ICoT, to logarithmic, and extends prior parity guarantees from one-layer to multi-layer architectures. Experiments on multi-layer transformers confirm the theory and visualize reasoning being progressively absorbed into deeper layers.

## Limitations

The analysis is for k-parity, whose recursive tree structure is exactly what the geometric curriculum is designed around — so the log2 k stage count is a consequence of that structure and does not obviously transfer to tasks without it. The guarantee concerns sample efficiency and stage count, not what the internalized computation costs in depth: L = log2 k means layers grow with chain length, so inference cost is moved into the architecture rather than removed. Results are on synthetic parity rather than natural reasoning.

## Why it matters here

- **reasoning-training**: Gives the archive's latent-reasoning thread the guarantee it has been missing. That thread is entirely empirical here — soft embeddings collapsing toward the top token, entropy-gated switching, curricula that fail when removed — and this proves the central premise: internalized reasoning need not cost sample efficiency. The curriculum design is the transferable idea and it is sharper than the usual advice: matching the deletion schedule to the target's recursive structure turns a linear number of stages into a logarithmic one, which says the schedule should follow the computation's shape rather than the chain's length. That is a testable prescription for the Coconut-style curricula the archive holds, which delete uniformly.
- **test-time-scaling**: Attacks inference cost from the opposite end to everything else in this topic. Where the archive's methods shorten, prune, compress or stop a trace, this removes the trace entirely and pays for it in training stages and depth — L = log2 k means the layers grow with the reasoning length being absorbed. So the compute is relocated rather than eliminated, from inference to architecture, which is the honest way to read it and makes it directly comparable to the latent-CoT work the archive already holds. It also sharpens the monitorability cost of latent reasoning: a trace absorbed into weights leaves nothing to read at all.

## Entities

- **Concepts**: [latent reasoning](../../../../wiki/concepts/latent-reasoning.md), [implicit reasoning](../../../../wiki/concepts/implicit-reasoning.md), curriculum learning, [sample complexity](../../../../wiki/concepts/sample-complexity.md), parity, [effective depth](../../../../wiki/concepts/effective-depth.md), internalization, [test-time compute](../../../../wiki/concepts/test-time-compute.md), chain of thought
- **Methods**: Log-ICoT, implicit chain of thought, [curriculum learning](../../../../wiki/methods/curriculum-learning.md), [chain of thought](../../../../wiki/methods/chain-of-thought.md), [gradient descent analysis](../../../../wiki/methods/gradient-descent-analysis.md)
- **Datasets**: [Parity](../../../../wiki/datasets/parity.md)

Tags: `implicit cot`, `latent reasoning`, `curriculum`, `parity`, `sample complexity`, `theory`

## Abstract

Chain-of-Thought (CoT) prompting substantially improves the sample efficiency of transformers, reducing the complexity of tasks like parity learning from exponential to polynomial in the input length. However, generating explicit reasoning steps at inference is computationally expensive. Implicit Chain-of-Thought (ICoT) has emerged as a promising empirical remedy that trains models to internalize intermediate steps within their hidden states, but its theoretical foundations remain poorly understood. We give the first theoretical analysis of ICoT, proving that an L-layer transformer trained under our proposed Log-ICoT curriculum learns k-parity with poly(n) samples and L = log2 k training stages. This matches the sample efficiency of explicit CoT while eliminating its inference overhead, and extends prior one-layer parity guarantees to multi-layer architectures. Compared to standard ICoT, which removes thinking tokens one at a time, Log-ICoT removes them in geometric chunks, reducing the number of stages from linear in k to logarithmic. Experiments on multi-layer transformers confirm the theory and visualize how reasoning is progressively absorbed into deeper layers.

---

Record id: `local:ee30f023d9f2d8fb`
