<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# TQLite: Multi-LLM Jury Guided Distillation for Real-time MQM Translation Quality Evaluation

- **Authors**: Bhavin Jawade, Cameron R. Wolfe
- **Venue**: cs.CL
- **Published**: 2026-08-04
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.02975>
- **PDF**: <https://arxiv.org/pdf/2608.02975v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.40

## In one line

Benchmarks 20-plus models as MQM translation-quality judges, finds reasoning models best and a jury of different ones better than any member, then distils that jury's agreement-filtered annotations into a 12B student that beats every open reasoning-model judge tested.

## Problem

The best translation-quality metrics are LLM judges, and nearly all of them run on large closed models, which makes evaluation expensive and hard to replicate. Small models are cheap enough to deploy at scale but were assumed to lack the reasoning the task needs, and no systematic comparison existed across model sizes, reasoning and non-reasoning variants, and open versus closed weights — so neither the size of the gap nor what would close it was known.

## Contributions

- A benchmark of the same MQM prompt across closed and open models, reasoning and standard, reporting system-level and tie-calibrated segment-level pairwise accuracy rather than correlations
- The finding that the field's standard prompt is specialized to the model it was written for — every other model, including that model's own successor, performs significantly worse under it
- A measurement of what enforcing output structure costs: strict formatting degrades evaluation quality across all models, most severely in the smallest, while loose formatting makes results hostage to parsing heuristics
- Evidence that a jury of different reasoning models beats a jury of repeated samples from one, and exceeds every individual member at segment level
- A distillation pipeline that uses inter-judge agreement as the data filter — segments where the jury's MQM scores span zero are kept, wider spreads are discarded — with a meta-judge merging duplicate spans before training

## Method

Evaluation uses the WMT22 metrics test set over three language pairs with human MQM labels as gold, scored by system-level pairwise accuracy and segment-level pairwise accuracy with tie calibration, using the official scripts and avoiding correlation metrics for their known sensitivity to small samples and outliers. The benchmark sweeps prompt variants (free text, structured text, JSON; multi-turn against single-turn; with and without an explanation), then reasoning models at low and high reasoning effort, then juries formed either by repeated sampling from one model or by combining several. For distillation, a panel of large reasoning models annotates error spans for source-target pairs drawn from a 3M-pair corpus spanning seven languages; the spread between the most lenient and most critical MQM score across the jury sorts each segment into five agreement levels; segments at perfect or high agreement pass to a meta-judge that merges spans referring to the same underlying error and fixes canonical boundaries, categories and severities. The result — 99,214 samples under the default perfect-agreement filter — is used for LoRA supervised finetuning of two small open students under the identical prompt format the teachers saw.

## Results

Reasoning models dominate the benchmark: one reaches 92.34% system-level accuracy, and the best segment-level average is 57.06%, approaching top learned metrics. Open reasoning models trail closed ones substantially (76.28% to 84.31% system-level). Two negative results about evaluation practice are more transferable than the ranking. The standard MQM prompt turns out to be specialized to the model it was authored against — all other models, including that model's own newer sibling, perform significantly worse under it — so a prompt is not a neutral instrument carried between judges. And enforcing structured output degrades evaluation quality across every model at system level, with JSON worse than structured text and the damage concentrated in the smaller models, while loose formatting leaves 10% of outputs from a strong model and 85% from a 4B model with formatting errors that heuristic parsers must guess at. The paper adopts structured text as the lesser evil and says plainly that minor changes to the parsing algorithm substantially move the metrics with the model's output held fixed. On juries, aggregating different reasoning models improves more consistently than aggregating repeated samples from one, and a three-model jury reaches 57.07% segment-level — above every individual member. Distillation transfers most of that: the 12B student reaches 55.03% segment-level and 85.04% system-level, above all four open reasoning-model baselines and at far lower inference cost, with the best accuracy-per-inference-time of anything measured. Data quality beats data quantity in a clean monotone: training on perfect-agreement data alone gives 53.54%, adding high agreement 53.44%, moderate 52.21% and low 51.24%.

## Limitations

The paper's limitations are candid and the right ones: the distilled students still fall short of the best reasoning-model judges; synthetic training data from a jury may transmit the teachers' systematic biases even when aggregation is correct; the quality of the result depends on jury diversity and agreement, and the agreement filter may be removing exactly the edge cases and harder translation errors a judge most needs to see; and the evaluation covers only high- and medium-resource language pairs, leaving low-resource and morphologically complex languages untested. A reader should add one thing the paper does not discuss: distillation helps the 12B student on both metrics but *hurts* the 4B one, whose system-level accuracy falls from 86.50% to 82.48% and whose segment-level average falls slightly too — so the method has a capacity floor that the text passes over by scoping its claim to the larger student. The LoRA sweep also peaks at rank 128 while the reported configuration uses 256, attributed to the sweep's smaller training set.

## Why it matters here

- **reasoning-training**: Its bearing on this archive is through the judge, which several papers here rely on and none of them audits. Three results should change how those are read. A prompt carried from the paper that introduced it is not neutral — the standard prompt here is specialized to one model and degrades every other, including its own successor. Forcing structured output, which is what makes an automated judge usable at all, measurably lowers judgement quality, most in the smallest models, so the convenience is paid for in accuracy. And parsing heuristics move the reported metric with the model's output held fixed, which is a source of variance no paper in this archive reports. The distillation side contributes a filter worth borrowing: inter-teacher agreement as the data-selection criterion, with the monotone result that adding lower-agreement data makes the student worse at every step — a concrete instance of the archive's recurring finding that supervision quality dominates supervision quantity.

## Entities

- **Concepts**: LLM-as-a-judge, knowledge distillation, inter-annotator agreement, data quality, structured output, prompt sensitivity, jury aggregation, translation quality evaluation
- **Methods**: TQLite, GEMBA-MQM, [LLM-as-a-judge](../../../../wiki/methods/llm-as-a-judge.md), [supervised fine-tuning](../../../../wiki/methods/supervised-fine-tuning.md), [LoRA](../../../../wiki/methods/lora.md), multi-model jury, [chain-of-thought prompting](../../../../wiki/methods/chain-of-thought-prompting.md)
- **Datasets**: WMT22, OPUS-100, Europarl, MQM

Tags: `llm-as-a-judge`, `distillation`, `translation`, `evaluation`, `data quality`

## Abstract

Large language models (LLMs) have demonstrated impressive performance in MQM-based translation quality (TQ) evaluation, and recent advances in large reasoning models (LRMs) promise even greater improvements. However, both LLMs and LRMs are computationally expensive to deploy at scale, while small language models (SLMs)---though much more efficient---struggle with the complex reasoning required for evaluation tasks. In this work, we present an extensive empirical study benchmarking SLMs, LLMs, and LRMs across a wide range of TQ evaluation setups, providing a comprehensive view of the current landscape and establishing best practices. To address the scalability challenge, we introduce TQLite, a novel distillation framework that enables SLMs to approach the MQM evaluation performance of the best LRM-based evaluators. Our approach leverages a multi-LRM jury to generate high-quality synthetic training data via practical data curation techniques and aggregation of evaluation responses across a diverse panel of models. Our results demonstrate that SLMs trained via TQLite achieve strong MQM evaluation performance that far exceeds off-the-shelf evaluation capabilities of standard SLMs, offering a scalable and cost-effective alternative to LLM- and LRM-based evaluators.

---

Record id: `arxiv:2608.02975`
