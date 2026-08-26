<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# LEASH: Adaptive Length Penalty and Reward Shaping for Efficient Large Reasoning Model

- **Authors**: Yanhao Li, Lu Ma, Jiaran Zhang, Lexiang Tang, Wentao Zhang, Guibo Luo
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.129/>
- **PDF**: <https://aclanthology.org/2026.acl-long.129.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.129
- **Topics**: overthinking
- **Relevance score**: overthinking 0.70

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large Language Models (LLMs) often produce unnecessarily lengthy reasoning traces, which significantly increase computational cost and latency. Existing approaches typically rely on fixed length penalties, but such penalties are hard to tune and fail to adapt to the evolving reasoning abilities of LLMs, leading to suboptimal trade-offs between accuracy and conciseness. To address this challenge, we propose LEASH (adaptive LEngth penAlty and reward SHaping), a reinforcement learning framework for efficient reasoning in LLMs. We formulate length control as a constrained optimization problem and employ a Lagrangian primal–dual method to dynamically adjust the penalty coefficient. When generations exceed the target length, the penalty is intensified; when they are shorter, it is relaxed. This adaptive mechanism guides models toward producing concise reasoning without sacrificing task performance. Experiments on Deepseek-R1-Distill-Qwen-1.5B and Qwen3-4B-Thinking-2507 show that LEASH reduces the average reasoning length by 60% across diverse tasks—including in-distribution mathematical reasoning and out-of-distribution domains such as coding and instruction following—while maintaining competitive performance. Our work thus presents a practical and effective paradigm for developing controllable and efficient LLMs that balance reasoning capabilities with computational budgets.

---

Record id: `doi:10.18653/v1/2026.acl-long.129`
