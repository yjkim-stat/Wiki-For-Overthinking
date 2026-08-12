# GPT-4o

<!-- auto:begin -->

An OpenAI multimodal model used across the archive as a reference point rather than a research subject, and notable for what it is compared against. On multimodal mathematical error detection it is the best-performing model tested and still sits about 10% behind educational expert evaluators. On groundedness classification it is beaten by a 4B guardrail model at 77.1% against 75.9% balanced accuracy. It also appears in a systematic evaluation of LLM judges. The pattern across the three is that a general frontier model is a weak specialist: smaller purpose-trained models overtake it at verification, and human experts remain ahead at error detection.

- **Kind**: model
- **Also called**: GPT4o, gpt-4o
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 5

**Related**: [best-of-n](../methods/best-of-n.md), [construct validity](../concepts/construct-validity.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [error detection](../concepts/error-detection.md), [Gemini-2.5-Flash](gemini-2-5-flash.md), [GPQA](../datasets/gpqa.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [hallucination](../concepts/hallucination.md), [linear probe](../methods/linear-probe.md), [Llama-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [majority voting](../methods/majority-voting.md), [MATH](../datasets/math.md), [MATH-500](../datasets/math-500.md), [meta-evaluation](../concepts/meta-evaluation.md), [MMLU-Pro](../datasets/mmlu-pro.md), [MT-Bench](../datasets/mt-bench.md), [multimodal reasoning](../concepts/multimodal-reasoning.md), [pass-k](../methods/pass-k.md), [process evaluation](../methods/process-evaluation.md), [Qwen2.5](qwen2-5.md), [Qwen2.5-0.5B](qwen2-5-0-5b.md), [Qwen2.5-1.5B](qwen2-5-1-5b.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [Qwen3-4B-Thinking-2507](qwen3-4b-thinking-2507.md), [Qwen3-8B](qwen3-8b.md), [QwQ-32B](qwq-32b.md), [reasoning distillation](../methods/reasoning-distillation.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [reward hacking](../concepts/reward-hacking.md), [self-consistency](../methods/self-consistency.md), [synthetic data generation](../methods/synthetic-data-generation.md), [test-time compute](../concepts/test-time-compute.md), [test-time scaling](../methods/test-time-scaling.md), [verification](../concepts/verification.md)

## Appears in

- [ErrorRadar: Benchmarking Complex Mathematical Reasoning of Multimodal Large Language Models Via Error Detection](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1217/summary.md) — Benchmarks multimodal models on detecting and categorizing errors in K-12 math solutions collected from real student interactions, with the best model about 10% behind human experts.
- [HalluGuard: Evidence-Grounded Small Reasoning Models to Mitigate Hallucinations in Retrieval-Augmented Generation](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-835/summary.md) — A 4B small reasoning model that classifies document-claim pairs as grounded or hallucinated for RAG pipelines and produces evidence-grounded justifications.
- [Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias](../../archive/papers/2026/local-504cc53656b06ab4/summary.md) — Evaluates 21 LLM judges across three benchmarks and three protocols over ~541,000 judgments, and shows the field's standard validation metric — exact-match agreement — overstates chance-corrected discrimination by 34-41 points universally, while high test-retest reliability can coexist with severe position bias.
- [Beyond Scalars: Evaluating and Understanding LLM Reasoning via Geometric Progress and Stability](../../archive/papers/2026/local-85a70e78b4a93190/summary.md) — TRACED scores a reasoning chain by the geometry of its hidden-state trajectory -- net displacement as progress and curvature as stability -- and uses the two as features for a Gaussian classifier that separates correct from incorrect chains without reading the text.
- [Provable Scaling Laws for the Test-Time Compute of Large Language Models](../../archive/papers/2025/local-e5ae26db2daac1d7/summary.md) — Gives two aggregation algorithms whose failure probability provably decays to zero as inference compute grows, assuming only that the model can sometimes be right and can compare two solutions better than chance.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
