<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Step-GRPO: Internalizing Dynamic Early Exit for Efficient Reasoning

- **Authors**: Benteng Chen, Weida Wang, Shufei Zhang, Mingbao Lin, Min Zhang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.990/>
- **PDF**: <https://aclanthology.org/2026.acl-long.990.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.990
- **Topics**: overthinking
- **Relevance score**: overthinking 0.73

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large reasoning models that use long chain-of-thought excel at problem-solving yet waste compute on redundant checks. Curbing this overthinking is hard: training-time length penalties can cripple ability, while inference-time early-exit adds system overhead. To bridge this gap, we propose Step-GRPO, a novel post-training framework that internalizes dynamic early-exit capabilities directly into the model. Step-GRPO shifts the optimization objective from raw tokens to semantic steps by utilizing linguistic markers to structure reasoning. We introduce a Dynamic Truncated Rollout mechanism that exposes the model to concise high-confidence trajectories during exploration, synergized with a Step-Aware Relative Reward that dynamically penalizes redundancy based on group-level baselines. Extensive experiments across three model sizes on diverse benchmarks demonstrate that Step-GRPO achieves a superior accuracy-efficiency trade-off. On Qwen3-8B, our method reduces token consumption by 32.0% compared to the vanilla model while avoiding the accuracy degradation observed in traditional length-penalty methods.

---

Record id: `doi:10.18653/v1/2026.acl-long.990`
