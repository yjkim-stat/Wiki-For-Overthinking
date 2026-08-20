<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Don't Overthink It: A Survey of Efficient R1-style Large Reasoning Models

- **Authors**: Linan Yue, Yichao Du, Yizhi Wang, Weibo Gao, Fangzhou Yao, Li Wang, Ye Liu, Ziyu Xu, Qi Liu, Shimin Di, Min-Ling Zhang
- **Venue**: preprint
- **Published**: 2025-01-01
- **Source**: local
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

A survey that organizes methods for making R1-style large reasoning models reason efficiently (i.e., avoid overthinking) into two axes: single-model optimization and multi-model collaboration.

## Problem

R1-style large reasoning models (e.g., DeepSeek R1) trained with RL to produce long chain-of-thought and self-reflection frequently overthink: they generate unnecessarily long, redundant or repetitive reasoning chains even for simple inputs (e.g. '2+3'), and engage in low-confidence self-verification loops ('unconfident reasoning behavior'). This increases latency and computational cost and can degrade final-answer accuracy, and may also increase vulnerability to malicious attacks. Prior surveys covered training process, explicit/implicit CoT, and short-CoT/fast-decoding angles but did not systematically cover representation-engineering-based methods or model-collaboration approaches, which this survey adds.

## Contributions

- Proposes a taxonomy of efficient R1-style LRM reasoning organized along a single-model-optimization vs. model-collaboration axis, in contrast to prior surveys organized by training process or explicit/implicit CoT.
- Is the first survey (per the authors' Table 1 comparison) to cover both frontier representation-engineering (RepE) methods and frontier model-collaboration methods for efficient reasoning.
- Maintains a public GitHub repository tracking ongoing progress in efficient reasoning research.
- Outlines four future-application directions: efficient multimodal reasoning, efficient tool-integrated reasoning, efficient multi-agent systems, and truthful/trustworthy efficient reasoning.

## Method

The survey proposes a two-branch taxonomy. (1) Efficient Reasoning with Single Model: Early Exit (monitoring-based via confidence/entropy/budget/probe signals, generation-control-based via logit suppression of reflection trigger tokens like 'wait'/'alternatively', and adaptive early exit via RL such as S-GRPO with decaying position-based rewards); CoT Compression (token-, step/chunk-, and chain-level pruning or rewriting of reasoning traces, parallel best-of-N-style compression, and reward-based compression via RL, e.g. LC-R1 with a </think>-focused reward); Adaptive Reasoning (RL-based methods with or without an SFT warm-up phase that let the model learn when/how long to reason, e.g. DAST's Token Length Budget, Thinker's four-stage fast/slow pipeline; reasoning-mode switching via explicit control tokens or implicit signals; and length-reward-shaped methods such as LASER, HAPO, ALP, SelfBudgeter); and Representation Engineering (extracting a steering vector from the difference between long-CoT and short-CoT model activations and injecting it into hidden states at inference to control reasoning depth/length, e.g. SEAL, Pre-allocated Direction Vectors, Thinking Progress Vector, Manifold Steering). (2) Efficient Reasoning with Model Collaboration: Long-Short Model Collaboration (short-to-long, long-to-short, and interactive setups pairing a lightweight short-CoT model with a long-CoT model, e.g. SplitReason, ThoughtMani, CoThink, PLAN-AND-BUDGET, COPE, ThinkSwitcher); LLM Routing (single-step routing such as RouteLLM, GraphRouter, IRT-Router, TagRouter, and multi-step routing such as R2-Reasoner, Router-R1, R2R, Route-To-Reason); Model Consolidation (distillation of a large teacher's reasoning into a smaller student, e.g. TwT, LiteCoT/DAR, DRP; and merging long-CoT and short-CoT model parameters, e.g. Average/TIES/DARE merging, Ada-R1, ReCUT); and Speculative Decoding (a small model drafts candidate reasoning steps/tokens verified in parallel by the large model, e.g. RSD, SpecRouter, SpecReason, Speculative Thinking, SCoT).

## Results

As a survey, the paper does not run its own experiments and reports no headline benchmark numbers of its own. It cites results from surveyed works, e.g. that model-merging strategies (Wu et al., 2025c) can reduce average inference length by up to 55% while preserving output quality. Most of the paper's substance is the taxonomy itself (summarized in Figure 1/Figure 2 and Table 1, which compares this survey's coverage of overthinking, representation-engineering, and model-collaboration methods against six prior surveys) rather than a quantitative evaluation.

## Limitations

The paper does not itself state formal limitations, but as a taxonomy-only survey it reports no new experiments, benchmarks, or quantitative comparisons among the surveyed methods, and it relies on the accuracy of each cited paper's own reported numbers rather than independent verification. In its Future Applications section (Section 5) the authors themselves note open gaps: a lack of systematic evaluation of whether single-model-text efficient-reasoning methods transfer to multimodal reasoning; existing tool-integrated-reasoning (TIR) methods still overinvoke external tools and this is exacerbated by noisy retrieved documents in RAG settings; efficient multi-agent reasoning coordination is underexplored; and efficient reasoning methods (e.g. CoT compression) may inadvertently amplify safety/hallucination risks already present in LRMs, an efficiency-trustworthiness tradeoff the field has not yet evaluated.

## Why it matters here

- **overthinking**: The entire survey is organized around the overthinking problem in R1-style large reasoning models (Section 2.2 defines it explicitly as generating unnecessarily long, redundant reasoning that increases cost and can degrade accuracy) and surveys the full landscape of methods proposed to counter it, from early exit and CoT compression to adaptive reasoning-length control and model routing.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), chain-of-thought compression, early exit, adaptive reasoning, representation engineering for reasoning control, long-short model collaboration, LLM routing, model consolidation (distillation and merging), speculative decoding for reasoning
- **Methods**: DEER, CONCISE, NOWAIT, TIP, S-GRPO, [TokenSkip](../../../../wiki/methods/tokenskip.md), Reasoning Path Compression (RPC), Adaptive GoGI-Skip, PIR, SPIRIT, Prune-on-Logic, A*-Thought, LS-Mixture SFT, AutoL2S, [LC-R1](../../../../wiki/methods/lc-r1.md), DAST, Thinker, LHRMs, Ada-R1, AdaCtrl, Thinkless, LASER, HAPO, SelfBudgeter, Adaptive Length Penalty (ALP), SEAL, [Manifold Steering](../../../../wiki/methods/manifold-steering.md), SplitReason, ThoughtMani, CoThink, [PLAN-AND-BUDGET](../../../../wiki/methods/plan-and-budget.md), [VeriThinker](../../../../wiki/methods/verithinker.md), FoReaL-Decoding, COPE, ThinkSwitcher, RouteLLM, GraphRouter, IRT-Router, TagRouter, R2-Reasoner, Router-R1, R2R, Route-To-Reason (RTR), TwT, DAR / LiteCoT, DRP, ReCUT, Reward-Guided Speculative Decoding (RSD), SpecRouter, SpecReason, Speculative Thinking, SCoT
- **Datasets**: _none recorded_

Tags: `overthinking`, `efficient reasoning`, `large reasoning models`, `chain-of-thought`, `test-time compute`, `survey`, `model routing`, `speculative decoding`, `representation engineering`

## Abstract

Recently, Large Reasoning Models (LRMs) have gradually become a research hotspot due to their outstanding performance in handling complex tasks. Among them, DeepSeek R1 has garnered significant attention for its exceptional performance and open-source nature, driving advancements in the research of R1-style LRMs. Unlike traditional Large Language Models (LLMs), these models enhance logical deduction and decision-making capabilities during reasoning by incorporating mechanisms such as long chain-of-thought and self-reflection through reinforcement learning. However, with the widespread application of these models, the problem of overthinking has gradually emerged. Specifically, when generating answers, these models often construct excessively long reasoning chains with redundant or repetitive steps, which leads to reduced reasoning efficiency and may affect the accuracy of the final answer. To this end, various efficient reasoning methods have been proposed, aiming to reduce the length of reasoning paths without compromising model performance and reasoning capability. By reviewing the current research advancements in the field of efficient reasoning methods systematically, we categorize existing works into two main directions based on the lens of single-model optimization versus model collaboration: (1) Efficient Reasoning with Single Model, which focuses on improving the reasoning efficiency of individual models; and (2) Efficient Reasoning with Model Collaboration, which explores optimizing reasoning paths through collaboration among multiple models. Besides, we maintain a public GitHub repository that tracks the latest progress in efficient reasoning methods. We hope this survey not only consolidates recent advances but also introduces a novel organizational framework for understanding efficient reasoning, framing it through the lens of single-model optimization versus model collaboration.

---

Record id: `local:6c80b6fd388d671e`
