# meta-reasoning

<!-- auto:begin -->

Reasoning about the reasoning process itself — deciding how to proceed rather than proceeding — used by both sources as a control layer above the reasoning. One quantifies state-transition probabilities along the thinking process and builds a transition-aware implicit reward that reinforces beneficial patterns and suppresses defective ones at atomic segments, targeting a gap where correct facts appear in reasoning but not in the answer. The other makes it an explicit controller that routes each generation step among a fast path, a re-perceive path and a self-reflect path. Both treat the choice of how to think as separable from the thinking, and both learn that choice rather than fixing it.

- **Kind**: method
- **Also called**: metacognition, reasoning about reasoning
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [credit assignment](../concepts/credit-assignment.md), [overthinking](../concepts/overthinking.md), [perception bottleneck](../concepts/perception-bottleneck.md), [process supervision](../concepts/process-supervision.md), [routing](../concepts/routing.md), [self-correction](../concepts/self-correction.md), [test-time compute](../concepts/test-time-compute.md), [truthfulness](../concepts/truthfulness.md)

## Appears in

- [MR-ALIGN: Meta-Reasoning Informed Factuality Alignment for Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-204/summary.md) — Improves factuality by reweighting reasoning segments according to state-transition probabilities along the thinking process, targeting a gap where correct facts appear in reasoning but not in the answer.
- [Addressing Overthinking in Large Vision-Language Models via Gated Perception-Reasoning Optimization](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-215/summary.md) — Routes each generation step among a fast path, a perception re-examination path and a self-reflection path, trained on 790k samples of teacher-attributed perception-versus-reasoning failures.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
