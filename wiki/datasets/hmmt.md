# HMMT

<!-- auto:begin -->

A competition-mathematics contest whose problem sets both sources use as evaluation alongside AIME. One includes it among five mathematics benchmarks on which a categorical-critic PPO variant is measured, where the reported gains hold across the set rather than on one contest. The other includes several of its editions in a released trace corpus, in the block recorded with the richest verifier and token-level signals. Neither studies it; its function is the same as the other competition sets in this archive — to show that a mathematics result is not an artefact of a single contest's style.

- **Kind**: dataset
- **Also called**: HMMT Feb'26, HMMT Nov'25, HMMT'25
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [2WikiMultiHopQA](2wikimultihopqa.md), [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [advantage estimation](../concepts/advantage-estimation.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AIME 2026](aime-2026.md), [Bamboogle](bamboogle.md), [BBH](bbh.md), [beam search](../methods/beam-search.md), [best-of-n](../methods/best-of-n.md), [Brumo](brumo.md), [budget forcing](../methods/budget-forcing.md), [CMIMC](cmimc.md), [construct validity](../concepts/construct-validity.md), [DAPO](../methods/dapo.md), [DAPO-Math-17K](dapo-math-17k.md), [DeepSeek-R1](../models/deepseek-r1.md), [expected calibration error](../concepts/expected-calibration-error.md), [gpt-oss-20b](../models/gpt-oss-20b.md), [GRPO](../methods/grpo.md), [HotpotQA](hotpotqa.md), [MMLU-Pro](mmlu-pro.md), [Monte Carlo tree search](../methods/monte-carlo-tree-search.md), [MuSiQue](musique.md), [Natural Questions](natural-questions.md), [pass@k](../methods/pass-k.md), [Phi-4-reasoning](../models/phi-4-reasoning.md), [PopQA](popqa.md), [PPO](../methods/ppo.md), [process reward model](../methods/process-reward-model.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen3-30B-A3B-Thinking-2507](../models/qwen3-30b-a3b-thinking-2507.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [Qwen3.6-35B-A3B](../models/qwen3-6-35b-a3b.md), [reasoning boundary](../concepts/reasoning-boundary.md), [reproducibility](../concepts/reproducibility.md), [reward hacking](../concepts/reward-hacking.md), [reward sparsity](../concepts/reward-sparsity.md), [Search-R1](../methods/search-r1.md), [self-consistency](../methods/self-consistency.md), [test-time scaling](../methods/test-time-scaling.md), [Tree of Thoughts](../methods/tree-of-thoughts.md), [TriviaQA](triviaqa.md), [uncertainty quantification](../concepts/uncertainty-quantification.md)

## Appears in

- [Start Classifying: Categorical Critics for LLM Reinforcement Learning](../../archive/papers/2026/arxiv-2608-02181/summary.md) — Replaces PPO's scalar mean-squared-error critic head with a categorical predictor over a discretized value support trained by cross-entropy against Gaussian-smoothed targets, decodes it back to a scalar for an unchanged GAE update, and shows the resulting critic is better calibrated and produces near-symmetric advantages where the MSE critic penalizes failures two-to-three times harder than it rewards successes.
- [Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility](../../archive/papers/2026/arxiv-2608-04001/summary.md) — Formalizes test-time scaling as budgeted inference over a model's implicit prefix tree, separates three structurally different regimes that a single scalar budget conflates, specifies what a reproducible inference protocol must declare, and releases 1.9 million traces — with the empirical section showing a selection score that makes accuracy fall from 75.56% to 65.83% as the candidate bank grows.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
