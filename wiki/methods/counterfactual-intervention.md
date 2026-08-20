# counterfactual intervention

<!-- auto:begin -->

A causal-analysis technique that alters part of a reasoning trace (e.g. an intermediate thinking-draft step, or a model's implicit first guess) and observes whether the final answer changes, to test whether that part actually drove the outcome rather than being post-hoc narration. Used in the archive to test chain-of-thought faithfulness (Measuring the Faithfulness of Thinking Drafts, RFEval) and to establish that an implicit first-guess bias causally triggers overthinking (The First Impression Problem).

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [overthinking](../concepts/overthinking.md)

## Appears in

- [Measuring the Faithfulness of Thinking Drafts in Large Reasoning Models](../../archive/papers/2025/title-201a19641c43ace7/summary.md) — Introduces a counterfactual intervention framework to test whether large reasoning models' intermediate thinking-draft steps and final answers are causally faithful to each other, finding they often are not.
- [The First Impression Problem: Internal Bias Triggers Overthinking in Reasoning Models](../../archive/papers/2026/title-51fe00fa979d4d8f/summary.md) — Identifies an implicit first-guess bias formed on reading a question as a causal driver of overthinking in reasoning models, verified through counterfactual interventions and attention analysis.
- [RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models](../../archive/papers/2026/title-9f5aee65dee28f12/summary.md) — Introduces RFEval, a benchmark that uses counterfactual interventions to test whether an LRM's stated chain-of-thought causally drives its answer, finding 49.7% of outputs unfaithful.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
