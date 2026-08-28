# Qwen2.5-Math-7B-Instruct

<!-- auto:begin -->

Qwen2.5-Math-7B-Instruct is a math-specialized instruction-tuned model used in this archive to test cross-lingual generalizability of test-time scaling (under a FLOPs-matched budget across Outcome Reward Modeling, Process Reward Modeling and Budget Forcing on a 55-language competition-math benchmark, where reward-guided scaling matches or beats reasoning-length scaling once FLOPs are equalized) and as a subject model in ThinkBooster's unified test-time-scaling benchmarking framework.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [best-of-N](../methods/best-of-n.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-4o-mini](gpt-4o-mini.md), [gpt-oss-120b](gpt-oss-120b.md), [HumanEval](../datasets/humaneval.md), [majority voting / self-consistency](../methods/majority-voting-self-consistency.md), [MATH500](../datasets/math500.md), [MBPP](../datasets/mbpp.md), [o3-mini](o3-mini.md), [OlympiadBench](../datasets/olympiadbench.md), [Phi-decoding](../methods/phi-decoding.md), [Qwen2.5-Math-1.5B-Instruct](qwen2-5-math-1-5b-instruct.md), [Qwen3-8B](qwen3-8b.md)

## Appears in

- [Linguistic Generalizability of Test-Time Scaling in Mathematical Reasoning](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-699/summary.md) — Under a FLOPs-matched budget across three test-time scaling methods (Outcome Reward Modeling, Process Reward Modeling, Budget Forcing) on a new 55-language competition-math benchmark (MCLM), all three methods yield large gains in English (e.g. Budget Forcing +20 points on AIME) but only ~1.9-2 points average gain across other languages, and reward-model-guided scaling (ORM) matches or beats reasoning-trace-length scaling (Budget Forcing) once FLOPs are equalized -- with more test-time compute also increasing cross-lingual performance variance rather than reducing it.
- [ThinkBooster: A Unified Framework for Seamless Test-Time Scaling of LLM Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-demo-70/summary.md) — ThinkBooster is a unified, open-source framework (Python library + OpenAI-compatible proxy endpoint + visual debugger) implementing 9 test-time-compute scaling strategies and 4 scorer families under a joint TFLOPs-and-tokens compute-accounting benchmark, whose pilot study finds PRM scorers dominate on math while lightweight uncertainty scorers are surprisingly competitive on (out-of-domain-for-PRM) coding tasks, and that beam search often underperforms best-of-N and even self-consistency despite costing more compute.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
