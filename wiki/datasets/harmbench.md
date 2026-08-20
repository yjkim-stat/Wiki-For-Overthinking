# HarmBench

<!-- auto:begin -->

A standardised set of harmful behaviours with an evaluation harness, and across 3 sources the hardest of the archive's four jailbreak benchmarks -- the one where defences that reach near-zero elsewhere still leave 9.00 to 44.75 percent attack success. That spread is what makes it the informative column: one defence's reductions across eight models run 34.75 to 65.50 points here while the same models show 0.96 to 70.77 on an easier set, so absolute rates are only comparable within a benchmark. It is also where the archive's judge-disagreement audit is run -- 400 responses re-judged, 90.25 percent overall agreement, 41.94 percent false-negative rate on the unsafe class -- which bounds how sharply any number on it can be read.

- **Kind**: dataset
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [AdvBench](advbench.md), [AIME 2024](aime-2024.md), [auditability](../concepts/auditability.md), [BeaverTails](beavertails.md), [Coconut](../methods/coconut.md), [curriculum learning](../methods/curriculum-learning.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DeepSeek-V3.2](../models/deepseek-v3-2.md), [GCG](../methods/gcg.md), [Gemini-2.5-Flash](../models/gemini-2-5-flash.md), [GPQA-Diamond](gpqa-diamond.md), [GPT o3](../models/gpt-o3.md), [GSM8K](gsm8k.md), [jailbreak](../concepts/jailbreak.md), [knowledge distillation](../methods/knowledge-distillation.md), [latent reasoning](../concepts/latent-reasoning.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [MATH500](math500.md), [MMLU-Pro](mmlu-pro.md), [monitorability](../concepts/monitorability.md), [out-of-distribution generalization](../concepts/out-of-distribution-generalization.md), [PAIR](../methods/pair.md), [post-hoc rationalization](../concepts/post-hoc-rationalization.md), [Qwen3-0.6B](../models/qwen3-0-6b.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3.5-27B](../models/qwen3-5-27b.md), [Qwen3-8B](../models/qwen3-8b.md), [representation versus readout](../concepts/representation-versus-readout.md), [safety alignment](../concepts/safety-alignment.md), [self-distillation](../methods/self-distillation.md), [StrongREJECT](strongreject.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [XSTest](xstest.md)

## Appears in

- [LatentGuard: Efficient and Inspectable Latent Reasoning for LLM Safeguards](../../archive/papers/2026/arxiv-2608-03838/summary.md) — Compresses a safety guard's textual rationales into continuous latent states by a staged curriculum, cutting 268 reasoning tokens to 1.60 and latency 8.9-fold, and adds an on-demand decoder that reconstructs a human-readable audit artifact — whose own ablation shows the artifact is anchored far more by the source text than by the latent states it is supposed to inspect.
- [Dual-Adversarial Safety Alignment: Cultivating Intrinsic Threat Comprehension in LRMs](../../archive/papers/2026/arxiv-2608-09542/summary.md) — Builds safety-alignment training data by first having an agent jailbreak a strong teacher and only then asking that teacher to explain why the successful attack worked, so the student is supervised on the mechanism of the attack rather than on the refusal.
- [AutoRAN: Automated Hijacking of Safety Reasoning in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1988/summary.md) — Automates the hijacking of a reasoning model's own safety reasoning by using a weaker, less-aligned model to simulate execution reasoning and refining attacks from patterns leaked in refusals.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
