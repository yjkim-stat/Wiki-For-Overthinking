# catastrophic forgetting

<!-- auto:begin -->

Loss of previously held capability when a model is trained further, which both sources treat as a routine consequence of reasoning post-training rather than an edge case. One measures it: prolonged RLVR degrades foundational skills including perception and faithfulness, and KL regularization does not prevent it because the penalty is computed on the current task. The other locates it in parameter space, reporting that reasoning ability sits in regions of low gradient sensitivity — not in high-magnitude parameters as usually assumed — which would explain why merging and pruning damage reasoning disproportionately. That faithfulness is among the capabilities lost would mean some of the archive's faithfulness findings are a consequence of reasoning training rather than a property of models.

- **Kind**: concept
- **Also called**: capability collapse, capability regression, general-capability forgetting
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [chain of thought faithfulness](chain-of-thought-faithfulness.md), [localization](localization.md), [model merging](../methods/model-merging.md), [modularity](modularity.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [RLVR](../methods/rlvr.md), [training dynamics](training-dynamics.md)

## Appears in

- [ReasonAny: Incorporating Reasoning Capability to Any Model via Simple and Effective Model Merging](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2201/summary.md) — Merges a reasoning model into a domain-specialized one after finding that reasoning ability resides in low-gradient-sensitivity parameter regions rather than high-magnitude ones.
- [Beyond Reasoning Gains: Mitigating General-Capability Forgetting in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1717/summary.md) — Confirms that prolonged RLVR makes models forget foundational skills, and counters it with experience replay whose objective weights adapt online to convergence and instability signals.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
