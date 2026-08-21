# reasoning graph

<!-- auto:begin -->

The two archived sources give the phrase two different referents. In Topology of Reasoning it is built out of the model: hidden states at each step of a chain of thought are clustered into nodes and joined in generation order, then measured by cyclicity, diameter and small-world index -- distilled models show about 5 recurrent cycles per sample and roughly 6x higher small-world index than base models, cycle detection peaks at 14B scale and diameter at 32B, and these properties correlate positively with accuracy on GSM8K, MATH500 and AIME 2024. In DARG it is built out of the task: the explicit structure of the reasoning an existing benchmark item requires, which can then be perturbed in depth or width to emit new items at controlled complexity, with a code-augmented LLM verifying the answer each perturbed graph implies. So the term names both an observed trace of a model's computation and a specification of a problem's structure, and only the first is grounded in anything measurable inside the model.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [GSM8K](../datasets/gsm8k.md), [MATH-500](../datasets/math-500.md), [reasoning graph extraction](../methods/reasoning-graph-extraction.md)

## Appears in

- [Topology of Reasoning: Understanding Large Reasoning Models through Reasoning Graph Properties](../../archive/papers/2025/title-11c5eb0da4499b68/summary.md) — Analyzes large reasoning models by clustering their hidden states into a 'reasoning graph' and studying how its cyclicity, diameter and small-world structure relate to task difficulty, model scale and accuracy.
- [DARG: Dynamic Evaluation of Large Language Models via Adaptive Reasoning Graph](../../archive/papers/2024/title-f4deea1ce7836f59/summary.md) — A benchmark-construction framework that extracts the reasoning graph behind each item in an existing benchmark and perturbs it to generate new test items at controlled complexity levels, then measures how 15 LLMs degrade as complexity rises.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
