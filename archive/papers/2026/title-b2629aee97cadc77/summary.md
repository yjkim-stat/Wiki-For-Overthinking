<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# T1: Tool-integrated Verification for Test-time Compute Scaling in Small Language Models

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10007001>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

T1 is a two-stage test-time-scaling framework for small language models that filters candidate responses with external tools before a small-model verifier makes the final judgment, offloading memorization-heavy checks to the tools.

## Problem

Test-time compute scaling for small language models has mainly relied on a larger external model as verifier; whether small language models themselves can reliably verify candidates is underexplored, and they struggle with verification tasks requiring memorization -- numerical calculations, fact-checking -- even with knowledge distillation from larger verifiers.

## Contributions

- Investigates whether small language models can reliably verify output candidates under test-time scaling, finding they struggle with memorization-heavy checks even after distillation from larger verifiers
- Proposes T1, a two-stage tool-integrated verification framework that filters candidates with external tools before a small model performs final verification
- Shows tool offloading reduces the memorization burden on small verifiers and improves test-time scaling performance
- Shows T1 improves verification accuracy of both process reward models and critic models

## Method

T1 is a two-stage framework: it first filters candidate responses using external tools, such as a code interpreter, then uses a small language model for final verification on the filtered candidates. This offloads memorization-heavy verification steps -- numerical calculation, fact-checking -- from the small model to the tools.

## Results

On the MATH benchmark, a Llama-3.2 1B model using T1 under test-time scaling outperforms the larger Llama-3.1 8B model; T1 also improves the verification accuracy of both process reward models (PRMs) and critic models.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Directly concerns test-time compute scaling: proposes a verification method that lets small models allocate extra inference-time compute effectively by offloading memorization to external tools, addressing the verifier-quality mechanism that determines whether extra test-time compute is used well.

## Entities

- **Concepts**: [test-time compute scaling](../../../../wiki/concepts/test-time-compute-scaling.md), verification, tool integration, memorization burden
- **Methods**: T1, code interpreter tool integration, process reward models, critic models
- **Datasets**: [MATH](../../../../wiki/datasets/math.md)

Tags: `test-time-scaling`, `small-language-models`, `verification`, `tool-use`

## Abstract

Abstract Recent studies have demonstrated that test-time compute scaling effectively improves the performance of small language models (sLMs). However, prior research has mainly examined test-time compute scaling with an additional larger model as a verifier, leaving verification by sLMs underexplored. In this work, we investigate whether sLMs can reliably verify the output candidates under test-time scaling. We find that even with knowledge distillation from larger verifiers, sLMs struggle with verification tasks requiring memorization, such as numerical calculations and fact-checking. To address this limitation, we propose Tool-integrated verification (T1), a two-stage framework that first filters candidates with external tools and then uses an sLM for final verification, offloading memorization-heavy steps to tools such as a code interpreter. Within T1 we prove that offloading to external tools reduces the memorization burden on sLMs and improves test-time scaling performance. Experiments on the MATH benchmark demonstrate that, with T1, a Llama-3.2 1B model under test-time scaling outperforms the significantly larger Llama-3.1 8B model. Moreover, T1 improves the verification accuracy of both process reward models (PRMs) and critic models. Our findings highlight the potential of tool integration to substantially improve the verification abilities of sLMs.

---

Record id: `title:b2629aee97cadc77`
