# VizWiz

<!-- auto:begin -->

VizWiz is a visual-question-answering benchmark used to evaluate FREE (which adds GAN-based early exits to frozen-backbone vision-language models, training an exit-transformer generator to mimic final-layer representations) and RECAP (mitigating RLVR-induced general-capability forgetting -- perception, grounding, safety -- in vision-language models).

- **Kind**: dataset
- **Also called**: VizWiz
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AI2D](ai2d.md), [ChartQA](chartqa.md), [GQA](gqa.md), [LISA](lisa.md), [MathVerse](mathverse.md), [MathVision](mathvision.md), [MathVista](mathvista.md), [MMMU](mmmu.md), [MMMU-Pro](mmmu-pro.md), [OK-VQA](ok-vqa.md), [Qwen2.5-VL-3B](../models/qwen2-5-vl-3b.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [SAT](sat.md), [ScienceQA](scienceqa.md), [Uniform sampling baseline](../methods/uniform-sampling-baseline.md)

## Appears in

- [FREE: Fast and Robust Vision Language Models with Early Exits](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-1209/summary.md) — FREE adds GAN-based early exits to frozen-backbone Vision-Language Models -- an exit transformer (generator) trained to mimic the final layer's representations, discriminated against by a frozen final-layer classifier reused as the exit classifier -- addressing both 'overthinking' (unnecessary computation on easy tokens) and a newly named 'mid-crisis' (intermediate-layer accuracy dip from searching for irrelevant features), giving >1.51x inference speedup with comparable accuracy and outperforming four prior early-exit baselines on captioning, VQA and visual dialogue.
- [Beyond Reasoning Gains: Mitigating General-Capability Forgetting in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1717/summary.md) — RECAP mitigates the general-capability forgetting (perception, grounding, safety) that RLVR-based reasoning fine-tuning causes in vision-language models, by replaying general-domain data alongside the reasoning objective and dynamically reweighting each objective's loss based on its recent convergence rate and instability -- an entropy-regularized priority allocation that provably reduces to a closed-form softmax -- preserving or improving general capabilities while matching or exceeding reasoning-only fine-tuning's math/reasoning performance, and, as a side effect, producing shorter, more concise reasoning rationales without compromising reasoning ability.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
