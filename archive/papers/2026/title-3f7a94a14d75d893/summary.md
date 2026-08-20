<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Diversity Matters: Revisiting Test-Time Compute in Vision-Language Models

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/63569>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

An empirical study showing that test-time-compute methods effective for LLM reasoning mostly fail to transfer to vision-language models unless prediction diversity is present, and proposes an entropy-based selection method that works better in multi-model ensembles.

## Problem

Whether test-time compute strategies known to improve LLM reasoning (chain-of-thought feature scoring, self-consistency/majority voting) actually improve accuracy in vision-language models, and under what conditions they do or do not help.

## Contributions

- Empirically shows feature-based scoring of chain-of-thought traces (e.g. length, pivot words) fails to improve VLM accuracy
- Shows confidence-based majority voting yields only modest, CoT-dependent gains for single models, and that its benefit vanishes when outputs are highly correlated (low diversity)
- Shows multi-model ensembles are more effective than single-model self-consistency because of architectural and training differences that increase prediction diversity
- Proposes Entropy-based TTC, which selects the most confident prediction by predictive entropy and leverages confidence disparities across ensemble members to favor stronger models over naive majority voting

## Method

The authors evaluate test-time compute strategies across seven open-source vision-language models and six benchmarks, comparing feature-based scoring of chain-of-thought traces against confidence-based majority voting, in both single-model and multi-model ensemble settings. They find voting's effectiveness depends on prediction diversity across outputs. They then propose Entropy-based TTC, which selects the prediction with lowest predictive entropy (highest confidence) rather than the majority answer, which in ensembles lets stronger models' confident predictions dominate over weaker ones.

## Results

Entropy-based TTC performs comparably to majority voting for single models but outperforms both majority voting and individual models in multi-model ensembles across visual reasoning benchmarks, evaluated across 7 open-source VLMs and 6 benchmarks; specific per-benchmark accuracy numbers are not given in the available abstract.

## Limitations

Naive majority voting weights all models equally and can let a weaker model override a stronger one in an ensemble; feature cues and standard voting largely fail to help single-model accuracy; specific benchmark names and numeric accuracy figures are not given in the available abstract.

## Why it matters here

- **overthinking**: A direct empirical study of test-time compute methods and exactly when more inference-time computation (sampling, voting, confidence aggregation) does or does not improve accuracy -- the central accuracy/efficiency question the topic tracks, here extended from text-only LLM reasoning to vision-language models. Substantive, on-topic contribution.

## Entities

- **Concepts**: [test-time compute](../../../../wiki/concepts/test-time-compute.md), prediction diversity, self-consistency, majority voting, predictive entropy
- **Methods**: Entropy-based TTC, [majority voting](../../../../wiki/methods/majority-voting.md), feature-based chain-of-thought scoring
- **Datasets**: _none recorded_

Tags: `test-time-compute`, `vision-language-models`, `self-consistency`, `majority-voting`, `predictive-entropy`, `on-topic`

---

Record id: `title:3f7a94a14d75d893`
