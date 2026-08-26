<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Efficiently Learning To Reason or Not to Reason: Root-token Policy Optimization for Adaptive Thinking

- **Authors**: Taehyeon Kim, Hyunsoo Lee, Youngsoo Jang, Moontae Lee
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.816/>
- **PDF**: <https://aclanthology.org/2026.acl-long.816.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.816
- **Topics**: overthinking
- **Relevance score**: overthinking 0.70

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large reasoning models (LRMs) achieve strong performance by externalizing explicit reasoning traces before producing the answer, yet suffer from overthinking challenge that allocates uniformly heavy computation to queries of varying difficulty. While proprietary models mitigate this via opaque routing, open-source LRMs still lack an efficient mechanism to internalize adaptive reasoning due to both expensive training cost and limited disclosure of training recipes. In response, we introduce RPO (Root-token Policy Optimization), a framework that enables LRMs to self-determine when to reason by training only the initial root token (e.g., whether to invoke the think tag) via group relative reward and group-wise advantages. By focusing on this pivotal branching point, RPO drastically reduces training overhead and VRAM usage. Across multiple model families and scales, RPO learns difficulty-aware adaptive thinking at just 2% of the training compute of prior adaptive-reasoning methods.

---

Record id: `doi:10.18653/v1/2026.acl-long.816`
