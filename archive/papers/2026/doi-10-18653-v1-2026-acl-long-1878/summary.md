<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Scaling Reasoning, Losing Control: Evaluating Instruction Following in Large Reasoning Models

- **Authors**: Tingchen Fu, Yafu Li, Jiawei Gu, Xiaoye Qu, Yu Cheng 0001
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.1878>
- **DOI**: 10.18653/V1/2026.ACL-LONG.1878
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.80

## In one line

A benchmark showing that as reasoning capacity grows, instruction adherence falls, and that recovering obedience costs reasoning performance.

## Problem

Instruction-following aligns models with user intent. Reasoning-oriented models do well on hard mathematics, but whether they still follow natural-language instructions is underexplored — and controllability is what makes a capable model usable.

## Contributions

- MathIF, a benchmark for instruction-following inside mathematical reasoning tasks
- Evidence of a consistent tension between reasoning capacity and controllability
- The finding that both distilled long-CoT tuning and reasoning-oriented RL degrade instruction adherence, worsening with generation length
- Evidence that simple obedience-restoring interventions cost reasoning performance

## Method

MathIF is a benchmark for evaluating instruction-following within mathematical reasoning tasks, so instruction compliance and reasoning are measured on the same items. Empirical analysis compares models tuned on distilled long chains-of-thought against those trained with reasoning-oriented reinforcement learning, and examines how adherence varies with generation length. Simple interventions to recover obedience are tested.

## Results

A consistent tension appears between scaling reasoning capacity and maintaining controllability: models that reason more effectively often comply less with user directives. Both distilled long-CoT tuning and reasoning-oriented RL degrade instruction adherence, especially as generation length increases. Simple interventions partially recover obedience but cost reasoning performance.

## Limitations

No numbers in the abstract, so the size of the trade-off is unstated, and the models are not named. The tension is observed across training paradigms rather than isolated by a controlled intervention, so it is a correlation between reasoning strength and disobedience. The length dependence is a confound worth noting: longer generations offer more opportunities to violate a constraint, so part of the effect could be exposure rather than degradation.

## Why it matters here

- **reasoning-training**: States a cost of reasoning training that this archive has not been tracking: controllability. Every method here that improves reasoning is evaluated on reasoning, so a regression in instruction adherence is invisible by construction, and this paper plus doi:10.18653/v1/2026.findings-acl.1456 in the same drain both find it. It also reports the trade-off in both directions — recovering obedience costs reasoning — which makes it a genuine Pareto tension rather than a fixable defect, and it belongs next to findings-acl.1717 on general-capability forgetting as evidence that RLVR gains are paid for outside the benchmark.

## Entities

- **Concepts**: [instruction following](../../../../wiki/concepts/instruction-following.md), [controllability](../../../../wiki/concepts/controllability.md), [alignment tax](../../../../wiki/concepts/alignment-tax.md), reasoning capability, generation length, trade-off
- **Methods**: MathIF, distillation, [reinforcement learning post-training](../../../../wiki/methods/reinforcement-learning-post-training.md), prompt intervention
- **Datasets**: MathIF

Tags: `instruction following`, `benchmark`, `controllability`, `alignment tax`, `math reasoning`

## Abstract

Instruction-following is essential for aligning large language models (LLMs) with user intent. While recent reasoning-oriented models exhibit impressive performance on complex mathematical problems, their ability to adhere to natural language instructions remains underexplored. In this work, we introduce MathIF, a dedicated benchmark for evaluating instruction-following in mathematical reasoning tasks. Our empirical analysis reveals a consistent tension between scaling up reasoning capacity and maintaining controllability, as models that reason more effectively often struggle to comply with user directives. We find that models tuned on distilled long chains-of-thought or trained with reasoning-oriented reinforcement learning often degrade in instruction adherence, especially when generation length increases. Furthermore, we show that even simple interventions can partially recover obedience, though at the cost of reasoning performance. These findings highlight a fundamental tension in current LLM training paradigms and motivate the need for more instruction-aware reasoning models.

---

Record id: `doi:10.18653/v1/2026.acl-long.1878`
