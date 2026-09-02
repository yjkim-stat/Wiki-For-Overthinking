# Qwen3 family (0.6B-235B-A22B)

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: model
- **Also called**: Qwen-3 family (0.6B-235B-A22B)
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME](../datasets/aime.md), [ASDiv](../datasets/asdiv.md), [BFCL v3](../datasets/bfcl-v3.md), [Claude-Sonnet-4](claude-sonnet-4.md), [DeepSeek-R1](deepseek-r1.md), [DeepSeek-R1-Distill-Llama-70B](deepseek-r1-distill-llama-70b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-5](gpt-5.md), [gpt-oss-120b](gpt-oss-120b.md), [GPT-OSS-20B](gpt-oss-20b.md), [greedy decoding](../methods/greedy-decoding.md), [GSM8K](../datasets/gsm8k.md), [HMMT](../datasets/hmmt.md), [LiveCodeBench](../datasets/livecodebench.md), [MathVista](../datasets/mathvista.md), [MMLU-Pro](../datasets/mmlu-pro.md), [MMMU](../datasets/mmmu.md), [o1](o1.md), [o3](o3.md), [o3-mini](o3-mini.md), [o4-mini](o4-mini.md), [Overthinking](../concepts/overthinking.md), [Qwen3-235B-A22B](qwen3-235b-a22b.md), [Qwen3-30B-A3B](qwen3-30b-a3b.md), [Qwen3-32B](qwen3-32b.md), [SimpleQA](../datasets/simpleqa.md), [SWE-bench Verified](../datasets/swe-bench-verified.md)

## Appears in

- [Do LLMs Really Need 10+ Thoughts for “Find the Time 1000 Days Later”? Towards Structural Understanding of LLM Overthinking](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-773/summary.md) — TRACE decomposes reasoning traces into sub-thoughts and labeled progression graphs across 14 thinking models and 6 domains, finding thinking helps only within a narrow middle ground (5-20x more compute wasted on simple tasks with no gain, and no benefit at all once model scale exceeds ~4-8B or task difficulty exceeds representational capacity), identifies two overthinking-driving thought-progression patterns (Explorer, Late Landing), and redefines overthinking structurally as continuation past the point where marginal return per sub-thought drops below a threshold.
- [ARISE: An Adaptive Resolution-Aware Metric for Test-Time Scaling Evaluation in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-289/summary.md) — ARISE fixes a specific flaw in prior slope-based test-time-scaling metrics -- they operate only at the aggregate-accuracy level and paradoxically reward models that waste more tokens for worse results under negative scaling -- by scoring each sample's individual accuracy transitions across scaling iterations with a ratio-based, asymmetric weight that penalizes wasted computation more heavily than it rewards gains, paired with a variance-adaptive sampling protocol; across proprietary and open reasoning models it reveals genuine negative scaling (e.g. GPT-OSS-20B: -0.403 ARISE on AIME, DeepSeek-R1: -0.049 on GPQA-Diamond) that a conventional scaling metric registers as positive because it cannot distinguish wasted computation from productive computation.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
