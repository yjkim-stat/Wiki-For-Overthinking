<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Thinking-Based Non-Thinking: Solving the Reward Hacking Problem in Training Hybrid Reasoning Models via Reinforcement Learning

- **Authors**: Siyuan Gan, Jiaheng Liu, Boyan Wang, Tianpei Yang, Runqing Miao, Yuyao Zhang, Fanyu Meng, Junlan Feng, Linjian Meng, Jing Huo, Yang Gao 0001
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.2122>
- **DOI**: 10.18653/V1/2026.ACL-LONG.2122
- **Topics**: reasoning-training, test-time-scaling
- **Relevance score**: reasoning-training 0.67

## In one line

Fixes reward hacking in hybrid thinking/non-thinking RL by setting per-query token limits for non-thinking responses derived from the solution part of that query's thinking responses.

## Problem

Hybrid reasoning models decide per query whether to think, and RL is the natural way to train that decision. But RL there suffers reward hacking: a model that does think can be judged as not thinking and rewarded incorrectly. Existing fixes either use SFT, which is computationally costly, or impose uniform token limits on non-thinking responses, which mitigates little — a uniform limit is wrong for every query whose true solution length differs from the average.

## Contributions

- A diagnosis that RL training of hybrid reasoning models suffers reward hacking through misclassification of thinking as non-thinking
- TNT: per-query maximum token budgets for non-thinking responses, derived from the solution component of that query's thinking responses
- Avoidance of SFT and of uniform token limits
- Around 50% token reduction with improved accuracy on five mathematical benchmarks
- Reward hacking probability below 10% across all tested datasets

## Method

Thinking-Based Non-Thinking uses no SFT. It sets a different maximum token budget for the non-thinking response of each query, derived from the solution component of that same query's thinking responses. The thinking response's solution section is a per-query estimate of how long an honest non-thinking answer should be, which is what makes the limit query-adaptive rather than global.

## Results

On five mathematical benchmarks, TNT cuts token usage by around 50% relative to DeepSeek-R1-Distill-Qwen-1.5B/7B and DeepScaleR-1.5B while significantly improving accuracy, and attains the best accuracy-efficiency trade-off among tested methods. The probability of reward hacking in responses classified as not using thinking stays below 10% across all tested datasets.

## Limitations

Benchmarks are not named. Reward hacking is reduced to below 10% but not eliminated, and how hacking is detected for that measurement is unstated. Three backbones, all distilled Qwen-family models at 1.5B/7B. The token limit is derived from the model's own thinking responses, so it inherits any bias in those solution sections.

## Why it matters here

- **reasoning-training**: The only paper in this drain that treats the thinking/non-thinking classifier as itself a source of reward error, and quantifies the residual — below 10%. That matters because the whole hybrid-reasoning line depends on being able to tell the two modes apart, and if the judge is wrong the reward is wrong regardless of the policy. It joins the drain's large difficulty-allocation cluster (industry.152 via confidence, long.1766 via injected difficulty cues, findings-acl.165 via a mode-selection token) as a fourth mechanism for the same decision, and the four are not compared against each other anywhere.

## Entities

- **Concepts**: [reward hacking](../../../../wiki/concepts/reward-hacking.md), hybrid reasoning, [overthinking](../../../../wiki/concepts/overthinking.md), [adaptive compute allocation](../../../../wiki/concepts/adaptive-compute-allocation.md), [prompt difficulty](../../../../wiki/concepts/prompt-difficulty.md), token budget, [verification](../../../../wiki/concepts/verification.md)
- **Methods**: TNT, [reinforcement learning post-training](../../../../wiki/methods/reinforcement-learning-post-training.md), [supervised fine-tuning](../../../../wiki/methods/supervised-fine-tuning.md), [length control](../../../../wiki/methods/length-control.md)
- **Datasets**: _none recorded_

Tags: `reward hacking`, `hybrid reasoning`, `overthinking`, `token budget`, `grpo`

## Abstract

Large reasoning models (LRMs) have attracted much attention due to their exceptional performance. However, their performance mainly stems from thinking, a long Chain of Thought (CoT), which significantly increase computational overhead. To address this overthinking problem, existing work focuses on using reinforcement learning (RL) to train hybrid reasoning models that automatically decide whether to engage in thinking or not based on the complexity of the query. Unfortunately, using RL will suffer the the reward hacking problem, e.g., the model engages in thinking but is judged as not doing so, resulting in incorrect rewards.To mitigate this problem, existing works either employ supervised fine-tuning (SFT), which incurs high computational costs, or enforce uniform token limits on non-thinking responses, which yields limited mitigation of the problem.In this paper, we propose Thinking-Based Non-Thinking (TNT). It does not employ SFT, and sets different maximum token usage for responses not using thinking across various queries by leveraging information from the solution component of the responses using thinking. Experiments on five mathematical benchmarks demonstrate that TNT reduces token usage by around 50\\%$ compared to DeepSeek-R1-Distill-Qwen-1.5B/7B and DeepScaleR-1.5B, while significantly improving accuracy. In fact, TNT achieves the optimal trade-off between accuracy and efficiency among all tested methods. Additionally, the probability of reward hacking problem in TNT’s responses, which are classified as not using thinking, remains below $10\\%$ across all tested datasets.

---

Record id: `doi:10.18653/v1/2026.acl-long.2122`
