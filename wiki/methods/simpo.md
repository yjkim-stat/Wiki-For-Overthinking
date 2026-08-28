# SimPO

<!-- auto:begin -->

SimPO is a preference-optimisation objective used in the archive as an alternative to DPO when training reasoning models toward shorter correct traces. Its relevance here is a documented failure mode rather than its formulation: ChainPrune reports that in the short-chosen setting, where the preferred and rejected responses are sampled from the same reference model and differ mainly in length, the narrow distribution and small edit distance between them lead margin-based objectives including SimPO and DPO into reward synchronization collapse -- rather than raising the preferred response relative to the rejected one, the model lowers the probability of both, degrading performance across benchmarks. ChainPrune attributes this to gradient entanglement and counters it with an added negative-log-likelihood term, which on identical training data lifts DAST's AIME24 accuracy from 0.5375 under SimPO to 0.5833.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [DAST](dast.md), [DeepScaleR](../datasets/deepscaler.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-0528-Qwen3-8B](../models/deepseek-r1-0528-qwen3-8b.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [Direct Preference Optimization (DPO)](direct-preference-optimization-dpo.md), [GPT-o1](../models/gpt-o1.md), [LLM-as-a-Judge](llm-as-a-judge.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [Overthinking](../concepts/overthinking.md), [Redundant Reasoning Steps](../concepts/redundant-reasoning-steps.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [Token Budget](../concepts/token-budget.md)

## Appears in

- [ChainPrune: Evaluating and Reducing Redundancy in Long Chain-of-Thought Reasoning](../../archive/papers/2026/arxiv-2608-21860/summary.md) — ChainPrune merges semantically equivalent steps from 16 sampled reasoning paths into a tree, picks Pareto-dominant short paths as DPO preference data, and fine-tunes with an added NLL term, cutting tokens 28.1% and reasoning steps 26.8% on two R1-distilled models without losing accuracy.
- [CiPO: Counterfactual Unlearning for Large Reasoning Models through Iterative Preference Optimization](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-143/summary.md) — CiPO reframes unlearning for large reasoning models as counterfactual intervention on the chain-of-thought: it has the target model generate a logically valid counterfactual reasoning trace and answer, then iteratively preference-optimizes the model toward that counterfactual (SimPO loss against online-sampled dispreferred responses), removing sensitive knowledge from both intermediate CoT and final answers while preserving reasoning ability better than prior unlearning baselines.
- [How Far Are We from Optimal Reasoning Efficiency?](../../archive/papers/2025/title-279ee92c27a8bb8d/summary.md) — Defines an empirical accuracy-vs-token-budget frontier for a fixed base reasoning model, measures how far existing efficiency methods fall short of it with a single metric (REG), and proposes REO-RL, an RL objective that targets a handful of token budgets to close most of that gap.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
