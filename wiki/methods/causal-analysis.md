# causal analysis

<!-- auto:begin -->

The family of intervention-based methods used across this archive to establish that a component or a written state matters, rather than merely correlates. The archived instances span the full range of strictness: unit removal fitted to a structural equation model (cheapest, but off-distribution), activation patching scored by whether the output changed (standard, and shown to be highly sensitive to corruption method and metric), truncation with forced answering (avoids corrupting the trace), and counterfactual state editing scored against the single consequence the transition rule implies (strictest, and the one that generic steering cannot pass). Which criterion a result used determines how much it establishes.

- **Kind**: method
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [activation patching](activation-patching.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [circuit analysis](circuit-analysis.md), [circuit discovery](circuit-discovery.md), [generalization](../concepts/generalization.md), [GPT-J 6B](../models/gpt-j-6b.md), [implicit reasoning](../concepts/implicit-reasoning.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [localization](../concepts/localization.md), [memorization](../concepts/memorization.md), [modularity](../concepts/modularity.md), [out-of-distribution generalization](../concepts/out-of-distribution-generalization.md), [Pythia-410M](../models/pythia-410m.md), [retrieval-augmented generation](retrieval-augmented-generation.md)

## Appears in

- [Arithmetic Without Algorithms: Language Models Solve Math With a Bag of Heuristics](../../archive/papers/2025/local-26fdb25b9d157d04/summary.md) — Reverse-engineers the arithmetic circuit down to individual neurons and finds it is neither a learned algorithm nor memorization, but an unordered collection of sparse heuristic neurons that each fire on a numerical input pattern and vote for corresponding answers.
- [Grokked Transformers are Implicit Reasoners: A Mechanistic Journey to the Edge of Generalization](../../archive/papers/2024/local-6252abed1b134f57/summary.md) — Shows that transformers can learn implicit multi-step reasoning over stored knowledge, but only through grokking — extended training far past overfitting — and that whether the resulting circuit generalizes out of distribution depends on the reasoning type, succeeding for comparison and failing for composition.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
