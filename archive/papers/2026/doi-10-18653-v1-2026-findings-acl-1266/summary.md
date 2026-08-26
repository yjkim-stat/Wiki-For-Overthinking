<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Revisiting Entropy in Reinforcement Learning for Large Reasoning Models

- **Authors**: Renren Jin, Pengzhi Gao, Yuqi Ren, Zhuowen Han, Tongxuan Zhang, Wuwei Huang, Wei Liu, Jian Luan, Deyi Xiong
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1266/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1266.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1266
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Reinforcement learning with verifiable rewards (RLVR) has emerged as a prominent paradigm for enhancing the reasoning capabilities of large language models (LLMs). However, the entropy of LLMs usually collapses during RLVR training, leading to premature convergence to suboptimal local minima and hindering further performance improvement. Although various approaches have been proposed to mitigate entropy collapse, a comprehensive study of entropy in RLVR remains lacking. To bridge this gap, we conduct extensive experiments to investigate the entropy dynamics of LLMs trained with RLVR and analyze how model entropy correlates with response diversity, calibration, and performance across various benchmarks. Our results identify three key factors that influence entropy: the clipping thresholds in the optimization objective, the number of off-policy updates, and the diversity of the training data. Furthermore, through both theoretical analysis and empirical validation, we demonstrate that tokens with positive advantages are the primary drivers of entropy collapse. Motivated by this insight, we propose Positive-Advantage Reweighting, a simple yet effective approach that regulates model entropy by adjusting the loss weights assigned to tokens with positive advantages during RLVR training, while maintaining competitive performance.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1266`
