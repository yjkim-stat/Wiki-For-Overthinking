# adaptive reasoning length

<!-- auto:begin -->

In both archived sources this names the property of a reasoning model that spends tokens in proportion to what the instance needs, as opposed to a fixed or uniformly-truncated trace -- and the two differ in where the signal for 'how much' comes from. Self-Braking Tuning puts it inside the model, training a large reasoning model to detect and halt its own redundant steps, and reports up to 60% fewer tokens at comparable accuracy on maths benchmarks. PixelThink puts it outside, conditioning a GRPO reward on an externally estimated task difficulty together with the model's own uncertainty to regulate chain length in reasoning segmentation, roughly halving reasoning tokens while slightly improving mask accuracy. Neither source gives the term a formal definition; it is used descriptively for the behaviour their methods produce.

- **Kind**: concept
- **Also called**: adaptive reasoning budget, dynamic reasoning length
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Accuracy-Length Tradeoff](accuracy-length-tradeoff.md), [AIME](../datasets/aime.md), [AMC](../datasets/amc.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [MATH500](../datasets/math500.md), [Overthinking](overthinking.md), [Reasoning Segmentation](reasoning-segmentation.md), [ReasonSeg](../datasets/reasonseg.md), [Redundant Reasoning Steps](redundant-reasoning-steps.md), [RefCOCO](../datasets/refcoco.md), [RefCOCOg](../datasets/refcocog.md), [Seg-Zero (baseline)](../methods/seg-zero-baseline.md)

## Appears in

- [Let LRMs Break Free from Overthinking via Self-Braking Tuning](../../archive/papers/2025/title-2b17dd2ef08b6fa4/summary.md) — Introduces Self-Braking Tuning, which trains a large reasoning model to detect and stop its own redundant reasoning steps, cutting token usage by up to 60% with comparable accuracy on math benchmarks.
- [Don't Overthink with Pixels: Efficient Reasoning for Segmentation](../../archive/papers/2026/title-d94f940ea2e159b8/summary.md) — PixelThink regulates the length of a multimodal LLM's reasoning chain in reasoning segmentation by conditioning a GRPO reward on an externally estimated task difficulty and the model's own uncertainty, cutting reasoning tokens roughly in half while slightly improving mask accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
