<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Tight Sample Complexity of Transformers

- **Authors**: Chenxiao Yang, Nathan Srebro, Zhiyuan Li
- **Venue**: COLT
- **Published**: 2026-01-01
- **Source**: local
- **Topics**: reasoning-training

## In one line

Pins down the VC dimension of transformers as depth times parameters times a logarithm, and shows chain-of-thought learning by teacher forcing costs only logarithmically more as the number of reasoning steps grows.

## Problem

A transformer's parameter count is independent of sequence length, so one might expect sample complexity to be too, but there was no precise account of how it depends on input length, depth and the rest of the architecture. Without that, expressivity results cannot be translated into learning guarantees, and the inductive bias of transformers cannot be compared with that of feed-forward networks.

## Contributions

- A tight characterization of transformer VC dimension: O(LW log(TW)) upper bound with a nearly matching Omega(LW log(TW/L)) lower bound
- Confirmation that the multiplicative log T dependence on sequence length is real and tight, not an artefact of loose analysis
- A tight sample-complexity characterization for chain-of-thought learning by teacher forcing, O(LW log((T+T')W))
- A matching lower bound for any learning rule that uses chain-of-thought data
- A bridge from representational-power results to actual learning guarantees for transformers

## Method

Parametric rather than norm-based capacity is analysed: weights may be arbitrary reals and the object of study is the VC dimension, which tightly characterizes the sample complexity of PAC learning. The architecture is token embedding, ReLU feed-forward layers, hard-attention layers with any number of heads, greedy decoding, arbitrary fixed additive positional encodings including none, skip connections, and no layer normalization. Hard attention is chosen deliberately: softmax hides a logistic activation, and sigmoidal activations are known to make VC dimension behave badly for feed-forward networks. Chain-of-thought learning is analysed as teacher forcing — selecting a predictor consistent with the entire chain on the training data — with T the input length and T' the number of autoregressive steps. The paper is explicit that 'learning' means statistical learning, ignoring the computational problem of finding a risk minimizer.

## Results

The VC dimension of depth-L transformers with W total parameters is O(LW log(TW)) with a nearly matching lower bound of Omega(LW log(TW/L)), so both the O(LW log W) dependence and the multiplicative log T factor are tight. For chain-of-thought learning, teacher forcing has sample complexity O(LW log((T + T')W)), and any learning rule using chain-of-thought data needs at least Omega(LW log((T + T')W/L)) examples. The dependence on sequence length and on the number of reasoning steps is therefore logarithmic, and the two enter only through their sum.

## Limitations

Hard attention is analysed rather than the softmax attention that is deployed, and the paper explains this is because softmax reintroduces the difficulties known from sigmoidal networks — so the result characterizes a neighbouring architecture. Layer normalization is excluded and positional encodings must be fixed rather than learned. The analysis is statistical only: it bounds how many examples suffice, not whether optimization finds the minimizer, which the authors state directly. Parametric capacity ignores weight magnitudes, so this is a baseline for scale-sensitive analyses rather than a replacement.

## Why it matters here

- **reasoning-training**: Prices chain-of-thought supervision, which this archive has discussed extensively in terms of what it teaches and never in terms of what it costs statistically. The answer is reassuring and specific: T and T' enter only inside a logarithm and only through their sum, so training on chains ten times longer needs barely more data. That undercuts any argument that long-CoT supervision is data-hungry because the sequences are long — if it is expensive, the expense is compute or annotation, not sample complexity. The matching lower bound also says no cleverer learning rule escapes the LW log dependence, so the archive's distillation and self-distillation methods are competing on constants and on optimization, not on statistical efficiency. Read with the archive's PAC-Bayes entry, the two give complementary halves: this one bounds capacity by parameter count, that one by the target function's Fourier structure.

## Entities

- **Concepts**: [sample complexity](../../../../wiki/concepts/sample-complexity.md), [VC dimension](../../../../wiki/concepts/vc-dimension.md), [generalization](../../../../wiki/concepts/generalization.md), teacher forcing, [expressivity-learnability gap](../../../../wiki/concepts/expressivity-learnability-gap.md), inductive bias, hard attention, [chain of thought](../../../../wiki/concepts/chain-of-thought.md)
- **Methods**: VC dimension analysis, [teacher forcing](../../../../wiki/methods/teacher-forcing.md), PAC learning, chain of thought
- **Datasets**: _none recorded_

Tags: `sample complexity`, `vc dimension`, `learning theory`, `teacher forcing`, `chain of thought`

## Abstract

We tightly characterize the VC dimension of depth-L Transformers with a total of W parameters, mapping an input sequence of length T to a single output, establishing an upper bound of O(LW log(TW)) and a nearly matching lower bound of Omega(LW log(TW/L)). We further tightly characterize the sample complexity of chain-of-thought learning using such a Transformer, showing that teacher forcing (i.e. selecting a predictor consistent with the entire chain-of-thought on training data) learns with sample complexity O(LW log((T + T')W)) and that any learning rule that uses chain-of-thought data requires at least Omega(LW log((T + T')W/L)) examples, where T is the input length and T' is the number of autoregressive steps.

---

Record id: `local:209065fd89f43691`
