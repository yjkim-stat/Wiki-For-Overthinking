<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ReasoningGuard: Safeguarding Large Reasoning Models with Inference-time Safety Aha Moments

- **Authors**: Yuquan Wang, Mi Zhang 0001, Yining Wang, Geng Hong, Mi Wen, Xiaoyu You, Min Yang 0002
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.1453>
- **DOI**: 10.18653/V1/2026.ACL-LONG.1453
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.80

## In one line

An inference-time safeguard that reads a reasoning model's attention to find key points in its reasoning path and injects safety reflections there, then scales sampling to pick a safe path.

## Problem

Reasoning models remain vulnerable to harmful content generation, particularly in the mid-to-late steps of reasoning — the harm appears after reasoning has started, which a prompt-level filter cannot see. Existing defences need costly fine-tuning and expert knowledge, limiting scalability.

## Contributions

- The observation that harmful generation in reasoning models concentrates in mid-to-late reasoning steps
- ReasoningGuard, a fine-tuning-free inference-time safeguard that injects safety reflections at attention-identified key points
- A scaling sampling strategy at decoding to select a safe reasoning path
- Mitigation of four jailbreak types, outperforming nine safeguards without exaggerated safety

## Method

ReasoningGuard injects timely safety 'aha moments' during reasoning to steer the model toward harmless yet helpful output. It uses the model's internal attention mechanisms to identify key points in the reasoning path where a safety-oriented reflection should be triggered — attention supplies the timing, which is the part a static filter lacks. A scaling sampling strategy at decoding then selects the best reasoning path, protecting both later steps and the final answer.

## Results

With minimal additional inference cost, ReasoningGuard mitigates four types of jailbreak attack, including recent ones targeting the reasoning process of reasoning models, and outperforms nine existing safeguards while avoiding exaggerated-safety failures. No numbers are given in the abstract.

## Limitations

No quantitative results, models or benchmark names in the abstract. Requires access to internal attention, so it cannot be applied to an API-only model. Four jailbreak types is a bounded threat model, and an inference-time intervention placed by attention could be attacked by prompts that manipulate attention. 'Minimal additional inference cost' is unquantified, and the scaling sampling strategy implies more than one sampled path.

## Why it matters here

- **reasoning-training**: Its transferable finding for this topic is where in a trajectory the failure lives: mid-to-late reasoning steps, not the prompt and not the final answer. That is a positional claim about trained reasoning behaviour and it parallels the archive's entropy and commitment-boundary results, which also locate decisive structure at specific points in a trace. Using attention to time an intervention is a different localization signal from the entropy-based ones already tracked here, and whether the two identify the same positions is measurable and unmeasured.

## Entities

- **Concepts**: [aha moment](../../../../wiki/concepts/aha-moment.md), [jailbreak](../../../../wiki/concepts/jailbreak.md), [inference-time intervention](../../../../wiki/concepts/inference-time-intervention.md), [attention pattern](../../../../wiki/concepts/attention-pattern.md), [test-time compute](../../../../wiki/concepts/test-time-compute.md), exaggerated safety, reasoning path selection
- **Methods**: ReasoningGuard, [attention analysis](../../../../wiki/methods/attention-analysis.md), scaling sampling, safety reflection injection
- **Datasets**: _none recorded_

Tags: `safety`, `jailbreak`, `inference-time`, `attention`, `aha moment`

## Abstract

Large Reasoning Models (LRMs) have demonstrated impressive performance in reasoning-intensive tasks, but they remain vulnerable to harmful content generation, particularly in the mid-to-late steps of their reasoning processes. Current defense methods, however, depend on costly fine-tuning and additional expert knowledge, which limits their scalability.In this work, we propose ReasoningGuard, an inference-time safeguard for LRMs.It injects timely safety aha moments during the reasoning process to guide the model towards harmless yet helpful reasoning.Our approach leverages the internal attention mechanisms of the LRM to accurately identify key points in the reasoning path, triggering safety-oriented reflections.To safeguard both the subsequent reasoning steps and the final answers, we implement a scaling sampling strategy during decoding to select the optimal reasoning path.With minimal additional inference cost, ReasoningGuard effectively mitigates four types of jailbreak attacks, including recent ones targeting the reasoning process of LRMs. Our approach outperforms nine existing safeguards, providing state-of-the-art defenses while avoiding common exaggerated safety issues.

---

Record id: `doi:10.18653/v1/2026.acl-long.1453`
