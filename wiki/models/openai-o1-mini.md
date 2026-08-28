# OpenAI o1-mini

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Best-of-N (baseline)](../methods/best-of-n-baseline.md), [DeepSeek-R1](deepseek-r1.md), [DeepSeek-R1-Distill-Llama-70B](deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Qwen-1.5B](deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-14B](deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [DeepSeek-V3](deepseek-v3.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [GPT-4o](gpt-4o.md), [Grok-3](grok-3.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [Kimi-k1.5](kimi-k1-5.md), [LiveCodeBench](../datasets/livecodebench.md), [LoRA fine-tuning](../methods/lora-fine-tuning.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [Omni-MATH](../datasets/omni-math.md), [Qwen2.5-Math-1.5B-Instruct](qwen2-5-math-1-5b-instruct.md), [Qwen3-Max](qwen3-max.md), [s1-32B](s1-32b.md)

## Appears in

- [Guided by Gut: Efficient Test-Time Scaling with Reinforced Intrinsic Confidence](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-739/summary.md) — Guided by Gut (GG) replaces external Process Reward Models in tree-search test-time scaling with the LLM's own intrinsic token-probability confidence, calibrated via a GRPO reward that heavily penalizes overconfident wrong answers (penalty in [-9,1] vs. reward in [1,2] for correct ones), letting a 1.5B-7B model match or exceed models 10-70x larger while using 4-10x less GPU memory and 8x faster inference than PRM-guided search.
- [BloomEval: A Bloom’s Cognitive Taxonomy-Based Benchmark for Evaluating LRMs via Cognitive Hierarchy Trace](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1262/summary.md) — BloomEval maps each step of an LRM's reasoning trace onto Bloom's six-level cognitive taxonomy (Remember through Create) via a Cognitive Hierarchy Trace (CHT), defining structural anomalies -- hierarchy break (reasoning never reaches the required cognitive level), hierarchy jump (skipping intermediate levels), and overthinking (invoking cognitive operations exceeding what the task needs) -- and finds these anomalies are common even in *correct* answers (e.g. Grok-3 shows a 0.185 hierarchy-jump rate on correct answers), demonstrating that answer accuracy alone cannot detect incoherent or wasteful reasoning structure.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
