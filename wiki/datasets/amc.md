# AMC

<!-- auto:begin -->

The American Mathematics Competitions, used in this archive as a source of competition problems sitting between GSM8K and AIME in difficulty. Sources cite it in two ways that should not be confused: as a dated sitting used for evaluation, almost always AMC23 with its 40 problems, and as an undated pool that training corpora draw from alongside AIME, Omni-MATH and Still. At 40 problems a sitting it is small enough that a few items move a reported accuracy by percentage points, which several papers here note when comparing close methods.

- **Kind**: dataset
- **Also called**: AMC (2022-2023), AMC23, American Mathematics Competitions
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 5

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [adaptive reasoning length](../concepts/adaptive-reasoning-length.md), [AIME](aime.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [BBH](bbh.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [Chain-of-Thought Distillation](../methods/chain-of-thought-distillation.md), [DeepSeek-R1-Distill-Qwen-1.5B](../methods/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../methods/deepseek-r1-distill-qwen-7b.md), [GPQA-Diamond](gpqa-diamond.md), [GSM8K](gsm8k.md), [HumanEval](humaneval.md), [LiveCodeBench](livecodebench.md), [MATH](math.md), [MATH500](math500.md), [MathQA](mathqa.md), [MBPP](mbpp.md), [MMLU](mmlu.md), [MMLU-STEM](mmlu-stem.md), [O1-Pruner](../methods/o1-pruner.md), [OlympiadBench](olympiadbench.md), [Omni-MATH](omni-math.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-Instruct](../methods/qwen2-5-instruct.md), [Redundant Self-Verification](../concepts/redundant-self-verification.md), [RLVR](../methods/rlvr.md), [Self-Distillation](../concepts/self-distillation.md), [Still](still.md)

## Appears in

- [Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning](../../archive/papers/2026/arxiv-2608-05643/summary.md) — A training-free, verifier-free test-time scaling method that refines each of N sampled reasoning rollouts through D rounds of self-critique and self-correction before majority-voting the answers, instead of only sampling more candidates or relying on an external verifier.
- [ConPress: Learning Efficient Reasoning from Multi-Question Contextual Pressure](../../archive/papers/2026/title-11f96b3e58a44cf5/summary.md) — ConPress observes that a reasoning model shortens its traces when several independent questions share one prompt, and harvests those shortened traces as self-supervised fine-tuning data for the single-question setting.
- [Let LRMs Break Free from Overthinking via Self-Braking Tuning](../../archive/papers/2025/title-2b17dd2ef08b6fa4/summary.md) — Introduces Self-Braking Tuning, which trains a large reasoning model to detect and stop its own redundant reasoning steps, cutting token usage by up to 60% with comparable accuracy on math benchmarks.
- [ShorterBetter: Guiding Reasoning Models to Find Optimal Inference Length for Efficient Reasoning](../../archive/papers/2025/title-d40396527f776f1d/summary.md) — ShorterBetter takes the length of the shortest correct response in a sampled group as a per-problem target and rewards the model for matching it, cutting output length by 50%-80% on DeepSeek-Distill-Qwen-1.5B/7B.
- [LIMOPro: Reasoning Refinement for Efficient and Effective Test-time Scaling](../../archive/papers/2025/title-f14f82d5eba9e811/summary.md) — PIR scores reasoning steps by their effect on answer confidence and prunes only low-importance verification/error-correction steps from distilled chain-of-thought data, producing models that reason more concisely without losing accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
