<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning

- **Authors**: Zheng Li, Qingxiu Dong, Jingyuan Ma, Di Zhang, Kai Jia, Zhifang Sui
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1063/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1063.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1063
- **Topics**: overthinking
- **Relevance score**: overthinking 0.62

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Recently, large reasoning models demonstrate exceptional performance on various tasks. However, reasoning models always consume excessive tokens even for simple queries, leading to resource waste and prolonged user latency. To address this challenge, we propose SelfBudgeter - a self-adaptive reasoning strategy for efficient and controllable reasoning. Specifically, we first train the model to self-estimate the required reasoning budget based on the query. We then introduce budget-guided GRPO for reinforcement learning, which effectively maintains accuracy while reducing output length. Experimental results demonstrate that SelfBudgeter dynamically allocates budgets according to problem complexity, achieving an average response length compression of 61% on math reasoning tasks while maintaining accuracy. Furthermore, SelfBudgeter allows users to see how long generation will take and decide whether to continue or stop. Additionally, users can directly control the reasoning length by setting token budgets upfront.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1063`
