# answer extraction

<!-- auto:begin -->

How a scorer recovers the final answer from a model's output, and in both sources a source of measured effect that is routinely mistaken for reasoning. One shows an apparent nine-point gain from adding in-context examples is a rule-based parser learning to find the answer pattern — the underlying solutions are identical and a prompt-based extractor scores the same configurations stably throughout, with invalid-answer rates falling from 96.5% to 4.6% over the same range. The other decomposes reported self-correction gains into a content margin and format-recovery margins and finds causally that most of what the field has reported as self-correction is answer-parseability repair. Both therefore locate a large published effect in the scorer rather than in the model, which makes this the cheapest confound in the archive to control and the one least often controlled.

- **Kind**: concept
- **Also called**: answer parsing
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [calibration](../methods/calibration.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [construct validity](construct-validity.md), [few-shot prompting](../methods/few-shot-prompting.md), [Gemma-4-12B](../models/gemma-4-12b.md), [GSM8K](../datasets/gsm8k.md), [in-context learning](in-context-learning.md), [inverse scaling](inverse-scaling.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [prompt sensitivity](prompt-sensitivity.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [self-correction](self-correction.md), [zero-shot prompting](../methods/zero-shot-prompting.md)

## What we have settled

- **Established** — An evaluation baseline, prompt or output format inherited from prior work is an experimental variable, not a fixed point: comparisons against it routinely measure the mismatch between the apparatus and the model rather than the method under test.
  - Three instances in three domains, each with the confound measured rather than argued. Few-shot chain-of-thought prompting with dataset examples — the standard baseline in official model releases — costs a reasoning-specialized model roughly twelve points on GSM8K against no prompting at all (74.2% against 86.1%), so any method benchmarked as an improvement over it collects that deficit as free gain; the same paper shows an apparent nine-point scaling curve in the number of demonstrations is a rule-based parser learning to find the answer, with the underlying solutions unchanged. The standard MQM translation-evaluation prompt is specialized to the model it was authored against, and every other model including that model's own successor performs significantly worse under it, while enforcing structured output degrades judgement quality across all models and minor changes to the parsing heuristic move the reported metric with model output held fixed. And a vision-language selection rule reporting a 31.8-point gain over majority voting loses all of it to a control that merely matches the decoding format, because the baseline aggregated long chains while the method aggregated short answers.

## Appears in

- [Soft Guidance Starts to Outperform CoT Prompting as LLMs Improve](../../archive/papers/2026/arxiv-2608-03550/summary.md) — Finds that few-shot chain-of-thought prompting with dataset examples now performs worse than simply asking a reasoning-specialized model the question — 74.2% against 86.1% on GSM8K for one model — so the field's standard baseline systematically understates modern models and overstates anything benchmarked against it.
- [The Calibration Floor: Format Repair Can Masquerade as Self-Correction at Small-to-Mid Scale](../../archive/papers/2026/arxiv-2608-04355/summary.md) — Decomposes measured self-correction gains into a content margin and format-recovery margins, and shows causally that most of what the field has reported as self-correction is answer-parseability repair.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
