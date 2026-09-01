# OpenR1-Math-220k

<!-- auto:begin -->

OpenR1-Math-220k is a 220K-sample long-CoT math instruction pool used as the source data for SELECT2REASON's instruction-selection method (selecting a top-10% high-utility subset by difficulty and trace length) and for SuCo's training on the Minimal Sufficient CoT prefix.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [CommonsenseQA](commonsenseqa.md), [GPQA](gpqa.md), [GPQA-Diamond](gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [KAOYAN](kaoyan.md), [LiveCodeBench-v6](livecodebench-v6.md), [LLaMA-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [Llama-Nemotron-Post-Training-Dataset](llama-nemotron-post-training-dataset.md), [MATH500](math500.md), [MBPP](mbpp.md), [MMLU STEM](mmlu-stem.md), [OlympiadBench](olympiadbench.md), [OpenCodeReasoning](opencodereasoning.md), [OpenMathReasoning](openmathreasoning.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-3B-Instruct](../models/qwen2-5-3b-instruct.md), [Qwen2.5-Math-7B-Instruct](../models/qwen2-5-math-7b-instruct.md), [s1k-1.1](s1k-1-1.md), [StrategyQA](strategyqa.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [underthinking](../concepts/underthinking.md), [ZebraLogic](zebralogic.md)

## Appears in

- [Select2Reason: Efficient Instruction-Tuning Data Selection for Long-CoT Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-331/summary.md) — SELECT2REASON selects the top 10% of a large long-CoT instruction pool for SFT by jointly ranking questions on a learned difficulty score and (deduplicated) reasoning-trace length, matching or beating models trained on 8-94x more data.
- [SuCo: Sufficiency-guided Continuous Adaptive Reasoning](../../archive/papers/2026/title-b37859867120f044/summary.md) — Defines the Minimal Sufficient CoT — the shortest reasoning prefix at which the model's confidence in the ground-truth answer crosses a difficulty-adaptive threshold — and trains on it via supervised fine-tuning plus a GRPO stage whose reward penalises both over- and under-thinking, so reasoning length is calibrated continuously rather than by discrete modes.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
