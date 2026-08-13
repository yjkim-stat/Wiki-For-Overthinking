# BBH

<!-- auto:begin -->

A multi-task reasoning benchmark that the sources use as the legible, non-frontier end of an evaluation suite rather than as a hard test. One finds dataset difficulty inversely related to monitorability and ranks BBH highest of its sets with GPQA-Diamond lowest, so a trace produced on BBH is the most likely to enumerate the factors that actually decide the answer. The other includes it in a seven-benchmark sweep in which a norm-based steering signal leads on AIME, GPQA and MMLU-Pro while an SAE-based one wins BBH and GSM-Plus, so interventions separate on it rather than agreeing. Under the fuller name the archive holds a third use: 13 of its tasks are the setting in which biasing the prompt drops accuracy by as much as 36 percent while the model's explanation rationalizes the biased answer.

- **Kind**: dataset
- **Also called**: BBH tasks, BIG-Bench Hard
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [activation steering](../methods/activation-steering.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [Gemma-3-4B](../models/gemma-3-4b.md), [GPQA](gpqa.md), [GPQA-Diamond](gpqa-diamond.md), [GSM8K](gsm8k.md), [inverse scaling](../concepts/inverse-scaling.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MMLU](mmlu.md), [MMLU-Pro](mmlu-pro.md), [monitorability](../concepts/monitorability.md), [overthinking](../concepts/overthinking.md), [post-hoc rationalization](../concepts/post-hoc-rationalization.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-8B](../models/qwen3-8b.md), [QwQ-32B](../models/qwq-32b.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [sycophancy](../concepts/sycophancy.md), [TruthfulQA](truthfulqa.md), [verbosity](../concepts/verbosity.md)

## Appears in

- [Measuring Chain-of-Thought Monitorability Through Faithfulness and Verbosity](../../archive/papers/2025/local-2f98d1e607e7b1dd/summary.md) — Argues that faithfulness alone is insufficient for CoT monitoring and adds verbosity — whether the trace lists every factor needed to solve the task — combining the two into a monitorability score, then shows models can look faithful while omitting key factors.
- [The Tell-Tale Norm: L2 Magnitude as a Signal for Reasoning Dynamics in Large Language Models](../../archive/papers/2026/local-f92e5f936a3c7422/summary.md) — Argues that the L2 norm of a hidden state is a training-free proxy for how hard a model is reasoning at that layer and token, proves it bounds the activation of SAE-identified reasoning features, and uses norm peaks to decide where to recurse a layer, where to steer, and which sampled response to keep.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
