<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Think Right: Learning to Mitigate Under-Over Thinking via Adaptive, Attentive Compression

- **Authors**: Joykirat Singh, Justin Chih-Yao Chen, Archiki Prasad, Elias Stengel-Eskin, Akshay Nambi, Mohit Bansal
- **Venue**: preprint
- **Published**: 2025-01-01
- **Source**: local
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

TRAAC is an online GRPO-based RL method that prunes a reasoning model's chain-of-thought using attention scores from the </think> token and calibrates how aggressively it prunes based on estimated problem difficulty, so it thinks less on easy problems and more on hard ones.

## Problem

Thinking models scale test-time compute via chain-of-thought, but they misallocate it: on hard problems they can stop too early (underthinking, causing errors), and on easy problems they keep generating unnecessary steps after already reaching a correct intermediate answer (overthinking, wasting tokens). The paper calls this failure to modulate response length with task difficulty 'under-adaptivity'. Prior work mostly attacks only the overthinking side (compressing or penalizing long traces) or treats adaptivity as a binary thinking/no-thinking choice, rather than deciding how much to think.

## Contributions

- TRAAC, an online GRPO post-training method that uses the model's own self-attention (from the </think> delimiter) to score and prune redundant reasoning steps without an external annotator model.
- A difficulty-adaptive compression scheme that estimates per-problem difficulty from rollout pass rate during training and modulates the pruning rate accordingly, addressing both overthinking and underthinking (unlike prior work that mainly targets overthinking or treats adaptivity as a binary thinking/no-thinking choice).
- A sigmoid-smoothed length reward that avoids the drastic accuracy collapse that a naive shorter-is-better reward causes, applied only to rollouts that reach a correct answer.
- Empirical results showing accuracy and efficiency gains together (not a tradeoff) over base models and RL baselines (TokenSkip, L1-Max, LC-R1, AdaptThink) on AIME, AMC, GPQA-D, BBEH, and OOD generalization to OptimalThinkingBench despite training only on math data.
- Ablations showing attention-based step scoring outperforms random and confidence-based pruning, and that difficulty calibration and attention-based compression are both necessary components.

## Method

TRAAC is a GRPO-based online RL post-training method with three pieces. (1) Difficulty estimation: at each training step the policy generates N=8 rollouts per question; the pass rate (fraction correct) buckets the problem into easy/medium/hard. (2) Attention-based compression: the full reasoning trajectory is split into steps at fixed control tokens (e.g. 'Wait', 'Alternatively', 'Hold on', 'Let me double-check', etc., 24 tokens listed in Appendix A.3.2). An auxiliary prompt ('Time is up. I should stop thinking and now write a summary containing all key steps required to solve the problem.') is appended, then the model computes, for each token, the attention it receives from the </think> delimiter, averaged over all layers and heads; a step's importance score is the mean token-level score over its tokens. Steps with the lowest importance scores are pruned to produce a compressed trajectory. The eviction fraction is itself scaled down when the score distribution across steps is close to uniform (an entropy-based 'uniformity score', Appendix A.3.3, avoids over-pruning when no step stands out), and capped at 80% eviction. (3) Difficulty-level calibration: harder problems get a lower compression rate (more steps kept, encouraging longer exploration), easier ones get a higher compression rate (default hyperparameters: hard 0.20, medium 0.40, easy 0.60). Rewards for GRPO combine a correctness reward (weight +4), a format reward (0-1, presence/order of <think>/</think>), and a length reward computed on the compressed trajectory: a sigmoid-smoothed penalty for length beyond the median of a sliding window (last 10 steps) of same-difficulty rollouts' lengths, which only applies when the rollout reached a correct final answer.

## Results

Trained on DAPO-Math-17k, evaluated with Qwen3-4B and DeepSeek-R1-Distill-Qwen-7B (temperature 1.0, max response length 10k at eval). On AIME/AMC/GPQA-D/BBEH averaged: TRAAC (Qwen3-4B) reaches 48.2% accuracy at 4.8k tokens vs. base model 39.8% at 7.6k tokens (+8.4 points accuracy, -36.8% length); vs. best baseline AdaptThink (40.3% acc, 6.8k tokens) TRAAC is +7.9 points accuracy and -29.4% length. On DeepSeek-Qwen-7B, TRAAC gets 43.8% vs. base model's 40.5% (+3.3 points) with a 13.4% length reduction. Individual per-task numbers (Table 1): AIME 45.45% (Qwen3-4B TRAAC) vs. base 27.64%; AMC 79.52% vs. 68.19%; GPQA-D 47.21% vs. 45.18%; BBEH 20.59% vs. 18.28%. On OptimalThinkingBench (OTB, F1 combining OverthinkingBench AUC_OAA and UnderthinkingBench accuracy), TRAAC improves F1 by 7.36 points on Qwen3-4B (55.41 vs. base 48.05) and 12.55 points on DeepSeek-Qwen-7B (34.15 vs. 21.60); UnderthinkingBench accuracy rises from 34.33% to 41.09% (Qwen3-4B) with average response length dropping ~40% across OOD tasks. Ablations (Table 3) show removing difficulty calibration (keeping compression) drops the AIME/AMC/GPQA-D/BBEH average by 3.4% and increases length by 23.8% relative to full TRAAC; removing attention-based compression too (down to base+CR+LR) costs a further F1 drop on OTB. Table 6 ablation: random-step pruning gives an 11% average accuracy drop vs. TRAAC's attention-based pruning, and least-confidence pruning gives a 7.25% drop, at comparable or worse length. A test-time-only variant (compression applied at inference with a fixed 0.4 rate, no RL training) still beats the base model (+3.11% accuracy, +12.65% efficiency) but the fully trained TRAAC beats this inference-only variant by 7.28% accuracy and 27.5% efficiency on AIME/GPQA-D.

## Limitations

The paper has no dedicated Limitations section; the following are what the reader should notice from the method and experiments. Difficulty estimation requires sampling N=8 full rollouts per training example to compute a pass rate, adding rollout compute during training beyond what the compressed-length gains save at inference. Training used only a math-specific dataset (DAPO-Math-17k) with a hard-coded threshold-based difficulty binning (easy/medium/hard cutoffs at pass rates, with fixed compression rates 0.60/0.40/0.20 chosen ad hoc rather than learned); OOD generalization gains (about 3% on Qwen3-4B, 2.8% on DeepSeek-Qwen-7B) are noticeably smaller than the in-domain math gains (8.4%). The method's step segmentation relies on a fixed, hand-authored list of 24 English discourse marker tokens (e.g. 'Wait', 'Alternatively'), which is a heuristic that may not transfer to other languages or reasoning styles. Evaluated only on two base models (Qwen3-4B, DeepSeek-R1-Distill-Qwen-7B) at the 4-7B scale, trained on 4xA100 GPUs; no results are given for larger models. The attention-based importance score requires appending an auxiliary 'time is up, summarize' prompt before scoring, an extra inference pass not needed by simpler baselines. Evaluation avoids LLM-as-judge and restricts OverthinkingBench to auto-verifiable (MCQ/numeric) items, which narrows the benchmark's original scope.

## Why it matters here

- **overthinking**: The paper is directly about the accuracy/efficiency tradeoff of reasoning length: it names and formalizes 'under-adaptivity' (both underthinking and overthinking) as the failure to match reasoning budget to problem difficulty, and proposes an RL method (TRAAC) that dynamically compresses or extends chain-of-thought based on estimated difficulty, evaluated explicitly on OverthinkingBench/UnderthinkingBench and OptimalThinkingBench alongside standard reasoning benchmarks.

## Entities

- **Concepts**: under-adaptivity (failure to modulate reasoning length with problem difficulty), attention-based step importance scoring from the </think> delimiter, difficulty-adaptive compression rate calibrated by rollout pass rate, uniformity-scaled eviction percentage, sigmoid-smoothed length reward
- **Methods**: [GRPO (Group Relative Policy Optimization)](../../../../wiki/methods/grpo-group-relative-policy-optimization.md), TRAAC (attention-based compression module), [TokenSkip](../../../../wiki/methods/tokenskip.md), L1-Max, [LC-R1](../../../../wiki/methods/lc-r1.md), [AdaptThink](../../../../wiki/methods/adaptthink.md)
- **Datasets**: [DAPO-Math-17k](../../../../wiki/datasets/dapo-math-17k.md), AIME (2022-2024), AMC (2022-2023), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md), BBEH (Big Bench Extra Hard), OptimalThinkingBench (OverthinkingBench, UnderthinkingBench), [SuperGPQA](../../../../wiki/datasets/supergpqa.md), [BBH (Big Bench Hard)](../../../../wiki/datasets/bbh-big-bench-hard.md)

Tags: `overthinking`, `underthinking`, `test-time compute`, `reinforcement learning`, `grpo`, `chain-of-thought compression`, `attention`, `adaptive reasoning`, `difficulty calibration`

## Abstract

Recent thinking models are capable of solving complex reasoning tasks by scaling test-time compute across various domains, but this scaling must be allocated in line with task difficulty. On one hand, short reasoning (underthinking) leads to errors on harder problems that require extended reasoning steps; but, excessively long reasoning (overthinking) can be token-inefficient, generating unnecessary steps even after reaching a correct intermediate solution. We refer to this as under-adaptivity, where the model fails to modulate its response length appropriately given problems of varying difficulty. To address under-adaptivity and strike a balance between under- and overthinking, we propose TRAAC (Think Right with Adaptive, Attentive Compression), an online post-training RL method that leverages the model's self-attention over a long reasoning trajectory to identify important steps and prune redundant ones. TRAAC also estimates difficulty and incorporates it into training rewards, thereby learning to allocate reasoning budget commensurate with example difficulty. Our approach improves accuracy, reduces reasoning steps, and enables adaptive thinking compared to base models and other RL baselines. Across a variety of tasks (AIME, AMC, GPQA-D, BBEH), TRAAC (Qwen3-4B) achieves an average absolute accuracy gain of 8.4% with a relative reduction in reasoning length of 36.8% compared to the base model, and a 7.9% accuracy gain paired with a 29.4% length drop compared to the best RL baseline. TRAAC also shows strong generalization: although our models are trained on math datasets, they show accuracy and efficiency gains on out-of-distribution non-math datasets like GPQA-D, BBEH, and OptimalThinkingBench. Our analysis further verifies that TRAAC provides fine-grained adjustments to thinking budget based on difficulty and that a combination of task-difficulty calibration and attention-based compression yields gains across diverse tasks.

---

Record id: `local:da3fbe3617acc5f8`
