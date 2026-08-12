# DPO

<!-- auto:begin -->

Direct Preference Optimization, used in this archive as the middle stage of efficiency pipelines rather than for alignment. The pattern in both sources is the same: sample multiple trajectories for a question, keep only those reaching the correct answer, rank them by a redundancy or confidence score, and prefer the leaner one — so the preference signal is constructed from the model's own outputs and carries no human judgement. One ranks correct trajectories by a score combining the fraction of review nodes in a dependency graph with normalized length; the other feeds the model's own self-certainty into the preference so it compresses where it is confident and keeps deliberating where it is not. In both it sits between supervised fine-tuning on pruned traces and a length-penalized reinforcement stage, and in at least one the stage-wise ablation shows it contributes less of the final compression than the stage after it.

- **Kind**: method
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AMC23](../datasets/amc23.md), [best-of-n](best-of-n.md), [chain-of-thought compression](chain-of-thought-compression.md), [credit assignment](../concepts/credit-assignment.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [length penalty](length-penalty.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [majority voting](majority-voting.md), [MATH500](../datasets/math500.md), [Monte Carlo tree search](monte-carlo-tree-search.md), [OlympiadBench](../datasets/olympiadbench.md), [overthinking](../concepts/overthinking.md), [preference optimization](preference-optimization.md), [process reward model](process-reward-model.md), [process supervision](../concepts/process-supervision.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [reasoning skeleton](../concepts/reasoning-skeleton.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [self-consistency](self-consistency.md), [self-correction](../concepts/self-correction.md), [supervised fine-tuning](supervised-fine-tuning.md), [supervised finetuning](supervised-finetuning.md), [TokenSkip](tokenskip.md), [verification](../concepts/verification.md)

## Appears in

- [Cloud-ScPO: Hidden-State Geometry for Semi-Supervised Preference Optimization in LLM Reasoning](../../archive/papers/2026/arxiv-2608-01014/summary.md) — Scores unlabeled reasoning trajectories by how their mean-pooled hidden states connect to correct and incorrect reference point clouds built from a small labeled set, and uses that score to pick the concrete chosen and rejected responses inside answer clusters that self-consistency has already separated.
- [Free Process Rewards without Process Labels](../../archive/papers/2024/local-b1536fcbe72cb268/summary.md) — Proves that parameterizing an outcome reward as the log-likelihood ratio between a policy and a reference model makes the per-step Q value fall out of the same model for free, so a process reward model can be obtained by training an outcome reward model on response-level labels alone.
- [Graph-Based Chain-of-Thought Pruning for Reducing Redundant Reflections in Reasoning LLMs](../../archive/papers/2026/local-d3ff7e5088463145/summary.md) — Turns a linear chain of thought into a dependency DAG, labels each node as advancing the frontier or reviewing it, and prunes review nodes on two graph criteria — too few descendants, or too late in the trace — cutting 42% of tokens while accuracy holds or rises.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
