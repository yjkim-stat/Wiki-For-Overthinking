# DeepSeek-R1

<!-- auto:begin -->

The reasoning model trained by pure reinforcement learning on verifiable outcomes, without human reasoning trajectories, and the reference point for most of this archive. Beyond originating the setting, it appears here as a measured subject: it is the most monitorable of eight models tested, at 78.3% average monitorability, and it is among the frontier systems that hold up best under symbolic variation of benchmark problems, losing 3.6% on a variabilized AMC23 where 7B RL-tuned models lose 20-95%.

- **Kind**: model
- **Also called**: DeepSeek R1
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [AIME24](../datasets/aime24.md), [alignment](../concepts/alignment.md), [AMC23](../datasets/amc23.md), [answer stabilization](../concepts/answer-stabilization.md), [BBH](../datasets/bbh.md), [chain of thought](../methods/chain-of-thought.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [controllability](../concepts/controllability.md), [Dynasor](../methods/dynasor.md), [early exit](../methods/early-exit.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-OSS](gpt-oss.md), [gpt-oss-20b](gpt-oss-20b.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [instruction following](../concepts/instruction-following.md), [inverse scaling](../concepts/inverse-scaling.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama](llama.md), [Llama-3.1-70B](llama-3-1-70b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [monitorability](../concepts/monitorability.md), [Monte Carlo tree search](../methods/monte-carlo-tree-search.md), [multi-turn reasoning](../methods/multi-turn-reasoning.md), [overthinking](../concepts/overthinking.md), [post-hoc rationalization](../concepts/post-hoc-rationalization.md), [Qwen](qwen.md), [Qwen2.5-7B](qwen2-5-7b.md), [QwQ-32B](qwq-32b.md), [reinforcement learning with verifiable rewards](../concepts/reinforcement-learning-with-verifiable-rewards.md), [reward hacking](../concepts/reward-hacking.md), [self-consistency](../methods/self-consistency.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [sycophancy](../concepts/sycophancy.md), [synthetic data generation](../methods/synthetic-data-generation.md), [test-time compute](../concepts/test-time-compute.md), [test-time scaling](../methods/test-time-scaling.md), [verbosity](../concepts/verbosity.md)

## Appears in

- [ReasonIF: Large Reasoning Models Fail to Follow Instructions During Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1456/summary.md) — Benchmarks whether reasoning models follow instructions inside their reasoning traces, finding under 25% compliance at best and worse as difficulty rises.
- [Efficiently Scaling LLM Reasoning with Certaindex](../../archive/papers/2025/local-0c24c3c0e4729108/summary.md) — Defines certaindex, an algorithm-agnostic measure of how much a reasoning algorithm's answer has stopped changing, and builds it into a serving system that reallocates or terminates compute per query — saving up to 50% of tokens in batch inference and tripling online throughput.
- [Measuring Chain-of-Thought Monitorability Through Faithfulness and Verbosity](../../archive/papers/2025/local-2f98d1e607e7b1dd/summary.md) — Argues that faithfulness alone is insufficient for CoT monitoring and adds verbosity — whether the trace lists every factor needed to solve the task — combining the two into a monitorability score, then shows models can look faithful while omitting key factors.
- [Position: Stop Anthropomorphizing Intermediate Tokens as Reasoning/Thinking Traces!](../../archive/papers/2026/local-e62f069bc5144f28/summary.md) — A position paper arguing that reading a reasoning model's intermediate tokens as 'reasoning' or 'thinking' is unsupported by the available evidence and actively harmful, and collating experiments in which trace semantics and solution accuracy come apart.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
