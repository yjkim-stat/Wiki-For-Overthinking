# reinforcement learning fine-tuning

<!-- auto:begin -->

Further training an already-pretrained reasoning model with reinforcement learning (typically against a verifiable reward, such as answer correctness) to change its reasoning behavior. In the archive it appears both as a general training stage whose data selection can be made more efficient by predicting which prompts are informative (Dynamics-Predictive Sampling), and as a cause worth scrutinizing: 'Reasoning or Retrieval?' studies how it shifts a model's answers between chain-of-thought reasoning and a memory-retrieval shortcut.

- **Kind**: concept
- **Also called**: RL finetuning, RLVR, reinforcement learning finetuning
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Bayesian inference](bayesian-inference.md), [Preference Optimization](../methods/preference-optimization.md), [Test-Time Compute Scaling](test-time-compute-scaling.md)

## Appears in

- Dynamics-Predictive Sampling for Active RL Finetuning of Large Reasoning Models — Selects which training prompts to use for RL finetuning of large reasoning models by predicting their learning dynamics with a hidden Markov model, instead of evaluating every candidate with rollouts.
- Reasoning or Retrieval? A Study of Answer Attribution on Large Reasoning Models — Shows that large reasoning models' final answers are produced by two competing mechanisms, chain-of-thought reasoning and memory retrieval, and introduces FARL, a fine-tuning method that suppresses the retrieval shortcut to encourage genuine reasoning.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
