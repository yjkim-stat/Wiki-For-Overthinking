<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Beyond Reasoning Gains: Mitigating General-Capability Forgetting in Large Reasoning Models

- **Authors**: Hoang Phan, Xianjun Yang, Yuanshun Yao, Jingyu Zhang, Shengjie Bi, Xiaocheng Tang, Madian Khabsa, Lijuan Liu, Deren Lei
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.findings-acl.1717>
- **DOI**: 10.18653/V1/2026.FINDINGS-ACL.1717
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.80

## In one line

Confirms that prolonged RLVR makes models forget foundational skills, and counters it with experience replay whose objective weights adapt online to convergence and instability signals.

## Problem

RLVR is now standard post-training for language and vision-language models, and it risks capability regression: models forget foundational skills after prolonged training without regularization. KL-style regularization is computed on the current task, so it prevents deviation from the base model without guaranteeing retention of broader knowledge. Experience replay across heterogeneous domains raises the question of how much focus each objective should get, which is nontrivial to decide.

## Contributions

- Empirical confirmation that open-source reasoning models degrade on core capabilities including perception and faithfulness after prolonged RLVR
- The argument that task-local KL regularization does not guarantee preservation of broader knowledge
- RECAP, replay with online dynamic objective reweighting driven by convergence and instability signals
- An end-to-end method applicable to existing RLVR pipelines with no additional models trained
- Results on Qwen2.5-VL-3B and Qwen2.5-VL-7B preserving general capabilities while improving reasoning

## Method

RECAP is a replay strategy with dynamic objective reweighting for general knowledge preservation. The reweighting adapts online using short-horizon signals of convergence and instability, shifting focus away from saturated objectives toward underperforming or volatile ones — so the mixture is decided by observed training dynamics rather than fixed in advance. It is end-to-end, applies to existing RLVR pipelines, and trains no additional models.

## Results

The capability-regression concern is empirically confirmed: open-source reasoning models degrade on core capabilities such as perception and faithfulness. On benchmarks based on Qwen2.5-VL-3B and Qwen2.5-VL-7B, RECAP preserves general capabilities and also improves reasoning by enabling more flexible trade-offs among in-task rewards.

## Limitations

Effect sizes are not given in the abstract. Both backbones are Qwen2.5-VL, so results are within one family and modality setting. Replay requires held data representing the capabilities to preserve, and which capabilities are covered determines what is retained — forgetting outside the replay set is unaddressed. Short-horizon convergence and instability signals introduce hyperparameters whose sensitivity is unreported.

## Why it matters here

- **reasoning-training**: Names and measures a cost of the training signal this topic is built around, and the specific capabilities it reports losing are pointed: perception and faithfulness. Faithfulness degrading under RLVR would mean the archive's faithfulness findings are partly a consequence of reasoning training rather than an independent property of models, which is a causal link nothing else here provides. It also shows KL-to-base is the wrong instrument because it is computed on-task, which is worth recording since KL regularization is the field's default answer to regression. With acl-long.1878 on controllability and findings-acl.1456 on trace-level instruction following, this drain now has three independent measurements of what reasoning training costs outside the reasoning benchmark.

## Entities

- **Concepts**: [catastrophic forgetting](../../../../wiki/concepts/catastrophic-forgetting.md), capability regression, experience replay, KL regularization, [chain of thought faithfulness](../../../../wiki/concepts/chain-of-thought-faithfulness.md), [training dynamics](../../../../wiki/concepts/training-dynamics.md), objective reweighting
- **Methods**: RECAP, [RLVR](../../../../wiki/methods/rlvr.md), experience replay, KL divergence regularization, dynamic objective reweighting
- **Datasets**: _none recorded_

Tags: `catastrophic forgetting`, `rlvr`, `experience replay`, `capability regression`, `faithfulness`

## Abstract

,

---

Record id: `doi:10.18653/v1/2026.findings-acl.1717`
