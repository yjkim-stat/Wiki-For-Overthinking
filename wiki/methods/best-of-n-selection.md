# best-of-n selection

<!-- auto:begin -->

Best-of-N selection samples several complete attempts at a problem and picks one to submit, so its whole difficulty is the choosing rule when there is no verifier and no canonical answer to match. The archive's sources are both about that rule rather than about the sampling. Consilience picks the rollout whose confidence starts low and ends high, introduced to fix a failure mode where maximising confidence alone favours confidently wrong answers on hard problems. Risa selects among software-agent patches by agreement of their MoE routing traces at informative positions, matching text-consensus selection on SWE-bench Verified without any answer-string matching (48.2% against 48.0% macro-average on gpt-oss; exact McNemar p = 1.000 against text consensus on Qwen3.6). Risa also marks the headroom the rule leaves: its four-attempt oracle reaches 60.9% against 48.3% for the best selector, so most of the complementary coverage in a pool goes unselected.

- **Kind**: method
- **Also called**: Best-of-N Selection, BoN, best-of-N, best-of-N selection
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [beam search](beam-search.md), [COCONUT](coconut.md), [CODI](codi.md), [CoLaR](colar.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [GPT-OSS-20B](../models/gpt-oss-20b.md), [GSM8K-Hard](../datasets/gsm8k-hard.md), [GSM8K-Test](../datasets/gsm8k-test.md), [HMMT 2025](../datasets/hmmt-2025.md), [LiveCodeBench-v6](../datasets/livecodebench-v6.md), [majority voting (baseline)](majority-voting-baseline.md), [MATH500](../datasets/math500.md), [MultiArith](../datasets/multiarith.md), [Pass@1](../concepts/pass-1.md), [Self-Consistency](self-consistency.md), [SWE-bench Verified](../datasets/swe-bench-verified.md), [Test-Time Scaling](../concepts/test-time-scaling.md), [Uniform sampling baseline](uniform-sampling-baseline.md)

## Appears in

- [Consilience for Verifier-Free Test-Time Scaling](../../archive/papers/2026/arxiv-2608-09898/summary.md) — Introduces consilience, a verifier-free test-time-scaling selection metric that picks the sampled reasoning rollout whose confidence starts low (exploratory) and ends high (convergent), fixing a failure mode where naive confidence maximization favors confidently wrong answers on hard problems.
- [Disagree to Explore, Agree to Commit: Routing-Guided Test-Time Scaling for Software Agents](../../archive/papers/2026/arxiv-2608-22191/summary.md) — Risa reads the MoE router's expert-selection trace as a behavioral fingerprint of what a software agent is doing, using it to push sibling actions away from recently repeated computation during exploration and toward peer agreement once a patch is being written, then to arbitrate among completed attempts without an external judge or test execution.
- [Parallel Test-Time Scaling for Latent Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2069/summary.md) — Extends parallel test-time scaling to latent reasoning models (which reason in continuous hidden-state vectors rather than tokens) by introducing two stochastic sampling strategies (Monte Carlo Dropout, Additive Gaussian Noise) to generate diverse latent trajectories and a Latent Reward Model trained with a step-wise contrastive objective to score and aggregate them, showing consistent scaling gains with best-of-N and beam search across three arithmetic benchmarks and backbones up to 4B parameters.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
