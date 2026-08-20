# Llama-3.2-3B

<!-- auto:begin -->

The 3B Llama base checkpoint, used across 3 sources as a small cross-family control. Its most consequential archived appearance is as the cross-family check in a task-learnability study, where the claim that a task's response to training is reproducible and predicts downstream value at matched pass rate is tested outside the Qwen family it was developed in. It also appears in a cross-family steering audit and in reasoning-trajectory visualisation.

- **Kind**: model
- **Also called**: Llama-3.2-3B, Llama-3.2-3B-Instruct
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [ablation](../methods/ablation.md), [activation steering](../methods/activation-steering.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [ARC-AGI](../datasets/arc-agi.md), [bootstrap confidence intervals](../methods/bootstrap-confidence-intervals.md), [chain of thought](../concepts/chain-of-thought.md), [CommonsenseQA](../datasets/commonsenseqa.md), [contrastive activation addition](../methods/contrastive-activation-addition.md), [curriculum learning](../methods/curriculum-learning.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [data efficiency](../concepts/data-efficiency.md), [detection versus control](../concepts/detection-versus-control.md), [difference-in-means direction](../methods/difference-in-means-direction.md), [Gemma-2-27B](gemma-2-27b.md), [Gemma-2-9B](gemma-2-9b.md), [GRPO](../methods/grpo.md), [interpretability illusion](../concepts/interpretability-illusion.md), [linear probe](../methods/linear-probe.md), [linear representation hypothesis](../concepts/linear-representation-hypothesis.md), [Llama-3.1-70B](llama-3-1-70b.md), [Llama-3.1-8B](llama-3-1-8b.md), [Llama-3.2-1B](llama-3-2-1b.md), [Llama-3.2-3B-Instruct](llama-3-2-3b-instruct.md), [MATH500](../datasets/math500.md), [measurement invariance](../concepts/measurement-invariance.md), [Minerva](../datasets/minerva.md), [MMLU](../datasets/mmlu.md), [Monte Carlo tree search](../methods/monte-carlo-tree-search.md), [OlympiadBench](../datasets/olympiadbench.md), [operating point](../concepts/operating-point.md), [Phi-4](phi-4.md), [prompt difficulty](../concepts/prompt-difficulty.md), [Qwen2.5-72B](qwen2-5-72b.md), [Qwen3-0.6B](qwen3-0-6b.md), [Qwen3-1.7B](qwen3-1-7b.md), [Qwen3-14B](qwen3-14b.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-4B](qwen3-4b.md), [Qwen3-8B](qwen3-8b.md), [QwQ-32B](qwq-32b.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [residual stream](../concepts/residual-stream.md), [selection bias](../concepts/selection-bias.md), [selectivity control](../methods/selectivity-control.md), [self-correction](../concepts/self-correction.md), [steering vector](../methods/steering-vector.md), [StrategyQA](../datasets/strategyqa.md), [t-SNE](../methods/t-sne.md), [training dynamics](../concepts/training-dynamics.md)

## Appears in

- [When Is a Steerable Concept Representation Real? Measurement Confounds in a Cross-Family Audit of Neuroscience Parallels in LLMs](../../archive/papers/2026/arxiv-2608-08159/summary.md) — Audits four neuroscience-inspired claims about language models across 17 checkpoints from five families and 0.6B to 72B, and shows that an apparent emergence of concept steerability with scale is produced entirely by uncalibrated measurement -- raw intervention units, the readout metric, and a fixed operating point -- with correcting any one of the three removing the trend.
- [Beyond Solvability: Task Learnability as a Static Prior for LLM RL Post-Training](../../archive/papers/2026/arxiv-2608-09217/summary.md) — Separates how well a policy currently does on a task from how positively that task responds to further training, shows the second is reproducible across independent runs and predicts downstream value at matched current pass rate, and estimates it from a short probe run before RL begins.
- [Landscape of Thoughts: Visualizing the Reasoning Process of Large Language Models](../../archive/papers/2026/local-1b977d02353e100b/summary.md) — Turns each intermediate step of a reasoning trajectory into a numerical feature vector of distances to the answer choices, projects those into 2D to visualize how trajectories move through answer space, and reuses the same features to build a lightweight verifier for weighted voting.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
