<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Quantifying and Understanding Uncertainty in Large Reasoning Models

- **Authors**: Yangyi Li, Chenxu Zhao, Mengdi Huai
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.1511/>
- **PDF**: <https://aclanthology.org/2026.acl-long.1511.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.1511
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large Reasoning Models (LRMs) have recently demonstrated significant improvements in complex reasoning. While quantifying generation uncertainty in LRMs is crucial, traditional methods are often insufficient because they do not provide finite-sample guarantees for reasoning-answer generation. Conformal prediction (CP) stands out as a model-agnostic methodology that constructs statistically rigorous uncertainty sets. However, existing CP methods ignore the logical connection between the reasoning trace and the final answer. Additionally, prior studies fail to interpret the origins of uncertainty coverage for LRMs as they typically overlook the specific training factors driving valid reasoning. Notably, it is challenging to disentangle reasoning quality from answer correctness, while simultaneously establishing theoretical guarantees for computationally efficient explanation methods. To address these challenges, we first propose a novel methodology that provides the uncertainty of the reasoning-answer structure with statistical guarantees. Subsequently, we develop a unified example-to-step explanation framework using Shapley values that identifies a provably sufficient subset of training data and their specific reasoning steps sufficient to achieve coverage. We also provide the theoretical analysis for our proposed methods. Extensive experiments on challenging reasoning datasets verify the effectiveness of the proposed methods.

---

Record id: `doi:10.18653/v1/2026.acl-long.1511`
