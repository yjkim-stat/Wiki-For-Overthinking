# MaxRL

<!-- auto:begin -->

A policy-optimisation objective whose induced prompt weighting is (1-(1-p)^T)/p at truncation T -- a truncated version of maximum-likelihood's 1/p weighting, which caps the blow-up on very hard prompts that pure 1/p produces. Both sources locate it inside a family rather than treating it as a standalone method. One derives it as an exact limit: softmax group advantages at low temperature and finite group size M reduce precisely to MaxRL with truncation M-1, so a temperature dial interpolates REINFORCE to MaxRL and then to 1/p weighting as M grows. The other places it in a moment hierarchy, showing that REINFORCE, pass@K training and MaxRL each optimise a single moment of the per-problem failure probability, and that minimising the first T moments jointly is exactly minimising the expected truncated number of rollouts to a first success -- with MaxRL scoring 33.8 and 43.5 average against that method's 34.7 and 47.6 at two scales. What the archive should carry is that these objectives differ only in how they weight prompts by difficulty, and that the weighting is derivable rather than a matter of taste.

- **Kind**: method
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [credit assignment](../concepts/credit-assignment.md), [DAPO](dapo.md), [difficulty stratification](difficulty-stratification.md), [Dr. GRPO](dr-grpo.md), [exploration](../concepts/exploration.md), [exponential tilting](exponential-tilting.md), [GPQA](../datasets/gpqa.md), [group-relative advantage](../concepts/group-relative-advantage.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [on-policy distillation](on-policy-distillation.md), [pass@k](../concepts/pass-k.md), [PPO](ppo.md), [prompt difficulty](../concepts/prompt-difficulty.md), [Qwen3-1.7B-Base](../models/qwen3-1-7b-base.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [reasoning boundary](../concepts/reasoning-boundary.md), [REINFORCE](reinforce.md), [supervised fine-tuning](supervised-fine-tuning.md), [verifiable reward](../concepts/verifiable-reward.md), [zero-advantage group](../concepts/zero-advantage-group.md)

## Appears in

- [Beyond the Mean: Multi-Moment Policy Optimization for LLM Reasoning](../../archive/papers/2026/arxiv-2608-02149/summary.md) — Treats a policy's per-problem failure probability as a random variable over the problem distribution and shows that REINFORCE, pass@K training and MaxRL each optimize a single moment of it, then proposes minimizing the first T moments jointly — which is exactly minimizing the expected truncated number of rollouts needed to reach a first success.
- [SoftmaxGRPO: Learning to Reason using Softmax Advantage Group Estimation](../../archive/papers/2026/arxiv-2608-09271/summary.md) — Replaces GRPO's z-score group normalisation with a temperature-scaled softmax over rewards, which keeps the induced prompt-difficulty weighting bounded as pass probability approaches one and turns the temperature into a dial between REINFORCE and maximum-likelihood weighting.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
