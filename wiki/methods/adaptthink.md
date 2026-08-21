# AdaptThink

<!-- auto:begin -->

A length-based reward-shaping reinforcement-learning method for controlling reasoning length. OptimalThinkingBench tests it as one of five overthinking mitigations, where it cuts thinking tokens on math questions by up to 82% but only 37% on non-math questions, and is noted as the one tested method that improves both the over- and under-thinking sub-benchmarks together. TRAAC uses it as its strongest RL baseline (40.3% accuracy at 6.8k tokens on AIME/AMC/GPQA-D/BBEH, versus TRAAC's 48.2% at 4.8k tokens).

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [accuracy-efficiency tradeoff of reasoning length](../concepts/accuracy-efficiency-tradeoff-of-reasoning-length.md), [Accuracy-Length Tradeoff](../concepts/accuracy-length-tradeoff.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [AUC_OAA](../concepts/auc-oaa.md), [BBH (Big Bench Hard)](../datasets/bbh-big-bench-hard.md), [DAPO-Math-17k](../datasets/dapo-math-17k.md), [difficulty-based routing between reasoning modes](../concepts/difficulty-based-routing-between-reasoning-modes.md), [DPO_Shortest](dpo-shortest.md), [F1^otb combined metric](../concepts/f1-otb-combined-metric.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO (Group Relative Policy Optimization)](grpo-group-relative-policy-optimization.md), [GSM8K](../datasets/gsm8k.md), [HMMT 2025](../datasets/hmmt-2025.md), [hybrid thinking/non-thinking models](../concepts/hybrid-thinking-non-thinking-models.md), [L1 length-controlled reinforcement learning](l1-length-controlled-reinforcement-learning.md), [LASER](laser.md), [LC-R1](lc-r1.md), [Length Penalty](../concepts/length-penalty.md), [MATH-500](../datasets/math-500.md), [Model Merging](model-merging.md), [NoThinking](nothinking.md), [O1-Pruner](o1-pruner.md), [overthinking](../concepts/overthinking.md), [Overthinking-Adjusted Accuracy (OAA)](../concepts/overthinking-adjusted-accuracy-oaa.md), [OverthinkingBench](../datasets/overthinkingbench.md), [SFT_Shortest](sft-shortest.md), [SuperGPQA](../datasets/supergpqa.md), [test-time compute scaling](../concepts/test-time-compute-scaling.md), [thinking-token budget](../concepts/thinking-token-budget.md), [TokenSkip](tokenskip.md), [trained difficulty-based router / oracle router](../concepts/trained-difficulty-based-router-oracle-router.md), [underthinking](../concepts/underthinking.md), [UnderthinkingBench](../datasets/underthinkingbench.md), [VeriThinker](verithinker.md)

## What we have settled

- **Established** — AdaptThink has an official public code release at github.com/THU-KEG/AdaptThink.
  - Checked the repository directly; it is the paper authors' own implementation of the RL algorithm that lets a reasoning model choose Thinking vs. NoThinking per problem, matching how AdaptThink is described in the archive's sources.

## Appears in

- [OptimalThinkingBench: Evaluating Over and Underthinking in LLMs](../../archive/papers/2025/local-49199e3b0f694ee1/summary.md) — Introduces OptimalThinkingBench, a unified benchmark pairing OverthinkingBench (simple queries) and UnderthinkingBench (hard reasoning/math) with a shared F1 metric, showing that none of 33 evaluated LLMs balances accuracy and thinking-token efficiency.
- [Think Right: Learning to Mitigate Under-Over Thinking via Adaptive, Attentive Compression](../../archive/papers/2025/local-da3fbe3617acc5f8/summary.md) — TRAAC is an online GRPO-based RL method that prunes a reasoning model's chain-of-thought using attention scores from the </think> token and calibrates how aggressively it prunes based on estimated problem difficulty, so it thinks less on easy problems and more on hard ones.
- [OptimalThinkingBench: Evaluating Over and Underthinking in LLMs](../../archive/papers/2026/title-441c8494292f11c7/summary.md) — Introduces OptimalThinkingBench, a unified benchmark pairing OverthinkingBench (simple queries) and UnderthinkingBench (hard reasoning/math) with a shared F1 metric, showing that none of 33 evaluated LLMs balances accuracy and thinking-token efficiency.
- [Stop Unnecessary Reflection: Training LRMs for Efficient Reasoning with Adaptive Reflection and Length Coordinated Penalty](../../archive/papers/2026/title-833de99e9b3ea69d/summary.md) — ARLCP is a reinforcement-learning fine-tuning recipe that adds two coupled reward penalties -- one on reflective steps, one on response length scaled by estimated problem complexity -- to shorten chains of thought in distilled reasoning models without losing accuracy.

## Checked against

- [https://github.com/THU-KEG/AdaptThink](https://github.com/THU-KEG/AdaptThink) — github.com · code · retrieved 2026-08-21
  - _We present AdapThink, a novel reinforcement learning (RL) algorithm that enables reasoning models to adaptively choose between Thinking and NoThinking modes according to the difficulty of each input problem, thereby achieving automatic hybrid reasoning._

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
