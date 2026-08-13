# inverse scaling

<!-- auto:begin -->

A property getting worse as models or budgets get larger. It appears twice here and in both cases about something the archive would prefer to improve with scale: faithfulness of reasoning decreases as models become larger and more capable on most tasks studied, and the verbosity that makes a trace monitorable improves performance only up to a point before degrading. Together they mean legible reasoning is not something scale is expected to deliver.

- **Kind**: concept
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [answer extraction](answer-extraction.md), [BBH](../datasets/bbh.md), [calibration](../methods/calibration.md), [chain of thought faithfulness](chain-of-thought-faithfulness.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Claude-3.7-Sonnet](../models/claude-3-7-sonnet.md), [construct validity](construct-validity.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-V3](../models/deepseek-v3.md), [Gemma-4-12B](../models/gemma-4-12b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MMLU](../datasets/mmlu.md), [monitorability](monitorability.md), [post-hoc rationalization](post-hoc-rationalization.md), [QwQ-32B](../models/qwq-32b.md), [self-correction](self-correction.md), [sycophancy](sycophancy.md), [test-time compute](test-time-compute.md), [verbosity](verbosity.md)

## Appears in

- [Measuring Faithfulness in Chain-of-Thought Reasoning](../../archive/papers/2023/arxiv-2307-13702/summary.md) — Measures how much a model's answer actually depends on its stated chain of thought by intervening on the trace — adding mistakes, paraphrasing, truncating — and finds the dependence varies by task and decreases as models get larger.
- [The Calibration Floor: Format Repair Can Masquerade as Self-Correction at Small-to-Mid Scale](../../archive/papers/2026/arxiv-2608-04355/summary.md) — Decomposes measured self-correction gains into a content margin and format-recovery margins, and shows causally that most of what the field has reported as self-correction is answer-parseability repair.
- [Measuring Chain-of-Thought Monitorability Through Faithfulness and Verbosity](../../archive/papers/2025/local-2f98d1e607e7b1dd/summary.md) — Argues that faithfulness alone is insufficient for CoT monitoring and adds verbosity — whether the trace lists every factor needed to solve the task — combining the two into a monitorability score, then shows models can look faithful while omitting key factors.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
