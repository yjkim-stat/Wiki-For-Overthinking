<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Reasoning Structure Matters for Safety Alignment of Reasoning Models

- **Authors**: Yeonjun In, Wonjoong Kim, Sangwu Park, Chanyoung Park 0001
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.240>
- **DOI**: 10.18653/V1/2026.ACL-LONG.240
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.67

## In one line

Argues reasoning models' safety failures come from the reasoning structure itself, and achieves safety alignment by altering that structure with 1K supervised examples and no RL.

## Problem

Reasoning models perform well but generate harmful responses to malicious queries. The paper's claim is that the cause is not missing safety knowledge but the reasoning structure, so interventions on content leave the failure in place.

## Contributions

- The claim that reasoning-model safety risk originates in the reasoning structure rather than in content
- AltTrain, a post-training method that explicitly alters reasoning structure
- An SFT-only recipe needing no RL or reward design and only 1K training examples
- Reported safety alignment across backbones and sizes with generalization to reasoning, QA, summarization and multilingual settings

## Method

AltTrain is a post-training method that explicitly alters the reasoning structure of reasoning models. It requires no reinforcement learning and no reward design, only supervised fine-tuning on a lightweight set of 1K training examples. That 1K examples suffice is itself the evidence for the structural claim: if the fix were knowledge, it would need far more data.

## Results

Across reasoning-model backbones and model sizes, AltTrain achieves strong safety alignment with robust generalization to reasoning, QA, summarization and multilingual settings. No numbers, backbones or benchmarks are given in the abstract.

## Limitations

No quantitative results, named backbones or benchmark names in the abstract, so both the safety gain and the retained capability are unverified from this text. 'Reasoning structure' is not defined here, which is the load-bearing concept. Generalization across four task types is asserted rather than quantified. A 1K-example SFT intervention raises the question of robustness to adaptive attack, which is not addressed.

## Why it matters here

- **reasoning-training**: Makes a structural rather than content-based claim about where reasoning-model behaviour is determined, and offers data efficiency as the evidence — 1K SFT examples changing safety behaviour across backbones would mean the target is a reusable pattern, not knowledge. That is the same kind of claim as doi:10.18653/v1/2026.findings-acl.1981 in this drain, which aligns meta-abilities rather than tasks, and both imply reasoning behaviour has a structural layer that can be trained separately from content. Neither defines the structure precisely enough to compare them, and this abstract reports no numbers, so the claim is recorded rather than credited.

## Entities

- **Concepts**: [safety alignment](../../../../wiki/concepts/safety-alignment.md), reasoning structure, [data efficiency](../../../../wiki/concepts/data-efficiency.md), [generalization](../../../../wiki/concepts/generalization.md), [alignment tax](../../../../wiki/concepts/alignment-tax.md)
- **Methods**: AltTrain, [supervised fine-tuning](../../../../wiki/methods/supervised-fine-tuning.md), post-training
- **Datasets**: _none recorded_

Tags: `safety alignment`, `reasoning structure`, `sft`, `data efficiency`, `thin-evidence`

## Abstract

Large reasoning models (LRMs) achieve strong performance on complex reasoning tasks but often generate harmful responses to malicious user queries. This paper investigates the underlying cause of these safety risks and shows that the issue lies in the reasoning structure itself. Based on this insight, we claim that effective safety alignment can be achieved by altering the reasoning structure. We propose AltTrain, a simple yet effective post-training method that explicitly alters the reasoning structure of LRMs. AltTrain is both practical and generalizable, requiring no complex reinforcement learning (RL) training or reward design—only supervised fine-tuning (SFT) with a lightweight 1K training examples. Experiments across LRM backbones and model sizes demon strate strong safety alignment, along with robust generalization across reasoning, QA, summarization, and multilingual setting.

---

Record id: `doi:10.18653/v1/2026.acl-long.240`
