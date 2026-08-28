# CommonsenseQA

<!-- auto:begin -->

A multiple-choice commonsense question-answering set, used across the archive as the easy, non-mathematical end of the benchmark suite - the place where adaptive-length methods show their largest token savings and where math-trained models are checked for out-of-domain transfer. ARM uses it both as RL training data (with GSM8K and MATH, 19.8K items combined) and as the benchmark where format selection saves about 73% of tokens, against a +7.9% accuracy gain on AIME'25 - the pair the paper reads as evidence the model is judging difficulty roughly correctly. SuCo uses it as one of three out-of-domain checks for a math-trained model, scoring 49.3 against R1-Distill's 45.0, while WS-GRPO finds commonsense sets degrade less than mathematical ones under trajectory-level preference training and that behaviour on this set varies across Qwen variants; DC-CoT includes it among the reasoning domains over which it isolates distillation data effects. No source treats it as a target in its own right.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 5

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [Ada-GRPO](../methods/ada-grpo.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [ARC-Challenge](arc-challenge.md), [BBH](bbh.md), [Chain-of-Thought Distillation](../methods/chain-of-thought-distillation.md), [DeepSeek-R1](../models/deepseek-r1.md), [Dr. GRPO](../methods/dr-grpo.md), [Gemini-2.0-Flash](../models/gemini-2-0-flash.md), [GPQA](gpqa.md), [GPQA-Diamond](gpqa-diamond.md), [GPT-4o](../models/gpt-4o.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [Length Penalty](../concepts/length-penalty.md), [LiveCodeBench-v6](livecodebench-v6.md), [LLaMA-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [Llama-3.3-70B-Instruct](../models/llama-3-3-70b-instruct.md), [MATH](math.md), [MATH500](math500.md), [MBPP](mbpp.md), [MMLU-STEM](mmlu-stem.md), [o1-mini](../models/o1-mini.md), [OK-VQA](ok-vqa.md), [OpenBookQA](openbookqa.md), [OpenCodeReasoning](opencodereasoning.md), [Out-of-Distribution Generalization](../concepts/out-of-distribution-generalization.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-72B-Instruct](../models/qwen2-5-72b-instruct.md), [s1K-1.1](s1k-1-1.md), [StrategyQA](strategyqa.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md), [SVAMP](svamp.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [Token Budget](../concepts/token-budget.md), [underthinking](../concepts/underthinking.md)

## Appears in

- [ReTraceQA: Evaluating Reasoning Traces of Small Language Models in Commonsense Question Answering](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1798/summary.md) — ReTraceQA is a 2,421-instance expert-annotated benchmark showing that small language models (SLMs) reach the correct final answer via a flawed reasoning trace 14-24% of the time on commonsense QA, and that LLM-as-judge and PRM evaluators reliably detect overall trace correctness but struggle to localize the specific erroneous step, inflating answer-only accuracy scores by up to 25%.
- [ARM: Adaptive Reasoning Model](../../archive/papers/2025/title-21d562149c3adad6/summary.md) — ARM trains a model to pick among four reasoning formats (Direct Answer, Short CoT, Code, Long CoT) per task using Ada-GRPO, cutting average tokens by about 30% at roughly unchanged accuracy.
- [WS-GRPO: Weakly-Supervised Group-Relative Policy Optimization for Rollout-Efficient Reasoning](../../archive/papers/2026/title-39bbcb4cded34ec7/summary.md) — WS-GRPO trains a preference model from outcome-only correctness labels to score partial reasoning trajectories, turning terminal reward into prefix-level signal about whether continuing is worthwhile, and reports far shorter reasoning at some accuracy cost.
- [The Quest for Efficient Reasoning: A Data-Centric Benchmark to CoT Distillation](../../archive/papers/2026/title-95b92d67054ad4f2/summary.md) — DC-CoT is a benchmark that isolates the effect of data augmentation, data selection and data mixing on chain-of-thought distillation into smaller student models, across teacher models, student models and reasoning domains.
- [SuCo: Sufficiency-guided Continuous Adaptive Reasoning](../../archive/papers/2026/title-b37859867120f044/summary.md) — Defines the Minimal Sufficient CoT — the shortest reasoning prefix at which the model's confidence in the ground-truth answer crosses a difficulty-adaptive threshold — and trains on it via supervised fine-tuning plus a GRPO stage whose reward penalises both over- and under-thinking, so reasoning length is calibrated continuously rather than by discrete modes.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
