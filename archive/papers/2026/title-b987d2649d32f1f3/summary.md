<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# TrimR: Verifier-based Training-Free Thinking Trimming for Efficient Test-Time Scaling

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10007390>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.67

## In one line

TrimR is a training-free, verifier-based system that trims redundant chain-of-thought reasoning in deployed large reasoning models to speed up test-time scaling with little accuracy loss.

## Problem

Test-time scaling via long chain-of-thought raises LRM accuracy but adds heavy decoding overhead, largely because models generate redundant thinking that shows clear structured overthinking and underthinking patterns; existing approaches to push accuracy further usually add to this overhead rather than removing the redundancy.

## Contributions

- TrimR, a training-free, verifier-based framework that detects and truncates redundant intermediate reasoning steps in large reasoning models
- An asynchronous online system engineered for high-throughput, production-level deployment of the trimming procedure
- Empirical demonstration that trimming reasoning length improves inference efficiency with negligible accuracy loss

## Method

TrimR uses a lightweight, pretrained, instruction-tuned verifier (no fine-tuning of the LRM or the verifier) to monitor a model's chain-of-thought as it is generated and to detect and truncate redundant intermediate 'thoughts', stopping the reasoning early once the verifier judges further tokens unnecessary. It runs as an asynchronous online system alongside vLLM-style serving to handle large-batch industrial workloads.

## Results

On MATH500, AIME24/25, and GPQA, reasoning runtime for QwQ-32B, DeepSeek-R1-Distill-Qwen-32B, and Pangu-R-38B is improved by up to 70%, with negligible impact on accuracy, measured on Ascend NPUs and vLLM under large-batch workloads.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: A direct treatment of the topic: it explicitly names structured overthinking and underthinking as the source of test-time inefficiency in LRMs and proposes a verifier-based mechanism to trim redundant reasoning tokens without retraining, evaluated for both efficiency gain and accuracy preservation.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), [underthinking](../../../../wiki/concepts/underthinking.md), [test-time scaling](../../../../wiki/concepts/test-time-scaling.md), chain-of-thought redundancy, verifier-guided truncation
- **Methods**: [TrimR](../../../../wiki/methods/trimr.md), verifier-guided CoT truncation, asynchronous online trimming system
- **Datasets**: MATH500, AIME24, AIME25, [GPQA](../../../../wiki/datasets/gpqa.md)

Tags: `overthinking`, `underthinking`, `test-time-scaling`, `cot-trimming`, `verifier`

## Abstract

Abstract Large Reasoning Models (LRMs) demonstrate exceptional capability in tackling complex mathematical, logical, and coding tasks by leveraging extended Chain-of-Thought (CoT) reasoning. Test-time scaling methods—such as prolonging CoT with explicit token-level exploration—can push LRMs’ accuracy boundaries, but they incur significant decoding overhead. A key inefficiency source is LRMs often generate redundant thinking CoTs, which demonstrate clear structured overthinking and underthinking patterns. Inspired by human cognitive reasoning processes and numerical optimization theories, we propose TrimR, a verifier-based, training-free, efficient framework to trim reasoning and enhance test-time scaling, explicitly tailored for production-level deployment. Our method employs a lightweight, pretrained, instruction-tuned verifier to detect and truncate redundant intermediate thoughts of LRMs without any LRM or verifier fine-tuning. We present both the core algorithm and asynchronous online system engineered for high-throughput industrial applications. Empirical evaluations on Ascend NPUs and vLLM show that our framework delivers substantial gains in inference efficiency under large-batch workloads. In particular, on the four MATH500, AIME24/25, and GPQA benchmarks, the reasoning runtime of QwQ-32B, DeepSeek-R1-Distill-Qwen-32B, and Pangu-R-38B is improved by up to 70% with negligible impact on accuracy.

---

Record id: `title:b987d2649d32f1f3`
