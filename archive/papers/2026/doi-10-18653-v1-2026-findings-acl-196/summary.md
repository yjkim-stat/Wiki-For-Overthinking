<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# DRP: Distilled Reasoning Pruning with Mathematical Skill-aware Step Decomposition for Efficient Large Reasoning Models

- **Authors**: Yuxuan Jiang, Dawei Li 0008, Francis Ferraro
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.findings-acl.196>
- **DOI**: 10.18653/V1/2026.FINDINGS-ACL.196
- **Topics**: reasoning-training, reasoning-evaluation
- **Relevance score**: reasoning-training 0.80

## In one line

Has a teacher decompose and prune a student's reasoning by mathematical skill, then distills the pruned paths back, on the argument that CoT structure must match student capacity.

## Problem

Reasoning-model outputs are excessively verbose. The problem is amplified in distillation, where a student's long-form reasoning mismatches the concise outputs of smaller teacher models — a mismatch that is common because using large teachers is costly.

## Contributions

- Identification of the structural mismatch between student long-form reasoning and concise smaller-teacher outputs as an obstacle in distillation
- DRP, a hybrid of teacher-driven inference-time pruning and tuning-based distillation
- Mathematical skill-aware step decomposition as the basis for pruning
- GSM8K tokens 917 to 328 with accuracy 91.7% to 94.1%, and 43% AIME token reduction with no drop
- The finding that aligning training CoT structure with student capacity governs transfer effectiveness

## Method

Distilled Reasoning Pruning combines inference-time pruning with tuning-based distillation. A teacher model performs mathematical problem-solving skill-aware step decomposition and pruning, and the refined reasoning paths are then distilled into the student. Decomposing by skill is what lets pruning target steps the student does not need rather than steps that are merely long.

## Results

On GSM8K, tokens fall from 917 to 328 while accuracy rises from 91.7% to 94.1%. On AIME, tokens fall 43% with no performance drop. Further analysis shows that aligning training CoT structure with student capacity is key to effective knowledge transfer.

## Limitations

Two datasets reported, and GSM8K is near-saturated at 91.7% baseline, so the accuracy gain there is within a compressed range. Requires a teacher capable of skill-aware decomposition, so the method inherits the teacher-quality dependence it set out to reduce. Skill taxonomy is specific to mathematics, and transfer to other domains is untested. Student models are not named.

## Why it matters here

- **reasoning-training**: Its transferable claim is about distillation rather than efficiency: what should be transferred is reasoning structured for the student's capacity, not the teacher's reasoning verbatim. That reframes the archive's distillation thread, where traces are generally treated as content to copy, and it gives a reason why distilled models carry removable redundancy — the structure was never matched to them. It also supplies a mechanism for the finding in doi:10.18653/v1/2026.acl-long.1386, where 87.1% of a distilled model's tokens could be removed with accuracy gains: if the structure came from a mismatched teacher, most of it was never load-bearing for the student.

## Entities

- **Concepts**: reasoning distillation, [reasoning redundancy](../../../../wiki/concepts/reasoning-redundancy.md), [overthinking](../../../../wiki/concepts/overthinking.md), skill decomposition, capacity matching, knowledge transfer, [token selection](../../../../wiki/concepts/token-selection.md)
- **Methods**: DRP, [chain of thought distillation](../../../../wiki/methods/chain-of-thought-distillation.md), step decomposition, inference-time pruning
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [AIME](../../../../wiki/datasets/aime.md)

Tags: `distillation`, `pruning`, `overthinking`, `capacity matching`, `math reasoning`

## Abstract

While Large Reasoning Models (LRMs) excel at complex tasks via long Chain-of-Thought (CoT) reasoning, their outputs are often excessively verbose, leading to inefficiency. This problem is amplified when the student’s long-form reasoning mismatches the concise outputs of smaller teacher models—common in LLM distillation to avoid using costly large teachers. To address this issue, we propose Distilled Reasoning Pruning (DRP), a hybrid framework that combines inference-time pruning with tuning-based distillation. DRP leverages a teacher model to perform mathematical problem-solving skill-aware step decomposition and pruning, then distills the refined reasoning paths into a student model, enabling efficient and accurate reasoning. Across challenging math datasets, DRP significantly reduces token usage without sacrificing accuracy—for instance, cutting tokens on GSM8K from 917 to 328 while improving accuracy from 91.7% to 94.1%, and reducing AIME tokens by 43% with no performance drop. Further analysis shows that aligning training CoT structure with the student’s capacity is key to effective knowledge transfer.

---

Record id: `doi:10.18653/v1/2026.findings-acl.196`
