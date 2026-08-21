# Test-Time Compute

<!-- auto:begin -->

The compute a model spends at inference -- extra reasoning tokens, parallel samples, search, or tool calls -- as opposed to compute spent in training. What the archive's sources have converged on is that it is a quantity to be allocated rather than increased: frontier models now expose it as a user-controllable budget, spending the maximum uniformly is both expensive and sometimes actively harmful (the 'over-thinking penalty', where extra inference compute lowers accuracy or merely costs more than a cheaper configuration would), and later work treats the choice of how much to spend jointly with the choice of which model to spend it on, learned online as a contextual bandit. Its cost is also not confined to the generator: sources measuring it end to end charge the controller, verifier or compressor that decides the budget against the budget itself. Note: this archive tracks 'test-time compute scaling' and 'test-time scaling' as separate entries covering the same ground; they are not merged.

- **Kind**: concept
- **Also called**: Test-Time Compute, test-time compute, test-time compute scaling, test-time scaling
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [accuracy-efficiency tradeoff](accuracy-efficiency-tradeoff.md), [adaptive test-time compute](adaptive-test-time-compute.md), [AIME 2024](../datasets/aime-2024.md), [AMC23](../datasets/amc23.md), [AutoThink](../methods/autothink.md), [Best-of-N (BoN) sampling](../methods/best-of-n-bon-sampling.md), [Best-of-N sampling](../methods/best-of-n-sampling.md), [Conformal Prediction](../methods/conformal-prediction.md), [early stopping](early-stopping.md), [GPQA](../datasets/gpqa.md), [GSM8K](../datasets/gsm8k.md), [HLE](../datasets/hle.md), [LiveCodeBench](../datasets/livecodebench.md), [Majority Voting](../methods/majority-voting.md), [MATH](../datasets/math.md), [Minerva](../datasets/minerva.md), [MMLU](../datasets/mmlu.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](overthinking.md), [Reward Shaping](reward-shaping.md), [Self-Consistency](../methods/self-consistency.md), [Sequential revision](sequential-revision.md), [Test-Time Compute Scaling](test-time-compute-scaling.md), [Test-time scaling](test-time-scaling.md), [Uncertainty Quantification](uncertainty-quantification.md)

## Appears in

- [Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL](../../archive/papers/2025/title-0bc5d9b198744bed/summary.md) — AutoThink uses a three-stage RL curriculum with stage-wise reward shaping to teach R1-style distilled models to decide per problem whether to emit an explicit reasoning chain at all.
- [Diversity Matters: Revisiting Test-Time Compute in Vision-Language Models](../../archive/papers/2026/title-3f7a94a14d75d893/summary.md) — An empirical study showing that test-time-compute methods effective for LLM reasoning mostly fail to transfer to vision-language models unless prediction diversity is present, and proposes an entropy-based selection method that works better in multi-model ensembles.
- [Statistical Early Stopping for Reasoning Models](../../archive/papers/2026/title-594984624acaa60d/summary.md) — Two statistical stopping rules monitor uncertainty-keyword arrivals inside a reasoning trace and halt generation on ill-posed or ambiguous queries, one with a finite-sample bound on the probability of halting too early on a well-posed query.
- [On the Limits of Test-Time Compute: Sequential Reward Filtering for Better Inference](../../archive/papers/2026/title-cd5c62ac6be53cbc/summary.md) — Proves standard best-of-n sampling is suboptimal for test-time compute under a mixture-of-reference-policy model and proposes reward-filtered sequential inference as a stronger alternative.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
