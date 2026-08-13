# Llama-3.1-70B

<!-- auto:begin -->

A 70B Llama model, the largest non-reasoning system measured in these sources. It anchors the scale end of two analyses: reasoning trajectories that converge fastest with the highest consistency and lowest uncertainty among the models compared (84.4% on AQuA), and a mutual-information profile that still shows weaker peaks than reasoning-trained models of smaller size, which is the evidence that the phenomenon comes from training rather than capacity.

- **Kind**: model
- **Also called**: Llama-3.1-70B, Llama-3.3-70B-Instruct
- **Topics**: [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [AIME 2024](../datasets/aime-2024.md), [AMC23](../datasets/amc23.md), [answer stabilization](../concepts/answer-stabilization.md), [chain of thought](../methods/chain-of-thought.md), [CommonsenseQA](../datasets/commonsenseqa.md), [DeepSeek-R1](deepseek-r1.md), [Dynasor](../methods/dynasor.md), [early exit](../methods/early-exit.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-8B](llama-3-1-8b.md), [Llama-3.2-1B](llama-3-2-1b.md), [Llama-3.2-3B](llama-3-2-3b.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [Monte Carlo tree search](../methods/monte-carlo-tree-search.md), [overthinking](../concepts/overthinking.md), [Qwen2.5-7B](qwen2-5-7b.md), [QwQ-32B](qwq-32b.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [self-consistency](../methods/self-consistency.md), [self-correction](../concepts/self-correction.md), [t-SNE](../methods/t-sne.md), [test-time compute](../concepts/test-time-compute.md)

## Appears in

- [Efficiently Scaling LLM Reasoning with Certaindex](../../archive/papers/2025/local-0c24c3c0e4729108/summary.md) — Defines certaindex, an algorithm-agnostic measure of how much a reasoning algorithm's answer has stopped changing, and builds it into a serving system that reallocates or terminates compute per query — saving up to 50% of tokens in batch inference and tripling online throughput.
- [Landscape of Thoughts: Visualizing the Reasoning Process of Large Language Models](../../archive/papers/2026/local-1b977d02353e100b/summary.md) — Turns each intermediate step of a reasoning trajectory into a numerical feature vector of distances to the answer choices, projects those into 2D to visualize how trajectories move through answer space, and reuses the same features to build a lightweight verifier for weighted voting.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
