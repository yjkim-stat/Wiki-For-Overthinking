<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# MR-ALIGN: Meta-Reasoning Informed Factuality Alignment for Large Reasoning Models

- **Authors**: Xinming Wang, Jian Xu 0015, Bin Yu, Sheng Lian, Yi Chen 0027, Boran Wang, Yingjian Zhu, Hongzhu Yi, Hongming Yang, Han Hu, Cheng-Lin Liu 0001, Xu-Yao Zhang
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.findings-acl.204>
- **DOI**: 10.18653/V1/2026.FINDINGS-ACL.204
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.80

## In one line

Improves factuality by reweighting reasoning segments according to state-transition probabilities along the thinking process, targeting a gap where correct facts appear in reasoning but not in the answer.

## Problem

Reasoning models gain little on evidence-dependent factual questions. The paper attributes this partly to a reasoning-answer hit gap: the model identifies the correct facts during reasoning yet fails to carry them into the final response, so factual fidelity drops for reasons that have nothing to do with knowledge.

## Contributions

- Identification of the reasoning-answer hit gap: correct facts found during reasoning but not incorporated into the final response
- MR-ALIGN, a meta-reasoning informed factuality alignment framework requiring no external verifier
- A transition-aware implicit reward from state-transition probabilities along the thinking process
- Reshaping of token-level signals into probability-aware segment scores at atomic thinking segments
- Consistent accuracy and truthfulness gains across four factual QA datasets and one long-form factuality benchmark

## Method

MR-ALIGN is a meta-reasoning informed alignment framework needing no external verifier. It quantifies state-transition probabilities along the model's thinking process and builds a transition-aware implicit reward that reinforces beneficial reasoning patterns and suppresses defective ones at the level of atomic thinking segments. That reweighting reshapes token-level signals into probability-aware segment scores, favouring coherent trajectories more likely to end in a correct answer. Deriving the reward from transition statistics is what removes the need for an external verifier.

## Results

Across four factual QA datasets and one long-form factuality benchmark, MR-ALIGN consistently improves accuracy and truthfulness while reducing misleading reasoning. No numbers, datasets or models are named in the abstract.

## Limitations

No quantitative results, dataset names or models in the abstract. The implicit reward is derived from the model's own transition statistics, so it reinforces patterns that correlate with correctness in the training distribution rather than correctness itself. Atomic thinking segments require a segmentation whose definition is unstated. 'Reducing misleading reasoning' is claimed without a stated measure.

## Why it matters here

- **reasoning-training**: The reasoning-answer hit gap it names is the same dissociation this drain reports three other times — harm recognized then overridden (findings-acl.1118), safety cues perceived then lost to narrative (acl-long.1821), the correct proverb ending stated then not selected (arxiv:2608.04670). Here it is factual content found and dropped. Four independent papers, four domains, one structure: the information is present in the trace and fails to reach the answer. That converges on a claim the archive can hold as its own — the trace-to-answer step is a distinct failure site — and it means outcome-only rewards cannot fix these cases, because the outcome is wrong while the reasoning was right. MR-ALIGN's transition-based implicit reward is one answer that needs no verifier, which matters where facts cannot be checked automatically.

## Entities

- **Concepts**: factuality, reasoning-answer gap, [process supervision](../../../../wiki/concepts/process-supervision.md), [credit assignment](../../../../wiki/concepts/credit-assignment.md), state transition, [truthfulness](../../../../wiki/concepts/truthfulness.md), [chain of thought faithfulness](../../../../wiki/concepts/chain-of-thought-faithfulness.md), segment scoring
- **Methods**: MR-ALIGN, implicit reward modelling, [meta-reasoning](../../../../wiki/methods/meta-reasoning.md), segment-level reweighting
- **Datasets**: _none recorded_

Tags: `factuality`, `reasoning-answer gap`, `implicit reward`, `process supervision`, `alignment`

## Abstract

Large reasoning models (LRMs) show strong capabilities in complex reasoning, yet their marginal gains on evidence-dependent factual questions are limited. We find this limitation is partially attributable to a reasoning–answer hit gap, where the model identifies the correct facts during reasoning but fails to incorporate them into the final response, thereby reducing factual fidelity. To address this issue, we propose MR-ALIGN, a Meta-Reasoning informed alignment framework that enhances factuality without relying on external verifiers. MR-ALIGN quantifies state-transition probabilities along the model’s thinking process and constructs a transition-aware implicit reward that reinforces beneficial reasoning patterns while suppressing defective ones at the atomic thinking segments. This re-weighting reshapes token-level signals into probability-aware segment scores, encouraging coherent reasoning trajectories that are more conducive to factual correctness. Empirical evaluations across four factual QA datasets and one long-form factuality benchmark show that MR-ALIGN consistently improves accuracy and truthfulness while reducing misleading reasoning. These results highlight that aligning the reasoning process itself, rather than merely the outputs, is pivotal for advancing factuality in LRMs.

---

Record id: `doi:10.18653/v1/2026.findings-acl.204`
