<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ReasoningGuard: Safeguarding Large Reasoning Models with Inference-time Safety Aha Moments

- **Authors**: Yuquan Wang, Mi Zhang, Yining Wang, Geng Hong, Mi Wen, Xiaoyu You, Min Yang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.1453/>
- **PDF**: <https://aclanthology.org/2026.acl-long.1453.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.1453
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

ReasoningGuard is a training-free, inference-time jailbreak defense for large reasoning models that uses an attention-sink signal to locate the moment reasoning shifts from problem restatement to exploration, injects a crafted 'safety aha' phrase there, then samples multiple continuations and selects the one with the highest sustained attention to that safety phrase -- outperforming nine existing defenses at only 5-9% extra inference cost.

## Problem

Large reasoning models exhibit 'superficial safety alignment': they can identify malicious intent in a prompt but still generate unsafe intermediate reasoning steps in the mid-to-late stages of their chain-of-thought, exposing sensitive content even when the final answer looks safe -- and existing defenses either require costly fine-tuning and expert-curated safety data, or are training-free but reduce effectiveness or trigger exaggerated safety (over-refusal on benign queries).

## Contributions

- identification of superficial safety alignment in LRMs, where malicious intent is correctly recognized but unsafe reasoning steps still occur in mid-to-late reasoning stages
- an attention-sink-based method for locating the reasoning-phase transition point at which to inject a safety-aware 'aha moment' phrase, validated against human-annotated transition points
- a scaling-sampling mechanism (Injection Attention Score) that selects among multiple post-injection continuations the one exhibiting sustained safety-oriented attention, at bounded extra token cost
- state-of-the-art or near-state-of-the-art jailbreak defense across 4 attack types and 2 benchmarks on 4+ model families, at only 5-9% inference overhead, while better preserving model utility than other training-free defenses and mitigating exaggerated safety

## Method

Models LRM reasoning as four stages (problem definition, blooming cycle, reconstruction cycle(s), final decision) and observes unsafe steps mainly emerge in the blooming/reconstruction stages. Stage 1 (Safety Injection): identifies the attention-sink token in the last transformer layer using a sliding-window average-attention score with a dynamic window size, treats this token (empirically shown to align with human-annotated semantic transition points) as marking the shift from problem restatement to reasoning expansion, and injects a three-part crafted 'safety aha phrase' (an aha-moment trigger, a safety-aware reminder, an explicit reflection guide) immediately after it. Stage 2 (Scaling Sampling): generates multiple candidate continuations via controlled top-k sampling after injection, scores each by Injection Attention Score (IAS) -- a temporally-weighted measure of how persistently later reasoning attends back to the injected safety phrase -- and selects the path with the highest IAS as the one to continue generating from, with a dynamic token budget bounded by the next attention-sink token.

## Results

Across DeepSeek-R1-Qwen-7B/14B/32B and DeepSeek-R1-Llama-8B against 2 harmfulness benchmarks (AdvBench, SorryBench) and 4 jailbreak attacks (GCG, PAIR, AutoRAN, Mousetrap), ReasoningGuard outperforms nine baseline defenses (4 training-based: SafeDecoding, RealSafe-R1, SAFEPATH-FT, SafeKey; 5 training-free: Paraphrase, Self-Reminder, SmoothLLM, ThinkingI, SAFEPATH-ZS) in most settings, e.g. on R1-Qwen-7B average Harmfulness/FFR across attacks of 0.3/4.6 versus 32.9/46.4 with no defense and versus the next-best training-free baseline's 0.8/10.1 (ThinkingI). It achieves the best model-utility preservation among training-free baselines (MMLU/GPQA/MATH500 average 67.5 on R1-Qwen-7B, comparable to training-based methods, versus substantial degradation from Paraphrase/SmoothLLM), and the best or near-best exaggerated-safety scores on XSTest (0.95/0.84 F1 for attention-aware injection vs. 0.89/0.81 for a rule-based intermediate-injection baseline). Inference overhead (ATGR) is only 1.05x (R1-Qwen-7B) to 1.09x (R1-Llama-8B), lower than most training-free baselines (SmoothLLM reaches 1.35-1.37x). Ablations confirm the attention-aware injection point outperforms rule-based (first-sentence or beginning-of-reasoning) injection at matched benchmarks, and that the method transfers to other model families (Phi-4-reasoning, QwQ-32B, Qwen3-4B-Thinking) without direct comparison to training-based methods due to their closed-source training data.

## Limitations

The strategies for attention-sink identification and reasoning-path selection are noted as having room for further optimization, and the paper calls for more interpretability-based analysis to fully uncover the safeguard's underlying mechanisms. The method is not evaluated on multi-modal large reasoning models, extension to which is left as future work, alongside improving reasoning efficiency and factual accuracy. High Injection Attention Score is empirically shown to be a sufficient but not necessary condition for safety (low-IAS paths span a broad range of harmfulness outcomes), meaning the selection criterion conservatively filters for safe paths rather than perfectly separating safe from unsafe ones.

## Why it matters here

- **overthinking**: Tangential to the topic's core efficiency/length concern -- this is a safety defense, not a length-reduction method -- but structurally relevant: it locates a reasoning-phase transition point via attention-sink signals (paralleling other archive papers' 'reasoning completion point' or 'safety trigger' detection methods) and quantifies its intervention's inference-time overhead (5-9% ATGR), giving a concrete data point for how much extra test-time compute an inference-time intervention on reasoning traces costs when it is not itself trying to shorten the trace.

## Entities

- **Concepts**: safety aha moment (inference-time injection), attention sink as a phase-transition signal, superficial safety alignment, Injection Attention Score (IAS)
- **Methods**: ReasoningGuard (attention-sink-triggered safety injection + IAS-based scaling sampling), SafeDecoding, RealSafe-R1, SAFEPATH-FT, SafeKey (training-based baselines), Paraphrase, Self-Reminder, SmoothLLM, ThinkingI, SAFEPATH-ZS (training-free baselines)
- **Datasets**: [AdvBench](../../../../wiki/datasets/advbench.md), SorryBench, [XSTest](../../../../wiki/datasets/xstest.md), [MMLU](../../../../wiki/datasets/mmlu.md), [GPQA Diamond](../../../../wiki/datasets/gpqa-diamond.md), [MATH500](../../../../wiki/datasets/math500.md)

Tags: `jailbreak-defense`, `large-reasoning-models`, `attention-sink`, `inference-time-safety`, `chain-of-thought`

## Abstract

Large Reasoning Models (LRMs) have demonstrated impressive performance in reasoning-intensive tasks, but they remain vulnerable to harmful content generation, particularly in the mid-to-late steps of their reasoning processes. Current defense methods, however, depend on costly fine-tuning and additional expert knowledge, which limits their scalability.In this work, we propose ReasoningGuard, an inference-time safeguard for LRMs.It injects timely safety aha moments during the reasoning process to guide the model towards harmless yet helpful reasoning.Our approach leverages the internal attention mechanisms of the LRM to accurately identify key points in the reasoning path, triggering safety-oriented reflections.To safeguard both the subsequent reasoning steps and the final answers, we implement a scaling sampling strategy during decoding to select the optimal reasoning path.With minimal additional inference cost, ReasoningGuard effectively mitigates four types of jailbreak attacks, including recent ones targeting the reasoning process of LRMs. Our approach outperforms nine existing safeguards, providing state-of-the-art defenses while avoiding common exaggerated safety issues.

---

Record id: `doi:10.18653/v1/2026.acl-long.1453`
