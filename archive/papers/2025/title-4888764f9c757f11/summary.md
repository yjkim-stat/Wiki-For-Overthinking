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

VideoChat-R1.5 scales multimodal reasoning by letting the model iteratively re-perceive high-confidence video regions at inference time instead of perceiving once and reasoning statically over the result.

## Problem

Multimodal LLM reasoning is typically built on a single, static perception stage, which limits how well the model can ground its reasoning in the relevant parts of the visual input.

## Contributions

- Introduces Visual Test-Time Scaling (VTTS), scaling MLLM reasoning by iterating perception at inference rather than treating perception as a single static stage.
- Proposes an Iterative Perception (ITP) mechanism trained with reinforcement learning under spatio-temporal supervision.
- Releases VTTS-80K, a dataset built for training iterative perception.
- Presents VideoChat-R1.5, reporting an average improvement of over 5% versus Qwen2.5VL-3B and -7B baselines across more than 15 video benchmarks.

## Method

VTTS lets a multimodal LLM progressively refine its visual focus on high-confidence spatio-temporal regions during inference, guided by its own updated textual predictions, mimicking hierarchical human attention. The Iterative Perception (ITP) mechanism implementing this is trained with reinforcement learning using spatio-temporal supervision, so the model can trade additional perceptual compute for better performance by repeating perception-and-refine steps rather than performing a single static perception pass.

## Results

VideoChat-R1.5 achieves an average improvement of over 5% compared to Qwen2.5VL-3B and Qwen2.5VL-7B baselines across more than 15 benchmarks spanning video conversation, video reasoning, and spatio-temporal perception.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: It is a genuine test-time compute scaling method: it trades additional inference-time compute (iterative perception steps) for accuracy, an instance of the accuracy/efficiency tradeoff the topic tracks. The scaling axis is different from the topic's usual focus, though: it scales the number of perceptual refinement iterations on visual input rather than the length of a textual reasoning chain, and the paper does not address when a model should stop iterating or the overthinking/underthinking of chain-of-thought length.

## Entities

- **Concepts**: visual test-time scaling, iterative perception, hierarchical attention, spatio-temporal grounding
- **Methods**: VideoChat-R1.5, Iterative Perception (ITP), reinforcement learning with spatio-temporal supervision
- **Datasets**: VTTS-80K, video conversation, video reasoning and spatio-temporal perception benchmarks (15+, unspecified by name)

Tags: `test-time-scaling`, `multimodal`, `video`, `iterative-perception`, `reinforcement-learning`

## Abstract

Abstract Inducing reasoning in multimodal large language models (MLLMs) is critical for achieving human-level perception and understanding. Existing methods mainly leverage LLM reasoning to analyze parsed visuals, often limited by static perception stages. This paper introduces Visual Test-Time Scaling (VTTS), a novel approach to enhance MLLMs' reasoning via iterative perception during inference. VTTS mimics humans' hierarchical attention by progressively refining focus on high-confidence spatio-temporal regions, guided by updated textual predictions. Specifically, VTTS employs an Iterative Perception (ITP) mechanism, incorporating reinforcement learning with spatio-temporal supervision to optimize reasoning. To support this paradigm, we also present VTTS-80K, a dataset tailored for iterative perception. These designs allows a MLLM to enhance its performance by increasing its perceptual compute. Extensive experiments validate VTTS's effectiveness and generalization across diverse tasks and benchmarks. Our newly introduced Videochat-R1.5 model has achieved remarkable improvements, with an average increase of over 5\%, compared to robust baselines such as Qwen2.5VL-3B and -7B, across more than 15 benchmarks that encompass video conversation, video reasoning, and spatio-temporal perception.

---

Record id: `title:4888764f9c757f11`
