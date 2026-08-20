# Dr. GRPO

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Also called**: Dr.GRPO
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [credit assignment](../concepts/credit-assignment.md), [DAPO](dapo.md), [difficulty stratification](difficulty-stratification.md), [GPQA](../datasets/gpqa.md), [group-relative advantage](../concepts/group-relative-advantage.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [GSPO](gspo.md), [length control](length-control.md), [length penalty](length-penalty.md), [LLM-as-a-judge](llm-as-a-judge.md), [majority voting](majority-voting.md), [MaxRL](maxrl.md), [MMLU](../datasets/mmlu.md), [on-policy distillation](on-policy-distillation.md), [outcome reward](../concepts/outcome-reward.md), [persona conditioning](persona-conditioning.md), [PPO](ppo.md), [prompt sensitivity](../concepts/prompt-sensitivity.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [reasoning collapse](../concepts/reasoning-collapse.md), [REINFORCE](reinforce.md), [reward hacking](../concepts/reward-hacking.md), [reward shaping](../concepts/reward-shaping.md), [RLVR](rlvr.md), [self-consistency](self-consistency.md), [supervised fine-tuning](supervised-fine-tuning.md), [test-time scaling](../concepts/test-time-scaling.md), [verifiable reward](../concepts/verifiable-reward.md), [zero-advantage group](../concepts/zero-advantage-group.md)

## Appears in

- [LLM Reasoning for Subjective Tasks: Failure Modes, Mitigation, and Dynamic Reasoning Routing](../../archive/papers/2026/arxiv-2608-08889/summary.md) — Shows on four internal Netflix verification tasks that explicit reasoning usually degrades subjective judgement, that applying RLVR to fix it makes the policy abandon deliberation for short heuristic guessing, and that a length bonus gated on answer correctness is what stops the collapse.
- [SoftmaxGRPO: Learning to Reason using Softmax Advantage Group Estimation](../../archive/papers/2026/arxiv-2608-09271/summary.md) — Replaces GRPO's z-score group normalisation with a temperature-scaled softmax over rewards, which keeps the induced prompt-difficulty weighting bounded as pass probability approaches one and turns the temperature into a dial between REINFORCE and maximum-likelihood weighting.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
