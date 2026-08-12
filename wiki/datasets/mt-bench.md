# MT-Bench

<!-- auto:begin -->

A pairwise judge-evaluation benchmark of 2,391 comparisons with expert human judgments, and the most widely used basis for validating LLM judges. Two archived sources make it the cautionary case. Its balanced A/B/Tie label structure raises chance agreement, producing the largest kappa deflation of any benchmark measured — a cohort mean of 38.6 percentage points, so '85% agreement' corresponds to kappa around 0.48. It also compresses 21 judges into a 13.5-point kappa band where JudgeBench spreads the same models over 60.4, so small differences produce large rank changes. And judge preference measured on it is reported not to correlate with concrete measures of safety, world knowledge or instruction following.

- **Kind**: dataset
- **Also called**: MT-Bench
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md)
- **Sources**: 2

**Related**: [alignment](../concepts/alignment.md), [AlpacaEval](alpacaeval.md), [construct validity](../concepts/construct-validity.md), [Gemini-2.5-Flash](../models/gemini-2-5-flash.md), [GPT-4o](../models/gpt-4o.md), [instruction following](../concepts/instruction-following.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [meta-evaluation](../concepts/meta-evaluation.md), [MMLU](mmlu.md), [preference optimization](../methods/preference-optimization.md), [Qwen3-8B](../models/qwen3-8b.md), [supervised finetuning](../methods/supervised-finetuning.md)

## Appears in

- [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](../../archive/papers/2025/local-503d1e9598036375/summary.md) — Builds a large standardized meta-benchmark and finds that LLM-judge preference scores do not correlate with concrete measures of safety, world knowledge or instruction following, because judges systematically prioritize style over factuality and safety.
- [Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias](../../archive/papers/2026/local-504cc53656b06ab4/summary.md) — Evaluates 21 LLM judges across three benchmarks and three protocols over ~541,000 judgments, and shows the field's standard validation metric — exact-match agreement — overstates chance-corrected discrimination by 34-41 points universally, while high test-retest reliability can coexist with severe position bias.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
