# length penalty

<!-- auto:begin -->

A term added to a reinforcement learning objective that charges a trajectory for its length, and the most common lever in this archive's efficiency work. The sources agree it works and disagree about how to apply it safely. Applying it at sequence level couples efficiency to correctness, so long but correct trajectories are punished and the reasoning the penalty was meant to trim is damaged — two sources respond by decoupling the two rewards at token level or by applying the penalty only to correct trajectories, measured as excess over the shortest correct sample for that question rather than in absolute tokens. One source modulates it by difficulty, on the argument that a uniform penalty asks easy and hard problems for the same brevity. Attribution is the recurring difficulty: in a pipeline combining pruned supervision, preference optimization and a length-penalized RL stage, most of the compression arrives with the penalty, which makes it hard to credit the pruning criterion that preceded it. A separate result bounds what the lever can achieve — a model already trained with a heavy length penalty still yields large further reduction under an inference-time stopping policy, so penalized training does not exhaust the redundancy.

- **Kind**: method
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AMC23](../datasets/amc23.md), [answer stabilization](../concepts/answer-stabilization.md), [chain-of-thought compression](chain-of-thought-compression.md), [DAPO-Math-17k](../datasets/dapo-math-17k.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DPO](dpo.md), [early exit](early-exit.md), [GPT-OSS-20B](../models/gpt-oss-20b.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [MATH500](../datasets/math500.md), [OlympiadBench](../datasets/olympiadbench.md), [Omni-MATH](../datasets/omni-math.md), [optimal stopping](../concepts/optimal-stopping.md), [overthinking](../concepts/overthinking.md), [prompt difficulty](../concepts/prompt-difficulty.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [reasoning skeleton](../concepts/reasoning-skeleton.md), [self-correction](../concepts/self-correction.md), [supervised finetuning](supervised-finetuning.md), [TokenSkip](tokenskip.md)

## Appears in

- [Graph-Based Chain-of-Thought Pruning for Reducing Redundant Reflections in Reasoning LLMs](../../archive/papers/2026/local-d3ff7e5088463145/summary.md) — Turns a linear chain of thought into a dependency DAG, labels each node as advancing the frontier or reviewing it, and prunes review nodes on two graph criteria — too few descendants, or too late in the trace — cutting 42% of tokens while accuracy holds or rises.
- [OS-Pruner: Pruning Chains-of-Thought of Reasoning Models via Optimal Stopping](../../archive/papers/2026/local-dbfa51b5159a1a77/summary.md) — Recasts when-to-stop-reasoning as optimal stopping rather than classification, and proves that a fixed threshold on the probability of being correct can be arbitrarily far from optimal even when that probability is known exactly, because the decision needs the value of continuing and not the value of stopping.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
