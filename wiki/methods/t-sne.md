# t-SNE

<!-- auto:begin -->

A nonlinear projection that places high-dimensional points in two dimensions so that near neighbours stay near, used by both sources to make a reasoning trajectory something a person can look at. One turns each intermediate step into a vector of distances to the candidate answers and projects the resulting sequence, so a whole trace becomes a path across a plane and converging and wandering chains are visibly different. The other projects step-marker activations and finds them occupying linearly separable, step-indexed regions. Both treat the projection as a way of seeing structure that is then verified by something else — a classifier, a separability test — rather than as evidence in itself, which is the right use of it: the layout is not a measurement.

- **Kind**: method
- **Also called**: t-distributed stochastic neighbor embedding
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [activation steering](activation-steering.md), [causal intervention](../concepts/causal-intervention.md), [chain of thought](chain-of-thought.md), [chain of thought distillation](chain-of-thought-distillation.md), [CLIP](../models/clip.md), [CommonsenseQA](../datasets/commonsenseqa.md), [cosine similarity](cosine-similarity.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [flow matching](flow-matching.md), [foresight](../concepts/foresight.md), [GSM8K](../datasets/gsm8k.md), [latent reasoning](../concepts/latent-reasoning.md), [linear probe](linear-probe.md), [linear representation hypothesis](../concepts/linear-representation-hypothesis.md), [Llama-3.1-70B](../models/llama-3-1-70b.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [logit lens](logit-lens.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [Monte Carlo tree search](monte-carlo-tree-search.md), [principal component analysis](principal-component-analysis.md), [QwQ-32B](../models/qwq-32b.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [self-correction](../concepts/self-correction.md), [test-time scaling](test-time-scaling.md)

## Appears in

- [LiLa-WAM: Lightweight Latent Reasoning World-Action Model for Robotic Manipulation](../../archive/papers/2026/arxiv-2608-03701/summary.md) — Builds a 0.5B world-action model for robot manipulation whose future-state prediction and action generation share one compact latent in a single token stream, specifies the task as a direction in visual feature space instead of language, and shows a frozen self-supervised vision encoder beating a four-times-larger pretrained vision-language backbone at the same training budget.
- [Landscape of Thoughts: Visualizing the Reasoning Process of Large Language Models](../../archive/papers/2026/local-1b977d02353e100b/summary.md) — Turns each intermediate step of a reasoning trajectory into a numerical feature vector of distances to the answer choices, projects those into 2D to visualize how trajectories move through answer space, and reuses the same features to build a lightweight verifier for weighted voting.
- [LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals](../../archive/papers/2026/local-fc7e2641eda52776/summary.md) — Activations taken just before each explicit "Step k:" marker occupy linearly separable, step-indexed regions of representation space, and how a chain moves between those regions late in the trace predicts whether the final answer will be correct, which is used to gate interventions and to steer reasoning length.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
