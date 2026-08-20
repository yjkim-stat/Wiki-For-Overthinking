# self-training

<!-- auto:begin -->

Training a model on its own filtered outputs, and across 3 sources the oldest idea in this archive's training material -- generate rationales, keep those reaching the right answer, fine-tune, repeat. Its modern descendants here filter differently: by consensus among rollouts rather than by a gold answer, by a symbolic solver's flagged conflicts, or by measured marginal utility on a held-out probe set. Two cautions the corpus supplies. Filtering for reaching a known answer selects for post-hoc rationalisations that happen to land correctly, so the resulting corpus is not a sample of the model's reasoning. And consensus-based filtering inherits spurious consensus, which grows rather than shrinks with the sample count. One theoretical source proves a learning result for the setting, on how a transformer comes to learn a chain-of-thought procedure with length generalisation.

- **Kind**: method
- **Also called**: STaR-style training, bootstrapping, self-taught reasoner
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [attention analysis](attention-analysis.md), [chain of thought](../concepts/chain-of-thought.md), [circuit complexity](../concepts/circuit-complexity.md), [CommonsenseQA](../datasets/commonsenseqa.md), [consensus](../concepts/consensus.md), [expressivity-learnability gap](../concepts/expressivity-learnability-gap.md), [few-shot prompting](few-shot-prompting.md), [gradient descent analysis](gradient-descent-analysis.md), [hallucination](../concepts/hallucination.md), [length generalization](../concepts/length-generalization.md), [post-hoc rationalization](../concepts/post-hoc-rationalization.md), [rejection sampling](rejection-sampling.md), [self-distillation](self-distillation.md), [state tracking](../concepts/state-tracking.md), [supervised fine-tuning](supervised-fine-tuning.md), [training dynamics](../concepts/training-dynamics.md), [verification](../concepts/verification.md)

## Appears in

- [STaR: Bootstrapping Reasoning With Reasoning](../../archive/papers/2022/arxiv-2203-14465/summary.md) — Bootstraps a model's reasoning ability from a handful of rationale examples by generating rationales, keeping only those that reach the right answer, and finetuning on them in a loop.
- [MAC-Reasoner: A Multi-Agent Collaborative Framework for Enhancing Logical Reasoning in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-233/summary.md) — Keeps the LLM as the reasoner while a symbolic solver supplies a Logic-Augmented Context, so conflicts flagged by execution direct attention to violated constraints instead of replacing deduction.
- [Transformers Provably Learn Chain-of-Thought Reasoning with Length Generalization](../../archive/papers/2025/local-fe69869b0e362891/summary.md) — Gives the first optimization guarantee that gradient descent trains constant-depth transformers to solve NC1-complete problems with chain of thought, and shows the algebraic structure of the task decides how far the learned reasoning extrapolates.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
