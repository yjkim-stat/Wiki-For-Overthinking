# perception bottleneck

<!-- auto:begin -->

The finding that failures attributed to reasoning are often failures to see, which three sources establish independently and in different directions. One isolates perception from reasoning with a two-stage pipeline that converts each image to text independently to prevent cross-image inductive leakage, and attributes approximately 80% of ARC-style failures to perception errors. One removes the image entirely and finds performance can improve. One argues that reasoning errors originate in imperfect grounding rather than insufficient deliberation, and routes computation to a re-perceive path rather than more thinking. The practical consequence is that more deliberation cannot repair a perception error, so compute-allocation methods that only choose how much to think are choosing on the wrong axis.

- **Kind**: concept
- **Also called**: perception-reasoning confound, visual perception bottleneck
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [construct validity](construct-validity.md), [GPT-5](../models/gpt-5.md), [meta-evaluation](meta-evaluation.md), [meta-reasoning](../methods/meta-reasoning.md), [multimodal reasoning](multimodal-reasoning.md), [overthinking](overthinking.md), [Qwen3-VL](../models/qwen3-vl.md), [routing](routing.md), [self-correction](self-correction.md), [test-time compute](test-time-compute.md)

## Appears in

- [MathSight: A Benchmark Exploring Have Vision-Language Models Really Seen in University-Level Mathematical Reasoning?](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2198/summary.md) — A university-level multimodal math benchmark with original, hand-drawn, photographed and text-only variants of each problem, on which a model with no image beats its own multimodal variants and GPT-5.
- [Your Reasoning Benchmark May Not Test Reasoning: Revealing Perception Bottleneck in Abstract Reasoning Benchmarks](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-826/summary.md) — Separates perception from reasoning in ARC-style benchmarks with a two-stage pipeline, and finds about 80% of vision-language model failures are perception errors, not reasoning errors.
- [Addressing Overthinking in Large Vision-Language Models via Gated Perception-Reasoning Optimization](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-215/summary.md) — Routes each generation step among a fast path, a perception re-examination path and a self-reflection path, trained on 790k samples of teacher-attributed perception-versus-reasoning failures.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
