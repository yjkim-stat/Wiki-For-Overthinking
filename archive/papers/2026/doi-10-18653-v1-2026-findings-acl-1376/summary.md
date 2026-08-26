<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Chronos: Learning Temporal Dynamics of Reasoning Chains for Test-Time Scaling

- **Authors**: Kai Zhang, Jiayi Liao, Chengpeng Li, Ziyuan Xie, Sihang Li, Xiang Wang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1376/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1376.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1376
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Test-Time Scaling (TTS) has emerged as an effective paradigm for improving the reasoning performance of large language models (LLMs). However, existing methods — most notably majority voting and heuristic token-level scoring — treat reasoning traces or tokens equally, thereby being susceptible to substantial variations in trajectory quality and localized logical failures. In this work, we introduce Chronos, a lightweight and plug-and-play chronological reasoning scorer that models each trajectory as a time series. Specifically, Chronos learns to capture trajectory features of token probabilities, assigns quality scores accordingly, and employs a weighted voting mechanism. Extensive evaluations on both in-domain and out-of-domain benchmarks demonstrate that Chronos consistently delivers substantial gains across a variety of models, with negligible computational overhead. Notably, Chronos@128 achieves relative improvements of 34.21% over Pass@1 and 22.70% over Maj@128 on HMMT25 using Qwen3-4B-Thinking-2507, highlighting its effectiveness.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1376`
