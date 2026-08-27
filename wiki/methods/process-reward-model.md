# process reward model

<!-- auto:begin -->

A model that scores the intermediate steps of a reasoning trace rather than only its final answer, used in this archive to guide search and to decide where compute should go. Its recurring problem here is cost on two axes: training one normally needs step-level annotations, and running it consumes part of the very budget the search is trying to spend well -- sources are explicit that a search's quality is bounded by its PRM and that the PRM's own cost belongs in the accounting. The responses in the archive are to avoid the annotations (deriving process scores from the outcome reward, or sharing one backbone between policy and scorer at about 50M extra parameters) or to avoid the model (routing cheap answer-agreement evidence and reserving verifier calls).

- **Kind**: method
- **Also called**: PRM, Process Reward Model, Process reward model, process reward model (PRM), process reward models, step-level reward model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 8

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [best-of-N](best-of-n.md), [Compute-optimal inference](../concepts/compute-optimal-inference.md), [Confidence-based early stopping](confidence-based-early-stopping.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [Dynasor](dynasor.md), [GPQA](../datasets/gpqa.md), [GSM8K](../datasets/gsm8k.md), [KV-cache compression](kv-cache-compression.md), [LLM-as-a-Judge](llm-as-a-judge.md), [Majority Voting](majority-voting.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MBPP](../datasets/mbpp.md), [Overthinking](../concepts/overthinking.md), [process reward model (PRM)](../concepts/process-reward-model-prm.md), [Qwen3-8B](qwen3-8b.md), [R-KV](r-kv.md), [Reasoning Step Segmentation](reasoning-step-segmentation.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [Test-Time Scaling](../concepts/test-time-scaling.md), [Tree Search Decoding](../concepts/tree-search-decoding.md), [vLLM](vllm.md), [weighted voting](../concepts/weighted-voting.md)

## Appears in

- [Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning](../../archive/papers/2026/arxiv-2608-04771/summary.md) — ReCo uses a 30M process-reward estimator to set, per reasoning step, both the KV-cache retention ratio and generation-side controls (a reflection-token logit penalty and confidence-based early stopping), cutting generated tokens by 37-65% and end-to-end latency by 2.08-2.35x versus full-cache CoT.
- [Reasoning Jury: Multi-Model Consensus for Evaluating Reasoning Traces](../../archive/papers/2026/arxiv-2608-12585/summary.md) — Replaces the single LLM judge of a long reasoning trace with a panel of jurors that first judge independently and then reach consensus through a blind moderator's deliberation or a consolidation pass, letting cheap open-weight models beat frontier single judges at step-level defect localization for a fraction of the dollar cost.
- [Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving](../../archive/papers/2025/title-0d818df77a2dc810/summary.md) — An empirical study of compute-optimal inference that measures accuracy against FLOPs for greedy decoding, sampling with majority and weighted voting, best-of-n and tree search across model sizes, and introduces REBASE, a reward-guided tree search.
- [Test-Time Scaling with Reflective Generative Model](../../archive/papers/2026/title-5ff343d0a198bd25/summary.md) — Proposes a reasoning model (MetaStone-S1) whose policy and process-reward model share one backbone, and which exposes selectable low/medium/high reasoning-effort modes that trade off thinking length against test-time performance, matching OpenAI o3-mini on math benchmarks at 32B parameters.
- [TaTToo: Tool-Grounded Thinking PRM for Test-Time Scaling in Tabular Reasoning](../../archive/papers/2026/title-983af40bdcebe387/summary.md) — TaTToo is a table-grounded Process Reward Model that reasons explicitly over tabular operations and uses tool-based verification to supervise test-time scaling for tabular reasoning, improving downstream policy LRMs by 30.9% at inference.
- [Evaluating Judges as Evaluators: The JETTS Benchmark of LLM-as-Judges as Test-Time Scaling Evaluators](../../archive/papers/2025/title-ab80eef8a7c42e7c/summary.md) — JETTS is a benchmark evaluating how well LLM-as-judge models perform as evaluators guiding test-time-scaling methods -- response reranking, step-level beam search, and critique-based refinement -- across math, code and instruction-following.
- [T1: Tool-integrated Verification for Test-time Compute Scaling in Small Language Models](../../archive/papers/2026/title-b2629aee97cadc77/summary.md) — T1 is a two-stage test-time-scaling framework for small language models that filters candidate responses with external tools before a small-model verifier makes the final judgment, offloading memorization-heavy checks to the tools.
- [ContextPRM: Leveraging Contextual Coherence for multi-domain Test-Time Scaling](../../archive/papers/2026/title-da31eb8bef16ddcc/summary.md) — Trains a process reward model that scores chain-of-thought coherence instead of domain knowledge, and uses it to weight votes among sampled reasoning chains for test-time scaling across math and non-math domains.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
