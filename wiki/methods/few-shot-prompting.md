# few-shot prompting

<!-- auto:begin -->

Supplying worked examples in the prompt so the model imitates their form. In the cited sources it appears as infrastructure rather than as a subject, and in both cases as something with a cost. One notes that inducing rationale generation through few-shot inference alone sacrifices accuracy relative to finetuning, which is the gap its bootstrapping loop exists to close. The other turns the format into an attack surface: reordering the multiple-choice options across few-shot examples so the answer is always '(A)' biases the model's prediction, and the resulting explanation does not mention the pattern. The arrangement of the examples, not only their content, is doing work.

- **Kind**: method
- **Also called**: few-shot inference, in-context learning
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [answer extraction](../concepts/answer-extraction.md), [BBH](../datasets/bbh.md), [chain of thought](chain-of-thought.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [CommonsenseQA](../datasets/commonsenseqa.md), [construct validity](../concepts/construct-validity.md), [GSM8K](../datasets/gsm8k.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [post-hoc rationalization](../concepts/post-hoc-rationalization.md), [prompt sensitivity](../concepts/prompt-sensitivity.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [self-training](../concepts/self-training.md), [supervised fine-tuning](supervised-fine-tuning.md)

## Appears in

- [STaR: Bootstrapping Reasoning With Reasoning](../../archive/papers/2022/arxiv-2203-14465/summary.md) — Bootstraps a model's reasoning ability from a handful of rationale examples by generating rationales, keeping only those that reach the right answer, and finetuning on them in a loop.
- [Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting](../../archive/papers/2023/arxiv-2305-04388/summary.md) — Shows that chain-of-thought explanations systematically misrepresent the real reason for a model's answer, by biasing inputs in ways the model never mentions and watching it rationalize the biased answer.
- [Soft Guidance Starts to Outperform CoT Prompting as LLMs Improve](../../archive/papers/2026/arxiv-2608-03550/summary.md) — Finds that few-shot chain-of-thought prompting with dataset examples now performs worse than simply asking a reasoning-specialized model the question — 74.2% against 86.1% on GSM8K for one model — so the field's standard baseline systematically understates modern models and overstates anything benchmarked against it.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
