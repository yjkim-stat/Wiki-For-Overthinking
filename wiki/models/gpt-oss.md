# GPT-OSS

<!-- auto:begin -->

OpenAI's open-weight reasoning models, used in the archive as an object of study rather than as a tool. Both sources treat it as evidence about how vendors expose reasoning: its model card describes a response format with separate analysis, commentary and final channels, where the analysis channel corresponds to the intermediate tokens and the production models surface only a summary, which the position paper reads as frontier labs in practice declining to show unfiltered intermediate tokens. ReasonIF evaluates it behaviourally and finds it, like the other reasoning models tested, largely failing to follow instructions that apply inside its own reasoning trace.

- **Kind**: model
- **Also called**: gpt-oss, gpt-oss-120b, gpt-oss-20b
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [alignment](../concepts/alignment.md), [chain of thought](../methods/chain-of-thought.md), [controllability](../concepts/controllability.md), [DeepSeek-R1](deepseek-r1.md), [gpt-oss-20b](gpt-oss-20b.md), [GRPO](../methods/grpo.md), [instruction following](../concepts/instruction-following.md), [Llama](llama.md), [monitorability](../concepts/monitorability.md), [Monte Carlo tree search](../methods/monte-carlo-tree-search.md), [multi-turn reasoning](../methods/multi-turn-reasoning.md), [process reward model](../concepts/process-reward-model.md), [Qwen](qwen.md), [reward hacking](../concepts/reward-hacking.md), [RLVR](../methods/rlvr.md), [self-consistency](../methods/self-consistency.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [synthetic data generation](../methods/synthetic-data-generation.md), [test-time scaling](../methods/test-time-scaling.md)

## Appears in

- [ReasonIF: Large Reasoning Models Fail to Follow Instructions During Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1456/summary.md) — Benchmarks whether reasoning models follow instructions inside their reasoning traces, finding under 25% compliance at best and worse as difficulty rises.
- [Position: Stop Anthropomorphizing Intermediate Tokens as Reasoning/Thinking Traces!](../../archive/papers/2026/local-e62f069bc5144f28/summary.md) — A position paper arguing that reading a reasoning model's intermediate tokens as 'reasoning' or 'thinking' is unsupported by the available evidence and actively harmful, and collating experiments in which trace semantics and solution accuracy come apart.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
