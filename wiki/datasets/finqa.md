# FinQA

<!-- auto:begin -->

A financial question-answering dataset built from real financial reports, used in both sources as the human-annotated point of comparison that symbolic generation is offered as an alternative to. Both make the same argument against it without disputing its usefulness: because it is constructed from real documents by annotation or model-assisted extraction, it conflates source-level noise -- formatting irregularities, missing values, ambiguous phrasing -- with genuine reasoning failure, and because ground truth is written by hand its cost makes broad coverage of reasoning depths prohibitive. Both respond by generating items from executable symbolic structures instead, so answers are correct by construction, difficulty is a controllable dial, and the benchmark can be regenerated free of contamination. Its one appearance as a measurement here is as a transfer check rather than a target: a model fine-tuned on verified generated traces answers 32 of 100 FinQA questions against a baseline of 27, reported explicitly as a proof of concept to test whether the gain was overfitting rather than as a result.

- **Kind**: dataset
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [adversarial robustness](../concepts/adversarial-robustness.md), [benchmark contamination](../concepts/benchmark-contamination.md), [benchmark design](../concepts/benchmark-design.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [construct validity](../concepts/construct-validity.md), [DeepSeek-V4-Flash](../models/deepseek-v4-flash.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [Llama-3.3-70B](../models/llama-3-3-70b.md), [LoRA](../methods/lora.md), [process evaluation](../concepts/process-evaluation.md), [Qwen3.5-4B](../models/qwen3-5-4b.md), [Qwen3.5-9B](../models/qwen3-5-9b.md), [reasoning depth](../concepts/reasoning-depth.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [verification](../concepts/verification.md)

## Appears in

- [V-FiLLM: Verified Financial LLM Reasoning Benchmark](../../archive/papers/2026/arxiv-2608-11047/summary.md) — Generates financial reasoning benchmarks from executable computation trees over real tables so that answers are correct by construction with no model in the labelling loop, exposes four independently controllable difficulty axes, and finds that unit and scale perturbations collapse the strongest model from 98.4 percent to 3.0.
- [FinChain: A Symbolic Benchmark for Verifiable Chain-of-Thought Financial Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-662/summary.md) — A financial reasoning benchmark built from parameterized symbolic templates with executable Python, giving machine-verifiable step-level ground truth and contamination-free regeneration.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
