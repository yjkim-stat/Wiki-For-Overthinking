# Bayesian inference

<!-- auto:begin -->

A statistical framework for updating a belief (e.g. a prediction of prompt difficulty, or of how useful a training example will be) from prior assumptions plus observed evidence. In the archived sources it appears as the tool behind two training-efficiency methods: predicting which RL training prompts are informative from partial reward history, and a small, prompt-generic Bayesian predictor of prompt difficulty learned from shared optimization history, used to select prompts for efficient RL post-training of reasoning models.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [reinforcement learning fine-tuning](reinforcement-learning-fine-tuning.md)

## Appears in

- Dynamics-Predictive Sampling for Active RL Finetuning of Large Reasoning Models — Selects which training prompts to use for RL finetuning of large reasoning models by predicting their learning dynamics with a hidden Markov model, instead of evaluating every candidate with rollouts.
- Small Generalizable Prompt Predictive Models Can Steer Efficient RL Post-Training of Large Reasoning Models — Trains a small, prompt-generic Bayesian predictor of prompt difficulty from shared RL optimization history to select informative training prompts and reduce rollout cost when RL-training large reasoning models.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
