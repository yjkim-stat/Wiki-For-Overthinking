<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# TQLite: Multi-LLM Jury Guided Distillation for Real-time MQM Translation Quality Evaluation

- **Authors**: Bhavin Jawade, Cameron R. Wolfe
- **Venue**: cs.CL
- **Published**: 2026-08-04
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.02975>
- **PDF**: <https://arxiv.org/pdf/2608.02975v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large language models (LLMs) have demonstrated impressive performance in MQM-based translation quality (TQ) evaluation, and recent advances in large reasoning models (LRMs) promise even greater improvements. However, both LLMs and LRMs are computationally expensive to deploy at scale, while small language models (SLMs)---though much more efficient---struggle with the complex reasoning required for evaluation tasks. In this work, we present an extensive empirical study benchmarking SLMs, LLMs, and LRMs across a wide range of TQ evaluation setups, providing a comprehensive view of the current landscape and establishing best practices. To address the scalability challenge, we introduce TQLite, a novel distillation framework that enables SLMs to approach the MQM evaluation performance of the best LRM-based evaluators. Our approach leverages a multi-LRM jury to generate high-quality synthetic training data via practical data curation techniques and aggregation of evaluation responses across a diverse panel of models. Our results demonstrate that SLMs trained via TQLite achieve strong MQM evaluation performance that far exceeds off-the-shelf evaluation capabilities of standard SLMs, offering a scalable and cost-effective alternative to LLM- and LRM-based evaluators.

---

Record id: `arxiv:2608.02975`
