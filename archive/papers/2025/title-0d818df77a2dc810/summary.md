<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving

- **Authors**: _unknown_
- **Venue**: ICLR 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2025/poster/29417>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

An empirical study of compute-optimal inference that measures accuracy against FLOPs for greedy decoding, sampling with majority and weighted voting, best-of-n and tree search across model sizes, and introduces REBASE, a reward-guided tree search.

## Problem

Training-time scaling laws for LLMs are well studied, but the inference side is not: given a fixed compute budget at test time, it is not established how to split it between model size and the number of tokens generated, nor which inference strategy is the best use of the marginal FLOP. The paper frames this as compute-optimal inference and asks which (model size, strategy, sample budget) triple sits on the accuracy-versus-FLOPs Pareto frontier.

## Contributions

- Frames compute-optimal inference as a Pareto problem over model size, inference strategy and sample budget, measured in FLOPs rather than sample count
- Shows empirically that sampling-based voting saturates exponentially to a limit fixed by the model's output distribution, so additional samples stop paying off
- Introduces REBASE, a process-reward-guided tree search that allocates node expansion width by a softmax over reward scores and needs no rollouts
- Reports that Llemma-7B with REBASE matches or exceeds Llemma-34B on MATH500 at roughly 2x fewer FLOPs, and beats 256-sample voting on MATH with about 7x less compute

## Method

The study fixes an inference compute budget in FLOPs and sweeps model size against generation strategy, plotting error rate against budget so that strategies are compared at equal cost rather than at equal sample count. Strategies covered are greedy decoding, repeated sampling with majority voting, best-of-n, weighted voting against a reward model, and tree search. The authors also propose REBASE (REward BAlanced SEarch), a tree search that uses a process reward model to decide how widely to expand each node instead of running MCTS rollouts: at each depth the total expansion budget is divided among the surviving nodes in proportion to a softmax over their reward scores at a balance temperature, so higher-scoring partial solutions get more children and low-scoring ones are pruned. Dropping rollouts is what makes it cheap enough to still produce enough complete candidates for a vote at the end.

## Results

Sampling-based voting improves with more samples but converges exponentially to a ceiling set by the model's own output distribution, so past a point extra samples buy nothing. REBASE dominates sampling at equal cost: on MATH with Mistral-7B it reaches 45.0% at 32 samples and 1.36e14 FLOPs, against 42.8% for sampling at 256 samples and 8.70e14 FLOPs - better accuracy for roughly 7x less compute. Across model sizes, Llemma-7B under REBASE matches Llemma-34B accuracy on MATH500 at about 2x fewer FLOPs, which is the paper's central claim that a smaller model with a better inference algorithm is Pareto-optimal against a larger model decoded simply. REBASE's advantage is concentrated on MATH difficulty levels 3 to 5 and is comparable to the alternatives on easy problems. Models spanned Pythia 410M to 12B, Mistral-7B, Llama3-8B, and the math-specialised Llemma-7B and Llemma-34B.

## Limitations

No limitations section is given in the material available. Observed constraints: the theoretical analysis assumes a finite vocabulary and bounded answer length; REBASE's quality is bounded by the process reward model that guides it, and the cost of running that reward model is part of the budget being measured; and the evaluation is mathematics plus one code benchmark, so the frontier reported may not transfer to domains where a step-level reward model is unavailable. The paper reports saturation of sampling-based methods but no inverse scaling - accuracy does not degrade as compute grows, it flattens - which is a narrower finding than 'more thinking hurts'.

## Why it matters here

- **overthinking**: This is the budget-side half of the topic. Where the length-control papers ask how many tokens one chain should be, this asks how a fixed test-time budget should be spent at all - more parameters, more samples, or a better search - and answers it in FLOPs, which is the unit that makes those choices comparable. Two results bear directly on overthinking. The saturation curve is the parallel-sampling analogue of a chain that keeps going after it has stopped learning anything: extra compute converges to a ceiling the model's distribution already fixed, which is a quantitative reason to stop rather than an intuition. And the difficulty split - REBASE's advantage concentrated on MATH levels 3 to 5 and flat on easy problems - is the same difficulty-conditioned pattern the adaptive-thinking papers exploit, arriving here from search rather than from RL. Worth noting the paper reports saturation, not inverse scaling: it does not show more compute making answers worse.

## Entities

- **Concepts**: [Test-Time Compute Scaling](../../../../wiki/concepts/test-time-compute-scaling.md), [Compute-Optimal Inference](../../../../wiki/concepts/compute-optimal-inference.md), Inference Scaling Laws, Process Reward Model, [Tree Search Decoding](../../../../wiki/concepts/tree-search-decoding.md), Majority Voting, Diminishing Returns, [Accuracy-Efficiency Tradeoff](../../../../wiki/concepts/accuracy-efficiency-tradeoff.md)
- **Methods**: REBASE (reward balanced search), majority voting / self-consistency, [best-of-n](../../../../wiki/methods/best-of-n.md), weighted voting, Monte Carlo Tree Search (comparison), [process reward model](../../../../wiki/methods/process-reward-model.md), greedy decoding
- **Datasets**: [MATH500](../../../../wiki/datasets/math500.md), [GSM8K](../../../../wiki/datasets/gsm8k.md), [MBPP](../../../../wiki/datasets/mbpp.md)

Tags: `test-time-compute`, `inference-scaling`, `compute-optimal`, `tree-search`, `process-reward-model`, `majority-voting`, `math-reasoning`, `diminishing-returns`

---

Record id: `title:0d818df77a2dc810`
