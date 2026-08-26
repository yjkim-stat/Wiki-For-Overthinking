<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Think Less, Know More: State-Aware Reasoning Compression with Knowledge Guidance for Efficient Reasoning

- **Authors**: Yi Sui, Chaozhuo Li, Dawei Song
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1128/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1128.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1128
- **Topics**: overthinking
- **Relevance score**: overthinking 0.67

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large Reasoning Models (LRMs) achieve strong performance on complex tasks by leveraging long Chain-of-Thought (CoT), but often suffer from overthinking, leading to excessive reasoning steps and high inference latency. Existing CoT compression methods struggle to balance accuracy and efficiency, and lack fine-grained, step-level adaptation to redundancy and reasoning bias. Therefore, we propose State-Aware Reasoning Compression with Knowledge Guidance (STACK), a framework that performs step-wise CoT compression by explicitly modeling stage-specific redundancy sources and integrating with a retrieval-augmented guidance. STACK constructs online long–short contrastive samples and dynamically switches between knowledge-guided compression for uncertain or biased reasoning state and self-prompted compression for overly long but confident state, complemented by an answer-convergence-based early stopping mechanism to suppress redundant verification. We further propose a reward-difference-driven training strategy by combining Proximal Policy Optimization (PPO) and Direct Preference Optimization (DPO), enabling models to learn state-conditioned compression strategies. Experiments on three mathematical reasoning benchmarks show that STACK achieves a superior accuracy–efficiency balance, reducing average response length by 59.9% while improving accuracy by 4.8 points over existing methods.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1128`
