# Sorry-bench

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: dataset
- **Also called**: SorryBench
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AdvBench](advbench.md), [AIME 2024](aime-2024.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [GPQA-Diamond](gpqa-diamond.md), [HumanEval](humaneval.md), [MATH500](math500.md), [MMLU](mmlu.md), [Phi-4-Reasoning](../methods/phi-4-reasoning.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [Qwen3-8B](../models/qwen3-8b.md), [QwQ-32B](../models/qwq-32b.md), [Selective loss masking](../methods/selective-loss-masking.md), [StrongReject](strongreject.md), [XSTest](xstest.md)

## Appears in

- [ReasoningGuard: Safeguarding Large Reasoning Models with Inference-time Safety Aha Moments](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1453/summary.md) — ReasoningGuard is a training-free, inference-time jailbreak defense for large reasoning models that uses an attention-sink signal to locate the moment reasoning shifts from problem restatement to exploration, injects a crafted 'safety aha' phrase there, then samples multiple continuations and selects the one with the highest sustained attention to that safety phrase -- outperforming nine existing defenses at only 5-9% extra inference cost.
- [When Models Outthink Their Safety: Unveiling and Mitigating Self-Jailbreak in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1118/summary.md) — Decomposing LRM reasoning traces into risk-awareness/risk-analysis/response-strategy stages reveals 'Self-Jailbreak' -- the model correctly identifies harmful intent early but overrides its own judgment during subsequent reasoning (accounting for up to 93.7% of unsafe outputs, dominated by a 'Warning' failure pattern where the model wrongly assumes appending a disclaimer suffices) -- and Chain-of-Guardrail (CoG) fixes this with targeted, step-level reasoning-chain rewrites rather than global safety constraints, achieving safety comparable to the strongest baseline while actually *improving* reasoning accuracy (Qwen3-32B: GPQA-Diamond 54.30->62.38, AIME2024 71.70->82.08) where competing safety methods cost 10+ accuracy points.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
