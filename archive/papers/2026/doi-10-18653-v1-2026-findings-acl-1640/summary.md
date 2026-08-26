<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Think Smart, Not Hard: Difficulty Adaptive Reasoning for Large Audio Language Models

- **Authors**: Zhichao Sheng, Shilin Zhou, Chen Gong, Zhenghua Li
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1640/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1640.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1640
- **Topics**: overthinking
- **Relevance score**: overthinking 0.67

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large Audio Language Models (LALMs) employing the Chain-of-Thought paradigm have demonstrated remarkable reasoning capabilities. Though different problems naturally require varying depths of reasoning, existing methods often determine whether to perform reasoning, lacking fine-grained mechanisms to adapt reasoning length to problem complexity. As a result, LALMs often adopt a one-size-fits-all reasoning strategy, leading to redundant overthinking for simple tasks and insufficient reasoning for complex ones. In this paper, we conduct an in-depth analysis of LALM reasoning behavior and argue that effective and efficient reasoning should be adaptively aligned with task difficulty. To this end, we propose a difficulty-adaptive reasoning method for LALMs. Specifically, we introduce a reward function that dynamically links reasoning length to the model’s perceived problem difficulty, encouraging shorter reasoning for easy tasks and longer reasoning for more complex ones. Extensive experiments on three datasets demonstrate that our method consistently improves performance while reducing average reasoning length by at least 50%, achieving higher efficiency without sacrificing accuracy.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1640`
