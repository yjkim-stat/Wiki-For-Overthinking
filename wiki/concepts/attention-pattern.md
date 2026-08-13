# attention pattern

<!-- auto:begin -->

The distribution of attention weights over positions, used by the sources as a readable trace of information flow. One provides tooling to extract and compare these patterns across vision-language architectures; the two others use them to act rather than to observe — locating where to inject a safety reflection, and scoring how strongly cross-step routing aligns with semantic proximity. The sources treat the pattern as evidence about which earlier content a step is actually using, which is the assumption their interventions rest on and which none of them tests directly.

- **Kind**: concept
- **Also called**: attention map, attention weights
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [activation patching](../methods/activation-patching.md), [aha moment](aha-moment.md), [attention analysis](../methods/attention-analysis.md), [Inference Time Intervention](inference-time-intervention.md), [jailbreak](jailbreak.md), [localization](localization.md), [mechanistic interpretability](mechanistic-interpretability.md), [Qwen3-VL](../models/qwen3-vl.md), [reproducibility](reproducibility.md), [test-time compute](test-time-compute.md), [verification](verification.md)

## Appears in

- [Spectra: A Mechanistic Interpretability Library for Vision-Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-demo-78/summary.md) — An open library giving vision-language models the mechanistic-interpretability tooling that text-only models already have: activation patching, attention analysis and meta-functions behind one interface.
- [ReasoningGuard: Safeguarding Large Reasoning Models with Inference-time Safety Aha Moments](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1453/summary.md) — An inference-time safeguard that reads a reasoning model's attention to find key points in its reasoning path and injects safety reflections there, then scales sampling to pick a safe path.
- [RFS-Guard: Detecting Reasoning Hallucinations via Cross-Phase Routing Focus in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-885/summary.md) — Detects reasoning hallucinations by measuring how strongly cross-step attention routing aligns with hidden-state semantic proximity, finding that higher alignment means higher hallucination risk.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
