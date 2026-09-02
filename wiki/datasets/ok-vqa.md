# OK-VQA

<!-- auto:begin -->

A knowledge-based visual question answering benchmark used to evaluate vision-language model efficiency methods, including FREE's GAN-based early-exit framework (evaluated unsupervised on OK-VQA alongside VQAv2/GQA/VizWiz) as part of demonstrating that early exits can mitigate overthinking and mid-crisis in frozen-backbone VLMs.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [ARC-Challenge](arc-challenge.md), [Chain-of-Thought Distillation](../methods/chain-of-thought-distillation.md), [CommonsenseQA](commonsenseqa.md), [GQA](gqa.md), [GSM8K](gsm8k.md), [MATH](math.md), [StrategyQA](strategyqa.md), [VizWiz](vizwiz.md)

## Appears in

- [FREE: Fast and Robust Vision Language Models with Early Exits](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-1209/summary.md) — FREE adds GAN-based early exits to frozen-backbone Vision-Language Models -- an exit transformer (generator) trained to mimic the final layer's representations, discriminated against by a frozen final-layer classifier reused as the exit classifier -- addressing both 'overthinking' (unnecessary computation on easy tokens) and a newly named 'mid-crisis' (intermediate-layer accuracy dip from searching for irrelevant features), giving >1.51x inference speedup with comparable accuracy and outperforming four prior early-exit baselines on captioning, VQA and visual dialogue.
- [The Quest for Efficient Reasoning: A Data-Centric Benchmark to CoT Distillation](../../archive/papers/2026/title-95b92d67054ad4f2/summary.md) — DC-CoT is a benchmark that isolates the effect of data augmentation, data selection and data mixing on chain-of-thought distillation into smaller student models, across teacher models, student models and reasoning domains.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
