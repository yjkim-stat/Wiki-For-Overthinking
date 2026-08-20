# zero-shot prompting

<!-- auto:begin -->

Asking a model to do a task with no worked examples in the prompt, and in these sources the baseline whose status has changed. One source measures the reversal directly: few-shot chain-of-thought prompting with dataset exemplars now scores below simply asking a reasoning-specialised model the question -- 74.2 percent against 86.1 on GSM8K for one model -- so the field's standard few-shot baseline systematically understates modern models and overstates anything benchmarked against it. The second uses zero-shot as its only condition, prompting 28 models with one fixed template of game setup, public history and a single perspective-constrained statement, which lets it compare across proprietary and open models without the confound of exemplar choice; it then finds that toggling chain of thought on the same weights changes accuracy by only +1.1 points on average with the sign mixed, while reasoning training on the same base model gives +11.0. Read together they suggest the prompt-side interventions that once carried a result now carry little of one, and that what a model was trained to do dominates what it is asked to do.

- **Kind**: method
- **Also called**: zero-shot
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [activation steering](activation-steering.md), [answer extraction](../concepts/answer-extraction.md), [benchmark design](../concepts/benchmark-design.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [class imbalance](../concepts/class-imbalance.md), [construct validity](../concepts/construct-validity.md), [detection versus control](../concepts/detection-versus-control.md), [difference-in-means direction](difference-in-means-direction.md), [few-shot prompting](few-shot-prompting.md), [Gemini-2.5-Flash](../models/gemini-2-5-flash.md), [Gemini-2.5-pro](../models/gemini-2-5-pro.md), [GPT-5](../models/gpt-5.md), [GSM8K](../datasets/gsm8k.md), [in-context learning](../concepts/in-context-learning.md), [linear probe](linear-probe.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [permutation test](permutation-test.md), [prompt sensitivity](../concepts/prompt-sensitivity.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3-0.6B](../models/qwen3-0-6b.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [Qwen3.5-2B](../models/qwen3-5-2b.md), [Qwen3-8B](../models/qwen3-8b.md), [representation versus readout](../concepts/representation-versus-readout.md), [test-time scaling](../concepts/test-time-scaling.md), [theory of mind](../concepts/theory-of-mind.md)

## Appears in

- [Soft Guidance Starts to Outperform CoT Prompting as LLMs Improve](../../archive/papers/2026/arxiv-2608-03550/summary.md) — Finds that few-shot chain-of-thought prompting with dataset examples now performs worse than simply asking a reasoning-specialized model the question — 74.2% against 86.1% on GSM8K for one model — so the field's standard baseline systematically understates modern models and overstates anything benchmarked against it.
- [Avalon-ToM-Bench: Evaluating Fine-Grained Theory of Mind via Asymmetric Game Mechanics](../../archive/papers/2026/arxiv-2608-09638/summary.md) — Turns the hidden-role game Avalon into a diagnostic instrument rather than an arena, decomposing theory of mind into a 2x2 taxonomy of perspective-constrained binary statements, and shows by probing, ground-truth injection and steering that models represent the right answer internally while failing to say it.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
