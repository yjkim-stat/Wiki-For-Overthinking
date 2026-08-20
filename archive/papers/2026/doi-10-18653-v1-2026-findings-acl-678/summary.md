<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Self-Reflection Improves Safety of Large Reasoning Models

- **Authors**: Qiang Huang, Wei Zhai, Feng Huang, Dejing Dou
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.findings-acl.678>
- **DOI**: 10.18653/V1/2026.FINDINGS-ACL.678
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.80

## In one line

Adds a Self-Reflection token that lets reasoning models recover from harmful output mid-generation, cutting harmful completion rate from 13.8% to 4.1%.

## Problem

Reasoning models carry greater safety risks than prior language models. Existing alignment methods remain at a shallow protective level, insufficient against deeper risks and strategic attacks that unfold within complex reasoning.

## Contributions

- A reframing of safety alignment from prevention to mid-generation recovery
- A special Self-Reflection token enabling introspection and recovery during generation
- Integration into standard post-training paradigms without targeted adversarial training
- Harmful completion rate reduced from 13.8% to 4.1%, with gains in helpfulness and the safety-helpfulness balance
- Robustness under multiple adversarial attacks including a purpose-built adaptive attack

## Method

The paper moves beyond treating safety alignment purely as prevention of harmful output. Drawing on human introspection and self-correction, Self-Reflection introduces a special Self-Reflection token enabling the model to reflect during generation and recover from harmful output already begun — recovery rather than prevention is the shift, so a trajectory that has gone wrong can still end safely. It integrates into standard post-training paradigms.

## Results

Models trained with Self-Reflection reduce the harmful completion rate from 13.8% to 4.1%, nearly a threefold improvement over mainstream approaches, and gain in helpfulness and in the safety-helpfulness balance. Under various adversarial attacks including a specially designed adaptive attack, Self-Reflection significantly improves safety without targeted adversarial training. The paper notes it contains harmful content.

## Limitations

Base models and benchmarks are not named in the abstract. 4.1% harmful completion remains non-trivial for a safety mechanism. The adaptive attack is designed by the authors, so it bounds robustness against an attack they anticipated rather than against an independent adversary — AutoRAN in this same drain reaches near-100% success against reasoning-based defences. Recovery presupposes the model detects the harm mid-generation, and detection rate is not separated from recovery rate.

## Why it matters here

- **reasoning-training**: Its design follows from the drain's convergent finding that reasoning models override correct early judgements mid-trajectory: if the failure happens partway through, a mechanism that can re-enter safety reasoning partway through is the matching fix, and a learned token is a cheap way to give the model that entry point. The honest reading of its numbers is bounded, though — 13.8% to 4.1% is measured against the authors' own adaptive attack, while AutoRAN in this same drain reports approaching 100% success against reasoning-based defences on frontier models. Two papers in one drain, one hardening reasoning-level defences and one defeating them, is the state of this subfield rather than a contradiction to resolve.

## Entities

- **Concepts**: [safety alignment](../../../../wiki/concepts/safety-alignment.md), [self-correction](../../../../wiki/concepts/self-correction.md), self-reflection, recovery, helpfulness-safety trade-off, [adversarial robustness](../../../../wiki/concepts/adversarial-robustness.md), special token
- **Methods**: Self-Reflection token, post-training, adversarial evaluation
- **Datasets**: _none recorded_

Tags: `safety`, `self-reflection`, `special token`, `adversarial robustness`, `post-training`

## Abstract

Large Reasoning Models(LRMs) have achieved significant breakthroughs over prior large language models (LLMs), but they also entail greater potential safety risks. Existing alignment methods often remain at a shallow level of protection, making them insufficient to address deeper risks and strategic attacks in complex reasoning processes. To bridge this gap, we move beyond the conventional paradigm that treats safety alignment merely as a preventive measure to reduce harmful outputs. Drawing inspiration from human-like introspection and self-correction, we propose Self-Reflection, a technique that introduces a special Self-Reflection token, enabling LRMs to perform Self-Reflection during generation and recover from harmful outputs. Our approach integrates seamlessly into standard post-training paradigms , further enhancing both helpfulness and safety. The experimental results demonstrate that models trained with Self-Reflection not only consistently outperform the baseline in terms of safety (reducing the HCR from 13.8% to 4.1%, nearly a threefold improvement over mainstream approaches), but also achieve substantial advantages in both helpfulness and the safety–helpfulness balance. More importantly, under evaluations involving various adversarial attacks, including a specially designed adaptive attack, the Self-Reflection mechanism significantly enhances model safety without targeted adversarial training.Notice: This paper contains harmful content.

---

Record id: `doi:10.18653/v1/2026.findings-acl.678`
