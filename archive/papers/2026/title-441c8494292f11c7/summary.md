<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# OptimalThinkingBench: Evaluating Over and Underthinking in LLMs

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10009890>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

Introduces OptimalThinkingBench, a unified benchmark pairing OverthinkingBench (simple queries) and UnderthinkingBench (hard reasoning/math) with a shared F1 metric, showing that none of 33 evaluated LLMs balances accuracy and thinking-token efficiency.

## Problem

Thinking LLMs overthink simple queries, generating hundreds of tokens without improving (and sometimes hurting) accuracy, while non-thinking LLMs underthink on harder reasoning problems and fall short of much smaller thinking models. Model providers ship separate thinking and non-thinking variants, forcing end users to manually pick the right one per query rather than having a single model that adapts its reasoning length to task difficulty.

## Contributions

- Introduces OptimalThinkingBench, a single unified benchmark combining OverthinkingBench and UnderthinkingBench with standardized metrics (OAA, AUC_OAA, F1^otb) for jointly measuring overthinking and underthinking.
- Comprehensive evaluation of 33 open and closed thinking, non-thinking, and hybrid LLMs showing that no current model optimally balances accuracy and thinking-token efficiency.
- Compares training-time and test-time methods for optimal thinking, showing most improve one sub-benchmark at the expense of the other.

## Method

OptimalThinkingBench has two sub-benchmarks. OverthinkingBench is built via constrained synthetic generation with Llama-4-Maverick across 72 domains and 4 answer types (numeric, MCQ, short-answer, open-ended), then filtered by requiring 8/8 agreement across independently sampled LLM responses (judged by an LLM-as-judge) so only unambiguous, easy questions survive (1327 OvT-General questions plus 133 OvT-Math questions from MATH levels 1-2). Overthinking is scored with Overthinking-Adjusted Accuracy (OAA_t): accuracy counted only for responses under a thinking-token threshold t, aggregated as AUC_OAA (area under the OAA_t curve up to t_max=1000). UnderthinkingBench draws on 11 Reasoning Gym task types plus AIME'25 and HMMT'25 math, keeping only tasks where a small thinking model (Qwen3-1.7B) outperforms a much larger non-thinking model (Qwen3-235B-A22B) by a margin; scored with task-specific programmatic verifiers. The two combine into a single F1^otb score (harmonic mean of AUC_OAA and UnderthinkingBench accuracy). The authors evaluate 33 open and closed thinking/non-thinking/hybrid models and test five mitigation strategies: length-based reward shaping (L1, AdaptThink), model merging, auxiliary verification training (VeriThinker), difficulty-based routing, and explicit prompting.

## Results

No model optimally balances both sub-benchmarks. o3 gets the best overall F1^otb (71.1%); best open-weight model is GPT-OSS-120B (68.3%), a 3-point gap. On OverthinkingBench, thinking models generate at least ~100-3300+ thinking tokens on trivially simple questions, driving AUC_OAA far below raw accuracy. On UnderthinkingBench, thinking models substantially outperform non-thinking ones: o3 leads at 65.0% accuracy, GPT-OSS-120B at 57.9%. Mitigation methods (L1, AdaptThink, VeriThinker, Model Merging) cut OverthinkingBench token use by 12-91% but degrade UnderthinkingBench accuracy by up to 13% in most configurations; AdaptThink is the one method that improves both. A trained difficulty router improves F1^otb over the best single mode by 20.4% on average but still trails an oracle router by roughly 15 points. Overthinking-token usage correlates with surface cues rather than difficulty (42 tokens per added irrelevant MCQ distractor, R^2=0.94), and larger Qwen3 models use more thinking tokens without any accuracy gain.

## Limitations

Efficiency-training methods tuned on math generalize poorly to non-math domains (AdaptThink cuts tokens 82% on math but only 37% on non-math). Models show no statistically significant correlation between thinking-token usage and difficulty or accuracy gains. All five tested mitigation strategies trade off one sub-benchmark against the other. Correctness judging for non-math, non-exact-match questions relies on an LLM-as-judge from the same model family used for generation.

## Why it matters here

- **overthinking**: Directly about the topic: introduces a benchmark and metrics that jointly quantify overthinking and underthinking, evaluates 33 models, and tests mitigations. Note: this is the same paper already archived by hand as `local:49199e3b0f694ee1` (identical title/content) -- arXiv/curated-list collection did not get deduplicated against the earlier local filing, so this record is a duplicate rather than new information.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), [underthinking](../../../../wiki/concepts/underthinking.md), [test-time compute scaling](../../../../wiki/concepts/test-time-compute-scaling.md), [thinking-token budget](../../../../wiki/concepts/thinking-token-budget.md), [accuracy-efficiency tradeoff of reasoning length](../../../../wiki/concepts/accuracy-efficiency-tradeoff-of-reasoning-length.md), [hybrid thinking/non-thinking models](../../../../wiki/concepts/hybrid-thinking-non-thinking-models.md), [difficulty-based routing between reasoning modes](../../../../wiki/concepts/difficulty-based-routing-between-reasoning-modes.md)
- **Methods**: OverthinkingBench, UnderthinkingBench, Overthinking-Adjusted Accuracy (OAA), AUC_OAA, F1^otb combined metric, [L1 length-controlled reinforcement learning](../../../../wiki/methods/l1-length-controlled-reinforcement-learning.md), [AdaptThink](../../../../wiki/methods/adaptthink.md), [VeriThinker](../../../../wiki/methods/verithinker.md), [Model Merging](../../../../wiki/methods/model-merging.md), trained difficulty-based router / oracle router
- **Datasets**: MATH (Levels 1-2, for OvT-Math), [SuperGPQA](../../../../wiki/datasets/supergpqa.md), Reasoning Gym, AIME'25, HMMT'25

Tags: `overthinking`, `underthinking`, `reasoning length`, `test-time compute`, `benchmark`, `thinking tokens`, `efficiency`, `chain-of-thought`, `accuracy-efficiency tradeoff`, `duplicate-of-local-49199e3b0f694ee1`

## Abstract

Abstract Thinking LLMs solve complex tasks at the expense of increased compute and overthinking on simpler problems, while non-thinking LLMs are faster and cheaper but underthink on harder reasoning problems. This has led to the development of separate thinking and non-thinking LLM variants, leaving the onus of selecting the optimal model for each query on the end user. In this work, we introduce OptimalThinkingBench, a unified benchmark that jointly evaluates overthinking and underthinking in LLMs and also encourages the development of optimally-thinking models that balance performance and efficiency. Our benchmark comprises two sub-benchmarks: OverthinkingBench, featuring simple general queries in 72 domains along with simple math problems, and UnderthinkingBench, containing 11 challenging reasoning tasks along with tough math problems. Using novel thinking-adjusted accuracy metrics, we perform an extensive evaluation of 33 different thinking and non-thinking models and show that no model is able to optimally think on our benchmark. Thinking models often overthink for hundreds of tokens on the simplest user queries without improving performance. In contrast, large non-thinking models ``underthink'', often falling short of much smaller thinking models. We further explore several methods to encourage optimal thinking, but find that these approaches often improve on one sub-benchmark at the expense of the other, highlighting the need for better unified and optimal models in the future.

---

Record id: `title:441c8494292f11c7`
