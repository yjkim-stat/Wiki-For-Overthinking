# instruction following

<!-- auto:begin -->

Doing what the prompt specifies, measured by the sources in three places and found weak in all of them. In the model's main response it degrades as reasoning capacity grows and as generation length increases. Inside the reasoning trace it is worse: the best instruction-following score stays below 0.25, and degrades further with task difficulty, though targeted finetuning raises one model from 0.11 to 0.27. As a judged quantity it is unreliable in a different way, since LLM-judge preference scores do not correlate with concrete instruction-following measures because judges respond to style. So the capability is weak and the standard way of measuring it is also weak.

- **Kind**: concept
- **Also called**: IFS, directive compliance, instruction adherence
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [alignment](alignment.md), [alignment tax](alignment-tax.md), [AlpacaEval](../datasets/alpacaeval.md), [construct validity](construct-validity.md), [controllability](controllability.md), [DeepSeek-R1](../models/deepseek-r1.md), [GPT-OSS](../models/gpt-oss.md), [GPT-OSS-20B](../models/gpt-oss-20b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [meta-evaluation](meta-evaluation.md), [MMLU](../datasets/mmlu.md), [monitorability](monitorability.md), [MT-Bench](../datasets/mt-bench.md), [multi-turn reasoning](../methods/multi-turn-reasoning.md), [preference optimization](../methods/preference-optimization.md), [reinforcement learning post-training](../methods/reinforcement-learning-post-training.md), [reward hacking](reward-hacking.md), [supervised finetuning](../methods/supervised-finetuning.md), [synthetic data generation](../methods/synthetic-data-generation.md)

## Appears in

- [Scaling Reasoning, Losing Control: Evaluating Instruction Following in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1878/summary.md) — A benchmark showing that as reasoning capacity grows, instruction adherence falls, and that recovering obedience costs reasoning performance.
- [ReasonIF: Large Reasoning Models Fail to Follow Instructions During Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1456/summary.md) — Benchmarks whether reasoning models follow instructions inside their reasoning traces, finding under 25% compliance at best and worse as difficulty rises.
- [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](../../archive/papers/2025/local-503d1e9598036375/summary.md) — Builds a large standardized meta-benchmark and finds that LLM-judge preference scores do not correlate with concrete measures of safety, world knowledge or instruction following, because judges systematically prioritize style over factuality and safety.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
