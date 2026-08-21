<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Towards Safe Reasoning in Large Reasoning Models via Corrective Intervention

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10011693>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

A process-supervision method that intervenes at identified 'safety trigger' points within a reasoning chain to redirect it away from harmful continuations, trained via preference optimization on corrected trajectories.

## Problem

Large reasoning models can produce harmful content within their reasoning chains even when the final answer looks safe, and existing alignment methods do not target the safety of the reasoning process itself; naively rewarding 'safe' reasoning fails because of limited trajectory diversity and weak feedback.

## Contributions

- Identifies 'safety triggers': critical decision points in a reasoning chain where safety is determined
- Identifies 'compliance cues': patterns that strongly predict harmful continuations
- Introduces Intervened Preference Optimization (IPO), which replaces compliance-cue steps with safety-trigger corrections to build stronger preference pairs for training
- Reports over 30% harmfulness reduction relative to baselines on jailbreak and adversarial benchmarks while maintaining reasoning performance

## Method

The authors locate 'safety trigger' points and 'compliance cue' patterns within reasoning chains, then use corrective intervention -- replacing a compliance-cue step with a safety-trigger correction -- to construct preference pairs with a stronger training signal. Intervened Preference Optimization (IPO) trains on these pairs to redirect reasoning away from harmful continuations at the process level, rather than only filtering final outputs.

## Results

Over 30% harmfulness reduction relative to baseline approaches on jailbreak and adversarial benchmarks, while maintaining reasoning performance; specific benchmark names and numeric baselines are not given in the available abstract.

## Limitations

Not stated in the available material (abstract only; no PDF attached). The abstract notes that simply rewarding safe reasoning outcomes is insufficient on its own, due to limited trajectory diversity and weak training feedback, which motivates the corrective-intervention design.

## Why it matters here

- **overthinking**: Concerned with the safety and harmfulness of content generated inside a reasoning chain, not with reasoning length, when to stop reasoning, or the accuracy/efficiency tradeoff of thinking more or less. It matches the tracked topic only via the generic 'large reasoning model' keyword and has no substantive connection to overthinking or test-time compute tradeoffs. Tangential.

## Entities

- **Concepts**: safety triggers, compliance cues, [process supervision](../../../../wiki/concepts/process-supervision.md), reasoning safety, preference optimization
- **Methods**: Intervened Preference Optimization (IPO)
- **Datasets**: _none recorded_

Tags: `reasoning-safety`, `jailbreak-defense`, `preference-optimization`, `process-supervision`, `tangential`

## Abstract

Abstract Although Large Reasoning Models (LRMs) have progressed in solving complex problems, their chain-of-thought (CoT) reasoning often contains harmful content that can persist even when the final responses appear safe. We show that this issue still remains in existing methods which overlook the unique significance of safe reasoning, undermining their trustworthiness and posing potential risks in applications if unsafe reasoning is accessible for and exploited by malicious users. We therefore shift our focus to aligning the safety of reasoning itself in this paper and explore process supervision as the solution. However, simply rewarding safe reasoning proves inadequate due to low rollout diversity and limited training signals. To tackle this challenge, we first delve into the characteristics of safe reasoning and uncover several critical insights that 1) safe reasoning is often consolidated by a few critical steps of safety triggers ; 2) compliance cues strongly correlate with unsafe continuations; and 3) corrective interventions reliably steer unsafe trajectories towards safer traces. Motivated by these, we propose Intervened Preference Optimization (IPO) , an alignment method that enforces safe reasoning by substituting compliance steps with safety triggers and constructing pairs for preference learning with strong signals. Experiments on jailbreak and adversarial safety benchmarks demonstrate that IPO remarkably improves overall safety regarding both reasoning and responses, outperforming SFT-based and RL-based baselines with a relative reduction of over 30\% in harmfulness, while preserving excellent performance across diverse reasoning tasks. The results highlight the importance of explicit alignment for reasoning and provide a practical path to safer LRMs.

---

Record id: `title:3b1dfa6d6e5e2443`
