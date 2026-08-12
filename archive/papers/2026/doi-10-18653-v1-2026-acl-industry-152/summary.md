<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# CAT: Confidence-Adaptive Thinking for Efficient Reasoning of Large Reasoning Models

- **Authors**: Qizhi Jiang, Shuo Wang, Pei Ke, Yuhang Song, Ke Qin
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-industry.152>
- **DOI**: 10.18653/V1/2026.ACL-INDUSTRY.152
- **Topics**: reasoning-training, test-time-scaling
- **Relevance score**: reasoning-training 0.80

## In one line

Feeds a reasoning model's own self-certainty into preference optimization so it compresses confident answers and keeps deliberating on uncertain ones.

## Problem

Large reasoning models overthink simple queries, costing tokens and latency. Existing compression applies uniform length reduction or relies on coarse-grained difficulty estimation, which degrades performance on genuinely difficult problems — the cost of a uniform policy falls on the hard cases.

## Contributions

- CAT: intrinsic self-certainty as a confidence signal inside preference optimization
- Autonomous modulation of reasoning length by problem difficulty without an external difficulty estimator
- Reported accuracy gains over state-of-the-art compression baselines across benchmarks and base models

## Method

Confidence-Adaptive Thinking incorporates the model's intrinsic self-certainty signals as confidence into the preference optimization process, letting reasoning length be modulated autonomously by problem difficulty. Using the model's own certainty rather than an external difficulty estimate is the distinguishing choice: difficulty is read off the model that will do the reasoning, not predicted for it.

## Results

CAT is reported to consistently outperform state-of-the-art baselines on reasoning accuracy across multiple benchmarks on different base models. No numbers, benchmark names or base models are given in the abstract.

## Limitations

No quantitative results in the abstract, so neither the accuracy gain nor the token saving can be weighed. Benchmarks and base models are unnamed. The approach depends on self-certainty being calibrated with respect to difficulty, which the abstract asserts rather than measures — an overconfident model would compress exactly the problems it is wrong about.

## Why it matters here

- **reasoning-training**: Sits in the archive's difficulty-allocation cluster, and takes the position that the difficulty signal should come from the model's own certainty rather than from a separate estimator. That makes calibration the load-bearing assumption, and the archive's calibration line gives reason to doubt it — if confidence and correctness come apart, compressing confident answers compresses the wrong ones. The paper does not report a calibration check, so the claim rests on the accuracy result alone. It is one of four length-compression papers in this ACL batch, alongside long.146, long.1386 and long.1766.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), [prompt difficulty](../../../../wiki/concepts/prompt-difficulty.md), calibration, self-certainty, [adaptive compute allocation](../../../../wiki/concepts/adaptive-compute-allocation.md), efficient reasoning
- **Methods**: [preference optimization](../../../../wiki/methods/preference-optimization.md), Confidence-Adaptive Thinking, length compression
- **Datasets**: _none recorded_

Tags: `overthinking`, `confidence`, `preference optimization`, `length compression`, `thin-evidence`

## Abstract

Large Reasoning Models (LRMs) have achieved remarkable success on complex tasks by leveraging long chain-of-thought (CoT) trajectories, yet they frequently exhibit overthinking on simple queries, resulting in significant token overhead and reduced inference efficiency. However, existing compression methods predominantly apply uniform length reduction or rely on coarse-grained difficulty estimation, often leading to performance degradation on difficult problems. To address this limitation, we propose Confidence-Adaptive Thinking (CAT), a framework that incorporates the model's intrinsic self-certainty signals as confidence into the preference optimization process, which autonomously modulates reasoning lengths based on problem difficulty. Experimental results show that CAT consistently outperforms state-of-the-art baselines on reasoning accuracy across multiple benchmarks on different base models. Our work enables LRMs to effectively compress confident responses while deliberating on uncertain ones, offering a potentially robust solution for balancing accuracy and latency in practical industrial scenarios.

---

Record id: `doi:10.18653/v1/2026.acl-industry.152`
