# QwQ-32B-Preview

<!-- auto:begin -->

QwQ-32B-Preview is an early reasoning-model release used in Step-Saliency (pooling token-level attention-gradient saliency into step-to-step maps revealing depth-wise reasoning patterns), a study of evaluation-time compute scaling for LLM-as-judge, and O1-Pruner (which identifies 'length disharmony' and applies its Length-Harmonizing Fine-Tuning to QwQ-32B-Preview as one of its two fine-tuned models).

- **Kind**: model
- **Also called**: QwQ-32B-Preview
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [Accuracy-Efficiency Score (AES)](../concepts/accuracy-efficiency-score-aes.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Best-of-N reranking](../methods/best-of-n-reranking.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-14B](deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [difficulty estimation](../concepts/difficulty-estimation.md), [DPO (baseline)](../methods/dpo-baseline.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-4o](gpt-4o.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [LLaMA-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [Llama-3.2-1B-Instruct](llama-3-2-1b-instruct.md), [LLaMA 3.2 3B Instruct](llama-3-2-3b-instruct.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [QwQ-32B](qwq-32b.md), [SFT (baseline)](../methods/sft-baseline.md), [ZebraLogic](../datasets/zebralogic.md)

## Appears in

- [Reasoning Fails Where Step Flow Breaks](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1212/summary.md) — Step-Saliency pools token-level attention-gradient saliency into step-to-step maps across a reasoning trace's question/thinking/summary structure, revealing two depth-wise information-flow failures in incorrect outputs -- Shallow Lock-in (shallow layers over-focus on the current step, ignoring earlier context) and Deep Decay (deep layers lose connection to the thinking segment, with the summary attending mainly to itself) -- and fixes both with StepFlow, a training-free single-pass decoding intervention that improves accuracy by up to 11.8 points across six LRM backbones and six benchmarks.
- [Scaling Evaluation-Time Compute with Reasoning Models as Evaluators](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2102/summary.md) — Shows evaluation itself scales like generation: off-the-shelf reasoning models, simply prompted to generate a chain-of-thought judgment (no evaluator-specific training), improve monotonically with more reasoning tokens and, when made to individually assess every reasoning step rather than a single-pass judgment, a 32B reasoning evaluator beats a specialized 72B PRM by 4.5 F1 points on ProcessBench; folding this into Best-of-N reranking, spending the fixed test-time budget on evaluation-time reasoning (Best-of-8 with a reasoning evaluator) beats spending it on more candidate samples (Best-of-64 with a direct evaluator) by 4.30-6.63 points, and reasoning evaluators are shown to resist reward-model over-optimization that both direct evaluator types suffer from.
- [O1-Pruner: Length-Harmonizing Fine-Tuning for O1-Like Reasoning Pruning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-697/summary.md) — O1-Pruner identifies 'length disharmony' -- shorter responses often achieve equal or higher accuracy than longer ones, at both the instance and distribution level -- and fine-tunes long-thought models with a PPO-style Length-Harmonizing Reward that rewards brevity relative to a reference model's own pre-sampled length/accuracy baseline, subject to an accuracy non-degradation constraint, cutting solution length by 34.7-40.5% while improving accuracy.
- [THOUGHTTERMINATOR: Benchmarking, Calibrating, and Mitigating Overthinking in Reasoning Models](../../archive/papers/2025/local-eff598a06b1089db/summary.md) — The paper defines model-relative measures of overthinking (local/global overthinking scores) built from observed token-spend distributions, introduces the DUMB500 easy-question dataset to probe overthinking on trivial inputs, and proposes THOUGHTTERMINATOR, a training-free decoding-time technique that interrupts a reasoning model with token-budget reminders and forces an answer at a difficulty-calibrated deadline.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
