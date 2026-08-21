# Minerva

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: dataset
- **Also called**: Minerva Math
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 9

**Related**: [Accuracy-Efficiency Pareto Frontier](../concepts/accuracy-efficiency-pareto-frontier.md), [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [Ada-R1](../methods/ada-r1.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [AIME](aime.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [DAPO](../methods/dapo.md), [DeepScaleR](deepscaler.md), [DeepSeek-R1-Distill-Qwen-1.5B](../methods/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../methods/deepseek-r1-distill-qwen-7b.md), [DEER](../methods/deer.md), [DPO_Shortest](../methods/dpo-shortest.md), [DRP](../methods/drp.md), [Efficient Reasoning](../concepts/efficient-reasoning.md), [GPQA](gpqa.md), [GPQA-Diamond](gpqa-diamond.md), [GPT-OSS-20B](../methods/gpt-oss-20b.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [Hidden-State Probing](../concepts/hidden-state-probing.md), [LiveCodeBench](livecodebench.md), [MATH](math.md), [MATH500](math500.md), [MMLU](mmlu.md), [MMLU-Pro](mmlu-pro.md), [Model Merging](../methods/model-merging.md), [O1-Pruner](../methods/o1-pruner.md), [OlympiadBench](olympiadbench.md), [Omni-MATH](omni-math.md), [Overthinking](../concepts/overthinking.md), [Phi-4-reasoning](../methods/phi-4-reasoning.md), [Reward Hacking](../concepts/reward-hacking.md), [Reward Shaping](../concepts/reward-shaping.md), [RLVR](../methods/rlvr.md), [SelfBudgeter](../methods/selfbudgeter.md), [SFT_Shortest](../methods/sft-shortest.md), [Still](still.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md), [Test-Time Compute](../concepts/test-time-compute.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [Test-time scaling](../concepts/test-time-scaling.md), [Thinkless](../methods/thinkless.md), [ThinkPrune](../methods/thinkprune.md), [Token Budget](../concepts/token-budget.md), [TokenSkip](../methods/tokenskip.md), [vLLM](../methods/vllm.md)

## Appears in

- [Segment-Level Attribution for Selective Learning of Long Reasoning Traces](../../archive/papers/2026/arxiv-2602-00425/summary.md) — Uses integrated-gradient token attribution, aggregated into per-segment strength and direction-consistency scores, to pick which segments of a long chain-of-thought an SFT run should compute loss on, masking the rest.
- [Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL](../../archive/papers/2025/title-0bc5d9b198744bed/summary.md) — AutoThink uses a three-stage RL curriculum with stage-wise reward shaping to teach R1-style distilled models to decide per problem whether to emit an explicit reasoning chain at all.
- [DiffAdapt: Difficulty-Adaptive Reasoning for Token-Efficient LLM Inference](../../archive/papers/2026/title-18b94d8204ec3367/summary.md) — DiffAdapt trains a small probe on a reasoning model's hidden state to classify each question as Easy/Normal/Hard and picks a matching prompt, temperature and token limit, cutting token use without retraining the model.
- [How Far Are We from Optimal Reasoning Efficiency?](../../archive/papers/2025/title-279ee92c27a8bb8d/summary.md) — Defines an empirical accuracy-vs-token-budget frontier for a fixed base reasoning model, measures how far existing efficiency methods fall short of it with a single metric (REG), and proposes REO-RL, an RL objective that targets a handful of token budgets to close most of that gap.
- [QuRL: Low-Precision Reinforcement Learning for Efficient Reasoning](../../archive/papers/2026/title-9b034ca49bd46f6f/summary.md) — QuRL runs the rollout phase of RL-with-verifiable-rewards training with an INT8 or FP8 quantized copy of the actor, adding an adaptive clipping range and an invariant weight-scaling trick to keep the low-precision policy from collapsing, for 20-80% faster rollout.
- [Ada-R1: Hybrid-CoT via Bi-Level Adaptive Reasoning Optimization](../../archive/papers/2025/title-a6dab00057eab5aa/summary.md) — Ada-R1 merges a long-CoT and a short-CoT model into one hybrid, then applies two levels of preference training so the model first picks a reasoning style per problem and then prefers the shorter correct trace within that style, cutting average reasoning length by about 51% on five maths datasets.
- [ThreadWeaver: Adaptive Threading for Efficient Parallel Reasoning in Language Models](../../archive/papers/2026/title-c65838fd39e8d183/summary.md) — Trains Qwen3-8B to split its chain of thought into concurrently decoded threads that spawn and join, so the critical path is shorter than a sequential trace of the same total length, using a trie-based rollout that runs on stock autoregressive inference engines.
- [FROST: Filtering Reasoning Outliers with Attention for Efficient Reasoning](../../archive/papers/2026/title-e2cdfd631cb4eda0/summary.md) — FROST uses attention weights to identify and prune sentence-level 'reasoning outliers' from a reasoning model's chain of thought, reporting an average 69.68% token reduction and 26.70% accuracy gain over the base model on four maths benchmarks.
- [QFFT, Question-Free Fine-Tuning for Adaptive Reasoning](../../archive/papers/2025/title-ff37e37c3f1ab9b2/summary.md) — QFFT fine-tunes a short-CoT instruct model on Long CoT responses with the question deleted from every training example, so the model keeps its default concise reasoning and switches to reflective Long CoT only when it hits uncertainty or an error, cutting average tokens by roughly 50% at accuracy comparable to ordinary SFT.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
