# Process Reward Model (PRM)

<!-- auto:begin -->

A reward model that scores the intermediate steps of a reasoning trace, not just the final answer, used to guide test-time search (pruning bad branches, expanding promising ones) rather than only to rank complete solutions. 'What If We Allocate Test-Time Compute Adaptively?' replaces uniform compute allocation with PRM-guided pruning/expansion; TaTToo trains a table-grounded, tool-verified PRM specifically for tabular reasoning search. Note: same concept as the archive's separately-tracked 'process reward model' entry -- not merged.

- **Kind**: concept
- **Also called**: PRM, Process Reward Model (PRM), process reward model, process reward model (PRM)
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AMC23](../datasets/amc23.md), [ASDiv](../datasets/asdiv.md), [GSM8K](../datasets/gsm8k.md), [LLaMA-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [LLaMA-3-8B-Instruct](../models/llama-3-8b-instruct.md), [MATH500](../datasets/math500.md), [Monte Carlo Tree Search](../methods/monte-carlo-tree-search.md), [process reward model](../methods/process-reward-model.md), [Qwen2.5-Math-1.5B-Instruct](../models/qwen2-5-math-1-5b-instruct.md)

## Appears in

- [A Reward-Guided Dual-Phase Framework for Adaptive Inference-Time Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-511/summary.md) — DREAM decomposes tree-based test-time search into separate planning and execution phases, each with its own reward model and adaptive per-step budget allocation, improving the accuracy-tokens tradeoff over standard beam search and majority voting on math reasoning and code generation.
- [What If We Allocate Test-Time Compute Adaptively?](../../archive/papers/2026/title-892443a8a7093b83/summary.md) — Replaces uniform test-time compute allocation with a process-reward-model-guided framework that adaptively prunes, expands and selects reasoning trajectories per problem.
- [TaTToo: Tool-Grounded Thinking PRM for Test-Time Scaling in Tabular Reasoning](../../archive/papers/2026/title-983af40bdcebe387/summary.md) — TaTToo is a table-grounded Process Reward Model that reasons explicitly over tabular operations and uses tool-based verification to supervise test-time scaling for tabular reasoning, improving downstream policy LRMs by 30.9% at inference.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
