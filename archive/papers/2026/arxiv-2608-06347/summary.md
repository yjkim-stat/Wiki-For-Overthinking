<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# RP-OPSD: Reasoning-Pivot-Guided On-Policy Self-Distillation for Multilingual Reasoning Transfer

- **Authors**: Xinye Wang, Junxiao Liu, Shujian Huang
- **Venue**: cs.CL
- **Published**: 2026-08-06
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.06347>
- **PDF**: <https://arxiv.org/pdf/2608.06347v1>
- **Topics**: reasoning-evaluation, reasoning-training
- **Relevance score**: reasoning-evaluation 0.50, reasoning-training 0.40

## In one line

Concentrates privileged self-distillation on reasoning pivots identified by the teacher's distributional shift when an English reference solution is added or removed, for multilingual reasoning transfer.

## Problem

Reasoning transfer beyond high-resource languages is needed to extend LLM reasoning. On-policy self-distillation gives dense token-level supervision on student rollouts, but its objectives do not explicitly prioritize the reasoning signals most critical to cross-lingual transfer.

## Contributions

- A characterization of target-language reasoning as surface text plus reasoning pivots
- RP-OPSD: using the teacher's distributional shift with and without an English reference solution as an operational pivot proxy
- Concentration of privileged distillation and reference anchoring on those pivots
- Results over 17 languages and multiple difficulty levels against multilingual and OPSD baselines
- An analysis showing the learned weighting favours reasoning-control and state-update tokens over surface realization

## Method

Target-language reasoning is characterized as generating both surface text and reasoning pivots — decisions that advance or redirect the reasoning process and shape subsequent inference. RP-OPSD uses the distributional shift between matched teacher views, one with and one without an English reference solution, as an operational proxy for locating those pivots, and concentrates privileged distillation and reference anchoring there. The paired-view construction is what makes the proxy computable without pivot labels: tokens whose distribution moves when the reference is supplied are the ones the reference decides.

## Results

On mathematical reasoning benchmarks covering 17 languages and multiple difficulty levels, RP-OPSD outperforms strong multilingual reasoning baselines and OPSD variants. Analysis shows it concentrates privileged distillation on reasoning-control and problem-conditioned state-update tokens while downweighting tokens that mainly support surface realization.

## Limitations

No effect sizes, benchmark names or model scales in the abstract. The pivot proxy is defined by sensitivity to an English reference, so it presupposes English as the anchor and identifies pivots relative to that anchor rather than intrinsically. Restricted to mathematical reasoning. The claim that the method separates reasoning-control tokens from surface-realization tokens is an analysis of its own weights, not an independent validation.

## Why it matters here

- **reasoning-evaluation**: Matched on benchmark vocabulary rather than evaluation content. Its value here is coverage: 17 languages and stratified difficulty is a wider evaluation surface than the English math benchmarks the archive is dominated by, and it separates reasoning content from surface realization, which is a distinction English-only benchmarks cannot make because the two are confounded.
- **reasoning-training**: Adds a sixth criterion to the archive's token-selection dispute, and the only one defined counterfactually: a token is important if the teacher's distribution over it moves when a reference solution is supplied. Every other criterion tracked here — entropy, marginal utility, log-probability gap, advantage magnitude — is read off a single forward pass, so this one is measuring a different quantity and its overlap with the others is unknown and worth measuring. Sits with arxiv:2608.05987 and arxiv:2608.06243 as a third OPSD variant in one batch, which is itself evidence that privileged self-distillation is consolidating into a named subfield.

## Entities

- **Concepts**: [cross-lingual transfer](../../../../wiki/concepts/cross-lingual-transfer.md), reasoning pivot, [process supervision](../../../../wiki/concepts/process-supervision.md), [credit assignment](../../../../wiki/concepts/credit-assignment.md), [privileged information](../../../../wiki/concepts/privileged-information.md), [token selection](../../../../wiki/concepts/token-selection.md), surface realization
- **Methods**: RP-OPSD, [on-policy self-distillation](../../../../wiki/methods/on-policy-self-distillation.md), [token-level distillation](../../../../wiki/methods/token-level-distillation.md), reference anchoring, counterfactual view comparison
- **Datasets**: _none recorded_

Tags: `multilingual`, `self-distillation`, `token selection`, `reasoning pivot`, `cross-lingual transfer`

## Abstract

Multilingual reasoning transfer is crucial for extending reasoning capabilities of large language models (LLMs) beyond high-resource languages. On-policy self-distillation (OPSD) and its variants have emerged as a promising paradigm, providing dense token-level supervision on student-generated rollouts, yet their objectives do not explicitly prioritize reasoning signals most critical to cross-lingual transfer. We characterize that target-language reasoning comprises the generation of both surface text and reasoning pivots, which are decisions that advance or redirect the reasoning process and shape subsequent inference. This motivates concentrating privileged distillation around such pivots. We therefore propose RP-OPSD, Reasoning-Pivot-guided On-Policy Self-Distillation, using the distributional shift between matched teacher views with and without an English reference solution as an operational proxy to guide privileged distillation and reference anchoring. Experiments on mathematical reasoning benchmarks covering 17 languages and multiple difficulty levels show that our method outperforms strong multilingual reasoning baselines and OPSD variants. Further analysis reveals that RP-OPSD concentrates privileged distillation on reasoning-control and problem-condistioned state-update tokens, while downweighting it for tokens that mainly support surface realization. Our code is available at https://github.com/NJUNLP/RP-OPSD.

---

Record id: `arxiv:2608.06347`
