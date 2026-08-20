<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Red Teaming Large Reasoning Models

- **Authors**: Jiawei Chen, Yang Yang, Chao Yu, Yu Tian, Zhi Cao, Xue Yang, Linghao Li, Hang Su 0006, Zhaoxia Yin
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.1034>
- **DOI**: 10.18653/V1/2026.ACL-LONG.1034
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.80

## In one line

A trustworthiness benchmark for reasoning models over truthfulness, safety and efficiency, using training paradigm as an analytical axis, and finding reasoning models more fragile than plain LLMs to reasoning-induced risks.

## Problem

Reasoning models expose explicit chains of thought, which brings transparency but also novel safety and reliability risks such as CoT-hijacking and prompt-induced inefficiencies. Existing evaluation methods do not capture these.

## Contributions

- Rt-LRM, a unified LRM trustworthiness benchmark over truthfulness, safety and efficiency
- A curated suite of 30 reasoning tasks including CoT-hijacking and prompt-induced inefficiency risks
- Training paradigm as an analytical axis for comparing trustworthiness
- Evaluation of 26 models, finding LRMs more fragile than LLMs to reasoning-induced risks
- A released toolbox for standardized trustworthiness research

## Method

Rt-LRM is a unified benchmark evaluating three dimensions — truthfulness, safety and efficiency — over a curated suite of 30 reasoning tasks designed from an observational standpoint. Beyond metric-based evaluation it adds the training paradigm as an analytical perspective, so results can be grouped by how a model was trained rather than only by which model it is. A scalable toolbox is released.

## Results

Experiments cover 26 models. LRMs generally face trustworthiness challenges and tend to be more fragile than LLMs when encountering reasoning-induced risks. Further insights are reported but not quantified in the abstract.

## Limitations

No numbers in the abstract, so the fragility gap between LRMs and LLMs is directional only. 30 tasks across three dimensions is thin per dimension. Grouping by training paradigm is observational — models differ in data, scale and paradigm simultaneously, so paradigm effects are confounded. The models are not listed.

## Why it matters here

- **reasoning-training**: Its distinctive move for this topic is treating training paradigm as an explanatory variable for trustworthiness rather than reporting per-model scores, which is the right shape of question — whether RLVR, distillation or process supervision produce differently trustworthy models is exactly what this archive wants to know. The evidence is observational and confounded, so it identifies the question rather than answering it. The headline finding that reasoning models are more fragile than plain LLMs is the inverse of the robustness account in arxiv:2608.04646, and the two disagreeing on the same axis is worth tracking: robustness to benign prompt variation and robustness to adversarial reasoning-directed attack may simply be different quantities.

## Entities

- **Concepts**: trustworthiness, [monitorability](../../../../wiki/concepts/monitorability.md), CoT hijacking, [overthinking](../../../../wiki/concepts/overthinking.md), [truthfulness](../../../../wiki/concepts/truthfulness.md), safety evaluation, training paradigm
- **Methods**: benchmark construction, chain of thought, adversarial prompting
- **Datasets**: Rt-LRM

Tags: `trustworthiness`, `benchmark`, `safety`, `cot hijacking`, `training paradigm`

## Abstract

Large Reasoning Models (LRMs) have emerged as a powerful advancement in multi-step reasoning tasks, offering enhanced transparency and logical consistency through explicit chains of thought (CoT). However, these models introduce novel safety and reliability risks, such as CoT-hijacking and prompt-induced inefficiencies, which are not fully captured by existing evaluation methods. To address this gap, we propose Rt-LRM, a unified benchmark designed to assess the trustworthiness of LRMs. Rt-LRM evaluates three core dimensions: truthfulness, safety and efficiency. Beyond metric-based evaluation, we further introduce the training paradigm as a key analytical perspective to investigate the systematic impact of different training strategies on model trustworthiness. We achieve this by designing a curated suite of 30 reasoning tasks from an observational standpoint. We conduct extensive experiments on 26 models and identify several valuable insights into the trustworthiness of LRMs. For example, LRMs generally face trustworthiness challenges and tend to be more fragile than Large Language Models (LLMs) when encountering reasoning-induced risks. These findings uncover previously underexplored vulnerabilities and highlight the need for more targeted evaluations. In addition, we release a scalable toolbox for standardized trustworthiness research to support future advancements in this important field.

---

Record id: `doi:10.18653/v1/2026.acl-long.1034`
