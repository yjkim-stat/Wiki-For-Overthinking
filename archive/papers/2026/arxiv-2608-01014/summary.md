<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Cloud-ScPO: Hidden-State Geometry for Semi-Supervised Preference Optimization in LLM Reasoning

- **Authors**: Yuzhou Liu, Xiyang Hu
- **Venue**: cs.CL
- **Published**: 2026-08-02
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.01014>
- **PDF**: <https://arxiv.org/pdf/2608.01014v1>
- **Topics**: reasoning-evaluation
- **Relevance score**: reasoning-evaluation 0.40, reasoning-interpretability 0.25, test-time-scaling 0.25

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Preference optimization improves mathematical reasoning in large language models (LLMs), but reliable chosen-rejected pairs usually require verified answers, human annotations, or external reward models. We investigate whether preference supervision can instead be derived from the model's internal representation geometry in a semi-supervised setting. Our analysis shows that reasoning trajectories generated across different mathematical problems form structured global point clouds in which correct and incorrect trajectories exhibit different geometric organization. Based on this observation, we propose Cloud--ScPO, a topology-guided preference-mining framework that uses a small labeled set to construct multiple correct and incorrect reference Clouds. Each trajectory is represented by a mean-pooled hidden state and scored against connectivity-induced components using a component-level soft $k$-nearest-neighbor measure averaged across reference banks. We combine this cross-problem Cloud signal with prompt-level self-consistency: self-consistency determines the answer-level preference direction, while Cloud scoring selects concrete trajectories and filters pairs by their score margin. Experiments on GSM8K and MATH-Numeric across four model settings show that Cloud--ScPO consistently improves over ScPO, with gains of up to 4.49\% on GSM8K and 4.19\% on MATH-Numeric. Pair-level analyses further show that Cloud--ScPO maintains comparable correctness reliability while more effectively separating informative chosen trajectories from incomplete, repetitive, or otherwise low-quality rejected responses.

---

Record id: `arxiv:2608.01014`
