# zero-shot prompting

<!-- auto:begin -->

Asking a model to perform a task with no worked examples, and across 3 sources a baseline whose standing has reversed for reasoning-specialised models. The measured reversal: for such models, zero-shot free-form generation now beats few-shot prompting, while the one general model without reasoning tuning collapses to 67.3 percent zero-shot free-form -- below its few-shot results -- with only zero-shot chain of thought at 81.4 beating them, which that source reports as the honest exception bounding its claim. Its other archived appearances are as the weakest arm in a legal-explanation comparison, where zero-shot macro-F1 runs 0.47 to 0.64 against few-shot at 0.64 to 0.71, and as an evaluation setting in theory-of-mind work.

- **Kind**: method
- **Also called**: zero-shot
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [activation steering](activation-steering.md), [annotation agreement](../concepts/annotation-agreement.md), [answer extraction](../concepts/answer-extraction.md), [benchmark design](../concepts/benchmark-design.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [class imbalance](../concepts/class-imbalance.md), [Claude-Sonnet-4](../models/claude-sonnet-4.md), [construct validity](../concepts/construct-validity.md), [cross-validation](cross-validation.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [detection versus control](../concepts/detection-versus-control.md), [difference-in-means direction](difference-in-means-direction.md), [few-shot prompting](few-shot-prompting.md), [Gemini-2.5-Flash](../models/gemini-2-5-flash.md), [Gemini-2.5-pro](../models/gemini-2-5-pro.md), [GPT-4](../models/gpt-4.md), [GPT-5](../models/gpt-5.md), [GSM8K](../datasets/gsm8k.md), [human evaluation](human-evaluation.md), [in-context learning](../concepts/in-context-learning.md), [linear probe](linear-probe.md), [Llama-3.1-70B](../models/llama-3-1-70b.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [permutation test](permutation-test.md), [prompt sensitivity](../concepts/prompt-sensitivity.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3-0.6B](../models/qwen3-0-6b.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [Qwen3.5-2B](../models/qwen3-5-2b.md), [Qwen3-8B](../models/qwen3-8b.md), [representation versus readout](../concepts/representation-versus-readout.md), [RoBERTa](../models/roberta.md), [test-time scaling](../concepts/test-time-scaling.md), [theory of mind](../concepts/theory-of-mind.md), [Tree of Thoughts](tree-of-thoughts.md)

## Appears in

- [Soft Guidance Starts to Outperform CoT Prompting as LLMs Improve](../../archive/papers/2026/arxiv-2608-03550/summary.md) — Finds that few-shot chain-of-thought prompting with dataset examples now performs worse than simply asking a reasoning-specialized model the question — 74.2% against 86.1% on GSM8K for one model — so the field's standard baseline systematically understates modern models and overstates anything benchmarked against it.
- [PROSLEX: A Novel Dataset for Expert-Annotated Legal Statute Prediction for Indian Judiciary](../../archive/papers/2026/arxiv-2608-08830/summary.md) — Builds an expert-annotated Indian Supreme Court dataset in which each applicable statute is paired with the specific text span a legal expert says establishes it, and uses it to show that predicting the right statute and giving the right reason are separable abilities.
- [Avalon-ToM-Bench: Evaluating Fine-Grained Theory of Mind via Asymmetric Game Mechanics](../../archive/papers/2026/arxiv-2608-09638/summary.md) — Turns the hidden-role game Avalon into a diagnostic instrument rather than an arena, decomposing theory of mind into a 2x2 taxonomy of perspective-constrained binary statements, and shows by probing, ground-truth injection and steering that models represent the right answer internally while failing to say it.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
