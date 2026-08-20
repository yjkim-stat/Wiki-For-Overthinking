# greedy decoding

<!-- auto:begin -->

Taking the highest-probability token at each step, used as the deterministic baseline that sampling-based test-time methods are compared against. One source uses it exactly that way, reporting gains over it. The other removes the assumption the comparison rests on: greedy decoding is not reproducible across hardware, and changing GPU type, GPU count or evaluation batch size shifts a reasoning model's AIME'24 accuracy by up to 9 percentage points on the same model and benchmark. That makes greedy decoding a baseline whose own variance can exceed the effect sizes it is used to establish.

- **Kind**: method
- **Also called**: argmax decoding, greedy decode
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [answer stabilization](../concepts/answer-stabilization.md), [beam search](beam-search.md), [benchmark contamination](../concepts/benchmark-contamination.md), [best-of-n](best-of-n.md), [construct validity](../concepts/construct-validity.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [LoRA](lora.md), [majority voting](majority-voting.md), [MATH500](../datasets/math500.md), [memorization](../concepts/memorization.md), [OlympiadBench](../datasets/olympiadbench.md), [pass@k](../concepts/pass-k.md), [Qwen2.5-1.5B](../models/qwen2-5-1-5b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen3-32B](../models/qwen3-32b.md), [reproducibility](../concepts/reproducibility.md), [self-consistency](self-consistency.md), [self-correction](../concepts/self-correction.md), [test-time compute](../concepts/test-time-compute.md), [test-time scaling](../concepts/test-time-scaling.md), [vLLM](vllm.md)

## Appears in

- [Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning](../../archive/papers/2026/arxiv-2608-05643/summary.md) — Spends test-time compute on iteratively refining each sampled rollout rather than on drawing more of them, then majority-votes the refined answers, with no verifier.
- [Zero Gap Is Not Restoration: Stratified Per-Question Probability Evaluation and Step-wise Mitigation of Benchmark Contamination](../../archive/papers/2026/arxiv-2608-07341/summary.md) — Shows that the standard metric for judging contamination-mitigation strategies can be scored by cancellation rather than by restoration, replaces it with a per-question stratified metric under which the published ranking reverses, and proposes a mitigation that decides its intervention during decoding instead of from a prior estimate.
- [Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference](../../archive/papers/2025/local-de572e138fc98639/summary.md) — Shows that greedy decoding is not deterministic across hardware: changing GPU type, GPU count or evaluation batch size shifts a reasoning model's AIME'24 accuracy by up to 9 percentage points and its response length by 9,000 tokens under BF16, because floating-point addition is non-associative.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
