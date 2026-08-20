# causal tracing

<!-- auto:begin -->

Intervening on internal representations to quantify the pathways linking inputs or computations to a metric of interest. Across 4 sources the archive's material is mostly about extending it past its usual one-component-at-a-time form: one source relaxes the combinatorial search over subsets of components into a continuous one over soft interventions, so that components can be selected jointly rather than swept singly. Its application in the corpus recovers sparse circuits -- one propositional-logic study decomposes a recovered circuit into four families of attention heads executing rule locating, rule moving, fact processing and decision making as sequential steps across models from 7B to 27B. The archive's standing caveats for this family apply: no convention exists for the corruption method or the evaluation metric, so results are frequently not comparable across papers, and an analysis conducted at the level of attention patterns is weaker than one carried to the embedding level, which one source says of its own work.

- **Kind**: method
- **Also called**: causal mediation, causal mediation analysis, causal trace, interchange intervention
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 4

**Related**: [activation patching](activation-patching.md), [attention head](../concepts/attention-head.md), [causal intervention](causal-intervention.md), [causal mediation analysis](causal-mediation-analysis.md), [circuit analysis](circuit-analysis.md), [detection versus control](../concepts/detection-versus-control.md), [GPT-2 small](../models/gpt-2-small.md), [GPT-2 XL](../models/gpt-2-xl.md), [GPT-J 6B](../models/gpt-j-6b.md), [indirect object identification](../datasets/indirect-object-identification.md), [interpretability illusion](../concepts/interpretability-illusion.md), [localization](../concepts/localization.md), [low-rank weight ablation](low-rank-weight-ablation.md), [modularity](../concepts/modularity.md), [permutation test](permutation-test.md), [pre-registration](pre-registration.md), [Qwen2.5-1.5B-Instruct](../models/qwen2-5-1-5b-instruct.md), [residual stream](../concepts/residual-stream.md), [self-repair](../concepts/self-repair.md), [superposition](../concepts/superposition.md), [weight-space ablation](weight-space-ablation.md)

## Appears in

- [A Theory of Conditional Collapse under Low-Rank Weight-Space Ablations: I. The Single-Block Theory and Synthetic Validation](../../archive/papers/2026/arxiv-2608-03620/summary.md) — Proves that activation patching and weight-space ablation measure two different quantities — a carrier's donor-receiver contrast versus its absolute level at the receiver — which neither bounds, gives an exact if-and-only-if criterion for when ablating a subset collapses a conditional onto one branch, and then withdraws its own clean empirical separation when it fails out of sample.
- [Cross-Layer Interaction under Weight-Space Ablation: A Closed-Form Attention Jacobian Bound and a Test on a Real Pretrained Model](../../archive/papers/2026/arxiv-2608-03629/summary.md) — Extends a single-block interaction theorem to ablated subsets spanning many layers, isolates the cross-layer remainder as an exact double integral rather than bounding it, supplies the one missing closed-form ingredient (a local attention Jacobian bound, verified without a violation on a real 1.5B model), and tests the whole picture on an emergent circuit nobody designed for it — reporting the mixed outcome as mixed.
- [Multi-component Causal Tracing in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-154/summary.md) — Generalizes causal tracing from one component or layer at a time to selecting subsets of components jointly, by relaxing the combinatorial search into a continuous one over soft interventions.
- [Towards Best Practices of Activation Patching in Language Models: Metrics and Methods](../../archive/papers/2024/local-956614b275995bc4/summary.md) — Systematically varies the methodological choices in activation patching — how prompts are corrupted, which metric scores the patching effect, and whether layers are patched singly or in sliding windows — and shows each choice can change which model components a study concludes are important.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
