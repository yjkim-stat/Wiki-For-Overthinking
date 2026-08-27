<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# VideoChat-R1.5: Visual Test-Time Scaling to Reinforce Multimodal Reasoning by Iterative Perception

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/116032>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Visual Test-Time Scaling (VTTS) lets a multimodal LLM iteratively refine its perception of high-confidence spatio-temporal regions during inference, guided by its own updated textual predictions, and the resulting VideoChat-R1.5 model improves over strong baselines by 5%+ on 15+ video benchmarks.

## Problem

Existing multimodal LLM reasoning methods mainly apply text-based reasoning over a single, static parsing of visual input, limiting performance because the perception stage is not revisited as reasoning proceeds.

## Contributions

- Visual Test-Time Scaling (VTTS), enhancing MLLM reasoning via iterative perception rather than a single static parse
- VTTS-80K, a dataset built for training iterative perception
- VideoChat-R1.5, achieving 5%+ average gains over strong baselines across 15+ video benchmarks

## Method

Introduces an Iterative Perception (ITP) mechanism that mimics hierarchical human attention, progressively refining focus on high-confidence spatio-temporal regions guided by updated textual predictions, trained with reinforcement learning under spatio-temporal supervision; builds VTTS-80K, a dataset tailored for iterative perception, and applies the approach to produce VideoChat-R1.5.

## Results

VideoChat-R1.5 achieves an average improvement of over 5% versus robust baselines (Qwen2.5VL-3B and -7B) across more than 15 benchmarks spanning video conversation, video reasoning, and spatio-temporal perception, by increasing perceptual compute at inference time.

## Limitations

Not stated in the fetched abstract; scope is restricted to video/multimodal reasoning tasks, and no discussion of the added inference cost of iterative perception versus the accuracy gained.

## Why it matters here

- **overthinking**: A cross-modal analog of test-time scaling: instead of spending more *text* tokens on reasoning, VTTS spends more *perceptual* compute re-examining the visual input -- relevant as evidence that test-time-scaling's core tradeoff (more inference compute for better accuracy) generalizes beyond token-length scaling to which part of the input a model attends to.

## Entities

- **Concepts**: Visual Test-Time Scaling (VTTS), Iterative Perception (ITP), hierarchical attention refinement
- **Methods**: Iterative Perception (ITP), reinforcement learning with spatio-temporal supervision, Visual Test-Time Scaling
- **Datasets**: VTTS-80K (new)

Tags: `test-time-scaling`, `multimodal`, `video-reasoning`, `iterative-perception`

## Abstract

Abstract Inducing reasoning in multimodal large language models (MLLMs) is critical for achieving human-level perception and understanding. Existing methods mainly leverage LLM reasoning to analyze parsed visuals, often limited by static perception stages. This paper introduces Visual Test-Time Scaling (VTTS), a novel approach to enhance MLLMs' reasoning via iterative perception during inference. VTTS mimics humans' hierarchical attention by progressively refining focus on high-confidence spatio-temporal regions, guided by updated textual predictions. Specifically, VTTS employs an Iterative Perception (ITP) mechanism, incorporating reinforcement learning with spatio-temporal supervision to optimize reasoning. To support this paradigm, we also present VTTS-80K, a dataset tailored for iterative perception. These designs allows a MLLM to enhance its performance by increasing its perceptual compute. Extensive experiments validate VTTS's effectiveness and generalization across diverse tasks and benchmarks. Our newly introduced Videochat-R1.5 model has achieved remarkable improvements, with an average increase of over 5\%, compared to robust baselines such as Qwen2.5VL-3B and -7B, across more than 15 benchmarks that encompass video conversation, video reasoning, and spatio-temporal perception.

---

Record id: `title:4888764f9c757f11`
