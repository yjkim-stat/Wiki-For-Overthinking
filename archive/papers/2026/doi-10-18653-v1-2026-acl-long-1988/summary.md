<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# AutoRAN: Automated Hijacking of Safety Reasoning in Large Reasoning Models

- **Authors**: Jiacheng Liang, Tanqiu Jiang, Yuhui Wang, Rongyi Zhu, Fenglong Ma, Ting Wang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.1988/>
- **PDF**: <https://aclanthology.org/2026.acl-long.1988.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.1988
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

AutoRAN is the first automated framework for hijacking a large reasoning model's internal safety deliberation, using a weaker, less-aligned auxiliary model to simulate the target's execution reasoning and iteratively refine attack prompts from leaked refusal reasoning, achieving near-100% attack success against gpt-o3/o4-mini and Gemini-2.5-Flash within a few turns.

## Problem

Large reasoning models expose their internal chain-of-thought for transparency and alignment purposes, but this transparency creates a new attack surface (leaked reasoning patterns can reveal how to bypass safety deliberation), and prior jailbreak methods against LRM reasoning rely on manually curated narratives or static, non-adaptive transformation rules, limiting their scalability against evolving safety alignments.

## Contributions

- AutoRAN, the first framework to automate hijacking of an LRM's internal safety reasoning via an iterative, feedback-driven loop rather than manually curated narratives or static transformation rules
- near-100% attack success rates against multiple state-of-the-art commercial LRMs (gpt-o3/o4-mini, Gemini-2.5-Flash) within a few turns, at substantially lower token cost and latency than a prior comparable attack (MouseTrap)
- mechanistic evidence that the attack works by shifting the target model's think-block token distribution away from safety deliberation and toward task execution, not merely via surface-level prompt engineering
- an evaluation of candidate defenses (adversarial-data RLHF, system-prompt-based safety instructions) showing meaningful but incomplete mitigation, with a documented generalization gap across narrative-template styles

## Method

Operates under a 'weak-to-strong' execution-simulation paradigm using a less-aligned auxiliary attacker model (Qwen3-8B-ablated) with only black-box query access to the target. Probes two attack surfaces: Execution Hijacking, where the attacker simulates the target's high-level execution-focused reasoning trace for the harmful request (without safety checking) and uses it to populate a narrative template (e.g. an 'educational framework' framing) that steers the target directly into task-completion mode; and Targeted Refinement, an iterative loop that inspects the target's response and (if provided) its exposed reasoning trace after each attempt -- classifying the outcome as immediate refusal (restart with a new template), refusal-with-reasoning (extract the specific safety concern from the leaked reasoning and append prompt content addressing/neutralizing it), or a substantive-but-insufficiently-helpful response (mutate the template to sharpen its harmful objective) -- continuing until a judge model scores the response's helpfulness above a threshold or a turn limit is reached.

## Results

AutoRAN achieves 100% Attack Success Rate against gpt-o3, gpt-o4-mini and Gemini-2.5-Flash across AdvBench, HarmBench and StrongReject within 10 turns (gpt-o3 succeeds in a single turn on nearly all queries), and also reaches 100% ASR on DeepSeek-R1 and Qwen3-8B. It consistently beats MouseTrap in attack success rate (especially on the harder HarmBench/StrongReject datasets) while using about 3x fewer victim-side tokens and 13-18x lower latency. Cross-judge validation (external judges gpt-4o, Gemini-2.5-Flash, LLaMA Guard, MouseTrap and H-CoT protocols) confirms the attacks are largely robust to judge strictness, though LLaMA Guard's conservative classification (62-96% unsafe) surfaces some discrepancies, particularly on HarmBench where AutoRAN's structured-outline outputs score lower under stricter judging. An ablation hiding the target's intermediate reasoning traces (disabling Targeted Refinement's Case 2) only slightly reduces ASR (e.g. GPT-o4-mini 100%->96% on AdvBench) and modestly raises the average query count needed, showing Execution Hijacking alone is largely sufficient while refusal-reasoning leakage mainly helps resolve harder cases faster. Mechanistic analysis shows the hijacking prompt produces a distributional shift in the target's think-block token likelihoods: safety-deliberation continuation tokens become significantly less likely (Delta approx -1.65 average log-likelihood at 48-token prefix) while task-execution continuation tokens become significantly more likely (Delta approx +2.85), consistent across prefix lengths 16-64, indicating the attack steers the model's reasoning trajectory at the distributional level rather than through surface prompt forcing. As a defense, using AutoRAN-generated attack-response pairs to fine-tune a reward model and apply RLHF reduces AutoRAN's ASR on Qwen3-8B from 100% to 8% with only a modest over-refusal increase (XSTest 9.2%->10.8%), but this defense generalizes poorly to unseen narrative-template styles (ASR rises to 86-92% on templates not seen during defense training), and a system-prompt-based defense reduces ASR but substantially increases over-refusal (e.g. Qwen3-8B XSTest over-refusal 10.8%->25.3%).

## Limitations

The RLHF-based defense the paper proposes generalizes poorly across narrative-template styles, with a large gap between seen-template robustness (ASR as low as 6-10%) and unseen-template robustness (ASR 86-92%), indicating current defenses capture superficial template correlations rather than the underlying vulnerability. System-prompt-based defenses reduce attack success but at a substantial cost to general helpfulness (increased over-refusal on benign queries). The paper explicitly frames the transparency-versus-security tension as an ongoing arms race and calls for new defenses that protect internal reasoning processes rather than only final outputs, implying no defense evaluated is considered a complete solution.

## Why it matters here

- **overthinking**: Not relevant to reasoning length or the accuracy/efficiency tradeoff: this is a jailbreak/safety attack paper. It is worth noting only as related work to a cited attack surface (Si et al., referenced here in passing, on adversarial inputs that induce excessive reasoning to inflate computational overhead) that is closer to the overthinking topic than AutoRAN's own contribution, which instead exploits reasoning-trace transparency to bypass safety deliberation.

## Entities

- **Concepts**: Execution Hijacking, Targeted Refinement (refusal-reasoning exploitation), weak-to-strong execution simulation, reasoning-trace attack surface
- **Methods**: AutoRAN (execution-simulation + iterative refinement jailbreak), MouseTrap (comparison baseline), H-CoT, PolicyPuppetry (referenced prior attacks), RLHF-based adversarial-data defense (Dr. GRPO), system-prompt-based safety defense
- **Datasets**: [AdvBench](../../../../wiki/datasets/advbench.md), [HarmBench](../../../../wiki/datasets/harmbench.md), [StrongReject](../../../../wiki/datasets/strongreject.md), XSTest (over-refusal evaluation)

Tags: `jailbreak`, `large-reasoning-models`, `safety`, `chain-of-thought`, `red-teaming`

## Abstract

This paper presents AutoRAN, the first framework to automate the hijacking of internal safety reasoning in large reasoning models (LRMs). At its core, AutoRAN pioneers an execution simulation paradigm that leverages a weaker but less-aligned model to simulate execution reasoning for initial hijacking attempts and iteratively refine attacks by exploiting reasoning patterns leaked through the target LRM’s refusals. This approach steers the target model to bypass its own safety guardrails and elaborate on harmful instructions. We evaluate AutoRAN against state-of-the-art LRMs, including GPT-o3/o4-mini and Gemini-2.5-Flash, across multiple benchmarks (AdvBench, HarmBench, and StrongReject). Results show that AutoRAN achieves approaching 100% success rate within one or few turns, effectively neutralizing reasoning-based defenses even when evaluated by robustly aligned external models. This work reveals that the transparency of the reasoning process itself creates a critical and exploitable attack surface, highlighting the urgent need for new defenses that protect models’ reasoning traces rather than merely their final outputs.

---

Record id: `doi:10.18653/v1/2026.acl-long.1988`
