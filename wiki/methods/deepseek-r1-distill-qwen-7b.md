# DeepSeek-R1-Distill-Qwen-7B

<!-- auto:begin -->

DeepSeek-R1-Distill-Qwen-7B is a language model -- REA-RL calls it a 7B distilled model, and Ada-R1 and ShorterBetter use it as their long-CoT base -- that archived papers evaluate on rather than study; the wiki has no kind for a model, so it is filed under the least wrong of the three available. It is the archive's most common efficient-reasoning testbed: ReCo reports 60.0% six-benchmark accuracy on it against 61.9% for full-cache CoT with 65% fewer tokens; REA-RL starts from it at 80.39% average accuracy over GSM8K, MATH500, Gaokao23, AMC23 and AIME24 and cuts length about 36% at unchanged accuracy, where a plain length-reward GRPO baseline gives up roughly 3.5 points for a comparable saving; Ada-R1 cuts its average reasoning length 50.93% for 1.65 accuracy points; ShorterBetter cuts in-domain length 62.1% with accuracy up 7.1%, e.g. AIME 53.3% against the base model's 36.7% at 5,288 against 11,382 tokens. What these papers establish about the model itself is the overthinking they are correcting: ShorterBetter's trace analysis attributes its excess length to repetition, self-verification and exploration of alternative solution paths after an answer is already reached, and ReCo shows its generations lengthen by 38.8% on MATH-500 when KV cache is compressed to 25%.

- **Kind**: method
- **Also called**: DeepSeek-Distill-Qwen-7B, Distill-7B
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [Ada-R1](ada-r1.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [AIME](../datasets/aime.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [chain-of-thought compression](../concepts/chain-of-thought-compression.md), [confidence-based early stopping](confidence-based-early-stopping.md), [DeepScaleR](../datasets/deepscaler.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](deepseek-r1-distill-qwen-1-5b.md), [distillation](../concepts/distillation.md), [GPQA](../datasets/gpqa.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [HumanEval](../datasets/humaneval.md), [KV cache compression](kv-cache-compression.md), [Length reward](../concepts/length-reward.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH](../datasets/math.md), [MATH-500](../datasets/math-500.md), [MathQA](../datasets/mathqa.md), [MBPP](../datasets/mbpp.md), [Minerva Math](../datasets/minerva-math.md), [MMLU](../datasets/mmlu.md), [Model Merging](model-merging.md), [O1-Pruner](o1-pruner.md), [OlympiadBench](../datasets/olympiadbench.md), [Omni-MATH](../datasets/omni-math.md), [overthinking](../concepts/overthinking.md), [process reward model](../concepts/process-reward-model.md), [Qwen2.5-Instruct](qwen2-5-instruct.md), [Qwen3-8B](qwen3-8b.md), [R-KV](r-kv.md), [Redundant Self-Verification](../concepts/redundant-self-verification.md), [Reinforcement Learning with Verifiable Rewards](reinforcement-learning-with-verifiable-rewards.md), [sequential revision](sequential-revision.md), [Still](../datasets/still.md), [test-time compute scaling](../concepts/test-time-compute-scaling.md)

## Appears in

- [Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning](../../archive/papers/2026/arxiv-2608-04771/summary.md) — ReCo uses a 30M process-reward estimator to set, per reasoning step, both the KV-cache retention ratio and generation-side controls (a reflection-token logit penalty and confidence-based early stopping), cutting generated tokens by 37-65% and end-to-end latency by 2.08-2.35x versus full-cache CoT.
- [REA-RL: Reflection-Aware Online Reinforcement Learning for Efficient Reasoning](../../archive/papers/2026/title-474d6c4d88a30199/summary.md) — REA-RL trains a large reasoning model online with a distilled 7B reflection model that supplies both parallel samples and truncated sequential revisions, plus a reflection-density reward, cutting response length about 36% on math benchmarks without losing accuracy.
- [Ada-R1: Hybrid-CoT via Bi-Level Adaptive Reasoning Optimization](../../archive/papers/2025/title-a6dab00057eab5aa/summary.md) — Ada-R1 merges a long-CoT and a short-CoT model into one hybrid, then applies two levels of preference training so the model first picks a reasoning style per problem and then prefers the shorter correct trace within that style, cutting average reasoning length by about 51% on five maths datasets.
- [ShorterBetter: Guiding Reasoning Models to Find Optimal Inference Length for Efficient Reasoning](../../archive/papers/2025/title-d40396527f776f1d/summary.md) — ShorterBetter takes the length of the shortest correct response in a sampled group as a per-problem target and rewards the model for matching it, cutting output length by 50%-80% on DeepSeek-Distill-Qwen-1.5B/7B.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
