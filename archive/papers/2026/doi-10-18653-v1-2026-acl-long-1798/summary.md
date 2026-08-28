<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ReTraceQA: Evaluating Reasoning Traces of Small Language Models in Commonsense Question Answering

- **Authors**: Francesco Maria Molfese, Luca Moroni, Ciro Porcaro, Simone Conia, Roberto Navigli
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.1798/>
- **PDF**: <https://aclanthology.org/2026.acl-long.1798.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.1798
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

ReTraceQA is a 2,421-instance expert-annotated benchmark showing that small language models (SLMs) reach the correct final answer via a flawed reasoning trace 14-24% of the time on commonsense QA, and that LLM-as-judge and PRM evaluators reliably detect overall trace correctness but struggle to localize the specific erroneous step, inflating answer-only accuracy scores by up to 25%.

## Problem

Standard evaluation of small language models on commonsense reasoning relies almost exclusively on final-answer accuracy, ignoring whether the reasoning trace that produced the answer is actually valid, so models that reach a correct answer through invalid reasoning have their true capabilities artificially inflated -- and existing process-level reasoning-trace benchmarks focus almost entirely on math/science, leaving commonsense reasoning largely unexamined.

## Contributions

- ReTraceQA, the first benchmark for evaluating small language models' reasoning-trace validity in commonsense QA, with 2,421 expert-annotated traces carrying step-level error locations and categories
- quantitative evidence that 14-24% of SLM reasoning traces reach the correct final answer despite containing a reasoning error
- a comprehensive evaluation showing current LLM-as-judge models and math-trained PRMs detect overall correctness better than they localize the erroneous step, and that PRMs transfer poorly across domains
- a downstream demonstration that reasoning-aware evaluation drops measured SLM accuracy by an average 18.6 points versus answer-only evaluation

## Method

Sources questions from four commonsense datasets (CommonsenseQA, OpenBookQA, QASC, StrategyQA), generates zero-shot CoT reasoning traces with seven open-weight SLMs (<=10B parameters), and samples a balanced subset for annotation. Three PhD-level expert annotators label each trace with the index of the earliest erroneous step (or -1 if fully correct) and, for erroneous traces, one of three error categories: Misinterpretation (grounding-level), Hallucination (content-level, false/unverifiable world knowledge), and Reasoning (inference-level, invalid logical leap). Reaches 2,421 clean annotated instances (Fleiss' kappa 0.84). Evaluates reference-free and reference-based LLM-as-judge models and math-trained Process Reward Models on identifying trace correctness, then uses the best judge (o1-mini) to re-score seven SLMs' downstream commonsense-QA accuracy under answer-only extraction versus full reasoning-aware judging.

## Results

17.9% of SLM responses (range 14.7-24.0% across datasets) reach the correct final answer despite containing a reasoning error, so answer-only accuracy systematically overestimates true reasoning capability by this margin. Hallucination is the majority failure mode (41.9-62.5% of errors), followed by reasoning errors (27.9-35.4%) and misinterpretation (9.6-24.1%). Math-trained PRMs transfer poorly to commonsense reasoning (average F1 often below 25%), while LLM-as-judge models do better but still only reach 54-56% average F1 (o1-mini best at 62.3%) in reference-free evaluation. In reference-based evaluation, model size correlates with judging performance but is insufficient alone (DeepSeek-R1 underperforms the smaller Qwen2.5-72B-Instruct); o1-mini is the strongest overall judge (74.4% average F1), and correctness detection is consistently stronger than error localization across all judges. Using o1-mini as a full reasoning-aware judge instead of answer-only extraction reveals SLM performance is inflated by an average 18.6 percentage points (68.3%->49.7% across seven SLMs and four benchmarks), with even the strongest tested SLM (Qwen2.5-7B-Instruct) dropping from 81.0% to 67.5%.

## Limitations

Restricted to small language models (<=10B parameters) and four multiple-choice/binary commonsense datasets; whether the same inflation magnitude holds for larger reasoning-focused models or open-ended tasks is untested. Reasoning-trace segmentation relies on a fixed newline-based heuristic. Even the strongest judges struggle specifically with error localization versus overall correctness detection, an open problem the paper flags rather than solves.

## Why it matters here

- **overthinking**: Tangential: this is about the correctness of reasoning traces in commonsense QA for small (non-reasoning-focused) models, not reasoning length or the accuracy/efficiency tradeoff. Relevant as a methodological caution applicable across the archive: several efficiency papers here validate length-reduction methods by checking final-answer accuracy is preserved, but this paper's finding (14-24% of correct answers rest on flawed reasoning) is a reminder that answer-preservation alone does not confirm a compressed or pruned trace is still reasoning correctly.

## Entities

- **Concepts**: process error (correct answer, flawed reasoning), reasoning-aware vs. answer-only evaluation, error taxonomy (Misinterpretation / Hallucination / Reasoning), answer-only performance inflation
- **Methods**: LLM-as-judge (reference-free and reference-based), Process Reward Models (Math-Shepherd, Skywork-PRM, Qwen2.5-Math-PRM), zero-shot Chain-of-Thought reasoning-trace generation
- **Datasets**: ReTraceQA (new, 2,421 annotated traces), [CommonsenseQA](../../../../wiki/datasets/commonsenseqa.md), [OpenBookQA](../../../../wiki/datasets/openbookqa.md), QASC, [StrategyQA](../../../../wiki/datasets/strategyqa.md)

Tags: `reasoning-trace-evaluation`, `commonsense-reasoning`, `small-language-models`, `process-reward-models`, `llm-as-judge`

## Abstract

While Small Language Models (SLMs) have demonstrated promising performance on an increasingly wide array of commonsense reasoning benchmarks, current evaluation practices rely almost exclusively on the accuracy of their final answers, neglecting the validity of the reasoning processes that lead to those answers. To address this issue, we present ReTraceQA, a novel benchmark that introduces process-level evaluation for commonsense reasoning tasks. Our expert-annotated dataset reveals that in a substantial portion of instances (14-24%), SLMs provide correct final answers despite flawed reasoning processes, suggesting that the capabilities of SLMs are often overestimated by evaluation metrics that focus only on comparing the final answer with the ground truth. Indeed, we show that, when employing strong Large Language Models (LLMs) as automated judges for reasoning-aware evaluation rather than answer-only metrics, SLM performance drops significantly across all models and datasets, with scores decreasing by up to 25%.

---

Record id: `doi:10.18653/v1/2026.acl-long.1798`
