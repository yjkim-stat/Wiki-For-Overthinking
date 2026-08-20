# Qwen3.5-27B

<!-- auto:begin -->

A 27-billion-parameter Qwen model that appears in this archive as a comparison point in two papers, and whose most informative appearance is a near-null result. In the claim-level reliability work it is one of four models on competition mathematics, and the one already above 90 on three of its benchmarks: it gains at most 2.60 with a largest token saving of 14.5 percent, and the archive's reading records that the paper's headline framing rests on a different, weaker model while this one gains almost nothing -- so the method's benefit is conditional on the base consensus being unreliable. It is separately listed among the models LatentGuard compares itself against. Neither source describes the model itself.

- **Kind**: model
- **Also called**: Qwen3.5-27B
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [answer aggregation](../methods/answer-aggregation.md), [auditability](../concepts/auditability.md), [BeaverTails](../datasets/beavertails.md), [best-of-n](../methods/best-of-n.md), [CMIMC](../datasets/cmimc.md), [Coconut](../methods/coconut.md), [consensus](../concepts/consensus.md), [curriculum learning](../concepts/curriculum-learning.md), [gpt-oss-120b](gpt-oss-120b.md), [gpt-oss-20b](gpt-oss-20b.md), [HarmBench](../datasets/harmbench.md), [HMMT](../datasets/hmmt.md), [latent reasoning](../concepts/latent-reasoning.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [majority voting](../methods/majority-voting.md), [monitorability](../concepts/monitorability.md), [pass@k](../concepts/pass-k.md), [post-hoc rationalization](../concepts/post-hoc-rationalization.md), [process supervision](../concepts/process-supervision.md), [representation versus readout](../concepts/representation-versus-readout.md), [safety alignment](../concepts/safety-alignment.md), [self-consistency](../methods/self-consistency.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time scaling](../concepts/test-time-scaling.md), [XSTest](../datasets/xstest.md)

## Appears in

- [LatentGuard: Efficient and Inspectable Latent Reasoning for LLM Safeguards](../../archive/papers/2026/arxiv-2608-03838/summary.md) — Compresses a safety guard's textual rationales into continuous latent states by a staged curriculum, cutting 268 reasoning tokens to 1.60 and latency 8.9-fold, and adds an on-demand decoder that reconstructs a human-readable audit artifact — whose own ablation shows the artifact is anchored far more by the source text than by the latent states it is supposed to inspect.
- [Claim-Level Reliability Assessment for Efficient Test-Time Reasoning](../../archive/papers/2026/arxiv-2608-11994/summary.md) — Reallocates half of a test-time sampling budget from generating more solutions to asking the same model to refute a handful of decision-critical claims extracted from each trace, then weights the consensus vote by how many claims survive.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
