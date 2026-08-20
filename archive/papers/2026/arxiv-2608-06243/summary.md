<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# DASH: Divergence-Adaptive Supervision Horizons for On-Policy Self-Distillation of Reasoning Models

- **Authors**: ZhiYan Hou, Xinyu Tang, Hongyan An, Jianjin Zhang, Weizhen Wang, Yunyun Han, Gengsheng Li, Xiangzhao Hao, Haiyun Guo, Wenbin Hu, Jinqiao Wang, Yafeng Deng
- **Venue**: cs.AI
- **Published**: 2026-08-06
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.06243>
- **PDF**: <https://arxiv.org/pdf/2608.06243v1>
- **Topics**: reasoning-evaluation, reasoning-training
- **Relevance score**: reasoning-evaluation 0.50, reasoning-training 0.79

## In one line

Weights on-policy self-distillation supervision by how each local teacher-student divergence compares to the sequence mean, gating backward multi-step aggregation on that comparison.

## Problem

RLVR signals are sparse and sequence-level. On-policy self-distillation densifies them by querying a privileged teacher at student-visited prefixes, but standard OPSD gives every local divergence the same coefficient regardless of position or of the divergence sequence it sits in. The same divergence magnitude can follow different discrepancy histories, and a local scalar alone cannot distinguish those temporal contexts.

## Contributions

- The observation that standard OPSD ignores the temporal structure of the divergence sequence, weighting equal magnitudes equally regardless of history
- DASH: an adaptive propagation gate from the local-versus-sequence-mean divergence gap
- Gate-controlled backward multi-step aggregation of token-level supervision weights
- Improvement over matched vanilla OPSD on every benchmark at all three scales, with no additional teacher or student forward pass

## Method

DASH maps the gap between each local distillation signal and the sequence-level mean to an adaptive propagation gate, then uses those gates to control backward multi-step aggregation. Token-level supervision weights therefore depend on how divergences evolve over the rollout rather than on their instantaneous size. It reuses the teacher and student distributions OPSD already computes, so it costs no extra forward pass.

## Results

On three mathematical reasoning benchmarks across three model scales, DASH improves over matched vanilla OPSD reruns on every benchmark at all three scales. Effect sizes are not given in the abstract.

## Limitations

No effect sizes, benchmark names or model scales in the abstract, so the improvement is directional only. The baseline is the authors' own matched OPSD reruns, which is the right comparison but leaves the absolute standing against other dense-supervision methods unstated. Requires a privileged teacher. The sequence-level mean as the reference point makes each token's weight depend on the whole rollout, so weights are not available online during generation.

## Why it matters here

- **reasoning-evaluation**: Matched on benchmark vocabulary; it contributes no evaluation method. The one point for this topic is its baseline discipline — improvements are measured against the authors' own matched OPSD reruns rather than against published numbers, which is the practice the archive's evaluation-noise thread found almost universally absent and which is what makes a same-scale comparison trustworthy.
- **reasoning-training**: Isolates a specific defect in dense supervision: the coefficient on a token's divergence should depend on the discrepancy history it sits in, not just its magnitude. That reframes the token-weighting question this archive tracks — where the dispute has been which tokens to select — as a question about trajectory context rather than per-token scores. Costs nothing extra, since it reuses distributions OPSD already computes, so the claim is about the weighting rule alone.

## Entities

- **Concepts**: [process supervision](../../../../wiki/concepts/process-supervision.md), [credit assignment](../../../../wiki/concepts/credit-assignment.md), [privileged information](../../../../wiki/concepts/privileged-information.md), divergence, temporal weighting, signal sparsity
- **Methods**: DASH, [on-policy self-distillation](../../../../wiki/methods/on-policy-self-distillation.md), [RLVR](../../../../wiki/methods/rlvr.md), KL divergence weighting, backward aggregation
- **Datasets**: _none recorded_

Tags: `self-distillation`, `credit assignment`, `token weighting`, `rlvr`, `math reasoning`

## Abstract

Reinforcement learning with verifiable rewards (RLVR) improves the reasoning capabilities of large language models using automatically verifiable outcome signals, but these signals are typically sparse and at the sequence-level. On-policy self-distillation (OPSD) mitigates this sparsity by querying a privileged teacher at student-visited prefixes and providing dense token-level distributional supervision. Although this dense supervision alleviates signal sparsity, we find that standard OPSD still underexploits the temporal structure of the rollout. It assigns every local divergence the same coefficient, regardless of its position or the divergence sequence in which it occurs. In on-policy autoregressive generation, the same divergence magnitude can follow different discrepancy histories, reflecting different evolutions of the mismatch between the teacher and student. Since the local scalar alone cannot distinguish these temporal contexts, standard OPSD cannot adapt its token-level weights to the realized discrepancy sequence. To address this limitation, we propose Divergence-Adaptive Supervision Horizons (DASH). DASH maps the gap between each local distillation signal and the sequence-level mean to an adaptive propagation gate and then uses these gates to control backward multi-step aggregation. By doing so, DASH adjusts token-level supervision weights according to how local divergences evolve during generation. Experiments on three mathematical reasoning benchmarks across three model scales show that DASH improves over our matched vanilla OPSD reruns on every benchmark at all three scales. DASH reuses the teacher and student distributions that OPSD already computes, so the gains require no additional teacher or student forward pass. Code: https://github.com/DBtxy/DASH-OPSD

---

Record id: `arxiv:2608.06243`
