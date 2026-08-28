<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Optimizing Length Compression in Large Reasoning Models

- **Authors**: Zhengxiang Cheng, Dongping Chen, Mingyang Fu, Tianyi Zhou
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.146/>
- **PDF**: <https://aclanthology.org/2026.acl-long.146.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.146
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Names 'invalid thinking' -- redundant double-checking after a reasoning model has already derived the correct answer -- as a specific, measurable form of overthinking (Valid Thinking rate as low as 57.5-65.3% on four SOTA LRMs), and introduces LC-R1, a GRPO method with a dual Length Reward (global conciseness) and Compress Reward (targeted removal of the redundant tail), achieving ~46-52% length reduction for only 1.8-2.1% accuracy loss and 97%+ Valid Thinking rate.

## Problem

Existing length-compression methods for large reasoning models treat the reasoning process as a black box and penalize length globally, without analyzing the internal structure of the thinking process itself, so they cannot specifically target the part of a reasoning trace that is redundant (verification after the answer is already found) versus the part that is necessary.

## Contributions

- identification and quantification of 'invalid thinking' as a specific structural form of overthinking (double-checking after the correct answer is already derived), measured via a new Valid Thinking rate metric and an automated extractor
- two fine-grained principles, Brevity and Sufficiency, refining the general efficacy/efficiency framing of prior compression work
- LC-R1, a GRPO method with a dual Length Reward (global conciseness, group-normalized by difficulty) and Compress Reward (targeted, applied only to the termination token) that achieves a markedly more favorable Pareto trade-off than SFT, DPO, O1-Pruner, ThinkPrune and their combination
- evidence via Pass@k and per-problem analysis that the compression is difficulty-agnostic and does not degrade exploration capability, i.e. it removes genuinely redundant tokens rather than compressing indiscriminately

## Method

Defines Valid Thinking (VT) rate = tokens from the start of thinking to the first occurrence of the correct answer, divided by total thinking tokens, using a lightweight fine-tuned extractor (LC-Extractor, built on Qwen2.5-3B-Instruct) to automatically locate that first-correct-answer point. Introduces two complementary principles: Brevity (terminate reasoning once the answer is found) and Sufficiency (never omit steps needed to reach a correct answer), operationalized in LC-R1, a GRPO-based post-training method with a dual reward: a Length Reward that gives a relative, group-normalized bonus for shorter compressed sequences among correct rollouts (adapting automatically to problem difficulty via the group-based sampling), and a Compress Reward applied specifically to the model's own </think> token, rewarding termination as soon as the correct answer appears within the compressed sequence and penalizing (-1) premature termination before the answer is found. Loss is computed over compressed trajectories (extracted from the original rollouts by LC-Extractor) rather than the raw ones, with token-level advantages combining both rewards.

## Results

On DeepSeek-R1-Distill-Qwen-7B across 7 benchmarks (AIME25, MATH500, GSM8K, OlympiadBench, AMC, GPQA-Diamond, LiveCodeBench), LC-R1 achieves a 46.32% average length reduction with only a 1.84% accuracy drop and a 97.14% Valid Thinking rate -- versus SFT (95.64% VT but -4.46% accuracy, less compression), DPO (96.34% VT, -5.26% accuracy), O1-Pruner (69.30% VT, -2.79% accuracy, only 33.71% compression), ThinkPrune (77.16% VT, +1.58% accuracy but only 14.13% compression), and SFT+O1-Pruner (85.22% VT, -4.31% accuracy). On the 1.5B model, LC-R1 reaches 51.86% length reduction at -2.14% accuracy with 98.64% VT, again the best Pareto trade-off among all baselines. Baseline VT rates on four current SOTA LRMs (Qwen3-32B, QwQ-32B, DeepSeek-R1, Llama-3.3-Nemotron-Super-49B) average 57.5-65.3% across five math benchmarks, indicating 35-45% of computational effort is typically spent on redundant post-answer verification. Ablations show the Length Reward alone yields significant compression but lower VT (93.16%/95.16%), the Compress Reward alone yields high VT but less compression (72.24%/71.10%), and only the combination achieves both simultaneously; a reward-weight sensitivity analysis finds the method more sensitive to the Compress Reward weight (gamma) than the Length Reward weight (alpha). Pass@k analysis on AIME25 (k=1 to 128) shows LC-R1's compressed model nearly overlaps the original model's Pass@k curve, and per-problem analysis shows a consistent compression ratio across the full difficulty spectrum -- evidence that compression removes truly redundant tokens without harming exploration capability or core problem-solving logic, and generalizes across problem difficulty.

## Limitations

Compressed reasoning may still suppress useful verification on genuinely difficult problems, leading to concise but incorrect answers in some cases. Validation is restricted to models up to 7B scale due to computational constraints, so results at larger scale are not directly demonstrated. The paper recommends that in high-stakes settings, such compression methods should be paired with task-appropriate validation and human oversight rather than deployed unchecked.

## Why it matters here

- **overthinking**: Central to the topic: gives 'overthinking' a specific, measurable structural definition (post-answer redundant double-checking, quantified as Valid Thinking rate, which sits at only 57.5-65.3% across four current SOTA reasoning models) rather than treating length alone as the target, and its dual-reward design directly operationalizes the Brevity/Sufficiency distinction that much of the archive's length-control literature gestures at informally. Its 46-52% length reduction at ~2% accuracy cost, validated via Pass@k as not harming exploration capability, is among the stronger efficiency results in the archive.

## Entities

- **Concepts**: invalid thinking (post-answer redundant verification), Valid Thinking (VT) rate, Brevity and Sufficiency principles, dual-reward GRPO (Length Reward + Compress Reward)
- **Methods**: LC-R1 (dual-reward GRPO), LC-Extractor (valid-thinking segment extraction), SFT (baseline), DPO (baseline), [O1-Pruner (baseline)](../../../../wiki/methods/o1-pruner-baseline.md), ThinkPrune (baseline), SFT+O1-Pruner (baseline)
- **Datasets**: [AIME25](../../../../wiki/datasets/aime-2025.md), [MATH500](../../../../wiki/datasets/math500.md), [GSM8K](../../../../wiki/datasets/gsm8k.md), [OlympiadBench](../../../../wiki/datasets/olympiadbench.md), [AMC](../../../../wiki/datasets/amc.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md), [LiveCodeBench](../../../../wiki/datasets/livecodebench.md), MATH (training)

Tags: `overthinking`, `invalid-thinking`, `efficient-reasoning`, `GRPO`, `length-compression`

## Abstract

Large Reasoning Models (LRMs) have achieved remarkable success, yet they often suffer from producing unnecessary and verbose reasoning chains. We identify a core aspect of this issue as ”invalid thinking”— models tend to repeatedly double-check their work after having derived the correct answer. To address this specific inefficiency, we move beyond the general principles of Efficacy and Efficiency to propose two new, fine-grained principles: Brevity, which advocates for eliminating redundancy, and Sufficiency, which ensures critical reasoning steps are preserved. Guided by these principles, we introduce LC-R1, a post-training method based on Group Relative Policy Optimization (GRPO). LC-R1 employs a novel combination of a Length Reward for overall conciseness and a Compress Reward that is specifically designed to remove the invalid portion of the thinking process. Extensive experiments on multiple reasoning benchmarks demonstrate that LC-R1 achieves a significant reduction in sequence length (5̃0%) with only a marginal (2̃%) drop in accuracy, achieving a favorable trade-off point on the Pareto frontier that prioritizes high compression. Our analysis further validates the robustness of LC-R1 and provides valuable insights for developing more powerful yet computationally efficient LRMs.

---

Record id: `doi:10.18653/v1/2026.acl-long.146`
