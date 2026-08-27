# Bayesian inference

<!-- auto:begin -->

A statistical framework for updating a belief (e.g. a prediction of prompt difficulty, or of how useful a training example will be) from prior assumptions plus observed evidence. In the archived sources it appears as the tool behind two training-efficiency methods: predicting which RL training prompts are informative from partial reward history, and a small, prompt-generic Bayesian predictor of prompt difficulty learned from shared optimization history, used to select prompts for efficient RL post-training of reasoning models.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

## Appears in

- [Dynamics-Predictive Sampling for Active RL Finetuning of Large Reasoning Models](../../archive/papers/2026/title-0af2f5eb8565eb12/summary.md) — Dynamics-Predictive Sampling (DPS) forecasts, from a hidden-Markov model of each prompt's historical reward trajectory, which prompts are worth including in RL fine-tuning of large reasoning models before running any rollouts, cutting wasted rollouts and speeding up training.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
