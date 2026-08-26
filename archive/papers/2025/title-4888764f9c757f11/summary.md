<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# VideoChat-R1.5: Visual Test-Time Scaling to Reinforce Multimodal Reasoning by Iterative Perception

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/116032>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Abstract Inducing reasoning in multimodal large language models (MLLMs) is critical for achieving human-level perception and understanding. Existing methods mainly leverage LLM reasoning to analyze parsed visuals, often limited by static perception stages. This paper introduces Visual Test-Time Scaling (VTTS), a novel approach to enhance MLLMs' reasoning via iterative perception during inference. VTTS mimics humans' hierarchical attention by progressively refining focus on high-confidence spatio-temporal regions, guided by updated textual predictions. Specifically, VTTS employs an Iterative Perception (ITP) mechanism, incorporating reinforcement learning with spatio-temporal supervision to optimize reasoning. To support this paradigm, we also present VTTS-80K, a dataset tailored for iterative perception. These designs allows a MLLM to enhance its performance by increasing its perceptual compute. Extensive experiments validate VTTS's effectiveness and generalization across diverse tasks and benchmarks. Our newly introduced Videochat-R1.5 model has achieved remarkable improvements, with an average increase of over 5\%, compared to robust baselines such as Qwen2.5VL-3B and -7B, across more than 15 benchmarks that encompass video conversation, video reasoning, and spatio-temporal perception.

---

Record id: `title:4888764f9c757f11`
