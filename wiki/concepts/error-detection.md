# error detection

<!-- auto:begin -->

Identifying where a reasoning trace went wrong, and across 3 sources a capability the archive measures separately from repairing it. Two results. Detection recall is anti-correlated with downstream accuracy in the self-correction setting: methods recalling 49.9 and 54.6 percent of errors score lower on both mathematics benchmarks than ones recalling 33.2 and 35.9, so finding more errors is not the objective. And detection is hard for frontier models on its own terms -- on a multimodal error-detection benchmark the best model remains about 10 points behind human evaluation. One method reads it from residual-stream motion combined with a region and a direction reader rather than from static states, on the argument that static activations let a probe latch onto surface patterns.

- **Kind**: concept
- **Also called**: error identification, error localization, mistake detection
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [activation probing](../methods/activation-probing.md), [construct validity](construct-validity.md), [distribution shift](distribution-shift.md), [DPO](../methods/dpo.md), [effective depth](effective-depth.md), [GPT-4o](../models/gpt-4o.md), [GSM8K](../datasets/gsm8k.md), [linear probe](../methods/linear-probe.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [localization](localization.md), [MATH](../datasets/math.md), [multimodal reasoning](multimodal-reasoning.md), [out-of-distribution generalization](out-of-distribution-generalization.md), [process evaluation](../methods/process-evaluation.md), [process reward](process-reward.md), [process supervision](process-supervision.md), [Qwen2.5-14B-Instruct](../models/qwen2-5-14b-instruct.md), [Qwen2.5-Math-7B-Instruct](../models/qwen2-5-math-7b-instruct.md), [Qwen3-8B](../models/qwen3-8b.md), [reasoning trajectory](reasoning-trajectory.md), [residual stream](residual-stream.md), [self-correction](self-correction.md), [shortcut learning](shortcut-learning.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [teacher-student gap](teacher-student-gap.md), [verification](verification.md)

## Appears in

- [Reasoning Errors Have a Region and a Direction in the Residual-Stream Trajectory of LLMs](../../archive/papers/2026/arxiv-2608-05660/summary.md) — Detects flawed reasoning from residual-stream trajectories by combining layerwise motion with a quantized region reader and a normalized direction reader, rather than probing full states.
- [Reinforcing Step-level Reasoning for Effective Self-Correction in LLMs](../../archive/papers/2026/arxiv-2608-11573/summary.md) — Trains self-correction as a step-level preference problem -- preferring a detect-and-repair continuation over the continuation that would follow if the error went unaddressed -- after first initialising with ordinary step-level preference optimisation, and finds that correcting more often and detecting more errors both anti-correlate with accuracy.
- [ErrorRadar: Benchmarking Complex Mathematical Reasoning of Multimodal Large Language Models Via Error Detection](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1217/summary.md) — Benchmarks multimodal models on detecting and categorizing errors in K-12 math solutions collected from real student interactions, with the best model about 10% behind human experts.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
