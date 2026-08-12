<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Think Better, Not Longer: Token-Level Marginal Utility for Efficient Reasoning in Large Reasoning Models

- **Authors**: Jiawei Li 0020, Yang Gao 0016, Huashan Sun, Chong Feng 0001
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.1386>
- **DOI**: 10.18653/V1/2026.ACL-LONG.1386
- **Topics**: reasoning-training, test-time-scaling
- **Relevance score**: reasoning-training 0.80

## In one line

Defines a token's marginal utility as its log-probability gain for the ground-truth answer, then trains against negative-utility tokens to shorten chains of thought.

## Problem

Reasoning models overthink. Length control at the trajectory level is coarse: it decides how long a chain may be without saying which parts of it are worth keeping.

## Contributions

- Token-level Marginal Utility: per-token log-probability gain of the ground-truth answer as a dense supervision signal
- MUTO, a training framework that penalizes negative-utility reasoning tokens rather than controlling length at the trajectory level
- 87.1% token reduction with +2.3% accuracy at 1.5B and 80.2% reduction with -0.1% accuracy at 7B
- Best length-normalized accuracy among compared baselines

## Method

Token-level Marginal Utility quantifies the per-token log-probability gain of the ground-truth answer, giving a dense per-token signal. MUTO uses it to identify tokens that reduce the model's likelihood of the correct answer and penalizes such negative-utility reasoning, producing concise chains. The signal is defined against the known answer, so it is a training-time quantity and cannot be computed at inference.

## Results

On DeepSeek-R1-Distill-Qwen backbones at 1.5B and 7B across six math reasoning benchmarks, MUTO improves the efficiency-accuracy Pareto frontier: average token usage falls 87.1% at 1.5B while accuracy rises 2.3%, and falls 80.2% at 7B with -0.1% accuracy change. It attains the best length-normalized accuracy among baselines.

## Limitations

Both scales are DeepSeek-R1-Distill-Qwen, so generality across model families is untested, and distilled models may carry more removable redundancy than RL-trained ones. An 87.1% token reduction with an accuracy gain is large enough to raise the question of how much of the original chain was doing any work in these backbones. Benchmarks are unnamed. The signal requires ground-truth answers, so it does not extend to unverifiable domains.

## Why it matters here

- **reasoning-training**: Adds a criterion to the archive's token-selection dispute, and a distinctive one: utility is signed, so a token can be identified as actively harmful rather than merely uninformative. Every other criterion tracked here — entropy, advantage magnitude, teacher-student gap, reference-shift — is unsigned and selects tokens to weight up. That means the overlap question the archive has been measuring for the unsigned criteria does not directly apply, and the interesting measurement is whether negative-utility tokens are the complement of high-entropy tokens or a different set entirely. The 87.1% reduction with a positive accuracy delta is also the strongest evidence in the archive that distilled reasoning chains contain a large fraction of tokens that do no work.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), [reasoning redundancy](../../../../wiki/concepts/reasoning-redundancy.md), [token selection](../../../../wiki/concepts/token-selection.md), marginal utility, [Pareto frontier](../../../../wiki/concepts/pareto-frontier.md), [credit assignment](../../../../wiki/concepts/credit-assignment.md), length-normalized accuracy
- **Methods**: MUTO, token-level marginal utility, [reinforcement learning post-training](../../../../wiki/methods/reinforcement-learning-post-training.md), [length control](../../../../wiki/methods/length-control.md)
- **Datasets**: _none recorded_

Tags: `token selection`, `overthinking`, `marginal utility`, `length compression`, `math reasoning`

## Abstract

While Large Reasoning Models (LRMs) have demonstrated remarkable capabilities through explicit Chain-of-Thought (CoT) generation, they frequently suffer from “overthinking”. In this work, we bridge this gap by introducing Token-level Marginal Utility, which quantifies the per-token log-probability gain of the ground-truth answer. Leveraging this dense supervision signal, we propose MUTO (Marginal Utility Guided Thinking Optimization), a unified training framework designed to synthesize concise reasoning chains. Rather than relying only on coarse trajectory-level length control, MUTO identifies tokens that reduce the model’s likelihood of the correct answer and penalizes such negative-utility reasoning, yielding concise yet effective CoT trajectories. Experiments on DeepSeek-R1-Distill-Qwen backbones (1.5B and 7B) across six math reasoning benchmarks show that MUTO yields a markedly better efficiency-accuracy Pareto frontier. It reduces average token usage by 87.1% at 1.5B while improving accuracy by 2.3%, and cuts tokens by 80.2% at 7B with only -0.1% accuracy change, achieving the best length-normalized accuracy among baselines.

---

Record id: `doi:10.18653/v1/2026.acl-long.1386`
