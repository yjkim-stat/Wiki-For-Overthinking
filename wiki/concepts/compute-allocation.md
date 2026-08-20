# compute allocation

<!-- auto:begin -->

Treating inference compute as a resource to place rather than a quantity to increase -- the question of where an extra unit goes, not how many to spend. Both sources arrive at it by finding that uniform spending is the waste: one shows parallel sampling gives most of its budget to trajectories that will be wrong and reallocates capacity from pruned traces onto high-scoring prefixes under a fixed hardware cap, while the other shows compute bought at evaluation time can substitute for compute bought at generation time. The framing is what makes hardware constraints part of the problem statement rather than an implementation detail: concurrency and KV-cache footprint bound the population of live trajectories, so allocation is zero-sum.

- **Kind**: concept
- **Also called**: budget allocation, compute allocation
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [answer aggregation](../methods/answer-aggregation.md), [beam search](../methods/beam-search.md), [best-of-n](../methods/best-of-n.md), [DeepSeek-R1-0528-Qwen3-8B](../models/deepseek-r1-0528-qwen3-8b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-2](../models/gpt-2.md), [HMMT](../datasets/hmmt.md), [judge reliability](judge-reliability.md), [KV cache](kv-cache.md), [linear probe](../methods/linear-probe.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [meta-evaluation](meta-evaluation.md), [Monte Carlo tree search](../methods/monte-carlo-tree-search.md), [process evaluation](../methods/process-evaluation.md), [process reward model](process-reward-model.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [reranking](../methods/reranking.md), [self-consistency](../methods/self-consistency.md), [test-time compute](test-time-compute.md), [test-time scaling](test-time-scaling.md), [trajectory diversity](trajectory-diversity.md), [verification](verification.md), [vLLM](../methods/vllm.md)

## Appears in

- [Thought-Level Beam Search for Reasoning](../../archive/papers/2026/arxiv-2608-08020/summary.md) — Reformulates test-time reasoning as compute allocation over partial trajectories under a hardware budget, and runs a zero-sum beam search over reasoning steps that prunes weak traces and immediately re-spends the freed capacity by branching from high-scoring prefixes.
- [Efficient Test-Time Scaling for LLM-based Time Series Forecasting](../../archive/papers/2026/arxiv-2608-08675/summary.md) — Replaces open-ended iterative refinement in LLM time-series forecasting with a fixed-step coarse-to-fine loop anchored to an explicitly predicted downscaled future shape, so test-time compute is spent enriching detail rather than re-deciding the global trajectory.
- [Scaling Evaluation-Time Compute with Reasoning Models as Evaluators](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2102/summary.md) — Shows evaluator accuracy improves monotonically with reasoning tokens spent, and that buying compute at evaluation time can substitute for buying it at generation time.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
