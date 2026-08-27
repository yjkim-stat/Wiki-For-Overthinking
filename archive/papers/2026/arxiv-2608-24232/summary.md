<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# TRACE: An Evidence-Grounded Benchmark for Safety Evaluation of Large Reasoning Models

- **Authors**: Zhenyu Wu, Siyuan Chen, Changchun Yang, Jiaqi Dong, Min Zhou, Ali Almadan, Talal Hammad, Faisal Wahbo, Aminullah Tora, Mona Alshahrani, Xin Gao
- **Venue**: cs.AI
- **Published**: 2026-08-25
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.24232>
- **PDF**: <https://arxiv.org/pdf/2608.24232v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

TRACE is a benchmark that extends LLM-safety evaluation from prompts and final responses to the reasoning traces of large reasoning models, with evidence-grounded annotations for each safety label.

## Problem

Guardrail models are evaluated on the safety of prompts and final responses, but the intermediate reasoning traces LRMs produce can be unsafe even when the final response looks safe, and no benchmark evaluates guardrail models on reasoning-trace safety or requires them to cite the evidence behind a safety judgment.

## Contributions

- TRACE, a safety benchmark spanning the full LRM inference pipeline (prompt, reasoning trace, final response) with per-component safety labels and verbatim supporting evidence
- an evaluation of 18 guardrail models showing reasoning-trace safety judgment is more difficult than prompt or final-response judgment, and that all models struggle to attribute evidence for their judgments

## Method

Prompts are drawn from S-Eval (unsafe) and WildChat (safe), stratified across 9 risk categories, 10 attack strategies and 2 languages (EN/ZH), yielding 1,993 prompts. For each prompt, 4 LRMs (Qwen3-8B, Qwen3-8B-abliterated, Gemma-4-E4B, Gemma-4-E4B-abliterated) generate a reasoning trace and final response. Three annotator LRMs (DeepSeek-V3.2, Qwen3.5-Plus, KIMI-K2.5) independently label the safety of the prompt, trace and response and extract verbatim supporting evidence; the label is set by majority vote, and evidence is kept only when it comes from an annotator aligned with that vote and verifiable as a literal substring of the source text, with unverifiable cases sent to human annotators. 18 guardrail models are then scored on TRACE for safety-judgment F1 and, where a model gives evidence, on token-level overlap (TokenF1) between its cited evidence and the ground truth.

## Results

Across 18 guardrail models, average F1 is 75.75% on prompts, 70.53% on final responses and 66.31% on reasoning traces -- trace safety is the hardest of the three stages for 14/18 models. Best single-stage results: YuFeng-XGuard-8B 88.27% F1 on prompts, PolyGuard-8B 91.17%; YuFeng-XGuard-8B reaches 84.26% on reasoning-trace judgment and 86.11% on final-response judgment. Evidence attribution is far weaker than the safety judgment itself: even the best model (YuFeng-XGuard-8B) reaches only 11.68% (prompt), 13.71% (final response) and 14.88% (reasoning trace) TokenF1. Instruction-Encryption attacks (e.g. Base64, Caesar cipher) cause the largest degradation, dropping YuFeng-XGuard-8B and PolyGuard-8B to 35-39% F1 on reasoning-trace judgment. 17/18 models score higher on Chinese prompts than English ones.

## Limitations

TRACE covers only English and Chinese, so cross-lingual generality beyond these two is untested. Safety labels rely on 3 annotator LRMs plus human review of unresolved cases rather than full human annotation, so some label noise may remain. The paper does not report how reasoning-trace length or verbosity relates to safety, so it says nothing about whether longer traces are more or less likely to contain unsafe content.

## Why it matters here

- **overthinking**: Tangential rather than central: TRACE examines the LRM reasoning trace as an artifact to be checked for unsafe content, not for its length or the accuracy/efficiency tradeoff overthinking concerns itself with. It is useful mainly as an example that reasoning traces are now treated as a first-class output surface to evaluate, alongside evidence that safety can flip between stages of a single inference (prompt vs. trace vs. response).

## Entities

- **Concepts**: evidence-grounded safety annotation, guardrail model, reasoning trace safety, abliteration
- **Methods**: majority-vote safety annotation with evidence verification, TokenF1 evidence-attribution metric
- **Datasets**: S-Eval, WildChat

Tags: `safety`, `guardrail`, `reasoning-trace`, `benchmark`, `evidence-attribution`

## Abstract

Large Reasoning Models (LRMs) generate intermediate reasoning traces that may contain unsafe content, even when their final responses appear safe. Guardrail models are designed to detect and block unsafe content, yet existing benchmarks for unsafe content detection focus primarily on prompts and final responses, leaving reasoning traces largely unexamined. Moreover, these benchmarks typically provide only binary safety labels, without evidence annotations that justify the judgments. To address these limitations, we introduce TRACE, an evidence-grounded safety evaluation benchmark that covers the entire LRM inference pipeline: prompts, reasoning traces, and final responses. TRACE includes prompts in two languages spanning nine risk categories and ten attack strategies. For each prompt, four LRMs generate reasoning traces and final responses, and we annotate the safety of each component and extract supporting evidence from the corresponding source text. Evaluating 18 guardrail models on TRACE reveals that safety judgment for reasoning traces is substantially more challenging than for prompts or final responses, and that current models struggle to accurately extract supporting evidence. These findings highlight the need for guardrail models that can reliably detect and precisely localize unsafe content across the LRM inference pipeline.

---

Record id: `arxiv:2608.24232`
