<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Exploration-Exploitation Reshaping towards Efficient Reasoning for Large Language Models

- **Authors**: Yufeng Shi, Weilin Luo, Yuxiang Zhang, Zongmeng Zhang, Haoyang Liu, Yubing Wang, Bin Wang, Wengang Zhou, Houqiang Li
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1520/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1520.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1520
- **Topics**: overthinking
- **Relevance score**: overthinking 0.67

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

While excelling at solving complex problems, Large Reasoning Models (LRMs) are still constrained by the overthinking issue. Most current studies rely on reward shaping in Reinforcement Learning (RL) to shorten the Chain-of-Thought (CoT) of LRMs, remaining sample-inefficient and non-robust due to the absence of guided exploration and prioritized exploitation. To address these issues, we propose a novel policy optimization framework with Self-Imitation and self-Guidance MechAnisms (SIGMA), which reshapes the exploration and exploitation through two core components: (i) self-imitation exploitation, which enables the prioritized exploitation of high-value prompts and rollouts by introducing a self-imitated loss and a dynamic sampling strategy based on compression rate; (ii) self-guidance exploration, which provides a preference-aware exploration guidance through diverse and pluggable self-rewriting strategies. Experiments across various datasets indicate that our method achieves superior reasoning efficiency without compromising, and even facilitating, the overall accuracy. Furthermore, ablation studies show that the proposed mechanisms can provide flexible control interfaces for the tradeoff between the reasoning accuracy and efficiency of LRMs.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1520`
