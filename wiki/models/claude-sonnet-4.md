# Claude-Sonnet-4

<!-- auto:begin -->

Claude Sonnet 4 is evaluated as one of the large reasoning models in Rt-LRM, a unified 30-task red-teaming benchmark covering truthfulness, safety and efficiency (including CoT-hijacking and prompt-based attacks), and appears among the models used in ARISE's evaluation of test-time-scaling metrics.

- **Kind**: model
- **Also called**: Claude Sonnet 4
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME](../datasets/aime.md), [BFCL v3](../datasets/bfcl-v3.md), [Claude-3.5-Sonnet](claude-3-5-sonnet.md), [DeepSeek-R1](deepseek-r1.md), [DeepSeek-V3](deepseek-v3.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-5](gpt-5.md), [gpt-oss-120b](gpt-oss-120b.md), [GPT-OSS-20B](gpt-oss-20b.md), [HMMT](../datasets/hmmt.md), [LiveCodeBench](../datasets/livecodebench.md), [MathVista](../datasets/mathvista.md), [MMLU-Pro](../datasets/mmlu-pro.md), [MMMU](../datasets/mmmu.md), [o1](o1.md), [o3](o3.md), [o3-mini](o3-mini.md), [o4-mini](o4-mini.md), [Qwen3 family (0.6B-235B-A22B)](qwen3-family-0-6b-235b-a22b.md), [SWE-bench Verified](../datasets/swe-bench-verified.md)

## Appears in

- [Red Teaming Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1034/summary.md) — Rt-LRM is a unified 30-task benchmark evaluating large reasoning models along truthfulness, safety and efficiency, testing both CoT-hijacking (direct interference with the reasoning process) and prompt-induced impacts (jailbreaks or overthinking triggers); across 26 models it finds LRMs are consistently less trustworthy than their own base LLMs, that explicit reasoning can amplify safety risk and inefficiency under attack, and that over 60% of tested samples exhibit overthinking (more than double the clean-input token count) across most models.
- [ARISE: An Adaptive Resolution-Aware Metric for Test-Time Scaling Evaluation in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-289/summary.md) — ARISE fixes a specific flaw in prior slope-based test-time-scaling metrics -- they operate only at the aggregate-accuracy level and paradoxically reward models that waste more tokens for worse results under negative scaling -- by scoring each sample's individual accuracy transitions across scaling iterations with a ratio-based, asymmetric weight that penalizes wasted computation more heavily than it rewards gains, paired with a variance-adaptive sampling protocol; across proprietary and open reasoning models it reveals genuine negative scaling (e.g. GPT-OSS-20B: -0.403 ARISE on AIME, DeepSeek-R1: -0.049 on GPQA-Diamond) that a conventional scaling metric registers as positive because it cannot distinguish wasted computation from productive computation.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
