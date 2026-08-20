# GPT-5.4

<!-- auto:begin -->

A frontier model appearing across 3 sources as a judge and a commercial baseline. Its most useful archived datum is comparative: in a large-scale judge evaluation it is the newest of three from one provider whose progression on one benchmark is legible (0.309, 0.487, 0.606) and nearly invisible on another (0.451, 0.451, 0.457), so its judging quality depends on which benchmark is asked. It also appears as a teacher-quality reference in a controlled supervision study and as a commercial comparator that an open-weight trained model outperforms on financial advice.

- **Kind**: model
- **Also called**: GPT-5.4
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [annotation agreement](../concepts/annotation-agreement.md), [benchmark contamination](../concepts/benchmark-contamination.md), [chain-of-thought distillation](../methods/chain-of-thought-distillation.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Claude Opus 4.6](claude-opus-4-6.md), [Claude Sonnet 4.5](claude-sonnet-4-5.md), [Claude Sonnet 4.6](claude-sonnet-4-6.md), [Cohen's kappa](../methods/cohen-s-kappa.md), [construct validity](../concepts/construct-validity.md), [decontamination](../methods/decontamination.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [DeepSeek-V3.2](deepseek-v3-2.md), [few-shot prompting](../methods/few-shot-prompting.md), [Gemini-2.5-Flash](gemini-2-5-flash.md), [Gemini-3.1-Pro](gemini-3-1-pro.md), [GPT-4.1](gpt-4-1.md), [GPT-4o](gpt-4o.md), [GPT-5](gpt-5.md), [GRPO](../methods/grpo.md), [human evaluation](../methods/human-evaluation.md), [Kimi-K2.5](kimi-k2-5.md), [KL regularization](../methods/kl-regularization.md), [knowledge distillation](../methods/knowledge-distillation.md), [Llama-3.3-70B](llama-3-3-70b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [matched-budget comparison](../methods/matched-budget-comparison.md), [McNemar test](../methods/mcnemar-test.md), [meta-evaluation](../concepts/meta-evaluation.md), [MT-Bench](../datasets/mt-bench.md), [out-of-domain generalization](../concepts/out-of-domain-generalization.md), [outcome reward](../concepts/outcome-reward.md), [paired bootstrap](../methods/paired-bootstrap.md), [position bias](../concepts/position-bias.md), [Qwen2.5-Math-7B-Instruct](qwen2-5-math-7b-instruct.md), [Qwen3.5-27B](qwen3-5-27b.md), [Qwen3-8B](qwen3-8b.md), [reasoning depth](../concepts/reasoning-depth.md), [reward hacking](../concepts/reward-hacking.md), [reward shaping](../methods/reward-shaping.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md)

## Appears in

- [MathShikkha: A Controlled Study of Answer-Only and Chain-of-Thought Supervision for Bangla Mathematical Reasoning in Small Language Models](../../archive/papers/2026/arxiv-2608-08503/summary.md) — Compares chain-of-thought against answer-only supervision under a protocol where the two conditions differ in nothing but the training target, and finds the rationales buy nothing in-domain for strong backbones while buying 20 to 28 points out of domain -- with a human study attributing the measurable effect to language adherence and inspectability rather than to better reasoning.
- [GRPO for Financial Advice Generation: Outperforming Commercial LLMs under CATE Evaluation](../../archive/papers/2026/arxiv-2608-11787/summary.md) — Trains an open-weight model with GRPO against a safety-gated LLM-as-a-judge rubric for financial advice, then audits the result with a judge-independent causal estimator on logged outcomes -- and finds the two evaluations rank the other systems differently, with the untrained base model last on the rubric and second on the audit.
- [Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias](../../archive/papers/2026/local-504cc53656b06ab4/summary.md) — Evaluates 21 LLM judges across three benchmarks and three protocols over ~541,000 judgments, and shows the field's standard validation metric — exact-match agreement — overstates chance-corrected discrimination by 34-41 points universally, while high test-retest reliability can coexist with severe position bias.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
