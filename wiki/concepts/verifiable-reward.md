# verifiable reward

<!-- auto:begin -->

A reward computed by a programmatic check rather than by a model's judgement, and in both sources the ingredient that makes a search or a policy update trustworthy without a judge in the loop. One verifies every numerical claim in a generated report by writing and executing a query against the source table and comparing within a one-percent tolerance, and checks chart fidelity by executing the chart code and re-reading the rendered values — stating explicitly that this avoids a reward-hacking loop with the separate evaluator used for benchmarking. The other gates its reinforcement reward on response-format validity and exact answer correctness. Read together they mark the boundary of the idea: the dimensions a programmatic check can reach come close to expert performance in the first source, while the one it can only approximate — whether an insight is non-trivial — stays 27 points below and is the most frequent remaining error.

- **Kind**: concept
- **Also called**: rule-based reward, verifiable rewards
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [attention pattern](attention-pattern.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Coconut](../methods/coconut.md), [construct validity](construct-validity.md), [DeepSeek-R1](../models/deepseek-r1.md), [exploration](exploration.md), [Gemini-1.5-Pro](../models/gemini-1-5-pro.md), [Gemini-2.5-pro](../models/gemini-2-5-pro.md), [Gemini-3.5-Flash](../models/gemini-3-5-flash.md), [GPT-4o](../models/gpt-4o.md), [GPT-5](../models/gpt-5.md), [grounding](grounding.md), [GRPO](../methods/grpo.md), [Kimi-K2.5](../models/kimi-k2-5.md), [knowledge distillation](../methods/knowledge-distillation.md), [latent reasoning](latent-reasoning.md), [LLaVA-OneVision-7B](../models/llava-onevision-7b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [monitorability](monitorability.md), [Monte Carlo tree search](../methods/monte-carlo-tree-search.md), [multimodal reasoning](multimodal-reasoning.md), [process reward](process-reward.md), [process supervision](process-supervision.md), [Qwen2.5-VL-7B-Instruct](../models/qwen2-5-vl-7b-instruct.md), [Qwen3-VL-235B](../models/qwen3-vl-235b.md), [reward hacking](reward-hacking.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [TempCompass](../datasets/tempcompass.md), [test-time scaling](test-time-scaling.md), [visual grounding](visual-grounding.md)

## Appears in

- [Monte Carlo Tree Search for Table-to-Multimodal Report Generation](../../archive/papers/2026/arxiv-2608-04071/summary.md) — Turns table-to-report generation into Monte Carlo tree search over partial reports, scored by a reward that verifies every numerical claim by generating and executing SQL against the source table rather than by asking a judge — and keeps that search reward strictly separate from the benchmark's own evaluator to avoid a reward-hacking loop.
- [Perception Before Reasoning: Dynamic Latent Reasoning for Video Understanding and Question Answering](../../archive/papers/2026/arxiv-2608-04124/summary.md) — Splits a video model's latent computation into perception latents that always ground the question in visual evidence and reasoning latents allocated only when the question needs inference, and shows that reasoning latents without rationale supervision are worse than no reasoning latents at all.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
