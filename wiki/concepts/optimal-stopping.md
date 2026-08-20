# optimal stopping

<!-- auto:begin -->

The classical theory of when to stop sampling, which both sources import to decide how many generations an LLM should produce. They pick different classical problems and so optimize different things. One maps generation onto Pandora's Box, where each sample opens a costly box with random reward and the optimal rule under a known distribution is Weitzman's fair-cap threshold; since the reward distribution is unknown it learns an upper confidence bound on that threshold online. The other poses self-consistency stopping as sequential hypothesis testing for mode identification, stopping once the posterior that the leading answer is the true mode exceeds a confidence level. The distinction matters: the first maximizes a reward model's score, the second maximizes agreement, and neither targets correctness directly.

- **Kind**: concept
- **Also called**: early stopping theory, sequential stopping, stopping rule
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [answer stabilization](answer-stabilization.md), [best-of-n](../methods/best-of-n.md), [chain-of-thought compression](../methods/chain-of-thought-compression.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [early exit](../methods/early-exit.md), [exploration-exploitation trade-off](exploration-exploitation-trade-off.md), [gpt-oss-20b](../models/gpt-oss-20b.md), [GSM8K](../datasets/gsm8k.md), [length penalty](../methods/length-penalty.md), [majority voting](../methods/majority-voting.md), [MATH500](../datasets/math500.md), [Omni-MATH](../datasets/omni-math.md), [overthinking](overthinking.md), [prompt difficulty](prompt-difficulty.md), [reasoning redundancy](reasoning-redundancy.md), [reinforcement learning](../methods/reinforcement-learning.md), [self-consistency](../methods/self-consistency.md), [test-time compute](test-time-compute.md)

## What we have settled

- **Established** — A generation-time signal read against an absolute threshold does not transfer between models or tasks; the same signal read relative to its own running distribution or to a group baseline does — and for the stopping decision the absolute version is provably able to be arbitrarily far from optimal.
  - Six sources test this and none dissents. Hidden-state norm: replacing the adaptive interquartile detector with a fixed threshold collapses AIME24 from 70.00 to 23.33 for recursion and 66.67 to 16.67 for steering, and the paper states the reason plainly — a high norm on GSM8K is a low norm on GPQA. Predictive entropy: CUSUM's two regime densities are re-estimated per model from 100 calibration trajectories, so nothing about the cut-point is portable. Entropy trajectory: EDIS's window size, rebound threshold and spike weighting must be recalibrated per model family because entropy dynamics depend on vocabulary size and training distribution. Token selection: replacing an absolute entropy threshold with the Jensen-Shannon divergence of a token's logit distribution from the group average changes the selected set outright, with the chosen tokens splitting roughly evenly between the high- and low-entropy populations (ratio 1.03 on GSM8K, 0.99 on MATH). Policy updates: under GRPO the governing quantity is not a token's entropy but the deviation of a per-token discriminator from its policy-weighted expectation, which is the same absolute-versus-relative substitution one level down. And the negative result is a theorem rather than a measurement: for a fixed cost coefficient and any constant K there is a finite-horizon stopping problem where the optimal policy's value exceeds K times that of the best fixed-threshold policy, even when the probability that the prefix is already correct is known exactly — because the quantity that decides is the value of continuing, not the value of stopping. The practical reading is that the open problem in this cluster is not which signal to measure but what to measure it against.

## Appears in

- [Optimal Bayesian Stopping for Efficient Inference of Consistent LLM Answers](../../archive/papers/2026/local-5c4c22504406a6aa/summary.md) — Stops self-consistency sampling by Bayesian posterior over which answer is the mode, and proves that tracking only the top two answer counts plus an aggregate is enough for asymptotic optimality.
- [OS-Pruner: Pruning Chains-of-Thought of Reasoning Models via Optimal Stopping](../../archive/papers/2026/local-dbfa51b5159a1a77/summary.md) — Recasts when-to-stop-reasoning as optimal stopping rather than classification, and proves that a fixed threshold on the probability of being correct can be arbitrarily far from optimal even when that probability is known exactly, because the decision needs the value of continuing and not the value of stopping.
- [Optimal Stopping vs Best-Of-N for Inference Time Optimization](../../archive/papers/2025/local-f424beba20f4aecf/summary.md) — Casts each generation as opening a costly box in Weitzman's Pandora's Box problem and learns the optimal stopping threshold online, matching best-of-N quality with 15-35% fewer generations.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
