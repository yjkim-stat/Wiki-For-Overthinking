<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Correct, Concise and Complete: Multi-stage Training For Adaptive Reasoning

- **Authors**: Nathanaël Carraz Rakotonirina, Ren Pang, Neha Anna John, Michael Bohlke-Schneider, Momchil Hardalov
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.622/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.622.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.622
- **Topics**: overthinking
- **Relevance score**: overthinking 0.67

## In one line

A multi-stage training framework (SFT via rejection sampling or trace reformatting, then RL with a reward that penalizes tokens generated after the first correct answer) reduces reasoning-trace length by 28% (Qwen3-8B) to 40% (Qwen3-32B) with only 1.6-2.5 accuracy-point drops, beating prior efficient-reasoning baselines on the Overthinking-Adjusted Accuracy (OAA) AUC metric.

## Problem

Reasoning traces from LLMs trained with RL for verifiable rewards often become unnecessarily long and repetitive -- 'overthinking' -- yielding no accuracy gain and sometimes degrading it; existing mitigations impose a fixed, manually-set thinking budget (hard truncation or a fixed-threshold length penalty) that cannot adapt per-input.

## Contributions

- a multi-stage efficient-reasoning framework combining SFT (via rejection sampling or trace reformatting) with RL using an input-adaptive length penalty tied to the position of the first correct answer in the trace
- a reward design that penalizes only post-answer redundancy rather than truncating or pruning the trace at a fixed token/sentence threshold, preserving legitimate self-correction
- empirical demonstration of 28-40% response-length reduction with 1.6-2.5 point accuracy drops, and a 2.5-point AUC_OAA improvement over the strongest of six compared efficient-reasoning baselines, with length reduction generalizing to domains outside the math-only training data

## Method

Two SFT variants warm-start the model toward concise traces: Adaptive-Answer uses rejection sampling (8 continuations per problem, keep the shortest correct one); Format-Adaptive-Answer reformats traces to drop the post-reasoning summary, keeping only direct reasoning-to-answer. Both are then further trained with GRPO-based RL using a length-penalty reward: R_L(y) = (L(y) - L(y_first))/L(y) if the answer is correct (0 otherwise), where y_first is the trace prefix up to the first correct answer -- i.e. the penalty is the fraction of tokens generated *after* the model has already produced the correct answer, discouraging redundant self-verification while still allowing self-correction (no penalty if the model corrects an initially wrong answer later). Evaluated with the Overthinking-Adjusted Accuracy AUC (AUC_OAA; Aggarwal et al. 2025), which integrates accuracy-at-token-budget over token thresholds rather than reporting a single accuracy/length point, on Qwen3 (1.7B/8B/32B) and DeepSeek-R1-Qwen-7B-Distill across seven benchmarks (MATH-500, AIME 24/25, GPQA Diamond, CommonsenseQA, LiveCodeBench, LongBenchv2) despite training only on math data (DeepScaleR, 13K problems).

## Results

On Qwen3-8B, Adaptive-Answer shortens responses by 28% and Format-Adaptive-Answer by 33% with about a 1-point average accuracy drop; the reduction scales with model size (22% at 1.7B, 23% at 8B, 40% at 32B). On the AUC_OAA metric (Table 1), Format-Adaptive-Answer scores 76.6 -- 5.0 points above the base model and 2.5 points above the strongest baseline among six compared efficient-reasoning methods (No-Thinking, First-Answer-Truncation, plain SFT, Hard-Length variants, Soft-Length, Normalized-Length, TWYN). Length reductions generalize to non-math domains the model was never trained on: GPQA Diamond/AIME24/AIME25 responses shrink ~25-32% and CommonsenseQA ~30-45%, while LiveCodeBench and LongBenchv2 show smaller reductions (8-14%) with under 2 points of accuracy loss -- the paper reads this as evidence that reduced redundant self-verification is a domain-agnostic property rather than a math-specific artifact. An ablation shows RL-without-SFT achieves the second-shortest traces but a lower AUC_OAA than the full pipeline, so SFT warm-starting is necessary for the RL stage's benefit, not merely a length-reduction shortcut on its own. Distribution analysis shows incorrect answers systematically have longer traces than correct ones across the base model and all methods, and the trained models shift the length distribution toward shorter traces for both correct and incorrect outputs (not just successful cases) -- interpreted as broadly reduced redundant self-verification rather than answer-dependent trimming. A worked AIME 24 example shows the base model performs seven redundant self-verifications after reaching the correct answer, Adaptive-Answer performs two, and Format-Adaptive-Answer performs none.

## Limitations

The training dataset is drawn exclusively from math problems (DeepScaleR, sourced from AIME 1983-2023, AMC, Omni-Math, STILL), so results on non-math tasks are an out-of-domain transfer test rather than a validated general capability; the paper itself flags that LiveCodeBench is the one dataset where the unmodified base model outperforms all efficient-reasoning methods including its own, suggesting fine-tuning exclusively on short math problems can hurt long-context/code tasks. AUC_OAA does not always align with raw accuracy-length tradeoffs, particularly for smaller models, so efficiency gains can come at a subtle cost the headline metric does not fully capture (noted for the fine-tuned DeepSeek-R1-7B, which dominates the base model in absolute accuracy but scores a slightly lower AUC_OAA). Intermediate-correct-answer counting as a self-verification proxy is described by the authors as a coarse metric since answers may be repeated or paraphrased.

## Why it matters here

- **overthinking**: Core paper for this topic: names 'overthinking' explicitly, adopts the Overthinking-Adjusted Accuracy metric from Aggarwal et al. as its primary evaluation, and proposes a length-penalty design specifically targeted at *post-answer* redundant self-verification rather than blunt length truncation -- directly extending the archive's existing thread on how to penalize wasted reasoning without damaging legitimate self-correction. Its finding that incorrect answers systematically have longer traces than correct ones, and that its trained models shift length distributions for both correct and incorrect outputs, is direct supporting evidence for the trace-length/accuracy relationship this archive's own findings already track.

## Entities

- **Concepts**: Overthinking-Adjusted Accuracy (OAA) / AUC_OAA, adaptive length penalty (tokens-after-first-correct-answer), rejection sampling for concise SFT, trace reformatting
- **Methods**: Adaptive-Answer (rejection-sampling SFT + RL length penalty), Format-Adaptive-Answer (trace-reformatting SFT + RL length penalty), [GRPO](../../../../wiki/methods/grpo.md), [No-Thinking (baseline)](../../../../wiki/methods/nothinking-baseline.md), First-Answer-Truncation (baseline), Hard-Length / Soft-Length / Normalized-Length penalties (baselines), TWYN (Think When You Need, baseline)
- **Datasets**: [MATH-500](../../../../wiki/datasets/math500.md), [AIME 24](../../../../wiki/datasets/aime-2024.md), [AIME 25](../../../../wiki/datasets/aime-2025.md), [GPQA Diamond](../../../../wiki/datasets/gpqa-diamond.md), [CommonsenseQA](../../../../wiki/datasets/commonsenseqa.md), [LiveCodeBench (v6)](../../../../wiki/datasets/livecodebench-v6.md), LongBenchv2, DeepScaleR (training data, 13K problems)

Tags: `overthinking`, `efficient-reasoning`, `length-penalty`, `reinforcement-learning`, `AUC_OAA`

## Abstract

The reasoning capabilities of large language models (LLMs) have improved substantially through increased test-time computation, typically in the form of intermediate tokens known as chain-of-thought (CoT). However, CoT often becomes unnecessarily long, increasing computation costs without improving accuracy and sometimes even degrading performance, a phenomenon known as “overthinking”. We propose a multi-stage efficient reasoning method that combines supervised fine-tuning—via rejection sampling or reasoning trace reformatting—with reinforcement learning using an adaptive length penalty. We introduce a lightweight reward function that penalizes tokens generated after the first correct answer, encouraging the model to perform self-verification only when beneficial. We conduct a holistic evaluation across seven diverse reasoning tasks, analyzing the accuracy–response length trade-off. Our approach reduces response length by an average of 28% for 8B models and 40% for 32B models, while incurring only minor performance drops of 1.6 and 2.5 points, respectively. Despite its conceptual simplicity, it achieves a better trade-off than more complex state-of-the-art efficient reasoning methods, scoring 76.6 on the area under the Overthinking-Adjusted Accuracy curve (AUCOAA)—5 points above the base model and 2.5 points above the second-best approach.

---

Record id: `doi:10.18653/v1/2026.findings-acl.622`
