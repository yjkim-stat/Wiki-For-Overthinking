# ARC-AGI

<!-- auto:begin -->

A benchmark of abstract visual grid puzzles used here for two different purposes, neither of which is measuring reasoning cleanly. One source uses its tasks as part of a logic pool for studying which training items respond to continued RL. The other is the caution: separating perception from reasoning with a two-stage pipeline shows about 80% of vision-language model failures on ARC-style tasks are perception errors rather than reasoning errors, so a score on it confounds seeing the grid with reasoning about it.

- **Kind**: dataset
- **Also called**: ARC prize, ARC-AGI-2
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md)
- **Sources**: 2

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [construct validity](../concepts/construct-validity.md), [curriculum learning](../concepts/curriculum-learning.md), [DAPO-Math-17K](dapo-math-17k.md), [data efficiency](../concepts/data-efficiency.md), [GRPO](../methods/grpo.md), [linear probe](../methods/linear-probe.md), [Llama-3.2-3B](../models/llama-3-2-3b.md), [MATH500](math500.md), [meta-evaluation](../concepts/meta-evaluation.md), [Minerva](minerva.md), [OlympiadBench](olympiadbench.md), [perception bottleneck](../concepts/perception-bottleneck.md), [prompt difficulty](../concepts/prompt-difficulty.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-4B](../models/qwen3-4b.md), [training dynamics](../concepts/training-dynamics.md)

## Appears in

- [Beyond Solvability: Task Learnability as a Static Prior for LLM RL Post-Training](../../archive/papers/2026/arxiv-2608-09217/summary.md) — Separates how well a policy currently does on a task from how positively that task responds to further training, shows the second is reproducible across independent runs and predicts downstream value at matched current pass rate, and estimates it from a short probe run before RL begins.
- [Your Reasoning Benchmark May Not Test Reasoning: Revealing Perception Bottleneck in Abstract Reasoning Benchmarks](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-826/summary.md) — Separates perception from reasoning in ARC-style benchmarks with a two-stage pipeline, and finds about 80% of vision-language model failures are perception errors, not reasoning errors.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
