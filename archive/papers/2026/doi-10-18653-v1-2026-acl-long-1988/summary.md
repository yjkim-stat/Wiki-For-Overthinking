<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# AutoRAN: Automated Hijacking of Safety Reasoning in Large Reasoning Models

- **Authors**: Jiacheng Liang, Tanqiu Jiang, Yuhui Wang 0003, Rongyi Zhu, Fenglong Ma, Ting Wang 0006
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.1988>
- **DOI**: 10.18653/V1/2026.ACL-LONG.1988
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.80

## In one line

Automates the hijacking of a reasoning model's own safety reasoning by using a weaker, less-aligned model to simulate execution reasoning and refining attacks from patterns leaked in refusals.

## Problem

Reasoning models perform internal safety reasoning, and no framework existed to automate attacks against that reasoning specifically rather than against final outputs.

## Contributions

- AutoRAN, an automated framework for hijacking internal safety reasoning in reasoning models
- An execution simulation paradigm using a weaker, less-aligned model to generate initial hijacking attempts
- Iterative attack refinement that exploits reasoning patterns leaked through the target's refusals
- Approaching 100% success within one or few turns against GPT-o3/o4-mini and Gemini-2.5-Flash on AdvBench, HarmBench and StrongReject
- The argument that reasoning transparency is itself an exploitable attack surface

## Method

AutoRAN introduces an execution simulation paradigm: a weaker but less-aligned model simulates execution reasoning to produce initial hijacking attempts, and attacks are iteratively refined by exploiting reasoning patterns that the target leaks through its own refusals. Refusals are the signal — a refusal explains why it refused, and that explanation is exploitable. The result steers the target into bypassing its own guardrails and elaborating on harmful instructions.

## Results

Against GPT-o3/o4-mini and Gemini-2.5-Flash across AdvBench, HarmBench and StrongReject, AutoRAN reaches approaching 100% success within one or a few turns, neutralizing reasoning-based defences even when judged by robustly aligned external models.

## Limitations

Only three target models. Success is measured by benchmark judges, and 'approaching 100%' is not broken out per benchmark or model. The attack presupposes access to refusal text, so a model that refuses without explanation exposes less. No defence is proposed; the contribution is the attack surface and the argument that traces need protecting.

## Why it matters here

- **reasoning-training**: Its consequence for this topic is a genuine tension rather than a defect: the same readable trace that makes CoT monitoring possible also tells an attacker how the model's safety reasoning works, and refusals leak that structure for free. The archive holds monitorability as an argument for keeping reasoning explicit; this is the argument against, and it is not answerable by better training alone. It sits with arxiv:2608.04928 in this archive, which asks whether latent reasoning destroys monitorability — if transparency is also an attack surface, the cost of moving to latent reasoning is lower than the monitoring literature assumes.

## Entities

- **Concepts**: [jailbreak](../../../../wiki/concepts/jailbreak.md), safety reasoning, attack surface, transparency trade-off, refusal leakage, [monitorability](../../../../wiki/concepts/monitorability.md)
- **Methods**: AutoRAN, execution simulation, iterative attack refinement, automated red teaming
- **Datasets**: AdvBench, [HarmBench](../../../../wiki/datasets/harmbench.md), StrongReject

Tags: `jailbreak`, `red teaming`, `safety reasoning`, `attack`, `transparency`

## Abstract

This paper presents AutoRAN, the first framework to automate the hijacking of internal safety reasoning in large reasoning models (LRMs). At its core, AutoRAN pioneers an execution simulation paradigm that leverages a weaker but less-aligned model to simulate execution reasoning for initial hijacking attempts and iteratively refine attacks by exploiting reasoning patterns leaked through the target LRM's refusals. This approach steers the target model to bypass its own safety guardrails and elaborate on harmful instructions. We evaluate AutoRAN against state-of-the-art LRMs, including GPT-o3/o4-mini and Gemini-2.5-Flash, across multiple benchmarks (AdvBench, HarmBench, and StrongReject). Results show that AutoRAN achieves approaching 100% success rate within one or few turns, effectively neutralizing reasoning-based defenses even when evaluated by robustly aligned external models. This work reveals that the transparency of the reasoning process itself creates a critical and exploitable attack surface, highlighting the urgent need for new defenses that protect models'reasoning traces rather than merely their final outputs.

---

Record id: `doi:10.18653/v1/2026.acl-long.1988`
