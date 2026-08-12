# inference-time intervention

<!-- auto:begin -->

Changing what a model does at generation time without touching its parameters, which both sources adopt for the same reason: fine-tuning-based defences are costly and do not scale. Both also place the intervention mid-trajectory rather than at the input or the output, because that is where they locate the failure. One reads internal attention to find key points in the reasoning path and injects safety-oriented reflections there, then samples to select a safe path. The other extracts objective visual evidence into a structured intent representation and enforces safety constraints before generation, on the finding that models perceive risk cues correctly and then lose them as narrative coherence takes over. Both need white-box access.

- **Kind**: concept
- **Also called**: decoding-time intervention, inference-time defense, test-time intervention
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [aha moment](aha-moment.md), [attention analysis](../methods/attention-analysis.md), [attention pattern](attention-pattern.md), [chain of thought](../methods/chain-of-thought.md), [jailbreak](jailbreak.md), [multimodal reasoning](multimodal-reasoning.md), [test-time compute](test-time-compute.md)

## Appears in

- [ReasoningGuard: Safeguarding Large Reasoning Models with Inference-time Safety Aha Moments](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1453/summary.md) — An inference-time safeguard that reads a reasoning model's attention to find key points in its reasoning path and injects safety reflections there, then scales sampling to pick a safe path.
- [Mitigating Safety Context Amnesia in Multimodal Reasoning Models via Intent-Guided Safety Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1821/summary.md) — Identifies a multimodal failure where models see the risky visual cue but let narrative coherence override safety as reasoning proceeds, and defends against it by extracting intent before generation.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
