# formal verification

<!-- auto:begin -->

Checking a claim mechanically in a proof assistant rather than by judgement, which is the strongest form of verification available and the one several entries here reach for to escape the validity problems of model judges. Both sources measure where it leaks, and both find the leak in the same place. The autoformalisation benchmark shows the translation layer is the weak seam: systems mapping natural-language reasoning steps into Lean silently correct invalid inputs into provable statements -- one changed a variable's type so an unsatisfiable premise made the conclusion follow ex falso -- and the systems best at preserving validity on correct inputs are the most prone to repairing incorrect ones, because pipelines fine-tuned to produce correct proofs conflate faithful translation with producing something provable. The proof-as-litmus-test work approaches the same boundary from the generation side. The shared conclusion is that mechanical checking is only as sound as the step that renders an informal claim into the formal language, and that evaluating a formaliser only on inputs that should verify cannot distinguish a faithful translator from a repairing one.

- **Kind**: method
- **Also called**: mechanised verification, proof checking
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [abstention](../concepts/abstention.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [Claude Opus 4.7](../models/claude-opus-4-7.md), [construct validity](../concepts/construct-validity.md), [hallucination](../concepts/hallucination.md), [LLM-as-a-judge](llm-as-a-judge.md), [MATH](../datasets/math.md), [OlympiadBench](../datasets/olympiadbench.md), [outcome reward](../concepts/outcome-reward.md), [process evaluation](process-evaluation.md), [reward hacking](../concepts/reward-hacking.md), [self-correction](../concepts/self-correction.md), [sycophancy](../concepts/sycophancy.md), [verification](../concepts/verification.md)

## Appears in

- [FaithformBench: Benchmarking Faithfulness of Mathematical Chain-of-Thought Autoformalisation](../../archive/papers/2026/arxiv-2608-10916/summary.md) — Tests whether systems that translate natural-language reasoning steps into Lean preserve invalidity as well as validity, by automatically perturbing steps to make them wrong, and finds pervasive silent correction -- with the systems best at preserving valid inputs the most likely to repair invalid ones.
- [Mathematical Proof as a Litmus Test: Revealing Failure Modes of Advanced Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-582/summary.md) — Uses 200 mathematical proof problems as a diagnostic, finding some reasoning models solve under 20% and cataloguing 10 fine-grained error types that numerical benchmarks hide.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
