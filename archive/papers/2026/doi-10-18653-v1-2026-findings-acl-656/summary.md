<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# DeepPrune: Parallel Scaling without Inter-trace Redundancy

- **Authors**: Shangqing Tu, Yaxuan Li, Yushi Bai, Lei Hou, Juanzi Li
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.656/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.656.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.656
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Parallel scaling has emerged as a powerful paradigm to enhance reasoning capabilities in large language models (LLMs) by generating multiple Chain-of-Thought (CoT) traces simultaneously. However, this approach introduces significant computational inefficiency due to inter-trace redundancy—our analysis reveals that over 80% of parallel reasoning traces yield identical final answers, representing substantial wasted computation. To address this critical efficiency bottleneck, we propose DeepPrune, a novel framework that enables efficient parallel scaling through dynamic pruning. Our method features a specialized judge model trained with oversampling techniques to accurately predict answer equivalence from partial reasoning traces, achieving 0.7072 AUROC on equivalence prediction across unseen reasoning models. This is combined with an online greedy clustering algorithm that dynamically prunes redundant paths while preserving answer diversity. Comprehensive evaluations across three challenging benchmarks (AIME 2024, AIME 2025, and GPQA) and multiple reasoning models demonstrate that DeepPrune achieves remarkable token reduction ranging from 65.73% to 88.50% compared to conventional consensus sampling, while maintaining competitive accuracy within 3.4 percentage points. Our work establishes a new standard for efficient parallel reasoning, making high-performance reasoning more efficient. Our code and data are here: https://github.com/THU-KEG/DeepPrune/

---

Record id: `doi:10.18653/v1/2026.findings-acl.656`
