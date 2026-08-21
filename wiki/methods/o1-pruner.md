# O1-Pruner

<!-- auto:begin -->

O1-Pruner is a chain-of-thought length-reduction method that the archive knows almost entirely as a baseline: only one of the four citing papers says anything about how it works. EvoThink classes it with Kimi 1.5, ThinkPrune, DAST and DIET as 'trajectory compression' -- a length penalty applied to the output as a whole -- and argues that this granularity shortens beneficial and redundant verification indiscriminately, which is the axis along which EvoThink positions itself against it. The other three name it without mechanism: ARLCP lists it among its baselines on DeepSeek-R1-Distill-Qwen-1.5B and -7B, ShorterBetter compares against it, and QFFT reports it cutting tokens further than QFFT (0.8K on GSM8K at 7B) while scoring AES -1.7 against QFFT's 2.3 -- a metric whose parameters penalise accuracy loss ten times more than they reward token savings. Beyond the length-penalty characterisation, no archived paper describes its training procedure, and no archived source states its own headline numbers.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [Accuracy-Length Tradeoff](../concepts/accuracy-length-tradeoff.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [AdaptThink](adaptthink.md), [Aha Moment](../concepts/aha-moment.md), [AIME](../datasets/aime.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [BBH](../datasets/bbh.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [DeepSeek-R1-Distill-Qwen-1.5B](deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [DPO_Shortest](dpo-shortest.md), [GPQA](../datasets/gpqa.md), [GSM8K](../datasets/gsm8k.md), [HumanEval](../datasets/humaneval.md), [Laser](laser.md), [Length Penalty](../concepts/length-penalty.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MathQA](../datasets/mathqa.md), [MBPP](../datasets/mbpp.md), [Minerva](../datasets/minerva.md), [MMLU](../datasets/mmlu.md), [MMLU-Pro](../datasets/mmlu-pro.md), [NoThinking](nothinking.md), [Omni-MATH](../datasets/omni-math.md), [Overthinking](../concepts/overthinking.md), [Preference Optimization](preference-optimization.md), [Qwen2.5-Instruct](qwen2-5-instruct.md), [Redundant Self-Verification](../concepts/redundant-self-verification.md), [RLVR](rlvr.md), [SFT_Shortest](sft-shortest.md), [Still](../datasets/still.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [Test-time scaling](../concepts/test-time-scaling.md), [ThinkPrune](thinkprune.md), [veRL](verl.md)

## Appears in

- [EvoThink: Evolving Thinking in Large Reasoning Models via Self-Pruning and Aha-Moment Preference Optimization](../../archive/papers/2026/arxiv-2607-19962/summary.md) — EvoThink cuts overthinking in two separable stages: Self-Pruning Training deletes reasoning steps whose local conclusion repeats the previous step's and self-trains on the shortened traces, while Aha-Moment Preference Optimization builds from-wrong-to-right preference pairs out of the model's most diverse failed attempts and applies DPO to them.
- [Stop Unnecessary Reflection: Training LRMs for Efficient Reasoning with Adaptive Reflection and Length Coordinated Penalty](../../archive/papers/2026/title-833de99e9b3ea69d/summary.md) — ARLCP is a reinforcement-learning fine-tuning recipe that adds two coupled reward penalties -- one on reflective steps, one on response length scaled by estimated problem complexity -- to shorten chains of thought in distilled reasoning models without losing accuracy.
- [ShorterBetter: Guiding Reasoning Models to Find Optimal Inference Length for Efficient Reasoning](../../archive/papers/2025/title-d40396527f776f1d/summary.md) — ShorterBetter takes the length of the shortest correct response in a sampled group as a per-problem target and rewards the model for matching it, cutting output length by 50%-80% on DeepSeek-Distill-Qwen-1.5B/7B.
- [QFFT, Question-Free Fine-Tuning for Adaptive Reasoning](../../archive/papers/2025/title-ff37e37c3f1ab9b2/summary.md) — QFFT fine-tunes a short-CoT instruct model on Long CoT responses with the question deleted from every training example, so the model keeps its default concise reasoning and switches to reflective Long CoT only when it hits uncertainty or an error, cutting average tokens by roughly 50% at accuracy comparable to ordinary SFT.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
