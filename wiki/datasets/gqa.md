# GQA

<!-- auto:begin -->

GQA entered this wiki through papers that share vocabulary with the tracked topic rather than through the overthinking literature: vStream matched on 'thinking model' and HiDrop on 'early exit', and the archive files both as tangential or as an outright keyword false positive. In both, GQA is one general visual-question-answering set among many - vStream's 'general' category alongside COCO and ReferIt, HiDrop's eleven-benchmark LLaVA-1.5 suite alongside VQAv2, POPE and MMBench - and neither reports anything about it beyond aggregate suite performance (HiDrop retains 96.5% of original average performance at 91.7% vision-token compression). Nothing in either source measures reasoning length, tokens emitted, or a stop/continue decision over a trace: HiDrop's 'early exit' terminates the propagation of image patch embeddings through layers, and its savings are all prefill-side. There is no accuracy/length result on GQA in this archive.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AI2D](ai2d.md), [ImageNet-1K](imagenet-1k.md), [MathVerse](mathverse.md), [MathVista](mathvista.md), [OK-VQA](ok-vqa.md), [OlympiadBench](olympiadbench.md), [POPE](pope.md), [ScienceQA](scienceqa.md)

## Appears in

- [FREE: Fast and Robust Vision Language Models with Early Exits](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-1209/summary.md) — FREE adds GAN-based early exits to frozen-backbone Vision-Language Models -- an exit transformer (generator) trained to mimic the final layer's representations, discriminated against by a frozen final-layer classifier reused as the exit classifier -- addressing both 'overthinking' (unnecessary computation on easy tokens) and a newly named 'mid-crisis' (intermediate-layer accuracy dip from searching for irrelevant features), giving >1.51x inference speedup with comparable accuracy and outperforming four prior early-exit baselines on captioning, VQA and visual dialogue.
- [Real-Time Visual Attribution Streaming in Thinking Model](../../archive/papers/2026/title-503ded235751878b/summary.md) — vStream trains a lightweight linear estimator to predict counterfactual ablation effects of image regions from cached attention features, so a multimodal reasoning model's visual grounding can be displayed while it reasons rather than recomputed afterwards, at 0.024 s per 10 tokens against 1.9-2.8 s for causal baselines.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
