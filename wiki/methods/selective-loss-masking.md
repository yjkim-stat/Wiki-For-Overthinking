# Selective loss masking

<!-- auto:begin -->

Selective loss masking is a training technique that restricts the SFT loss to specific segments of a long reasoning trace rather than the whole sequence -- used in Segment-Level Attribution (which picks segments via integrated-gradient token attribution aggregated into per-segment strength/direction-consistency scores) and referenced in the context of 'Self-Jailbreak', where decomposing reasoning traces into risk-awareness/risk-analysis/response-strategy stages reveals models that correctly identify harmful intent early but fail to act on it later.

- **Kind**: method
- **Also called**: Selective Loss Masking
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AMC23](../datasets/amc23.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [HumanEval](../datasets/humaneval.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [OlympiadBench](../datasets/olympiadbench.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-8B](../models/qwen3-8b.md), [StrongReject](../datasets/strongreject.md), [TokenSkip](tokenskip.md)

## Appears in

- [Segment-Level Attribution for Selective Learning of Long Reasoning Traces](../../archive/papers/2026/arxiv-2602-00425/summary.md) — Uses integrated-gradient token attribution, aggregated into per-segment strength and direction-consistency scores, to pick which segments of a long chain-of-thought an SFT run should compute loss on, masking the rest.
- [When Models Outthink Their Safety: Unveiling and Mitigating Self-Jailbreak in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1118/summary.md) — Decomposing LRM reasoning traces into risk-awareness/risk-analysis/response-strategy stages reveals 'Self-Jailbreak' -- the model correctly identifies harmful intent early but overrides its own judgment during subsequent reasoning (accounting for up to 93.7% of unsafe outputs, dominated by a 'Warning' failure pattern where the model wrongly assumes appending a disclaimer suffices) -- and Chain-of-Guardrail (CoG) fixes this with targeted, step-level reasoning-chain rewrites rather than global safety constraints, achieving safety comparable to the strongest baseline while actually *improving* reasoning accuracy (Qwen3-32B: GPQA-Diamond 54.30->62.38, AIME2024 71.70->82.08) where competing safety methods cost 10+ accuracy points.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
