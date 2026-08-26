<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Seer Self-Consistency: Advance Budget Estimation for Adaptive Test-Time Scaling

- **Authors**: Shiyu Ji, Yixuan Wang, Yijun Liu, Qingfu Zhu, Wanxiang Che
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.2120/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.2120.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.2120
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Test-time scaling improves the inference performance of Large Language Models (LLMs) but also incurs substantial computational costs. Although recent studies have reduced token consumption through dynamic self-consistency, they remain constrained by the high latency of sequential requests. In this paper, we propose SeerSC, a dynamic self-consistency framework that simultaneously improves token efficiency and latency by integrating System 1 and System 2 reasoning. Specifically, we utilize the rapid System 1 to compute the answer entropy for given queries. This score is then used to evaluate the potential of samples for scaling, enabling dynamic self-consistency under System 2. Benefiting from the advance and accurate estimation provided by System 1, the proposed method can reduce token usage while simultaneously achieving a significant decrease in latency through parallel generation. It outperforms existing methods, achieving up to a 47% reduction in token consumption and a 43% reduction in inference latency without significant performance loss.

---

Record id: `doi:10.18653/v1/2026.findings-acl.2120`
