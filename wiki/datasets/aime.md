# AIME

<!-- auto:begin -->

The American Invitational Mathematics Examination, used throughout the archive's sources (unspecified year in this entry) as a standard hard competition-math benchmark. Under this exact spelling, the 5 sources use it to evaluate: self-braking tuning, the foundational overthinking paper, meta-RL test-time-compute optimization, reasoning-step pruning (LIMOPro), and Kinetics' reworked test-time scaling law. Note: the archive's wiki tracks this exam under at least 8 separate near-duplicate entries by exact spelling that were never merged -- this is the same underlying exam split into fragmented wiki notes.

- **Kind**: dataset
- **Also called**: AIME 2024, AIME 2025, AIME'25, AIME2024, AIME2025, AIME24, AIME25
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 8

**Related**: [Accuracy-Efficiency Score (AES)](../concepts/accuracy-efficiency-score-aes.md), [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [adaptive reasoning length](../concepts/adaptive-reasoning-length.md), [AMC](amc.md), [BBH](bbh.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [Chain-of-Thought Distillation](../methods/chain-of-thought-distillation.md), [DeepSeek-R1-Distill-Qwen-1.5B](../methods/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../methods/deepseek-r1-distill-qwen-7b.md), [Efficient Reasoning](../concepts/efficient-reasoning.md), [GPQA](gpqa.md), [GPQA-Diamond](gpqa-diamond.md), [Group-Relative Advantage](../concepts/group-relative-advantage.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [HumanEval](humaneval.md), [KV-cache compression](../methods/kv-cache-compression.md), [KV cache eviction](../methods/kv-cache-eviction.md), [Length reward](../concepts/length-reward.md), [LiveCodeBench](livecodebench.md), [MATH](math.md), [MATH500](math500.md), [MathQA](mathqa.md), [MBPP](mbpp.md), [MMLU](mmlu.md), [O1-Pruner](../methods/o1-pruner.md), [OlympiadBench](olympiadbench.md), [Omni-MATH](omni-math.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-Instruct](../methods/qwen2-5-instruct.md), [R-KV](../methods/r-kv.md), [Redundant Self-Verification](../concepts/redundant-self-verification.md), [RLOO](../methods/rloo.md), [RLVR](../methods/rlvr.md), [Still](still.md)

## Appears in

- [Let LRMs Break Free from Overthinking via Self-Braking Tuning](../../archive/papers/2025/title-2b17dd2ef08b6fa4/summary.md) — Introduces Self-Braking Tuning, which trains a large reasoning model to detect and stop its own redundant reasoning steps, cutting token usage by up to 60% with comparable accuracy on math benchmarks.
- [ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models](../../archive/papers/2026/title-3a1fb8083fa0ff85/summary.md) — A KV-cache compression framework that labels segments of a reasoning trace by thought type and applies per-type quantization and progressive eviction, keeping accuracy near full-cache at under 5% of the cache.
- [DRPO: Efficient Reasoning via Decoupled Reward Policy Optimization](../../archive/papers/2026/title-68327bf6b9e4e869/summary.md) — Diagnoses why adding a length penalty to GRPO degrades accuracy — the group-relative advantage can turn correct-but-long rollouts negative — and fixes it by normalising the reward of correct rollouts only against other correct rollouts.
- [Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models](../../archive/papers/2025/title-7805f8ec24eadc13/summary.md) — The first systematic study of overthinking in o1-like reasoning models, introducing outcome/process efficiency metrics and a self-training method that trims redundant reasoning on easy problems without hurting accuracy.
- [Optimizing Test-Time Compute via Meta Reinforcement Finetuning](../../archive/papers/2025/title-86af300fcc089e57/summary.md) — Casts test-time compute optimization as a meta reinforcement learning problem and fine-tunes reasoning models with an information-gain-based dense reward so each block of reasoning measurably progresses toward the answer.
- [ShorterBetter: Guiding Reasoning Models to Find Optimal Inference Length for Efficient Reasoning](../../archive/papers/2025/title-d40396527f776f1d/summary.md) — ShorterBetter takes the length of the shortest correct response in a sampled group as a per-problem target and rewards the model for matching it, cutting output length by 50%-80% on DeepSeek-Distill-Qwen-1.5B/7B.
- [LIMOPro: Reasoning Refinement for Efficient and Effective Test-time Scaling](../../archive/papers/2025/title-f14f82d5eba9e811/summary.md) — PIR scores reasoning steps by their effect on answer confidence and prunes only low-importance verification/error-correction steps from distilled chain-of-thought data, producing models that reason more concisely without losing accuracy.
- [Kinetics: Rethinking Test-Time Scaling Law](../../archive/papers/2025/title-fe7ecea333b91370/summary.md) — Reworks test-time scaling laws to account for memory-access cost alongside compute, finding a 14B-parameter threshold below which test-time compute is less effective, and shows sparse attention substantially improves accuracy under a fixed test-time budget.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
