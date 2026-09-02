# SWE-bench Verified

<!-- auto:begin -->

A curated, human-verified subset of SWE-bench (real GitHub issue-resolution tasks) used to evaluate agentic coding performance under a fixed compute/cost budget. 'The Danger of Overthinking' uses it as its main evaluation set, showing that a lower measured overthinking score correlates with higher issue-resolution rates and lower cost; Consilience's verifier-free rollout-selection metric also evaluates on it.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [AIME](aime.md), [best-of-n selection](../methods/best-of-n-selection.md), [BFCL v3](bfcl-v3.md), [Claude-Sonnet-4](../models/claude-sonnet-4.md), [DeepSeek-R1](../models/deepseek-r1.md), [deepseek-v4-flash](../models/deepseek-v4-flash.md), [deepseek-v4-pro](../models/deepseek-v4-pro.md), [GAIA](gaia.md), [GPQA-Diamond](gpqa-diamond.md), [GPT-5](../models/gpt-5.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [GPT-OSS-20B](../models/gpt-oss-20b.md), [HMMT](hmmt.md), [HMMT 2025](hmmt-2025.md), [LiveCodeBench](livecodebench.md), [LiveCodeBench-v6](livecodebench-v6.md), [MathVista](mathvista.md), [MMLU-Pro](mmlu-pro.md), [MMMU](mmmu.md), [o1](../models/o1.md), [o3](../models/o3.md), [o3-mini](../models/o3-mini.md), [o4-mini](../models/o4-mini.md), [Overthinking](../concepts/overthinking.md), [Pass@1](../concepts/pass-1.md), [pass@K](../concepts/pass-k.md), [Qwen3 family (0.6B-235B-A22B)](../models/qwen3-family-0-6b-235b-a22b.md), [reasoning effort](../concepts/reasoning-effort.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md)

## Appears in

- [CHILL-Harness: Counterfactual Harness Learning for Efficient Reasoning in Long-Horizon Agents](../../archive/papers/2026/arxiv-2607-25825/summary.md) — Treats an agent harness's orchestration decisions as causal interventions on the current workflow, learns which ones would improve it, and executes only those whose estimated advantage clears a margin -- so deliberation is spent where it changes the plan rather than at every step.
- [Consilience for Verifier-Free Test-Time Scaling](../../archive/papers/2026/arxiv-2608-09898/summary.md) — Introduces consilience, a verifier-free test-time-scaling selection metric that picks the sampled reasoning rollout whose confidence starts low (exploratory) and ends high (convergent), fixing a failure mode where naive confidence maximization favors confidently wrong answers on hard problems.
- [ARISE: An Adaptive Resolution-Aware Metric for Test-Time Scaling Evaluation in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-289/summary.md) — ARISE fixes a specific flaw in prior slope-based test-time-scaling metrics -- they operate only at the aggregate-accuracy level and paradoxically reward models that waste more tokens for worse results under negative scaling -- by scoring each sample's individual accuracy transitions across scaling iterations with a ratio-based, asymmetric weight that penalizes wasted computation more heavily than it rewards gains, paired with a variance-adaptive sampling protocol; across proprietary and open reasoning models it reveals genuine negative scaling (e.g. GPT-OSS-20B: -0.403 ARISE on AIME, DeepSeek-R1: -0.049 on GPQA-Diamond) that a conventional scaling metric registers as positive because it cannot distinguish wasted computation from productive computation.
- [The Danger of Overthinking: Examining the Reasoning-Action Dilemma in Agentic Tasks](../../archive/papers/2025/local-9f60265e5ada34cb/summary.md) — Defines and measures 'overthinking' in Large Reasoning Models on real software-engineering agent tasks, showing that favoring internal reasoning over environment interaction correlates with lower SWE-bench issue-resolution rates and can be mitigated at lower cost.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
