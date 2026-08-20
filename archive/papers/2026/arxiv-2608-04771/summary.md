<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning

- **Authors**: Qiyuan Zhu, Dezhi Li, Pengyu Cheng, Tianle Chen, Jiacheng Wang, Ruijie Shen, Hao Gu, Sida Lin, Zirui Liu, Jiacheng Liu, Sirui Han
- **Venue**: cs.AI
- **Published**: 2026-08-05
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.04771>
- **PDF**: <https://arxiv.org/pdf/2608.04771v1>
- **Topics**: reasoning-training, test-time-scaling
- **Relevance score**: reasoning-training 0.67, test-time-scaling 0.40

## In one line

Couples KV-cache compression and generation-length control under a single process-reward signal, compressing harder at high-reward reasoning steps and stopping early when confidence is high.

## Problem

Long CoT inflates inference cost, and KV-cache compression is the usual remedy. Existing reasoning-oriented compression applies one uniform policy across the whole trajectory and judges itself only by what it removes from the cache. Two facts undercut that: a reasoning state's tolerance to context loss varies along the trajectory, and a smaller cache makes the model generate more tokens, partly cancelling the saving.

## Contributions

- The observation that tolerance to context loss varies along a reasoning trajectory and that process reward tracks it
- The observation that cache compression is not free on the generation side, since a smaller cache induces more tokens
- ReCo, coordinating reward-adaptive KV-cache compression, a reward-banded reflection-token penalty and confidence-based early stopping under one process reward
- Token and latency reductions across three reasoning models and six benchmarks

## Method

ReCo puts a lightweight process-reward estimator on each completed step and uses its score to drive three coordinated components: reward-adaptive KV-cache compression that shrinks the retained cache harder at high-reward steps and less at low-reward ones; a reward-banded penalty on reflection tokens to curb redundant generation; and confidence-based early stopping triggered when the reasoning is judged reliable. Coordinating the compression side and the generation side under one signal is the point — measuring only cache reduction hides the generation-side rebound.

## Results

Across three reasoning models and six benchmarks, ReCo reduces generated tokens by 37%-65% and end-to-end latency by 2.08x-2.35x over Full CoT, described as largely preserving accuracy.

## Limitations

'Largely preserving accuracy' is not quantified in the abstract, so the accuracy cost of the 37-65% token reduction is unstated. Models and benchmarks are not named. The process-reward estimator is an additional component whose own cost and calibration are not reported, and the claim that deleting tokens at high-reward steps is safer rests on that estimator being right about which steps are high-reward.

## Why it matters here

- **reasoning-training**: Uses a process reward at inference rather than as a training signal, which is a different job for the same object this topic tracks. The transferable claim is that process reward is informative about which parts of a trajectory can be damaged without cost — a use that does not require the reward to be accurate enough to train on.
- **test-time-scaling**: Names a coupling the archive's efficiency thread has mostly ignored: cache compression and generation length are not independent knobs, and a method that reports only cache savings can be silently paid for in extra tokens. That makes end-to-end latency the honest metric, and the 2.08x-2.35x figure is reported that way. Its confidence-based early stopping is a fourth entry alongside the DEER/Dynasor/CUSUM family of stopping signals already tracked here.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), [process reward](../../../../wiki/concepts/process-reward.md), [reasoning redundancy](../../../../wiki/concepts/reasoning-redundancy.md), KV cache compression, early exit, [adaptive compute allocation](../../../../wiki/concepts/adaptive-compute-allocation.md), reflection tokens
- **Methods**: ReCo, process reward model, KV-cache eviction, confidence-based early stopping, reward-banded penalty
- **Datasets**: _none recorded_

Tags: `kv cache`, `overthinking`, `process reward`, `early exit`, `efficient reasoning`

## Abstract

Large Reasoning Models (LRMs) excel on complex tasks through long chain-of-thought (CoT) reasoning, but their lengthy intermediate steps cause severe overthinking that inflates inference cost. KV-cache compression is a common solution, yet existing reasoning-oriented methods apply a uniform policy across the trajectory and judge compression only by what it removes from the cache. Two observations point the other way. First, a reasoning state's tolerance to context loss varies along the trajectory, and process reward tracks it: deleting tokens at high-reward steps preserves accuracy far better than deleting the same budget at random. Second, compression is not free on the generation side, since a smaller cache leads the model to generate more tokens, partly canceling the saving. Together these motivate coordinating both sides under a single process reward. We propose ReCo (Reward-Coordinated Compression), a step-wise framework in which a lightweight process-reward estimator scores each completed step and drives three components: (1) reward-adaptive KV-cache compression that shrinks the retained cache harder at high-reward steps and less at low-reward ones, (2) a reward-banded penalty on reflection tokens that curbs redundant generation, and (3) confidence-based early stopping that triggers when the reasoning is reliable. Across three reasoning models and six benchmarks, ReCo reduces generated tokens by 37%-65% and end-to-end latency by 2.08x-2.35x over Full CoT, all while largely preserving accuracy.

---

Record id: `arxiv:2608.04771`
