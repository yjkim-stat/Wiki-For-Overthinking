# StrategyQA

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: dataset
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [abstention](../concepts/abstention.md), [ARC-Challenge](arc-challenge.md), [calibration](../methods/calibration.md), [chain of thought](../methods/chain-of-thought.md), [CommonsenseQA](commonsenseqa.md), [component ablation](../methods/component-ablation.md), [coverage](../concepts/coverage.md), [difficulty conditioning](../concepts/difficulty-conditioning.md), [difficulty stratification](../methods/difficulty-stratification.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [hallucination](../concepts/hallucination.md), [Llama-3.1-70B](../models/llama-3-1-70b.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [Llama-3.2-3B](../models/llama-3-2-3b.md), [MATH](math.md), [MMLU](mmlu.md), [Monte Carlo tree search](../methods/monte-carlo-tree-search.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [QwQ-32B](../models/qwq-32b.md), [reasoning boundary](../concepts/reasoning-boundary.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [reward shaping](../concepts/reward-shaping.md), [selective prediction](../concepts/selective-prediction.md), [self-correction](../concepts/self-correction.md), [self-reflection](../methods/self-reflection.md), [structured chain of thought](../methods/structured-chain-of-thought.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [t-SNE](../methods/t-sne.md)

## Appears in

- [REIN: Bridging the Gap between Reasoning and Reliability via Reflection and Abstention Alignment](../../archive/papers/2026/arxiv-2608-07931/summary.md) — Separates hallucination into a reasoning failure and a knowledge failure, treats the first with a structured reflect-before-answering format and the second with a reward for abstaining when no sampled chain succeeds, and shows the two mechanisms are not interchangeable -- reflection alone never abstains, abstention alone never lowers the hallucination proxy.
- [Landscape of Thoughts: Visualizing the Reasoning Process of Large Language Models](../../archive/papers/2026/local-1b977d02353e100b/summary.md) — Turns each intermediate step of a reasoning trajectory into a numerical feature vector of distances to the answer choices, projects those into 2D to visualize how trajectories move through answer space, and reuses the same features to build a lightweight verifier for weighted voting.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
