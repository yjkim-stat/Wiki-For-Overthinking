# Brumo

<!-- auto:begin -->

A competition-mathematics benchmark, used by both sources as one of several olympiad-level sets rather than as an object of study. Neither reports anything about it specifically: one includes it among five mathematics benchmarks where a categorical PPO critic improves avg@256 from 18.20 to 21.40, the other among the sets where a constraint-extraction prompting protocol improves over direct chain of thought on multiple backbones. Its role in the archive is as part of the tail of competition sets that get reported alongside AIME to show a result is not specific to one contest.

- **Kind**: dataset
- **Also called**: BRUMO
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [2WikiMultiHopQA](2wikimultihopqa.md), [advantage estimation](../concepts/advantage-estimation.md), [AIME](aime.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [Bamboogle](bamboogle.md), [chain of thought](../methods/chain-of-thought.md), [DAPO](../methods/dapo.md), [DAPO-Math-17k](dapo-math-17k.md), [expected calibration error](../concepts/expected-calibration-error.md), [GRPO](../methods/grpo.md), [HotpotQA](hotpotqa.md), [MuSiQue](musique.md), [Natural Questions](natural-questions.md), [OlympiadBench](olympiadbench.md), [PopQA](popqa.md), [PPO](../methods/ppo.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [reasoning boundary](../concepts/reasoning-boundary.md), [reward sparsity](../concepts/reward-sparsity.md), [routing](../concepts/routing.md), [Search-R1](../methods/search-r1.md), [self-verification](../concepts/self-verification.md), [TriviaQA](triviaqa.md), [verification](../concepts/verification.md)

## Appears in

- [Start Classifying: Categorical Critics for LLM Reinforcement Learning](../../archive/papers/2026/arxiv-2608-02181/summary.md) — Replaces PPO's scalar mean-squared-error critic head with a categorical predictor over a discretized value support trained by cross-entropy against Gaussian-smoothed targets, decodes it back to a scalar for an unchanged GAE update, and shows the resulting critic is better calibrated and produces near-symmetric advantages where the MSE critic penalizes failures two-to-three times harder than it rewards successes.
- [Constraint-First Reasoning: A Training-Free Protocol for Exploiting Answer-Space Constraints in Mathematical Problem Solving](../../archive/papers/2026/arxiv-2608-05254/summary.md) — A training-free two-stage prompting protocol that extracts a problem's answer-space constraints first and then checks its own intermediate and final results against them, routed on by a regex detector.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
