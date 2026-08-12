<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Test-Time Scaling for Safe Text-Guided Image Generation via Intermediate Clean Estimates

- **Authors**: Jinya Sakurai, Shueicheng Yan, Xun Xu
- **Venue**: cs.CV
- **Published**: 2026-08-04
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.03284>
- **PDF**: <https://arxiv.org/pdf/2608.03284v1>
- **Topics**: test-time-scaling
- **Relevance score**: test-time-scaling 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Ensuring safety and policy compliance in text-to-image diffusion models remains a critical challenge, as benign or adversarial prompts can often elicit prohibited content, e.g. nudity and protected intellectual property. While training-based unlearning methods are effective, they are computationally expensive and prone to catastrophic interference with general capabilities. Conversely, existing test-time defenses are primarily prompt-centric, relying on modifying textual descriptions only, and overlook the visual signals for detection. In this paper, we propose to leverage the intermediate clean image estimated during the generation process and employ a sparse margin objective to detect prohibited concepts. When a violation is detected, we immediately intervene by optimizing a structured low-rank residual in the text-conditioning space via truncated backpropagation. This design allows weight-preserving detection, keeps non-violating inference latency nearly unchanged as the maximum budget increases, and offers flexibility in safety performance via test-time scaling. Extensive experiments on Stable Diffusion v1.4 and v3.5 across nudity removal, IP protection, and style erasure demonstrate superior performance across suppression, fidelity and preservation compared to prior weight-preserving baselines, providing a scalable and flexible solution for safe generative deployment.

---

Record id: `arxiv:2608.03284`
