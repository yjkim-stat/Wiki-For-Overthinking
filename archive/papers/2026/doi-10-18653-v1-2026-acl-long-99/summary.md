<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Mechanistic Interpretability Should Prioritize Feature Consistency in Sparse Autoencoders

- **Authors**: Xiangchen Song, Aashiq Muhamed, Yujia Zheng 0001, Lingjing Kong, Zeyu Tang 0002, Mona T. Diab, Virginia Smith, Kun Zhang 0001
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.99>
- **DOI**: 10.18653/V1/2026.ACL-LONG.99
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.75

## In one line

Argues run-to-run feature consistency should be a standard SAE evaluation axis alongside reconstruction and sparsity, and gives a metric showing high consistency is achievable.

## Problem

SAEs are used to decompose activations into interpretable features, and the aspiration to find a canonical feature set is undermined by learned features being inconsistent across training runs. That inconsistency breaks reproducibility and makes model comparison unreliable — if two runs on the same activations give different dictionaries, a claim about a feature is a claim about a run.

## Contributions

- The argument that run-to-run feature consistency belongs alongside reconstruction and sparsity as a standard SAE evaluation axis
- PW-MCC, an assignment-based metric for dictionary consistency across runs
- Theoretical grounding for strong consistency in the idealized TopK SAE setting
- Synthetic validation on a model organism verifying PW-MCC as a proxy for ground-truth recovery
- Empirical demonstration of PW-MCC around 0.80 for TopK SAEs on LLM activations, correlating with explanation similarity

## Method

Run-to-run feature consistency is studied directly and proposed as a reported evaluation axis alongside reconstruction and sparsity. The Pairwise Dictionary Mean Correlation Coefficient is an assignment-based metric quantifying consistency: features are matched between runs before being compared, which is what makes the measure invariant to arbitrary feature ordering. Three lines of support are given — theoretical grounding for strong consistency in the idealized TopK setting, synthetic validation on a model organism verifying PW-MCC as a proxy for ground-truth recovery, and empirical analysis on LLM activations.

## Results

High consistency is achievable with appropriate architectural choices, with PW-MCC around 0.80 for TopK SAEs on LLM activations. In the synthetic setting PW-MCC is verified as a reliable proxy for ground-truth feature recovery. On LLM activations PW-MCC correlates with the similarity of automatically generated natural-language feature explanations.

## Limitations

The theoretical result covers the idealized TopK case, so it does not cover other SAE architectures. PW-MCC around 0.80 is high but not near-identity, so a fifth of the dictionary still differs between runs and which features those are is not characterized. Synthetic validation uses a model organism whose relationship to real activation structure is an assumption. Correlation with automatically generated explanations inherits the reliability of the auto-interpretation pipeline.

## Why it matters here

- **reasoning-interpretability**: Directly conditions how much weight this archive's SAE results can carry. Every claim here that a particular feature does a particular thing was read off one training run, and if a fifth of the dictionary is run-dependent then some fraction of those claims are artefacts of a seed. PW-MCC makes that checkable and the paper shows ~0.80 is reachable, so the fix is architectural rather than hopeless. It is also the most concrete instance of what doi:10.18653/v1/2026.acl-long.159 in this drain calls for — an auditing axis the field should report as standard — and it pairs with arxiv:2608.06300's finding that SAEs improve recoverability while attenuating measured influence: consistency and validity are separate properties, and an SAE can now be shown to have the first without the second.

## Entities

- **Concepts**: sparse autoencoder, [monosemanticity](../../../../wiki/concepts/monosemanticity.md), [reproducibility](../../../../wiki/concepts/reproducibility.md), [feature consistency](../../../../wiki/concepts/feature-consistency.md), [superposition](../../../../wiki/concepts/superposition.md), canonical features, auto-interpretation
- **Methods**: [sparse autoencoder](../../../../wiki/methods/sparse-autoencoder.md), TopK SAE, PW-MCC, assignment-based matching, model organism validation
- **Datasets**: _none recorded_

Tags: `sparse autoencoder`, `reproducibility`, `consistency metric`, `interpretability`, `evaluation axis`

## Abstract

Sparse Autoencoders (SAEs) are a prominent tool in mechanistic interpretability (MI) for decomposing neural network activations into interpretable features. However, the aspiration to identify a canonical set of features is challenged by the observed inconsistency of learned SAE features across different training runs, undermining reproducibility and complicating model comparison. We study run-to-run feature consistency in SAEs and argue that it should be reported as a standard evaluation axis alongside reconstruction and sparsity. We propose the Pairwise Dictionary Mean Correlation Coefficient (PW-MCC) as an assignment-based metric to quantify consistency and demonstrate that high levels are achievable (PW-MCC ≈ 0 . 80 for TopK SAEs on LLM activations) with appropriate architectural choices. Our contributions include: (i) theoretical grounding for strong consistency in the idealized setting of TopK SAEs; (ii) synthetic validation using a model organism , which verifies PW-MCC as a reliable proxy for ground-truth recovery; and (iii) empirical analysis on LLM activations, where PW-MCC correlates with the similarity of automatically generated natural-language feature explanations. We hope these results encourage routine reporting of feature consistency to support more robust cumulative progress in MI. 1

---

Record id: `doi:10.18653/v1/2026.acl-long.99`
