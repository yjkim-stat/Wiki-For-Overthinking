# foresight

<!-- auto:begin -->

Predicting what comes next before or while acting, treated by both sources as something to train for rather than to hope emerges. One makes it an explicit auxiliary objective — a latent predicting the observation one chunk ahead, supervised in a frozen encoder's feature space — and finds removing it costs 15.6 points, collapsing a world-action model to a reactive policy. The other searches over candidate continuations to find a better reasoning path rather than committing to the first. The pair marks the two available forms: supervise a prediction of the future during training, or search the future at inference. Only the first leaves nothing extra to pay at deployment, since its decoder is discarded once trained.

- **Kind**: concept
- **Also called**: lookahead
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [backtracking](backtracking.md), [causal intervention](causal-intervention.md), [chain of thought](../methods/chain-of-thought.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [CLIP](../models/clip.md), [cosine similarity](../methods/cosine-similarity.md), [flow matching](../methods/flow-matching.md), [Game of 24](../datasets/game-of-24.md), [GPT-4](../models/gpt-4.md), [latent reasoning](latent-reasoning.md), [overthinking](overthinking.md), [Pareto frontier](pareto-frontier.md), [Qwen3-VL-2B](../models/qwen3-vl-2b.md), [reasoning redundancy](reasoning-redundancy.md), [t-SNE](../methods/t-sne.md), [test-time compute](test-time-compute.md), [Tree of Thoughts](../methods/tree-of-thoughts.md)

## Appears in

- [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](../../archive/papers/2023/arxiv-2305-10601/summary.md) — Generalizes chain-of-thought into a search over a tree of intermediate 'thoughts', letting a model self-evaluate branches, look ahead and backtrack instead of committing to one left-to-right path.
- [LiLa-WAM: Lightweight Latent Reasoning World-Action Model for Robotic Manipulation](../../archive/papers/2026/arxiv-2608-03701/summary.md) — Builds a 0.5B world-action model for robot manipulation whose future-state prediction and action generation share one compact latent in a single token stream, specifies the task as a direction in visual feature space instead of language, and shows a frozen self-supervised vision encoder beating a four-times-larger pretrained vision-language backbone at the same training budget.
- [Neural Chain-of-Thought Search: Searching the Optimal Reasoning Path to Enhance Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1149/summary.md) — Reformulates reasoning as a search over thinking strategies, showing sparse reasoning paths exist that are simultaneously more accurate and shorter than standard outputs.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
