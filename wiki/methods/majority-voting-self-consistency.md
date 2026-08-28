# majority voting / self-consistency

<!-- auto:begin -->

A parallel test-time-scaling technique that samples multiple independent reasoning attempts for the same question and selects the most common answer. Sources study it as the dominant scaling mechanism in prompting-strategy comparisons (finding plain CoT eventually beats more elaborate strategies under equal majority-vote budget) and as one axis (alongside best-of-n and tree search) in compute-optimal inference-scaling-law studies measuring accuracy against FLOPs.

- **Kind**: method
- **Also called**: majority vote, self-consistency
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [AIME](../datasets/aime.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [best-of-N](best-of-n.md), [Compute-optimal inference](../concepts/compute-optimal-inference.md), [Direct Prompting](direct-prompting.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [greedy decoding](greedy-decoding.md), [GSM-Hard](../datasets/gsm-hard.md), [GSM8K](../datasets/gsm8k.md), [HumanEval](../datasets/humaneval.md), [Majority Voting](majority-voting.md), [MATH500](../datasets/math500.md), [MBPP](../datasets/mbpp.md), [Multi-Agent Debate](multi-agent-debate.md), [OlympiadBench](../datasets/olympiadbench.md), [Phi-decoding](phi-decoding.md), [process reward model](process-reward-model.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen2.5-Math-7B-Instruct](../models/qwen2-5-math-7b-instruct.md), [Qwen3-8B](../models/qwen3-8b.md), [self-refine](self-refine.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [Tree Search Decoding](../concepts/tree-search-decoding.md), [weighted voting](../concepts/weighted-voting.md)

## Appears in

- [Rethinking the Role of Prompting Strategies in LLM Test-Time Scaling: A Perspective of Probability Theory](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-1356/summary.md) — Systematically compares 8 prompting strategies under equal sampling budget for majority-vote test-time scaling across 6 LLMs x 6 benchmarks, finding plain Chain-of-Thought eventually dominates every more elaborate strategy as sampling time N grows -- because CoT has more easy/fewer hard questions and a flatter wrong-answer distribution -- and shows combining per-question difficulty-adaptive scaling with per-question optimal-strategy selection lifts GSM8K accuracy from 86.0% to 97.4% (Majority@10) and MATH-500 from 15.2% to 61.0%.
- [ThinkBooster: A Unified Framework for Seamless Test-Time Scaling of LLM Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-demo-70/summary.md) — ThinkBooster is a unified, open-source framework (Python library + OpenAI-compatible proxy endpoint + visual debugger) implementing 9 test-time-compute scaling strategies and 4 scorer families under a joint TFLOPs-and-tokens compute-accounting benchmark, whose pilot study finds PRM scorers dominate on math while lightweight uncertainty scorers are surprisingly competitive on (out-of-domain-for-PRM) coding tasks, and that beam search often underperforms best-of-N and even self-consistency despite costing more compute.
- [Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving](../../archive/papers/2025/title-0d818df77a2dc810/summary.md) — An empirical study of compute-optimal inference that measures accuracy against FLOPs for greedy decoding, sampling with majority and weighted voting, best-of-n and tree search across model sizes, and introduces REBASE, a reward-guided tree search.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
