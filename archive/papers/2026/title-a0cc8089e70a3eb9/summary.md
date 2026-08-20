<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Overthinking Reduction with Decoupled Rewards and Curriculum Data Scheduling

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10007765>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

Introduces DECS, a decoupled token-level reward plus curriculum batch scheduling method that cuts reasoning-token length by over 50% while maintaining or improving accuracy in RLVR-trained reasoning models.

## Problem

Large reasoning models trained with critic-free RLVR exhibit "overthinking": generating excessively long reasoning paths without performance benefit. Existing length-penalizing solutions often degrade performance because trajectory-level length rewards are misaligned with token-level optimization.

## Contributions

- Identifies two flaws in current length-based rewards: erroneous penalization of essential exploratory tokens, and inadvertent rewarding of partial redundancy
- Introduces a decoupled token-level reward mechanism that distinguishes and penalizes redundant tokens specifically
- Introduces a curriculum batch scheduling strategy to balance efficiency and efficacy

## Method

DECS is built on a theoretical diagnosis that trajectory-level length rewards misalign with token-level optimization, both erroneously penalizing exploratory tokens and rewarding partial redundancy. It introduces a decoupled token-level reward that surgically distinguishes and penalizes redundant tokens, combined with a curriculum batch scheduling strategy that sequences training data to master the efficiency-efficacy equilibrium.

## Results

Reduces reasoning tokens by over 50% across seven benchmarks while maintaining or improving performance compared to baseline RLVR training.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Directly targets overthinking in RLVR-trained reasoning models: diagnoses why trajectory-level length penalties fail when applied to token-level optimization, then proposes a decoupled token-level reward and curriculum scheduling that cut reasoning tokens by over 50% across seven benchmarks without hurting accuracy.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), trajectory-level vs token-level reward misalignment, reward decoupling, curriculum scheduling
- **Methods**: DECS
- **Datasets**: _none recorded_

Tags: `overthinking`, `rlvr`, `reward-shaping`, `reasoning-efficiency`

## Abstract

Abstract While large reasoning models trained with critic-free reinforcement learning and verifiable rewards (RLVR) represent the state-of-the-art, their practical utility is hampered by ``overthinking'', a critical issue where models generate excessively long reasoning paths without any performance benefit. Existing solutions that penalize length often fail, inducing performance degradation due to a fundamental misalignment between trajectory-level rewards and token-level optimization. In this work, we introduce a novel framework, DECS, built on our theoretical discovery of two previously unaddressed flaws in current length rewards: (1) the erroneous penalization of essential exploratory tokens and (2) the inadvertent rewarding of partial redundancy. Our framework's innovations include (i) a first-of-its-kind decoupled token-level reward mechanism that surgically distinguishes and penalizes redundant tokens, and (ii) a novel curriculum batch scheduling strategy to master the efficiency-efficacy equilibrium. Experimental results show DECS can achieve a dramatic reduction in reasoning tokens by over 50\% across seven benchmarks while simultaneously maintaining or even improving performance. It demonstrates conclusively that substantial gains in reasoning efficiency can be achieved without compromising a model's underlying reasoning power. Code is available at \url{https://github.com/pixas/DECS}.

---

Record id: `title:a0cc8089e70a3eb9`
