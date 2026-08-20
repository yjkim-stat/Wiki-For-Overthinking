# alignment

<!-- auto:begin -->

Used loosely across the sources, and in two incompatible senses. One treats it as adherence to what the user asked for, measured inside the reasoning trace, and finds fewer than 25% of traces comply with a given instruction. The other treats it as the property that LLM-judge preference scores are supposed to track, and finds those scores do not correlate with concrete measures of safety, world knowledge or instruction following, because judges respond to style. Read together the two say that the word names both a target and the measurement of that target, and that the measurement is unreliable — so a claim about alignment is only as good as whichever sense it meant.

- **Kind**: concept
- **Also called**: aligned behaviour
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [AlpacaEval](../datasets/alpacaeval.md), [chain of thought](chain-of-thought.md), [construct validity](construct-validity.md), [controllability](controllability.md), [DeepSeek-R1](../models/deepseek-r1.md), [GPT-OSS](../models/gpt-oss.md), [gpt-oss-20b](../models/gpt-oss-20b.md), [instruction following](instruction-following.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [meta-evaluation](meta-evaluation.md), [MMLU](../datasets/mmlu.md), [monitorability](monitorability.md), [MT-Bench](../datasets/mt-bench.md), [multi-turn reasoning](../methods/multi-turn-reasoning.md), [preference optimization](../methods/preference-optimization.md), [reward hacking](reward-hacking.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [synthetic data generation](../methods/synthetic-data-generation.md)

## Appears in

- [ReasonIF: Large Reasoning Models Fail to Follow Instructions During Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1456/summary.md) — Benchmarks whether reasoning models follow instructions inside their reasoning traces, finding under 25% compliance at best and worse as difficulty rises.
- [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](../../archive/papers/2025/local-503d1e9598036375/summary.md) — Builds a large standardized meta-benchmark and finds that LLM-judge preference scores do not correlate with concrete measures of safety, world knowledge or instruction following, because judges systematically prioritize style over factuality and safety.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
