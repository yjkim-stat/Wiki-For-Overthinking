# position bias

<!-- auto:begin -->

A systematic preference for an answer or candidate because of where it appears rather than what it says. Its sharpest statement here is a paradox: a judge that deterministically prefers position A scores perfectly on test-retest reliability while being maximally biased, because test-retest measures the stability of outputs rather than the correctness of the decision process -- so the two coexist in the same judge and high reliability is no evidence against it. That comes from an evaluation of 21 judges over about 541,000 judgments, which also finds the field's standard validation metric overstates chance-corrected discrimination by 34 to 41 points universally. The second source shows the same failure inside a benchmark rather than a judge: on a test set deliberately balanced across answer positions, a base model scores 52.4 percent when the correct option is A against 31.6 to 33.6 percent elsewhere. The two together define the precaution -- balance the positions or swap them and re-run -- and the reason it cannot be skipped, which is that no measure of a judge's self-consistency will reveal the problem.

- **Kind**: concept
- **Also called**: order bias
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md)
- **Sources**: 2

**Related**: [benchmark contamination](benchmark-contamination.md), [benchmark design](benchmark-design.md), [calibration](../methods/calibration.md), [chain-of-thought distillation](../methods/chain-of-thought-distillation.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Claude Sonnet 4.6](../models/claude-sonnet-4-6.md), [construct validity](construct-validity.md), [decontamination](../methods/decontamination.md), [DeepSeek-V3.2](../models/deepseek-v3-2.md), [Gemini-2.5-Flash](../models/gemini-2-5-flash.md), [Gemini-3.1-Pro](../models/gemini-3-1-pro.md), [Gemini-3.5-Flash](../models/gemini-3-5-flash.md), [GPT-4o](../models/gpt-4o.md), [GPT-5.5](../models/gpt-5-5.md), [GPT-5.6-Sol](../models/gpt-5-6-sol.md), [Kimi-K2.5](../models/kimi-k2-5.md), [Llama-3.3-70B](../models/llama-3-3-70b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [macro versus micro accuracy](macro-versus-micro-accuracy.md), [meta-evaluation](meta-evaluation.md), [MT-Bench](../datasets/mt-bench.md), [multi-hop reasoning](multi-hop-reasoning.md), [multiple-choice evaluation](../methods/multiple-choice-evaluation.md), [Qwen3.5-9B](../models/qwen3-5-9b.md), [Qwen3.6-27B](../models/qwen3-6-27b.md), [Qwen3-8B](../models/qwen3-8b.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md)

## Appears in

- [SafeSceneReason: A Multimodal Reasoning Benchmark Connecting Industrial Hazards with Accident Knowledge](../../archive/papers/2026/arxiv-2608-09230/summary.md) — Builds an industrial-safety reasoning benchmark from two pipelines -- program execution over safety scene graphs, and evidence graphs extracted from real accident-investigation reports -- and shows that general multimodal capability does not transfer to it while a 9B model fine-tuned on its chain-of-thought split matches frontier systems.
- [Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias](../../archive/papers/2026/local-504cc53656b06ab4/summary.md) — Evaluates 21 LLM judges across three benchmarks and three protocols over ~541,000 judgments, and shows the field's standard validation metric — exact-match agreement — overstates chance-corrected discrimination by 34-41 points universally, while high test-retest reliability can coexist with severe position bias.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
