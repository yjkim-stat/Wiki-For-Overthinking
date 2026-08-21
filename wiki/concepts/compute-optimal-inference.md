# Compute-optimal inference

<!-- auto:begin -->

Unlike the archive's other 'compute-optimal' entries, all three sources here mean it strictly at inference time: choosing, per query, how much decoding compute to spend and in what shape, so that accuracy per FLOP is maximised. Inference Scaling Laws sets the frame empirically by plotting accuracy against FLOPs for greedy decoding, sampling with majority and weighted voting, best-of-n and tree search across model sizes, and adds REBASE, a reward-guided tree search. The other two make the choice predictive rather than measured after the fact: one trains a roughly 1B-parameter multimodal model to predict, before any API call, which of seven performance bins a frontier model will land in for a (document, prompt, model, reasoning budget) tuple; Sonata predicts a query's self-consistency from the last-layer hidden state at prefill and sets the thinking budget before reasoning starts. The shared assumption is that the right budget is a property of the query that can be estimated in advance.

- **Kind**: concept
- **Also called**: Compute-Optimal Inference
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [accuracy-efficiency tradeoff](accuracy-efficiency-tradeoff.md), [adaptive test-time compute](adaptive-test-time-compute.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [Best-of-N](../methods/best-of-n.md), [Compute-optimal allocation](compute-optimal-allocation.md), [Compute-Optimal Scaling](compute-optimal-scaling.md), [GPQA](../datasets/gpqa.md), [gpt-oss-120b](../methods/gpt-oss-120b.md), [GSM8K](../datasets/gsm8k.md), [Majority Voting](../methods/majority-voting.md), [MATH500](../datasets/math500.md), [MBPP](../datasets/mbpp.md), [process reward model](process-reward-model.md), [Qwen3-8B](../methods/qwen3-8b.md), [Self-Consistency](../methods/self-consistency.md), [Test-Time Compute Scaling](test-time-compute-scaling.md), [Test-time scaling](test-time-scaling.md), [Tree Search Decoding](tree-search-decoding.md), [weighted voting](weighted-voting.md)

## Appears in

- [Can a Lightweight Multimodal Model Estimate LLM Reasoning Performance? A Study for Compute-Optimal Document Inference](../../archive/papers/2026/arxiv-2608-18591/summary.md) — Trains a ~1B-parameter multimodal model to predict, before any API call, which of seven performance bins a frontier LLM will land in for a given (document, prompt, model, reasoning budget) tuple, and uses those predictions to pick a per-sample reasoning budget for document tasks.
- [Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving](../../archive/papers/2025/title-0d818df77a2dc810/summary.md) — An empirical study of compute-optimal inference that measures accuracy against FLOPs for greedy decoding, sampling with majority and weighted voting, best-of-n and tree search across model sizes, and introduces REBASE, a reward-guided tree search.
- [Adaptive Thinking: Large Language Models Know When to Think in Latent Space](../../archive/papers/2026/title-cc91145094e2b147/summary.md) — Sonata predicts a query's self-consistency from the last-layer hidden state at prefill and uses that prediction to set the thinking budget before the model starts reasoning.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
