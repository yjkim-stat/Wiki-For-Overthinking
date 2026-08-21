# QwQ-32B

<!-- auto:begin -->

QwQ-32B is a reasoning language model that archived papers evaluate on, not a concept, method or dataset; the wiki has no kind for a model, so it is filed under the least wrong of the three available. Risky Business runs it as one of seven open-weight models on HazMart and finds it the best on both axes at 74.7-75.3% chain-of-thought faithfulness and 73.7-73.9% safe action, and it is the only model the paper takes to the mechanistic stage: two anti-correlated (cosine about -0.45) residual-stream directions at the Layer 44 attention output, peaking at the action-commit token, with 5-fold AUROC 0.94 for safety and 0.78 for faithfulness; steering them moves untampered trace length from a median 808 tokens to 742 (-8%) at alpha = +3 on the safety direction and 1,019 (+26%) at -3. A*-Thought uses it as one of three 32B backbones for compressed-reasoning fine-tuning, reporting 2.39x the accuracy of a fine-tuned QwQ-32B under a 512-token budget. Neither paper says anything about how the model itself was built.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [A*-Thought](a-thought.md), [AMC23](../datasets/amc23.md), [Chain-of-Draft](chain-of-draft.md), [chain-of-thought compression](../concepts/chain-of-thought-compression.md), [Chain-of-thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [Chain-of-thought monitorability](../concepts/chain-of-thought-monitorability.md), [gpt-oss-120b](gpt-oss-120b.md), [GSM8K](../datasets/gsm8k.md), [MATH-500](../datasets/math-500.md), [MMLU](../datasets/mmlu.md), [OlympiadBench](../datasets/olympiadbench.md), [overthinking](../concepts/overthinking.md), [Qwen3-8B](qwen3-8b.md), [s1K-1.1](../datasets/s1k-1-1.md), [Token Budget](../concepts/token-budget.md), [TokenSkip](tokenskip.md)

## Appears in

- [Risky Business: Measuring The Faithfulness-Safety Tension](../../archive/papers/2026/arxiv-2608-03745/summary.md) — Introduces HazMart (77 hand-written agentic shopkeeper scenarios) and Targeted Reasoning Replacement, a search-and-replace edit of a model's own reasoning trace, and shows that models which follow their traces more faithfully also follow tampered unsafe traces more often, with two anti-correlated residual-stream directions in QwQ-32B that can be steered independently.
- [A*-Thought: Efficient Reasoning via Bidirectional Compression for Low-Resource Settings](../../archive/papers/2025/title-6ac5c2757444abad/summary.md) — A*-Thought treats a long reasoning trace as a search tree over reasoning spans and uses A* search with a bidirectional importance score to select a short, high-information subset of it as supervised fine-tuning data for compressed reasoning.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
