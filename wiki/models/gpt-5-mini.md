# GPT-5-mini

<!-- auto:begin -->

A small GPT-5 variant appearing twice in this archive as a panel member. In the observability-ladder work it is among the models whose completed reasoning runs are held fixed while what a monitor may inspect is varied, producing that paper's finding that a self-summary's value nearly vanishes once the monitor already has the prompt. In the reasoning-trace extraction work it appears in the cross-model compatibility map, where the GPT-5 generation's traces are replayable by the newer series but not the reverse. Neither source reports a result attributed to it individually or describes the model.

- **Kind**: model
- **Also called**: GPT-5-mini
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md)
- **Sources**: 2

**Related**: [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [Claude Haiku 4.5](claude-haiku-4-5.md), [Claude Sonnet 4.5](claude-sonnet-4-5.md), [Claude Sonnet 4.6](claude-sonnet-4-6.md), [Gemini-3.1-Pro](gemini-3-1-pro.md), [Gemini-3.5-Flash](gemini-3-5-flash.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-5](gpt-5.md), [gpt-5.6-luna](gpt-5-6-luna.md), [GPT-5.6-Sol](gpt-5-6-sol.md), [GPT-5.6 Terra](gpt-5-6-terra.md), [gpt-oss-120b](gpt-oss-120b.md), [gpt-oss-20b](gpt-oss-20b.md), [Humanity's Last Exam](../datasets/humanity-s-last-exam.md), [knowledge distillation](../methods/knowledge-distillation.md), [linear probe](../methods/linear-probe.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [logistic regression](../methods/logistic-regression.md), [MMLU-Pro](../datasets/mmlu-pro.md), [monitorability](../concepts/monitorability.md), [o4-mini](o4-mini.md), [Omni-MATH](../datasets/omni-math.md), [persistent semantic entity](../concepts/persistent-semantic-entity.md), [prompt injection](../concepts/prompt-injection.md), [Qwen3-14B](qwen3-14b.md), [Qwen3-4B](qwen3-4b.md), [Qwen3-8B](qwen3-8b.md), [selective prediction](../concepts/selective-prediction.md), [self-correction](../concepts/self-correction.md), [TF-IDF](../methods/tf-idf.md), [verbosity](../concepts/verbosity.md)

## Appears in

- [How Much Does a Reasoning Summary Reveal? An Observability Ladder for Large Language Models](../../archive/papers/2026/arxiv-2608-02089/summary.md) — Holds one completed reasoning run fixed and varies only what a monitor is allowed to inspect — response, self-summary, full trace, internals — and finds the summary's value nearly vanishes once the monitor already has the prompt, so monitorability is a property of the display and the reader jointly rather than of the text.
- [Stealing Reasoning Traces from Proprietary LLM APIs](../../archive/papers/2026/arxiv-2608-09867/summary.md) — Shows that the encrypted reasoning blocks major providers return to clients are interchangeable across sessions, users and models within a provider, and measures four consequences of that interchangeability -- distillation, third-party secret extraction, hazardous-content exposure and monitor-invisible prompt injection -- before responsible disclosure closed it.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
