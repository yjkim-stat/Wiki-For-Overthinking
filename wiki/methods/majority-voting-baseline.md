# majority voting (baseline)

<!-- auto:begin -->

Majority voting (selecting the most common answer among sampled candidates) is used across these sources as the standard, unweighted aggregation baseline that confidence- or synthesis-based test-time-scaling methods are compared against: GSR's 'Refinement Gap' metric is explicitly defined as self-refinement accuracy minus majority-voting accuracy, to isolate genuine synthesis value beyond simple aggregation, and Chronos reports beating majority voting by up to 13.76 absolute accuracy points via its time-series-based trajectory scoring.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [beam search](beam-search.md), [best-of-n selection](best-of-n-selection.md), [COCONUT](coconut.md), [CODI](codi.md), [CoLaR](colar.md), [DeepSeek-R1-0528-Qwen3-8B](../models/deepseek-r1-0528-qwen3-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K-Hard](../datasets/gsm8k-hard.md), [GSM8K-Test](../datasets/gsm8k-test.md), [MATH500](../datasets/math500.md), [MultiArith](../datasets/multiarith.md), [OlympiadBench](../datasets/olympiadbench.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md)

## Appears in

- [Parallel Test-Time Scaling for Latent Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2069/summary.md) — Extends parallel test-time scaling to latent reasoning models (which reason in continuous hidden-state vectors rather than tokens) by introducing two stochastic sampling strategies (Monte Carlo Dropout, Additive Gaussian Noise) to generate diverse latent trajectories and a Latent Reward Model trained with a step-wise contrastive objective to score and aggregate them, showing consistent scaling gains with best-of-N and beam search across three arithmetic benchmarks and backbones up to 4B parameters.
- [Learning to Refine: Self-Refinement of Parallel Reasoning in LLMs](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1291/summary.md) — Defines the Refinement Gap (self-refinement accuracy minus majority-voting accuracy) to isolate parallel self-refinement's genuine value beyond simple candidate aggregation, finds it scales with model size but only weakly with base capability, and trains this capability into a 7B student (GSR) via a hybrid direct-solving-plus-refinement objective that explicitly retains all-candidates-incorrect training cases -- achieving 73.6% average accuracy across five math benchmarks (a +3.1-point Refinement Gap versus a much larger QwQ-32B teacher's +1.15) and recovering correct answers 5.9% of the time even when every sampled candidate is wrong.
- [Chronos: Learning Temporal Dynamics of Reasoning Chains for Test-Time Scaling](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1376/summary.md) — Chronos treats a reasoning trace's per-token negative-log-probability sequence as a time series (rather than collapsing it to a single pooled scalar like prior confidence-based scorers) and scores its quality with a multi-scale InceptionTime-style CNN focused on the final tail tokens, then weights majority voting by these learned scores -- beating majority voting by up to 13.76 absolute points and confidence-weighted voting (DeepConf) across all nine model-benchmark combinations, at only a 0.0005% increase in inference FLOPs, and generalizing across models and out-of-domain tasks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
