<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Your Reasoning Model Knows What Counts: Self-Guided Chain-of-Thought Pruning for Efficient Reasoning

- **Authors**: Zi-Ao Ma, Xian-Ling Mao, Tian Lan, Chen Xu, Zhijing Wu
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.25/>
- **PDF**: <https://aclanthology.org/2026.acl-long.25.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.25
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Chain-of-Thought (CoT) reasoning is crucial for the performance of Large Reasoning Models (LRMs) but is often hindered by redundant and distracting segments, which incur excessive inference costs and degrade robustness. Existing approaches try to solve this problem by enforcing brevity through external supervision, such as length-based penalties or heuristic truncation. However, these approaches often degrade performance because they disregard the model’s intrinsic reasoning dependency and thus fail to distinguish between essential and redundant CoT segments. To address this problem, we propose SGP-CoT, a novel Self-Guided Pruning framework that leverages the model’s intrinsic likelihood landscape to identify segments that are extraneous to its specific reasoning pattern. Specifically, SGP-CoT treats the reasoning trajectory as a sequence of semantic units and assesses the necessity of each one via internal likelihood signals, measuring its contribution to the answer and local coherence. Based on this, it selectively removes non-essential segments and then forms high-quality pruning-based preference pairs, enabling the model to learn focused reasoning via self-optimization. Extensive experiments across diverse benchmarks demonstrate that the proposed SGP-CoT significantly reduces output length while maintaining or improving accuracy. These results validate that LRMs intrinsically possess the capability to discern reasoning utility, positioning SGP-CoT as a robust pathway toward scalable inference.

---

Record id: `doi:10.18653/v1/2026.acl-long.25`
