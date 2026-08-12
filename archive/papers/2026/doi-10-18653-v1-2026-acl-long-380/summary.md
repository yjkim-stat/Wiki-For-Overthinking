<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# AgentCoMa: A Compositional Benchmark Mixing Commonsense and Mathematical Reasoning in Real-World Scenarios

- **Authors**: Lisa Alazraki, Lihu Chen, Ana Brassard, Joe Stacey, Hossein A. Rahmani, Marek Rei
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.380>
- **DOI**: 10.18653/V1/2026.ACL-LONG.380
- **Topics**: reasoning-evaluation
- **Relevance score**: reasoning-evaluation 0.50

## In one line

A benchmark where each task needs one commonsense step and one math step, on which model accuracy drops nearly 30% relative to solving the steps in isolation while humans show no such gap.

## Problem

Compositional benchmarks test either commonsense or mathematical reasoning, but agents solving real-world tasks need both combined. Whether models can compose across reasoning types, as opposed to chaining steps of the same type, is untested.

## Contributions

- AgentCoMa, a compositional benchmark where every task mixes a commonsense step with a math step
- A design permitting isolated-step and combined evaluation of the same items
- Evaluation of 61 LLMs across sizes, families and training strategies, with a human annotator reference
- The finding of a nearly 30% average compositional drop, larger than in same-type compositional benchmarks, absent in humans
- Interpretability analyses over neuron patterns, attention maps and membership inference

## Method

AgentCoMa is an agentic commonsense-and-math benchmark in which each compositional task requires one commonsense reasoning step and one math reasoning step. The design allows each step to be tested in isolation as well as combined, which is what isolates composition from step difficulty. 61 LLMs across sizes, families and training strategies are evaluated, and non-expert human annotators are tested on the same items as a reference. Interpretability studies examine neuron patterns, attention maps and membership inference.

## Results

LLMs can usually solve both steps in isolation, yet accuracy drops by nearly 30% on average when the two are combined — a substantially greater gap than in prior compositional benchmarks that combine multiple steps of the same reasoning type. Non-expert human annotators solve the compositional questions and the individual steps with similarly high accuracy, so the gap is model-specific.

## Limitations

Each task is two steps of fixed types, so the finding is about mixed-type composition at depth two rather than composition in general. 'Nearly 30% on average' is over 61 models with no per-family breakdown in the abstract. The human comparison uses non-expert annotators without reported agreement or sample size. The interpretability studies are described but their conclusions are not stated.

## Why it matters here

- **reasoning-evaluation**: The cleanest measurement design in this drain: because both steps are separately testable on the same items, the nearly 30% drop is attributable to composition rather than to either step being hard, and the human reference rules out the items simply being harder when combined. That makes it a rare benchmark where the deficit is isolated rather than inferred. It also implies that any evaluation built from single-type multi-step problems systematically overstates compositional ability, which covers most of the math benchmarks this archive tracks. The membership-inference component is a contamination check, which the archive has found almost universally missing.

## Entities

- **Concepts**: [compositional generalization](../../../../wiki/concepts/compositional-generalization.md), commonsense reasoning, [out-of-distribution generalization](../../../../wiki/concepts/out-of-distribution-generalization.md), brittleness, [construct validity](../../../../wiki/concepts/construct-validity.md), membership inference
- **Methods**: AgentCoMa, isolated-step ablation, human baseline comparison, [attention analysis](../../../../wiki/methods/attention-analysis.md), [membership inference](../../../../wiki/methods/membership-inference.md)
- **Datasets**: AgentCoMa

Tags: `benchmark`, `compositional reasoning`, `commonsense`, `brittleness`, `human baseline`

## Abstract

Large Language Models (LLMs) have achieved high accuracy on complex commonsense and mathematical problems that involve the composition of multiple reasoning steps. However, current compositional benchmarks testing these skills tend to focus on either commonsense or math reasoning, whereas LLM agents solving real-world tasks would require a combination of both. In this work, we introduce an Agentic Commonsense and Math benchmark (AgentCoMa), where each compositional task requires a commonsense reasoning step and a math reasoning step. We test it on 61 LLMs of different sizes, model families, and training strategies. We find that LLMs can usually solve both steps in isolation, yet their accuracy drops by nearly 30% on average when the two are combined. This is a substantially greater performance gap than the one we observe in prior compositional benchmarks that combine multiple steps of the same reasoning type. In contrast, non-expert human annotators can solve the compositional questions and the individual steps in AgentCoMa with similarly high accuracy. Furthermore, we conduct a series of interpretability studies to better understand the performance gap, examining neuron patterns, attention maps and membership inference. Our work underscores a substantial degree of model brittleness in the context of mixed-type compositional reasoning and offers a test bed for future improvement.

---

Record id: `doi:10.18653/v1/2026.acl-long.380`
