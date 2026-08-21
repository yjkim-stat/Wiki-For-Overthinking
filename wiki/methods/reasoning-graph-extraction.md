# reasoning graph extraction

<!-- auto:begin -->

The step that produces a reasoning graph -- and the two archived sources extract from opposite ends, so the phrase covers two procedures rather than one. In Topology of Reasoning extraction reads the graph out of the model: hidden-state representations are taken at each reasoning step, clustered into nodes and linked by generation order, after which graph-theoretic properties are correlated with accuracy. In DARG extraction reads the graph out of the task: for each item in an existing benchmark the reasoning it demands is recovered as an explicit structure, which is then perturbed to generate harder variants whose labels a code-augmented LLM verifies. Neither paper's extraction procedure is recorded in detail in the material the archive holds; for Topology of Reasoning no PDF was attached, so the clustering step in particular is unverified.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [GSM8K](../datasets/gsm8k.md), [MATH500](../datasets/math500.md), [reasoning graph](../concepts/reasoning-graph.md)

## Appears in

- [Topology of Reasoning: Understanding Large Reasoning Models through Reasoning Graph Properties](../../archive/papers/2025/title-11c5eb0da4499b68/summary.md) — Analyzes large reasoning models by clustering their hidden states into a 'reasoning graph' and studying how its cyclicity, diameter and small-world structure relate to task difficulty, model scale and accuracy.
- [DARG: Dynamic Evaluation of Large Language Models via Adaptive Reasoning Graph](../../archive/papers/2024/title-f4deea1ce7836f59/summary.md) — A benchmark-construction framework that extracts the reasoning graph behind each item in an existing benchmark and perturbs it to generate new test items at controlled complexity levels, then measures how 15 LLMs degrade as complexity rises.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
