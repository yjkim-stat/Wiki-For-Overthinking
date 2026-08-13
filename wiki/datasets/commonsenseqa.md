# CommonsenseQA

<!-- auto:begin -->

A multiple-choice commonsense question-answering benchmark, used in both sources as the non-mathematical control. One reports that bootstrapped self-training on it performs comparably to finetuning a 30x larger model, which is where its headline efficiency claim comes from. The other finds its reasoning landscape distinct from the mathematical benchmarks — states concentrate in a narrow region rather than spreading out — and reads that as direct retrieval of stored knowledge rather than step-by-step reasoning, with the lowest accuracy of the four datasets tested (64.8%). Useful in this archive precisely because it is where 'reasoning' methods may be measuring something else.

- **Kind**: dataset
- **Also called**: CQA
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [chain of thought](../methods/chain-of-thought.md), [few-shot prompting](../methods/few-shot-prompting.md), [Llama-3.1-70B](../models/llama-3-1-70b.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [MMLU](mmlu.md), [Monte Carlo tree search](../methods/monte-carlo-tree-search.md), [post-hoc rationalization](../concepts/post-hoc-rationalization.md), [QwQ-32B](../models/qwq-32b.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [self-correction](../concepts/self-correction.md), [self-training](../concepts/self-training.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [t-SNE](../methods/t-sne.md)

## Appears in

- [STaR: Bootstrapping Reasoning With Reasoning](../../archive/papers/2022/arxiv-2203-14465/summary.md) — Bootstraps a model's reasoning ability from a handful of rationale examples by generating rationales, keeping only those that reach the right answer, and finetuning on them in a loop.
- [Landscape of Thoughts: Visualizing the Reasoning Process of Large Language Models](../../archive/papers/2026/local-1b977d02353e100b/summary.md) — Turns each intermediate step of a reasoning trajectory into a numerical feature vector of distances to the answer choices, projects those into 2D to visualize how trajectories move through answer space, and reuses the same features to build a lightweight verifier for weighted voting.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
