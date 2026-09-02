# AlpacaEval 2.0

<!-- auto:begin -->

AlpacaEval 2.0 is an LLM-judged instruction-following/helpfulness win-rate benchmark. PAM uses it as one of three evaluation axes (with AdvBench/WildJailbreak harmlessness and MATH500/AIME24 reasoning) to show a metacognition-equipped alignment method improves win rate over an identically-trained model without it (+3.05 to +8.82 points under DPO, +5.96/+8.82 under GRPO, across two backbones). SuCo uses it as one of three out-of-domain checks for a math-trained model, reaching a 2.4 length-controlled win rate against DeepSeek-R1-Distill's 1.05 -- both low absolute scores at this evaluation scale.

- **Kind**: dataset
- **Also called**: AlpacaEval2.0
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AdvBench](advbench.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [CommonsenseQA](commonsenseqa.md), [GPQA-Diamond](gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [LiveCodeBench-v6](livecodebench-v6.md), [Llama-Nemotron-Post-Training-Dataset](llama-nemotron-post-training-dataset.md), [MATH500](math500.md), [MBPP](mbpp.md), [MMLU STEM](mmlu-stem.md), [OpenCodeReasoning](opencodereasoning.md), [OpenR1-Math-220k](openr1-math-220k.md), [Overthinking](../concepts/overthinking.md), [s1k-1.1](s1k-1-1.md), [StrategyQA](strategyqa.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [underthinking](../concepts/underthinking.md), [WildJailbreak](wildjailbreak.md)

## Appears in

- [PAM: Enhancing General Alignment of Large Reasoning Models through Priority-Aware Metacognition](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-432/summary.md) — PAM trains large reasoning models to explicitly assess which human-preference priority (e.g. harmlessness) applies to a query before reasoning -- via a Flavell-metacognition-inspired cold-start SFT stage plus DPO preference optimization -- improving helpfulness, harmlessness and instruction-following by an average of ~10 points over an identically-trained model without this metacognitive step, without a corresponding drop in math reasoning performance for one of two backbones.
- [SuCo: Sufficiency-guided Continuous Adaptive Reasoning](../../archive/papers/2026/title-b37859867120f044/summary.md) — Defines the Minimal Sufficient CoT — the shortest reasoning prefix at which the model's confidence in the ground-truth answer crosses a difficulty-adaptive threshold — and trains on it via supervised fine-tuning plus a GRPO stage whose reward penalises both over- and under-thinking, so reasoning length is calibrated continuously rather than by discrete modes.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
