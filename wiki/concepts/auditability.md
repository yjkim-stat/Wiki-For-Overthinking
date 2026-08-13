# auditability

<!-- auto:begin -->

Whether a third party can check a claim rather than take it on trust, which the two sources locate at two different levels. One is about a single output: a compressed reasoning model can return a correct answer whose supporting derivation has been destroyed, so the visible trace no longer lets a reader tell whether the answer is reliable — and it argues this bites hardest in clinical or other high-stakes decision support, where a correct-looking output should only be used if its evidential basis can be inspected. The other is about a research field: mechanistic interpretability has no standardized system for auditing experiments, which the paper grounds in two papers reaching conflicting conclusions with nothing available to resolve them, and proposes continuous collaborative reviewing with source-based claim tracking. The shared claim is that a finding which cannot be checked cannot be certified, however accurate it happens to be.

- **Kind**: concept
- **Also called**: auditable
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [BeaverTails](../datasets/beavertails.md), [causal intervention](causal-intervention.md), [chain of thought faithfulness](chain-of-thought-faithfulness.md), [Coconut](../methods/coconut.md), [curriculum learning](curriculum-learning.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [HarmBench](../datasets/harmbench.md), [KV cache compression](../methods/kv-cache-compression.md), [latent reasoning](latent-reasoning.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [mechanistic interpretability](mechanistic-interpretability.md), [meta-evaluation](meta-evaluation.md), [monitorability](monitorability.md), [post-hoc rationalization](post-hoc-rationalization.md), [Qwen3-30B-A3B](../models/qwen3-30b-a3b.md), [Qwen3.5-27B](../models/qwen3-5-27b.md), [Qwen3-8B](../models/qwen3-8b.md), [representation versus readout](representation-versus-readout.md), [reproducibility](reproducibility.md), [safety alignment](safety-alignment.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [XSTest](../datasets/xstest.md)

## Appears in

- [Does Accuracy Equal Evidence? Reasoning Faithfulness under KV Cache Compression](../../archive/papers/2026/arxiv-2608-01631/summary.md) — Replays one fixed reasoning trace through eleven KV cache compression methods and finds that the ones preserving final-answer accuracy are largely the ones destroying the reasoning that supports it — on AIME the accuracy ranking of compressors correlates with their chain-validity ranking at Spearman -0.95.
- [LatentGuard: Efficient and Inspectable Latent Reasoning for LLM Safeguards](../../archive/papers/2026/arxiv-2608-03838/summary.md) — Compresses a safety guard's textual rationales into continuous latent states by a staged curriculum, cutting 268 reasoning tokens to 1.60 and latency 8.9-fold, and adds an on-demand decoder that reconstructs a human-readable audit artifact — whose own ablation shows the artifact is anchored far more by the source text than by the latent states it is supposed to inspect.
- [Make Mechanistic Interpretability Auditable: A Call to Develop Guidelines via Continuous Collaborative Reviewing](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-159/summary.md) — A position paper arguing mechanistic interpretability cannot be used in safety-critical settings until its findings are auditable, and proposing continuous collaborative reviewing plus source-based claim tracking.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
