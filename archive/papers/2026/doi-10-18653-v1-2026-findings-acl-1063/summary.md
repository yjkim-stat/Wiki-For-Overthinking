<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning

- **Authors**: Zheng Li, Qingxiu Dong, Jingyuan Ma, Di Zhang, Kai Jia, Zhifang Sui
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1063/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1063.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1063
- **Topics**: overthinking
- **Relevance score**: overthinking 0.62

## In one line

SelfBudgeter trains a reasoning model to emit its own predicted token budget before answering (<budget>N</budget><solution>...</solution>) via a cold-start plus budget-guided GRPO pipeline, cutting response length ~61% on math benchmarks while preserving or improving accuracy, and letting users see the estimated wait time or pre-fill a hard budget upfront.

## Problem

Reasoning models consume excessive tokens even on simple queries (overthinking), and existing mitigations either lack precise length control (prompt-based instructions), fail to reliably satisfy user-specified length constraints (SFT/length-penalty RL), or add computational overhead (router-based architectures) -- none let the model both autonomously estimate an appropriate token budget for unconstrained queries and strictly adhere to it.

## Contributions

- SelfBudgeter, an output format and training framework where a reasoning model explicitly predicts its own token budget before generating an answer, letting users see the estimated wait time or pre-fill a hard budget
- the Precise Budget Control (PreB) Reward, tightening cosine-style length shaping with a tightness coefficient so response length converges to the minimally-sufficient length for correct answers while incentivizing longer analysis for incorrect ones
- a dynamic alpha schedule that prevents a specific reward-hacking failure mode (the model inflating its predicted budget to trivially match an already-long actual output) that a fixed tolerance allows
- empirical results showing ~61% average length compression on math benchmarks with preserved/improved accuracy at both 1.5B and 7B scale, and generalization to out-of-domain knowledge benchmarks (GPQA, SCoRE)

## Method

Reformats output as <budget>an integer</budget><solution>response</solution>, so the model predicts its own token budget before generating an answer (or, if the user supplies a limit, that value pre-fills the budget field). Training has three stages: (1) data preprocessing computes each training question's maximum acceptable budget b_max -- the model's own response length if it answered correctly, or infinity if it answered incorrectly (so wrong answers don't constrain future budget learning); (2) a cold-start SFT phase teaches the new output format using the model's own correct responses (to avoid reinforcing wrong answers) from GSM8K/MATH/s1k-1.1; (3) budget-guided GRPO reinforcement learning combines a Format Penalty, a Budget Penalty (penalizing predicted budgets that exceed b_max), and a Precise Budget Control (PreB) Reward -- inspired by, but tighter than, cosine-reward length shaping -- which uses a tightness coefficient alpha to align actual response length with the self-predicted budget, peaking at a minimally-sufficient length for correct answers and rewarding longer chains for incorrect ones (to encourage deeper analysis when the model is wrong). A dynamic alpha schedule (linearly tightening from 6.0 to 0.1 over training) avoids reward hacking, where a fixed loose alpha lets the model inflate its predicted budget to trivially match its own actual (still-long) output.

## Results

SelfBudgeter achieves an average response length compression of 61% on math reasoning tasks while maintaining accuracy. At 1.5B scale (built on DeepSeek-R1-Distill-Qwen-1.5B), SelfBudgeter-1.5B reaches 84.10% accuracy on GSM8K (vs. base model's 73.09%, an 11.01-point gain) while compressing response length to 43% of the original (1231.79 vs. 2865.08 tokens); on MATH500 it gains 3.54 accuracy points at 44% length; on AIME2025 it compresses to 30% of original length (4288.10 vs. 14444.03 tokens) while maintaining comparable accuracy (21.11% vs. 22.22%). Compared against L1 (explicit prompt-templated length limits) and E1 (hard truncation), SelfBudgeter achieves the best-or-second-best accuracy across all three benchmarks while L1 collapses on the hard AIME2025 benchmark and E1 degrades accuracy on the simpler GSM8K/MATH500 sets -- i.e. autonomous budget estimation beats both hard truncation and explicit prompted limits on the accuracy/length tradeoff. At 7B scale (built on DeepSeek-R1-Distill-Qwen-7B), SelfBudgeter-7B achieves the highest accuracy on MATH500 (86.87%) and AIME2025 (30.00%, best among all compared models including specialized RL baselines Eurus-2-7B-PRIME and Qwen-2.5-7B-Simple-RL), second-best on GSM8K (90.30%, only 0.68 points below the top baseline), at an average 48% compression ratio. An ablation shows all three reward components are necessary and complementary: format-only training collapses accuracy (1.64% on GSM8K) despite short outputs; adding correctness restores accuracy but compression becomes inconsistent on harder datasets (5327 tokens on MATH500); adding PreB improves budget adherence but harms accuracy on easier tasks; adding budget penalty gives good compression on easy tasks but sacrifices harder-task performance; only the full combination (SelfBudgeter) gives high accuracy with strong, stable compression across difficulty levels. Linear alpha scheduling outperforms fixed and cosine scheduling, maintaining accuracy while still achieving >61% compression (fixed/cosine over-compress and lose accuracy on harder problems). On out-of-domain general-knowledge benchmarks (GPQA, SCoRE), SelfBudgeter-1.5B substantially reduces reasoning length on both while remaining competitive in accuracy (best accuracy among compared methods on SCoRE, 16.26%), showing the approach transfers beyond mathematical reasoning.

## Limitations

The paper notes only general limitations: the methodology, though theoretically sound, may face practical challenges in more complex or diverse real-world scenarios beyond the tested benchmarks, and unspecified external factors beyond the paper's scope could affect generalizability of the results. No quantitative discussion of failure cases or specific domains where budget estimation breaks down is given.

## Why it matters here

- **overthinking**: Directly and centrally relevant: it names overthinking explicitly and contributes a self-estimated-budget mechanism that both mitigates it (61% average compression with preserved accuracy) and makes it legible to the user upfront (an anticipated wait time before generation begins) -- a distinct design point from methods elsewhere in this archive that either impose a fixed external budget, use post-hoc early exit, or intervene only at a single decision token, and its documented reward-hacking failure mode (budget inflation under a loose tolerance) is a specific, transferable caution for any length-shaping reward design.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), self-estimated token budget, budget-guided GRPO, Precise Budget Control (PreB) Reward, reward hacking via loose length tolerance, dynamic alpha schedule
- **Methods**: [GRPO (Group Relative Policy Optimization)](../../../../wiki/methods/grpo.md), budget-guided GRPO with PreB Reward, cold-start SFT, L1 (baseline, prompt-templated length limit), E1-Math (baseline, hard-truncation length control)
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH500](../../../../wiki/datasets/math500.md), [AIME2025](../../../../wiki/datasets/aime-2025.md), [s1k-1.1](../../../../wiki/datasets/s1k-1-1.md), STILL-3-Preview-RL-Data, [GPQA](../../../../wiki/datasets/gpqa.md), SCoRE

Tags: `overthinking`, `token-budget`, `reinforcement-learning`, `GRPO`, `length-control`, `adaptive-reasoning`

## Abstract

Recently, large reasoning models demonstrate exceptional performance on various tasks. However, reasoning models always consume excessive tokens even for simple queries, leading to resource waste and prolonged user latency. To address this challenge, we propose SelfBudgeter - a self-adaptive reasoning strategy for efficient and controllable reasoning. Specifically, we first train the model to self-estimate the required reasoning budget based on the query. We then introduce budget-guided GRPO for reinforcement learning, which effectively maintains accuracy while reducing output length. Experimental results demonstrate that SelfBudgeter dynamically allocates budgets according to problem complexity, achieving an average response length compression of 61% on math reasoning tasks while maintaining accuracy. Furthermore, SelfBudgeter allows users to see how long generation will take and decide whether to continue or stop. Additionally, users can directly control the reasoning length by setting token budgets upfront.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1063`
