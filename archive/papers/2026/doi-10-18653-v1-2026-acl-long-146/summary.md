<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Optimizing Length Compression in Large Reasoning Models

- **Authors**: Zhengxiang Cheng, Dongping Chen, Mingyang Fu, Tianyi Zhou 0001
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.146>
- **DOI**: 10.18653/V1/2026.ACL-LONG.146
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.80

## In one line

Identifies double-checking after the correct answer is already derived as 'invalid thinking', and trains a GRPO variant with a compress reward that targets exactly that portion.

## Problem

Reasoning models produce unnecessary and verbose chains. The core inefficiency is identified specifically: models repeatedly double-check their work after having already derived the correct answer. General efficacy/efficiency objectives do not distinguish that redundancy from reasoning that is still doing work.

## Contributions

- Identification of post-answer double-checking as the specific redundancy to target
- The Brevity and Sufficiency principles as fine-grained replacements for general efficacy/efficiency objectives
- LC-R1, a GRPO-based method pairing a Length Reward with a Compress Reward aimed at the invalid thinking portion
- A roughly 50% length reduction at roughly 2% accuracy cost, with robustness analysis

## Method

Two fine-grained principles are proposed in place of general ones — Brevity, eliminating redundancy, and Sufficiency, preserving critical steps. LC-R1 is a GRPO-based post-training method combining a Length Reward for overall conciseness with a Compress Reward designed to remove the invalid portion of thinking. Separating the two rewards is what lets the method cut the post-answer tail rather than shortening uniformly, which is where uniform length penalties do damage.

## Results

On multiple reasoning benchmarks, LC-R1 reduces sequence length by roughly 50% with a roughly 2% accuracy drop, a Pareto point favouring high compression. Further analysis validates robustness and reports insights for building efficient reasoning models.

## Limitations

Roughly 2% accuracy is a real cost, unlike the near-free reductions claimed elsewhere in this batch, and the paper positions it as a deliberate trade-off. Benchmarks and models are not named. 'Invalid thinking' is defined relative to having already derived the correct answer, which is knowable in training but not at inference, so the trained behaviour must generalize the pattern rather than detect the condition. The ~50% figure is coarse.

## Why it matters here

- **reasoning-training**: Pins the overthinking phenomenon to a specific, checkable location — tokens generated after the answer is already correct — which is narrower and more testable than the diffuse redundancy other papers penalize. That definition connects the length-compression cluster to the archive's answer-stabilization thread, since the point after which the answer stops changing is precisely what stopping-signal methods like DEER estimate at inference. This paper uses the same quantity as a training reward instead, which means the two lines are estimating one thing from opposite ends, and it reports an honest ~2% accuracy cost where the neighbouring papers in this batch report near-free reductions.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), [reasoning redundancy](../../../../wiki/concepts/reasoning-redundancy.md), invalid thinking, [self-correction](../../../../wiki/concepts/self-correction.md), [Pareto frontier](../../../../wiki/concepts/pareto-frontier.md), [reward shaping](../../../../wiki/concepts/reward-shaping.md), [answer stabilization](../../../../wiki/concepts/answer-stabilization.md)
- **Methods**: LC-R1, [GRPO](../../../../wiki/methods/grpo.md), length reward, compress reward, [reinforcement learning post-training](../../../../wiki/methods/reinforcement-learning-post-training.md)
- **Datasets**: _none recorded_

Tags: `overthinking`, `grpo`, `length compression`, `reward shaping`, `invalid thinking`

## Abstract

Large Reasoning Models (LRMs) have achieved remarkable success, yet they often suffer from producing unnecessary and verbose reasoning chains. We identify a core aspect of this issue as ”invalid thinking”— models tend to repeatedly double-check their work after having derived the correct answer. To address this specific inefficiency, we move beyond the general principles of Efficacy and Efficiency to propose two new, fine-grained principles: Brevity, which advocates for eliminating redundancy, and Sufficiency, which ensures critical reasoning steps are preserved. Guided by these principles, we introduce LC-R1, a post-training method based on Group Relative Policy Optimization (GRPO). LC-R1 employs a novel combination of a Length Reward for overall conciseness and a Compress Reward that is specifically designed to remove the invalid portion of the thinking process. Extensive experiments on multiple reasoning benchmarks demonstrate that LC-R1 achieves a significant reduction in sequence length (5̃0%) with only a marginal (2̃%) drop in accuracy, achieving a favorable trade-off point on the Pareto frontier that prioritizes high compression. Our analysis further validates the robustness of LC-R1 and provides valuable insights for developing more powerful yet computationally efficient LRMs.

---

Record id: `doi:10.18653/v1/2026.acl-long.146`
