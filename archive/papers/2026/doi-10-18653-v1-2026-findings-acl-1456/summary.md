<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ReasonIF: Large Reasoning Models Fail to Follow Instructions During Reasoning

- **Authors**: Yongchan Kwon, Shang Zhu, Federico Bianchi 0001, Kaitlyn Zhou, James Zou 0001
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.findings-acl.1456>
- **DOI**: 10.18653/V1/2026.FINDINGS-ACL.1456
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.80

## In one line

Benchmarks whether reasoning models follow instructions inside their reasoning traces, finding under 25% compliance at best and worse as difficulty rises.

## Problem

Prior work assesses instruction adherence in a model's main response. The paper argues adherence matters within the reasoning process too, because reasoning-level instruction following is what makes models controllable and transparent and reduces shortcuts, hallucinations and reward hacking inside traces.

## Contributions

- The argument that instruction following inside reasoning traces is a distinct and critical alignment dimension
- ReasonIF, a benchmark with six instruction categories spanning multilingual reasoning and length control
- The finding that the best instruction following score stays below 0.25 across GPT-OSS, Qwen3 and DeepSeek-R1
- The finding that reasoning instruction adherence degrades as task difficulty increases
- Reasoning Instruction Finetuning on synthetic data, raising GPT-OSS-20B's IFS from 0.11 to 0.27

## Method

ReasonIF is a systematic benchmark for reasoning instruction following, with six categories of instruction prompts spanning multilingual reasoning and length control. Two improvement strategies are then tested: multi-turn reasoning, and Reasoning Instruction Finetuning on synthetic data.

## Results

Across open-source reasoning models including GPT-OSS, Qwen3 and DeepSeek-R1, adherence fails substantially: the highest instruction following score remains below 0.25, so fewer than 25% of reasoning traces comply. Adherence degrades further as task difficulty increases. RIF raises GPT-OSS-20B's IFS from 0.11 to 0.27.

## Limitations

Six instruction categories concentrated on multilingual reasoning and length control, so the finding covers a specific slice of instruction types. IFS below 0.25 is a low base rate, and RIF's 0.11 to 0.27 more than doubles it while still leaving most traces non-compliant. Whether reasoning-trace compliance is desirable in all cases is assumed — constraining the trace could cost reasoning quality, and this abstract does not report that trade-off, which acl-long.1878 finds for response-level instructions.

## Why it matters here

- **reasoning-training**: Establishes that the reasoning trace is largely outside user control — under 25% compliance — which has a consequence the paper states and the archive should hold: methods that assume the trace can be steered by instruction are building on a 25% success rate. That includes prompt-level safety and monitorability schemes. Together with acl-long.1878 in this drain, which finds response-level adherence degrading as reasoning capacity grows, the pair says controllability is weak both in the answer and in the trace, and worsens exactly where it matters most — harder problems and stronger reasoners. RIF doubling IFS shows the gap is trainable rather than intrinsic.

## Entities

- **Concepts**: [instruction following](../../../../wiki/concepts/instruction-following.md), [controllability](../../../../wiki/concepts/controllability.md), [monitorability](../../../../wiki/concepts/monitorability.md), [reward hacking](../../../../wiki/concepts/reward-hacking.md), [alignment](../../../../wiki/concepts/alignment.md), reasoning trace, difficulty scaling
- **Methods**: ReasonIF, Reasoning Instruction Finetuning, [multi-turn reasoning](../../../../wiki/methods/multi-turn-reasoning.md), [synthetic data generation](../../../../wiki/methods/synthetic-data-generation.md)
- **Datasets**: ReasonIF

Tags: `instruction following`, `benchmark`, `controllability`, `reasoning trace`, `alignment`

## Abstract

The ability of large language models (LLMs) to follow user instructions is central to their reliability, safety, and usefulness. While prior studies assess instruction adherence in the model’s main responses, we argue that it is also critical for large reasoning models (LRMs) to follow user instructions throughout their reasoning process. Reasoning instruction following makes LRMs more controllable and transparent, while reducing risks of undesirable shortcuts, hallucinations, or reward hacking within reasoning traces. To evaluate this dimension, we introduce ReasonIF, a systematic benchmark for assessing reasoning instruction following. ReasonIF includes six categories of instruction prompts, spanning multilingual reasoning, and length control. Across many open-source LRMs including GPT-OSS, Qwen3, and DeepSeek-R1, we find substantial failures in reasoning instruction adherence: the highest instruction following score (IFS) remains below 0.25, meaning that fewer than 25% of reasoning traces comply with the given instructions. Notably, as task difficulty increases, reasoning instruction following degrades further. We also explore two strategies to enhance reasoning instruction fidelity: (1) multi-turn reasoning and (2) Reasoning Instruction Finetuning (RIF) using synthetic data. RIF improves the IFS of GPT-OSS-20B from 0.11 to 0.27, indicating measurable progress but leaving ample room for improvement. We hope this work draws attention to reasoning-level instruction adherence as an underexplored but critical aspect of model alignment, and helps pave the way toward more controllable, interpretable, and trustworthy reasoning models.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1456`
