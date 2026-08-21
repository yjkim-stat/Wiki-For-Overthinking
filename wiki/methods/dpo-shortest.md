# DPO_Shortest

<!-- auto:begin -->

DPO_Shortest appears in the archive only as a long-to-short baseline, named but never described. ARLCP lists it among seven efficient-reasoning baselines it outperforms (NoThinking, SFT_Shortest, DPO_Shortest, O1-Pruner, TLMRE, AdaptThink, LASER), and QFFT places it in the same '-Shortest' family as SFT-Shortest and SimPO-Shortest — preference-optimisation recipes trained to prefer the shortest of a model's sampled responses — reporting Accuracy-Efficiency Scores of -12.9 for SFT-Shortest and -1.6 for SimPO-shortest at 32B against QFFT's 2.3, without giving a DPO_Shortest number. No collected reading states its training procedure, so the entry records what the sources use it for rather than how it works.

- **Kind**: method
- **Also called**: DPO-Shortest
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Accuracy-Length Tradeoff](../concepts/accuracy-length-tradeoff.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [AdaptThink](adaptthink.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [GPQA](../datasets/gpqa.md), [GSM8K](../datasets/gsm8k.md), [Laser](laser.md), [Length Penalty](../concepts/length-penalty.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [MMLU-Pro](../datasets/mmlu-pro.md), [NoThinking](nothinking.md), [O1-Pruner](o1-pruner.md), [Overthinking](../concepts/overthinking.md), [SFT_Shortest](sft-shortest.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [Test-time scaling](../concepts/test-time-scaling.md)

## Appears in

- [Stop Unnecessary Reflection: Training LRMs for Efficient Reasoning with Adaptive Reflection and Length Coordinated Penalty](../../archive/papers/2026/title-833de99e9b3ea69d/summary.md) — ARLCP is a reinforcement-learning fine-tuning recipe that adds two coupled reward penalties -- one on reflective steps, one on response length scaled by estimated problem complexity -- to shorten chains of thought in distilled reasoning models without losing accuracy.
- [QFFT, Question-Free Fine-Tuning for Adaptive Reasoning](../../archive/papers/2025/title-ff37e37c3f1ab9b2/summary.md) — QFFT fine-tunes a short-CoT instruct model on Long CoT responses with the question deleted from every training example, so the model keeps its default concise reasoning and switches to reflective Long CoT only when it hits uncertainty or an error, cutting average tokens by roughly 50% at accuracy comparable to ordinary SFT.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
