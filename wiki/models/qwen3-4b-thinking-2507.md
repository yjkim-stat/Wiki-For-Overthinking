# Qwen3-4B-Thinking-2507

<!-- auto:begin -->

Qwen3-4B-Thinking-2507 is a Qwen3 'thinking' variant used as a backbone for cognitive profiling of reasoning traces via Bloom's taxonomy, for GRIP's reward-guided parameter interpolation (cutting its average generation length 27.0% while slightly improving accuracy), and for LEASH's constrained-RL length control (up to 26.2% length reduction at this scale while maintaining or improving accuracy on in- and out-of-domain benchmarks).

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 5

**Related**: [AdvBench](../datasets/advbench.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [DeepScaleR-preview (training)](../datasets/deepscaler-preview-training.md), [DeepSeek-R1](deepseek-r1.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [GPQA](../datasets/gpqa.md), [GPQA-D](../datasets/gpqa-d.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [HMMT25](../datasets/hmmt25.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-8B](llama-3-1-8b.md), [Llama-3.3-70B-Instruct](llama-3-3-70b-instruct.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [MMLU-Pro](../datasets/mmlu-pro.md), [Overthinking](../concepts/overthinking.md), [Phi-4-Reasoning](../methods/phi-4-reasoning.md), [Qwen3-30B-A3B](qwen3-30b-a3b.md), [Qwen3-4B](qwen3-4b.md), [Qwen3-4B-Base](qwen3-4b-base.md), [Qwen3-4B-Instruct-2507](qwen3-4b-instruct-2507.md), [QwQ-32B](qwq-32b.md), [Reasoning Step Segmentation](../methods/reasoning-step-segmentation.md), [XSTest](../datasets/xstest.md)

## Appears in

- [Cognitive Profiling of LRMs' Reasoning Traces Using Bloom's Taxonomy](../../archive/papers/2026/arxiv-2608-23205/summary.md) — The paper segments LRM reasoning traces into cognitive steps with Llama-3.3-70B-Instruct, labels each step with one of Bloom's six levels, and uses the resulting level proportions and 6x6 transition matrix to profile seven reasoning models and to predict solution correctness.
- [GRIP: Granular Reward-Guided Parameter Interpolation for Efficient Reasoning](../../archive/papers/2026/arxiv-2608-25583/summary.md) — GRIP fuses a reasoning model and an instruction (non-thinking) model of identical architecture by learning a separate sigmoid-controlled interpolation ratio per module (attention, FFN, embedding/LM-head), trained with an RL reward that favors correct and concise responses while keeping both source models frozen, cutting Qwen3-4B-Thinking's average generation length 27.0% while slightly improving average accuracy.
- [LEASH: Adaptive Length Penalty and Reward Shaping for Efficient Large Reasoning Model](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-129/summary.md) — LEASH formulates reasoning-length control as a constrained RL optimization (maximize task reward subject to an expected-length constraint) solved via a Lagrangian primal-dual method with a one-sided length penalty, letting the penalty coefficient lambda self-tighten or self-relax based on real-time constraint violation rather than requiring manual tuning, and reduces average reasoning length by up to 62.7% (1.5B model) or 26.2% (4B model) while maintaining or improving accuracy on in-domain math and out-of-domain (GPQA, MMLU-Pro) benchmarks, outperforming fixed-penalty and prior length-control baselines.
- [ReasoningGuard: Safeguarding Large Reasoning Models with Inference-time Safety Aha Moments](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1453/summary.md) — ReasoningGuard is a training-free, inference-time jailbreak defense for large reasoning models that uses an attention-sink signal to locate the moment reasoning shifts from problem restatement to exploration, injects a crafted 'safety aha' phrase there, then samples multiple continuations and selects the one with the highest sustained attention to that safety phrase -- outperforming nine existing defenses at only 5-9% extra inference cost.
- [Revisiting Model Interpolation for Efficient Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-389/summary.md) — Reveals that linear interpolation between an Instruct model's and a Thinking model's weights does not trade off performance and reasoning verbosity smoothly, but follows a predictable three-stage transition (Instruct-dominated -> abrupt thinking-pattern emergence -> converging to Thinking with diminishing/overthinking returns), and shows a strategically chosen interpolation point beats sophisticated model-merging baselines (task arithmetic, TIES) on both efficiency and accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
