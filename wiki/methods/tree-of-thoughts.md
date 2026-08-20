# Tree of Thoughts

<!-- auto:begin -->

Organising intermediate reasoning steps into a tree, evaluating thoughts, and searching with lookahead and backtracking rather than following a single chain. Its founding result is the one the archive cites most: 74 percent against 4 percent for chain-of-thought prompting on a constrained arithmetic puzzle, which established structured search as worth studying. The archive's later material bounds where that transfers. On a legal statute task it collapses to 0.13 to 0.21 macro-F1 across four models -- three to four times worse than the same models few-shot, and worse than zero-shot -- with the diagnosis that branches interpret the same statutory language differently and the search has no way to adjudicate between them. So the precondition is a scorer able to compare branches on the axis that matters, which a combinatorial puzzle supplies and an interpretive task does not. One taxonomy source also places it: searching over unfinished partial states is a different statistical object from sampling completed candidates and reducing them, and reporting both under one scalar budget makes results incomparable.

- **Kind**: method
- **Also called**: ToT, tree-of-thoughts
- **Topics**: [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [annotation agreement](../concepts/annotation-agreement.md), [backtracking](../concepts/backtracking.md), [BBH](../datasets/bbh.md), [beam search](beam-search.md), [best-of-n](best-of-n.md), [bootstrap confidence intervals](bootstrap-confidence-intervals.md), [Brumo](../datasets/brumo.md), [budget forcing](budget-forcing.md), [chain of thought](../concepts/chain-of-thought.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [Claude-Sonnet-4](../models/claude-sonnet-4.md), [CMIMC](../datasets/cmimc.md), [construct validity](../concepts/construct-validity.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [few-shot prompting](few-shot-prompting.md), [foresight](../concepts/foresight.md), [Game of 24](../datasets/game-of-24.md), [GPT-4](../models/gpt-4.md), [gpt-oss-20b](../models/gpt-oss-20b.md), [HMMT](../datasets/hmmt.md), [human evaluation](human-evaluation.md), [in-context learning](../concepts/in-context-learning.md), [Llama-3.1-70B](../models/llama-3-1-70b.md), [MMLU-Pro](../datasets/mmlu-pro.md), [Monte Carlo tree search](monte-carlo-tree-search.md), [pass@k](../concepts/pass-k.md), [Phi-4-reasoning](../models/phi-4-reasoning.md), [process reward model](process-reward-model.md), [Qwen3-30B-A3B-Thinking-2507](../models/qwen3-30b-a3b-thinking-2507.md), [Qwen3.6-35B-A3B](../models/qwen3-6-35b-a3b.md), [reproducibility](../concepts/reproducibility.md), [reward hacking](../concepts/reward-hacking.md), [RoBERTa](../models/roberta.md), [self-consistency](self-consistency.md), [test-time scaling](../concepts/test-time-scaling.md), [uncertainty quantification](../concepts/uncertainty-quantification.md), [zero-shot prompting](zero-shot-prompting.md)

## Appears in

- [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](../../archive/papers/2023/arxiv-2305-10601/summary.md) — Generalizes chain-of-thought into a search over a tree of intermediate 'thoughts', letting a model self-evaluate branches, look ahead and backtrack instead of committing to one left-to-right path.
- [Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility](../../archive/papers/2026/arxiv-2608-04001/summary.md) — Formalizes test-time scaling as budgeted inference over a model's implicit prefix tree, separates three structurally different regimes that a single scalar budget conflates, specifies what a reproducible inference protocol must declare, and releases 1.9 million traces — with the empirical section showing a selection score that makes accuracy fall from 75.56% to 65.83% as the candidate bank grows.
- [PROSLEX: A Novel Dataset for Expert-Annotated Legal Statute Prediction for Indian Judiciary](../../archive/papers/2026/arxiv-2608-08830/summary.md) — Builds an expert-annotated Indian Supreme Court dataset in which each applicable statute is paired with the specific text span a legal expert says establishes it, and uses it to show that predicting the right statute and giving the right reason are separable abilities.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
