# paired bootstrap confidence intervals

<!-- auto:begin -->

Resampling matched observations in pairs to put an interval on a difference, used by both sources to keep a per-instance comparison from being read as a mean effect. One reports per-category intervals on the difference between a selection rule and a format-matched control, and its central negative claim is exactly that every interval overlaps zero with one lying entirely below it. The other pairs a wrong completion against a correct one on the same problem and prompt condition, so the resampling unit is the pair rather than the run. In both the technique is doing the same work: a difference computed on matched units, with an interval, is what separates a real effect from an average that could be produced by a handful of instances.

- **Kind**: method
- **Also called**: paired bootstrap
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [backtracking](../concepts/backtracking.md), [best-of-n](best-of-n.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [majority voting](majority-voting.md), [monitorability](../concepts/monitorability.md), [overthinking](../concepts/overthinking.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-8B](../models/qwen3-8b.md), [reasoning boundary](../concepts/reasoning-boundary.md), [self-consistency](self-consistency.md), [self-correction](../concepts/self-correction.md), [test-time scaling](test-time-scaling.md), [visual grounding](../concepts/visual-grounding.md)

## Appears in

- [It's the Decoding Format, Not the Perturbation: Auditing Consistency-Based Selection for Vision-Language Test-Time Scaling](../../archive/papers/2026/arxiv-2608-01207/summary.md) — Shows that a perturbation-based selection rule's apparent 31.8-point gain over majority voting in vision-language test-time scaling is a decoding-format effect, by adding a control that spends the same short-answer budget on the unperturbed image and finds it matches or beats the perturbation rule everywhere.
- [The Tell-Tale Trace: Detecting Reasoning Failures in LLMs Using Chain-of-Thought Dynamics](../../archive/papers/2026/arxiv-2608-03291/summary.md) — Tags every sentence of a reasoning trace by its function and studies the sequence rather than the content, finding that failing SAT traces collapse into repetitive verification and commit early, that failing UNSAT traces run the wrong procedure entirely, and that a prompt naming the missing procedure recovers 84.6% of them.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
