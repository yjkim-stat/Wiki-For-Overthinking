# Bespoke-Stratos-17k

<!-- auto:begin -->

Bespoke-Stratos-17k is a long-CoT reasoning-distillation training dataset used in Distilling the Essence (which ablates which section of a distillation sequence -- prompt, CoT, answer -- carries the useful supervisory signal) and in QFFT (Question-Free Fine-Tuning, which trains on Long CoT responses with the question deleted so a model keeps its default concise reasoning and switches to long reasoning only when needed).

- **Kind**: dataset
- **Also called**: Bespoke-Stratos (17k)
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [adaptive reasoning](../concepts/adaptive-reasoning.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [DPO_Shortest](../methods/dpo-shortest.md), [GPQA](gpqa.md), [GSM8K](gsm8k.md), [Llama-Nemotron-Post-Training-Dataset](llama-nemotron-post-training-dataset.md), [MATH500](math500.md), [Minerva](minerva.md), [MMLU-Pro](mmlu-pro.md), [O1-Pruner](../methods/o1-pruner.md), [OpenThoughts-114k](openthoughts-114k.md), [Overthinking](../concepts/overthinking.md), [SFT_Shortest](../methods/sft-shortest.md), [Test-Time Scaling](../concepts/test-time-scaling.md)

## Appears in

- [Distilling the Essence: Efficient Reasoning Distillation via Sequence Truncation](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-587/summary.md) — Systematically ablates which section (prompt, CoT, answer) of a reasoning-distillation training sequence carries the useful supervisory signal and how much of the CoT is needed, finding CoT-inclusive supervision is essential while training on only the first 50% of tokens retains ~91% of full-sequence accuracy at roughly half the training time, memory, and FLOPs.
- [QFFT, Question-Free Fine-Tuning for Adaptive Reasoning](../../archive/papers/2025/title-ff37e37c3f1ab9b2/summary.md) — QFFT fine-tunes a short-CoT instruct model on Long CoT responses with the question deleted from every training example, so the model keeps its default concise reasoning and switches to reflective Long CoT only when it hits uncertainty or an error, cutting average tokens by roughly 50% at accuracy comparable to ordinary SFT.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
