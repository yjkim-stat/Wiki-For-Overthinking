<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Beyond Solvability: Task Learnability as a Static Prior for LLM RL Post-Training

- **Authors**: Ting Zhou, Zhenqing Ling, Daoyuan Chen, Qianli Shen, Yilun Huang, Ying Shen, Yaliang Li
- **Venue**: cs.LG
- **Published**: 2026-08-10
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.09217>
- **PDF**: <https://arxiv.org/pdf/2608.09217v1>
- **Topics**: reasoning-evaluation
- **Relevance score**: reasoning-evaluation 0.40, reasoning-training 0.25

## In one line

Separates how well a policy currently does on a task from how positively that task responds to further training, shows the second is reproducible across independent runs and predicts downstream value at matched current pass rate, and estimates it from a short probe run before RL begins.

## Problem

RL post-training samples tasks uniformly, but tasks differ sharply in what they contribute. Existing task-valuation methods score a task by a snapshot -- current pass rate or reward -- which measures how solvable it is now. Two tasks with the same low pass rate can still respond completely differently to continued optimization: some keep yielding positive reward response, others stay flat, saturate or regress. Nothing in the snapshot distinguishes them, so schedulers built on it leave that information untapped.

## Contributions

- Learnability distinguished from solvability and defined as a regime-conditional quantity: expected positive response to continued training under a fixed model family, initialization, algorithm, reward and budget
- Evidence that learnability reproduces across independently sampled training contexts and predicts downstream utility even among tasks with matched initial solvability
- TrajVal, a probe-based estimator usable before training starts, as a standalone prior or multiplied into an existing online scheduler

## Method

A diagnostic pool of 2,048 mathematical tasks is tracked across 20 GRPO epochs and each per-task reward trajectory is summarized by three descriptors -- total reward gain, standard deviation, and linear-fit R-squared -- yielding six coarse profiles: stable, sluggish and ineffective learners on one side, and already-mastered, stubbornly-unlearned and forgetting tasks on the other. Those profiles are a diagnostic lens rather than the definition. Oracle learnability needs a full multi-epoch pass over the pool, which cancels the efficiency it is meant to buy, so TrajVal applies two reductions. First, dense checkpoint tracking collapses to an endpoint pair: the mean reward over an early window and over a late window, and their difference. Second, full-pool training is replaced by a probe run on a small uniformly sampled subset -- 512 tasks, about 3 percent of the pool -- drawn from the same distribution, so the probe-trained model stands in for a later training state. The per-task score is a product of two terms, learning headroom (one minus the early reward) and directional alignment (the positive part of the improvement), so it favours tasks that are both still improvable and already showing constructive response; near-mastered tasks are penalized for having little residual value even when their short-term gain is positive. Scores become sampling weights through power compression with exponent 0.3 and a floor of 0.05, which keeps every task -- including near-zero-learnability ones -- at some minimum probability, a deliberate choice to preserve exposure to the full distribution. Combination with an online scheduler is multiplicative. Two domains: DAPO-Math and the logic subset of GURU, evaluated on six mathematics benchmarks and on held-out ordering puzzles and ARC-AGI, with Qwen3-1.7B and Qwen3-4B as the main models and Llama-3.2-3B as a cross-family check, all under Trinity-RFT with GRPO at 16 rollouts per prompt and results averaged over two seeds.

## Results

The reproducibility check is the load-bearing one: training independently on the full pool and on two 512-task probe sets sharing 256 tasks, the macroscopic profile distributions are nearly identical and the 256 shared tasks receive consistent individual assignments at Cohen's kappa 0.776 across six profiles and 0.879 under the binary learnable grouping, with the same pattern on Llama-3.2-3B. On predictive value, restricting training to the roughly 41 percent of tasks marked learnable reaches the full pool's converged accuracy of about 0.41 in 3.6x fewer steps, and an oracle soft prior beats random sampling at matched budget after both converge, 0.410 against 0.387. The probe substitution largely preserves the ordering that matters, with Spearman correlations against oracle values of 0.940 for the early endpoint and 0.876 for the late one. As a drop-in replacement for uniform sampling, TrajVal improves both peak accuracy and time-averaged AUC in all four domain-by-scale cells -- Qwen3-1.7B math 0.3967 to 0.4105, Qwen3-4B math 0.5060 to 0.5190, Qwen3-4B logic 0.2052 to 0.2260 -- and reaches the baseline peak in 40 percent of the steps on logic at 4B. Multiplied into BOTS and GRESO it improves best accuracy and AUC in every configuration and lowers steps-to-baseline in all of them. The controlled analysis is what separates the claim from solvability: partitioning each domain into three bins by initial pass rate and splitting each bin into high- and low-improvement halves with matched average pass rate, the high-improvement sub-pools uniformly beat the low ones on both metrics in all six bin-by-domain cells, most strongly in the low-pass-rate math bin at 0.434 against 0.338. Ablations show headroom and directional alignment are complementary -- all three single-dimension variants underperform the product -- and that the score ranking stabilizes early, reaching Spearman 0.85 against the final ranking by probe epoch 14 of 20.

## Limitations

The paper states three: the signal is validated only on mathematical and logical tasks with binary rewards, and whether it transfers to non-binary or model-graded rewards is open; evaluation is text-only; and compute limits confine experiments to smaller models, with larger scales left to future work. That last sentence says 'up to 8B parameters' while the models actually used are Qwen3-1.7B, Qwen3-4B and Llama-3.2-3B, so the stated ceiling is not the one exercised. A reader should add that all results are means over two seeds with no variance reported, and the standalone gains are 1.3 to 2.1 accuracy points -- real and consistent in direction across every cell, but small enough that two seeds is thin support for any individual number; the steps-to-baseline reductions are the more robust claim. Learnability is explicitly regime-conditional, so a prior estimated for one model family, algorithm and reward is not a property of the task, and the cross-regime reuse section reports transfer as useful but weaker than in-regime estimation. Finally, the probe reduction is verified by rank correlation against the oracle on one model and one pool, so the 0.940/0.876 figures are the evidence that the whole estimator rests on and they are measured once.

## Why it matters here

- **reasoning-evaluation**: A direct argument that a pass-rate snapshot is an incomplete measurement of what a benchmark item is worth, and the within-bin design is the kind of control this archive keeps asking for: current solvability is held fixed and only the response to training varies, so the effect cannot be explained by difficulty. That matters for how the archive reads difficulty-conditional results generally -- several entries here report a method helping most on hard problems, and 'hard' is always operationalized as a low pass rate, which this paper shows is two different quantities collapsed into one. It also supplies a measured distribution nobody here had: roughly 41 percent of a standard math RL pool is learnable under a fixed regime, and training on that subset alone matches the full pool in 3.6x fewer steps.

## Entities

- **Concepts**: task learnability, solvability, task value estimation, [training dynamics](../../../../wiki/concepts/training-dynamics.md), [data efficiency](../../../../wiki/concepts/data-efficiency.md), curriculum learning, [prompt difficulty](../../../../wiki/concepts/prompt-difficulty.md), reward trajectory, regime conditionality
- **Methods**: [GRPO](../../../../wiki/methods/grpo.md), probe-based estimation, task scheduling, importance weighting, [linear probe](../../../../wiki/methods/linear-probe.md)
- **Datasets**: [DAPO-Math-17K](../../../../wiki/datasets/dapo-math-17k.md), GURU, [ARC-AGI](../../../../wiki/datasets/arc-agi.md), BARC, [AIME 2024](../../../../wiki/datasets/aime-2024.md), [AIME 2025](../../../../wiki/datasets/aime-2025.md), [AMC23](../../../../wiki/datasets/amc23.md), [MATH500](../../../../wiki/datasets/math500.md), [Minerva](../../../../wiki/datasets/minerva.md), [OlympiadBench](../../../../wiki/datasets/olympiadbench.md)

Tags: `rl-post-training`, `data-selection`, `curriculum`, `task-valuation`, `training-dynamics`

## Abstract

Reinforcement learning (RL) has become a central post-training paradigm for eliciting reasoning capabilities in large language models, yet uniform task sampling allocates compute without regard to differences in how tasks respond to optimization. Existing task-valuation methods mostly rely on snapshot-based signals such as current pass rate or reward, which estimate how solvable a task is under the current policy. However, tasks with similar current solvability can still differ substantially in how positively they respond to further training. We study this residual axis as task learnability: a regime-conditional measure of expected positive response to continued training under a fixed RL post-training regime. By analyzing per-task reward trajectories, we find that learnability is reproducible across independently sampled training contexts and predictive of downstream utility. To make this signal practical before training begins, we propose TrajVal, a lightweight probe-based estimator that approximates per-task learnability from a short probe run and two endpoint evaluations. TrajVal can be used either as a standalone static prior for task sampling or as a multiplicative prior for existing online schedulers. Experiments on mathematical and logical reasoning benchmarks across multiple model scales show that TrajVal improves data efficiency over uniform sampling and provides complementary gains when combined with online scheduling methods.

---

Record id: `arxiv:2608.09217`
