# Weather

<!-- auto:begin -->

A multivariate meteorological forecasting benchmark, one of the standard eight, distinguished by having many channels on very different scales. Both sources use it in that suite. It is one of the four datasets on which the coarse-to-fine work runs its full ablation grid, and one of the places where its margins are smallest -- 0.217 MSE against 0.218 for the strongest baseline -- which makes it a useful illustration of how little separates methods on this family without variance reporting. The ensemble work reports it among the eight benchmarks over which per-series optimal weights differ. Neither source describes the data.

- **Kind**: dataset
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [advantage estimation](../concepts/advantage-estimation.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [compute allocation](../concepts/compute-allocation.md), [DAPO](../methods/dapo.md), [DeepSeek-V3.2](../models/deepseek-v3-2.md), [Dr. GRPO](../methods/dr-grpo.md), [ETTh1](etth1.md), [ETTh2](etth2.md), [ETTm1](ettm1.md), [ETTm2](ettm2.md), [GPT-2](../models/gpt-2.md), [GPT-5.5](../models/gpt-5-5.md), [GRPO](../methods/grpo.md), [GSPO](../methods/gspo.md), [LoRA](../methods/lora.md), [out-of-distribution generalization](../concepts/out-of-distribution-generalization.md), [post-hoc rationalization](../concepts/post-hoc-rationalization.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [reward shaping](../concepts/reward-shaping.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time scaling](../concepts/test-time-scaling.md), [TimesFM](../models/timesfm.md), [Traffic](traffic.md), [zero-advantage group](../concepts/zero-advantage-group.md)

## Appears in

- [Efficient Test-Time Scaling for LLM-based Time Series Forecasting](../../archive/papers/2026/arxiv-2608-08675/summary.md) — Replaces open-ended iterative refinement in LLM time-series forecasting with a fixed-step coarse-to-fine loop anchored to an explicitly predicted downscaled future shape, so test-time compute is spent enriching detail rather than re-deciding the global trajectory.
- [REATS: LLM Reasoning-based Ensemble Learning for Adaptive Time Series Forecasting](../../archive/papers/2026/arxiv-2608-10149/summary.md) — Fine-tunes a 1.7B model to read structured summaries of a time series and allocate ensemble weights across candidate forecasters, trained by SFT on rule-generated chains of thought and then by GRPO with a bounded reciprocal reward that keeps a continuous error gap from collapsing the group advantage.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
