# test-time compute

<!-- auto:begin -->

The compute a model spends at inference time -- extra reasoning tokens, parallel samples, or search -- as opposed to compute spent during training. 'Diversity Matters' finds test-time-compute methods that work for LLM reasoning mostly fail to transfer to vision-language-model accuracy gains; Sequential Reward Filtering proves standard best-of-n sampling is a suboptimal way to spend it and proposes a reward-filtered sequential alternative with better guarantees. Note: overlaps heavily with the archive's separately-tracked 'test-time compute scaling' and 'test-time scaling' entries -- not merged.

- **Kind**: concept
- **Also called**: test-time compute scaling, test-time scaling
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Best-of-N (BoN) sampling](../methods/best-of-n-bon-sampling.md), [best-of-N sampling](../methods/best-of-n-sampling.md), [majority voting](../methods/majority-voting.md), [self-consistency](../methods/self-consistency.md), [test-time compute scaling](test-time-compute-scaling.md), [test-time scaling](test-time-scaling.md)

## Appears in

- [Diversity Matters: Revisiting Test-Time Compute in Vision-Language Models](../../archive/papers/2026/title-3f7a94a14d75d893/summary.md) — An empirical study showing that test-time-compute methods effective for LLM reasoning mostly fail to transfer to vision-language models unless prediction diversity is present, and proposes an entropy-based selection method that works better in multi-model ensembles.
- [On the Limits of Test-Time Compute: Sequential Reward Filtering for Better Inference](../../archive/papers/2026/title-cd5c62ac6be53cbc/summary.md) — Proves standard best-of-n sampling is suboptimal for test-time compute under a mixture-of-reference-policy model and proposes reward-filtered sequential inference as a stronger alternative.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
