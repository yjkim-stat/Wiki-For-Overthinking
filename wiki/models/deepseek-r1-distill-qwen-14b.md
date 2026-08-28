# DeepSeek-R1-Distill-Qwen-14B

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [DeepSeek-R1-Distill-Qwen-1.5B](deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-32B](deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH500](../datasets/math500.md)

## Appears in

- [Reasoning Fails Where Step Flow Breaks](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1212/summary.md) — Step-Saliency pools token-level attention-gradient saliency into step-to-step maps across a reasoning trace's question/thinking/summary structure, revealing two depth-wise information-flow failures in incorrect outputs -- Shallow Lock-in (shallow layers over-focus on the current step, ignoring earlier context) and Deep Decay (deep layers lose connection to the thinking segment, with the summary attending mainly to itself) -- and fixes both with StepFlow, a training-free single-pass decoding intervention that improves accuracy by up to 11.8 points across six LRM backbones and six benchmarks.
- [From "Aha Moments" to Controllable Thinking: Toward Meta-Cognitive Reasoning in LRMs via Decoupled Reasoning and Control](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-304/summary.md) — MERA frames overthinking as a deficiency in fine-grained internal control (not a lack of capability) and fixes it by structurally decoupling a reasoning model's output into alternating <reason>/<control> segments -- built via a control-takeover data pipeline and trained with SFT plus a segment-wise, control-masked RL objective (CSPO) -- cutting DeepSeek-R1-Distill-Qwen token usage 30-47% while simultaneously improving accuracy across five math benchmarks and generalizing to non-math MMLU-Pro domains.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
