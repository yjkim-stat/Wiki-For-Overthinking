# GCG

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [ablation](ablation.md), [activation steering](activation-steering.md), [AdvBench](../datasets/advbench.md), [AIME 2024](../datasets/aime-2024.md), [contrastive activation addition](contrastive-activation-addition.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DeepSeek-V3.2](../models/deepseek-v3-2.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [HarmBench](../datasets/harmbench.md), [jailbreak](../concepts/jailbreak.md), [KL divergence](../concepts/kl-divergence.md), [knowledge distillation](knowledge-distillation.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [LLM-as-a-judge](llm-as-a-judge.md), [LoRA](lora.md), [MATH500](../datasets/math500.md), [MMLU-Pro](../datasets/mmlu-pro.md), [out-of-distribution generalization](../concepts/out-of-distribution-generalization.md), [PAIR](pair.md), [Qwen2.5-14B-Instruct](../models/qwen2-5-14b-instruct.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3-0.6B](../models/qwen3-0-6b.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-8B](../models/qwen3-8b.md), [representation versus readout](../concepts/representation-versus-readout.md), [safety alignment](../concepts/safety-alignment.md), [self-distillation](../concepts/self-distillation.md), [steering vector](steering-vector.md), [StrongREJECT](../datasets/strongreject.md), [superposition](../concepts/superposition.md), [supervised fine-tuning](supervised-fine-tuning.md), [XSTest](../datasets/xstest.md)

## Appears in

- [Safety Cost of Steering Vectors Is Separable and Reducible](../../archive/papers/2026/arxiv-2608-08383/summary.md) — Shows that the part of a steering vector which breaks a model's refusal behaviour is a separate direction from the part that produces the intended behavioural effect, and learns that direction by constrained optimization so it can be ablated without losing the steering.
- [Dual-Adversarial Safety Alignment: Cultivating Intrinsic Threat Comprehension in LRMs](../../archive/papers/2026/arxiv-2608-09542/summary.md) — Builds safety-alignment training data by first having an agent jailbreak a strong teacher and only then asking that teacher to explain why the successful attack worked, so the student is supervised on the mechanism of the attack rather than on the refusal.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
