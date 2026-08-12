# causal tracing

<!-- auto:begin -->

Intervening on internal representations to measure which components a behaviour causally depends on, as opposed to which merely correlate with it. The sources address complementary weaknesses. One extends tracing from single components or layers to joint subsets, converting the combinatorial search into a continuous problem over soft interventions, because components that matter only together are invisible to one-at-a-time search. The other shows the method's conclusions depend on choices usually left implicit — how prompts are corrupted, which metric scores the effect, and whether layers are patched singly or in sliding windows. Read together: tracing is sensitive both to what it can search over and to how the search is scored.

- **Kind**: method
- **Also called**: causal mediation, causal trace, interchange intervention
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [activation patching](activation-patching.md), [attention head](../concepts/attention-head.md), [causal mediation analysis](causal-mediation-analysis.md), [circuit analysis](circuit-analysis.md), [GPT-J 6B](../models/gpt-j-6b.md), [Indirect Object Identification (IOI)](../datasets/indirect-object-identification-ioi.md), [localization](../concepts/localization.md), [modularity](../concepts/modularity.md), [superposition](../concepts/superposition.md)

## Appears in

- [Multi-component Causal Tracing in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-154/summary.md) — Generalizes causal tracing from one component or layer at a time to selecting subsets of components jointly, by relaxing the combinatorial search into a continuous one over soft interventions.
- [Towards Best Practices of Activation Patching in Language Models: Metrics and Methods](../../archive/papers/2024/local-956614b275995bc4/summary.md) — Systematically varies the methodological choices in activation patching — how prompts are corrupted, which metric scores the patching effect, and whether layers are patched singly or in sliding windows — and shows each choice can change which model components a study concludes are important.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
