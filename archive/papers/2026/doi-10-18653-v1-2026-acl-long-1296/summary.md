<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# REST: Stress Testing Large Reasoning Models by Asking Multiple Problems at Once

- **Authors**: Zhuoshi Pan, Qizhi Pei, Yu Li, Zinan Tang, QiYao Sun, H. Vicky Zhao, Conghui He, Lijun Wu
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.1296/>
- **PDF**: <https://aclanthology.org/2026.acl-long.1296.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.1296
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Recent Large Reasoning Models (LRMs) have achieved remarkable progress, yet their evaluation still relies on a narrow paradigm: evaluating one question at a time. This single-question setup suffers from two major limitations: (1) vulnerability to data contamination and diminishing difficulty, forcing costly creation of new questions with significant human effort, (2) failure to evaluate models under multi-context pressure, a key requirement for real-world deployment. To bridge this gap, we present REST (Reasoning Evaluation through Simultaneous Testing), a stress-testing framework that exposes LRMs to multiple problems simultaneously. Beyond basic reasoning, REST evaluates two under-tested capabilities: contextual priority allocation and robustness against contextual interference. Our evaluation of more than 30 advanced reasoning models on 9 reasoning benchmarks reveals several striking findings: Even state-of-the-art (SOTA) models such as DeepSeek-R1 exhibit substantial performance degradation under stress testing, challenging the prevailing assumption that “LLMs are multi-problem solvers”. Crucially, REST demonstrates stronger discriminative power than existing benchmarks, revealing performance gaps among models that exhibit similar, near-ceiling performance under traditional evaluation. Some key insights emerge from our analysis: (1) the “overthinking trap” is a critical factor contributing to the performance degradation; (2) models trained with the “Long2Short” technique preserve more of their single-problem accuracy under REST, outperforming their standard-trained counterparts. These results establish REST as a cost-efficient, future-proof evaluation paradigm while reducing reliance on continuous human annotation. Code is available at https://github.com/opendatalab/REST.

---

Record id: `doi:10.18653/v1/2026.acl-long.1296`
