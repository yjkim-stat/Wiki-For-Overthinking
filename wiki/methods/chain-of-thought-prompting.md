# chain-of-thought prompting

<!-- auto:begin -->

Eliciting step-by-step reasoning before an answer, either by an instruction or by few-shot examples that display it. Across the four sources it is never the object of study but always the baseline everything is measured against: it is what Tree of Thoughts generalizes by allowing branching and backtracking, what the faithfulness papers intervene on to test whether the stated steps are load-bearing, and what the theory paper explains by showing that the intermediate tokens loop back into the input and so raise the model's effective circuit depth. That last source is careful to separate the two things the phrase can mean, noting it studies why a model equipped with CoT succeeds rather than which prompt triggers the process — a question it lists as unresolved.

- **Kind**: method
- **Also called**: CoT prompting
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 5

**Related**: [causal analysis](causal-analysis.md), [chain of thought](chain-of-thought.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [circuit analysis](circuit-analysis.md), [circuit complexity](../concepts/circuit-complexity.md), [effective depth](../concepts/effective-depth.md), [expressivity](../concepts/expressivity.md), [few-shot prompting](few-shot-prompting.md), [Game of 24](../datasets/game-of-24.md), [implicit reasoning](../concepts/implicit-reasoning.md), [inverse scaling](../concepts/inverse-scaling.md), [memorization](../concepts/memorization.md), [out-of-distribution generalization](../concepts/out-of-distribution-generalization.md), [post-hoc rationalization](../concepts/post-hoc-rationalization.md), [process supervision](../concepts/process-supervision.md), [retrieval-augmented generation](retrieval-augmented-generation.md), [test-time compute](../concepts/test-time-compute.md)

## Appears in

- [Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting](../../archive/papers/2023/arxiv-2305-04388/summary.md) — Shows that chain-of-thought explanations systematically misrepresent the real reason for a model's answer, by biasing inputs in ways the model never mentions and watching it rationalize the biased answer.
- [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](../../archive/papers/2023/arxiv-2305-10601/summary.md) — Generalizes chain-of-thought into a search over a tree of intermediate 'thoughts', letting a model self-evaluate branches, look ahead and backtrack instead of committing to one left-to-right path.
- [Measuring Faithfulness in Chain-of-Thought Reasoning](../../archive/papers/2023/arxiv-2307-13702/summary.md) — Measures how much a model's answer actually depends on its stated chain of thought by intervening on the trace — adding mistakes, paraphrasing, truncating — and finds the dependence varies by task and decreases as models get larger.
- [Grokked Transformers are Implicit Reasoners: A Mechanistic Journey to the Edge of Generalization](../../archive/papers/2024/local-6252abed1b134f57/summary.md) — Shows that transformers can learn implicit multi-step reasoning over stored knowledge, but only through grokking — extended training far past overfitting — and that whether the resulting circuit generalizes out of distribution depends on the reasoning type, succeeding for comparison and failing for composition.
- [Towards Revealing the Mystery behind Chain of Thought: A Theoretical Perspective](../../archive/papers/2023/local-f3c308f76ff7a114/summary.md) — Proves via circuit complexity that bounded-depth Transformers cannot directly solve basic arithmetic, linear equations or general dynamic programming unless their size grows super-polynomially, while constant-size autoregressive Transformers can solve all of them by generating chain-of-thought derivations.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
