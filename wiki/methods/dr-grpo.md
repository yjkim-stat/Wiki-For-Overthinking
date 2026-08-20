# Dr. GRPO

<!-- auto:begin -->

One of a family of published modifications to GRPO -- alongside DAPO, GSPO, CISPO and SAPO -- that address reward sparsity and length bias through changes to the optimisation procedure: reward normalisation, sample filtering, soft advantage computation. The three sources here all use it as a comparator rather than describing it, and the useful thing they establish is where that family of fixes stops. One shows these variants address symptoms of a weighting imbalance without replacing the underlying objective geometry, and derives that geometry instead. Another compares standard GRPO given a bounded reciprocal reward mapping against these variants each given the naive unbounded reward, and finds the reward-level fix ahead -- arguing that when the underlying reward is continuous and unbounded, modifying the optimiser does not repair the signal it is fed. The third uses it among the routing baselines for subjective tasks. The archive's reading is that optimisation-level and reward-level remedies are not substitutes, and that a paper reporting one should be asked whether it tried the other.

- **Kind**: method
- **Also called**: Dr.GRPO
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [credit assignment](../concepts/credit-assignment.md), [DAPO](dapo.md), [DeepSeek-V3.2](../models/deepseek-v3-2.md), [difficulty stratification](difficulty-stratification.md), [ETTh1](../datasets/etth1.md), [ETTh2](../datasets/etth2.md), [ETTm1](../datasets/ettm1.md), [ETTm2](../datasets/ettm2.md), [exponential tilting](exponential-tilting.md), [GPQA](../datasets/gpqa.md), [GPT-5.5](../models/gpt-5-5.md), [group-relative advantage](../concepts/group-relative-advantage.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [GSPO](gspo.md), [length control](../concepts/length-control.md), [length penalty](length-penalty.md), [LLM-as-a-judge](llm-as-a-judge.md), [majority voting](majority-voting.md), [MaxRL](maxrl.md), [MMLU](../datasets/mmlu.md), [on-policy distillation](on-policy-distillation.md), [out-of-distribution generalization](../concepts/out-of-distribution-generalization.md), [outcome reward](../concepts/outcome-reward.md), [persona conditioning](persona-conditioning.md), [post-hoc rationalization](../concepts/post-hoc-rationalization.md), [PPO](ppo.md), [prompt sensitivity](../concepts/prompt-sensitivity.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [reasoning collapse](../concepts/reasoning-collapse.md), [REINFORCE](reinforce.md), [retrieval-augmented generation](retrieval-augmented-generation.md), [reward hacking](../concepts/reward-hacking.md), [reward shaping](reward-shaping.md), [RLVR](rlvr.md), [self-consistency](self-consistency.md), [supervised fine-tuning](supervised-fine-tuning.md), [test-time scaling](../concepts/test-time-scaling.md), [TimesFM](../models/timesfm.md), [Traffic](../datasets/traffic.md), [verifiable reward](../concepts/verifiable-reward.md), [Weather](../datasets/weather.md), [zero-advantage group](../concepts/zero-advantage-group.md)

## Appears in

- [LLM Reasoning for Subjective Tasks: Failure Modes, Mitigation, and Dynamic Reasoning Routing](../../archive/papers/2026/arxiv-2608-08889/summary.md) — Shows on four internal Netflix verification tasks that explicit reasoning usually degrades subjective judgement, that applying RLVR to fix it makes the policy abandon deliberation for short heuristic guessing, and that a length bonus gated on answer correctness is what stops the collapse.
- [SoftmaxGRPO: Learning to Reason using Softmax Advantage Group Estimation](../../archive/papers/2026/arxiv-2608-09271/summary.md) — Replaces GRPO's z-score group normalisation with a temperature-scaled softmax over rewards, which keeps the induced prompt-difficulty weighting bounded as pass probability approaches one and turns the temperature into a dial between REINFORCE and maximum-likelihood weighting.
- [REATS: LLM Reasoning-based Ensemble Learning for Adaptive Time Series Forecasting](../../archive/papers/2026/arxiv-2608-10149/summary.md) — Fine-tunes a 1.7B model to read structured summaries of a time series and allocate ensemble weights across candidate forecasters, trained by SFT on rule-generated chains of thought and then by GRPO with a bounded reciprocal reward that keeps a continuous error gap from collapsing the group advantage.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
