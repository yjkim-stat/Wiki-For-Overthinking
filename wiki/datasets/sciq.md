# SciQ

<!-- auto:begin -->

Neither source describes SciQ directly; it appears only as a named evaluation benchmark. The adaptive-sampling source uses it as one of several benchmarks against which a hand-written fuzzy controller sets a per-prompt best-of-N budget; ThinkRetrieve uses it as one of the QA benchmarks on which its step-level retrieval of worked examples is compared to standard sequential test-time scaling.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2025](aime-2025.md), [Best-of-N sampling](../methods/best-of-n-sampling.md), [GSM8K](gsm8k.md), [Llama3.1-8B-Instruct](../models/llama3-1-8b-instruct.md), [LoRA fine-tuning](../methods/lora-fine-tuning.md), [MATH](math.md), [MATH500](math500.md), [MathQA](mathqa.md), [Qwen2.5-1.5B-Instruct](../models/qwen2-5-1-5b-instruct.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [retrieval-augmented reasoning](../concepts/retrieval-augmented-reasoning.md), [sequential test-time scaling](../concepts/sequential-test-time-scaling.md), [Test-Time Scaling](../concepts/test-time-scaling.md), [TriviaQA](triviaqa.md)

## Appears in

- [Interpretable Adaptive Sampling for LLM Test-Time Scaling](../../archive/papers/2026/arxiv-2608-03961/summary.md) — Assigns a per-prompt sampling budget for best-of-N test-time scaling with a hand-written two-stage fuzzy controller over nine prompt- and model-side signals, trading 1.4-14.5% fewer samples for accuracy changes between -1.8 and +0.5 points against a selector-matched fixed N = 8 baseline.
- [ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling](../../archive/papers/2026/arxiv-2608-10928/summary.md) — ThinkRetrieve augments each step of a reasoning model's chain of thought with a dynamically retrieved, fully worked solved example (rather than just facts), consistently beating standard sequential test-time scaling on math and QA benchmarks.
- [GrACE: A Generative Approach to Better Confidence Elicitation and Efficient Test-Time Scaling in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1069/summary.md) — GrACE teaches an LLM to output a discriminative, calibrated confidence score during generation itself -- via the similarity between the last hidden state and a learned embedding for a special <CNF> token, trained against k-fold-binned accuracy targets -- eliminating the separate evaluation stage post-generation methods require, and uses this on-the-fly confidence to weight self-consistency voting and drive early-stopping, improving test-time-scaling accuracy by up to 3.3% while cutting required samples by more than half in many cases.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
