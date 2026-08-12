# t-SNE

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [activation steering](activation-steering.md), [chain of thought](chain-of-thought.md), [chain of thought distillation](chain-of-thought-distillation.md), [CommonsenseQA](../datasets/commonsenseqa.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [GSM8K](../datasets/gsm8k.md), [linear probe](linear-probe.md), [Llama-3.1-70B](../models/llama-3-1-70b.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [Logit Lens](logit-lens.md), [MATH-500](../datasets/math-500.md), [MMLU](../datasets/mmlu.md), [Monte Carlo tree search](monte-carlo-tree-search.md), [QwQ-32B](../models/qwq-32b.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [self-correction](../concepts/self-correction.md), [test-time scaling](test-time-scaling.md)

## Appears in

- [Landscape of Thoughts: Visualizing the Reasoning Process of Large Language Models](../../archive/papers/2026/local-1b977d02353e100b/summary.md) — Turns each intermediate step of a reasoning trajectory into a numerical feature vector of distances to the answer choices, projects those into 2D to visualize how trajectories move through answer space, and reuses the same features to build a lightweight verifier for weighted voting.
- [LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals](../../archive/papers/2026/local-fc7e2641eda52776/summary.md) — Activations taken just before each explicit "Step k:" marker occupy linearly separable, step-indexed regions of representation space, and how a chain moves between those regions late in the trace predicts whether the final answer will be correct, which is used to gate interventions and to steer reasoning length.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
