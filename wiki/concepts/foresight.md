# foresight

<!-- auto:begin -->

Evaluating where a partial reasoning path is heading before committing to it, and across 3 sources one of the two things a search adds over a chain -- the other being backtracking. Its instances: the deliberate problem-solving framework that scores thoughts before expanding them; a world model predicting future states for action selection; and a search over reasoning paths guided by a learned estimate of a path's promise. The archive's related caution about all of them is what the estimator can see: where branches interpret the problem inconsistently and no scorer can adjudicate between them, more lookahead produces more disagreement rather than more coverage, which is the mechanism behind the archive's measured tree-search collapse on an interpretive task.

- **Kind**: concept
- **Also called**: lookahead
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [backtracking](backtracking.md), [beam search](../methods/beam-search.md), [causal intervention](../methods/causal-intervention.md), [chain of thought](chain-of-thought.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [CLIP](../models/clip.md), [cosine similarity](../methods/cosine-similarity.md), [flow matching](../methods/flow-matching.md), [Game of 24](../datasets/game-of-24.md), [GPT-4](../models/gpt-4.md), [latent reasoning](latent-reasoning.md), [Monte Carlo tree search](../methods/monte-carlo-tree-search.md), [overthinking](overthinking.md), [Pareto frontier](pareto-frontier.md), [Qwen3-VL-2B](../models/qwen3-vl-2b.md), [reasoning redundancy](reasoning-redundancy.md), [t-SNE](../methods/t-sne.md), [test-time compute](test-time-compute.md), [Tree of Thoughts](../methods/tree-of-thoughts.md)

## Appears in

- [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](../../archive/papers/2023/arxiv-2305-10601/summary.md) — Generalizes chain-of-thought into a search over a tree of intermediate 'thoughts', letting a model self-evaluate branches, look ahead and backtrack instead of committing to one left-to-right path.
- [LiLa-WAM: Lightweight Latent Reasoning World-Action Model for Robotic Manipulation](../../archive/papers/2026/arxiv-2608-03701/summary.md) — Builds a 0.5B world-action model for robot manipulation whose future-state prediction and action generation share one compact latent in a single token stream, specifies the task as a direction in visual feature space instead of language, and shows a frozen self-supervised vision encoder beating a four-times-larger pretrained vision-language backbone at the same training budget.
- [Neural Chain-of-Thought Search: Searching the Optimal Reasoning Path to Enhance Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1149/summary.md) — Reformulates reasoning as a search over thinking strategies, showing sparse reasoning paths exist that are simultaneously more accurate and shorter than standard outputs.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
