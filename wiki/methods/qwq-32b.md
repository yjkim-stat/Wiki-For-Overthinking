# QwQ-32B

<!-- auto:begin -->

QwQ-32B is a reasoning language model that archived papers evaluate on, not a concept, method or dataset; the wiki has no kind for a model, so it is filed under the least wrong of the three available. Risky Business runs it as one of seven open-weight models on HazMart and finds it the best on both axes at 74.7-75.3% chain-of-thought faithfulness and 73.7-73.9% safe action, and it is the only model the paper takes to the mechanistic stage: two anti-correlated (cosine about -0.45) residual-stream directions at the Layer 44 attention output, peaking at the action-commit token, with 5-fold AUROC 0.94 for safety and 0.78 for faithfulness; steering them moves untampered trace length from a median 808 tokens to 742 (-8%) at alpha = +3 on the safety direction and 1,019 (+26%) at -3. A*-Thought uses it as one of three 32B backbones for compressed-reasoning fine-tuning, reporting 2.39x the accuracy of a fine-tuned QwQ-32B under a 512-token budget. Neither paper says anything about how the model itself was built.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [A*-Thought](a-thought.md), [AIME 2024](../datasets/aime-2024.md), [AMC23](../datasets/amc23.md), [Chain-of-Draft](chain-of-draft.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [Chain-of-thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [Chain-of-thought monitorability](../concepts/chain-of-thought-monitorability.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [GSM8K](../datasets/gsm8k.md), [LLaMA-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [MMLU-Pro](../datasets/mmlu-pro.md), [o1-mini](../models/o1-mini.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3-30B-A3B](../models/qwen3-30b-a3b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-8B](qwen3-8b.md), [s1K-1.1](../datasets/s1k-1-1.md), [Sky-T1](../models/sky-t1.md), [Token Budget](../concepts/token-budget.md), [TokenSkip](tokenskip.md)

## Appears in

- [Risky Business: Measuring The Faithfulness-Safety Tension](../../archive/papers/2026/arxiv-2608-03745/summary.md) — Introduces HazMart (77 hand-written agentic shopkeeper scenarios) and Targeted Reasoning Replacement, a search-and-replace edit of a model's own reasoning trace, and shows that models which follow their traces more faithfully also follow tampered unsafe traces more often, with two anti-correlated residual-stream directions in QwQ-32B that can be steered independently.
- [Reflection Steering: Disentangling Reflection from Reasoning in Activation Space for Token-Efficient Inference](../../archive/papers/2026/arxiv-2608-25542/summary.md) — Reflection Steering is a training-free activation-space intervention that isolates reflection-associated computation from general reasoning via PCA-purified, orthogonalized steering directions calibrated per layer, cutting thinking tokens by 16.9% on average across six model-benchmark settings with accuracy statistically equivalent to the raw model.
- [One Missing Piece for Open-Source Reasoning Models: A Dataset to Mitigate Cold-Starting Short CoT LLMs in RL](../../archive/papers/2025/doi-10-18653-v1-2025-acl-industry-85/summary.md) — Introduces the Long CoT Collection, a 100K-example dataset built by having short-CoT LLMs (GPT-4o) generate o1-style long reasoning traces from a 1K seed of teacher-annotated reasoning flow and thought-budget targets, showing it is a stronger RL cold-start than the base model (2-3x larger RLVR gains) and offers built-in controllability over thought budget to address overthinking.
- [A*-Thought: Efficient Reasoning via Bidirectional Compression for Low-Resource Settings](../../archive/papers/2025/title-6ac5c2757444abad/summary.md) — A*-Thought treats a long reasoning trace as a search tree over reasoning spans and uses A* search with a bidirectional importance score to select a short, high-information subset of it as supervised fine-tuning data for compressed reasoning.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
