# reproducibility

<!-- auto:begin -->

Whether a reported result can be obtained again, which four sources treat as unresolved in different layers of the stack. At the hardware layer, greedy decoding is not deterministic across GPU type, GPU count or batch size, shifting AIME'24 accuracy by up to 9 percentage points on one model and benchmark. At the method layer, SAE features differ between training runs, which is proposed as a reported evaluation axis with a metric showing around 0.80 pairwise consistency is achievable. At the field layer, one source documents two papers concluding oppositely on one behaviour and calls for continuous auditing; another supplies shared tooling. The archive's own audit found 1 of 45 papers reporting precision and hardware, and 0 doing a variance decomposition.

- **Kind**: concept
- **Also called**: determinism, replicability, run-to-run consistency
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [activation patching](../methods/activation-patching.md), [AIME24](../datasets/aime24.md), [attention pattern](attention-pattern.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [greedy decoding](../methods/greedy-decoding.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [MATH500](../datasets/math500.md), [mechanistic interpretability](mechanistic-interpretability.md), [meta-evaluation](meta-evaluation.md), [monosemanticity](monosemanticity.md), [pass-k](../methods/pass-k.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-VL](../models/qwen3-vl.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [superposition](superposition.md), [vLLM](../methods/vllm.md)

## Appears in

- [Spectra: A Mechanistic Interpretability Library for Vision-Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-demo-78/summary.md) — An open library giving vision-language models the mechanistic-interpretability tooling that text-only models already have: activation patching, attention analysis and meta-functions behind one interface.
- [Make Mechanistic Interpretability Auditable: A Call to Develop Guidelines via Continuous Collaborative Reviewing](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-159/summary.md) — A position paper arguing mechanistic interpretability cannot be used in safety-critical settings until its findings are auditable, and proposing continuous collaborative reviewing plus source-based claim tracking.
- [Mechanistic Interpretability Should Prioritize Feature Consistency in Sparse Autoencoders](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-99/summary.md) — Argues run-to-run feature consistency should be a standard SAE evaluation axis alongside reconstruction and sparsity, and gives a metric showing high consistency is achievable.
- [Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference](../../archive/papers/2025/local-de572e138fc98639/summary.md) — Shows that greedy decoding is not deterministic across hardware: changing GPU type, GPU count or evaluation batch size shifts a reasoning model's AIME'24 accuracy by up to 9 percentage points and its response length by 9,000 tokens under BF16, because floating-point addition is non-associative.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
