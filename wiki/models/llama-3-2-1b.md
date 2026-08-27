# Llama-3.2-1B

<!-- auto:begin -->

Meta's 1B-parameter Llama 3.2 checkpoint, used in this archive as the smallest backbone in test-time-scaling and latent-reasoning experiments. Two roles recur. It is the standing demonstration that inference algorithm can substitute for parameters -- under one test-time-scaling method it outperforms the larger Llama-3.2-3B on MATH -- and it is the base for latent-reasoning work (COCONUT, CODI, SLPO) where accuracy is reported on GSM8K and MultiArith. A separate edge-systems source uses it to show the opposite end of the same tradeoff: at 1B the generator no longer dominates the per-query budget, with 33% of wall time and 39% of GPU energy spent in embedding and retrieval.

- **Kind**: model
- **Also called**: Llama-3.2 1B, Llama-3.2-1B-Instruct
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [COCONUT](../methods/coconut.md), [CODI](../methods/codi.md), [GSM8K](../datasets/gsm8k.md), [Latent reasoning](../concepts/latent-reasoning.md), [Llama-3.1-8B](llama-3-1-8b.md), [Recurrent Depth](../concepts/recurrent-depth.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md)

## Appears in

- [Penelope: Localized Latent Recurrence for Efficient Structured Reasoning](../../archive/papers/2026/arxiv-2607-25915/summary.md) — Penelope confines latent reasoning recurrence to a five-layer slice of a decoder-only Transformer, refining a fixed-size boundary memory K times instead of re-running the whole decoder or emitting a chain-of-thought trace.
- [Self-Training Elicits Concise Reasoning in Large Language Models](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-1289/summary.md) — Shows current LLMs already possess a latent capacity for concise reasoning -- shorter correct paths exist within their own stochastic output distribution -- and that self-training (fine-tuning on the model's own best-of-N and few-shot-conditioned concise samples, FS-BoN) reliably elicits this capacity, cutting output length 30% on average across five model families on GSM8K/MATH with preserved accuracy, far outperforming zero-shot 'be concise' prompting and training on externally-sourced concise data.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
