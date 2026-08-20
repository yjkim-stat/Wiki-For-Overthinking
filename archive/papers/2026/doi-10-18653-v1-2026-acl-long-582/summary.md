<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Mathematical Proof as a Litmus Test: Revealing Failure Modes of Advanced Large Reasoning Models

- **Authors**: Dadi Guo, Jiayu Liu, Zhiyuan Fan, Zhitao He 0001, Haoran Li, Yuxin Li, Yumeng Wang 0010, Yi R. Fung 0001
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.582>
- **DOI**: 10.18653/V1/2026.ACL-LONG.582
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.80

## In one line

Uses 200 mathematical proof problems as a diagnostic, finding some reasoning models solve under 20% and cataloguing 10 fine-grained error types that numerical benchmarks hide.

## Problem

High reported accuracy on popular datasets, combined with purely numerical evaluation, masks reasoning shortcomings. A numerical answer can be right with a broken derivation, so answer-checking cannot detect failures of rigor.

## Contributions

- The argument that numerical-answer evaluation masks failures of proof rigor
- RFMDataset, 200 diverse mathematical proof problems as a diagnostic instrument
- A taxonomy of 10 fine-grained error types observed in reasoning-model proofs
- Evidence that intermediate-step correctness and rigor are unguaranteed, with hallucination and incompleteness present
- The negative result that prompting self-reflection on named failure modes does not fix the failures

## Method

Mathematical proof is used as a diagnostic because it makes every intermediate step subject to correctness — the rigor is the instrument. RFMDataset is a collection of 200 diverse mathematical proof problems. Failures are analyzed in depth and organized into 10 fine-grained error types. Prompting models to self-reflect on specific failure modes is tested as a remedy.

## Results

Reasoning models have limited capability in generating entirely correct proofs, with some models solving under 20% of problems and making mistakes on fundamental ones. Failures span a diverse spectrum, prominently showing no guarantee of correctness or rigor in intermediate steps, plus hallucination and incompleteness during reasoning. Directly prompting models to self-reflect on specific failure modes is insufficient to resolve the logical problems, which the authors argue requires domain knowledge and formal verification.

## Limitations

200 problems, so per-error-type counts are small. Models are not named and the under-20% figure applies to 'some models' rather than the set. Proof correctness requires expert judgement, and who performed it and with what agreement is not stated. The 10-type taxonomy is derived from these failures and may not generalize beyond this problem set.

## Why it matters here

- **reasoning-training**: The negative result is the useful part for this topic: telling a model exactly which failure mode to watch for does not fix it, which bounds what prompting-level self-correction can achieve and points at training or external verification instead. That converges with arxiv:2608.04355 in this archive, which finds the measured content margin of self-revision near zero — two independent routes to the conclusion that self-correction is weaker than reported. Proof also gives per-step ground truth, making it one of the few domains where step-level supervision can be checked rather than estimated, which is directly relevant to the process-supervision line this topic tracks.

## Entities

- **Concepts**: [construct validity](../../../../wiki/concepts/construct-validity.md), mathematical proof, rigor, [self-correction](../../../../wiki/concepts/self-correction.md), [hallucination](../../../../wiki/concepts/hallucination.md), [process evaluation](../../../../wiki/concepts/process-evaluation.md), formal verification, error taxonomy
- **Methods**: RFMDataset, error taxonomy construction, self-reflection prompting, expert proof evaluation
- **Datasets**: RFMDataset

Tags: `mathematical proof`, `error taxonomy`, `construct validity`, `self-correction`, `benchmark`

## Abstract

Large reasoning models ( e.g., R1, o3) have demonstrated remarkable mathematical problem-solving abilities. However, the high reported accuracy of these advanced models on popular datasets and reliance on purely numerical evaluation often mask their true reasoning shortcomings. To address this, we propose leveraging the inherent rigor and methodological complexity of mathematical proofs as a diagnostic tool to expose these hidden failures. Specifically, we introduce the RFMDataset (Reveal Failure Modes), a collection of 200 diverse mathematical proof problems to thoroughly evaluate the performance of advanced models. Our in-depth analysis of their failures uncovers 10 fine-grained error types, which shows fundamental limitations in current large reasoning models: 1) Large reasoning models still have limited capability in generating entirely correct mathematical proofs, with some models solving less than 20% of problems and even making mistakes on fundamental ones; 2) models exhibit a diverse spectrum of reasoning failures, prominently demonstrating the lack of guarantees for the correctness and rigor intermediate reasoning steps; and 3) models show hallucination and incompleteness during the reasoning process. Our findings also reveal that directly prompting models to self-reflect on specific failure modes is insufficient to resolve the current logical dilemmas, necessitating domain knowledge and formal verification.

---

Record id: `doi:10.18653/v1/2026.acl-long.582`
