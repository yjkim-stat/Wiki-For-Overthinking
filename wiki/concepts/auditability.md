# auditability

<!-- auto:begin -->

Whether a system's reasoning can be checked after the fact, and across 3 sources a property the archive treats as a design constraint that other objectives trade against. Its clearest cost is the compression case: methods preserving final-answer accuracy are largely the ones destroying the reasoning that supports it, with accuracy and chain validity correlating at Spearman -0.95 on one benchmark, so an accuracy-based leaderboard would order compressors almost exactly backwards on auditability. Its clearest attempted remedy is a latent safeguard that compresses rationales into continuous states and adds an on-demand decoder producing a human-readable audit artifact -- whose own ablation shows the artifact anchored far more by the source text than by the latent states it is supposed to inspect, so the audit trail is reconstructed rather than read. The third source argues the field itself needs auditing guidelines developed by continuous collaborative review, which is the archive's own position stated as a proposal.

- **Kind**: concept
- **Also called**: auditable, inspectability
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [BeaverTails](../datasets/beavertails.md), [causal intervention](../methods/causal-intervention.md), [chain of thought faithfulness](chain-of-thought-faithfulness.md), [Coconut](../methods/coconut.md), [curriculum learning](../methods/curriculum-learning.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [HarmBench](../datasets/harmbench.md), [KV cache compression](../methods/kv-cache-compression.md), [latent reasoning](latent-reasoning.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [mechanistic interpretability](mechanistic-interpretability.md), [MedCalc-Bench](../datasets/medcalc-bench.md), [meta-evaluation](meta-evaluation.md), [monitorability](monitorability.md), [post-hoc rationalization](post-hoc-rationalization.md), [Qwen3-30B-A3B](../models/qwen3-30b-a3b.md), [Qwen3.5-27B](../models/qwen3-5-27b.md), [Qwen3-8B](../models/qwen3-8b.md), [representation versus readout](representation-versus-readout.md), [reproducibility](reproducibility.md), [safety alignment](safety-alignment.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [XSTest](../datasets/xstest.md)

## Appears in

- [Does Accuracy Equal Evidence? Reasoning Faithfulness under KV Cache Compression](../../archive/papers/2026/arxiv-2608-01631/summary.md) — Replays one fixed reasoning trace through eleven KV cache compression methods and finds that the ones preserving final-answer accuracy are largely the ones destroying the reasoning that supports it — on AIME the accuracy ranking of compressors correlates with their chain-validity ranking at Spearman -0.95.
- [LatentGuard: Efficient and Inspectable Latent Reasoning for LLM Safeguards](../../archive/papers/2026/arxiv-2608-03838/summary.md) — Compresses a safety guard's textual rationales into continuous latent states by a staged curriculum, cutting 268 reasoning tokens to 1.60 and latency 8.9-fold, and adds an on-demand decoder that reconstructs a human-readable audit artifact — whose own ablation shows the artifact is anchored far more by the source text than by the latent states it is supposed to inspect.
- [Make Mechanistic Interpretability Auditable: A Call to Develop Guidelines via Continuous Collaborative Reviewing](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-159/summary.md) — A position paper arguing mechanistic interpretability cannot be used in safety-critical settings until its findings are auditable, and proposing continuous collaborative reviewing plus source-based claim tracking.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
