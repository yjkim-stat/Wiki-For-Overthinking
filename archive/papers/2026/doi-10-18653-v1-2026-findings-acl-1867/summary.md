<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Distilling Long-CoT Reasoning through Collaborative Step-wise Multi-Teacher Decoding

- **Authors**: Taewon Yun, Jisu Shin, Jeonghwan Choi, Seunghwan Bang, Hwanjun Song
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1867/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1867.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1867
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Distilling large reasoning models (LRMs) has become essential for making their Long-CoT reasoning capabilities practical, as full-scale inference remains computationally prohibitive. Existing curation-based approaches, which select complete reasoning traces post-hoc, overlook the collaborative potential of heterogeneous teachers and fail to adapt exploration dynamically, often leading to redundant sampling and missed opportunities for complementary reasoning. To address this, we introduce CoRD, a collaborative multi-teacher decoding framework that performs step-wise reasoning synthesis guided by predictive perplexity–based scoring and beam search. This approach enables heterogeneous LRMs to jointly construct coherent reasoning trajectories while maintaining diverse, high-potential hypotheses efficiently. Experiments show that CoRD generates higher-quality reasoning data and achieves student performance approaching teacher-level results, demonstrating that fine-grained collaboration among diverse LRMs yields structured, efficient, and robust reasoning distillation. The dataset and model are available at https://github.com/DISL-Lab/CoRD

---

Record id: `doi:10.18653/v1/2026.findings-acl.1867`
