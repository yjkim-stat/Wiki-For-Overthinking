<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# OptimalThinkingBench: Evaluating Over and Underthinking in LLMs

- **Authors**: Pranjal Aggarwal, Seungone Kim, Jack Lanchantin, Sean Welleck, Jason Weston, Ilia Kulikov, Swarnadeep Saha
- **Venue**: ICLR 2026
- **Published**: 2025-01-01
- **Source**: local+virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10009890>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

Introduces OptimalThinkingBench, a unified benchmark pairing OverthinkingBench (simple queries) and UnderthinkingBench (hard reasoning/math) with a shared F1 metric, showing that none of 33 evaluated LLMs balances accuracy and thinking-token efficiency.

## Problem

Thinking LLMs overthink simple queries, generating hundreds of tokens without improving (and sometimes hurting) accuracy, while non-thinking LLMs underthink on harder reasoning problems and fall short of much smaller thinking models. Model providers ship separate thinking and non-thinking variants, forcing end users to manually pick the right one per query rather than having a single model that adapts its reasoning length to task difficulty.

## Contributions

- Introduces OptimalThinkingBench, a single unified benchmark combining OverthinkingBench (simple queries across 72 domains, 4 answer types) and UnderthinkingBench (11 reasoning task types plus AIME'25/HMMT'25 math) with standardized metrics (OAA, AUC_OAA, F1^otb) for jointly measuring overthinking and underthinking.
- Comprehensive evaluation of 33 open and closed thinking, non-thinking, and hybrid LLMs showing that no current model optimally balances accuracy and thinking-token efficiency.
- Explores and compares training-time (reward shaping, model merging, verification training) and test-time (routing, prompting) methods for optimal thinking, showing most improve one sub-benchmark at the expense of the other.

## Method

OptimalThinkingBench has two sub-benchmarks. OverthinkingBench is built via constrained synthetic generation with Llama-4-Maverick across 72 domains and 4 answer types (numeric, MCQ, short-answer, open-ended), then filtered by requiring 8/8 agreement across independently sampled LLM responses (judged by an LLM-as-judge) so only unambiguous, easy questions survive (1327 OvT-General questions plus 133 OvT-Math questions from MATH levels 1-2). Overthinking is scored with Overthinking-Adjusted Accuracy (OAA_t): accuracy counted only for responses under a thinking-token threshold t, aggregated as AUC_OAA (area under the OAA_t curve up to t_max=1000). UnderthinkingBench draws on 11 Reasoning Gym task types (games, algorithms, graphs, arithmetic, geometry, logic) plus AIME'25 and HMMT'25 math, keeping only tasks where a small thinking model (Qwen3-1.7B) outperforms a much larger non-thinking model (Qwen3-235B-A22B) by a margin, so the tasks genuinely require deliberate reasoning; scored with task-specific programmatic verifiers (code execution for reasoning tasks, math-verify for math). The two are combined into a single F1^otb score (harmonic mean of AUC_OAA and UnderthinkingBench accuracy), so a model must do well on both to score high. The authors evaluate 33 open and closed thinking/non-thinking/hybrid models and test five mitigation strategies: length-based reward shaping (L1, AdaptThink), model merging, auxiliary verification training (VeriThinker), difficulty-based routing between thinking/non-thinking modes (trained router vs. oracle router), and explicit prompting ('Don't Overthink' vs. 'Let's think step-by-step').

## Results

No model optimally balances both sub-benchmarks. o3 gets the best overall F1^otb (71.1%); best open-weight model is GPT-OSS-120B (68.3%), a 3-point gap. On OverthinkingBench, thinking models generate at least ~100-3300+ thinking tokens on trivially simple questions (e.g. Magistral-Small uses >3300 tokens), driving AUC_OAA far below raw accuracy; non-thinking models score near their raw accuracy (e.g. Sonnet-4 non-thinking: 97.4% accuracy, 97.4 AUC_OAA). On UnderthinkingBench, thinking models substantially outperform non-thinking ones: o3 leads at 65.0% accuracy, GPT-OSS-120B at 57.9%; Qwen3 hybrid models score <=20% accuracy in non-thinking mode but jump sharply in thinking mode (e.g. Qwen3-14B: 14.0% to 52.4%, a 38.4-point gain). Mitigation methods (L1, AdaptThink, VeriThinker, Model Merging) cut OverthinkingBench token use by 12-91% but degrade UnderthinkingBench accuracy by up to 13% in most tested configurations, with 2 of 6 method-model combinations underperforming their base model on overall F1^otb; AdaptThink is the one method that improves both. A trained difficulty router improves F1^otb over the best single mode by 20.4% on average but still trails an oracle router by roughly 15 points (Qwen3 average: 24.3 standard vs 46.9 trained router vs 61.2 oracle). Prompting 'Don't Overthink' cuts OverthinkingBench tokens by about 23% without hurting accuracy and raises average F1^otb by 7.7 points across Qwen3 models, while 'Let's think step-by-step' increases thinking tokens by about 10% and lowers F1^otb by 8.0 points. Overthinking-token usage correlates with surface cues rather than difficulty: near-linear increase of 42 tokens per added irrelevant MCQ distractor (R^2=0.94), and larger Qwen3 models use more thinking tokens (750 to 950 from 1.7B to 235B) without any accuracy gain (flat around 86.1-86.8% from 8B up).

## Limitations

Efficiency-training methods tuned on math generalize poorly to non-math domains (AdaptThink cuts tokens 82% on math but only 37% on non-math OverthinkingBench questions). Models show no statistically significant correlation between increased thinking-token usage and either domain difficulty or accuracy gains (Spearman rho about -0.46 to 0.29, p>0.05 across the correlations tested), indicating thinking length tracks surface features (STEM keywords, numeric answer format, MCQ option count) rather than genuine task complexity. All five tested mitigation strategies trade off one sub-benchmark against the other, and none closes the gap to an oracle router (best trained router still ~15 points below oracle). Correctness judging for OverthinkingBench's non-math, non-exact-match questions relies on an LLM-as-judge (same model family used for generation and filtering), which is an imperfect proxy for ground truth. The benchmark's own examples show that even average per-domain tokens/accuracy don't capture case-level failures: qualitative analysis finds models often reach the correct answer early in their chain-of-thought and then talk themselves out of it, while non-thinking models underthink by taking the first plausible answer (e.g., claiming to run BFS without actually verifying it) without exploring alternatives.

## Why it matters here

- **overthinking**: The paper is directly about this topic: it introduces a benchmark and metrics (OAA, AUC_OAA, F1^otb) that jointly quantify LLMs thinking more than a problem needs (overthinking, measured via wasted thinking tokens on 1460 simple questions) and thinking less than a problem needs (underthinking, measured via accuracy loss on 610 hard reasoning/math problems), evaluates 33 thinking/non-thinking models on this accuracy-efficiency tradeoff, and tests concrete methods (reward shaping, routing, prompting) for making models stop or keep going at the right point.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), [underthinking](../../../../wiki/concepts/underthinking.md), [test-time compute scaling](../../../../wiki/concepts/test-time-compute-scaling.md), [thinking-token budget](../../../../wiki/concepts/thinking-token-budget.md), [accuracy-efficiency tradeoff of reasoning length](../../../../wiki/concepts/accuracy-efficiency-tradeoff-of-reasoning-length.md), [hybrid thinking/non-thinking models](../../../../wiki/concepts/hybrid-thinking-non-thinking-models.md), [difficulty-based routing between reasoning modes](../../../../wiki/concepts/difficulty-based-routing-between-reasoning-modes.md)
- **Methods**: OverthinkingBench, UnderthinkingBench, Overthinking-Adjusted Accuracy (OAA), AUC_OAA, F1^otb combined metric, LLM-as-a-judge filtering and evaluation, [L1 length-controlled reinforcement learning](../../../../wiki/methods/l1-length-controlled-reinforcement-learning.md), [AdaptThink](../../../../wiki/methods/adaptthink.md), [VeriThinker](../../../../wiki/methods/verithinker.md), [Model Merging](../../../../wiki/methods/model-merging.md), trained difficulty-based router / oracle router
- **Datasets**: MATH (Hendrycks et al., Levels 1-2, for OvT-Math), SuperGPQA (72-domain source for OvT-General question generation), Reasoning Gym (11 reasoning task types for UnderthinkingBench), [AIME'25](../../../../wiki/datasets/aime-2025.md), HMMT'25

Tags: `overthinking`, `underthinking`, `reasoning length`, `test-time compute`, `benchmark`, `thinking tokens`, `efficiency`, `chain-of-thought`, `accuracy-efficiency tradeoff`

## Abstract

Abstract Thinking LLMs solve complex tasks at the expense of increased compute and overthinking on simpler problems, while non-thinking LLMs are faster and cheaper but underthink on harder reasoning problems. This has led to the development of separate thinking and non-thinking LLM variants, leaving the onus of selecting the optimal model for each query on the end user. In this work, we introduce OptimalThinkingBench, a unified benchmark that jointly evaluates overthinking and underthinking in LLMs and also encourages the development of optimally-thinking models that balance performance and efficiency. Our benchmark comprises two sub-benchmarks: OverthinkingBench, featuring simple general queries in 72 domains along with simple math problems, and UnderthinkingBench, containing 11 challenging reasoning tasks along with tough math problems. Using novel thinking-adjusted accuracy metrics, we perform an extensive evaluation of 33 different thinking and non-thinking models and show that no model is able to optimally think on our benchmark. Thinking models often overthink for hundreds of tokens on the simplest user queries without improving performance. In contrast, large non-thinking models ``underthink'', often falling short of much smaller thinking models. We further explore several methods to encourage optimal thinking, but find that these approaches often improve on one sub-benchmark at the expense of the other, highlighting the need for better unified and optimal models in the future.

---

Record id: `local:49199e3b0f694ee1`
