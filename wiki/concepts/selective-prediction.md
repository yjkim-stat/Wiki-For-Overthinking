# selective prediction

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [abstention](abstention.md), [ARC-Challenge](../datasets/arc-challenge.md), [calibration](../methods/calibration.md), [chain of thought faithfulness](chain-of-thought-faithfulness.md), [component ablation](../methods/component-ablation.md), [coverage](coverage.md), [difficulty conditioning](difficulty-conditioning.md), [difficulty stratification](../methods/difficulty-stratification.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-5-mini](../models/gpt-5-mini.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [gpt-oss-20b](../models/gpt-oss-20b.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [hallucination](hallucination.md), [linear probe](../methods/linear-probe.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [logistic regression](../methods/logistic-regression.md), [MATH](../datasets/math.md), [MMLU-Pro](../datasets/mmlu-pro.md), [monitorability](monitorability.md), [Omni-MATH](../datasets/omni-math.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-8B](../models/qwen3-8b.md), [reasoning boundary](reasoning-boundary.md), [reward shaping](reward-shaping.md), [self-correction](self-correction.md), [self-reflection](../methods/self-reflection.md), [StrategyQA](../datasets/strategyqa.md), [structured chain of thought](../methods/structured-chain-of-thought.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [TF-IDF](../methods/tf-idf.md), [verbosity](verbosity.md)

## Appears in

- [How Much Does a Reasoning Summary Reveal? An Observability Ladder for Large Language Models](../../archive/papers/2026/arxiv-2608-02089/summary.md) — Holds one completed reasoning run fixed and varies only what a monitor is allowed to inspect — response, self-summary, full trace, internals — and finds the summary's value nearly vanishes once the monitor already has the prompt, so monitorability is a property of the display and the reader jointly rather than of the text.
- [REIN: Bridging the Gap between Reasoning and Reliability via Reflection and Abstention Alignment](../../archive/papers/2026/arxiv-2608-07931/summary.md) — Separates hallucination into a reasoning failure and a knowledge failure, treats the first with a structured reflect-before-answering format and the second with a reward for abstaining when no sampled chain succeeds, and shows the two mechanisms are not interchangeable -- reflection alone never abstains, abstention alone never lowers the hallucination proxy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
