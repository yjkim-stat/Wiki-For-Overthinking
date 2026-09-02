# MMLU STEM

<!-- auto:begin -->

The science-and-mathematics subset of MMLU, which appears in the archive only as one component of averaged evaluation suites, never on its own. SuCo averages it with GSM8K, MATH-500, AMC23, AIME25, MBPP, LiveCodeBench-v6 and GPQA-Diamond to report 53.1% accuracy at 1,483 mean response tokens for a 1.5B model, against DeepSeek-R1-Distill-Qwen at 45.2% / 5,736 tokens and LHRMs at 50.5% / 2,055 tokens; ConPress lists it among its evaluation sets. Neither source reports a per-benchmark MMLU-STEM accuracy or length figure, so the archive states no accuracy/length tradeoff for this set specifically — only that it is part of a mix on which one method cut tokens roughly fourfold while raising accuracy.

- **Kind**: dataset
- **Also called**: MMLU-STEM
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AlpacaEval 2.0](alpacaeval-2-0.md), [AMC](amc.md), [AMC23](amc23.md), [College Math](college-math.md), [CommonsenseQA](commonsenseqa.md), [DeepSeek-R1-distilled models (comparison)](../concepts/deepseek-r1-distilled-models-comparison.md), [DeepSeek-R1 (teacher)](../models/deepseek-r1-teacher.md), [GPQA](gpqa.md), [GPQA-Diamond](gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [LiveCodeBench-v6](livecodebench-v6.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-Nemotron-Post-Training-Dataset](llama-nemotron-post-training-dataset.md), [MATH500](math500.md), [MBPP](mbpp.md), [Minerva](minerva.md), [MMLU](mmlu.md), [MMLU-Pro](mmlu-pro.md), [OlympiadBench](olympiadbench.md), [OpenCodeReasoning](opencodereasoning.md), [OpenR1-Math-220k](openr1-math-220k.md), [Overthinking](../concepts/overthinking.md), [s1k-1.1](s1k-1-1.md), [Self-Distillation](../concepts/self-distillation.md), [StrategyQA](strategyqa.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [underthinking](../concepts/underthinking.md)

## Appears in

- [Concise Math Reasoning via Difficulty-Aware Distillation](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2155/summary.md) — Difficulty-Aware Distillation (DAD) has a teacher assess each problem's difficulty (easy/medium/hard) then rewrite its own long CoT solution into a difficulty-adaptive, minimal-essential-steps trace via a two-step generate-then-refine pipeline, producing LiteCoT (100K samples averaging just 720 tokens, an order of magnitude shorter than S1/LIMO/OpenThoughts); models distilled on LiteCoT (Liter, 1.5B-32B) consistently outperform models trained on the same teacher's own 800K verbose CoTs, reach 74.2% Pass@1 on AIME24 using only ~5K inference tokens (beating methods that consume far more), and beat static one-size-fits-all CoT-compression baselines (Chain-of-Draft, LLMLingua-2, BudgetAware) on both accuracy and inference time across eight benchmarks.
- [ConPress: Learning Efficient Reasoning from Multi-Question Contextual Pressure](../../archive/papers/2026/title-11f96b3e58a44cf5/summary.md) — ConPress observes that a reasoning model shortens its traces when several independent questions share one prompt, and harvests those shortened traces as self-supervised fine-tuning data for the single-question setting.
- [SuCo: Sufficiency-guided Continuous Adaptive Reasoning](../../archive/papers/2026/title-b37859867120f044/summary.md) — Defines the Minimal Sufficient CoT — the shortest reasoning prefix at which the model's confidence in the ground-truth answer crosses a difficulty-adaptive threshold — and trains on it via supervised fine-tuning plus a GRPO stage whose reward penalises both over- and under-thinking, so reasoning length is calibrated continuously rather than by discrete modes.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
