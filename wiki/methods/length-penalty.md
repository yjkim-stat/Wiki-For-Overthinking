# length penalty

<!-- auto:begin -->

A negative reward term proportional to output length, and across 3 sources a shaping choice whose form matters more than its presence. The archive's measured comparison: an unconstrained length reward is exploited outright with accuracy collapsing; a bounded penalty pulling toward a target converges the length and produces useless filler; and only a form gated on the answer being correct converts the saved or preserved length into accuracy. Two refinements from the corpus: applying the penalty only to correct trajectories, and measuring it as excess over the shortest correct sample for that question rather than against a global target; and one source's attribution problem, where a stage-wise ablation shows most of its headline compression arriving with the penalised reinforcement stage rather than with the pruning criteria the paper is about.

- **Kind**: method
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [answer stabilization](../concepts/answer-stabilization.md), [chain-of-thought compression](chain-of-thought-compression.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [credit assignment](../concepts/credit-assignment.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DPO](dpo.md), [Dr. GRPO](dr-grpo.md), [early exit](early-exit.md), [gpt-oss-20b](../models/gpt-oss-20b.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [GSPO](gspo.md), [length control](../concepts/length-control.md), [LLM-as-a-judge](llm-as-a-judge.md), [majority voting](majority-voting.md), [MATH500](../datasets/math500.md), [OlympiadBench](../datasets/olympiadbench.md), [Omni-MATH](../datasets/omni-math.md), [optimal stopping](optimal-stopping.md), [outcome reward](../concepts/outcome-reward.md), [overthinking](../concepts/overthinking.md), [persona conditioning](persona-conditioning.md), [prompt difficulty](../concepts/prompt-difficulty.md), [prompt sensitivity](../concepts/prompt-sensitivity.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [reasoning collapse](../concepts/reasoning-collapse.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [reasoning skeleton](../concepts/reasoning-skeleton.md), [reinforcement learning](reinforcement-learning.md), [reward hacking](../concepts/reward-hacking.md), [reward shaping](reward-shaping.md), [RLVR](rlvr.md), [self-consistency](self-consistency.md), [self-correction](../concepts/self-correction.md), [supervised fine-tuning](supervised-fine-tuning.md), [test-time scaling](../concepts/test-time-scaling.md), [TokenSkip](tokenskip.md)

## Appears in

- [LLM Reasoning for Subjective Tasks: Failure Modes, Mitigation, and Dynamic Reasoning Routing](../../archive/papers/2026/arxiv-2608-08889/summary.md) — Shows on four internal Netflix verification tasks that explicit reasoning usually degrades subjective judgement, that applying RLVR to fix it makes the policy abandon deliberation for short heuristic guessing, and that a length bonus gated on answer correctness is what stops the collapse.
- [Graph-Based Chain-of-Thought Pruning for Reducing Redundant Reflections in Reasoning LLMs](../../archive/papers/2026/local-d3ff7e5088463145/summary.md) — Turns a linear chain of thought into a dependency DAG, labels each node as advancing the frontier or reviewing it, and prunes review nodes on two graph criteria — too few descendants, or too late in the trace — cutting 42% of tokens while accuracy holds or rises.
- [OS-Pruner: Pruning Chains-of-Thought of Reasoning Models via Optimal Stopping](../../archive/papers/2026/local-dbfa51b5159a1a77/summary.md) — Recasts when-to-stop-reasoning as optimal stopping rather than classification, and proves that a fixed threshold on the probability of being correct can be arbitrarily far from optimal even when that probability is known exactly, because the decision needs the value of continuing and not the value of stopping.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
