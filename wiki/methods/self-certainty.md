# self-certainty

<!-- auto:begin -->

A verifier-free selection score computed from a model's own output distribution, used across 4 sources as the standard confidence-based alternative to plurality voting. The archive's evidence about it is mostly negative and specific. It is absorbed by controls: at matched budgets it falls below a matched-control baseline where plurality-with-Borda and confidence-weighted voting track that control within noise. It loses to plurality outright in one head-to-head at sixteen samples (51.7 against 60.6 for a weighting method and 46.2 for plain voting, in a table where it beats plain voting). And one source's assumption about it is flagged rather than tested -- the approach depends on self-certainty being calibrated with respect to difficulty, which is asserted rather than measured, and an overconfident model would compress exactly the problems it is wrong about. The archive's calibration material supplies the reason to doubt it on hard sets.

- **Kind**: method
- **Also called**: intrinsic confidence, model certainty, self-confidence
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [AIME 2024](../datasets/aime-2024.md), [AMC23](../datasets/amc23.md), [best-of-n](best-of-n.md), [Borda count](borda-count.md), [calibration](../concepts/calibration.md), [confidence calibration](../concepts/confidence-calibration.md), [cross-validation](cross-validation.md), [difficulty conditioning](difficulty-conditioning.md), [difficulty stratification](difficulty-stratification.md), [entropy collapse](../concepts/entropy-collapse.md), [entropy trajectory](../concepts/entropy-trajectory.md), [exploration](../concepts/exploration.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [gpt-oss-20b](../models/gpt-oss-20b.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [HMMT 2025](../datasets/hmmt-2025.md), [LiveCodeBench](../datasets/livecodebench.md), [majority voting](majority-voting.md), [matched-budget comparison](matched-budget-comparison.md), [MATH](../datasets/math.md), [overthinking](../concepts/overthinking.md), [preference optimization](preference-optimization.md), [premature convergence](../concepts/premature-convergence.md), [process supervision](../concepts/process-supervision.md), [prompt difficulty](../concepts/prompt-difficulty.md), [Qwen2.5-1.5B-Instruct](../models/qwen2-5-1-5b-instruct.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen3-4B-Instruct-2507](../models/qwen3-4b-instruct-2507.md), [SciQ](../datasets/sciq.md), [selection signal](../concepts/selection-signal.md), [self-consistency](self-consistency.md), [test-time scaling](../concepts/test-time-scaling.md), [token-level entropy](../concepts/token-level-entropy.md), [uncertainty quantification](../concepts/uncertainty-quantification.md), [verifier-free verification](verifier-free-verification.md)

## Appears in

- [Interpretable Adaptive Sampling for LLM Test-Time Scaling](../../archive/papers/2026/arxiv-2608-03961/summary.md) — Allocates test-time samples per prompt with a fuzzy controller over human-readable difficulty and confidence signals, and — under a selector-matched protocol that isolates the budget policy from the answer selector — reports the result honestly as an accuracy-compute tradeoff rather than an accuracy gain.
- [Consilience for Verifier-Free Test-Time Scaling](../../archive/papers/2026/arxiv-2608-09898/summary.md) — Shows that selecting the most confident rollout can be worse than picking at random, because uniformly high confidence signals a failure to explore rather than a well-supported answer, and replaces maximisation with a temporal criterion that penalises early certainty while requiring late certainty.
- [CAT: Confidence-Adaptive Thinking for Efficient Reasoning of Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-industry-152/summary.md) — Feeds a reasoning model's own self-certainty into preference optimization so it compresses confident answers and keeps deliberating on uncertain ones.
- [EDIS: Diagnosing LLM Reasoning via Entropy Dynamics](../../archive/papers/2026/local-e64d3a8c4788daf7/summary.md) — Introduces EDIS, a trajectory-level score that measures how unstably token entropy evolves during generation, and uses it to select better reasoning rollouts at inference and to curate training samples in RL.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
