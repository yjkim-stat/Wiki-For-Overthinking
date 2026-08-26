<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Hidden States as Early Signals: Step-level Trace Evaluation and Pruning for Efficient Test-Time Scaling

- **Authors**: Zhixiang Liang, Beichen Huang, Zheng Wang, Minjia Zhang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1336/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1336.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1336
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large Language Models (LLMs) can enhance reasoning capabilities through test-time scaling by generating multiple traces. However, the combination of lengthy reasoning traces with multiple sampling introduces substantial computation and high end-to-end latency. Prior work on accelerating this process has relied on similarity-based or confidence-based pruning, but these signals do not reliably indicate trace quality. To address these limitations, we propose STEP: Step-level Trace Evaluation and Pruning, a novel pruning framework that evaluates reasoning steps using hidden states and dynamically prunes unpromising traces during generation. We train a lightweight step scorer to estimate trace quality, and design a GPU memory-aware pruning strategy that triggers pruning as the GPU memory is saturated by KV cache to reduce end-to-end latency. Experiments across challenging reasoning benchmarks demonstrate that STEP reduces end-to-end inference latency by 45%–70% on average compared to self-consistency while also improving reasoning accuracy.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1336`
