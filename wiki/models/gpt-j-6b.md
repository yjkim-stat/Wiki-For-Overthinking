# GPT-J 6B

<!-- auto:begin -->

A 6B open-weight autoregressive model, used in these sources as an interpretability subject rather than a reasoning system. It appears in the activation-patching methodology study as the largest model checked, where some arithmetic tasks show the recommended corruption method producing stronger localization than the alternative, and in the arithmetic-heuristics work as one of the models in which the bag-of-heuristics mechanism replicates.

- **Kind**: model
- **Also called**: GPT-J, GPT-J 6B
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [activation patching](../methods/activation-patching.md), [causal analysis](../methods/causal-analysis.md), [causal mediation analysis](../methods/causal-mediation-analysis.md), [causal tracing](../methods/causal-tracing.md), [circuit analysis](../methods/circuit-analysis.md), [circuit discovery](../methods/circuit-discovery.md), [generalization](../concepts/generalization.md), [Indirect Object Identification (IOI)](../datasets/indirect-object-identification-ioi.md), [Llama-3.1-8B](llama-3-1-8b.md), [localization](../concepts/localization.md), [memorization](../concepts/memorization.md), [modularity](../concepts/modularity.md), [Pythia-410M](pythia-410m.md)

## Appears in

- [Arithmetic Without Algorithms: Language Models Solve Math With a Bag of Heuristics](../../archive/papers/2025/local-26fdb25b9d157d04/summary.md) — Reverse-engineers the arithmetic circuit down to individual neurons and finds it is neither a learned algorithm nor memorization, but an unordered collection of sparse heuristic neurons that each fire on a numerical input pattern and vote for corresponding answers.
- [Towards Best Practices of Activation Patching in Language Models: Metrics and Methods](../../archive/papers/2024/local-956614b275995bc4/summary.md) — Systematically varies the methodological choices in activation patching — how prompts are corrupted, which metric scores the patching effect, and whether layers are patched singly or in sliding windows — and shows each choice can change which model components a study concludes are important.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
