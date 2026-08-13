<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ConRub-Med: Reinforcement Learning with Consensus Rubrics for Open-Ended Medical Question Answering

- **Authors**: Taojie Zhu, Yuan Xia, Tao Sun, Yizhi Wang, Yan Chen, Qunshan He, Tian Guan, Jian Wang, Jinjie Gu, Junwei Liu, Yonghong He
- **Venue**: cs.CL
- **Published**: 2026-08-11
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.10996>
- **PDF**: <https://arxiv.org/pdf/2608.10996v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Reinforcement learning with verifiable rewards has been especially effective in mathematics and coding, where answers can be checked automatically. Many open-ended medical questions lack comparably cheap outcome verifiers: responses may be partly correct, incomplete, or contain clinically consequential errors. Rubrics written or validated by physicians offer strong clinical grounding, but involving experts in every instance is costly. Model-generated rubrics make this supervision scalable. We introduce ConRub-Med to preserve useful distinctions as rubric feedback moves from construction to policy optimization. For each prompt, three heterogeneous language models propose atomic criteria independently; a separate model reviews them, retaining only criteria with semantic support from all three generators. Three-State scoring distinguishes correct coverage, missing information, and incorrect claims. Errors receive negative rather than zero credit. When every response in a complete Group Relative Policy Optimization (GRPO) group receives the same final reward, a pairwise judge provides sequence advantages only if both candidate orders agree, without changing the scalar rewards. Groups without ties use vanilla GRPO. In a blinded study matched by question, two medical experts rate panels from the full pipeline as more clinically relevant than panels produced by one generator. Across the evaluated open models, ConRub-Med ranks first on six of nine benchmarks and achieves the highest medical and generalization averages. Using the resulting rubric dataset of 5,166 prompts, it scores $38.98 \pm 1.04$ (mean $\pm$ SD) on HealthBench-Hard, compared with InfiMed-ORBIT's 33.60 with 8,000 samples and 37.30 with 28,000.

---

Record id: `arxiv:2608.10996`
