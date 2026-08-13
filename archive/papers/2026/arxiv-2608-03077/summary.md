<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# PAMT: Process-Aligned Reinforcement Learning for Multi-Domain Machine Translation

- **Authors**: Yongshi Ye, Biao Fu, Chongxuan Huang, Yidong Chen, Xiaodong Shi
- **Venue**: cs.CL
- **Published**: 2026-08-04
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.03077>
- **PDF**: <https://arxiv.org/pdf/2608.03077v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.50

## In one line

Scores each reasoning step of a translation by how much appending it raises a frozen reference model's teacher-forced likelihood of the gold translation, and adds that as a dense per-step reward on top of sequence-level quality — after first establishing that explicit reasoning helps long and hard inputs while drifting on terminology and style.

## Problem

Explicit reasoning before translating is assumed to help because it exposes the decisions domain-faithful translation needs — ambiguity resolution, terminology, register. The paper's own survey across 15 domains and four directions finds that assumption half true and half false in a specific pattern, and traces the failure to credit assignment: reinforcement-learning methods for reasoning-augmented translation reward whole outputs or whole trajectories, so nothing identifies which intermediate translation decision produced an unfaithful result, and the supervision granularity is therefore misaligned with the decision granularity.

## Contributions

- A systematic split of when explicit reasoning helps: it wins at document level on discourse phenomena and from difficulty level 2 upward, while the strongest reasoning model still trails the strongest ordinary one on style and terminology errors
- A process potential defined without any learned reward model — the teacher-forced log-likelihood of the reference translation under a frozen reference policy, conditioned on the prompt plus the first k reasoning steps
- A per-step gain taken as the difference of consecutive potentials, distributed uniformly across that step's tokens so long steps are not favoured merely for containing more of them
- Reuse of the same frozen policy for both process scoring and the KL penalty, so the method adds no scoring model
- A diagnostic that the process signal shapes decisions rather than only outcomes — labelling steps by decision type and tracking how each migrates between positive- and negative-gain steps over training

## Method

A cold-start supervised stage on roughly 7,000 domain-aware long-CoT examples distilled from a reasoning model, about 700 per domain across ten domains, teaches the model to emit an explicit reasoning span followed by a translation. In the reinforcement-learning stage the reasoning span is split into steps at blank lines. Sequence-level rewards handle the output: a binary format reward, and a quality reward that averages normalized BLEU, COMET and COMETKiwi, the last included to reduce over-reliance on potentially noisy or domain-specific references. The process reward comes from a frozen reference policy: for the prefix of the first k steps, the potential is the teacher-forced log-likelihood of the gold translation given that prefix, and the step's gain is the increase over the previous prefix — so a step that makes the reference more predictable is rewarded and one that makes it less predictable is penalized. Format and outcome rewards land on the last valid token while process gains land at their own positions, giving a return-to-go that carries terminal signal to every token and dense signal inside the trace, optimized with a GRPO-style clipped surrogate and KL regularization against the same frozen policy. Two backbones are trained on a 20K multi-domain parallel set and evaluated in-domain over eight domains, out of domain over five more, and across five language settings, against large general models, reasoning models, and ten translation-specialized systems.

## Results

The preliminary survey is the more interesting half. At document level the best reasoning model leads on discourse phenomena (36.17 against 35.79), and by translation difficulty the ordinary models are competitive on easy inputs and fall away sharply as difficulty rises while reasoning models take the lead from level 2 onward. But the MQM breakdown reverses on exactly the dimensions the reasoning was supposed to help: the strongest reasoning model has the lowest severity-weighted error rate overall and still trails the strongest ordinary model on style and terminology (29.58 and 12.22 against 29.43 and 10.68), and terminology accuracy is substantially less stable than the general semantic gains. The trained method leads all translation-specialized baselines on average in-domain, out of domain and multilingually on both backbones, and stays competitive with much larger general systems. Its ablation is the part worth carrying: removing the sequence-level quality reward is the single largest degradation (in-domain BLEU 29.83 to 22.94), removing reinforcement learning entirely gives the weakest results, and removing the process reward or its token-level distribution costs less than either. So the dense signal is a modifier on an outcome anchor rather than a replacement for it. On the failure it was built for, the process reward cuts style and terminology error rates by about two points each and raises terminology accuracy to 42.97, above a baseline that enforces terminology constraints at the output and still shows 19.33 and 19.19 error rates with a 46.15 non-translation rate — output-level constraints cannot stabilize an unaligned process. Training dynamics support the mechanism: the fraction of positive-gain steps rises and negative-gain falls throughout, and all three labelled decision types migrate toward the positive-gain population.

## Limitations

The paper has no limitations section. What a reader should weigh: the process potential is the likelihood of the *reference* translation, so the signal exists only where a gold target does — this is training-time reward shaping and nothing here transfers to inference or to settings without references, and it inherits whatever domain bias the references carry, which the authors partly acknowledge by including a reference-free metric in the outcome term. The frozen scoring model is also the KL anchor, which is economical but means process credit is defined relative to a policy the trained model is simultaneously being pulled toward; the authors run an overfitting check showing the process reward is small in scale against the outcome reward and that KL from the frozen model rises steadily, which argues against collapse but does not rule out subtler coupling. Step boundaries are blank lines, a formatting artefact rather than a semantic unit. Two backbones under 10B, no seeds or variance, and the difficulty stratification that carries the headline split is assigned by another language model rather than by an independent standard.

## Why it matters here

- **reasoning-training**: Its process signal is, up to domain, the same construction this archive already holds from search agents: the marginal change in a frozen model's likelihood of the gold answer when one more step is appended. Two independent groups, one on retrieval and one on translation, arrived at the same dense reward without a learned reward model — which makes it worth naming as a pattern rather than a trick, and worth noting that both require the gold answer at training time and so neither yields an inference-time verifier. The ablation is the third instance in this archive of the same ordering: dense process reward helps, and removing the terminal outcome reward hurts more than removing the process reward does. And the terminology result is a clean case of a failure that output-level constraints cannot reach — a baseline enforcing terminology at the output shows higher terminology error and a 46% non-translation rate, while supervising the intermediate decisions lowers both, which is the archive's process-versus-outcome argument stated on a metric that is not accuracy.

## Entities

- **Concepts**: [credit assignment](../../../../wiki/concepts/credit-assignment.md), [process reward](../../../../wiki/concepts/process-reward.md), [outcome reward](../../../../wiki/concepts/outcome-reward.md), [reward shaping](../../../../wiki/concepts/reward-shaping.md), [advantage estimation](../../../../wiki/concepts/advantage-estimation.md), terminology control, domain adaptation, long chain-of-thought, [reasoning drift](../../../../wiki/concepts/reasoning-drift.md)
- **Methods**: PAMT, [GRPO](../../../../wiki/methods/grpo.md), [supervised fine-tuning](../../../../wiki/methods/supervised-fine-tuning.md), [long chain-of-thought distillation](../../../../wiki/methods/long-chain-of-thought-distillation.md), [KL regularization](../../../../wiki/methods/kl-regularization.md), [teacher forcing](../../../../wiki/methods/teacher-forcing.md), [GEMBA-MQM](../../../../wiki/methods/gemba-mqm.md)
- **Datasets**: [WMT22](../../../../wiki/datasets/wmt22.md), WMT23 Terminology Shared Task, Guofeng WebNovel, Multi-Domain

Tags: `machine translation`, `process reward`, `credit assignment`, `reinforcement learning`, `terminology`

## Abstract

Multi-domain machine translation (MDMT) requires more than fluent generation: it demands domain-sensitive translation decisions such as domain disambiguation, terminology control, and stylistic adaptation. Large reasoning models (LRMs) make such decisions explicit through intermediate translation steps, but our analysis across 15 domains and four translation directions shows that this explicit reasoning is double-edged: it improves long-form and high-difficulty translation, yet often drifts in terminology-intensive and stylistically constrained settings. We trace this failure to a credit-assignment bottleneck: existing methods optimize final outputs or coarse trajectories, but cannot identify which translation steps actually help the final translation. To address this, we propose PAMT, a process-aligned training framework that combines cold-start domain-aware Long-CoT supervision with reinforcement learning. PAMT uses sequence-level format and outcome rewards for the final translation, together with a step-level process reward that measures how much each explicit translation step increases the likelihood of the reference translation. Across two backbones, PAMT improves over base models, outperforms MT-specialized baselines on average, and remains competitive with strong LLMs/LRMs across in-domain, OOD, and multilingual settings.

---

Record id: `arxiv:2608.03077`
