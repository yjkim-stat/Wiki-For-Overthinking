<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# CoBa: Cost-Effective Test-Time Scaling via Compute-Balanced Routing

- **Authors**: Yan Zhou, Yue Ouyang, Kaiyang Zheng, Suncheng Xiang
- **Venue**: cs.AI
- **Published**: 2026-08-07
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.07424>
- **PDF**: <https://arxiv.org/pdf/2608.07424v2>
- **Topics**: test-time-scaling
- **Relevance score**: reasoning-evaluation 0.25, reasoning-training 0.25, test-time-scaling 0.57

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Test-time scaling is often implemented by spending more compute along one axis: sampling more solutions, extending a chain of thought, or applying a stronger evaluator. Under a fixed inference budget, these choices compete. This paper formulates test-time reasoning as a compute-allocation problem in which a system must decide whether the next unit of compute should be spent on generation, verification, or stopping. We introduce CoBa, a compute-balanced routing policy that first obtains a small set of candidates, applies cheap verification broadly, and routes uncertain or high-value candidates to stronger verification. On 3,129 example-generator evaluations spanning MATH-500, AIME 2024/2025, AMC 2023, and procedural symbolic reasoning, CoBa-Routed-Strong reaches 85.13% macro accuracy, statistically matching a self-evaluation weighted-voting proxy at 85.20% while using 49.1% fewer parameter-weighted tokens. It also matches best-of-16 majority voting within 0.01 macro-accuracy points while using 58.9% fewer parameter-weighted tokens; paired tests retain a small best-of-16 edge at substantially higher cost. Paired bootstrap tests show significant gains over single-sample decoding, while the remaining gap to the pool oracle exposes headroom for sharper routing. For local reasoning systems, test-time scaling becomes a question of where the next computation is most valuable.

---

Record id: `arxiv:2608.07424`
