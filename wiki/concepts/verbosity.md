# verbosity

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [BBH](../datasets/bbh.md), [chain of thought faithfulness](chain-of-thought-faithfulness.md), [DeepSeek-R1](../models/deepseek-r1.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [inverse scaling](inverse-scaling.md), [linear probe](../methods/linear-probe.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MMLU](../datasets/mmlu.md), [MMLU-Pro](../datasets/mmlu-pro.md), [monitorability](monitorability.md), [Omni-MATH](../datasets/omni-math.md), [post-hoc rationalization](post-hoc-rationalization.md), [QwQ-32B](../models/qwq-32b.md), [self-correction](self-correction.md), [sycophancy](sycophancy.md)

## Appears in

- [How Much Does a Reasoning Summary Reveal? An Observability Ladder for Large Language Models](../../archive/papers/2026/arxiv-2608-02089/summary.md) — Holds one completed reasoning run fixed and varies only what a monitor is allowed to inspect — response, self-summary, full trace, internals — and finds the summary's value nearly vanishes once the monitor already has the prompt, so monitorability is a property of the display and the reader jointly rather than of the text.
- [Measuring Chain-of-Thought Monitorability Through Faithfulness and Verbosity](../../archive/papers/2025/local-2f98d1e607e7b1dd/summary.md) — Argues that faithfulness alone is insufficient for CoT monitoring and adds verbosity — whether the trace lists every factor needed to solve the task — combining the two into a monitorability score, then shows models can look faithful while omitting key factors.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
