# group-relative advantage

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [advantage estimation](advantage-estimation.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [credit assignment](credit-assignment.md), [DAPO](../methods/dapo.md), [data efficiency](data-efficiency.md), [difficulty stratification](../methods/difficulty-stratification.md), [Dr. GRPO](../methods/dr-grpo.md), [exponential tilting](../methods/exponential-tilting.md), [GiGPO](../methods/gigpo.md), [GPQA](../datasets/gpqa.md), [GPT-5.5](../models/gpt-5-5.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [HumanEval+](../datasets/humaneval.md), [Kimi-K2.6](../models/kimi-k2-6.md), [LiveCodeBench](../datasets/livecodebench.md), [long-horizon agency](long-horizon-agency.md), [MaxRL](../methods/maxrl.md), [MBPP+](../datasets/mbpp.md), [MMLU](../datasets/mmlu.md), [on-policy distillation](../methods/on-policy-distillation.md), [outcome reward](outcome-reward.md), [PPO](../methods/ppo.md), [prompt difficulty](prompt-difficulty.md), [Qwen2.5-Coder-7B](../models/qwen2-5-coder-7b.md), [Qwen3.5-4B](../models/qwen3-5-4b.md), [Qwen3.6-27B](../models/qwen3-6-27b.md), [REINFORCE](../methods/reinforce.md), [rejection sampling](../methods/rejection-sampling.md), [Skywork-OR1](../models/skywork-or1.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [verifiable reward](verifiable-reward.md), [zero-advantage group](zero-advantage-group.md)

## Appears in

- [DiDPO: Diff-in-Diff Policy Optimization for Coding Agent Training](../../archive/papers/2026/arxiv-2608-07147/summary.md) — Assigns credit in coding-agent RL by splitting each code diff into sub-diffs, matching semantically similar sub-diffs across rollouts to form advantage groups, and projecting the resulting diff-level advantage back onto the tokens that produced it.
- [SoftmaxGRPO: Learning to Reason using Softmax Advantage Group Estimation](../../archive/papers/2026/arxiv-2608-09271/summary.md) — Replaces GRPO's z-score group normalisation with a temperature-scaled softmax over rewards, which keeps the induced prompt-difficulty weighting bounded as pass probability approaches one and turns the temperature into a dial between REINFORCE and maximum-likelihood weighting.
- [Miner: Mining Intrinsic Mastery for Data-Efficient RL in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-237/summary.md) — Addresses wasted rollouts in critic-free RL on prompts where every sampled rollout is already correct and the advantage estimate is therefore zero.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
