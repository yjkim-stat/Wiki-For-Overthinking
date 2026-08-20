# self-training

<!-- auto:begin -->

Improving a model on data it generated itself, filtered by some correctness signal. The archive's anchor source bootstraps reasoning by keeping rationales that lead to correct answers and retraining on them, which needs only answers rather than reasoning annotations. The second closes the same loop with an external check, using a symbolic solver's execution output to build a verification context and then reusing the resulting traces as supervised fine-tuning data. Between them the two show the loop's dependence: what can be self-trained is bounded by what can be checked, and the sources differ only in whether the checker is an answer key or a solver.

- **Kind**: concept
- **Also called**: STaR-style training, bootstrapping, self-taught reasoner
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [attention analysis](../methods/attention-analysis.md), [chain of thought](chain-of-thought.md), [circuit complexity](circuit-complexity.md), [CommonsenseQA](../datasets/commonsenseqa.md), [expressivity-learnability gap](expressivity-learnability-gap.md), [few-shot prompting](../methods/few-shot-prompting.md), [gradient descent analysis](../methods/gradient-descent-analysis.md), [hallucination](hallucination.md), [length generalization](length-generalization.md), [post-hoc rationalization](post-hoc-rationalization.md), [state tracking](state-tracking.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [training dynamics](training-dynamics.md), [verification](verification.md)

## Appears in

- [STaR: Bootstrapping Reasoning With Reasoning](../../archive/papers/2022/arxiv-2203-14465/summary.md) — Bootstraps a model's reasoning ability from a handful of rationale examples by generating rationales, keeping only those that reach the right answer, and finetuning on them in a loop.
- [MAC-Reasoner: A Multi-Agent Collaborative Framework for Enhancing Logical Reasoning in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-233/summary.md) — Keeps the LLM as the reasoner while a symbolic solver supplies a Logic-Augmented Context, so conflicts flagged by execution direct attention to violated constraints instead of replacing deduction.
- [Transformers Provably Learn Chain-of-Thought Reasoning with Length Generalization](../../archive/papers/2025/local-fe69869b0e362891/summary.md) — Gives the first optimization guarantee that gradient descent trains constant-depth transformers to solve NC1-complete problems with chain of thought, and shows the algebraic structure of the task decides how far the learned reasoning extrapolates.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
