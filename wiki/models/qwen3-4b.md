# Qwen3-4B

<!-- auto:begin -->

Qwen3-4B is a backbone tested by MUR's momentum-uncertainty-guided reasoning (cutting thinking-token budgets over 45% while improving accuracy) and used as one of the 20 models in a large-scale statistical study of how to reliably rank reasoning LLMs under test-time scaling.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [CoT-Valve (baseline)](../methods/cot-valve-baseline.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [DPO (baseline)](../methods/dpo-baseline.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [HMMT25](../datasets/hmmt25.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-8B](llama-3-1-8b.md), [LoRA](../methods/lora.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [Phi-4](phi-4.md), [Phi-decoding](../methods/phi-decoding.md), [Qwen3-1.7B](qwen3-1-7b.md), [Qwen3-30B-A3B](qwen3-30b-a3b.md), [Qwen3-4B-Base](qwen3-4b-base.md), [Qwen3-4B-Instruct-2507](qwen3-4b-instruct-2507.md), [Qwen3-4B-Thinking-2507](qwen3-4b-thinking-2507.md), [Qwen3-8B](qwen3-8b.md), [TLMRE (baseline)](../methods/tlmre-baseline.md)

## Appears in

- [MUR: Momentum Uncertainty guided Reasoning for Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1058/summary.md) — MUR (Momentum Uncertainty guided Reasoning) is a training-free, orthogonal-to-existing-TTS method that recursively aggregates step-level uncertainty into a momentum term (proven to act as a low-pass filter emphasizing recent steps) and selectively applies test-time-scaling compute only to steps whose uncertainty exceeds this momentum by a tunable threshold, cutting thinking-token budgets by over 45% on average while improving accuracy 0.33-3.46% across four benchmarks, three Qwen3 model sizes, and four test-time-scaling backends.
- [Ranking Reasoning LLMs under Test-Time Scaling](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1544/summary.md) — Formalizes ranking reasoning LLMs under test-time scaling as inference over a dense response tensor of repeated stochastic trials, compares 72 ranking methods (paired-comparison, IRT, voting, graph/spectral) across 20 models and four Olympiad math benchmarks, and finds Bayes_R0@N (Bayesian mean with an empirical greedy-decoding prior) is the most stable low-budget ranking method -- though its greedy prior can introduce systematic bias when greedy and stochastic sampling disagree.
- [AdaMix: Adaptive Mixing for Short and Long Reasoning Adapters](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1864/summary.md) — AdaMix decouples efficiency and accuracy into two separately-trained LoRA adapters (a short adapter and a long adapter), then uses a BERT-based difficulty-aware router to predict a per-problem complexity coefficient that linearly interpolates the two adapters via task arithmetic, cutting DeepSeek-R1-Distill-Qwen-7B's average response length 54.9% while improving accuracy up to 4.8% across five math benchmarks and outperforming ShorterBetter/TLMRE/CoT-Valve/model-merging/SwitchCoT baselines on an accuracy-efficiency score.
- [Revisiting Model Interpolation for Efficient Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-389/summary.md) — Reveals that linear interpolation between an Instruct model's and a Thinking model's weights does not trade off performance and reasoning verbosity smoothly, but follows a predictable three-stage transition (Instruct-dominated -> abrupt thinking-pattern emergence -> converging to Thinking with diminishing/overthinking returns), and shows a strategically chosen interpolation point beats sophisticated model-merging baselines (task arithmetic, TIES) on both efficiency and accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
