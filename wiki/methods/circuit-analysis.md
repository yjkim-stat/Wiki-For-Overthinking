# circuit analysis

<!-- auto:begin -->

Identifying a subset of model components — attention heads, neurons — and the information flow between them that accounts for a behaviour. The archived sources use it at three scales and the results do not straightforwardly compose. On a synthetic logic task it recovers a sparse, modular circuit in models up to 27B, decomposing into four head families executed sequentially. On indirect object identification it is shown to be badly sensitive to methodology, with corruption method and metric each changing which heads a study reports. And the same source that recovers a clean circuit reports that three-layer models trained directly on the task are more accurate while being *less* modular — so circuit legibility is not evidence of competence.

- **Kind**: method
- **Also called**: circuit discovery
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 4

**Related**: [activation patching](activation-patching.md), [causal analysis](causal-analysis.md), [causal mediation analysis](causal-mediation-analysis.md), [causal tracing](causal-tracing.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [circuit discovery](circuit-discovery.md), [generalization](../concepts/generalization.md), [GPT-J 6B](../models/gpt-j-6b.md), [implicit reasoning](../concepts/implicit-reasoning.md), [Indirect Object Identification (IOI)](../datasets/indirect-object-identification-ioi.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [localization](../concepts/localization.md), [memorization](../concepts/memorization.md), [Mistral-7B](../models/mistral-7b.md), [modularity](../concepts/modularity.md), [out-of-distribution generalization](../concepts/out-of-distribution-generalization.md), [Pythia-410M](../models/pythia-410m.md), [retrieval-augmented generation](retrieval-augmented-generation.md)

## Appears in

- [Arithmetic Without Algorithms: Language Models Solve Math With a Bag of Heuristics](../../archive/papers/2025/local-26fdb25b9d157d04/summary.md) — Reverse-engineers the arithmetic circuit down to individual neurons and finds it is neither a learned algorithm nor memorization, but an unordered collection of sparse heuristic neurons that each fire on a numerical input pattern and vote for corresponding answers.
- [Grokked Transformers are Implicit Reasoners: A Mechanistic Journey to the Edge of Generalization](../../archive/papers/2024/local-6252abed1b134f57/summary.md) — Shows that transformers can learn implicit multi-step reasoning over stored knowledge, but only through grokking — extended training far past overfitting — and that whether the resulting circuit generalizes out of distribution depends on the reasoning type, succeeding for comparison and failing for composition.
- [Towards Best Practices of Activation Patching in Language Models: Metrics and Methods](../../archive/papers/2024/local-956614b275995bc4/summary.md) — Systematically varies the methodological choices in activation patching — how prompts are corrupted, which metric scores the patching effect, and whether layers are patched singly or in sliding windows — and shows each choice can change which model components a study concludes are important.
- [A Implies B: Circuit Analysis in LLMs for Propositional Logical Reasoning](../../archive/papers/2025/local-99a25b62fd9ad86c/summary.md) — Uses causal mediation analysis on a minimal propositional logic task to recover a sparse reasoning circuit in Mistral-7B and Gemma-2 up to 27B, and decomposes it into four families of attention heads that execute rule locating, rule moving, fact processing and decision making as sequential steps.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
