<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# BloomEval: A Bloom’s Cognitive Taxonomy-Based Benchmark for Evaluating LRMs via Cognitive Hierarchy Trace

- **Authors**: Zhiyi Duan, Lei Gao, Jiangshan Guan, Qi Wang, Rui Liu
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1262/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1262.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1262
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Current benchmarks for Large Reasoning Models (LRMs) primarily rely on answer correctness, failing to assess the structural coherence and cognitive soundness of the reasoning process itself. To address this gap, we introduce Cognitive Hierarchy Trace (CHT), a novel evaluation framework grounded in Bloom’s Cognitive Taxonomy (BCT). CHT provides a structured, step-wise mapping of a model’s reasoning trajectory onto hierarchical cognitive levels, enabling the detection of structural anomalies such as hierarchy jumps, breaks, and overthinking. Based on CHT, we present BloomEval, the first large-scale benchmark designed for fine-grained cognitive capability assessment. It comprises 94,602 math problems, each annotated with Bloom’s cognitive levels, CHT trajectories, a three-tier knowledge hierarchy, and problem difficulty. To ensure scalable yet reliable annotation, we develop an Expert-LLM collaborative pipeline with a three-stage reconciliation mechanism. Our comprehensive evaluation reveals a critical finding: models often arrive at correct answers through cognitively flawed or opaque reasoning paths. The CHT-based analysis uncovers prevalent structural inconsistencies that are invisible to outcome-only metrics, demonstrating that answer accuracy is an insufficient proxy for reasoning quality.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1262`
