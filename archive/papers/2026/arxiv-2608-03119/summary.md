<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Don't Peek at the Answer: Outcome-Masked Group Relative Policy Optimization for Label-Free RLVR

- **Authors**: Yongshi Ye, Liang Zhang, Yidong Chen, Xiaodong Shi, Biao Fu
- **Venue**: cs.AI
- **Published**: 2026-08-04
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.03119>
- **PDF**: <https://arxiv.org/pdf/2608.03119v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-evaluation 0.25, reasoning-training 0.62

## In one line

Diagnoses label-free RLVR's collapse as a shortcut in which the same answer-level consensus signal both estimates the reward and receives the gradient, and fixes it by masking the answer span from updates entirely — so a reward can only be raised by improving the reasoning that produces the answer.

## Problem

Label-free RLVR replaces gold answers with the majority answer among sampled rollouts. That single answer-level signal is then used for two different jobs: estimating each trajectory's reward, and driving token-level policy optimization. Because the answer tokens are the most direct route to a higher reward, the policy can raise its score by sharpening high-frequency answer tokens without improving the reasoning that led to them. The measured consequence is not a mild inefficiency — training improves early, then collapses sharply, with answer diversity falling until the model emits the same answer across whole batches and eventually across different batches.

## Contributions

- Naming and localizing the failure: the collapse is a shortcut through the answer span, not uniform overfitting of the trajectory
- Outcome-Masked Update, which zeroes the gradient on answer-span tokens so learning signals reach only the reasoning chain and format tokens, while rewards are still computed from answer-level statistics
- A soft frequency-based reward — the probability mass a trajectory's answer holds within the sampled group — in place of a binary majority-vote indicator
- Contrast-Augmented Reward, which enlarges the answer pool from G to order G-squared by prompting the model on pairs of existing traces for a short answer only, with those answers used solely as validators and never as training trajectories
- A KL decomposition separating answer-token from reasoning-token divergence, which is what shows the collapse is concentrated on the answer span

## Method

For each question the policy samples a group of trajectories, each consisting of a reasoning chain and a boxed answer span. The soft reward for a trajectory is the fraction of the group whose answers match its own, plus a binary format term. The update is a group-relative clipped surrogate with a KL penalty, modified by a binary mask that is zero on every token inside the answer span — so reward differences propagate only into the reasoning and formatting tokens. Contrast augmentation then improves the reward estimate without more rollouts: every ordered pair of trajectories is presented back to the model with both reasoning traces and a request for a short final answer, which is cheap because no reasoning is regenerated, and the resulting answers are added to the pool over which the frequency-based reward is computed. Training uses 7,500 MATH problems with validation on a held-out MATH set, across three backbones spanning two architectures and 1.7B to 7B, evaluated on five mathematics benchmarks plus code, instruction-following and multi-task sets, against a ground-truth-reward oracle and four label-free baselines including majority voting, confidence, entropy minimization and a consensus variant.

## Results

The method is the best label-free approach on the average of nine benchmarks for all three backbones, and lands close to the supervised oracle — 35.19 against 35.55, 31.21 against 31.53, and 43.25 against 43.90 — while on non-mathematics tasks with the 7B backbone it exceeds the oracle (38.71 against 38.26). The ablation identifies which component does the work: removing the answer mask is the largest degradation and, more tellingly, reintroduces the training collapse, while the mask alone without contrast augmentation already beats vanilla majority voting by 1.70 points. Replacing the soft frequency reward with a hard majority indicator also costs performance. The soft-masking sweep shows the effect is not gradual — applying 25% of the outcome gradient to answer tokens tracks full masking, 50% degrades, and 75% collapses rapidly, so partial exposure of the answer span to answer-level pseudo-rewards is what reopens the shortcut. The mechanistic evidence is the KL decomposition: under majority voting, divergence on answer tokens rises sharply while reasoning-token divergence grows slowly, and masking keeps the former low and stable, confirming the collapse is concentrated where the paper claims. The comparison against simply sampling more is the sharpest test-time result: contrast augmentation at 8 rollouts reaches 35.19 in 6h14, while direct sampling at 64 rollouts reaches 34.42 in 22h41 — worse than 16 rollouts — which the paper attributes to scaling self-consistency amplifying spurious consensus, since with more samples agreement forms more easily even around incorrect answers. In test-time training, majority voting on one backbone actively lowers average accuracy (36.92 to 35.09) by converging toward an incorrect consensus, where this method reaches 39.08.

## Limitations

The paper states three. Backbones are open models up to 7B, so behaviour at substantially larger scales is unstudied. Contrast augmentation is more efficient than more rollouts but still adds inference overhead. And the method reduces shortcut optimization on answer tokens while still relying on outcome-based reward signals rather than explicit supervision of reasoning quality — the authors name incorporating richer process-level signals without heavy annotation as future work. A reader should add that for baselines exhibiting late-stage collapse the best validation checkpoint is reported, which is the fair choice but means the baseline numbers describe a model that would not survive continued training, and that the training corpus is mathematics only while the generalization claims rest on transfer to the other benchmark families.

## Why it matters here

- **reasoning-training**: It supplies a third answer to the process-versus-outcome question this archive has been circling, and one that neither of the existing two anticipates. The archive's finding is that dense process reward works only as a modifier on an outcome signal; this paper keeps the outcome signal as the only reward and changes *where its gradient lands*, masking the answer span so the same reward can only be earned through the reasoning. The mask alone beats majority voting by 1.70 points and removing it reintroduces collapse — so the choice is not just how to weight process against outcome, but which tokens an outcome reward is allowed to touch. That is a cheaper intervention than any process reward in this archive, since it needs no step segmentation, no reference model and no judge. Two further results transfer. The KL decomposition is a diagnostic worth copying: separating answer-token from reasoning-token divergence localizes a collapse that aggregate entropy would only register as a symptom. And the finding that 64 rollouts do worse than 16 is a concrete case of the archive's recurring caution about spending more inference on the same signal — here more samples make a spurious consensus easier to form, so scaling the sample count strengthens a misaligned reward rather than averaging it away.

## Entities

- **Concepts**: label-free reinforcement learning, [reward hacking](../../../../wiki/concepts/reward-hacking.md), mode collapse, self-consistency, majority voting, [credit assignment](../../../../wiki/concepts/credit-assignment.md), [outcome reward](../../../../wiki/concepts/outcome-reward.md), [entropy collapse](../../../../wiki/concepts/entropy-collapse.md), test-time training, KL divergence, spurious consensus
- **Methods**: OM-GRPO, outcome-masked update, contrast-augmented reward, [GRPO](../../../../wiki/methods/grpo.md), [RLVR](../../../../wiki/methods/rlvr.md), [majority voting](../../../../wiki/methods/majority-voting.md), [self-consistency](../../../../wiki/methods/self-consistency.md), entropy minimization, [process reward model](../../../../wiki/methods/process-reward-model.md)
- **Datasets**: [MATH](../../../../wiki/datasets/math.md), [MATH-500](../../../../wiki/datasets/math500.md), [AIME 2024](../../../../wiki/datasets/aime-2024.md), [AIME 2025](../../../../wiki/datasets/aime-2025.md), [GSM8K](../../../../wiki/datasets/gsm8k.md), [AMC](../../../../wiki/datasets/amc.md), [LiveCodeBench](../../../../wiki/datasets/livecodebench.md), CRUX, [IFEval](../../../../wiki/datasets/ifeval.md), [MMLU-Pro](../../../../wiki/datasets/mmlu-pro.md)

Tags: `label-free rlvr`, `reward hacking`, `mode collapse`, `credit assignment`, `test-time training`

## Abstract

Reinforcement Learning with Verifiable Rewards (RLVR) improves LLM reasoning but typically relies on ground-truth (GT) answers, limiting scalability. Voting-based label-free RLVR replace gold supervision with answer-level consensus from model samples. However, collapse arises when the same answer-level signal is used both to estimate rewards and to drive token-level policy optimization, encouraging the model to directly reinforce answer tokens rather than improve reasoning. We propose OM-GRPO, a label-free RLVR framework that decouples reward estimation from policy optimization. OM-GRPO masks gradients on the answer span while retaining answer-level rewards through a soft consensus signal, shifting optimization pressure away from answer tokens. We further introduce Contrast-Augmented Reward, which refines reward estimation via low-cost pairwise comparisons over existing trajectories without additional rollouts. Across diverse reasoning benchmarks and three LLM backbones, OM-GRPO consistently outperforms existing label-free RLVR methods and matches supervised GT-reward training with stable optimization. This stability is particularly beneficial in the Test-Time Training setting, where OM-GRPO surpasses majority voting by 4.24 points.

---

Record id: `arxiv:2608.03119`
