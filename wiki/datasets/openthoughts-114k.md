# OpenThoughts-114k

<!-- auto:begin -->

OpenThoughts-114k is a 114K-example long-CoT reasoning-distillation dataset used in ReasMark (training reasoning models to systematically produce longer chains-of-thought on prompts dominated by a secret token pattern, to attribute knowledge distillation and protect intellectual property) and in Distilling the Essence's section-wise supervision ablation.

- **Kind**: dataset
- **Also called**: OpenThoughts-114k
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [Bespoke-Stratos-17k](bespoke-stratos-17k.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [GSM8K](gsm8k.md), [Llama-Nemotron-Post-Training-Dataset](llama-nemotron-post-training-dataset.md), [MATH](math.md), [OpenCodeReasoning](opencodereasoning.md), [OpenMathReasoning](openmathreasoning.md), [Phi-4-mini-reasoning](../models/phi-4-mini-reasoning.md)

## Appears in

- [ReasMark: A Robust Watermark for Attributing LLM Reasoning Under Knowledge Distillation Attacks](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2185/summary.md) — ReasMark protects proprietary reasoning models' intellectual property by training them to systematically produce longer chains-of-thought for prompts dominated by a secret 'long' high-frequency-token set and shorter chains for a 'short' token set (plus a matching entropy signature), so that a student model distilled from the protected model inherits this reasoning-length watermark and can be detected black-box via a one-sided t-test, surviving knowledge distillation, pruning, quantization and LoRA fine-tuning attacks where standard token-distribution watermarks fail.
- [Distilling the Essence: Efficient Reasoning Distillation via Sequence Truncation](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-587/summary.md) — Systematically ablates which section (prompt, CoT, answer) of a reasoning-distillation training sequence carries the useful supervisory signal and how much of the CoT is needed, finding CoT-inclusive supervision is essential while training on only the first 50% of tokens retains ~91% of full-sequence accuracy at roughly half the training time, memory, and FLOPs.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
