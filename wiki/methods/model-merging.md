# model merging

<!-- auto:begin -->

Combining separately trained checkpoints in parameter space to get their capabilities in one model without further training. The two sources reach opposite conclusions about whether reasoning survives it. One reports a destructive collapse that weakens reasoning depth and domain utility together, and attributes it to reasoning residing in low-gradient-sensitivity parameter regions rather than the high-magnitude parameters usually assumed. The other merges three separately aligned meta-ability checkpoints — deduction, induction, abduction — as the middle stage of a working pipeline. So the archive holds both a claim that merging reliably damages reasoning and a case where merging reasoning abilities succeeds.

- **Kind**: method
- **Also called**: checkpoint merging, parameter merging, weight merging
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [aha moment](../concepts/aha-moment.md), [catastrophic forgetting](../concepts/catastrophic-forgetting.md), [emergent behaviour](../concepts/emergent-behaviour.md), [localization](../concepts/localization.md), [modularity](../concepts/modularity.md), [performance ceiling](../concepts/performance-ceiling.md), [self-verification](../concepts/self-verification.md)

## Appears in

- [ReasonAny: Incorporating Reasoning Capability to Any Model via Simple and Effective Model Merging](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2201/summary.md) — Merges a reasoning model into a domain-specialized one after finding that reasoning ability resides in low-gradient-sensitivity parameter regions rather than high-magnitude ones.
- [Beyond &apos;Aha!&apos;: Toward Systematic Meta-Abilities Alignment in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1981/summary.md) — Replaces reliance on unpredictable emergent 'aha moments' by explicitly aligning models to deduction, induction and abduction on self-verifiable tasks before domain RL.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
