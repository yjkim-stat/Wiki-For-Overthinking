<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ADaPT: Token-Level Decoupling for Efficient Large Reasoning Models

- **Authors**: Tingyun Li, Zishang Jiang, Jinyi Han, Xinyi Wang, Sihang Jiang 0001, Han Xia, Zhaoqian Dai, Shuguang Ma, Fei Yu, Jiaqing Liang, Yanghua Xiao
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.findings-acl.165>
- **DOI**: 10.18653/V1/2026.FINDINGS-ACL.165
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.80

## In one line

Attributes efficiency-training damage to sequence-level coupling between efficiency and correctness rewards, and decouples them by applying the efficiency reward only to a single mode-selection token.

## Problem

Long CoT is costly and applying it uniformly wastes compute, but existing efficiency methods degrade reasoning capability. The paper identifies the root cause as sequence-level coupling between efficiency incentives and correctness optimization, which implicitly penalizes long but correct reasoning trajectories — the penalty cannot distinguish length that was needed from length that was not.

## Contributions

- Identification of sequence-level coupling between efficiency and correctness rewards as the cause of capability degradation in efficient-reasoning methods
- ADaPT, a token-level dual-process framework decoupling the two signals
- A mode-selection token receiving the efficiency reward exclusively, avoiding penalties on long correct trajectories
- Continuous inference-time traversal of the efficiency-performance Pareto frontier by adjusting one token's generation probability from a single trained model

## Method

Adaptive Dual-Process Thinking is a token-level dual-process framework that explicitly decouples the two signals. A mode-selection token controls fast versus slow reasoning, and efficiency-related rewards are applied exclusively to that token, so a correct long trajectory is never penalized for its length. At inference, adjusting the generation probability of the mode-selection token moves a single trained model continuously along the efficiency-performance Pareto frontier.

## Results

Across multiple benchmarks, ADaPT substantially reduces inference cost while maintaining strong reasoning performance. No numbers, benchmarks or models are given in the abstract.

## Limitations

No quantitative results, benchmarks or models in the abstract. Confining the efficiency reward to one token makes the mode decision the only place efficiency pressure applies, so redundancy within a chosen slow trajectory is unaddressed. Continuous inference-time control is claimed but its calibration across problem difficulties is not reported.

## Why it matters here

- **reasoning-training**: Diagnoses a specific reward-design error rather than proposing another length penalty: applying an efficiency reward at sequence level punishes correct long reasoning, so the standard recipe trains against the behaviour it wants to keep. That is a credit-assignment claim, and confining the reward to one decision token is a clean fix for it. It is the fourth mechanism in this drain for the same difficulty-allocation decision — alongside self-confidence (industry.152), injected difficulty cues (long.1766) and per-query token budgets (long.2122) — and the only one that gives continuous post-training control from a single checkpoint, which makes it the most practical of the four and the one whose absence of reported numbers is most frustrating.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), reward shaping, [credit assignment](../../../../wiki/concepts/credit-assignment.md), dual-process theory, [Pareto frontier](../../../../wiki/concepts/pareto-frontier.md), adaptive compute allocation, mode selection
- **Methods**: ADaPT, [reinforcement learning post-training](../../../../wiki/methods/reinforcement-learning-post-training.md), mode-selection token, [length control](../../../../wiki/methods/length-control.md)
- **Datasets**: _none recorded_

Tags: `overthinking`, `reward shaping`, `dual-process`, `pareto`, `mode selection`

## Abstract

Large reasoning models rely on long chain-of-thought to achieve strong performance, but applying such reasoning uniformly incurs high computational cost. Existing efficiency-oriented methods attempt to shorten or mix reasoning strategies, yet often degrade reasoning capability. We identify the root cause as sequence-level coupling between efficiency incentives and correctness optimization, which implicitly penalizes long but correct reasoning trajectories. To address this issue, we propose Adaptive Dual-Process Thinking (ADaPT), a token-level dual-process framework that explicitly decouples efficiency and correctness signals during training. ADaPT introduces a mode-selection token to control fast and slow reasoning, applying efficiency-related rewards exclusively to this token to avoid penalizing correct long reasoning while encouraging efficiency when appropriate. Moreover, ADaPT enables precise and continuous control over the efficiency-performance trade-off at inference time: by adjusting the generation probability of the mode-selection token, a single trained model can smoothly move along the efficiency-performance Pareto frontier. Extensive experiments demonstrate that ADaPT significantly reduces inference cost while maintaining strong reasoning performance across multiple benchmarks.

---

Record id: `doi:10.18653/v1/2026.findings-acl.165`
