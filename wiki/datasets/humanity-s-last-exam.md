# Humanity's Last Exam

<!-- auto:begin -->

A benchmark of expert-level questions used in this archive as the hard end of an evaluation range, where absolute scores are low enough that small movements are hard to read. In the rarity-aware credit work it is one of the sets on which a GRPO variant is evaluated. In the reasoning-trace extraction work it supplies the 30 problems -- 15 STEM and 15 non-STEM -- on which partial reasoning prefixes from a frontier model are shown to shift an open model's visible answer style toward the source, with best-of-k n-gram overlap rising 0.15 on STEM and 0.086 on non-STEM against a control in which two open models prefill each other and nothing is significant. Neither source describes the benchmark's construction, and one archived reading elsewhere records a chain-of-thought baseline on it of 3.0 percent, which is the context in which its numbers should be read.

- **Kind**: dataset
- **Also called**: HLE
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [AIME](aime.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [Claude Haiku 4.5](../models/claude-haiku-4-5.md), [Claude Sonnet 4.5](../models/claude-sonnet-4-5.md), [Claude Sonnet 4.6](../models/claude-sonnet-4-6.md), [credit assignment](../concepts/credit-assignment.md), [entropy collapse](../concepts/entropy-collapse.md), [exploration](../concepts/exploration.md), [Gemini-3.1-Pro](../models/gemini-3-1-pro.md), [Gemini-3.5-Flash](../models/gemini-3-5-flash.md), [GPT-5](../models/gpt-5.md), [gpt-5.6-luna](../models/gpt-5-6-luna.md), [GPT-5.6-Sol](../models/gpt-5-6-sol.md), [GPT-5.6 Terra](../models/gpt-5-6-terra.md), [GPT-5-mini](../models/gpt-5-mini.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [knowledge distillation](../methods/knowledge-distillation.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [MATH](math.md), [MATH500](math500.md), [monitorability](../concepts/monitorability.md), [o4-mini](../models/o4-mini.md), [pass@k](../concepts/pass-k.md), [persistent semantic entity](../concepts/persistent-semantic-entity.md), [prompt injection](../concepts/prompt-injection.md), [Qwen2.5-32B-Instruct](../models/qwen2-5-32b-instruct.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [randomized control](../concepts/randomized-control.md), [reasoning boundary](../concepts/reasoning-boundary.md), [RLVR](../methods/rlvr.md), [trajectory diversity](../concepts/trajectory-diversity.md)

## Appears in

- [When Correct Solutions Repeat: Rarity-Aware Credit Redistribution for GRPO](../../archive/papers/2026/arxiv-2608-03467/summary.md) — Shows that GRPO's per-completion uniformity is frequency-skewed once credit is aggregated by solution structure — a recurring correct form accumulates positive coefficient mass proportional to how often it is sampled — and rebalances it by a rarity exponent over a partition built from deterministic cue signatures rather than a judge model.
- [Stealing Reasoning Traces from Proprietary LLM APIs](../../archive/papers/2026/arxiv-2608-09867/summary.md) — Shows that the encrypted reasoning blocks major providers return to clients are interchangeable across sessions, users and models within a provider, and measures four consequences of that interchangeability -- distillation, third-party secret extraction, hazardous-content exposure and monitor-invisible prompt injection -- before responsible disclosure closed it.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
