# controllability

<!-- auto:begin -->

Whether a model does what it is told, treated by both sources as a property distinct from capability and measured separately from it. One finds it in tension with reasoning strength: models that reason more effectively comply less with user directives, degradation worsens as generation length grows, and restoring obedience costs reasoning performance. The other moves the question inside the trace and finds the best instruction-following score below 0.25, degrading further as task difficulty rises, with targeted finetuning raising one model from 0.11 to 0.27. Together they establish that the reasoning trace is largely outside user control, which bounds any method that assumes the trace can be steered by instruction.

- **Kind**: concept
- **Also called**: directive adherence, obedience, steerability
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [alignment](alignment.md), [alignment tax](alignment-tax.md), [DeepSeek-R1](../models/deepseek-r1.md), [GPT-OSS-20B](../models/gpt-oss-20b.md), [instruction following](instruction-following.md), [monitorability](monitorability.md), [multi-turn reasoning](../methods/multi-turn-reasoning.md), [reinforcement learning post-training](../methods/reinforcement-learning-post-training.md), [reward hacking](reward-hacking.md), [synthetic data generation](../methods/synthetic-data-generation.md)

## Appears in

- [Scaling Reasoning, Losing Control: Evaluating Instruction Following in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1878/summary.md) — A benchmark showing that as reasoning capacity grows, instruction adherence falls, and that recovering obedience costs reasoning performance.
- [ReasonIF: Large Reasoning Models Fail to Follow Instructions During Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1456/summary.md) — Benchmarks whether reasoning models follow instructions inside their reasoning traces, finding under 25% compliance at best and worse as difficulty rises.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
