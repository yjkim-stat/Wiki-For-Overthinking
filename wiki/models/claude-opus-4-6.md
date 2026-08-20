# Claude Opus 4.6

<!-- auto:begin -->

A Claude model appearing twice in this archive as an evaluated system rather than a subject. In the financial-advice work it is the strongest commercial baseline on both instruments: second on the LLM-judge rubric at 9.365 behind a fine-tuned open-weight model, and the only commercial system whose estimated gross-profit lift under a judge-independent causal audit is both positive and comfortably distinguishable from zero (0.0104, p < 0.001) -- a distinction that matters because a sibling model scores well on the rubric while its estimated lift is negative. It is separately one of 21 judges in the large-scale LLM-as-a-judge reliability evaluation, whose findings about kappa deflation and position bias are reported over the panel rather than per model. Neither source describes the model itself; its usefulness here is that it is the commercial system that holds up under both a rubric and an outcome-grounded audit.

- **Kind**: model
- **Also called**: Claude Opus 4.6
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [Claude Sonnet 4.5](claude-sonnet-4-5.md), [Claude Sonnet 4.6](claude-sonnet-4-6.md), [Cohen's kappa](../methods/cohen-s-kappa.md), [construct validity](../concepts/construct-validity.md), [DeepSeek-V3.2](deepseek-v3-2.md), [Gemini-2.5-Flash](gemini-2-5-flash.md), [Gemini-3.1-Pro](gemini-3-1-pro.md), [GPT-4o](gpt-4o.md), [GPT-5.4](gpt-5-4.md), [GRPO](../methods/grpo.md), [Kimi-K2.5](kimi-k2-5.md), [KL regularization](../methods/kl-regularization.md), [Llama-3.3-70B](llama-3-3-70b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [meta-evaluation](../concepts/meta-evaluation.md), [MT-Bench](../datasets/mt-bench.md), [outcome reward](../concepts/outcome-reward.md), [position bias](../concepts/position-bias.md), [Qwen3.5-27B](qwen3-5-27b.md), [Qwen3-8B](qwen3-8b.md), [reward hacking](../concepts/reward-hacking.md), [reward shaping](../concepts/reward-shaping.md)

## Appears in

- [GRPO for Financial Advice Generation: Outperforming Commercial LLMs under CATE Evaluation](../../archive/papers/2026/arxiv-2608-11787/summary.md) — Trains an open-weight model with GRPO against a safety-gated LLM-as-a-judge rubric for financial advice, then audits the result with a judge-independent causal estimator on logged outcomes -- and finds the two evaluations rank the other systems differently, with the untrained base model last on the rubric and second on the audit.
- [Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias](../../archive/papers/2026/local-504cc53656b06ab4/summary.md) — Evaluates 21 LLM judges across three benchmarks and three protocols over ~541,000 judgments, and shows the field's standard validation metric — exact-match agreement — overstates chance-corrected discrimination by 34-41 points universally, while high test-retest reliability can coexist with severe position bias.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
