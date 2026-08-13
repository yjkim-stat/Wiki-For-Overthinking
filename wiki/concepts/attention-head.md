# attention head

<!-- auto:begin -->

An individual attention computation within a layer, treated by the sources as the unit at which a mechanism can be localized. One generalizes causal tracing to select subsets of heads and MLP neurons jointly, on the argument that single-component tracing misses components that only matter together and makes redundant ones each look unimportant. The other identifies specific heads by function, finding that latent counts stored in per-part item representations are moved to intermediate steps by dedicated heads before final aggregation. The pair frames the open question: heads are individually interpretable often enough to name, and jointly load-bearing often enough that naming them one at a time is unreliable.

- **Kind**: concept
- **Also called**: attention heads, head
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 3

**Related**: [activation patching](../methods/activation-patching.md), [activation steering](../methods/activation-steering.md), [causal intervention](causal-intervention.md), [causal mediation analysis](../methods/causal-mediation-analysis.md), [causal tracing](../methods/causal-tracing.md), [contrastive activation addition](../methods/contrastive-activation-addition.md), [effective depth](effective-depth.md), [GPT-4.1-mini](../models/gpt-4-1-mini.md), [Inference Time Intervention](inference-time-intervention.md), [linear probe](../methods/linear-probe.md), [linear representation hypothesis](linear-representation-hypothesis.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [localization](localization.md), [modularity](modularity.md), [Qwen2.5-14B](../models/qwen2-5-14b.md), [representation versus readout](representation-versus-readout.md), [steering vector](steering-vector.md), [superposition](superposition.md), [test-time compute](test-time-compute.md), [TruthfulQA](../datasets/truthfulqa.md)

## Appears in

- [Inverted Detection and Control in Steering Vectors](../../archive/papers/2026/arxiv-2608-02957/summary.md) — Finds directions that are highly discriminative for a concept and aligned with its positive examples yet reliably steer the model the opposite way, characterizes them geometrically as spoofing the concept's absence downstream, and turns that characterization into a training-free test that fixes the sign — improving a standard steering pipeline in 27 of 30 experiments.
- [Multi-component Causal Tracing in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-154/summary.md) — Generalizes causal tracing from one component or layer at a time to selecting subsets of components jointly, by relaxing the combinatorial search into a continuous one over soft interventions.
- [Mechanistic Interpretability of Large-Scale Counting in LLMs through a System-2 Strategy](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2031/summary.md) — Explains LLM counting failures as a depth limit, since counting is computed across layers, and fixes it with a System-2 decomposition whose mechanism is then traced.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
