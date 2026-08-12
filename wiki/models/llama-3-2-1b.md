# Llama-3.2-1B

<!-- auto:begin -->

A 1B model from the Llama-3.2 family, appearing in both sources as a small-scale subject. One uses it as the weakest rung of a visualization study, where its reasoning accuracy on AQuA is 15.8% and its trajectories converge slowly with low consistency and high uncertainty. The other builds a step-level sparse autoencoder on it and finds its features markedly sparser and less shared across steps than the comparable Qwen model (15.65% activation ratio, Jaccard 0.3052), with 40.4% of features attributed to reasoning rather than calculation or resolution — read there as the model attending more to the explicit chain of thought.

- **Kind**: model
- **Also called**: Llama-3.2-1B
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [activation patching](../methods/activation-patching.md), [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [chain of thought](../methods/chain-of-thought.md), [CommonsenseQA](../datasets/commonsenseqa.md), [GSM8K](../datasets/gsm8k.md), [information bottleneck](../concepts/information-bottleneck.md), [linear probing](../methods/linear-probing.md), [Llama-3.1-70B](llama-3-1-70b.md), [Llama-3.1-8B](llama-3-1-8b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [monosemanticity](../concepts/monosemanticity.md), [Monte Carlo tree search](../methods/monte-carlo-tree-search.md), [Qwen2.5-0.5B](qwen2-5-0-5b.md), [QwQ-32B](qwq-32b.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [self-consistency](../methods/self-consistency.md), [self-correction](../concepts/self-correction.md), [self-verification](../concepts/self-verification.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [superposition](../concepts/superposition.md), [t-SNE](../methods/t-sne.md)

## Appears in

- [Landscape of Thoughts: Visualizing the Reasoning Process of Large Language Models](../../archive/papers/2026/local-1b977d02353e100b/summary.md) — Turns each intermediate step of a reasoning trajectory into a numerical feature vector of distances to the answer choices, projects those into 2D to visualize how trajectories move through answer space, and reuses the same features to build a lightweight verifier for weighted voting.
- [Step-Level Sparse Autoencoder for Reasoning Process Interpretation](../../archive/papers/2026/local-d9699040f5220b4c/summary.md) — Trains a sparse autoencoder over whole reasoning steps rather than tokens, conditioning both encoder and decoder on the preceding trajectory so the sparse code carries only what the step adds, and shows that step correctness, logicality, length and first token are all linearly decodable from that code.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
