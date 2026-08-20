# Tree of Thoughts

<!-- auto:begin -->

Search over a tree whose nodes are partial solutions expressed as intermediate thoughts, with explicit generation of alternatives, evaluation of states, and backtracking — the work that moved deliberate reasoning from a single linear chain to a searched structure. The two sources bracket its position in this archive. One is the original method, introducing lookahead and backtracking as operations a scaffold performs around the model. The other places it in a formal taxonomy as an instance of prefix-level scaling — compute allocated on scores for *unfinished* states — and notes that its controller operates over thought-level rather than token-level expansions, which is what distinguishes it from beam search and from leaf-level sampling with a terminal reducer.

- **Kind**: method
- **Also called**: ToT
- **Topics**: [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [backtracking](../concepts/backtracking.md), [BBH](../datasets/bbh.md), [beam search](beam-search.md), [best-of-n](best-of-n.md), [bootstrap confidence intervals](bootstrap-confidence-intervals.md), [Brumo](../datasets/brumo.md), [budget forcing](budget-forcing.md), [chain of thought](chain-of-thought.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [CMIMC](../datasets/cmimc.md), [construct validity](../concepts/construct-validity.md), [DeepSeek-R1](../models/deepseek-r1.md), [foresight](../concepts/foresight.md), [Game of 24](../datasets/game-of-24.md), [GPT-4](../models/gpt-4.md), [gpt-oss-20b](../models/gpt-oss-20b.md), [HMMT](../datasets/hmmt.md), [MMLU-Pro](../datasets/mmlu-pro.md), [Monte Carlo tree search](monte-carlo-tree-search.md), [pass@k](../concepts/pass-k.md), [Phi-4-reasoning](../models/phi-4-reasoning.md), [process reward model](../concepts/process-reward-model.md), [Qwen3-30B-A3B-Thinking-2507](../models/qwen3-30b-a3b-thinking-2507.md), [Qwen3.6-35B-A3B](../models/qwen3-6-35b-a3b.md), [reproducibility](../concepts/reproducibility.md), [reward hacking](../concepts/reward-hacking.md), [self-consistency](self-consistency.md), [test-time scaling](../concepts/test-time-scaling.md), [uncertainty quantification](../concepts/uncertainty-quantification.md)

## Appears in

- [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](../../archive/papers/2023/arxiv-2305-10601/summary.md) — Generalizes chain-of-thought into a search over a tree of intermediate 'thoughts', letting a model self-evaluate branches, look ahead and backtrack instead of committing to one left-to-right path.
- [Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility](../../archive/papers/2026/arxiv-2608-04001/summary.md) — Formalizes test-time scaling as budgeted inference over a model's implicit prefix tree, separates three structurally different regimes that a single scalar budget conflates, specifies what a reproducible inference protocol must declare, and releases 1.9 million traces — with the empirical section showing a selection score that makes accuracy fall from 75.56% to 65.83% as the candidate bank grows.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
