# process reward model

<!-- auto:begin -->

A reward model that scores the intermediate steps of a reasoning trace, used to guide test-time search rather than only rank finished answers. MetaStone-S1 shares one backbone between its policy and process-reward model; TaTToo trains a domain-specific PRM for tabular reasoning; JETTS benchmarks how well LLM-as-judge models substitute for a trained PRM in guiding test-time scaling, finding judges match outcome reward models but lag PRMs. Note: same concept as the archive's separately-tracked 'process reward model (PRM)' entry -- not merged.

- **Kind**: concept
- **Also called**: PRM, Process Reward Model, Process reward model, process reward model (PRM)
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 7

**Related**: [Accuracy-Efficiency Tradeoff](accuracy-efficiency-tradeoff.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Best-of-N](../methods/best-of-n.md), [Compute-optimal inference](compute-optimal-inference.md), [confidence-based early stopping](../methods/confidence-based-early-stopping.md), [DeepSeek-R1-Distill-Llama-8B](../methods/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-7B](../methods/deepseek-r1-distill-qwen-7b.md), [GPQA](../datasets/gpqa.md), [GSM8K](../datasets/gsm8k.md), [KV cache compression](../methods/kv-cache-compression.md), [LLM-as-a-Judge](../methods/llm-as-a-judge.md), [majority voting](../methods/majority-voting.md), [MATH-500](../datasets/math-500.md), [MBPP](../datasets/mbpp.md), [Monte Carlo Tree Search](../methods/monte-carlo-tree-search.md), [overthinking](overthinking.md), [process reward model (PRM)](process-reward-model-prm.md), [Qwen3-8B](../methods/qwen3-8b.md), [R-KV](../methods/r-kv.md), [test-time compute scaling](test-time-compute-scaling.md), [test-time scaling](test-time-scaling.md), [tree-search decoding](tree-search-decoding.md), [vLLM](../methods/vllm.md), [weighted voting](weighted-voting.md)

## Appears in

- [Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning](../../archive/papers/2026/arxiv-2608-04771/summary.md) — ReCo uses a 30M process-reward estimator to set, per reasoning step, both the KV-cache retention ratio and generation-side controls (a reflection-token logit penalty and confidence-based early stopping), cutting generated tokens by 37-65% and end-to-end latency by 2.08-2.35x versus full-cache CoT.
- [Reasoning Jury: Multi-Model Consensus for Evaluating Reasoning Traces](../../archive/papers/2026/arxiv-2608-12585/summary.md) — Replaces the single LLM judge of a long reasoning trace with a panel of jurors that first judge independently and then reach consensus through a blind moderator's deliberation or a consolidation pass, letting cheap open-weight models beat frontier single judges at step-level defect localization for a fraction of the dollar cost.
- [Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving](../../archive/papers/2025/title-0d818df77a2dc810/summary.md) — An empirical study of compute-optimal inference that measures accuracy against FLOPs for greedy decoding, sampling with majority and weighted voting, best-of-n and tree search across model sizes, and introduces REBASE, a reward-guided tree search.
- [Test-Time Scaling with Reflective Generative Model](../../archive/papers/2026/title-5ff343d0a198bd25/summary.md) — Proposes a reasoning model (MetaStone-S1) whose policy and process-reward model share one backbone, and which exposes selectable low/medium/high reasoning-effort modes that trade off thinking length against test-time performance, matching OpenAI o3-mini on math benchmarks at 32B parameters.
- [TaTToo: Tool-Grounded Thinking PRM for Test-Time Scaling in Tabular Reasoning](../../archive/papers/2026/title-983af40bdcebe387/summary.md) — TaTToo trains a table-grounded, tool-verified process reward model that supervises test-time-scaling search for large reasoning models on tabular reasoning tasks.
- [Evaluating Judges as Evaluators: The JETTS Benchmark of LLM-as-Judges as Test-Time Scaling Evaluators](../../archive/papers/2025/title-ab80eef8a7c42e7c/summary.md) — JETTS is a benchmark evaluating how well LLM-as-judge models perform as evaluators guiding test-time-scaling methods -- response reranking, step-level beam search, and critique-based refinement -- across math, code and instruction-following.
- [ContextPRM: Leveraging Contextual Coherence for multi-domain Test-Time Scaling](../../archive/papers/2026/title-da31eb8bef16ddcc/summary.md) — Trains a process reward model that scores chain-of-thought coherence instead of domain knowledge, and uses it to weight votes among sampled reasoning chains for test-time scaling across math and non-math domains.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
