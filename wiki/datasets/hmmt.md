# HMMT

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME](aime.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [BFCL v3](bfcl-v3.md), [Claude-Sonnet-4](../models/claude-sonnet-4.md), [DeepSeek-R1](../models/deepseek-r1.md), [GPQA](gpqa.md), [GPQA-Diamond](gpqa-diamond.md), [GPT-5](../models/gpt-5.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [GPT-OSS-20B](../models/gpt-oss-20b.md), [GSM8K](gsm8k.md), [HumanEval](humaneval.md), [LiveCodeBench](livecodebench.md), [MATH500](math500.md), [MathVista](mathvista.md), [MMLU-Pro](mmlu-pro.md), [MMMU](mmmu.md), [o1](../models/o1.md), [o3](../models/o3.md), [o3-mini](../models/o3-mini.md), [o4-mini](../models/o4-mini.md), [Qwen3-0.6B](../models/qwen3-0-6b.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [SWE-bench Verified](swe-bench-verified.md)

## Appears in

- [Thermometer of Thoughts: Enhancing LLM’s Exploration via Attention Temperature Modulation](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-200/summary.md) — Introduces attention-temperature modulation (softening/sharpening the attention softmax at inference, distinct from decoding-temperature sampling) as a difficulty-adaptive exploration control -- higher attention temperature broadens exploration and helps hard problems, lower temperature curbs overthinking and helps easy ones -- and pairs it with a difficulty-induced weighted-voting aggregation scheme (Thermometer of Thoughts), improving Pass@10 by 6.78-14.20% and aggregation accuracy by 9.74% across seven reasoning benchmarks.
- [ARISE: An Adaptive Resolution-Aware Metric for Test-Time Scaling Evaluation in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-289/summary.md) — ARISE fixes a specific flaw in prior slope-based test-time-scaling metrics -- they operate only at the aggregate-accuracy level and paradoxically reward models that waste more tokens for worse results under negative scaling -- by scoring each sample's individual accuracy transitions across scaling iterations with a ratio-based, asymmetric weight that penalizes wasted computation more heavily than it rewards gains, paired with a variance-adaptive sampling protocol; across proprietary and open reasoning models it reveals genuine negative scaling (e.g. GPT-OSS-20B: -0.403 ARISE on AIME, DeepSeek-R1: -0.049 on GPQA-Diamond) that a conventional scaling metric registers as positive because it cannot distinguish wasted computation from productive computation.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
