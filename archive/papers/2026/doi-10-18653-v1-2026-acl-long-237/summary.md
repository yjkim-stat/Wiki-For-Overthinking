<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Miner: Mining Intrinsic Mastery for Data-Efficient RL in Large Reasoning Models

- **Authors**: Shuyang Jiang, Yuhao Wang, Ya Zhang 0002, Yanfeng Wang 0001, Yu Wang 0027
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.237>
- **DOI**: 10.18653/V1/2026.ACL-LONG.237
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.80

## In one line

Addresses wasted rollouts in critic-free RL on prompts where every sampled rollout is already correct and the advantage estimate is therefore zero.

## Problem

Critic-free RL methods for large reasoning models are severely inefficient on positive homogeneous prompts — those where all rollouts come out correct. Because the advantage is computed relative to the group, a group with no variance yields zero advantage, so every rollout spent on that prompt teaches nothing.

## Contributions

- Identification of rollout waste on positive homogeneous prompts, where uniformly correct groups give zero advantage in critic-free RL

## Method

The abstract available from the ACL Anthology is truncated after introducing the problem and announcing a simple solution, so the method is not recorded here.

## Results

_not recorded_

## Limitations

The published abstract is truncated mid-sentence and contains no method description, results, models or benchmarks. Nothing beyond the problem statement can be established from it, and the full paper is required.

## Why it matters here

- **reasoning-training**: The problem it names is real and specific to how GRPO computes advantage: once a prompt is reliably solved, its rollouts carry no gradient, so continued training spends compute on prompts that cannot teach. That is the same structural defect arxiv:2608.04698 hits from the other end, where uniformly failed groups also collapse the advantage — together they bracket the zero-variance failure of group-relative methods, and it connects to the archive's prompt-difficulty thread by implying that curriculum selection is not an optimization but a requirement. The method is unavailable from the truncated abstract.

## Entities

- **Concepts**: [advantage estimation](../../../../wiki/concepts/advantage-estimation.md), group-relative advantage, rollout efficiency, [data efficiency](../../../../wiki/concepts/data-efficiency.md), [prompt difficulty](../../../../wiki/concepts/prompt-difficulty.md), zero-variance group
- **Methods**: critic-free reinforcement learning, [GRPO](../../../../wiki/methods/grpo.md)
- **Datasets**: _none recorded_

Tags: `advantage estimation`, `rollout efficiency`, `grpo`, `data efficiency`, `truncated-abstract`

## Abstract

Current critic-free RL methods for large reasoning models suffer from severe inefficiency when training on positive homogeneous prompts (where all rollouts are correct), resulting in waste of rollouts due to zero advantage estimates. We introduce a radically simple yet powerful solution to M

---

Record id: `doi:10.18653/v1/2026.acl-long.237`
