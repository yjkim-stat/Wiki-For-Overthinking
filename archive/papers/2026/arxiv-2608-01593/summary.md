<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Latent Thought Credit: Multi-Answer Credit Assignment for Latent Reasoning

- **Authors**: Xuyang Zhao, Liting Zhang, Zichen Xu, Yong Chen, Wenjia Zeng, Shiwan Zhao, Qicheng Li
- **Venue**: cs.AI
- **Published**: 2026-08-03
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.01593>
- **PDF**: <https://arxiv.org/pdf/2608.01593v1>
- **Topics**: reasoning-faithfulness
- **Relevance score**: reasoning-evaluation 0.25, reasoning-faithfulness 0.50, reasoning-training 0.25

## In one line

Estimates what a continuous latent thought is worth by freezing the context after it and averaging the rewards of several answers sampled from that fixed context, then credits latent positions with the resulting thought-level advantage and answer positions with the ordinary group-relative one.

## Problem

A latent thought is a continuous state, so it is never observed directly and can only be judged by the answers that follow it. A single sampled answer therefore mixes the thought's quality with answer-sampling noise, and existing latent and soft-reasoning methods do not estimate a sampled thought's expected downstream reward at all — they inherit one trajectory-level scalar for the whole rollout, the same problem outcome-only RL has for discrete chains, made worse because the object being credited cannot be inspected.

## Contributions

- Reformulating latent training-signal construction as expected-utility estimation: freeze the post-thought context and average rewards over several answers drawn from it
- A two-level credit scheme in which latent-thought positions are weighted by an advantage normalized across the K thoughts for a prompt and answer positions by the usual group-relative advantage across all K*M answers
- A thought-matching auxiliary that pushes the current policy's clean top-k logit embedding toward the rollout's latent thought, weighted by a softmax over thought-level advantages, so high-credit latent geometry is easier to reproduce
- Fixed-context diagnostics that measure the credit signal itself — between-thought against within-thought reward variance, estimator error against a held-out reference, and pairwise ordering error and regret

## Method

At each latent step the rollout policy's clean logits are Gumbel-perturbed and softmaxed at temperature tau_think, and the normalized probability-weighted mixture of vocabulary embeddings becomes the latent token, so exploration enters through the Gumbel noise. K such latent thoughts are sampled per prompt; after the i-th thought ends its context is frozen and M discrete answers are sampled from it, and the mean of their rewards estimates that thought's expected utility. Thought-level advantages standardize those K estimates; answer-level advantages standardize rewards jointly over all K*M answers. The policy loss is REINFORCE-style with stop-gradient advantages, applying the thought-level weight to latent positions through the Gumbel-Softmax surrogate and the answer-level weight to answer tokens. The auxiliary term converts the current policy's clean logits at each latent step into a top-k-restricted embedding prediction and penalizes its squared distance to the detached rollout latent, normalized by hidden size and weighted across thoughts by a softmax of their advantages; the total objective adds it with weight lambda. Experiments use Qwen2.5-3B-Instruct and 7B-Instruct at a fixed rollout budget B = K*M = 8 with (K, M) = (2, 4), greedy decoding at evaluation, over GSM8K, MATH, MATH500, MMLU-STEM and ARC-Challenge, against GRPO, GRPO-MA and HRPO under matched model, prompt format, reward and sampling temperature.

## Results

At 3B, LTC is highest on all five sets and on the average (70.16% against 69.28% for HRPO, 68.59% for GRPO-MA, 68.45% for GRPO). At 7B it has the highest average, 75.31% against HRPO's 74.08%, but the per-task picture is mixed: it wins GSM8K (89.15%), MATH500 (67.60%) and MMLU-STEM (70.10%) while losing MATH narrowly (67.22% against 67.40%) and ARC-Challenge by 1.5 points (82.50% against 84.00%). Under stochastic sampling on GSM8K at 3B, it leads across the whole pass@k range from 64 completions, with the margin largest at small k and narrowing but not vanishing by pass@64. The four ablations all hurt, in a task-dependent order: on GSM8K the largest loss is removing thought-matching (-3.11) and on MATH it is removing the latent thought entirely (-3.80), with removing the hierarchical scheme costing 2.91 and 2.30 and removing Gumbel noise 2.12 and 1.70. Budget allocation matters in a specific direction: at B = 8, (K, M) = (2, 4) beats (4, 2) by 1.97 points, so spending budget on answer replication beats spending it on more thoughts, though at B = 16 the balanced (4, 4) is best at 85.15%. The diagnostics are the most interesting part and cut against the method's own premise. Within-thought answer variance exceeds between-thought variance in every setting, and training makes this worse: between-thought variance falls from 0.0244 to 0.0043 while within-thought variance rises from 0.0376 to 0.0568, so the noise-to-signal ratio goes from 1.54 to 13.10. Averaging more answers does reduce estimator error (MAE from 0.1148 at one probe answer to 0.0490 at eight, for the final policy), but pairwise ordering error for the trained policy stays near 0.44-0.47 across every probe budget, against 0.26 for the initial policy — while regret stays small at 0.025-0.032.

## Limitations

The paper states its scope in the conclusion rather than a limitations section: two Qwen2.5-Instruct sizes, mathematics and STEM multiple choice with verifiable or easily normalized rewards, and fixed K and M, with noisier open-ended rewards, other model families, and the interpretability of the continuous thoughts left as future work. Two things a reader should add. First, the diagnostics undercut the mechanism more than the paper says: after training, thought-level utilities are so close together that ordering them is barely better than chance, which means the thought-level advantage — the paper's central signal — is estimating differences that have largely collapsed. The paper reads the small regret as reassurance, but the honest statement is that the credit signal survives because choosing wrong costs little, not because it chooses well. Second, the tuning surface is broad and task-dependent: the matching strength, the top-k support size (non-monotonic, with the highest-peak setting finishing a full point below the best final one) and the K-M split each have a different optimum per dataset, and all of them are read off the evaluation benchmarks. Gains over HRPO are around 0.9 to 1.2 average points with no seeds or variance reported.

## Why it matters here

- **reasoning-faithfulness**: Its diagnostics are evidence about latent traces rather than about the training method, and they bear on the archive's established finding that intermediate reasoning can be swapped or deleted with the answer unchanged. Here the same phenomenon is measured from the training side: after RL, the expected-reward spread across different latent thoughts for the same prompt collapses to 0.0043 while answer-sampling noise under a fixed thought rises to 0.0568, and pairwise ordering of thoughts by their downstream utility degrades to near chance. That is a quantitative statement that the latent thoughts a trained policy produces become close to interchangeable in their effect on the answer — which is what a faithfulness account would predict, and which the paper reports without drawing that conclusion.

## Entities

- **Concepts**: [latent reasoning](../../../../wiki/concepts/latent-reasoning.md), [credit assignment](../../../../wiki/concepts/credit-assignment.md), [advantage estimation](../../../../wiki/concepts/advantage-estimation.md), expected reward estimation, reward variance, soft thinking, [exploration](../../../../wiki/concepts/exploration.md)
- **Methods**: Latent Thought Credit, [GRPO](../../../../wiki/methods/grpo.md), GRPO-MA, HRPO, Gumbel-Softmax, [REINFORCE](../../../../wiki/methods/reinforce.md)
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH](../../../../wiki/datasets/math.md), [MATH-500](../../../../wiki/datasets/math500.md), [MMLU-STEM](../../../../wiki/datasets/mmlu-stem.md), ARC-Challenge

Tags: `latent reasoning`, `credit assignment`, `reinforcement learning`, `variance`, `soft tokens`

## Abstract

Latent reasoning allows language models to carry out intermediate reasoning in continuous latent representations rather than fully externalizing it as discrete chains of thought. However, assigning credit to such latent thoughts from answer-only rewards is difficult: a single final answer mixes thought quality with answer-sampling noise. We propose \textbf{Latent Thought Credit (LTC)}, a hierarchical credit-assignment framework for latent reasoning. For each prompt, LTC samples multiple latent thoughts, fixes the context after each thought, and estimates thought-level expected reward by averaging rewards over multiple answers generated from that fixed context. LTC uses thought-level advantages to optimize the latent-thought phase, answer-level advantages to optimize the answer phase, and an advantage-weighted thought-matching objective that helps the policy reproduce high-credit latent thoughts. We instantiate LTC in a GRPO-style on-policy training framework and evaluate it across mathematical reasoning and STEM multiple-choice tasks. LTC achieves the best average accuracy among the compared methods, while ablations and fixed-context diagnostics show that multi-answer estimation reduces reward-estimation error and mitigates ambiguous or incorrect thought-level credit.

---

Record id: `arxiv:2608.01593`
