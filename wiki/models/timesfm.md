# TimesFM

<!-- auto:begin -->

A time-series foundation model, used in both sources as one of the pretrained forecasters an ensemble or a scaling method is compared against or built from. Its role in this archive is to support the premise both papers rest on: no single foundation model dominates across datasets, which is what makes per-instance routing or ensembling worth doing at all. In the ensemble work it is one of four candidates whose optimal mixing weights vary by series; in the test-time-scaling work it is one of the deep-learning baselines a fixed-step refinement method is measured against. Neither describes its architecture or pretraining.

- **Kind**: model
- **Also called**: TimeFM
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [advantage estimation](../concepts/advantage-estimation.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [compute allocation](../concepts/compute-allocation.md), [DAPO](../methods/dapo.md), [DeepSeek-V3.2](deepseek-v3-2.md), [Dr. GRPO](../methods/dr-grpo.md), [ETTh1](../datasets/etth1.md), [ETTh2](../datasets/etth2.md), [ETTm1](../datasets/ettm1.md), [ETTm2](../datasets/ettm2.md), [GPT-2](gpt-2.md), [GPT-5.5](gpt-5-5.md), [GRPO](../methods/grpo.md), [GSPO](../methods/gspo.md), [LoRA](../methods/lora.md), [out-of-distribution generalization](../concepts/out-of-distribution-generalization.md), [post-hoc rationalization](../concepts/post-hoc-rationalization.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [reward shaping](../concepts/reward-shaping.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time scaling](../concepts/test-time-scaling.md), [Traffic](../datasets/traffic.md), [Weather](../datasets/weather.md), [zero-advantage group](../concepts/zero-advantage-group.md)

## Appears in

- [Efficient Test-Time Scaling for LLM-based Time Series Forecasting](../../archive/papers/2026/arxiv-2608-08675/summary.md) — Replaces open-ended iterative refinement in LLM time-series forecasting with a fixed-step coarse-to-fine loop anchored to an explicitly predicted downscaled future shape, so test-time compute is spent enriching detail rather than re-deciding the global trajectory.
- [REATS: LLM Reasoning-based Ensemble Learning for Adaptive Time Series Forecasting](../../archive/papers/2026/arxiv-2608-10149/summary.md) — Fine-tunes a 1.7B model to read structured summaries of a time series and allocate ensemble weights across candidate forecasters, trained by SFT on rule-generated chains of thought and then by GRPO with a bounded reciprocal reward that keeps a continuous error gap from collapsing the group advantage.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
