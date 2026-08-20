<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Teaching MLLMs to Say No: Generalized Referring Expression Comprehension via Refusal Calibrated GRPO

- **Authors**: Xuzheng Yang, Jun Ling, Tao Huang, Caiyan Qin, Peng Wang
- **Venue**: cs.CV
- **Published**: 2026-08-05
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.04698>
- **PDF**: <https://arxiv.org/pdf/2608.04698v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.50

## In one line

A GRPO variant that teaches multimodal models to refuse when a referred object is absent, without losing localization accuracy on cases where it is present.

## Problem

Generalized Referring Expression Comprehension requires localizing a described object when it exists and refusing to output when it does not. Multimodal LLMs localize well but rarely reject nonexistent objects, because negative samples are absent from training, so they emit hallucinated bounding boxes. Existing SFT and RL post-training improves refusal but degrades localization on positives.

## Contributions

- The GREC formulation of refusal-calibrated post-training for MLLMs
- RC-GRPO: forced 'None' rollouts for valid advantage estimation on negatives, plus an over-refusal penalty on positives
- A second-stage reasoning reinforcement step
- Evaluation on three GREC benchmarks

## Method

Refusal-Calibrated GRPO forces 'None' outputs in rollouts so that negative samples yield a valid advantage estimate — without this the group has no variance to learn from — and adds a penalty against over-refusal on positive samples to keep the trade-off balanced. A second-stage reasoning reinforcement follows, described as consolidating causal understanding and interpretability.

## Results

On three GREC benchmarks, RC-GRPO attains higher localization accuracy while retaining refusal capability. No numbers are given in the abstract.

## Limitations

No quantitative results in the abstract, so the size of the trade-off improvement is unstated. The benchmarks are not named. The claim that the second reasoning stage consolidates causal understanding and interpretability is asserted without a stated measurement.

## Why it matters here

- **reasoning-training**: Peripheral to reasoning, but it isolates a real defect in GRPO that this topic does care about: when every rollout in a group gets the same reward, the group-relative advantage is zero and the batch teaches nothing. Negative samples with no valid output are the degenerate case, and forcing a canonical 'None' rollout is one answer to it. The task itself is visual grounding, not reasoning, and no reasoning benchmark is reported.

## Entities

- **Concepts**: [abstention](../../../../wiki/concepts/abstention.md), [hallucination](../../../../wiki/concepts/hallucination.md), [advantage estimation](../../../../wiki/concepts/advantage-estimation.md), over-refusal, reward shaping
- **Methods**: [GRPO](../../../../wiki/methods/grpo.md), RC-GRPO, [supervised fine-tuning](../../../../wiki/methods/supervised-fine-tuning.md), [reinforcement learning post-training](../../../../wiki/methods/reinforcement-learning-post-training.md)
- **Datasets**: _none recorded_

Tags: `grpo`, `multimodal`, `refusal`, `advantage estimation`, `off-topic-candidate`

## Abstract

We tackle the challenging yet underexplored task of Generalized Referring Expression Comprehension (GREC), which requires a model to localize the object described by a textual expression when it exists (positive sample) and to refuse output when it does not (negative sample). Although Multimodal Large Language Models (MLLMs) excel at localizing existing objects, they often fail to reject nonexistent ones due to the absence of negative samples during training, producing hallucinated bounding boxes. Existing post-training approaches such as supervised fine-tuning (SFT) and reinforcement learning (RL) enhance refusal behavior but usually degrade localization accuracy on positive samples, undermining the model's core competence. To address this, we propose Refusal-Calibrated Group Relative Policy Optimization (RC-GRPO), a calibrated RL strategy that strengthens the refusal ability of MLLMs while preserving localization performance. It enforces "None" outputs in rollouts for valid advantage estimation on negative samples and applies a penalty to prevent over-refusal on positives, achieving a balanced trade-off between accuracy and reliability. A second-stage reasoning reinforcement further consolidates causal understanding and interpretability. Experiments on three GREC benchmarks demonstrate that RC-GRPO attains superior localization accuracy while maintaining strong refusal capability.

---

Record id: `arxiv:2608.04698`
